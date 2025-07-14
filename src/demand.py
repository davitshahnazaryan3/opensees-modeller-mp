from typing import List, Union
import numpy as np
from scipy.stats.distributions import norm
from pyDOE import lhs
from .demolition import Demolition


def convert_demands(demands):
    first_key = next(iter(demands))

    if "IM" in demands[first_key]["1"].keys():
        # those are IDA outputs
        return demands

    # those are MSA outputs
    out = {}

    # number of records
    nrecs = len(demands[first_key]["1"]["PFA"]["0"])
    nst = len(demands[first_key]["1"]["PFA"]) - 2

    imls: List[float] = []
    rps: List[str] = []
    for rp in demands.keys():
        # get IML range
        imls.append(demands[rp]["intensity-measure"])
        # return periods
        rps.append(rp)

    for rec in range(1, nrecs + 1):
        out[str(rec)] = {}
        for d in ["1", "2", "SRSS"]:
            if d not in demands[first_key]:
                continue

            out[str(rec)][d] = {
                "IM": imls,
                "PSD": {"global": np.zeros(len(imls))},
                "PFA": {"global": np.zeros(len(imls))},
                "RPSD": {"global": np.zeros(len(imls))},
            }

            for st in range(nst + 1):
                if st != 0:
                    out[str(rec)][d]["PSD"][str(st)] = np.zeros(len(imls))
                    out[str(rec)][d]["RPSD"][str(st)] = np.zeros(len(imls))
                out[str(rec)][d]["PFA"][str(st)] = np.zeros(len(imls))

    for rp_i, rp in enumerate(rps):
        for d in demands[rp].keys():
            if d == "return-period" or d == "intensity-measure":
                continue

            for edp in demands[rp][d].keys():
                if edp == "disp":
                    continue

                for st in demands[rp][d][edp].keys():
                    for rec in range(1, nrecs + 1):
                        out[str(rec)][d][edp][st][rp_i] = \
                            demands[rp][d][edp][st][rec - 1]

    # out = convert_ndarray_to_list(out)

    return out


def convert_list_to_ndarray(demands):

    if isinstance(demands, dict):
        for key, value in demands.items():
            demands[key] = convert_list_to_ndarray(value)
    elif isinstance(demands, list):
        return np.array(demands)

    return demands


def process_demands(non_directional_factor,
                    modelling_uncertainty, perform_simulations,
                    realizations):

    if self.demolition is not None:
        demo = Demolition(self.demands)
        self.residuals = demo.get_residuals()

    demand_object = Demand(self.demands, non_directional_factor,
                           modelling_uncertainty, perform_simulations,
                           realizations)
    self.imls = demand_object.imls
    self.demands = demand_object.demand
    self.demands_nd = demand_object.get_non_directional_demands()


