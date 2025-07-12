from typing import List, Union, Tuple
from pathlib import Path
import openseespy.opensees as op
import numpy as np
import warnings

from .utilities import create_path, read_text, \
    remove_directory_contents


def apply_time_series(
    dt: float,
    pathx: Path,
    pathy: Path,
    fx: float,
    fy: float,
    omegas: List[float],
    damping: float,
    tstagx: int = 51,
    tstagy: int = 52,
    ptagx: int = 10,
    ptagy: int = 20
) -> None:
    """Applies time series

    Parameters
    ----------
    dt : float
        Analysis time step in [s]
    pathx : Path
        Path to ground motion record in X direction
    pathy : Path
        Path to ground motion record in Y direction
    fx : float
        Acceleration scaling factor for ground motion record in X direction
    fy : float
        Acceleration scaling factor for ground motion record in Y direction
    omegas : List[float]
        Circular frequencies, length must be larger than 2
    damping : List[float]
        Damping ratio, length must be larger than 2
    tstagx : int, optional
        Unique tag for time series in X direction, by default 51
    tstagy : int, optional
        Unique tag for time series in Y direction, by default 52
    ptagx : int, optional
        Uniform excitation load pattern tag for X direction, by default 10
    ptagy : int, optional
        Uniform excitation load pattern tag for Y direction, by default 20
    """
    # Delete the old analysis and all of its component objects
    op.wipeAnalysis()

    omegas = np.array(omegas)

    w1 = omegas[0]
    w2 = omegas[2]
    a0 = 2 * w1 * w2 / (w2 ** 2 - w1 ** 2) * \
        (w2 * damping - w1 * damping)
    a1 = 2 * w1 * w2 / (w2 ** 2 - w1 ** 2) * \
        (-damping / w2 + damping / w1)

    # Rayleigh damping
    op.rayleigh(a0, 0.0, 0.0, a1)

    # Time series excitation
    # op.timeSeries('Path', tstagx, '-dt', dt,
    #               '-filePath', str(pathx), '-factor', fx)
    accx = list(np.loadtxt(pathx)[:, 1])
    op.timeSeries('Path', tstagx, '-dt', dt, '-values', *accx, '-factor', fx)

    op.pattern('UniformExcitation', ptagx, 1, '-accel', tstagx)

    if pathy is not None:
        # op.timeSeries('Path', tstagy, '-dt', dt,
        #               '-filePath', str(pathy), '-factor', fy)
        accy = list(np.loadtxt(pathy)[:, 1])
        op.timeSeries('Path', tstagy, '-dt', dt, '-values', *accy,
                      '-factor', fy)
        op.pattern('UniformExcitation', ptagy, 2, '-accel', tstagy)

    # Constraints
    op.constraints('Penalty', 1.0e15, 1.0e15)
    # op.constraints("Transformation")

    op.numberer('RCM')
    op.system('UmfPack')


