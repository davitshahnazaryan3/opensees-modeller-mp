from typing import List, Union
import numpy as np
from scipy import optimize, stats
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

from .utilities import mlefit_ida, spline, is_list_of_lists, \
    cdf_lognormal_norm, mlefit_msa
from .plot_styles import FONTSIZE


def plot_fragility(
    x: Union[List, np.ndarray],
    xlabel: str,
    xlim: List = None,
    mean: Union[float, List] = None,
    std: Union[float, List] = None,
    y: Union[List, List[List]] = None,
    labels: List[str] = None,
    linestyles: List[str] = None,
    colors: List[str] = None,
    figsize=(4, 3)
):
    """Fragility plotter

    Parameters
    ----------
    x : Union[List, np.ndarray]
        X axis values, typically Engineering demand parameter, EDP, range or
        Intensity measure level, IML, range
    xlabel : str
        X axis label
    xlim : List, optional
        X axis limits, by default [x[0], x[-1]]
    mean : Union[float, List], optional
        Means of the fragility functions, by default None
    std : Union[float, List], optional
        Standard deviations of the fragility functions, by default None
    y : Union[List, List[List]], optional
        Y axis values, i.e., probability of exceedances, by default None
        If 'mean' and 'std' are not provided, y must be provided
    labels : List[str], optional
        Labels of each fragility function, by default None
    linestyles : List[str], optional
        Linestyles of each fragility function curve, by default '-'
    colors : List[str], optional
        Colors of each fragility function curve, by default 'k'

    Returns
    -------
    fig : `.Figure`
    ax : `~.axes.Axes` or array of Axes

    Raises
    ------
    ValueError
        If 'mean', 'std' and 'y' are nor provided
    ValueError
        If 'y' is not provided, and one of 'mean' and 'std' is not provided
    ValueError
        If 'mean' and 'std' are Lists, but length are not matching
    ValueError
        If any of the provided means, stds, labels, linestyles
        or colors not matching
    """

    x = np.asarray(x)
    # To avoid zero value encountered in log
    x[x == 0] = 10e-8

    if xlim is None:
        xlim = [x[0], x[-1]]

    fig, ax = plt.subplots(figsize=figsize, dpi=100)

    if std is None and mean is None and y is None:
        plt.close()
        raise ValueError("Must provide at least mean and standard deviation,"
                         " or y axis values")
    if y is None:
        if std is None or mean is None:
            plt.close()
            raise ValueError("Standard deviations or means of"
                             " fragility functions are missing")

        if not isinstance(mean, float):
            if len(mean) != len(std):
                plt.close()
                raise ValueError("Length of means and standard"
                                 " deviations must match")
        else:
            mean, std = [mean], [std]

        if labels is None:
            labels = [None] * len(mean)
        if colors is None:
            colors = ['k'] * len(mean)
        if linestyles is None:
            linestyles = ['-'] * len(mean)

        if len(linestyles) != len(colors) != len(labels) != len(mean):
            raise ValueError("Length of linestylies, colors, labels"
                             " and/or means, std not matching")

        for i, (m, s) in enumerate(zip(mean, std)):
            y = stats.norm.cdf(
                np.log(x / m) / s, loc=0, scale=1
            )
            y[np.isnan(y)] = 0

            plt.plot(x, y, label=labels[i], color=colors[i], ls=linestyles[i],
                     clip_on=True)

    else:
        if not is_list_of_lists(y):
            y = [y]
        if labels is None:
            labels = [None] * len(y[0])
        if colors is None:
            colors = [None] * len(y[0])
        if linestyles is None:
            linestyles = ["-"] * len(y[0])

        for i in range(len(labels)):
            plt.plot(x, y[:, i], label=labels[i], color=colors[i],
                     ls=linestyles[i], clip_on=True)

    plt.xlabel(xlabel)
    plt.ylabel("Probability of Exceedance")

    plt.grid(True, which="major", axis="y", ls="--", lw=1.0)
    plt.xlim(xlim)
    plt.ylim([0, 1])

    if None not in labels:
        legend = plt.legend(facecolor='white', edgecolor=None,
                            loc="best", fontsize=FONTSIZE)
        frame = legend.get_frame()
        frame.set_linewidth(0)

    plt.tight_layout()
    plt.show()

    return fig, ax


def retrieve_demand_for_calc(directionality: Union[int, None],
                             level: int, demands_nd, demands):
    if directionality is None:
        dem = demands_nd[:, :, level]
    else:
        dem = demands[int(directionality) - 1][:, :, level]
    return dem


