import openseespy.opensees as ops
from pathlib import Path

from .model import build_model


def _set_algorithm(tol: float, ctrl_node: int, ctrl_dof: int, dincr: float, iter: int = 100) -> None:
    """Sets the solution algorithm for NSPA in ops domain.

    Parameters
    ----------
    tol : float
        The tolerance criteria used to check for convergence.
    ctrl_node : int
        Tag of control node.
    ctrl_dof : int
        Tag of control degrees of freedom, i.e., 1 or 2.
    dincr : float
        The displacement increment considered during analysis.
    iter : int, optional
        The max number of iterations to check before returning failure.
        By default 100.

    Return
    ------
    int
        Result of the new analysis step in OpenSees.
    """
    # Set testing and control procedures
    ops.test('NormDispIncr', tol, iter)
    ops.integrator('DisplacementControl', ctrl_node, ctrl_dof, dincr)
    # Try KrylovNewton
    ops.algorithm('KrylovNewton')
    ok = ops.analyze(1)
    # Try NewtonLineSearch algorithm
    if ok != 0:
        ops.algorithm('NewtonLineSearch', '-InitialInterpolated', 0.8)
        ok = ops.analyze(1)
    # Try Broyden algorithm
    if ok != 0:
        ops.algorithm('Broyden', 50)
        ok = ops.analyze(1)
    # Try Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithm
    if ok != 0:
        ops.algorithm('BFGS')
        ok = ops.analyze(1)
    # Return the analysis result
    return ok


def do_nspa_x(max_drift: float = 0.1, dincr: float = 0.0001) -> tuple[list[float], list[float]]:
    """Performs nonlinear static pushover analysis (NSPA) in x direction.

    Parameters
    ----------
    max_drift : float, optional.
        Maximum considered drift value for the control node.
        By default 0.1
    dincr : float, optional.
        First displacement increment considered during the analysis.
        By default 0.0001.

    Return
    ------
    ctrl_disp : list[float]
        Displacement values of control node.
    base_shear : list[float]
        Base shear value obtained as sum of the reaction forces.
    """
    # Set output directory
    output_directory = Path(__file__).parent / 'NSPA-Results'
    if not Path.exists(output_directory):
        Path.mkdir(output_directory)
    reaction_file_path = (output_directory / 'support_reactions_x.out').as_posix()
    disp_file_path = (output_directory / 'storey_displacements_x.out').as_posix()
    storey_heights_file_path = (output_directory / 'storey_heights.out').as_posix()

    # Build the numerical model
    build_model()

    # Add NSPA time-series and load pattern to ops domain
    ops.timeSeries('Linear', 2)
    ops.pattern('Plain', 2, 2)
    # Add lateral nspa loads to ops domain
    ops.load(91000, 0.13407360273425917, 0, 0, 0, 0, 0)
    ops.load(92000, 0.25520925742355594, 0, 0, 0, 0, 0)
    ops.load(93000, 0.34728011988139607, 0, 0, 0, 0, 0)
    ops.load(94000, 0.26343701996078883, 0, 0, 0, 0, 0)

    # Set the recorders
    ctrl_node = 94000  # Control node
    ctrl_dof = 1  # Control dof
    supports = [70000, 70010, 70020, 70100, 70110, 70120, 70200, 70210, 70220, 70300, 70310, 70320, 70400, 70410, 70420, 70500, 70510, 70520]  # Foundation nodes
    floors = [91000, 92000, 93000, 94000]  # Retained floor nodes
    ops.recorder('Node', '-file', disp_file_path, '-node', *floors, '-dof', ctrl_dof, 'disp')
    ops.recorder('Node', '-file', reaction_file_path, '-node', *supports, '-dof', ctrl_dof, 'reaction')

    # Base level coordinate
    base_level = min([ops.nodeCoord(node, 3) for node in supports])
    # Save storey heights
    with open(storey_heights_file_path, 'w') as file:
        for node in floors:
            file.write(f'{ops.nodeCoord(node, 3) - base_level}\n')

    # Set some analysis parameters
    max_disp = max_drift * (ops.nodeCoord(ctrl_node, 3) - base_level)
    tol_init = 1.0e-5
    iter_init = 20
    ops.wipeAnalysis()
    ops.system('UmfPack')
    ops.numberer('RCM')
    ops.constraints('Penalty', 1e12, 1e12)
    ops.test('NormDispIncr', tol_init, iter_init)
    ops.integrator('DisplacementControl', ctrl_node, ctrl_dof, dincr)
    ops.algorithm('Newton', '-initialThenCurrent')
    ops.analysis('Static')

    # Start performing the analysis
    base_shear = [0]
    ctrl_disp = [0]
    ok = 0
    cont = True
    while ok == 0 and cont:
        # Perform the analysis for a single step with current settings
        ok = ops.analyze(1)
        if ok != 0:  # try other algorithms
            ok = _set_algorithm(tol_init, ctrl_node, ctrl_dof, dincr)
        if ok != 0:  # reduce dincr to an half
            ok = _set_algorithm(tol_init, ctrl_node, ctrl_dof, 0.5 * dincr)
        if ok != 0:  # reduce dincr to a quarter
            ok = _set_algorithm(tol_init, ctrl_node, ctrl_dof, 0.25 * dincr)
        if ok != 0:  # increase tolerance by factor of 10
            ok = _set_algorithm(10 * tol_init, ctrl_node, ctrl_dof, 0.25 * dincr)
        if ok != 0:  # increase tolerance by factor of 100
            ok = _set_algorithm(100 * tol_init, ctrl_node, ctrl_dof, 0.25 * dincr)

        # Get the base shear force
        ops.reactions()
        current_disp = ops.nodeDisp(ctrl_node, ctrl_dof)
        current_shear = abs(sum([ops.nodeReaction(node, ctrl_dof) for node in supports]))
        # Set continue flag
        cont = current_disp < max_disp and current_shear < 50000 and current_shear >= 0.2*max(base_shear)
        # Append base shear and control node displacement
        if ok == 0 and cont:
            base_shear.append(current_shear)
            ctrl_disp.append(current_disp)

    # Wipe the model
    ops.wipe()
    # Return base shear and control node displacement history
    return ctrl_disp, base_shear


