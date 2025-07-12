import os
from pathlib import Path
from typing import List
import numpy as np

from .hazard import Hazard, analytical_mafe
from .utilities import read_pickle


class MSAPostprocessor:
    def __init__(self, msa: Path) -> None:
        """MSA postprocessor

        Parameters
        ----------
        msa : Path
            Directory containing MSA outputs
            It must not include any subdirectories other than pertinent to
            MSA outputs
        """
        self.msa = msa

    def _get_ground_motion_batches(self):
        return next(os.walk(self.msa))[1]

    def _get_rp_im(self, level, idx, rps, imls, coefs, hazard):
        im, rp = None, None

        if rps is not None:
            rp = rps[idx]
        if imls is not None and not isinstance(imls, dict):
            im = imls[idx]
        if coefs is None and hazard is not None:
            coefs = hazard['coef']
        if coefs is not None:
            coefs2 = coefs[2]

        if im is None:
            im = Hazard.get_im(1 / rp, coefs[0], coefs[1], coefs2)

        if rps is None:
            # infer from level
            try:
                mafe = float(level.split("-")[1])
                rp = int(1 / mafe)
            except Exception:
                rp = int(level)

                if isinstance(imls, dict):
                    im = imls[str(rp)]

            finally:
                # compute from hazard
                if rp is None:
                    mafe = analytical_mafe(im, coefs[0], coefs[1], coefs2)
                    rp = int(1 / mafe)

        return rp, im

    @staticmethod
    def get_edp(out, direction, storey, edptype, rps, factor=1.0):
        edp = []
        # For each return period
        for rp in rps:
            rp = str(rp)
            if edptype == "drift":
                edp.append(out[rp][str(direction+1)][edptype][str(storey)])
            else:
                # acc
                critical = np.array(max(
                    out[rp][str(1)][edptype][str(storey)],
                    out[rp][str(2)][edptype][str(storey)])) \
                    * factor
                edp.append(list(critical))

        return edp

    def postprocess(
            self, nst: int, imls: List[float] = None,
            return_periods: List[float] = None, coefs: List[float] = None,
            hazard=None) -> dict:
        """Postprocess MSA outputs

        Parameters
        ----------
        nst : int
            Number of storeys
        imls : List[float], optional
            Intensity measure levels obtained from probabilistic seismic
            hazard analysis (PSHA) and used to perform MSA, typically
            under filename 'imls_{IM type}.out' from PSHA, by default None
        return_periods : List[float], optional
            Return periods, by default None
            If None, will infer from ground motion directory naming convention
        coefs : List[float], optional
            SAC/FEMA-compatible hazard fitting coefficients, by default None
        fitted_hazard : HazardModelSchema, optional
            Fitted hazard function using Hazard module

        Raises
        -------
        ValueError
            Must provide either of: return_periods, imls if both are None
        ValueError
            Must provide either of: hazard, imls if any of return_periods or
            imls is None

        Returns
        -------
        dict
            Processed MSA outputs
            'global' stands for peak building response
            {
                'Level description': {
                    '1': {      Direction X
                        'PFA': {floor level: [], "global": []},
                        'disp': {floor level: [], "global": []},
                        'PSD': {storey level: [], "global": []}
                        'RPSD': {storey level: [], "global": []}
                    },
                    '2': {      Direction Y

                    }
                    'return-period': int,
                    'intensity-measure': float,
                }
            }
        """
        if return_periods is None and imls is None:
            raise ValueError("Must provide either of: return_periods, imls")

        if (imls is None or return_periods is None) and hazard is None and \
                imls is None:
            raise ValueError("Must provide either of: hazard, imls")

        # 3D building, process for 2 directions
        n_dir = 2

        # gm_levels = self._get_ground_motion_batches()

        # outputs
        out = {}

        # For each level of excitation
        for i in range(len(return_periods)):
            level = str(return_periods[i])

            rp, im = self._get_rp_im(
                level, i, return_periods, imls, coefs, hazard)

            out[level] = {
                "1": {"PFA": {}, "disp": {}, "PSD": {}, "RPSD": {}},
                "2": {"PFA": {}, "disp": {}, "PSD": {}, "RPSD": {}},
                "SRSS": {"PFA": {}, "disp": {}, "PSD": {}, "RPSD": {}},
                "return-period": rp,
                'intensity-measure': im,
            }

            print(f"[LEVEL] {level}, Return period {rp} years")

            # For each direction
            for d in range(n_dir):
                for st in range(nst + 1):
                    out[level][str(d + 1)]["PFA"][st] = []
                    out[level][str(d + 1)]["disp"][st] = []
                    out[level]['SRSS']["PFA"][st] = []
                    out[level]['SRSS']["disp"][st] = []
                    if st != nst:
                        out[level][str(d + 1)]["PSD"][st + 1] = []
                        out[level][str(d + 1)]["RPSD"][st + 1] = []
                        out[level]['SRSS']["PSD"][st + 1] = []
                        out[level]['SRSS']["RPSD"][st + 1] = []

                out[level][str(d + 1)]["PFA"]["global"] = []
                out[level][str(d + 1)]["disp"]["global"] = []
                out[level][str(d + 1)]["PSD"]["global"] = []
                out[level][str(d + 1)]["RPSD"]["global"] = []

            out[level]['SRSS']["PFA"]["global"] = []
            out[level]['SRSS']["disp"]["global"] = []
            out[level]['SRSS']["PSD"]["global"] = []
            out[level]['SRSS']["RPSD"]["global"] = []

            # for each record level
            for record in next(os.walk(self.msa / level))[-1]:
                """
                0 - accelerations [g], 1 - displacements [m], 2 - drifts
                each has a shape of d x s x r, where
                    d stands for number of directions
                    s stands for number of storeys and floors
                    r stands for number of steps of the record
                """
                data = read_pickle(self.msa / level / record)

                # SRSS
                pfa = (data[0][0]**2 + data[0][1]**2)**0.5
                disp = (data[1][0]**2 + data[1][1]**2)**0.5
                psd = (data[2][0]**2 + data[2][1]**2)**0.5

                res_drift_global = 0
                for st in range(nst + 1):
                    out[level]['SRSS']["PFA"][st].append(np.amax(pfa[st]))
                    out[level]['SRSS']["disp"][st].append(np.amax(disp[st]))
                    if st != nst:
                        out[level]['SRSS']["PSD"][st + 1].append(np.amax(psd[st]))

                        res_drift_val = (
                            self._compute_residual_drift(abs(data[3][0][st]), abs(data[2][0][st]))**2 +
                            self._compute_residual_drift(abs(data[3][1][st]), abs(data[2][1][st]))**2
                        )**0.5
                        if res_drift_val > res_drift_global:
                            res_drift_global = res_drift_val

                        out[level]['SRSS']["RPSD"][st + 1].append(res_drift_val)

                out[level]['SRSS']["PFA"]["global"].append(np.amax(pfa))
                out[level]['SRSS']["disp"]["global"].append(np.amax(disp))
                out[level]['SRSS']["PSD"]["global"].append(np.amax(psd))
                out[level]['SRSS']["RPSD"]["global"].append(res_drift_global)

                for d in range(n_dir):
                    res_drift_global = 0

                    for st in range(nst + 1):
                        out[level][str(d + 1)][
                            "PFA"][st].append(np.amax(abs(data[0][d][st])))
                        out[level][str(d + 1)][
                            "disp"][st].append(np.amax(abs(data[1][d][st])))
                        if st != nst:
                            out[level][str(d + 1)]["PSD"][
                                st + 1].append(np.amax(abs(data[2][d][st])))

                            res_drift_val = self._compute_residual_drift(
                                abs(data[3][d][st]),
                                abs(data[2][d][st])
                            )
                            if res_drift_val > res_drift_global:
                                res_drift_global = res_drift_val

                            out[level][str(
                                d + 1)]["RPSD"][st + 1].append(res_drift_val)

                    out[level][str(d + 1)][
                        "PFA"]["global"].append(np.amax(abs(data[0][d])))
                    out[level][str(d + 1)][
                        "disp"]["global"].append(np.amax(abs(data[1][d])))
                    out[level][str(d + 1)][
                        "PSD"]["global"].append(np.amax(abs(data[2][d])))
                    out[level][str(d + 1)
                               ]["RPSD"]["global"].append(res_drift_global)

        return out

    def _compute_residual_drift(self, res, drift):

        if len(res) > 1:
            val = float(sum(res[1:]) / len(res[1:]))
        else:
            val = float(drift[-1])

        return val