class SolutionAlgorithm:
    g = 9.81
    ITERATIONS = 50
    ALGORITHM_TYPE = 'KrylovNewton'
    TEST_TYPE = 'NormDispIncr'
    TOL = 1e-04
    collapse_index = 0

    def __init__(
        self,
        output_path: Path,
        dt: float,
        dur: float,
        dc: float,
        bnode: Union[np.array, List[int]],
        tnode: Union[np.array, List[int]],
        pflag: bool = True,
        extra_dur: float = 10.,
        directions: int = 2,
    ) -> None:
        """Algorithms to execute nonlinear time history analysis (NLTHA)

        Parameters
        ----------
        output_path : Path
            Base output path for outputting the results, e.g., Path(directory)
            without suffix
        dt : float
            Initial analysis time step, [s]
            NOT ground motion time step
        dur : float
            Length of ground motion record, [s]
        dc : float
            Drift capacity for both storey and rooft drif, [%]
        bnode : Union[np.array, List[int]]
            List of bottom nodes
        tnode : Union[np.array, List[int]]
            List of top nodes
        pflag : bool, optional
            Print statements, by default True
        extra_dur : float, optional
            Extra duration for free vibrations in [s], by default 10.
        """
        self.output_path = output_path
        if self.output_path is not None:
            self.output_path = self.output_path
        self.dt = dt
        self.dur = dur
        self.extra_dur = extra_dur
        self.dc = dc
        self.bnode = np.array(bnode)
        self.tnode = np.array(tnode)
        self.directions = directions

        # TODO, remove pflag and do logging instead
        self.pflag = pflag

        self._set_analysis()

    def _set_analysis(self):
        """Set up initial analysis parameters
        """
        op.test(self.TEST_TYPE, self.TOL, self.ITERATIONS)
        op.algorithm(self.ALGORITHM_TYPE)
        op.integrator('Newmark', 0.5, 0.25)
        op.analysis('Transient')

    def _algorithm(self, ok: int, control_time: float) -> None:
        """Algorithms necessary to perform the analysis

        Parameters
        ----------
        ok : int
            Analysis performed successfully or not, 0 stands for ok,
            != stands for not ok
        control_time : float
            Control time in seconds
        """
        dtt = self.dt
        if ok:
            if self.pflag:
                print(f"[FAILURE] Failed at {control_time} of {self.dur}"
                      " seconds")
        if ok:
            if self.pflag:
                print(f"[FAILURE] Failed at {control_time} - "
                      "Reduced timestep by half...")
            dtt = 0.5 * self.dt
            ok = op.analyze(1, dtt)
        if ok:
            if self.pflag:
                print(f"[FAILURE] Failed at {control_time} - "
                      "Reduced timestep by quarter...")
            dtt = 0.25 * self.dt
            ok = op.analyze(1, dtt)
        if ok:
            if self.pflag:
                print(
                    f"[FAILURE] Failed at {control_time} - Trying Broyden...")
            op.algorithm('Broyden', 8)
            dtt = self.dt
            ok = op.analyze(1, dtt)
            op.algorithm(self.ALGORITHM_TYPE)
        if ok:
            if self.pflag:
                print(f"[FAILURE] Failed at {control_time} - "
                      "Trying Newton with initial tangent...")
            op.algorithm('Newton', '-initial')
            dtt = self.dt
            ok = op.analyze(1, dtt)
            op.algorithm(self.ALGORITHM_TYPE)
        if ok:
            if self.pflag:
                print(f"[FAILURE] Failed at {control_time} - "
                      "Trying NewtonWithLineSearch...")
            op.algorithm('NewtonLineSearch', 0.8)
            dtt = self.dt
            ok = op.analyze(1, self.dt)
            op.algorithm(self.ALGORITHM_TYPE)
        if ok:
            if self.pflag:
                print(f"[FAILURE] Failed at {control_time} - "
                      "Trying Newton with initial tangent & relaxed "
                      f"convergence...")
            op.test('NormDispIncr', self.TOL * 0.1, self.ITERATIONS * 50)
            op.algorithm('Newton', '-initial')
            dtt = self.dt
            ok = op.analyze(1, dtt)
            op.test(self.TEST_TYPE, self.TOL, self.ITERATIONS)
            op.algorithm(self.ALGORITHM_TYPE)
        if ok:
            if self.pflag:
                print(f"[FAILURE] Failed at {control_time} - "
                      "Trying NewtonWithLineSearch & relaxed convergence...")
            op.test('NormDispIncr', self.TOL * 0.1, self.ITERATIONS * 50)
            op.algorithm('NewtonLineSearch', 0.8)
            dtt = self.dt
            ok = op.analyze(1, dtt)
            op.test(self.TEST_TYPE, self.TOL, self.ITERATIONS)
            op.algorithm(self.ALGORITHM_TYPE)
        # Next, halve the timestep with both algorithm and tolerance reduction
        if ok:
            if self.pflag:
                print(f"[FAILURE] Failed at {control_time} - "
                      "Trying Newton with initial tangent, reduced timestep &"
                      f" relaxed convergence...")
            op.test('NormDispIncr', self.TOL * 0.1, self.ITERATIONS * 50)
            op.algorithm('Newton', '-initial')
            dtt = 0.5 * self.dt
            ok = op.analyze(1, dtt)
            op.test(self.TEST_TYPE, self.TOL, self.ITERATIONS)
            op.algorithm(self.ALGORITHM_TYPE)
        if ok:
            if self.pflag:
                print(f"[FAILURE] Failed at {control_time} - "
                      "Trying NewtonWithLineSearch, reduced timestep &"
                      f" relaxed convergence...")
            op.test('NormDispIncr', self.TOL * 0.1, self.ITERATIONS * 50)
            op.algorithm('NewtonLineSearch', 0.8)
            dtt = 0.5 * self.dt
            ok = op.analyze(1, dtt)
            op.test(self.TEST_TYPE, self.TOL, self.ITERATIONS)
            op.algorithm(self.ALGORITHM_TYPE)
        if ok:
            if self.pflag:
                print(f"[FAILURE] Failed at {control_time} - exit analysis...")
            self.collapse_index = -1

    def _verify_against_zerolength(self) -> np.ndarray:
        """Verify that the elements of the model are not of zero length

        Returns
        -------
        np.ndarray
            Storey heights
        """
        for d in range(len(self.tnode)):
            top_nodes = self.tnode[d]
            bot_nodes = self.bnode[d]

            h = np.array([])
            for i, top_node in enumerate(top_nodes):
                top = op.nodeCoord(int(top_node), 3)
                bot = op.nodeCoord(int(bot_nodes[i]), 3)

                dist = top - bot
                h = np.append(h, dist)

                if dist == 0:
                    warnings.warn('[WARNING] Zerolength found in drift check.')
        return h

    def solve(self, rec: int = None
              ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Looks for a solution, performs nonlinear time history analysis

        Returns
        -------
        Tuple[np.ndarray, np.ndarray, np.ndarray]
            Tuple contains:
                Accelerations in [g]
                Displacements in [m]
                Drifts in [%]
                Residual drifts in [%]
        """
        # Create self.output_path and a temporary cache folder
        if self.output_path is not None:
            if rec is None:
                cache_path = self.output_path / 'cache'
            else:
                cache_path = self.output_path / f'rec{rec}_cache'
        else:
            if rec is None:
                cache_path = Path('cache')
            else:
                cache_path = Path(f'rec{rec}_cache')
        create_path(cache_path)

        # Set up analysis parameters
        control_time = 0.0
        ok = 0
        mdrift_init = 0.0

        # Recorders for both horizontal directions
        for j in range(self.directions):
            filename = f'accelerations_{j + 1}.txt'

            # Recorders for nodal accelerations, because in current version of
            # openseespy ground accelerations are not being recorded otherwise
            # op.recorder('Node', '-file', str(cache_path / filename),
            #             '-timeSeries', int(f"5{j + 1}"),
            #             '-nodeRange', int(self.bnode[0, 0]
            #                               ), int(self.tnode[0, -1]),
            #             '-dof', j + 1, 'accel')

            _nodes = np.concatenate(
                ([self.bnode[0][0]], self.tnode[0])).tolist()

            op.recorder('Node', '-file', str(cache_path / filename),
                        '-timeSeries', int(f"5{j + 1}"),
                        '-node', *_nodes,
                        '-dof', j + 1, 'accel')

        # Number of storeys
        nst = self.tnode.shape[1]

        # initialize maximum drifts and accelerations
        mdrift = np.zeros((self.directions, nst))
        # maccel = np.zeros((directions, nst + 1))

        # Recorders for displacements, accelerations and drifts, initialization
        displacements = np.zeros((self.directions, nst + 1, 1))
        accelerations = np.zeros((self.directions, nst + 1, 1))
        drifts = np.zeros((self.directions, nst, 1))
        residuals = np.zeros((self.directions, nst, 1))

        h = self._verify_against_zerolength()

        # Run the actual analysis now
        while self.collapse_index == 0 and control_time <= self.dur and \
                not ok:
            # Start analysis
            ok = op.analyze(1, self.dt)
            control_time = op.getTime()

            # If the analysis fails, try the following changes to achieve
            # convergence
            # Analysis will be slower in here though...
            self._algorithm(ok, control_time)

            # Recorders
            temp_accel = np.zeros((self.directions, nst + 1, 1))
            temp_disp = np.zeros((self.directions, nst + 1, 1))
            temp_drift = np.zeros((self.directions, nst, 1))
            temp_res = np.zeros((self.directions, nst, 1))

            # Recording EDPs at each storey level to return
            # For each direction
            for j in range(temp_accel.shape[0]):
                # At each storey level
                for i in range(nst + 1):
                    if i == nst:
                        # Index 0 indicates along X direction, and 1 indicates
                        # along Y direction
                        # Nodal displacements in m
                        temp_disp[j, i, 0] = op.nodeDisp(
                            int(self.tnode[0, i - 1]), j + 1)

                    else:
                        temp_disp[j, i, 0] = op.nodeDisp(
                            int(self.bnode[0, i]), j + 1)

                    if i > 0:
                        # Storey height
                        cht = h[i - 1]
                        # Storey drifts in %
                        temp_drift[j, i - 1, 0] = 100.0 * \
                            abs(temp_disp[j, i, 0]
                                - temp_disp[j, i - 1, 0]) / cht

                        if control_time >= self.dur - self.extra_dur:
                            temp_res[j, i - 1, 0] = 100.0 * \
                                abs(temp_disp[j, i, 0]
                                    - temp_disp[j, i - 1, 0]) / cht

            # Appending into the global numpy arrays to return
            displacements = np.append(displacements, temp_disp, axis=2)
            drifts = np.append(drifts, temp_drift, axis=2)
            if control_time >= self.dur - self.extra_dur:
                residuals = np.append(residuals, temp_res, axis=2)

            # Check storey drifts and accelerations
            for i in range(1, nst + 1):
                # Top node displacement
                tnode_disp_x = op.nodeDisp(int(self.tnode[0, i - 1]), 1)
                tnode_disp_y = op.nodeDisp(int(self.tnode[0, i - 1]), 2)
                # Bottom node displacement
                bnode_disp_x = op.nodeDisp(int(self.bnode[0, i - 1]), 1)
                bnode_disp_y = op.nodeDisp(int(self.bnode[0, i - 1]), 2)
                # Storey height
                cht = h[i - 1]
                # Storey drift in %
                cdrift_x = 100.0 * abs(tnode_disp_x - bnode_disp_x) / cht
                cdrift_y = 100.0 * abs(tnode_disp_y - bnode_disp_y) / cht
                # Record the peak storey drifts
                if cdrift_x >= mdrift[0, i - 1]:
                    mdrift[0, i - 1] = cdrift_x

                if self.directions == 2 and cdrift_y >= mdrift[1, i - 1]:
                    mdrift[1, i - 1] = cdrift_y

                if max(cdrift_x, cdrift_y) >= mdrift_init:
                    mdrift_init = max(cdrift_x, cdrift_y)

            # Check whether drift capacity has been exceeded
            if mdrift_init >= self.dc:
                # If it was exceeded then local structure collapse is assumed
                self.collapse_index = 1
                # Hard cap the mdrift_init value to the drift capacity
                mdrift_init = self.dc

        # Wipe the model
        op.wipe()

        # Record the absolute accelerations, when use_recorder is True
        accelerations = []
        for j in range(self.directions):
            filename = f'accelerations_{j + 1}.txt'

            accelerations.append(np.transpose(
                read_text(cache_path / filename) / self.g))

        remove_directory_contents(cache_path)

        accelerations = np.asarray(accelerations)

        if self.collapse_index == -1:
            print(f"[FAILURE] Analysis failed to converge at {control_time}"
                  f" of {self.dur}.")
        if self.collapse_index == 0:
            print('[SUCCESS] Analysis completed successfully.')
        if self.collapse_index == 1:
            print('[FAILURE] Local structure collapse.')

        return accelerations, displacements, drifts, residuals