def do_nspa_y(max_drift: float = 0.1, dincr: float = 0.0001) -> tuple[list[float], list[float]]:
    """Performs nonlinear static pushover analysis (NSPA) in y direction.

    Parameters
    ----------
    max_drift : float, optional.
        Maximum considered drift value for the control node.
        By default 0.1
    dincr : float, optional.
        First displacement increment considered during the analysis.
        By default 0.0001.

    Return
    ------
    ctrl_disp : list[float]
        Displacement values of control node.
    base_shear : list[float]
        Base shear value obtained as sum of the reaction forces.
    """
    # Set output directory
    output_directory = Path(__file__).parent / 'NSPA-Results'
    if not Path.exists(output_directory):
        Path.mkdir(output_directory)
    reaction_file_path = (output_directory / 'support_reactions_y.out').as_posix()
    disp_file_path = (output_directory / 'storey_displacements_y.out').as_posix()
    storey_heights_file_path = (output_directory / 'storey_heights.out').as_posix()

    # Build the numerical model
    build_model()

    # Add NSPA time-series and load pattern to ops domain
    ops.timeSeries('Linear', 2)
    ops.pattern('Plain', 2, 2)
    # Add lateral nspa loads to ops domain
    ops.load(91000, 0, 0.13799161008035973, 0, 0, 0, 0)
    ops.load(92000, 0, 0.2572955243376413, 0, 0, 0, 0)
    ops.load(93000, 0, 0.3453282565350739, 0, 0, 0, 0)
    ops.load(94000, 0, 0.2593846090469251, 0, 0, 0, 0)

    # Set the recorders
    ctrl_node = 94000  # Control node
    ctrl_dof = 2  # Control dof
    supports = [70000, 70010, 70020, 70100, 70110, 70120, 70200, 70210, 70220, 70300, 70310, 70320, 70400, 70410, 70420, 70500, 70510, 70520]  # Foundation nodes
    floors = [91000, 92000, 93000, 94000]  # Retained floor nodes
    ops.recorder('Node', '-file', disp_file_path, '-node', *floors, '-dof', ctrl_dof, 'disp')
    ops.recorder('Node', '-file', reaction_file_path, '-node', *supports, '-dof', ctrl_dof, 'reaction')

    # Base level coordinate
    base_level = min([ops.nodeCoord(node, 3) for node in supports])
    # Save storey heights
    with open(storey_heights_file_path, 'w') as file:
        for node in floors:
            file.write(f'{ops.nodeCoord(node, 3) - base_level}\n')

    # Set some analysis parameters
    max_disp = max_drift * (ops.nodeCoord(ctrl_node, 3) - base_level)
    tol_init = 1.0e-5
    iter_init = 20
    ops.wipeAnalysis()
    ops.system('UmfPack')
    ops.numberer('RCM')
    ops.constraints('Penalty', 1e12, 1e12)
    ops.test('NormDispIncr', tol_init, iter_init)
    ops.integrator('DisplacementControl', ctrl_node, ctrl_dof, dincr)
    ops.algorithm('Newton', '-initialThenCurrent')
    ops.analysis('Static')

    # Start performing the analysis
    base_shear = [0]
    ctrl_disp = [0]
    ok = 0
    cont = True
    while ok == 0 and cont:
        # Perform the analysis for a single step with current settings
        ok = ops.analyze(1)
        if ok != 0:  # try other algorithms
            ok = _set_algorithm(tol_init, ctrl_node, ctrl_dof, dincr)
        if ok != 0:  # reduce dincr to an half
            ok = _set_algorithm(tol_init, ctrl_node, ctrl_dof, 0.5 * dincr)
        if ok != 0:  # reduce dincr to a quarter
            ok = _set_algorithm(tol_init, ctrl_node, ctrl_dof, 0.25 * dincr)
        if ok != 0:  # increase tolerance by factor of 10
            ok = _set_algorithm(10 * tol_init, ctrl_node, ctrl_dof, 0.25 * dincr)
        if ok != 0:  # increase tolerance by factor of 100
            ok = _set_algorithm(100 * tol_init, ctrl_node, ctrl_dof, 0.25 * dincr)

        # Get the base shear force
        ops.reactions()
        current_disp = ops.nodeDisp(ctrl_node, ctrl_dof)
        current_shear = abs(sum([ops.nodeReaction(node, ctrl_dof) for node in supports]))
        # Set continue flag
        cont = current_disp < max_disp and current_shear < 50000 and current_shear >= 0.2*max(base_shear)
        # Append base shear and control node displacement
        if ok == 0 and cont:
            base_shear.append(current_shear)
            ctrl_disp.append(current_disp)

    # Wipe the model
    ops.wipe()
    # Return base shear and control node displacement history
    return ctrl_disp, base_shear
