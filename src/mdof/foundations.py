import openseespy.opensees as ops


def add_foundations() -> None:
    """Add foundation components to ops domain (nodes and constraints).
    """
    # Foundation or support under the column 3000
    # Fixed node
    ops.node(0, 0.0, 0.0, 0.0)
    ops.fix(0, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70000, 0.0, 0.0, 0.0, '-mass', 0.4243119266055046, 0.4243119266055046, 0.4243119266055046, 0.0, 0.0, 0.0)
    ops.equalDOF(0, 70000, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3010
    # Fixed node
    ops.node(10, 0.0, 5.25, 0.0)
    ops.fix(10, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70010, 0.0, 5.25, 0.0, '-mass', 0.5775356778797145, 0.5775356778797145, 0.5775356778797145, 0.0, 0.0, 0.0)
    ops.equalDOF(10, 70010, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3020
    # Fixed node
    ops.node(20, 0.0, 10.5, 0.0)
    ops.fix(20, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70020, 0.0, 10.5, 0.0, '-mass', 0.4243119266055046, 0.4243119266055046, 0.4243119266055046, 0.0, 0.0, 0.0)
    ops.equalDOF(20, 70020, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3100
    # Fixed node
    ops.node(100, 4.15, 0.0, 0.0)
    ops.fix(100, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70100, 4.15, 0.0, 0.0, '-mass', 0.4243119266055046, 0.4243119266055046, 0.4243119266055046, 0.0, 0.0, 0.0)
    ops.equalDOF(100, 70100, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3110
    # Fixed node
    ops.node(110, 4.15, 5.25, 0.0)
    ops.fix(110, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70110, 4.15, 5.25, 0.0, '-mass', 0.5775356778797145, 0.5775356778797145, 0.5775356778797145, 0.0, 0.0, 0.0)
    ops.equalDOF(110, 70110, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3120
    # Fixed node
    ops.node(120, 4.15, 10.5, 0.0)
    ops.fix(120, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70120, 4.15, 10.5, 0.0, '-mass', 0.4243119266055046, 0.4243119266055046, 0.4243119266055046, 0.0, 0.0, 0.0)
    ops.equalDOF(120, 70120, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4200
    # Fixed node
    ops.node(200, 8.3, 0.0, 0.0)
    ops.fix(200, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70200, 8.3, 0.0, 0.0, '-mass', 0.2121559633027523, 0.2121559633027523, 0.2121559633027523, 0.0, 0.0, 0.0)
    ops.equalDOF(200, 70200, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3210
    # Fixed node
    ops.node(210, 8.3, 5.25, 0.0)
    ops.fix(210, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70210, 8.3, 5.25, 0.0, '-mass', 0.5775356778797145, 0.5775356778797145, 0.5775356778797145, 0.0, 0.0, 0.0)
    ops.equalDOF(210, 70210, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3220
    # Fixed node
    ops.node(220, 8.3, 10.5, 0.0)
    ops.fix(220, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70220, 8.3, 10.5, 0.0, '-mass', 0.4243119266055046, 0.4243119266055046, 0.4243119266055046, 0.0, 0.0, 0.0)
    ops.equalDOF(220, 70220, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4300
    # Fixed node
    ops.node(300, 11.25, 0.0, 0.0)
    ops.fix(300, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70300, 11.25, 0.0, 0.0, '-mass', 0.2121559633027523, 0.2121559633027523, 0.2121559633027523, 0.0, 0.0, 0.0)
    ops.equalDOF(300, 70300, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3310
    # Fixed node
    ops.node(310, 11.25, 5.25, 0.0)
    ops.fix(310, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70310, 11.25, 5.25, 0.0, '-mass', 0.5775356778797145, 0.5775356778797145, 0.5775356778797145, 0.0, 0.0, 0.0)
    ops.equalDOF(310, 70310, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3320
    # Fixed node
    ops.node(320, 11.25, 10.5, 0.0)
    ops.fix(320, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70320, 11.25, 10.5, 0.0, '-mass', 0.4243119266055046, 0.4243119266055046, 0.4243119266055046, 0.0, 0.0, 0.0)
    ops.equalDOF(320, 70320, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3400
    # Fixed node
    ops.node(400, 15.4, 0.0, 0.0)
    ops.fix(400, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70400, 15.4, 0.0, 0.0, '-mass', 0.4243119266055046, 0.4243119266055046, 0.4243119266055046, 0.0, 0.0, 0.0)
    ops.equalDOF(400, 70400, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3410
    # Fixed node
    ops.node(410, 15.4, 5.25, 0.0)
    ops.fix(410, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70410, 15.4, 5.25, 0.0, '-mass', 0.5775356778797145, 0.5775356778797145, 0.5775356778797145, 0.0, 0.0, 0.0)
    ops.equalDOF(410, 70410, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3420
    # Fixed node
    ops.node(420, 15.4, 10.5, 0.0)
    ops.fix(420, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70420, 15.4, 10.5, 0.0, '-mass', 0.4243119266055046, 0.4243119266055046, 0.4243119266055046, 0.0, 0.0, 0.0)
    ops.equalDOF(420, 70420, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3500
    # Fixed node
    ops.node(500, 19.55, 0.0, 0.0)
    ops.fix(500, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70500, 19.55, 0.0, 0.0, '-mass', 0.4243119266055046, 0.4243119266055046, 0.4243119266055046, 0.0, 0.0, 0.0)
    ops.equalDOF(500, 70500, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3510
    # Fixed node
    ops.node(510, 19.55, 5.25, 0.0)
    ops.fix(510, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70510, 19.55, 5.25, 0.0, '-mass', 0.5775356778797145, 0.5775356778797145, 0.5775356778797145, 0.0, 0.0, 0.0)
    ops.equalDOF(510, 70510, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3520
    # Fixed node
    ops.node(520, 19.55, 10.5, 0.0)
    ops.fix(520, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70520, 19.55, 10.5, 0.0, '-mass', 0.4243119266055046, 0.4243119266055046, 0.4243119266055046, 0.0, 0.0, 0.0)
    ops.equalDOF(520, 70520, 1, 2, 3, 4, 5, 6)
