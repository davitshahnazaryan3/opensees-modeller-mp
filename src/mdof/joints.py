import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain (nodes and rigid offsets)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (2, 0, 0.5)
    # Central joint node
    ops.node(1201, 8.3, 0.0, 1.85, '-mass', 3.857145132517837, 3.857145132517837, 3.857145132517837, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31201, 8.45, 0.0, 1.85)
    ops.element('elasticBeamColumn', 31201, 1201, 31201, 99999, 88888)
    ops.node(21201, 8.3, 0.0, 1.7)
    ops.element('elasticBeamColumn', 21201, 21201, 1201, 99999, 99999)
    ops.node(71201, 8.3, 0.0, 2.0)
    ops.element('elasticBeamColumn', 71201, 1201, 71201, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 0.5)
    # Central joint node
    ops.node(1301, 11.25, 0.0, 1.85, '-mass', 3.857145132517837, 3.857145132517837, 3.857145132517837, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51301, 11.1, 0.0, 1.85)
    ops.element('elasticBeamColumn', 51301, 51301, 1301, 99999, 88888)
    ops.node(21301, 11.25, 0.0, 1.7)
    ops.element('elasticBeamColumn', 21301, 21301, 1301, 99999, 99999)
    ops.node(71301, 11.25, 0.0, 2.0)
    ops.element('elasticBeamColumn', 71301, 1301, 71301, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 1.5)
    # Central joint node
    ops.node(1202, 8.3, 0.0, 5.25, '-mass', 3.788337793068296, 3.788337793068296, 3.788337793068296, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31202, 8.45, 0.0, 5.25)
    ops.element('elasticBeamColumn', 31202, 1202, 31202, 99999, 88888)
    ops.node(21202, 8.3, 0.0, 5.1)
    ops.element('elasticBeamColumn', 21202, 21202, 1202, 99999, 99999)
    ops.node(71202, 8.3, 0.0, 5.4)
    ops.element('elasticBeamColumn', 71202, 1202, 71202, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 1.5)
    # Central joint node
    ops.node(1302, 11.25, 0.0, 5.25, '-mass', 3.788337793068296, 3.788337793068296, 3.788337793068296, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51302, 11.1, 0.0, 5.25)
    ops.element('elasticBeamColumn', 51302, 51302, 1302, 99999, 88888)
    ops.node(21302, 11.25, 0.0, 5.1)
    ops.element('elasticBeamColumn', 21302, 21302, 1302, 99999, 99999)
    ops.node(71302, 11.25, 0.0, 5.4)
    ops.element('elasticBeamColumn', 71302, 1302, 71302, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 2.5)
    # Central joint node
    ops.node(1203, 8.3, 0.0, 8.35, '-mass', 3.788337793068296, 3.788337793068296, 3.788337793068296, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31203, 8.45, 0.0, 8.35)
    ops.element('elasticBeamColumn', 31203, 1203, 31203, 99999, 88888)
    ops.node(21203, 8.3, 0.0, 8.2)
    ops.element('elasticBeamColumn', 21203, 21203, 1203, 99999, 99999)
    ops.node(71203, 8.3, 0.0, 8.5)
    ops.element('elasticBeamColumn', 71203, 1203, 71203, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 2.5)
    # Central joint node
    ops.node(1303, 11.25, 0.0, 8.35, '-mass', 3.788337793068296, 3.788337793068296, 3.788337793068296, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51303, 11.1, 0.0, 8.35)
    ops.element('elasticBeamColumn', 51303, 51303, 1303, 99999, 88888)
    ops.node(21303, 11.25, 0.0, 8.2)
    ops.element('elasticBeamColumn', 21303, 21303, 1303, 99999, 99999)
    ops.node(71303, 11.25, 0.0, 8.5)
    ops.element('elasticBeamColumn', 71303, 1303, 71303, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 3.5)
    # Central joint node
    ops.node(1204, 8.3, 0.0, 11.45, '-mass', 3.7883377930682958, 3.7883377930682958, 3.7883377930682958, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31204, 8.45, 0.0, 11.45)
    ops.element('elasticBeamColumn', 31204, 1204, 31204, 99999, 88888)
    ops.node(21204, 8.3, 0.0, 11.3)
    ops.element('elasticBeamColumn', 21204, 21204, 1204, 99999, 99999)
    ops.node(71204, 8.3, 0.0, 11.6)
    ops.element('elasticBeamColumn', 71204, 1204, 71204, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 3.5)
    # Central joint node
    ops.node(1304, 11.25, 0.0, 11.45, '-mass', 3.7883377930682958, 3.7883377930682958, 3.7883377930682958, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51304, 11.1, 0.0, 11.45)
    ops.element('elasticBeamColumn', 51304, 51304, 1304, 99999, 88888)
    ops.node(21304, 11.25, 0.0, 11.3)
    ops.element('elasticBeamColumn', 21304, 21304, 1304, 99999, 99999)
    ops.node(71304, 11.25, 0.0, 11.6)
    ops.element('elasticBeamColumn', 71304, 1304, 71304, 99999, 99999)

    # -------------------------------------------------
    # Add floor joints to ops domain (nodes, joint offsets and flexibility)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    # Central joint node
    ops.node(1, 0.0, 0.0, 3.7, '-mass', 8.369409206479421, 8.369409206479421, 8.369409206479421, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(30001, 0.15, 0.0, 3.7)
    ops.element('elasticBeamColumn', 30001, 1, 30001, 99999, 88888)
    ops.node(20001, 0.0, 0.0, 3.475)
    ops.element('elasticBeamColumn', 20001, 20001, 1, 99999, 99999)
    ops.node(70001, 0.0, 0.0, 3.925)
    ops.element('elasticBeamColumn', 70001, 1, 70001, 99999, 99999)
    ops.node(40001, 0.0, 0.15, 3.7)
    ops.element('elasticBeamColumn', 40001, 1, 40001, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10001, 1, 10001, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 1)
    # Central joint node
    ops.node(101, 4.15, 0.0, 3.7, '-mass', 11.711104345680555, 11.711104345680555, 11.711104345680555, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50101, 4.0, 0.0, 3.7)
    ops.element('elasticBeamColumn', 50101, 50101, 101, 99999, 88888)
    ops.node(30101, 4.3, 0.0, 3.7)
    ops.element('elasticBeamColumn', 30101, 101, 30101, 99999, 88888)
    ops.node(20101, 4.15, 0.0, 3.55)
    ops.element('elasticBeamColumn', 20101, 20101, 101, 99999, 99999)
    ops.node(70101, 4.15, 0.0, 3.85)
    ops.element('elasticBeamColumn', 70101, 101, 70101, 99999, 99999)
    ops.node(40101, 4.15, 0.15, 3.7)
    ops.element('elasticBeamColumn', 40101, 101, 40101, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10101, 101, 10101, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 1)
    # Central joint node
    ops.node(201, 8.3, 0.0, 3.7, '-mass', 8.512280001586454, 8.512280001586454, 8.512280001586454, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50201, 8.15, 0.0, 3.7)
    ops.element('elasticBeamColumn', 50201, 50201, 201, 99999, 88888)
    ops.node(30201, 8.45, 0.0, 3.7)
    ops.element('elasticBeamColumn', 30201, 201, 30201, 99999, 88888)
    ops.node(20201, 8.3, 0.0, 3.55)
    ops.element('elasticBeamColumn', 20201, 20201, 201, 99999, 99999)
    ops.node(70201, 8.3, 0.0, 3.85)
    ops.element('elasticBeamColumn', 70201, 201, 70201, 99999, 99999)
    ops.node(40201, 8.3, 0.15, 3.7)
    ops.element('elasticBeamColumn', 40201, 201, 40201, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10201, 201, 10201, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 1)
    # Central joint node
    ops.node(301, 11.25, 0.0, 3.7, '-mass', 8.512280001586454, 8.512280001586454, 8.512280001586454, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50301, 11.1, 0.0, 3.7)
    ops.element('elasticBeamColumn', 50301, 50301, 301, 99999, 88888)
    ops.node(30301, 11.4, 0.0, 3.7)
    ops.element('elasticBeamColumn', 30301, 301, 30301, 99999, 88888)
    ops.node(20301, 11.25, 0.0, 3.55)
    ops.element('elasticBeamColumn', 20301, 20301, 301, 99999, 99999)
    ops.node(70301, 11.25, 0.0, 3.85)
    ops.element('elasticBeamColumn', 70301, 301, 70301, 99999, 99999)
    ops.node(40301, 11.25, 0.15, 3.7)
    ops.element('elasticBeamColumn', 40301, 301, 40301, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10301, 301, 10301, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 1)
    # Central joint node
    ops.node(401, 15.4, 0.0, 3.7, '-mass', 11.711104345680555, 11.711104345680555, 11.711104345680555, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50401, 15.25, 0.0, 3.7)
    ops.element('elasticBeamColumn', 50401, 50401, 401, 99999, 88888)
    ops.node(30401, 15.55, 0.0, 3.7)
    ops.element('elasticBeamColumn', 30401, 401, 30401, 99999, 88888)
    ops.node(20401, 15.4, 0.0, 3.55)
    ops.element('elasticBeamColumn', 20401, 20401, 401, 99999, 99999)
    ops.node(70401, 15.4, 0.0, 3.85)
    ops.element('elasticBeamColumn', 70401, 401, 70401, 99999, 99999)
    ops.node(40401, 15.4, 0.15, 3.7)
    ops.element('elasticBeamColumn', 40401, 401, 40401, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10401, 401, 10401, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 1)
    # Central joint node
    ops.node(501, 19.55, 0.0, 3.7, '-mass', 8.369409206479421, 8.369409206479421, 8.369409206479421, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50501, 19.4, 0.0, 3.7)
    ops.element('elasticBeamColumn', 50501, 50501, 501, 99999, 88888)
    ops.node(20501, 19.55, 0.0, 3.475)
    ops.element('elasticBeamColumn', 20501, 20501, 501, 99999, 99999)
    ops.node(70501, 19.55, 0.0, 3.925)
    ops.element('elasticBeamColumn', 70501, 501, 70501, 99999, 99999)
    ops.node(40501, 19.55, 0.15, 3.7)
    ops.element('elasticBeamColumn', 40501, 501, 40501, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10501, 501, 10501, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 1)
    # Central joint node
    ops.node(11, 0.0, 5.25, 3.7, '-mass', 12.962060003172907, 12.962060003172907, 12.962060003172907, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(30011, 0.175, 5.25, 3.7)
    ops.element('elasticBeamColumn', 30011, 11, 30011, 99999, 88888)
    ops.node(20011, 0.0, 5.25, 3.475)
    ops.element('elasticBeamColumn', 20011, 20011, 11, 99999, 99999)
    ops.node(70011, 0.0, 5.25, 3.925)
    ops.element('elasticBeamColumn', 70011, 11, 70011, 99999, 99999)
    ops.node(60011, 0.0, 5.075, 3.7)
    ops.element('elasticBeamColumn', 60011, 60011, 11, 99999, 77777)
    ops.node(40011, 0.0, 5.425, 3.7)
    ops.element('elasticBeamColumn', 40011, 11, 40011, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10011, 11, 10011, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 1)
    # Central joint node
    ops.node(111, 4.15, 5.25, 3.7, '-mass', 16.366907977803518, 16.366907977803518, 16.366907977803518, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50111, 3.975, 5.25, 3.7)
    ops.element('elasticBeamColumn', 50111, 50111, 111, 99999, 88888)
    ops.node(30111, 4.325, 5.25, 3.7)
    ops.element('elasticBeamColumn', 30111, 111, 30111, 99999, 88888)
    ops.node(20111, 4.15, 5.25, 3.55)
    ops.element('elasticBeamColumn', 20111, 20111, 111, 99999, 99999)
    ops.node(70111, 4.15, 5.25, 3.85)
    ops.element('elasticBeamColumn', 70111, 111, 70111, 99999, 99999)
    ops.node(60111, 4.15, 5.075, 3.7)
    ops.element('elasticBeamColumn', 60111, 60111, 111, 99999, 77777)
    ops.node(40111, 4.15, 5.425, 3.7)
    ops.element('elasticBeamColumn', 40111, 111, 40111, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10111, 111, 10111, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 1)
    # Central joint node
    ops.node(211, 8.3, 5.25, 3.7, '-mass', 16.554057787995426, 16.554057787995426, 16.554057787995426, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50211, 8.125, 5.25, 3.7)
    ops.element('elasticBeamColumn', 50211, 50211, 211, 99999, 88888)
    ops.node(30211, 8.475, 5.25, 3.7)
    ops.element('elasticBeamColumn', 30211, 211, 30211, 99999, 88888)
    ops.node(20211, 8.3, 5.25, 3.55)
    ops.element('elasticBeamColumn', 20211, 20211, 211, 99999, 99999)
    ops.node(70211, 8.3, 5.25, 3.85)
    ops.element('elasticBeamColumn', 70211, 211, 70211, 99999, 99999)
    ops.node(60211, 8.3, 5.075, 3.7)
    ops.element('elasticBeamColumn', 60211, 60211, 211, 99999, 77777)
    ops.node(40211, 8.3, 5.425, 3.7)
    ops.element('elasticBeamColumn', 40211, 211, 40211, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10211, 211, 10211, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 1)
    # Central joint node
    ops.node(311, 11.25, 5.25, 3.7, '-mass', 16.554057787995426, 16.554057787995426, 16.554057787995426, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50311, 11.075, 5.25, 3.7)
    ops.element('elasticBeamColumn', 50311, 50311, 311, 99999, 88888)
    ops.node(30311, 11.425, 5.25, 3.7)
    ops.element('elasticBeamColumn', 30311, 311, 30311, 99999, 88888)
    ops.node(20311, 11.25, 5.25, 3.55)
    ops.element('elasticBeamColumn', 20311, 20311, 311, 99999, 99999)
    ops.node(70311, 11.25, 5.25, 3.85)
    ops.element('elasticBeamColumn', 70311, 311, 70311, 99999, 99999)
    ops.node(60311, 11.25, 5.075, 3.7)
    ops.element('elasticBeamColumn', 60311, 60311, 311, 99999, 77777)
    ops.node(40311, 11.25, 5.425, 3.7)
    ops.element('elasticBeamColumn', 40311, 311, 40311, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10311, 311, 10311, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 1)
    # Central joint node
    ops.node(411, 15.4, 5.25, 3.7, '-mass', 16.366907977803518, 16.366907977803518, 16.366907977803518, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50411, 15.225, 5.25, 3.7)
    ops.element('elasticBeamColumn', 50411, 50411, 411, 99999, 88888)
    ops.node(30411, 15.575, 5.25, 3.7)
    ops.element('elasticBeamColumn', 30411, 411, 30411, 99999, 88888)
    ops.node(20411, 15.4, 5.25, 3.55)
    ops.element('elasticBeamColumn', 20411, 20411, 411, 99999, 99999)
    ops.node(70411, 15.4, 5.25, 3.85)
    ops.element('elasticBeamColumn', 70411, 411, 70411, 99999, 99999)
    ops.node(60411, 15.4, 5.075, 3.7)
    ops.element('elasticBeamColumn', 60411, 60411, 411, 99999, 77777)
    ops.node(40411, 15.4, 5.425, 3.7)
    ops.element('elasticBeamColumn', 40411, 411, 40411, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10411, 411, 10411, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 1)
    # Central joint node
    ops.node(511, 19.55, 5.25, 3.7, '-mass', 12.962060003172907, 12.962060003172907, 12.962060003172907, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50511, 19.375, 5.25, 3.7)
    ops.element('elasticBeamColumn', 50511, 50511, 511, 99999, 88888)
    ops.node(20511, 19.55, 5.25, 3.475)
    ops.element('elasticBeamColumn', 20511, 20511, 511, 99999, 99999)
    ops.node(70511, 19.55, 5.25, 3.925)
    ops.element('elasticBeamColumn', 70511, 511, 70511, 99999, 99999)
    ops.node(60511, 19.55, 5.075, 3.7)
    ops.element('elasticBeamColumn', 60511, 60511, 511, 99999, 77777)
    ops.node(40511, 19.55, 5.425, 3.7)
    ops.element('elasticBeamColumn', 40511, 511, 40511, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10511, 511, 10511, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 1)
    # Central joint node
    ops.node(21, 0.0, 10.5, 3.7, '-mass', 8.369409206479421, 8.369409206479421, 8.369409206479421, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(30021, 0.15, 10.5, 3.7)
    ops.element('elasticBeamColumn', 30021, 21, 30021, 99999, 88888)
    ops.node(20021, 0.0, 10.5, 3.475)
    ops.element('elasticBeamColumn', 20021, 20021, 21, 99999, 99999)
    ops.node(70021, 0.0, 10.5, 3.925)
    ops.element('elasticBeamColumn', 70021, 21, 70021, 99999, 99999)
    ops.node(60021, 0.0, 10.35, 3.7)
    ops.element('elasticBeamColumn', 60021, 60021, 21, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10021, 21, 10021, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 1)
    # Central joint node
    ops.node(121, 4.15, 10.5, 3.7, '-mass', 11.711104345680555, 11.711104345680555, 11.711104345680555, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50121, 4.0, 10.5, 3.7)
    ops.element('elasticBeamColumn', 50121, 50121, 121, 99999, 88888)
    ops.node(30121, 4.3, 10.5, 3.7)
    ops.element('elasticBeamColumn', 30121, 121, 30121, 99999, 88888)
    ops.node(20121, 4.15, 10.5, 3.55)
    ops.element('elasticBeamColumn', 20121, 20121, 121, 99999, 99999)
    ops.node(70121, 4.15, 10.5, 3.85)
    ops.element('elasticBeamColumn', 70121, 121, 70121, 99999, 99999)
    ops.node(60121, 4.15, 10.35, 3.7)
    ops.element('elasticBeamColumn', 60121, 60121, 121, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10121, 121, 10121, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 1)
    # Central joint node
    ops.node(221, 8.3, 10.5, 3.7, '-mass', 10.081995039212236, 10.081995039212236, 10.081995039212236, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50221, 8.15, 10.5, 3.7)
    ops.element('elasticBeamColumn', 50221, 50221, 221, 99999, 88888)
    ops.node(30221, 8.45, 10.5, 3.7)
    ops.element('elasticBeamColumn', 30221, 221, 30221, 99999, 88888)
    ops.node(20221, 8.3, 10.5, 3.55)
    ops.element('elasticBeamColumn', 20221, 20221, 221, 99999, 99999)
    ops.node(70221, 8.3, 10.5, 3.85)
    ops.element('elasticBeamColumn', 70221, 221, 70221, 99999, 99999)
    ops.node(60221, 8.3, 10.35, 3.7)
    ops.element('elasticBeamColumn', 60221, 60221, 221, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10221, 221, 10221, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 1)
    # Central joint node
    ops.node(321, 11.25, 10.5, 3.7, '-mass', 10.081995039212236, 10.081995039212236, 10.081995039212236, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50321, 11.1, 10.5, 3.7)
    ops.element('elasticBeamColumn', 50321, 50321, 321, 99999, 88888)
    ops.node(30321, 11.4, 10.5, 3.7)
    ops.element('elasticBeamColumn', 30321, 321, 30321, 99999, 88888)
    ops.node(20321, 11.25, 10.5, 3.55)
    ops.element('elasticBeamColumn', 20321, 20321, 321, 99999, 99999)
    ops.node(70321, 11.25, 10.5, 3.85)
    ops.element('elasticBeamColumn', 70321, 321, 70321, 99999, 99999)
    ops.node(60321, 11.25, 10.35, 3.7)
    ops.element('elasticBeamColumn', 60321, 60321, 321, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10321, 321, 10321, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 1)
    # Central joint node
    ops.node(421, 15.4, 10.5, 3.7, '-mass', 11.711104345680555, 11.711104345680555, 11.711104345680555, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50421, 15.25, 10.5, 3.7)
    ops.element('elasticBeamColumn', 50421, 50421, 421, 99999, 88888)
    ops.node(30421, 15.55, 10.5, 3.7)
    ops.element('elasticBeamColumn', 30421, 421, 30421, 99999, 88888)
    ops.node(20421, 15.4, 10.5, 3.55)
    ops.element('elasticBeamColumn', 20421, 20421, 421, 99999, 99999)
    ops.node(70421, 15.4, 10.5, 3.85)
    ops.element('elasticBeamColumn', 70421, 421, 70421, 99999, 99999)
    ops.node(60421, 15.4, 10.35, 3.7)
    ops.element('elasticBeamColumn', 60421, 60421, 421, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10421, 421, 10421, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 1)
    # Central joint node
    ops.node(521, 19.55, 10.5, 3.7, '-mass', 8.369409206479421, 8.369409206479421, 8.369409206479421, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50521, 19.4, 10.5, 3.7)
    ops.element('elasticBeamColumn', 50521, 50521, 521, 99999, 88888)
    ops.node(20521, 19.55, 10.5, 3.475)
    ops.element('elasticBeamColumn', 20521, 20521, 521, 99999, 99999)
    ops.node(70521, 19.55, 10.5, 3.925)
    ops.element('elasticBeamColumn', 70521, 521, 70521, 99999, 99999)
    ops.node(60521, 19.55, 10.35, 3.7)
    ops.element('elasticBeamColumn', 60521, 60521, 521, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10521, 521, 10521, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 2)
    # Central joint node
    ops.node(2, 0.0, 0.0, 6.8, '-mass', 8.300601867029881, 8.300601867029881, 8.300601867029881, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(30002, 0.15, 0.0, 6.8)
    ops.element('elasticBeamColumn', 30002, 2, 30002, 99999, 88888)
    ops.node(20002, 0.0, 0.0, 6.575)
    ops.element('elasticBeamColumn', 20002, 20002, 2, 99999, 99999)
    ops.node(70002, 0.0, 0.0, 7.025)
    ops.element('elasticBeamColumn', 70002, 2, 70002, 99999, 99999)
    ops.node(40002, 0.0, 0.15, 6.8)
    ops.element('elasticBeamColumn', 40002, 2, 40002, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10002, 2, 10002, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 2)
    # Central joint node
    ops.node(102, 4.15, 0.0, 6.8, '-mass', 11.642297006231013, 11.642297006231013, 11.642297006231013, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50102, 4.0, 0.0, 6.8)
    ops.element('elasticBeamColumn', 50102, 50102, 102, 99999, 88888)
    ops.node(30102, 4.3, 0.0, 6.8)
    ops.element('elasticBeamColumn', 30102, 102, 30102, 99999, 88888)
    ops.node(20102, 4.15, 0.0, 6.65)
    ops.element('elasticBeamColumn', 20102, 20102, 102, 99999, 99999)
    ops.node(70102, 4.15, 0.0, 6.95)
    ops.element('elasticBeamColumn', 70102, 102, 70102, 99999, 99999)
    ops.node(40102, 4.15, 0.15, 6.8)
    ops.element('elasticBeamColumn', 40102, 102, 40102, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10102, 102, 10102, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 2)
    # Central joint node
    ops.node(202, 8.3, 0.0, 6.8, '-mass', 8.477876331861683, 8.477876331861683, 8.477876331861683, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50202, 8.15, 0.0, 6.8)
    ops.element('elasticBeamColumn', 50202, 50202, 202, 99999, 88888)
    ops.node(30202, 8.45, 0.0, 6.8)
    ops.element('elasticBeamColumn', 30202, 202, 30202, 99999, 88888)
    ops.node(20202, 8.3, 0.0, 6.65)
    ops.element('elasticBeamColumn', 20202, 20202, 202, 99999, 99999)
    ops.node(70202, 8.3, 0.0, 6.95)
    ops.element('elasticBeamColumn', 70202, 202, 70202, 99999, 99999)
    ops.node(40202, 8.3, 0.15, 6.8)
    ops.element('elasticBeamColumn', 40202, 202, 40202, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10202, 202, 10202, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 2)
    # Central joint node
    ops.node(302, 11.25, 0.0, 6.8, '-mass', 8.477876331861683, 8.477876331861683, 8.477876331861683, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50302, 11.1, 0.0, 6.8)
    ops.element('elasticBeamColumn', 50302, 50302, 302, 99999, 88888)
    ops.node(30302, 11.4, 0.0, 6.8)
    ops.element('elasticBeamColumn', 30302, 302, 30302, 99999, 88888)
    ops.node(20302, 11.25, 0.0, 6.65)
    ops.element('elasticBeamColumn', 20302, 20302, 302, 99999, 99999)
    ops.node(70302, 11.25, 0.0, 6.95)
    ops.element('elasticBeamColumn', 70302, 302, 70302, 99999, 99999)
    ops.node(40302, 11.25, 0.15, 6.8)
    ops.element('elasticBeamColumn', 40302, 302, 40302, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10302, 302, 10302, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 2)
    # Central joint node
    ops.node(402, 15.4, 0.0, 6.8, '-mass', 11.642297006231013, 11.642297006231013, 11.642297006231013, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50402, 15.25, 0.0, 6.8)
    ops.element('elasticBeamColumn', 50402, 50402, 402, 99999, 88888)
    ops.node(30402, 15.55, 0.0, 6.8)
    ops.element('elasticBeamColumn', 30402, 402, 30402, 99999, 88888)
    ops.node(20402, 15.4, 0.0, 6.65)
    ops.element('elasticBeamColumn', 20402, 20402, 402, 99999, 99999)
    ops.node(70402, 15.4, 0.0, 6.95)
    ops.element('elasticBeamColumn', 70402, 402, 70402, 99999, 99999)
    ops.node(40402, 15.4, 0.15, 6.8)
    ops.element('elasticBeamColumn', 40402, 402, 40402, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10402, 402, 10402, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 2)
    # Central joint node
    ops.node(502, 19.55, 0.0, 6.8, '-mass', 8.300601867029881, 8.300601867029881, 8.300601867029881, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50502, 19.4, 0.0, 6.8)
    ops.element('elasticBeamColumn', 50502, 50502, 502, 99999, 88888)
    ops.node(20502, 19.55, 0.0, 6.575)
    ops.element('elasticBeamColumn', 20502, 20502, 502, 99999, 99999)
    ops.node(70502, 19.55, 0.0, 7.025)
    ops.element('elasticBeamColumn', 70502, 502, 70502, 99999, 99999)
    ops.node(40502, 19.55, 0.15, 6.8)
    ops.element('elasticBeamColumn', 40502, 502, 40502, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10502, 502, 10502, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 2)
    # Central joint node
    ops.node(12, 0.0, 5.25, 6.8, '-mass', 12.868405568922142, 12.868405568922142, 12.868405568922142, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(30012, 0.175, 5.25, 6.8)
    ops.element('elasticBeamColumn', 30012, 12, 30012, 99999, 88888)
    ops.node(20012, 0.0, 5.25, 6.575)
    ops.element('elasticBeamColumn', 20012, 20012, 12, 99999, 99999)
    ops.node(70012, 0.0, 5.25, 7.025)
    ops.element('elasticBeamColumn', 70012, 12, 70012, 99999, 99999)
    ops.node(60012, 0.0, 5.075, 6.8)
    ops.element('elasticBeamColumn', 60012, 60012, 12, 99999, 77777)
    ops.node(40012, 0.0, 5.425, 6.8)
    ops.element('elasticBeamColumn', 40012, 12, 40012, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10012, 12, 10012, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 2)
    # Central joint node
    ops.node(112, 4.15, 5.25, 6.8, '-mass', 16.27325354355275, 16.27325354355275, 16.27325354355275, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50112, 3.975, 5.25, 6.8)
    ops.element('elasticBeamColumn', 50112, 50112, 112, 99999, 88888)
    ops.node(30112, 4.325, 5.25, 6.8)
    ops.element('elasticBeamColumn', 30112, 112, 30112, 99999, 88888)
    ops.node(20112, 4.15, 5.25, 6.65)
    ops.element('elasticBeamColumn', 20112, 20112, 112, 99999, 99999)
    ops.node(70112, 4.15, 5.25, 6.95)
    ops.element('elasticBeamColumn', 70112, 112, 70112, 99999, 99999)
    ops.node(60112, 4.15, 5.075, 6.8)
    ops.element('elasticBeamColumn', 60112, 60112, 112, 99999, 77777)
    ops.node(40112, 4.15, 5.425, 6.8)
    ops.element('elasticBeamColumn', 40112, 112, 40112, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10112, 112, 10112, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 2)
    # Central joint node
    ops.node(212, 8.3, 5.25, 6.8, '-mass', 16.460403353744663, 16.460403353744663, 16.460403353744663, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50212, 8.125, 5.25, 6.8)
    ops.element('elasticBeamColumn', 50212, 50212, 212, 99999, 88888)
    ops.node(30212, 8.475, 5.25, 6.8)
    ops.element('elasticBeamColumn', 30212, 212, 30212, 99999, 88888)
    ops.node(20212, 8.3, 5.25, 6.65)
    ops.element('elasticBeamColumn', 20212, 20212, 212, 99999, 99999)
    ops.node(70212, 8.3, 5.25, 6.95)
    ops.element('elasticBeamColumn', 70212, 212, 70212, 99999, 99999)
    ops.node(60212, 8.3, 5.075, 6.8)
    ops.element('elasticBeamColumn', 60212, 60212, 212, 99999, 77777)
    ops.node(40212, 8.3, 5.425, 6.8)
    ops.element('elasticBeamColumn', 40212, 212, 40212, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10212, 212, 10212, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 2)
    # Central joint node
    ops.node(312, 11.25, 5.25, 6.8, '-mass', 16.460403353744663, 16.460403353744663, 16.460403353744663, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50312, 11.075, 5.25, 6.8)
    ops.element('elasticBeamColumn', 50312, 50312, 312, 99999, 88888)
    ops.node(30312, 11.425, 5.25, 6.8)
    ops.element('elasticBeamColumn', 30312, 312, 30312, 99999, 88888)
    ops.node(20312, 11.25, 5.25, 6.65)
    ops.element('elasticBeamColumn', 20312, 20312, 312, 99999, 99999)
    ops.node(70312, 11.25, 5.25, 6.95)
    ops.element('elasticBeamColumn', 70312, 312, 70312, 99999, 99999)
    ops.node(60312, 11.25, 5.075, 6.8)
    ops.element('elasticBeamColumn', 60312, 60312, 312, 99999, 77777)
    ops.node(40312, 11.25, 5.425, 6.8)
    ops.element('elasticBeamColumn', 40312, 312, 40312, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10312, 312, 10312, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 2)
    # Central joint node
    ops.node(412, 15.4, 5.25, 6.8, '-mass', 16.27325354355275, 16.27325354355275, 16.27325354355275, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50412, 15.225, 5.25, 6.8)
    ops.element('elasticBeamColumn', 50412, 50412, 412, 99999, 88888)
    ops.node(30412, 15.575, 5.25, 6.8)
    ops.element('elasticBeamColumn', 30412, 412, 30412, 99999, 88888)
    ops.node(20412, 15.4, 5.25, 6.65)
    ops.element('elasticBeamColumn', 20412, 20412, 412, 99999, 99999)
    ops.node(70412, 15.4, 5.25, 6.95)
    ops.element('elasticBeamColumn', 70412, 412, 70412, 99999, 99999)
    ops.node(60412, 15.4, 5.075, 6.8)
    ops.element('elasticBeamColumn', 60412, 60412, 412, 99999, 77777)
    ops.node(40412, 15.4, 5.425, 6.8)
    ops.element('elasticBeamColumn', 40412, 412, 40412, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10412, 412, 10412, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 2)
    # Central joint node
    ops.node(512, 19.55, 5.25, 6.8, '-mass', 12.868405568922142, 12.868405568922142, 12.868405568922142, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50512, 19.375, 5.25, 6.8)
    ops.element('elasticBeamColumn', 50512, 50512, 512, 99999, 88888)
    ops.node(20512, 19.55, 5.25, 6.575)
    ops.element('elasticBeamColumn', 20512, 20512, 512, 99999, 99999)
    ops.node(70512, 19.55, 5.25, 7.025)
    ops.element('elasticBeamColumn', 70512, 512, 70512, 99999, 99999)
    ops.node(60512, 19.55, 5.075, 6.8)
    ops.element('elasticBeamColumn', 60512, 60512, 512, 99999, 77777)
    ops.node(40512, 19.55, 5.425, 6.8)
    ops.element('elasticBeamColumn', 40512, 512, 40512, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10512, 512, 10512, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 2)
    # Central joint node
    ops.node(22, 0.0, 10.5, 6.8, '-mass', 8.300601867029881, 8.300601867029881, 8.300601867029881, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(30022, 0.15, 10.5, 6.8)
    ops.element('elasticBeamColumn', 30022, 22, 30022, 99999, 88888)
    ops.node(20022, 0.0, 10.5, 6.575)
    ops.element('elasticBeamColumn', 20022, 20022, 22, 99999, 99999)
    ops.node(70022, 0.0, 10.5, 7.025)
    ops.element('elasticBeamColumn', 70022, 22, 70022, 99999, 99999)
    ops.node(60022, 0.0, 10.35, 6.8)
    ops.element('elasticBeamColumn', 60022, 60022, 22, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10022, 22, 10022, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 2)
    # Central joint node
    ops.node(122, 4.15, 10.5, 6.8, '-mass', 11.642297006231013, 11.642297006231013, 11.642297006231013, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50122, 4.0, 10.5, 6.8)
    ops.element('elasticBeamColumn', 50122, 50122, 122, 99999, 88888)
    ops.node(30122, 4.3, 10.5, 6.8)
    ops.element('elasticBeamColumn', 30122, 122, 30122, 99999, 88888)
    ops.node(20122, 4.15, 10.5, 6.65)
    ops.element('elasticBeamColumn', 20122, 20122, 122, 99999, 99999)
    ops.node(70122, 4.15, 10.5, 6.95)
    ops.element('elasticBeamColumn', 70122, 122, 70122, 99999, 99999)
    ops.node(60122, 4.15, 10.35, 6.8)
    ops.element('elasticBeamColumn', 60122, 60122, 122, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10122, 122, 10122, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 2)
    # Central joint node
    ops.node(222, 8.3, 10.5, 6.8, '-mass', 10.013187699762694, 10.013187699762694, 10.013187699762694, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50222, 8.15, 10.5, 6.8)
    ops.element('elasticBeamColumn', 50222, 50222, 222, 99999, 88888)
    ops.node(30222, 8.45, 10.5, 6.8)
    ops.element('elasticBeamColumn', 30222, 222, 30222, 99999, 88888)
    ops.node(20222, 8.3, 10.5, 6.65)
    ops.element('elasticBeamColumn', 20222, 20222, 222, 99999, 99999)
    ops.node(70222, 8.3, 10.5, 6.95)
    ops.element('elasticBeamColumn', 70222, 222, 70222, 99999, 99999)
    ops.node(60222, 8.3, 10.35, 6.8)
    ops.element('elasticBeamColumn', 60222, 60222, 222, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10222, 222, 10222, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 2)
    # Central joint node
    ops.node(322, 11.25, 10.5, 6.8, '-mass', 10.013187699762694, 10.013187699762694, 10.013187699762694, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50322, 11.1, 10.5, 6.8)
    ops.element('elasticBeamColumn', 50322, 50322, 322, 99999, 88888)
    ops.node(30322, 11.4, 10.5, 6.8)
    ops.element('elasticBeamColumn', 30322, 322, 30322, 99999, 88888)
    ops.node(20322, 11.25, 10.5, 6.65)
    ops.element('elasticBeamColumn', 20322, 20322, 322, 99999, 99999)
    ops.node(70322, 11.25, 10.5, 6.95)
    ops.element('elasticBeamColumn', 70322, 322, 70322, 99999, 99999)
    ops.node(60322, 11.25, 10.35, 6.8)
    ops.element('elasticBeamColumn', 60322, 60322, 322, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10322, 322, 10322, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 2)
    # Central joint node
    ops.node(422, 15.4, 10.5, 6.8, '-mass', 11.642297006231013, 11.642297006231013, 11.642297006231013, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50422, 15.25, 10.5, 6.8)
    ops.element('elasticBeamColumn', 50422, 50422, 422, 99999, 88888)
    ops.node(30422, 15.55, 10.5, 6.8)
    ops.element('elasticBeamColumn', 30422, 422, 30422, 99999, 88888)
    ops.node(20422, 15.4, 10.5, 6.65)
    ops.element('elasticBeamColumn', 20422, 20422, 422, 99999, 99999)
    ops.node(70422, 15.4, 10.5, 6.95)
    ops.element('elasticBeamColumn', 70422, 422, 70422, 99999, 99999)
    ops.node(60422, 15.4, 10.35, 6.8)
    ops.element('elasticBeamColumn', 60422, 60422, 422, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10422, 422, 10422, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 2)
    # Central joint node
    ops.node(522, 19.55, 10.5, 6.8, '-mass', 8.300601867029881, 8.300601867029881, 8.300601867029881, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50522, 19.4, 10.5, 6.8)
    ops.element('elasticBeamColumn', 50522, 50522, 522, 99999, 88888)
    ops.node(20522, 19.55, 10.5, 6.575)
    ops.element('elasticBeamColumn', 20522, 20522, 522, 99999, 99999)
    ops.node(70522, 19.55, 10.5, 7.025)
    ops.element('elasticBeamColumn', 70522, 522, 70522, 99999, 99999)
    ops.node(60522, 19.55, 10.35, 6.8)
    ops.element('elasticBeamColumn', 60522, 60522, 522, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10522, 522, 10522, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 3)
    # Central joint node
    ops.node(3, 0.0, 0.0, 9.9, '-mass', 8.300601867029881, 8.300601867029881, 8.300601867029881, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(30003, 0.15, 0.0, 9.9)
    ops.element('elasticBeamColumn', 30003, 3, 30003, 99999, 88888)
    ops.node(20003, 0.0, 0.0, 9.675)
    ops.element('elasticBeamColumn', 20003, 20003, 3, 99999, 99999)
    ops.node(70003, 0.0, 0.0, 10.125)
    ops.element('elasticBeamColumn', 70003, 3, 70003, 99999, 99999)
    ops.node(40003, 0.0, 0.15, 9.9)
    ops.element('elasticBeamColumn', 40003, 3, 40003, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10003, 3, 10003, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 3)
    # Central joint node
    ops.node(103, 4.15, 0.0, 9.9, '-mass', 11.642297006231013, 11.642297006231013, 11.642297006231013, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50103, 4.0, 0.0, 9.9)
    ops.element('elasticBeamColumn', 50103, 50103, 103, 99999, 88888)
    ops.node(30103, 4.3, 0.0, 9.9)
    ops.element('elasticBeamColumn', 30103, 103, 30103, 99999, 88888)
    ops.node(20103, 4.15, 0.0, 9.75)
    ops.element('elasticBeamColumn', 20103, 20103, 103, 99999, 99999)
    ops.node(70103, 4.15, 0.0, 10.05)
    ops.element('elasticBeamColumn', 70103, 103, 70103, 99999, 99999)
    ops.node(40103, 4.15, 0.15, 9.9)
    ops.element('elasticBeamColumn', 40103, 103, 40103, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10103, 103, 10103, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 3)
    # Central joint node
    ops.node(203, 8.3, 0.0, 9.9, '-mass', 8.477876331861683, 8.477876331861683, 8.477876331861683, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50203, 8.15, 0.0, 9.9)
    ops.element('elasticBeamColumn', 50203, 50203, 203, 99999, 88888)
    ops.node(30203, 8.45, 0.0, 9.9)
    ops.element('elasticBeamColumn', 30203, 203, 30203, 99999, 88888)
    ops.node(20203, 8.3, 0.0, 9.75)
    ops.element('elasticBeamColumn', 20203, 20203, 203, 99999, 99999)
    ops.node(70203, 8.3, 0.0, 10.05)
    ops.element('elasticBeamColumn', 70203, 203, 70203, 99999, 99999)
    ops.node(40203, 8.3, 0.15, 9.9)
    ops.element('elasticBeamColumn', 40203, 203, 40203, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10203, 203, 10203, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 3)
    # Central joint node
    ops.node(303, 11.25, 0.0, 9.9, '-mass', 8.477876331861683, 8.477876331861683, 8.477876331861683, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50303, 11.1, 0.0, 9.9)
    ops.element('elasticBeamColumn', 50303, 50303, 303, 99999, 88888)
    ops.node(30303, 11.4, 0.0, 9.9)
    ops.element('elasticBeamColumn', 30303, 303, 30303, 99999, 88888)
    ops.node(20303, 11.25, 0.0, 9.75)
    ops.element('elasticBeamColumn', 20303, 20303, 303, 99999, 99999)
    ops.node(70303, 11.25, 0.0, 10.05)
    ops.element('elasticBeamColumn', 70303, 303, 70303, 99999, 99999)
    ops.node(40303, 11.25, 0.15, 9.9)
    ops.element('elasticBeamColumn', 40303, 303, 40303, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10303, 303, 10303, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 3)
    # Central joint node
    ops.node(403, 15.4, 0.0, 9.9, '-mass', 11.642297006231013, 11.642297006231013, 11.642297006231013, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50403, 15.25, 0.0, 9.9)
    ops.element('elasticBeamColumn', 50403, 50403, 403, 99999, 88888)
    ops.node(30403, 15.55, 0.0, 9.9)
    ops.element('elasticBeamColumn', 30403, 403, 30403, 99999, 88888)
    ops.node(20403, 15.4, 0.0, 9.75)
    ops.element('elasticBeamColumn', 20403, 20403, 403, 99999, 99999)
    ops.node(70403, 15.4, 0.0, 10.05)
    ops.element('elasticBeamColumn', 70403, 403, 70403, 99999, 99999)
    ops.node(40403, 15.4, 0.15, 9.9)
    ops.element('elasticBeamColumn', 40403, 403, 40403, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10403, 403, 10403, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 3)
    # Central joint node
    ops.node(503, 19.55, 0.0, 9.9, '-mass', 8.300601867029881, 8.300601867029881, 8.300601867029881, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50503, 19.4, 0.0, 9.9)
    ops.element('elasticBeamColumn', 50503, 50503, 503, 99999, 88888)
    ops.node(20503, 19.55, 0.0, 9.675)
    ops.element('elasticBeamColumn', 20503, 20503, 503, 99999, 99999)
    ops.node(70503, 19.55, 0.0, 10.125)
    ops.element('elasticBeamColumn', 70503, 503, 70503, 99999, 99999)
    ops.node(40503, 19.55, 0.15, 9.9)
    ops.element('elasticBeamColumn', 40503, 503, 40503, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10503, 503, 10503, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 3)
    # Central joint node
    ops.node(13, 0.0, 5.25, 9.9, '-mass', 12.868405568922142, 12.868405568922142, 12.868405568922142, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(30013, 0.175, 5.25, 9.9)
    ops.element('elasticBeamColumn', 30013, 13, 30013, 99999, 88888)
    ops.node(20013, 0.0, 5.25, 9.675)
    ops.element('elasticBeamColumn', 20013, 20013, 13, 99999, 99999)
    ops.node(70013, 0.0, 5.25, 10.125)
    ops.element('elasticBeamColumn', 70013, 13, 70013, 99999, 99999)
    ops.node(60013, 0.0, 5.075, 9.9)
    ops.element('elasticBeamColumn', 60013, 60013, 13, 99999, 77777)
    ops.node(40013, 0.0, 5.425, 9.9)
    ops.element('elasticBeamColumn', 40013, 13, 40013, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10013, 13, 10013, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 3)
    # Central joint node
    ops.node(113, 4.15, 5.25, 9.9, '-mass', 16.27325354355275, 16.27325354355275, 16.27325354355275, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50113, 3.975, 5.25, 9.9)
    ops.element('elasticBeamColumn', 50113, 50113, 113, 99999, 88888)
    ops.node(30113, 4.325, 5.25, 9.9)
    ops.element('elasticBeamColumn', 30113, 113, 30113, 99999, 88888)
    ops.node(20113, 4.15, 5.25, 9.75)
    ops.element('elasticBeamColumn', 20113, 20113, 113, 99999, 99999)
    ops.node(70113, 4.15, 5.25, 10.05)
    ops.element('elasticBeamColumn', 70113, 113, 70113, 99999, 99999)
    ops.node(60113, 4.15, 5.075, 9.9)
    ops.element('elasticBeamColumn', 60113, 60113, 113, 99999, 77777)
    ops.node(40113, 4.15, 5.425, 9.9)
    ops.element('elasticBeamColumn', 40113, 113, 40113, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10113, 113, 10113, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 3)
    # Central joint node
    ops.node(213, 8.3, 5.25, 9.9, '-mass', 16.460403353744663, 16.460403353744663, 16.460403353744663, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50213, 8.125, 5.25, 9.9)
    ops.element('elasticBeamColumn', 50213, 50213, 213, 99999, 88888)
    ops.node(30213, 8.475, 5.25, 9.9)
    ops.element('elasticBeamColumn', 30213, 213, 30213, 99999, 88888)
    ops.node(20213, 8.3, 5.25, 9.75)
    ops.element('elasticBeamColumn', 20213, 20213, 213, 99999, 99999)
    ops.node(70213, 8.3, 5.25, 10.05)
    ops.element('elasticBeamColumn', 70213, 213, 70213, 99999, 99999)
    ops.node(60213, 8.3, 5.075, 9.9)
    ops.element('elasticBeamColumn', 60213, 60213, 213, 99999, 77777)
    ops.node(40213, 8.3, 5.425, 9.9)
    ops.element('elasticBeamColumn', 40213, 213, 40213, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10213, 213, 10213, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 3)
    # Central joint node
    ops.node(313, 11.25, 5.25, 9.9, '-mass', 16.460403353744663, 16.460403353744663, 16.460403353744663, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50313, 11.075, 5.25, 9.9)
    ops.element('elasticBeamColumn', 50313, 50313, 313, 99999, 88888)
    ops.node(30313, 11.425, 5.25, 9.9)
    ops.element('elasticBeamColumn', 30313, 313, 30313, 99999, 88888)
    ops.node(20313, 11.25, 5.25, 9.75)
    ops.element('elasticBeamColumn', 20313, 20313, 313, 99999, 99999)
    ops.node(70313, 11.25, 5.25, 10.05)
    ops.element('elasticBeamColumn', 70313, 313, 70313, 99999, 99999)
    ops.node(60313, 11.25, 5.075, 9.9)
    ops.element('elasticBeamColumn', 60313, 60313, 313, 99999, 77777)
    ops.node(40313, 11.25, 5.425, 9.9)
    ops.element('elasticBeamColumn', 40313, 313, 40313, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10313, 313, 10313, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 3)
    # Central joint node
    ops.node(413, 15.4, 5.25, 9.9, '-mass', 16.27325354355275, 16.27325354355275, 16.27325354355275, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50413, 15.225, 5.25, 9.9)
    ops.element('elasticBeamColumn', 50413, 50413, 413, 99999, 88888)
    ops.node(30413, 15.575, 5.25, 9.9)
    ops.element('elasticBeamColumn', 30413, 413, 30413, 99999, 88888)
    ops.node(20413, 15.4, 5.25, 9.75)
    ops.element('elasticBeamColumn', 20413, 20413, 413, 99999, 99999)
    ops.node(70413, 15.4, 5.25, 10.05)
    ops.element('elasticBeamColumn', 70413, 413, 70413, 99999, 99999)
    ops.node(60413, 15.4, 5.075, 9.9)
    ops.element('elasticBeamColumn', 60413, 60413, 413, 99999, 77777)
    ops.node(40413, 15.4, 5.425, 9.9)
    ops.element('elasticBeamColumn', 40413, 413, 40413, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10413, 413, 10413, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 3)
    # Central joint node
    ops.node(513, 19.55, 5.25, 9.9, '-mass', 12.868405568922142, 12.868405568922142, 12.868405568922142, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50513, 19.375, 5.25, 9.9)
    ops.element('elasticBeamColumn', 50513, 50513, 513, 99999, 88888)
    ops.node(20513, 19.55, 5.25, 9.675)
    ops.element('elasticBeamColumn', 20513, 20513, 513, 99999, 99999)
    ops.node(70513, 19.55, 5.25, 10.125)
    ops.element('elasticBeamColumn', 70513, 513, 70513, 99999, 99999)
    ops.node(60513, 19.55, 5.075, 9.9)
    ops.element('elasticBeamColumn', 60513, 60513, 513, 99999, 77777)
    ops.node(40513, 19.55, 5.425, 9.9)
    ops.element('elasticBeamColumn', 40513, 513, 40513, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10513, 513, 10513, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 3)
    # Central joint node
    ops.node(23, 0.0, 10.5, 9.9, '-mass', 8.300601867029881, 8.300601867029881, 8.300601867029881, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(30023, 0.15, 10.5, 9.9)
    ops.element('elasticBeamColumn', 30023, 23, 30023, 99999, 88888)
    ops.node(20023, 0.0, 10.5, 9.675)
    ops.element('elasticBeamColumn', 20023, 20023, 23, 99999, 99999)
    ops.node(70023, 0.0, 10.5, 10.125)
    ops.element('elasticBeamColumn', 70023, 23, 70023, 99999, 99999)
    ops.node(60023, 0.0, 10.35, 9.9)
    ops.element('elasticBeamColumn', 60023, 60023, 23, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10023, 23, 10023, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 3)
    # Central joint node
    ops.node(123, 4.15, 10.5, 9.9, '-mass', 11.642297006231013, 11.642297006231013, 11.642297006231013, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50123, 4.0, 10.5, 9.9)
    ops.element('elasticBeamColumn', 50123, 50123, 123, 99999, 88888)
    ops.node(30123, 4.3, 10.5, 9.9)
    ops.element('elasticBeamColumn', 30123, 123, 30123, 99999, 88888)
    ops.node(20123, 4.15, 10.5, 9.75)
    ops.element('elasticBeamColumn', 20123, 20123, 123, 99999, 99999)
    ops.node(70123, 4.15, 10.5, 10.05)
    ops.element('elasticBeamColumn', 70123, 123, 70123, 99999, 99999)
    ops.node(60123, 4.15, 10.35, 9.9)
    ops.element('elasticBeamColumn', 60123, 60123, 123, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10123, 123, 10123, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 3)
    # Central joint node
    ops.node(223, 8.3, 10.5, 9.9, '-mass', 10.013187699762694, 10.013187699762694, 10.013187699762694, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50223, 8.15, 10.5, 9.9)
    ops.element('elasticBeamColumn', 50223, 50223, 223, 99999, 88888)
    ops.node(30223, 8.45, 10.5, 9.9)
    ops.element('elasticBeamColumn', 30223, 223, 30223, 99999, 88888)
    ops.node(20223, 8.3, 10.5, 9.75)
    ops.element('elasticBeamColumn', 20223, 20223, 223, 99999, 99999)
    ops.node(70223, 8.3, 10.5, 10.05)
    ops.element('elasticBeamColumn', 70223, 223, 70223, 99999, 99999)
    ops.node(60223, 8.3, 10.35, 9.9)
    ops.element('elasticBeamColumn', 60223, 60223, 223, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10223, 223, 10223, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 3)
    # Central joint node
    ops.node(323, 11.25, 10.5, 9.9, '-mass', 10.013187699762694, 10.013187699762694, 10.013187699762694, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50323, 11.1, 10.5, 9.9)
    ops.element('elasticBeamColumn', 50323, 50323, 323, 99999, 88888)
    ops.node(30323, 11.4, 10.5, 9.9)
    ops.element('elasticBeamColumn', 30323, 323, 30323, 99999, 88888)
    ops.node(20323, 11.25, 10.5, 9.75)
    ops.element('elasticBeamColumn', 20323, 20323, 323, 99999, 99999)
    ops.node(70323, 11.25, 10.5, 10.05)
    ops.element('elasticBeamColumn', 70323, 323, 70323, 99999, 99999)
    ops.node(60323, 11.25, 10.35, 9.9)
    ops.element('elasticBeamColumn', 60323, 60323, 323, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10323, 323, 10323, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 3)
    # Central joint node
    ops.node(423, 15.4, 10.5, 9.9, '-mass', 11.642297006231013, 11.642297006231013, 11.642297006231013, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50423, 15.25, 10.5, 9.9)
    ops.element('elasticBeamColumn', 50423, 50423, 423, 99999, 88888)
    ops.node(30423, 15.55, 10.5, 9.9)
    ops.element('elasticBeamColumn', 30423, 423, 30423, 99999, 88888)
    ops.node(20423, 15.4, 10.5, 9.75)
    ops.element('elasticBeamColumn', 20423, 20423, 423, 99999, 99999)
    ops.node(70423, 15.4, 10.5, 10.05)
    ops.element('elasticBeamColumn', 70423, 423, 70423, 99999, 99999)
    ops.node(60423, 15.4, 10.35, 9.9)
    ops.element('elasticBeamColumn', 60423, 60423, 423, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10423, 423, 10423, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 3)
    # Central joint node
    ops.node(523, 19.55, 10.5, 9.9, '-mass', 8.300601867029881, 8.300601867029881, 8.300601867029881, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50523, 19.4, 10.5, 9.9)
    ops.element('elasticBeamColumn', 50523, 50523, 523, 99999, 88888)
    ops.node(20523, 19.55, 10.5, 9.675)
    ops.element('elasticBeamColumn', 20523, 20523, 523, 99999, 99999)
    ops.node(70523, 19.55, 10.5, 10.125)
    ops.element('elasticBeamColumn', 70523, 523, 70523, 99999, 99999)
    ops.node(60523, 19.55, 10.35, 9.9)
    ops.element('elasticBeamColumn', 60523, 60523, 523, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10523, 523, 10523, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 4)
    # Central joint node
    ops.node(4, 0.0, 0.0, 13.0, '-mass', 4.258234384868819, 4.258234384868819, 4.258234384868819, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(30004, 0.15, 0.0, 13.0)
    ops.element('elasticBeamColumn', 30004, 4, 30004, 99999, 88888)
    ops.node(20004, 0.0, 0.0, 12.775)
    ops.element('elasticBeamColumn', 20004, 20004, 4, 99999, 99999)
    ops.node(40004, 0.0, 0.15, 13.0)
    ops.element('elasticBeamColumn', 40004, 4, 40004, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10004, 4, 10004, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 4)
    # Central joint node
    ops.node(104, 4.15, 0.0, 13.0, '-mass', 7.492003937933359, 7.492003937933359, 7.492003937933359, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50104, 4.0, 0.0, 13.0)
    ops.element('elasticBeamColumn', 50104, 50104, 104, 99999, 88888)
    ops.node(30104, 4.3, 0.0, 13.0)
    ops.element('elasticBeamColumn', 30104, 104, 30104, 99999, 88888)
    ops.node(20104, 4.15, 0.0, 12.85)
    ops.element('elasticBeamColumn', 20104, 20104, 104, 99999, 99999)
    ops.node(40104, 4.15, 0.15, 13.0)
    ops.element('elasticBeamColumn', 40104, 104, 40104, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10104, 104, 10104, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 4)
    # Central joint node
    ops.node(204, 8.3, 0.0, 13.0, '-mass', 4.278781020954446, 4.278781020954446, 4.278781020954446, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50204, 8.15, 0.0, 13.0)
    ops.element('elasticBeamColumn', 50204, 50204, 204, 99999, 88888)
    ops.node(30204, 8.45, 0.0, 13.0)
    ops.element('elasticBeamColumn', 30204, 204, 30204, 99999, 88888)
    ops.node(20204, 8.3, 0.0, 12.85)
    ops.element('elasticBeamColumn', 20204, 20204, 204, 99999, 99999)
    ops.node(40204, 8.3, 0.15, 13.0)
    ops.element('elasticBeamColumn', 40204, 204, 40204, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10204, 204, 10204, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 4)
    # Central joint node
    ops.node(304, 11.25, 0.0, 13.0, '-mass', 4.278781020954446, 4.278781020954446, 4.278781020954446, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50304, 11.1, 0.0, 13.0)
    ops.element('elasticBeamColumn', 50304, 50304, 304, 99999, 88888)
    ops.node(30304, 11.4, 0.0, 13.0)
    ops.element('elasticBeamColumn', 30304, 304, 30304, 99999, 88888)
    ops.node(20304, 11.25, 0.0, 12.85)
    ops.element('elasticBeamColumn', 20304, 20304, 304, 99999, 99999)
    ops.node(40304, 11.25, 0.15, 13.0)
    ops.element('elasticBeamColumn', 40304, 304, 40304, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10304, 304, 10304, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 4)
    # Central joint node
    ops.node(404, 15.4, 0.0, 13.0, '-mass', 7.492003937933359, 7.492003937933359, 7.492003937933359, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50404, 15.25, 0.0, 13.0)
    ops.element('elasticBeamColumn', 50404, 50404, 404, 99999, 88888)
    ops.node(30404, 15.55, 0.0, 13.0)
    ops.element('elasticBeamColumn', 30404, 404, 30404, 99999, 88888)
    ops.node(20404, 15.4, 0.0, 12.85)
    ops.element('elasticBeamColumn', 20404, 20404, 404, 99999, 99999)
    ops.node(40404, 15.4, 0.15, 13.0)
    ops.element('elasticBeamColumn', 40404, 404, 40404, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10404, 404, 10404, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 4)
    # Central joint node
    ops.node(504, 19.55, 0.0, 13.0, '-mass', 4.258234384868819, 4.258234384868819, 4.258234384868819, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50504, 19.4, 0.0, 13.0)
    ops.element('elasticBeamColumn', 50504, 50504, 504, 99999, 88888)
    ops.node(20504, 19.55, 0.0, 12.775)
    ops.element('elasticBeamColumn', 20504, 20504, 504, 99999, 99999)
    ops.node(40504, 19.55, 0.15, 13.0)
    ops.element('elasticBeamColumn', 40504, 504, 40504, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10504, 504, 10504, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 4)
    # Central joint node
    ops.node(14, 0.0, 5.25, 13.0, '-mass', 7.972062551592888, 7.972062551592888, 7.972062551592888, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(30014, 0.175, 5.25, 13.0)
    ops.element('elasticBeamColumn', 30014, 14, 30014, 99999, 88888)
    ops.node(20014, 0.0, 5.25, 12.775)
    ops.element('elasticBeamColumn', 20014, 20014, 14, 99999, 99999)
    ops.node(60014, 0.0, 5.075, 13.0)
    ops.element('elasticBeamColumn', 60014, 60014, 14, 99999, 77777)
    ops.node(40014, 0.0, 5.425, 13.0)
    ops.element('elasticBeamColumn', 40014, 14, 40014, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10014, 14, 10014, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 4)
    # Central joint node
    ops.node(114, 4.15, 5.25, 13.0, '-mass', 14.122323370260194, 14.122323370260194, 14.122323370260194, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50114, 3.975, 5.25, 13.0)
    ops.element('elasticBeamColumn', 50114, 50114, 114, 99999, 88888)
    ops.node(30114, 4.325, 5.25, 13.0)
    ops.element('elasticBeamColumn', 30114, 114, 30114, 99999, 88888)
    ops.node(20114, 4.15, 5.25, 12.85)
    ops.element('elasticBeamColumn', 20114, 20114, 114, 99999, 99999)
    ops.node(60114, 4.15, 5.075, 13.0)
    ops.element('elasticBeamColumn', 60114, 60114, 114, 99999, 77777)
    ops.node(40114, 4.15, 5.425, 13.0)
    ops.element('elasticBeamColumn', 40114, 114, 40114, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10114, 114, 10114, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 4)
    # Central joint node
    ops.node(214, 8.3, 5.25, 13.0, '-mass', 12.531376850176876, 12.531376850176876, 12.531376850176876, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50214, 8.125, 5.25, 13.0)
    ops.element('elasticBeamColumn', 50214, 50214, 214, 99999, 88888)
    ops.node(30214, 8.475, 5.25, 13.0)
    ops.element('elasticBeamColumn', 30214, 214, 30214, 99999, 88888)
    ops.node(20214, 8.3, 5.25, 12.85)
    ops.element('elasticBeamColumn', 20214, 20214, 214, 99999, 99999)
    ops.node(60214, 8.3, 5.075, 13.0)
    ops.element('elasticBeamColumn', 60214, 60214, 214, 99999, 77777)
    ops.node(40214, 8.3, 5.425, 13.0)
    ops.element('elasticBeamColumn', 40214, 214, 40214, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10214, 214, 10214, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 4)
    # Central joint node
    ops.node(314, 11.25, 5.25, 13.0, '-mass', 12.531376850176876, 12.531376850176876, 12.531376850176876, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50314, 11.075, 5.25, 13.0)
    ops.element('elasticBeamColumn', 50314, 50314, 314, 99999, 88888)
    ops.node(30314, 11.425, 5.25, 13.0)
    ops.element('elasticBeamColumn', 30314, 314, 30314, 99999, 88888)
    ops.node(20314, 11.25, 5.25, 12.85)
    ops.element('elasticBeamColumn', 20314, 20314, 314, 99999, 99999)
    ops.node(60314, 11.25, 5.075, 13.0)
    ops.element('elasticBeamColumn', 60314, 60314, 314, 99999, 77777)
    ops.node(40314, 11.25, 5.425, 13.0)
    ops.element('elasticBeamColumn', 40314, 314, 40314, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10314, 314, 10314, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 4)
    # Central joint node
    ops.node(414, 15.4, 5.25, 13.0, '-mass', 14.122323370260194, 14.122323370260194, 14.122323370260194, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50414, 15.225, 5.25, 13.0)
    ops.element('elasticBeamColumn', 50414, 50414, 414, 99999, 88888)
    ops.node(30414, 15.575, 5.25, 13.0)
    ops.element('elasticBeamColumn', 30414, 414, 30414, 99999, 88888)
    ops.node(20414, 15.4, 5.25, 12.85)
    ops.element('elasticBeamColumn', 20414, 20414, 414, 99999, 99999)
    ops.node(60414, 15.4, 5.075, 13.0)
    ops.element('elasticBeamColumn', 60414, 60414, 414, 99999, 77777)
    ops.node(40414, 15.4, 5.425, 13.0)
    ops.element('elasticBeamColumn', 40414, 414, 40414, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10414, 414, 10414, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 4)
    # Central joint node
    ops.node(514, 19.55, 5.25, 13.0, '-mass', 7.972062551592888, 7.972062551592888, 7.972062551592888, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50514, 19.375, 5.25, 13.0)
    ops.element('elasticBeamColumn', 50514, 50514, 514, 99999, 88888)
    ops.node(20514, 19.55, 5.25, 12.775)
    ops.element('elasticBeamColumn', 20514, 20514, 514, 99999, 99999)
    ops.node(60514, 19.55, 5.075, 13.0)
    ops.element('elasticBeamColumn', 60514, 60514, 514, 99999, 77777)
    ops.node(40514, 19.55, 5.425, 13.0)
    ops.element('elasticBeamColumn', 40514, 514, 40514, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10514, 514, 10514, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 4)
    # Central joint node
    ops.node(24, 0.0, 10.5, 13.0, '-mass', 4.258234384868819, 4.258234384868819, 4.258234384868819, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(30024, 0.15, 10.5, 13.0)
    ops.element('elasticBeamColumn', 30024, 24, 30024, 99999, 88888)
    ops.node(20024, 0.0, 10.5, 12.775)
    ops.element('elasticBeamColumn', 20024, 20024, 24, 99999, 99999)
    ops.node(60024, 0.0, 10.35, 13.0)
    ops.element('elasticBeamColumn', 60024, 60024, 24, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10024, 24, 10024, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 4)
    # Central joint node
    ops.node(124, 4.15, 10.5, 13.0, '-mass', 7.492003937933359, 7.492003937933359, 7.492003937933359, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50124, 4.0, 10.5, 13.0)
    ops.element('elasticBeamColumn', 50124, 50124, 124, 99999, 88888)
    ops.node(30124, 4.3, 10.5, 13.0)
    ops.element('elasticBeamColumn', 30124, 124, 30124, 99999, 88888)
    ops.node(20124, 4.15, 10.5, 12.85)
    ops.element('elasticBeamColumn', 20124, 20124, 124, 99999, 99999)
    ops.node(60124, 4.15, 10.35, 13.0)
    ops.element('elasticBeamColumn', 60124, 60124, 124, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10124, 124, 10124, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 4)
    # Central joint node
    ops.node(224, 8.3, 10.5, 13.0, '-mass', 6.220119402107242, 6.220119402107242, 6.220119402107242, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50224, 8.15, 10.5, 13.0)
    ops.element('elasticBeamColumn', 50224, 50224, 224, 99999, 88888)
    ops.node(30224, 8.45, 10.5, 13.0)
    ops.element('elasticBeamColumn', 30224, 224, 30224, 99999, 88888)
    ops.node(20224, 8.3, 10.5, 12.85)
    ops.element('elasticBeamColumn', 20224, 20224, 224, 99999, 99999)
    ops.node(60224, 8.3, 10.35, 13.0)
    ops.element('elasticBeamColumn', 60224, 60224, 224, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10224, 224, 10224, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 4)
    # Central joint node
    ops.node(324, 11.25, 10.5, 13.0, '-mass', 6.220119402107242, 6.220119402107242, 6.220119402107242, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50324, 11.1, 10.5, 13.0)
    ops.element('elasticBeamColumn', 50324, 50324, 324, 99999, 88888)
    ops.node(30324, 11.4, 10.5, 13.0)
    ops.element('elasticBeamColumn', 30324, 324, 30324, 99999, 88888)
    ops.node(20324, 11.25, 10.5, 12.85)
    ops.element('elasticBeamColumn', 20324, 20324, 324, 99999, 99999)
    ops.node(60324, 11.25, 10.35, 13.0)
    ops.element('elasticBeamColumn', 60324, 60324, 324, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10324, 324, 10324, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 4)
    # Central joint node
    ops.node(424, 15.4, 10.5, 13.0, '-mass', 7.492003937933359, 7.492003937933359, 7.492003937933359, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50424, 15.25, 10.5, 13.0)
    ops.element('elasticBeamColumn', 50424, 50424, 424, 99999, 88888)
    ops.node(30424, 15.55, 10.5, 13.0)
    ops.element('elasticBeamColumn', 30424, 424, 30424, 99999, 88888)
    ops.node(20424, 15.4, 10.5, 12.85)
    ops.element('elasticBeamColumn', 20424, 20424, 424, 99999, 99999)
    ops.node(60424, 15.4, 10.35, 13.0)
    ops.element('elasticBeamColumn', 60424, 60424, 424, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10424, 424, 10424, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 4)
    # Central joint node
    ops.node(524, 19.55, 10.5, 13.0, '-mass', 4.258234384868819, 4.258234384868819, 4.258234384868819, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(50524, 19.4, 10.5, 13.0)
    ops.element('elasticBeamColumn', 50524, 50524, 524, 99999, 88888)
    ops.node(20524, 19.55, 10.5, 12.775)
    ops.element('elasticBeamColumn', 20524, 20524, 524, 99999, 99999)
    ops.node(60524, 19.55, 10.35, 13.0)
    ops.element('elasticBeamColumn', 60524, 60524, 524, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 10524, 524, 10524, 99999, '-orient', 0, 0, 1, 0, 1, 0)