class Demand:
    def __init__(
        self,
        demand: dict,
        non_directional_factor: float = 1.0,
        modelling_uncertainty: Union[float, List[float]] = None,
        perform_simulations: bool = False,
        realizations: int = 100,
    ):
        """Initialize demand processor for Nonlinear Time History Analysis
        (NLTHA) results

        Structure of IDA results (.pickle) obtained from ida_postprocessor of
        RCMRF

        dict: postprocessed IDA results
            {
                "record_number" {
                    "Direction": {         # "1" and "2"
                        "IM": List[float],
                        "PSD": {
                            # peak values for each storey level
                            "storey level": List[float],
                            # peak values for the building
                            "global": List[float],
                        },
                        "PFA": {
                            "floor level": List[float],
                            "global": List[float],
                        },
                        "RPSD": {
                            "storey level": List[float],
                            "global": List[float],
                        }
                    },
                }
            }

        Notes on the input demand:
            Keys: IM, PSD, PFA, RPSD in 'IDA':
                - Length of each list is number of stripes for MSA or
                number of runs for IDA
                - The peak values for the entire building in the direction
                of interest are recorded
            Floor level starts from 0 to number of storeys
            Storey level starts from 1 to number of storeys

        Parameters
        ----------
        demand : dict
            Demands following NLTHA
        non_directional_factor : float, Optional
            Non-directional conversion factor for components sensitive to both
            directions of response, by default 1.0.
        modelling_uncertainty : Union[float, List[float]], optional
            Modelling uncertainties (epistemic variabilities), by default None
        perform_simulations : bool, optional
            Whether to perform simulations using Latin Hypercube sampling,
            by default False
        realizations : int, optional
            Number of realizations, by default 100
        """
        self.demand = demand
        self.non_directional_factor = non_directional_factor
        self.modelling_uncertainty = modelling_uncertainty
        self.realizations = realizations

        # Intensity measure range for each ground motion record
        self.imls, self.iml_idxs = self._get_iml_range()

        # Transform demands into numpy ndarray
        self.demand = self._transform_demands()
        if perform_simulations:
            # Perform latin hypercube sampling
            self.demand = self._simulate_demands()

    def _get_iml_range(self) -> np.ndarray:
        """Sorts the IML and returns them

        Returns
        -------
        np.ndarray
            IML range, shape = (number of runs, number of records)
        """
        nrecs = len(self.demand)

        key_0 = next(iter(self.demand))
        key_1 = next(iter(self.demand[key_0]))

        iml = np.zeros((
            len(self.demand[key_0][key_1]['IM']),
            nrecs
        ))

        iml_idxs = np.zeros((
            len(self.demand[key_0][key_1]['IM']),
            nrecs
        ), dtype='i')

        # "IDA" is not sorted, while "summary_results" are sorted, and since
        # EDPs will be read from "summary_results", the IM values must be
        # sorted here
        for i, rec in enumerate(self.demand.keys()):
            iml[:, i] = np.sort(self.demand[rec][key_1]['IM'])
            iml_idxs[:, i] = np.argsort(self.demand[rec][key_1]['IM'])

        return iml, iml_idxs

    def _transform_demands(self) -> List[np.ndarray]:
        """Transforms demands into np.ndarray

        Returns
        -------
        List[np.ndarray]
            Transformed NLTHA outputs
                [
                    np.ndarray: (
                        Number of IML,
                        Number of ground motions,
                        Number of variables, # first PFA, then PSD
                    ), # direction 0
                    np.ndarray: (), # direction 1
                ]
        """
        # Number of ground motion record(s) (pairs)
        ngm = len(self.demand)

        # Number of intensity measure levels
        rec_key = next(iter(self.demand))
        niml = len(self.demand[rec_key]['1']['IM'])

        # Number of variables, excluding residuals, -2 for
        # global building response
        nvar = len(self.demand[rec_key]['1']['PFA']) + \
            len(self.demand[rec_key]['1']['PSD']) - 2
        nst = len(self.demand[rec_key]['1']['PSD']) - 1

        if self.modelling_uncertainty is None:
            # If not provided, set all uncertainties to zero
            self.modelling_uncertainty = np.zeros((niml, 1))

        # For each direction
        # Initialize NLTHA outputs ndarray variable
        # (direction, iml, ground motion, variable)
        nltha = [
            np.zeros((niml, ngm, nvar)),
            np.zeros((niml, ngm, nvar)),
            np.zeros((niml, ngm, nvar)),
        ]

        for gm_i, gm in enumerate(self.demand.keys()):
            for d, direction in enumerate(self.demand[gm].keys()):
                for st in range(nst + 1):
                    entry = np.array(
                        self.demand[gm][direction]["PFA"][str(st)])
                    nltha[d][:, gm_i, st] = entry[self.iml_idxs[:, gm_i]]

                    if st != 0:
                        entry = np.array(
                            self.demand[gm][direction]["PSD"][str(st)])
                        nltha[d][:, gm_i, nst
                                 + st] = entry[self.iml_idxs[:, gm_i]]

        # Replace nans with means of records at each IML
        for i, arr in enumerate(nltha):
            means_nrha = np.nanmean(arr, axis=1)
            nltha[i] = np.moveaxis(nltha[i], 1, 0)
            nltha[i] = np.where(np.isnan(nltha[i]), means_nrha, nltha[i])
            nltha[i] = np.moveaxis(nltha[i], 0, 1)

        return nltha

    def _simulate_demands(self) -> List[np.ndarray]:
        """Simulate the demands

        Returns
        -------
        List[np.ndarray]
            Simulated demands
            [
                np.ndarray: (
                    Number of IML,
                    Number of realizations,
                    Number of variables, # first PFA, then PSD
                ), # direction 0
                np.ndarray: (), # direction 1
            ]
        """
        # If number of realizations is less than the number of ground motions,
        # skip
        if self.realizations <= self.demand[0].shape(1):
            return self.demand

        nltha = []
        for i, arr in enumerate(self.demand):
            nltha.append(
                np.zeros((arr.shape[0], self.realizations, arr.shape[1])),
            )

            for j in range(arr.shape[0]):
                nltha[i][j, :, :] = self._latin_hypercube_sampling(
                    arr[j, :, :],
                    self.modelling_uncertainty[j]
                )

        return nltha

    def _latin_hypercube_sampling(
            self, demands: np.ndarray, beta: float) -> np.ndarray:
        """Latin Hypercube sampling to calculate the distribution of probable
        losses for each ground motion intensity or earthquake scenario.
        The original demands of shape (ngm, nvar) will be transformed to
        simulated shape (nr, nvar), where nr stands for number of realizations.

        Parameters
        ----------
        demands : np.ndarray
            Demands associated with the intensity measure of interest
        beta : float
            Modelling uncertainty associated with the intensity measure of
            interest

        Returns
        -------
        np.ndarray
            Simulated demands
        """
        nvar = demands.shape[1]

        # Reshape uncertainties to match
        betas = np.array([beta] * nvar).reshape(nvar, 1)

        # Take natural logarithm of the EDPs
        ln_edps = np.log(demands)

        # Find the mean matrix of lnEDPs
        ln_edps_mean = np.mean(ln_edps, axis=0).reshape(ln_edps.shape[1], 1)

        # Find covariance matrix of lnEDPs
        ln_edps_cov = np.cov(ln_edps, rowvar=False)

        # Find the rank of covariance matrix of lnEDPs
        ln_edps_cov_rank = np.linalg.matrix_rank(ln_edps_cov)

        # Inflate the variances with epistemic variability
        sigma = np.array([np.sqrt(np.diag(ln_edps_cov))]).transpose()
        sigmap2 = np.power(sigma, 2)

        sigma_t = sigma.transpose()
        r = ln_edps_cov / (sigma * sigma_t)

        # Inflate variance for modelling uncertainty
        sigmap2 = sigmap2 + (betas * betas)
        sigma = np.sqrt(sigmap2)
        sigma2 = sigma * sigma.transpose()
        ln_edps_cov_inflated = r * sigma2

        # Find the eigenvalues, eigenvectors of the covariance matrix
        eigen_values, eigen_vectors = np.linalg.eigh(ln_edps_cov_inflated)

        # Partition L_total to L_use. L_use is the part of eigenvector matrix
        # L_total that corresponds to positive eigenvalues
        # Similarly for D_use

        if ln_edps_cov_rank >= nvar:
            l_use = eigen_vectors
            d2_use = eigen_values
        else:
            l_use = eigen_vectors[:, nvar - ln_edps_cov_rank:]
            d2_use = eigen_values[nvar - ln_edps_cov_rank:]

        # Find the square roof of D2_use
        d_use = np.diag(np.power(d2_use, 0.5))

        # Generate Standard random numbers
        if ln_edps_cov_rank >= nvar:
            u = lhs(nvar, self.realizations)
        else:
            u = lhs(ln_edps_cov_rank, self.realizations)
        u = norm(loc=0, scale=1).ppf(u)

        u = u.transpose()

        # Create Lambda=D_use
        lam = np.matmul(l_use, d_use)

        # Create realizations matrix
        z = np.matmul(lam, u) + np.matmul(ln_edps_mean,
                                          np.ones([1, self.realizations]))

        ln_edps_sim_mean = np.mean(z, axis=1).reshape(nvar, 1)
        # ln_edps_sim_cov = np.cov(z)

        # Values of A should be close to 1, as the means of simulated demands
        # should be the same as the means of
        # original demands (currently imposing 5% tolerance)
        a = ln_edps_sim_mean / ln_edps_mean
        test = abs(a - 1) * 100
        if any(test[test >= 5.0]):
            print(
                "[WARNING] Means of simulated demands are not equal to the "
                "means of original demands!")

        # b = ln_edps_sim_cov / ln_edps_cov
        w = np.exp(z).transpose()

        return w

    def get_non_directional_demands(self) -> List[np.ndarray]:
        """Transforms NLTHA demands by a non-dimensional factor using the
        maximum of both directions

        Returns
        -------
        List[np.ndarray]
            Transformed NLTHA demands
        """
        return np.maximum(*self.demand) * self.non_directional_factor
