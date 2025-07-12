import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(10001, 0.0, 0.0, 3.7)
    ops.node(10101, 4.15, 0.0, 3.7)
    ops.node(10201, 8.3, 0.0, 3.7)
    ops.node(10301, 11.25, 0.0, 3.7)
    ops.node(10401, 15.4, 0.0, 3.7)
    ops.node(10501, 19.55, 0.0, 3.7)
    ops.node(10011, 0.0, 5.25, 3.7)
    ops.node(10111, 4.15, 5.25, 3.7)
    ops.node(10211, 8.3, 5.25, 3.7)
    ops.node(10311, 11.25, 5.25, 3.7)
    ops.node(10411, 15.4, 5.25, 3.7)
    ops.node(10511, 19.55, 5.25, 3.7)
    ops.node(10021, 0.0, 10.5, 3.7)
    ops.node(10121, 4.15, 10.5, 3.7)
    ops.node(10221, 8.3, 10.5, 3.7)
    ops.node(10321, 11.25, 10.5, 3.7)
    ops.node(10421, 15.4, 10.5, 3.7)
    ops.node(10521, 19.55, 10.5, 3.7)
    # Retained floor node
    ops.node(91000, 9.775, 5.32875703, 3.7)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 10001, 10101, 10201, 10301, 10401, 10501, 10011, 10111, 10211, 10311, 10411, 10511, 10021, 10121, 10221, 10321, 10421, 10521)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(10002, 0.0, 0.0, 6.8)
    ops.node(10102, 4.15, 0.0, 6.8)
    ops.node(10202, 8.3, 0.0, 6.8)
    ops.node(10302, 11.25, 0.0, 6.8)
    ops.node(10402, 15.4, 0.0, 6.8)
    ops.node(10502, 19.55, 0.0, 6.8)
    ops.node(10012, 0.0, 5.25, 6.8)
    ops.node(10112, 4.15, 5.25, 6.8)
    ops.node(10212, 8.3, 5.25, 6.8)
    ops.node(10312, 11.25, 5.25, 6.8)
    ops.node(10412, 15.4, 5.25, 6.8)
    ops.node(10512, 19.55, 5.25, 6.8)
    ops.node(10022, 0.0, 10.5, 6.8)
    ops.node(10122, 4.15, 10.5, 6.8)
    ops.node(10222, 8.3, 10.5, 6.8)
    ops.node(10322, 11.25, 10.5, 6.8)
    ops.node(10422, 15.4, 10.5, 6.8)
    ops.node(10522, 19.55, 10.5, 6.8)
    # Retained floor node
    ops.node(92000, 9.775, 5.32751941, 6.8)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 10002, 10102, 10202, 10302, 10402, 10502, 10012, 10112, 10212, 10312, 10412, 10512, 10022, 10122, 10222, 10322, 10422, 10522)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(10003, 0.0, 0.0, 9.9)
    ops.node(10103, 4.15, 0.0, 9.9)
    ops.node(10203, 8.3, 0.0, 9.9)
    ops.node(10303, 11.25, 0.0, 9.9)
    ops.node(10403, 15.4, 0.0, 9.9)
    ops.node(10503, 19.55, 0.0, 9.9)
    ops.node(10013, 0.0, 5.25, 9.9)
    ops.node(10113, 4.15, 5.25, 9.9)
    ops.node(10213, 8.3, 5.25, 9.9)
    ops.node(10313, 11.25, 5.25, 9.9)
    ops.node(10413, 15.4, 5.25, 9.9)
    ops.node(10513, 19.55, 5.25, 9.9)
    ops.node(10023, 0.0, 10.5, 9.9)
    ops.node(10123, 4.15, 10.5, 9.9)
    ops.node(10223, 8.3, 10.5, 9.9)
    ops.node(10323, 11.25, 10.5, 9.9)
    ops.node(10423, 15.4, 10.5, 9.9)
    ops.node(10523, 19.55, 10.5, 9.9)
    # Retained floor node
    ops.node(93000, 9.775, 5.32751941, 9.9)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 10003, 10103, 10203, 10303, 10403, 10503, 10013, 10113, 10213, 10313, 10413, 10513, 10023, 10123, 10223, 10323, 10423, 10523)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(10004, 0.0, 0.0, 13.0)
    ops.node(10104, 4.15, 0.0, 13.0)
    ops.node(10204, 8.3, 0.0, 13.0)
    ops.node(10304, 11.25, 0.0, 13.0)
    ops.node(10404, 15.4, 0.0, 13.0)
    ops.node(10504, 19.55, 0.0, 13.0)
    ops.node(10014, 0.0, 5.25, 13.0)
    ops.node(10114, 4.15, 5.25, 13.0)
    ops.node(10214, 8.3, 5.25, 13.0)
    ops.node(10314, 11.25, 5.25, 13.0)
    ops.node(10414, 15.4, 5.25, 13.0)
    ops.node(10514, 19.55, 5.25, 13.0)
    ops.node(10024, 0.0, 10.5, 13.0)
    ops.node(10124, 4.15, 10.5, 13.0)
    ops.node(10224, 8.3, 10.5, 13.0)
    ops.node(10324, 11.25, 10.5, 13.0)
    ops.node(10424, 15.4, 10.5, 13.0)
    ops.node(10524, 19.55, 10.5, 13.0)
    # Retained floor node
    ops.node(94000, 9.775, 5.39851739, 13.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 10004, 10104, 10204, 10304, 10404, 10504, 10014, 10114, 10214, 10314, 10414, 10514, 10024, 10124, 10224, 10324, 10424, 10524)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