def enforce_non_decreasing(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            arr[i] = arr[i - 1]  # Set it equal to the previous one
    return arr


class Fragility:
    def __init__(self, imls: np.ndarray) -> None:
        """Provides tools to calculate fragility functions

        Parameters
        ----------
        imls : np.ndarray
            Sorted IML ranges from analysis results,
            shape = (number of runs, number of records)
        """
        self.imls = imls

        # IML range for interpolations
        self.iml_range = np.linspace(np.min(self.imls), np.max(self.imls), 50)

    def collapse_capacity(
            self, demand: List[np.ndarray], flat_slope: float = 0.1,
            dcap: float = 10., beta: float = 0.0, fit='msa'):
        """Calculate IML vs POE fragility for the collapse limit state

        Parameters
        ----------
        demand : List[np.ndarray]
            Demands sorted based on self.imls
        flat_slope : float, optional
            Flattening slope, where collapse is assumed, by default 0.1
        dcap : float, optional
            Maximum PSD beyond which collapse is assumed in [%], by default 10.
        beta : float, optional
            Additional uncertainty to account for, typically modelling,
            by default 0.0

        Returns
        -------
        FragilityModel
            {
                'median': float,
                'beta': float,
                'probs': list,
            }
        """
        demand = np.maximum(*demand)

        # number of storeys
        nst = int((demand.shape[2] - 1) / 2)
        # number of realizations
        nsim = demand.shape[1]

        # Slice for PSDs only for collapse fragility computation
        demand = demand[:, :, nst + 1:]

        # Get the maximum PSDs for the building and shrink one axis of NLTHA
        demand = np.max(demand, axis=2)

        if fit=='ida':
            # Initialize
            psd_max = np.max(demand) if np.max(demand) < 10. else 10.
            iml_max = np.max(self.imls)

            psd_max_mod = min(psd_max, dcap)
            iml_max_mod = iml_max
            exceeds = np.zeros(nsim)

            for rec in range(nsim):
                order = self.imls[:, rec].argsort()
                iml_range = self.imls[:, rec][order]
                iml_range = np.append(iml_range, iml_range[-1])

                # Get the PSD range for each simulation/record
                psd = demand[:, rec][order]

                # flatline
                psd = np.append(psd, psd_max_mod)

                # Create a spline of psd vs iml
                psd_spline, iml_spline = spline(psd, iml_range)
                slope_init = iml_range[1] / psd[1]

                slopes = np.diff(iml_spline) / np.diff(psd_spline)

                try:
                    flat_idx = np.where(
                        slopes == slopes[(slopes < flat_slope * slope_init)
                                        & (slopes > 0)
                                        & (slopes != np.inf)][0])[0][0]
                except IndexError:
                    flat_idx = len(iml_spline) - 1
                    print(f"[WARNING] IDA for record {rec} not flatlining")

                flat_iml = iml_spline[flat_idx - 1]
                flat_psd = psd_spline[flat_idx - 1]
                flat_psd_lim = dcap
                if flat_psd > flat_psd_lim:
                    flat_psd = flat_psd_lim
                    flat_iml = float(iml_spline[np.where(
                        psd_spline == psd_spline[
                            psd_spline > flat_psd_lim][0])[0]])

                exceeds[rec] = flat_iml

            iml_min = min(exceeds)
            iml_max = max(exceeds)

            # Fragility calculations with maximum likelihood (MLE) fitting
            iml_all = np.linspace(0, iml_max_mod, 100)
            counts = np.zeros(iml_all.shape)

            counts = np.sum(exceeds[:, np.newaxis] < iml_all, axis=0)
            counts[iml_all < iml_min] = 0
            counts[iml_all > iml_max] = len(exceeds)

            # number of records
            n_rec = len(exceeds)

            xs = iml_all
            ys = counts
            if xs[0] == 0:
                xs, ys = xs[1:], ys[1:]
            theta_hat_mom = np.exp(np.mean(np.log(xs)))
            beta_hat_mom = np.std(np.log(xs))
            x0 = [theta_hat_mom, beta_hat_mom]

            xopt_mle = optimize.fmin(
                func=lambda var: mlefit_ida(median=var[0], dispersion=var[1],
                                        total_count=n_rec,
                                        count=np.array(ys[1:]), data=xs[1:]),
                x0=x0, maxiter=3000, maxfun=3000, disp=False)

            ecdf = (xs[1:], ys[1:] / n_rec)
            
        elif fit=='msa':
            num_gms = demand.shape[1]
            num_collapse = np.sum(demand >= dcap, axis=1)
            enforce_non_decreasing(num_collapse)  # TODO: I am not sure about this
            msa_imls = self.imls[:, 0]
            ecdf = (msa_imls, num_collapse / num_gms)
            xopt_mle = mlefit_msa(msa_imls, num_gms, num_collapse)
        
        theta_mle = xopt_mle[0]
        beta_mle = (xopt_mle[1] ** 2 + beta ** 2) ** 0.5

        probs = stats.norm.cdf(
            np.log(self.iml_range / theta_mle) / beta_mle, loc=0, scale=1
        )

        return {'median': theta_mle, 'beta': beta_mle, 'probs': list(probs), 'ecdf': ecdf}

    def demolition_capacity(self, residuals: np.ndarray, median: float,
                            beta: float):
        """Calculate IML vs POE fragility for the demolition limit state

        Parameters
        ----------
        residuals : np.ndarray
            Residual drifts sorted based on self.imls
            (number of stripes, number of ground motion records)
            ordered by sorted IML
        median : float
            Median EDP in %
        beta : float
            EDP dispersion

        Returns
        ----------
        dict
            {
                'median': float,
                'beta': float,
                'probs': list,
            }
        """
        # Get the maximum IML recorded from analysis results
        iml_max = np.max(self.imls)

        # Number of ground motion records
        num_recs = residuals.shape[1]

        # Demolition probabilities initialization
        p_demol_final = np.zeros(self.iml_range.shape)

        for i, iml in enumerate(self.iml_range):
            exceeds = np.array([])

            for rec in range(num_recs):
                iml_record = self.imls[:, rec]
                edp = residuals[:, rec]
                spline = interp1d(iml_record, edp)

                if iml <= max(iml_record):
                    exceeds = np.append(exceeds, float(spline(iml)))

            edp_min = min(exceeds)
            edp_max = max(exceeds)

            edp_range = np.linspace(0., edp_max * 1.5, 200)[1:]
            counts = sum(np.array(exceeds)[:, np.newaxis] < edp_range)
            counts[edp_range < edp_min] = 0.
            counts[edp_range > edp_max] = len(exceeds)

            # Start the fitting
            if edp_range[0] == 0:
                edp_range, counts = edp_range[1:], counts[1:]

            theta_hat_mom = np.exp(np.mean(np.log(edp_range)))
            beta_hat_mom = np.std(np.log(edp_range))
            x0 = [theta_hat_mom, beta_hat_mom]

            xopt_mle = optimize.fmin(
                func=lambda var: mlefit_ida(median=var[0], dispersion=var[1],
                                        total_count=num_recs,
                                        count=counts, data=edp_range),
                x0=x0, maxiter=100, maxfun=100, disp=False)

            theta_mle = xopt_mle[0]
            beta_mle = xopt_mle[1]

            p_demol_iml = stats.norm.cdf(
                np.log(theta_mle / median)
                / (beta_mle ** 2 + beta ** 2) ** 0.5,
                loc=0, scale=1)
            p_demol_final[i] = p_demol_iml

        # Final fitting
        xs = self.iml_range[self.iml_range <= iml_max]
        ys = np.round(p_demol_final * num_recs, 0)

        theta_hat_mom = np.exp(np.mean(np.log(xs)))
        beta_hat_mom = np.std(np.log(xs))
        x0 = [theta_hat_mom, beta_hat_mom]
        xopt_mle = optimize.fmin(
            func=lambda var: mlefit_ida(median=var[0], dispersion=var[1],
                                    total_count=num_recs,
                                    count=ys, data=xs),
            x0=x0, maxiter=100, maxfun=100, disp=False)
        theta_mle = xopt_mle[0]
        beta_mle = xopt_mle[1]

        probs = stats.norm.cdf(
            np.log(self.iml_range / theta_mle) / beta_mle, loc=0, scale=1
        )

        return {'median': theta_mle, 'beta': beta_mle, 'probs': list(probs)}

    def edp_given_im(
            self, demand: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """Calculate EDP vs POE fragility for a given IML, in terms of PDF.
        Records causing collapse are ignored.
        When the number of non-collapsing records is less than 3,
        the distribution at the previous IML is assumed

        Parameters
        ----------
        demand : np.ndarray
            Demands sorted based on self.imls for a particular EDP
            (number of runs, number of simulations)

        Parameters
        ----------
        tuple[np.ndarray, np.ndarray]
            (medians, dispersions)
        """
        # To store the counts of exceedances
        # (number of simulations, number of IML points)
        exceeds = np.zeros((self.imls.shape[1], len(self.iml_range)))
        for rec in range(demand.shape[1]):
            _demand = demand[:, rec][~np.isnan(demand[:, rec])]
            _imls = self.imls[:, rec][~np.isnan(demand[:, rec])]

            imls = np.insert(_imls, 0, 0)
            demand_range = np.insert(_demand, 0, 0)

            spline = interp1d(imls, demand_range, fill_value=max(
                demand_range), axis=0, bounds_error=False)

            exceeds[rec, :] = spline(self.iml_range)

        max_edps = np.max(exceeds, axis=0)

        # Demand range used for fitting, (number of simulations, 100)
        medians = np.zeros(max_edps.shape)
        betas = np.zeros(max_edps.shape)

        for i, val in enumerate(max_edps):
            fit_demand_range = np.linspace(0, val * 1.5, 101)[1:]
            counts = sum(map(lambda x: x < fit_demand_range,
                         exceeds[:, i])) / demand.shape[1]

            coef_opt, _ = optimize.curve_fit(
                cdf_lognormal_norm,
                fit_demand_range[1:],
                counts[1:],
                maxfev=10**6)

            medians[i], betas[i] = coef_opt
            # medians[i] = np.exp(medians[i])

        return medians, betas
