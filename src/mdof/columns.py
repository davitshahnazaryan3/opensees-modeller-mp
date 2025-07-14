import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170000, 0.0, 0.0, 0.0)
    ops.node(120001, 0.0, 0.0, 3.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3000, 170000, 120001, 0.09, 29549137.33101903, 12312140.55459126, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23000, 127.73126266, 0.00201044, 152.76120407, 0.04160444, 15.27612041, 0.1303158, -127.73126266, -0.00201044, -152.76120407, -0.04160444, -15.27612041, -0.1303158, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13000, 127.73126266, 0.00201044, 152.76120407, 0.04160444, 15.27612041, 0.1303158, -127.73126266, -0.00201044, -152.76120407, -0.04160444, -15.27612041, -0.1303158, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3000, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23000, 'My', 13000, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170000, 70000, 170000, 3000, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120001, 120001, 20001, 3000, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170100, 4.15, 0.0, 0.0)
    ops.node(120101, 4.15, 0.0, 3.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3100, 170100, 120101, 0.09, 31441526.12307622, 13100635.88461509, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23100, 147.60004465, 0.0020127, 174.86929763, 0.03882717, 17.48692976, 0.12020035, -147.60004465, -0.0020127, -174.86929763, -0.03882717, -17.48692976, -0.12020035, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13100, 147.60004465, 0.0020127, 174.86929763, 0.03882717, 17.48692976, 0.12020035, -147.60004465, -0.0020127, -174.86929763, -0.03882717, -17.48692976, -0.12020035, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3100, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23100, 'My', 13100, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170100, 70100, 170100, 3100, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120101, 120101, 20101, 3100, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170400, 15.4, 0.0, 0.0)
    ops.node(120401, 15.4, 0.0, 3.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3400, 170400, 120401, 0.09, 31171370.52145547, 12988071.05060645, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23400, 149.8877382, 0.00198994, 177.61866679, 0.03873121, 17.76186668, 0.1188522, -149.8877382, -0.00198994, -177.61866679, -0.03873121, -17.76186668, -0.1188522, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13400, 149.8877382, 0.00198994, 177.61866679, 0.03873121, 17.76186668, 0.1188522, -149.8877382, -0.00198994, -177.61866679, -0.03873121, -17.76186668, -0.1188522, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3400, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23400, 'My', 13400, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170400, 70400, 170400, 3400, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120401, 120401, 20401, 3400, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170500, 19.55, 0.0, 0.0)
    ops.node(120501, 19.55, 0.0, 3.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3500, 170500, 120501, 0.09, 31135749.74835729, 12973229.06181554, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23500, 133.4848676, 0.00191057, 159.36072188, 0.04260178, 15.93607219, 0.141324, -133.4848676, -0.00191057, -159.36072188, -0.04260178, -15.93607219, -0.141324, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13500, 133.4848676, 0.00191057, 159.36072188, 0.04260178, 15.93607219, 0.141324, -133.4848676, -0.00191057, -159.36072188, -0.04260178, -15.93607219, -0.141324, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3500, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23500, 'My', 13500, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170500, 70500, 170500, 3500, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120501, 120501, 20501, 3500, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 0.0, 5.25, 0.0)
    ops.node(120011, 0.0, 5.25, 3.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 170010, 120011, 0.1225, 30914198.70810824, 12880916.12837843, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 238.83154976, 0.00176147, 284.39071572, 0.03598855, 28.43907157, 0.11715825, -238.83154976, -0.00176147, -284.39071572, -0.03598855, -28.43907157, -0.11715825, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 281.02284421, 0.00176147, 334.63036135, 0.03598855, 33.46303614, 0.11715825, -281.02284421, -0.00176147, -334.63036135, -0.03598855, -33.46303614, -0.11715825, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120011, 120011, 20011, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170110, 4.15, 5.25, 0.0)
    ops.node(120111, 4.15, 5.25, 3.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3110, 170110, 120111, 0.1225, 30558146.77667942, 12732561.15694976, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23110, 257.83898751, 0.00188275, 306.05342878, 0.03715438, 30.60534288, 0.10839233, -257.83898751, -0.00188275, -306.05342878, -0.03715438, -30.60534288, -0.10839233, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13110, 257.83898751, 0.00188275, 306.05342878, 0.03715438, 30.60534288, 0.10839233, -257.83898751, -0.00188275, -306.05342878, -0.03715438, -30.60534288, -0.10839233, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3110, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23110, 'My', 13110, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170110, 70110, 170110, 3110, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120111, 120111, 20111, 3110, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170210, 8.3, 5.25, 0.0)
    ops.node(120211, 8.3, 5.25, 3.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3210, 170210, 120211, 0.1225, 31610591.77548276, 13171079.90645115, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23210, 201.3257229, 0.00167252, 238.86137225, 0.03231061, 23.88613722, 0.11096811, -201.3257229, -0.00167252, -238.86137225, -0.03231061, -23.88613722, -0.11096811, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13210, 201.3257229, 0.00167252, 238.86137225, 0.03231061, 23.88613722, 0.11096811, -201.3257229, -0.00167252, -238.86137225, -0.03231061, -23.88613722, -0.11096811, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3210, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23210, 'My', 13210, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170210, 70210, 170210, 3210, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120211, 120211, 20211, 3210, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170310, 11.25, 5.25, 0.0)
    ops.node(120311, 11.25, 5.25, 3.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3310, 170310, 120311, 0.1225, 30834168.09717469, 12847570.04048946, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23310, 196.34848008, 0.00175514, 233.1262, 0.03259954, 23.31262, 0.10828774, -196.34848008, -0.00175514, -233.1262, -0.03259954, -23.31262, -0.10828774, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13310, 196.34848008, 0.00175514, 233.1262, 0.03259954, 23.31262, 0.10828774, -196.34848008, -0.00175514, -233.1262, -0.03259954, -23.31262, -0.10828774, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3310, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23310, 'My', 13310, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170310, 70310, 170310, 3310, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120311, 120311, 20311, 3310, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170410, 15.4, 5.25, 0.0)
    ops.node(120411, 15.4, 5.25, 3.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3410, 170410, 120411, 0.1225, 30744531.39287541, 12810221.41369809, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23410, 248.73546169, 0.00192696, 295.21645078, 0.03763964, 29.52164508, 0.11025617, -248.73546169, -0.00192696, -295.21645078, -0.03763964, -29.52164508, -0.11025617, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13410, 248.73546169, 0.00192696, 295.21645078, 0.03763964, 29.52164508, 0.11025617, -248.73546169, -0.00192696, -295.21645078, -0.03763964, -29.52164508, -0.11025617, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3410, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23410, 'My', 13410, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170410, 70410, 170410, 3410, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120411, 120411, 20411, 3410, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170510, 19.55, 5.25, 0.0)
    ops.node(120511, 19.55, 5.25, 3.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3510, 170510, 120511, 0.1225, 31615232.57031474, 13173013.57096447, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23510, 236.67836077, 0.00174032, 281.5764083, 0.03629085, 28.15764083, 0.120833, -236.67836077, -0.00174032, -281.5764083, -0.03629085, -28.15764083, -0.120833, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13510, 277.16114624, 0.00174032, 329.73880596, 0.03629085, 32.9738806, 0.120833, -277.16114624, -0.00174032, -329.73880596, -0.03629085, -32.9738806, -0.120833, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3510, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23510, 'My', 13510, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170510, 70510, 170510, 3510, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120511, 120511, 20511, 3510, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 0.0, 10.5, 0.0)
    ops.node(120021, 0.0, 10.5, 3.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 170020, 120021, 0.09, 31392802.67323792, 13080334.44718247, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 126.90829264, 0.0018884, 151.4482521, 0.04312153, 15.14482521, 0.14312153, -126.90829264, -0.0018884, -151.4482521, -0.04312153, -15.14482521, -0.14312153, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 126.90829264, 0.0018884, 151.4482521, 0.04312153, 15.14482521, 0.14312153, -126.90829264, -0.0018884, -151.4482521, -0.04312153, -15.14482521, -0.14312153, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120021, 120021, 20021, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170120, 4.15, 10.5, 0.0)
    ops.node(120121, 4.15, 10.5, 3.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3120, 170120, 120121, 0.09, 30302653.07040482, 12626105.44600201, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23120, 148.38302719, 0.00205681, 175.9078574, 0.0375735, 17.59078574, 0.1112402, -148.38302719, -0.00205681, -175.9078574, -0.0375735, -17.59078574, -0.1112402, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13120, 148.38302719, 0.00205681, 175.9078574, 0.0375735, 17.59078574, 0.1112402, -148.38302719, -0.00205681, -175.9078574, -0.0375735, -17.59078574, -0.1112402, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3120, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23120, 'My', 13120, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170120, 70120, 170120, 3120, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120121, 120121, 20121, 3120, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170220, 8.3, 10.5, 0.0)
    ops.node(120221, 8.3, 10.5, 3.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3220, 170220, 120221, 0.09, 31356027.21230935, 13065011.33846223, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23220, 140.12685762, 0.0019832, 166.58446306, 0.03993301, 16.65844631, 0.12766186, -140.12685762, -0.0019832, -166.58446306, -0.03993301, -16.65844631, -0.12766186, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13220, 140.12685762, 0.0019832, 166.58446306, 0.03993301, 16.65844631, 0.12766186, -140.12685762, -0.0019832, -166.58446306, -0.03993301, -16.65844631, -0.12766186, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3220, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23220, 'My', 13220, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170220, 70220, 170220, 3220, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120221, 120221, 20221, 3220, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170320, 11.25, 10.5, 0.0)
    ops.node(120321, 11.25, 10.5, 3.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3320, 170320, 120321, 0.09, 30490892.56382168, 12704538.56825903, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23320, 141.13751295, 0.00202893, 167.92595668, 0.03973661, 16.79259567, 0.12332209, -141.13751295, -0.00202893, -167.92595668, -0.03973661, -16.79259567, -0.12332209, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13320, 141.13751295, 0.00202893, 167.92595668, 0.03973661, 16.79259567, 0.12332209, -141.13751295, -0.00202893, -167.92595668, -0.03973661, -16.79259567, -0.12332209, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3320, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23320, 'My', 13320, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170320, 70320, 170320, 3320, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120321, 120321, 20321, 3320, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170420, 15.4, 10.5, 0.0)
    ops.node(120421, 15.4, 10.5, 3.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3420, 170420, 120421, 0.09, 32075593.81419361, 13364830.755914, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23420, 146.98706443, 0.00206687, 174.02490171, 0.03877358, 17.40249017, 0.12302691, -146.98706443, -0.00206687, -174.02490171, -0.03877358, -17.40249017, -0.12302691, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13420, 146.98706443, 0.00206687, 174.02490171, 0.03877358, 17.40249017, 0.12302691, -146.98706443, -0.00206687, -174.02490171, -0.03877358, -17.40249017, -0.12302691, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3420, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23420, 'My', 13420, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170420, 70420, 170420, 3420, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120421, 120421, 20421, 3420, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170520, 19.55, 10.5, 0.0)
    ops.node(120521, 19.55, 10.5, 3.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3520, 170520, 120521, 0.09, 32329959.53314506, 13470816.47214377, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23520, 129.38751852, 0.00194991, 154.14012117, 0.0431782, 15.41401212, 0.1431782, -129.38751852, -0.00194991, -154.14012117, -0.0431782, -15.41401212, -0.1431782, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13520, 129.38751852, 0.00194991, 154.14012117, 0.0431782, 15.41401212, 0.1431782, -129.38751852, -0.00194991, -154.14012117, -0.0431782, -15.41401212, -0.1431782, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3520, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23520, 'My', 13520, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170520, 70520, 170520, 3520, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120521, 120521, 20521, 3520, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 3.925)
    ops.node(120002, 0.0, 0.0, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 170001, 120002, 0.09, 31310448.18327602, 13046020.07636501, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 131.27501569, 0.0018603, 157.3391565, 0.04693756, 15.73391565, 0.14693756, -131.27501569, -0.0018603, -157.3391565, -0.04693756, -15.73391565, -0.14693756, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 140.44418282, 0.0018603, 168.32882589, 0.04693756, 16.83288259, 0.14693756, -140.44418282, -0.0018603, -168.32882589, -0.04693756, -16.83288259, -0.14693756, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120002, 120002, 20002, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170101, 4.15, 0.0, 3.85)
    ops.node(120102, 4.15, 0.0, 6.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3101, 170101, 120102, 0.09, 32299093.1946432, 13457955.497768, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23101, 150.17817385, 0.00179353, 178.69894018, 0.04393651, 17.86989402, 0.14393651, -150.17817385, -0.00179353, -178.69894018, -0.04393651, -17.86989402, -0.14393651, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13101, 161.05983119, 0.00179353, 191.64716417, 0.04393651, 19.16471642, 0.14393651, -161.05983119, -0.00179353, -191.64716417, -0.04393651, -19.16471642, -0.14393651, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3101, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23101, 'My', 13101, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170101, 70101, 170101, 3101, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120102, 120102, 20102, 3101, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170401, 15.4, 0.0, 3.85)
    ops.node(120402, 15.4, 0.0, 6.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3401, 170401, 120402, 0.09, 30028935.70045829, 12512056.54185762, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23401, 147.68649512, 0.00188594, 176.2790408, 0.04355568, 17.62790408, 0.13403555, -147.68649512, -0.00188594, -176.2790408, -0.04355568, -17.62790408, -0.13403555, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13401, 158.33524437, 0.00188594, 188.98941965, 0.04355568, 18.89894196, 0.13403555, -158.33524437, -0.00188594, -188.98941965, -0.04355568, -18.89894196, -0.13403555, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3401, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23401, 'My', 13401, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170401, 70401, 170401, 3401, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120402, 120402, 20402, 3401, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170501, 19.55, 0.0, 3.925)
    ops.node(120502, 19.55, 0.0, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3501, 170501, 120502, 0.09, 31336381.13659529, 13056825.47358137, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23501, 131.25820508, 0.0017453, 157.31067903, 0.04781889, 15.7310679, 0.14781889, -131.25820508, -0.0017453, -157.31067903, -0.04781889, -15.7310679, -0.14781889, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13501, 141.14508231, 0.0017453, 169.15992966, 0.04781889, 16.91599297, 0.14781889, -141.14508231, -0.0017453, -169.15992966, -0.04781889, -16.91599297, -0.14781889, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3501, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23501, 'My', 13501, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170501, 70501, 170501, 3501, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120502, 120502, 20502, 3501, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 0.0, 5.25, 3.925)
    ops.node(120012, 0.0, 5.25, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 170011, 120012, 0.1225, 29935044.88287506, 12472935.36786461, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 219.54015921, 0.00156977, 263.08732952, 0.03931826, 26.30873295, 0.13095585, -219.54015921, -0.00156977, -263.08732952, -0.03931826, -26.30873295, -0.13095585, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 261.90684203, 0.00156977, 313.85771014, 0.03931826, 31.38577101, 0.13095585, -261.90684203, -0.00156977, -313.85771014, -0.03931826, -31.38577101, -0.13095585, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120012, 120012, 20012, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170111, 4.15, 5.25, 3.85)
    ops.node(120112, 4.15, 5.25, 6.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3111, 170111, 120112, 0.1225, 31154246.17458325, 12980935.90607635, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23111, 255.35175141, 0.00168358, 304.57655971, 0.04347107, 30.45765597, 0.13303031, -255.35175141, -0.00168358, -304.57655971, -0.04347107, -30.45765597, -0.13303031, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13111, 275.79560139, 0.00168358, 328.96142277, 0.04347107, 32.89614228, 0.13303031, -275.79560139, -0.00168358, -328.96142277, -0.04347107, -32.89614228, -0.13303031, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3111, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23111, 'My', 13111, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170111, 70111, 170111, 3111, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120112, 120112, 20112, 3111, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170211, 8.3, 5.25, 3.85)
    ops.node(120212, 8.3, 5.25, 6.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3211, 170211, 120212, 0.1225, 30124476.33149886, 12551865.13812453, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23211, 206.33204218, 0.00156644, 246.53268805, 0.03568561, 24.65326881, 0.12007048, -206.33204218, -0.00156644, -246.53268805, -0.03568561, -24.65326881, -0.12007048, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13211, 227.95892121, 0.00156644, 272.37323403, 0.03568561, 27.2373234, 0.12007048, -227.95892121, -0.00156644, -272.37323403, -0.03568561, -27.2373234, -0.12007048, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3211, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23211, 'My', 13211, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170211, 70211, 170211, 3211, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120212, 120212, 20212, 3211, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170311, 11.25, 5.25, 3.85)
    ops.node(120312, 11.25, 5.25, 6.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3311, 170311, 120312, 0.1225, 30270924.68025571, 12612885.28343988, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23311, 205.52273348, 0.0015632, 245.52995532, 0.03633497, 24.55299553, 0.12268237, -205.52273348, -0.0015632, -245.52995532, -0.03633497, -24.55299553, -0.12268237, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13311, 226.82922605, 0.0015632, 270.983987, 0.03633497, 27.0983987, 0.12268237, -226.82922605, -0.0015632, -270.983987, -0.03633497, -27.0983987, -0.12268237, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3311, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23311, 'My', 13311, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170311, 70311, 170311, 3311, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120312, 120312, 20312, 3311, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170411, 15.4, 5.25, 3.85)
    ops.node(120412, 15.4, 5.25, 6.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3411, 170411, 120412, 0.1225, 31555036.01345144, 13147931.67227143, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23411, 259.12254444, 0.00165021, 308.88612615, 0.04319843, 30.88861261, 0.13399037, -259.12254444, -0.00165021, -308.88612615, -0.04319843, -30.88861261, -0.13399037, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13411, 280.47513892, 0.00165021, 334.33941199, 0.04319843, 33.4339412, 0.13399037, -280.47513892, -0.00165021, -334.33941199, -0.04319843, -33.4339412, -0.13399037, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3411, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23411, 'My', 13411, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170411, 70411, 170411, 3411, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120412, 120412, 20412, 3411, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170511, 19.55, 5.25, 3.925)
    ops.node(120512, 19.55, 5.25, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3511, 170511, 120512, 0.1225, 30625221.39506496, 12760508.9146104, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23511, 220.03268343, 0.00157037, 263.43570429, 0.03972593, 26.34357043, 0.13525659, -220.03268343, -0.00157037, -263.43570429, -0.03972593, -26.34357043, -0.13525659, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13511, 261.52418299, 0.00157037, 313.11169896, 0.03972593, 31.3111699, 0.13525659, -261.52418299, -0.00157037, -313.11169896, -0.03972593, -31.3111699, -0.13525659, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3511, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23511, 'My', 13511, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170511, 70511, 170511, 3511, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120512, 120512, 20512, 3511, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 0.0, 10.5, 3.925)
    ops.node(120022, 0.0, 10.5, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 170021, 120022, 0.09, 30177516.60486295, 12573965.25202623, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 134.01891688, 0.00180172, 160.95555893, 0.04797335, 16.09555589, 0.14797335, -134.01891688, -0.00180172, -160.95555893, -0.04797335, -16.09555589, -0.14797335, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 144.54759517, 0.00180172, 173.60041041, 0.04797335, 17.36004104, 0.14797335, -144.54759517, -0.00180172, -173.60041041, -0.04797335, -17.36004104, -0.14797335, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120022, 120022, 20022, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170121, 4.15, 10.5, 3.85)
    ops.node(120122, 4.15, 10.5, 6.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3121, 170121, 120122, 0.09, 30607664.87715465, 12753193.69881444, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23121, 148.49017773, 0.00185265, 177.14230916, 0.04272587, 17.71423092, 0.13401259, -148.49017773, -0.00185265, -177.14230916, -0.04272587, -17.71423092, -0.13401259, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13121, 159.28105063, 0.00185265, 190.01535014, 0.04272587, 19.00153501, 0.13401259, -159.28105063, -0.00185265, -190.01535014, -0.04272587, -19.00153501, -0.13401259, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3121, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23121, 'My', 13121, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170121, 70121, 170121, 3121, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120122, 120122, 20122, 3121, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170221, 8.3, 10.5, 3.85)
    ops.node(120222, 8.3, 10.5, 6.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3221, 170221, 120222, 0.09, 30963576.5221842, 12901490.21757675, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23221, 125.77796363, 0.00173712, 150.37962257, 0.04406454, 15.03796226, 0.14406454, -125.77796363, -0.00173712, -150.37962257, -0.04406454, -15.03796226, -0.14406454, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13221, 125.77796363, 0.00173712, 150.37962257, 0.04406454, 15.03796226, 0.14406454, -125.77796363, -0.00173712, -150.37962257, -0.04406454, -15.03796226, -0.14406454, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3221, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23221, 'My', 13221, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170221, 70221, 170221, 3221, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120222, 120222, 20222, 3221, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170321, 11.25, 10.5, 3.85)
    ops.node(120322, 11.25, 10.5, 6.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3321, 170321, 120322, 0.09, 31248152.84991597, 13020063.68746499, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23321, 128.61132054, 0.00172424, 153.69631509, 0.04349053, 15.36963151, 0.14349053, -128.61132054, -0.00172424, -153.69631509, -0.04349053, -15.36963151, -0.14349053, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13321, 128.61132054, 0.00172424, 153.69631509, 0.04349053, 15.36963151, 0.14349053, -128.61132054, -0.00172424, -153.69631509, -0.04349053, -15.36963151, -0.14349053, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3321, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23321, 'My', 13321, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170321, 70321, 170321, 3321, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120322, 120322, 20322, 3321, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170421, 15.4, 10.5, 3.85)
    ops.node(120422, 15.4, 10.5, 6.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3421, 170421, 120422, 0.09, 30548724.20806331, 12728635.08669305, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23421, 146.43268898, 0.00189717, 174.69886546, 0.04297866, 17.46988655, 0.13444574, -146.43268898, -0.00189717, -174.69886546, -0.04297866, -17.46988655, -0.13444574, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13421, 156.53575999, 0.00189717, 186.75215121, 0.04297866, 18.67521512, 0.13444574, -156.53575999, -0.00189717, -186.75215121, -0.04297866, -18.67521512, -0.13444574, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3421, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23421, 'My', 13421, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170421, 70421, 170421, 3421, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120422, 120422, 20422, 3421, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170521, 19.55, 10.5, 3.925)
    ops.node(120522, 19.55, 10.5, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3521, 170521, 120522, 0.09, 31663722.74928774, 13193217.81220322, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23521, 130.60037915, 0.00172667, 156.41401462, 0.04698896, 15.64140146, 0.14698896, -130.60037915, -0.00172667, -156.41401462, -0.04698896, -15.64140146, -0.14698896, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13521, 140.35671175, 0.00172667, 168.09872152, 0.04698896, 16.80987215, 0.14698896, -140.35671175, -0.00172667, -168.09872152, -0.04698896, -16.80987215, -0.14698896, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3521, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23521, 'My', 13521, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170521, 70521, 170521, 3521, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120522, 120522, 20522, 3521, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 0.0, 0.0, 7.025)
    ops.node(120003, 0.0, 0.0, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 170002, 120003, 0.09, 31284154.91546357, 13035064.54810982, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 121.24453883, 0.00167662, 145.93003292, 0.0505413, 14.59300329, 0.1505413, -121.24453883, -0.00167662, -145.93003292, -0.0505413, -14.59300329, -0.1505413, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 131.22522997, 0.00167662, 157.94280149, 0.0505413, 15.79428015, 0.1505413, -131.22522997, -0.00167662, -157.94280149, -0.0505413, -15.79428015, -0.1505413, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120003, 120003, 20003, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170102, 4.15, 0.0, 6.95)
    ops.node(120103, 4.15, 0.0, 9.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3102, 170102, 120103, 0.09, 31336359.05442608, 13056816.27267753, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23102, 115.43881873, 0.00174185, 138.3900361, 0.04620335, 13.83900361, 0.14620335, -115.43881873, -0.00174185, -138.3900361, -0.04620335, -13.83900361, -0.14620335, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13102, 115.43881873, 0.00174185, 138.3900361, 0.04620335, 13.83900361, 0.14620335, -115.43881873, -0.00174185, -138.3900361, -0.04620335, -13.83900361, -0.14620335, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3102, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23102, 'My', 13102, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170102, 70102, 170102, 3102, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120103, 120103, 20103, 3102, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170402, 15.4, 0.0, 6.95)
    ops.node(120403, 15.4, 0.0, 9.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3402, 170402, 120403, 0.09, 31055081.00501032, 12939617.08542097, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23402, 115.88938721, 0.00171704, 139.0091141, 0.04507907, 13.90091141, 0.14507907, -115.88938721, -0.00171704, -139.0091141, -0.04507907, -13.90091141, -0.14507907, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13402, 115.88938721, 0.00171704, 139.0091141, 0.04507907, 13.90091141, 0.14507907, -115.88938721, -0.00171704, -139.0091141, -0.04507907, -13.90091141, -0.14507907, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3402, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23402, 'My', 13402, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170402, 70402, 170402, 3402, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120403, 120403, 20403, 3402, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170502, 19.55, 0.0, 7.025)
    ops.node(120503, 19.55, 0.0, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3502, 170502, 120503, 0.09, 32103288.56730719, 13376370.236378, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23502, 120.33302711, 0.00178026, 144.52350845, 0.0494417, 14.45235085, 0.1494417, -120.33302711, -0.00178026, -144.52350845, -0.0494417, -14.45235085, -0.1494417, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13502, 129.19211935, 0.00178026, 155.16353906, 0.0494417, 15.51635391, 0.1494417, -129.19211935, -0.00178026, -155.16353906, -0.0494417, -15.51635391, -0.1494417, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3502, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23502, 'My', 13502, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170502, 70502, 170502, 3502, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120503, 120503, 20503, 3502, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 0.0, 5.25, 7.025)
    ops.node(120013, 0.0, 5.25, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 170012, 120013, 0.1225, 31514330.31366819, 13130970.96402841, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 202.80349211, 0.0015013, 243.56774614, 0.04267532, 24.35677461, 0.14267532, -202.80349211, -0.0015013, -243.56774614, -0.04267532, -24.35677461, -0.14267532, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 243.63992237, 0.0015013, 292.61245034, 0.04267532, 29.26124503, 0.14267532, -243.63992237, -0.0015013, -292.61245034, -0.04267532, -29.26124503, -0.14267532, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120013, 120013, 20013, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170112, 4.15, 5.25, 6.95)
    ops.node(120113, 4.15, 5.25, 9.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3112, 170112, 120113, 0.1225, 30411888.6663686, 12671620.27765358, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23112, 239.37424562, 0.00166143, 287.39936709, 0.04601257, 28.73993671, 0.14573767, -239.37424562, -0.00166143, -287.39936709, -0.04601257, -28.73993671, -0.14573767, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13112, 260.4660262, 0.00166143, 312.72274461, 0.04601257, 31.27227446, 0.14573767, -260.4660262, -0.00166143, -312.72274461, -0.04601257, -31.27227446, -0.14573767, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3112, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23112, 'My', 13112, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170112, 70112, 170112, 3112, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120113, 120113, 20113, 3112, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170212, 8.3, 5.25, 6.95)
    ops.node(120213, 8.3, 5.25, 9.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3212, 170212, 120213, 0.1225, 31822774.57256261, 13259489.40523442, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23212, 185.27033324, 0.00145858, 221.93612707, 0.03914867, 22.19361271, 0.13914867, -185.27033324, -0.00145858, -221.93612707, -0.03914867, -22.19361271, -0.13914867, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13212, 206.06684132, 0.00145858, 246.84835333, 0.03914867, 24.68483533, 0.13914867, -206.06684132, -0.00145858, -246.84835333, -0.03914867, -24.68483533, -0.13914867, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3212, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23212, 'My', 13212, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170212, 70212, 170212, 3212, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120213, 120213, 20213, 3212, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170312, 11.25, 5.25, 6.95)
    ops.node(120313, 11.25, 5.25, 9.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3312, 170312, 120313, 0.1225, 33068103.77205007, 13778376.57168753, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23312, 181.89952889, 0.00143977, 217.20844004, 0.03914547, 21.720844, 0.13914547, -181.89952889, -0.00143977, -217.20844004, -0.03914547, -21.720844, -0.13914547, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13312, 201.1538746, 0.00143977, 240.20028846, 0.03914547, 24.02002885, 0.13914547, -201.1538746, -0.00143977, -240.20028846, -0.03914547, -24.02002885, -0.13914547, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3312, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23312, 'My', 13312, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170312, 70312, 170312, 3312, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120313, 120313, 20313, 3312, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170412, 15.4, 5.25, 6.95)
    ops.node(120413, 15.4, 5.25, 9.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3412, 170412, 120413, 0.1225, 31324040.71323092, 13051683.63051288, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23412, 234.4935304, 0.00163222, 281.06237416, 0.0474665, 28.10623742, 0.1474665, -234.4935304, -0.00163222, -281.06237416, -0.0474665, -28.10623742, -0.1474665, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13412, 254.30703365, 0.00163222, 304.81070637, 0.0474665, 30.48107064, 0.1474665, -254.30703365, -0.00163222, -304.81070637, -0.0474665, -30.48107064, -0.1474665, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3412, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23412, 'My', 13412, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170412, 70412, 170412, 3412, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120413, 120413, 20413, 3412, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170512, 19.55, 5.25, 7.025)
    ops.node(120513, 19.55, 5.25, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3512, 170512, 120513, 0.1225, 32495598.19316168, 13539832.58048403, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23512, 203.83484379, 0.00145925, 244.1917116, 0.04236788, 24.41917116, 0.14236788, -203.83484379, -0.00145925, -244.1917116, -0.04236788, -24.41917116, -0.14236788, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13512, 245.25595855, 0.00145925, 293.81371304, 0.04236788, 29.3813713, 0.14236788, -245.25595855, -0.00145925, -293.81371304, -0.04236788, -29.3813713, -0.14236788, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3512, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23512, 'My', 13512, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170512, 70512, 170512, 3512, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120513, 120513, 20513, 3512, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 0.0, 10.5, 7.025)
    ops.node(120023, 0.0, 10.5, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 170022, 120023, 0.09, 30942893.27039208, 12892872.1959967, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 121.50886971, 0.00172186, 146.36842424, 0.05127707, 14.63684242, 0.15127707, -121.50886971, -0.00172186, -146.36842424, -0.05127707, -14.63684242, -0.15127707, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 131.36928484, 0.00172186, 158.24618616, 0.05127707, 15.82461862, 0.15127707, -131.36928484, -0.00172186, -158.24618616, -0.05127707, -15.82461862, -0.15127707, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120023, 120023, 20023, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170122, 4.15, 10.5, 6.95)
    ops.node(120123, 4.15, 10.5, 9.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3122, 170122, 120123, 0.09, 31483339.01953378, 13118057.92480574, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23122, 118.43998841, 0.00173616, 141.94393563, 0.04516488, 14.19439356, 0.14516488, -118.43998841, -0.00173616, -141.94393563, -0.04516488, -14.19439356, -0.14516488, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13122, 118.43998841, 0.00173616, 141.94393563, 0.04516488, 14.19439356, 0.14516488, -118.43998841, -0.00173616, -141.94393563, -0.04516488, -14.19439356, -0.14516488, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3122, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23122, 'My', 13122, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170122, 70122, 170122, 3122, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120123, 120123, 20123, 3122, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170222, 8.3, 10.5, 6.95)
    ops.node(120223, 8.3, 10.5, 9.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3222, 170222, 120223, 0.09, 31152873.39708161, 12980363.91545067, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23222, 111.41415393, 0.00173225, 133.84701127, 0.0464372, 13.38470113, 0.1464372, -111.41415393, -0.00173225, -133.84701127, -0.0464372, -13.38470113, -0.1464372, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13222, 111.41415393, 0.00173225, 133.84701127, 0.0464372, 13.38470113, 0.1464372, -111.41415393, -0.00173225, -133.84701127, -0.0464372, -13.38470113, -0.1464372, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3222, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23222, 'My', 13222, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170222, 70222, 170222, 3222, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120223, 120223, 20223, 3222, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170322, 11.25, 10.5, 6.95)
    ops.node(120323, 11.25, 10.5, 9.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3322, 170322, 120323, 0.09, 31174754.26200213, 12989480.94250089, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23322, 113.98710269, 0.00165493, 136.93144846, 0.04705587, 13.69314485, 0.14705587, -113.98710269, -0.00165493, -136.93144846, -0.04705587, -13.69314485, -0.14705587, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13322, 113.98710269, 0.00165493, 136.93144846, 0.04705587, 13.69314485, 0.14705587, -113.98710269, -0.00165493, -136.93144846, -0.04705587, -13.69314485, -0.14705587, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3322, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23322, 'My', 13322, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170322, 70322, 170322, 3322, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120323, 120323, 20323, 3322, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170422, 15.4, 10.5, 6.95)
    ops.node(120423, 15.4, 10.5, 9.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3422, 170422, 120423, 0.09, 32047012.6643503, 13352921.94347929, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23422, 119.64593839, 0.00167918, 143.20751389, 0.04631966, 14.32075139, 0.14631966, -119.64593839, -0.00167918, -143.20751389, -0.04631966, -14.32075139, -0.14631966, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13422, 119.64593839, 0.00167918, 143.20751389, 0.04631966, 14.32075139, 0.14631966, -119.64593839, -0.00167918, -143.20751389, -0.04631966, -14.32075139, -0.14631966, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3422, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23422, 'My', 13422, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170422, 70422, 170422, 3422, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120423, 120423, 20423, 3422, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170522, 19.55, 10.5, 7.025)
    ops.node(120523, 19.55, 10.5, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3522, 170522, 120523, 0.09, 31408112.04309945, 13086713.35129144, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23522, 121.870074, 0.00169797, 146.63766167, 0.05092411, 14.66376617, 0.15092411, -121.870074, -0.00169797, -146.63766167, -0.05092411, -14.66376617, -0.15092411, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13522, 131.80754121, 0.00169797, 158.59471484, 0.05092411, 15.85947148, 0.15092411, -131.80754121, -0.00169797, -158.59471484, -0.05092411, -15.85947148, -0.15092411, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3522, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23522, 'My', 13522, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170522, 70522, 170522, 3522, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120523, 120523, 20523, 3522, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 0.0, 0.0, 10.125)
    ops.node(120004, 0.0, 0.0, 12.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 170003, 120004, 0.09, 32945460.92006255, 13727275.3833594, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 125.21246946, 0.0016092, 150.61839215, 0.05328926, 15.06183921, 0.15328926, -125.21246946, -0.0016092, -150.61839215, -0.05328926, -15.06183921, -0.15328926, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 145.41032159, 0.0016092, 174.91443891, 0.05328926, 17.49144389, 0.15328926, -145.41032159, -0.0016092, -174.91443891, -0.05328926, -17.49144389, -0.15328926, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120004, 120004, 20004, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170103, 4.15, 0.0, 10.05)
    ops.node(120104, 4.15, 0.0, 12.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3103, 170103, 120104, 0.09, 31428542.7167109, 13095226.13196287, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23103, 151.16130229, 0.00184557, 182.38281661, 0.05528883, 18.23828166, 0.15528883, -151.16130229, -0.00184557, -182.38281661, -0.05528883, -18.23828166, -0.15528883, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13103, 160.37801869, 0.00184557, 193.50319378, 0.05528883, 19.35031938, 0.15528883, -160.37801869, -0.00184557, -193.50319378, -0.05528883, -19.35031938, -0.15528883, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3103, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23103, 'My', 13103, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170103, 70103, 170103, 3103, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120104, 120104, 20104, 3103, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170403, 15.4, 0.0, 10.05)
    ops.node(120404, 15.4, 0.0, 12.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3403, 170403, 120404, 0.09, 30043662.11403469, 12518192.54751446, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23403, 154.99420841, 0.00177853, 187.68246926, 0.05746418, 18.76824693, 0.15746418, -154.99420841, -0.00177853, -187.68246926, -0.05746418, -18.76824693, -0.15746418, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13403, 165.61733445, 0.00177853, 200.54601138, 0.05746418, 20.05460114, 0.15746418, -165.61733445, -0.00177853, -200.54601138, -0.05746418, -20.05460114, -0.15746418, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3403, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23403, 'My', 13403, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170403, 70403, 170403, 3403, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120404, 120404, 20404, 3403, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170503, 19.55, 0.0, 10.125)
    ops.node(120504, 19.55, 0.0, 12.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3503, 170503, 120504, 0.09, 31004692.3099101, 12918621.79579588, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23503, 123.29877681, 0.00170643, 149.23168853, 0.05716837, 14.92316885, 0.15716837, -123.29877681, -0.00170643, -149.23168853, -0.05716837, -14.92316885, -0.15716837, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13503, 142.65055154, 0.00170643, 172.65364042, 0.05716837, 17.26536404, 0.15716837, -142.65055154, -0.00170643, -172.65364042, -0.05716837, -17.26536404, -0.15716837, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3503, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23503, 'My', 13503, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170503, 70503, 170503, 3503, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120504, 120504, 20504, 3503, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 5.25, 10.125)
    ops.node(120014, 0.0, 5.25, 12.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 170013, 120014, 0.1225, 32316821.6758344, 13465342.364931, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 208.07855933, 0.00146694, 250.61491792, 0.04707126, 25.06149179, 0.14707126, -208.07855933, -0.00146694, -250.61491792, -0.04707126, -25.06149179, -0.14707126, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 268.62806984, 0.00146694, 323.54223275, 0.04707126, 32.35422328, 0.14707126, -268.62806984, -0.00146694, -323.54223275, -0.04707126, -32.35422328, -0.14707126, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120014, 120014, 20014, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170113, 4.15, 5.25, 10.05)
    ops.node(120114, 4.15, 5.25, 12.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3113, 170113, 120114, 0.1225, 31101968.76518072, 12959153.65215863, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23113, 266.95962763, 0.00172553, 322.09005027, 0.05544728, 32.20900503, 0.15544728, -266.95962763, -0.00172553, -322.09005027, -0.05544728, -32.20900503, -0.15544728, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13113, 327.52957942, 0.00172553, 395.16843665, 0.05544728, 39.51684367, 0.15544728, -327.52957942, -0.00172553, -395.16843665, -0.05544728, -39.51684367, -0.15544728, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3113, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23113, 'My', 13113, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170113, 70113, 170113, 3113, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120114, 120114, 20114, 3113, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170213, 8.3, 5.25, 10.05)
    ops.node(120214, 8.3, 5.25, 12.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3213, 170213, 120214, 0.1225, 29567543.18400541, 12319809.66000226, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23213, 211.01327271, 0.00150924, 255.70023572, 0.04902023, 25.57002357, 0.14902023, -211.01327271, -0.00150924, -255.70023572, -0.04902023, -25.57002357, -0.14902023, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13213, 274.9013164, 0.00150924, 333.11805699, 0.04902023, 33.3118057, 0.14902023, -274.9013164, -0.00150924, -333.11805699, -0.04902023, -33.3118057, -0.14902023, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3213, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23213, 'My', 13213, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170213, 70213, 170213, 3213, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120214, 120214, 20214, 3213, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170313, 11.25, 5.25, 10.05)
    ops.node(120314, 11.25, 5.25, 12.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3313, 170313, 120314, 0.1225, 30688354.94502965, 12786814.56042902, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23313, 213.09616019, 0.00152111, 257.53815041, 0.04664455, 25.75381504, 0.14664455, -213.09616019, -0.00152111, -257.53815041, -0.04664455, -25.75381504, -0.14664455, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13313, 275.42314981, 0.00152111, 332.86366362, 0.04664455, 33.28636636, 0.14664455, -275.42314981, -0.00152111, -332.86366362, -0.04664455, -33.28636636, -0.14664455, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3313, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23313, 'My', 13313, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170313, 70313, 170313, 3313, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120314, 120314, 20314, 3313, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170413, 15.4, 5.25, 10.05)
    ops.node(120414, 15.4, 5.25, 12.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3413, 170413, 120414, 0.1225, 29948019.45604256, 12478341.44001773, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23413, 264.73667439, 0.00172189, 320.30434277, 0.05571919, 32.03043428, 0.15571919, -264.73667439, -0.00172189, -320.30434277, -0.05571919, -32.03043428, -0.15571919, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13413, 326.69451889, 0.00172189, 395.26700787, 0.05571919, 39.52670079, 0.15571919, -326.69451889, -0.00172189, -395.26700787, -0.05571919, -39.52670079, -0.15571919, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3413, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23413, 'My', 13413, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170413, 70413, 170413, 3413, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120414, 120414, 20414, 3413, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170513, 19.55, 5.25, 10.125)
    ops.node(120514, 19.55, 5.25, 12.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3513, 170513, 120514, 0.1225, 33767245.88513639, 14069685.7854735, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23513, 207.12675579, 0.00138922, 248.24288046, 0.04564554, 24.82428805, 0.14564554, -207.12675579, -0.00138922, -248.24288046, -0.04564554, -24.82428805, -0.14564554, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13513, 268.22956833, 0.00138922, 321.47503307, 0.04564554, 32.14750331, 0.14564554, -268.22956833, -0.00138922, -321.47503307, -0.04564554, -32.14750331, -0.14564554, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3513, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23513, 'My', 13513, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170513, 70513, 170513, 3513, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120514, 120514, 20514, 3513, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 0.0, 10.5, 10.125)
    ops.node(120024, 0.0, 10.5, 12.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 170023, 120024, 0.09, 33150804.88457468, 13812835.36857278, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 125.85324225, 0.00167379, 151.28115051, 0.05318627, 15.12811505, 0.15318627, -125.85324225, -0.00167379, -151.28115051, -0.05318627, -15.12811505, -0.15318627, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 145.26770651, 0.00167379, 174.61819322, 0.05318627, 17.46181932, 0.15318627, -145.26770651, -0.00167379, -174.61819322, -0.05318627, -17.46181932, -0.15318627, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120024, 120024, 20024, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170123, 4.15, 10.5, 10.05)
    ops.node(120124, 4.15, 10.5, 12.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3123, 170123, 120124, 0.09, 32125868.56503624, 13385778.5687651, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23123, 154.20220272, 0.00173158, 185.67289048, 0.05490865, 18.56728905, 0.15490865, -154.20220272, -0.00173158, -185.67289048, -0.05490865, -18.56728905, -0.15490865, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13123, 164.33134183, 0.00173158, 197.86925671, 0.05490865, 19.78692567, 0.15490865, -164.33134183, -0.00173158, -197.86925671, -0.05490865, -19.78692567, -0.15490865, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3123, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23123, 'My', 13123, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170123, 70123, 170123, 3123, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120124, 120124, 20124, 3123, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170223, 8.3, 10.5, 10.05)
    ops.node(120224, 8.3, 10.5, 12.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3223, 170223, 120224, 0.09, 31567460.13475573, 13153108.38948155, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23223, 134.51253304, 0.0017087, 162.34940755, 0.0555785, 16.23494076, 0.1555785, -134.51253304, -0.0017087, -162.34940755, -0.0555785, -16.23494076, -0.1555785, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13223, 134.51253304, 0.0017087, 162.34940755, 0.0555785, 16.23494076, 0.1555785, -134.51253304, -0.0017087, -162.34940755, -0.0555785, -16.23494076, -0.1555785, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3223, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23223, 'My', 13223, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170223, 70223, 170223, 3223, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120224, 120224, 20224, 3223, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170323, 11.25, 10.5, 10.05)
    ops.node(120324, 11.25, 10.5, 12.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3323, 170323, 120324, 0.09, 32010235.18021073, 13337597.99175447, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23323, 138.01140852, 0.00168879, 166.35112733, 0.05534935, 16.63511273, 0.15534935, -138.01140852, -0.00168879, -166.35112733, -0.05534935, -16.63511273, -0.15534935, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13323, 138.01140852, 0.00168879, 166.35112733, 0.05534935, 16.63511273, 0.15534935, -138.01140852, -0.00168879, -166.35112733, -0.05534935, -16.63511273, -0.15534935, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3323, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23323, 'My', 13323, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170323, 70323, 170323, 3323, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120324, 120324, 20324, 3323, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170423, 15.4, 10.5, 10.05)
    ops.node(120424, 15.4, 10.5, 12.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3423, 170423, 120424, 0.09, 30437284.81080484, 12682202.00450202, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23423, 153.97527771, 0.00176277, 186.26904173, 0.05734958, 18.62690417, 0.15734958, -153.97527771, -0.00176277, -186.26904173, -0.05734958, -18.62690417, -0.15734958, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13423, 164.40700826, 0.00176277, 198.88865497, 0.05734958, 19.8888655, 0.15734958, -164.40700826, -0.00176277, -198.88865497, -0.05734958, -19.8888655, -0.15734958, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3423, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23423, 'My', 13423, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170423, 70423, 170423, 3423, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120424, 120424, 20424, 3423, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170523, 19.55, 10.5, 10.125)
    ops.node(120524, 19.55, 10.5, 12.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3523, 170523, 120524, 0.09, 30816431.0851094, 12840179.61879558, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23523, 123.84496833, 0.00168656, 149.97376844, 0.05556034, 14.99737684, 0.15556034, -123.84496833, -0.00168656, -149.97376844, -0.05556034, -14.99737684, -0.15556034, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13523, 143.79112118, 0.00168656, 174.12815879, 0.05556034, 17.41281588, 0.15556034, -143.79112118, -0.00168656, -174.12815879, -0.05556034, -17.41281588, -0.15556034, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3523, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23523, 'My', 13523, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170523, 70523, 170523, 3523, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120524, 120524, 20524, 3523, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170200, 8.3, 0.0, 0.0)
    ops.node(121201, 8.3, 0.0, 1.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4200, 170200, 121201, 0.09, 31380797.09414742, 13075332.12256142, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24200, 151.68460321, 0.00143506, 179.49775742, 0.03706284, 17.94977574, 0.11407414, -151.68460321, -0.00143506, -179.49775742, -0.03706284, -17.94977574, -0.11407414, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14200, 151.68460321, 0.00143506, 179.49775742, 0.03706284, 17.94977574, 0.11407414, -151.68460321, -0.00143506, -179.49775742, -0.03706284, -17.94977574, -0.11407414, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4200, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24200, 'My', 14200, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170200, 70200, 170200, 4200, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121201, 121201, 21201, 4200, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171201, 8.3, 0.0, 2.0)
    ops.node(120201, 8.3, 0.0, 3.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5200, 171201, 120201, 0.09, 30980573.51540961, 12908572.29808734, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 25200, 144.1660392, 0.00149143, 170.98069536, 0.03874889, 17.09806954, 0.11981765, -144.1660392, -0.00149143, -170.98069536, -0.03874889, -17.09806954, -0.11981765, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 15200, 144.1660392, 0.00149143, 170.98069536, 0.03874889, 17.09806954, 0.11981765, -144.1660392, -0.00149143, -170.98069536, -0.03874889, -17.09806954, -0.11981765, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5200, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 25200, 'My', 15200, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171201, 71201, 171201, 5200, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120201, 120201, 20201, 5200, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170300, 11.25, 0.0, 0.0)
    ops.node(121301, 11.25, 0.0, 1.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4300, 170300, 121301, 0.09, 29777018.84654119, 12407091.18605883, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24300, 150.21712686, 0.00154888, 177.82554285, 0.03574097, 17.78255428, 0.10304841, -150.21712686, -0.00154888, -177.82554285, -0.03574097, -17.78255428, -0.10304841, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14300, 150.21712686, 0.00154888, 177.82554285, 0.03574097, 17.78255428, 0.10304841, -150.21712686, -0.00154888, -177.82554285, -0.03574097, -17.78255428, -0.10304841, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4300, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24300, 'My', 14300, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170300, 70300, 170300, 4300, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121301, 121301, 21301, 4300, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171301, 11.25, 0.0, 2.0)
    ops.node(120301, 11.25, 0.0, 3.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5300, 171301, 120301, 0.09, 33384676.62131044, 13910281.92554602, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 25300, 148.46441218, 0.00138994, 175.50357703, 0.038959, 17.5503577, 0.13196048, -148.46441218, -0.00138994, -175.50357703, -0.038959, -17.5503577, -0.13196048, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 15300, 148.46441218, 0.00138994, 175.50357703, 0.038959, 17.5503577, 0.13196048, -148.46441218, -0.00138994, -175.50357703, -0.038959, -17.5503577, -0.13196048, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5300, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 25300, 'My', 15300, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171301, 71301, 171301, 5300, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120301, 120301, 20301, 5300, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170201, 8.3, 0.0, 3.85)
    ops.node(121202, 8.3, 0.0, 5.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4201, 170201, 121202, 0.09, 31185685.79842636, 12994035.74934432, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24201, 134.46867488, 0.00132656, 160.15164513, 0.04138672, 16.01516451, 0.13500694, -134.46867488, -0.00132656, -160.15164513, -0.04138672, -16.01516451, -0.13500694, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14201, 134.46867488, 0.00132656, 160.15164513, 0.04138672, 16.01516451, 0.13500694, -134.46867488, -0.00132656, -160.15164513, -0.04138672, -16.01516451, -0.13500694, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4201, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24201, 'My', 14201, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170201, 70201, 170201, 4201, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121202, 121202, 21202, 4201, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171202, 8.3, 0.0, 5.4)
    ops.node(120202, 8.3, 0.0, 6.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5201, 171202, 120202, 0.09, 31333445.74991001, 13055602.39579584, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 25201, 132.46219722, 0.00131666, 158.02842616, 0.04162577, 15.80284262, 0.13951, -132.46219722, -0.00131666, -158.02842616, -0.04162577, -15.80284262, -0.13951, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 15201, 132.46219722, 0.00131666, 158.02842616, 0.04162577, 15.80284262, 0.13951, -132.46219722, -0.00131666, -158.02842616, -0.04162577, -15.80284262, -0.13951, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5201, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 25201, 'My', 15201, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171202, 71202, 171202, 5201, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120202, 120202, 20202, 5201, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170301, 11.25, 0.0, 3.85)
    ops.node(121302, 11.25, 0.0, 5.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4301, 170301, 121302, 0.09, 30896740.23048757, 12873641.76270315, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24301, 134.02517836, 0.00134387, 159.67917752, 0.04126335, 15.96791775, 0.13326883, -134.02517836, -0.00134387, -159.67917752, -0.04126335, -15.96791775, -0.13326883, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14301, 134.02517836, 0.00134387, 159.67917752, 0.04126335, 15.96791775, 0.13326883, -134.02517836, -0.00134387, -159.67917752, -0.04126335, -15.96791775, -0.13326883, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4301, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24301, 'My', 14301, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170301, 70301, 170301, 4301, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121302, 121302, 21302, 4301, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171302, 11.25, 0.0, 5.4)
    ops.node(120302, 11.25, 0.0, 6.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5301, 171302, 120302, 0.09, 30724527.35772214, 12801886.39905089, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 25301, 128.72148862, 0.00134765, 153.69768003, 0.04232428, 15.369768, 0.13873433, -128.72148862, -0.00134765, -153.69768003, -0.04232428, -15.369768, -0.13873433, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 15301, 128.72148862, 0.00134765, 153.69768003, 0.04232428, 15.369768, 0.13873433, -128.72148862, -0.00134765, -153.69768003, -0.04232428, -15.369768, -0.13873433, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5301, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 25301, 'My', 15301, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171302, 71302, 171302, 5301, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120302, 120302, 20302, 5301, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170202, 8.3, 0.0, 6.95)
    ops.node(121203, 8.3, 0.0, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4202, 170202, 121203, 0.09, 31055074.27362947, 12939614.28067895, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24202, 120.11896852, 0.00130104, 143.99366146, 0.045428, 14.39936615, 0.145428, -120.11896852, -0.00130104, -143.99366146, -0.045428, -14.39936615, -0.145428, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14202, 120.11896852, 0.00130104, 143.99366146, 0.045428, 14.39936615, 0.145428, -120.11896852, -0.00130104, -143.99366146, -0.045428, -14.39936615, -0.145428, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4202, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24202, 'My', 14202, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170202, 70202, 170202, 4202, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121203, 121203, 21203, 4202, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171203, 8.3, 0.0, 8.5)
    ops.node(120203, 8.3, 0.0, 9.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5202, 171203, 120203, 0.09, 32241364.15806303, 13433901.73252626, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 25202, 114.27685544, 0.00126762, 136.91043583, 0.04582345, 13.69104358, 0.14582345, -114.27685544, -0.00126762, -136.91043583, -0.04582345, -13.69104358, -0.14582345, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 15202, 114.27685544, 0.00126762, 136.91043583, 0.04582345, 13.69104358, 0.14582345, -114.27685544, -0.00126762, -136.91043583, -0.04582345, -13.69104358, -0.14582345, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5202, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 25202, 'My', 15202, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171203, 71203, 171203, 5202, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120203, 120203, 20203, 5202, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170302, 11.25, 0.0, 6.95)
    ops.node(121303, 11.25, 0.0, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4302, 170302, 121303, 0.09, 31924882.2026888, 13302034.25112033, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24302, 120.24826857, 0.00131782, 143.88859845, 0.04469659, 14.38885985, 0.14469659, -120.24826857, -0.00131782, -143.88859845, -0.04469659, -14.38885985, -0.14469659, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14302, 120.24826857, 0.00131782, 143.88859845, 0.04469659, 14.38885985, 0.14469659, -120.24826857, -0.00131782, -143.88859845, -0.04469659, -14.38885985, -0.14469659, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4302, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24302, 'My', 14302, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170302, 70302, 170302, 4302, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121303, 121303, 21303, 4302, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171303, 11.25, 0.0, 8.5)
    ops.node(120303, 11.25, 0.0, 9.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5302, 171303, 120303, 0.09, 31036334.67733297, 12931806.1155554, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 25302, 113.31574478, 0.00129184, 136.14503145, 0.04613883, 13.61450315, 0.14613883, -113.31574478, -0.00129184, -136.14503145, -0.04613883, -13.61450315, -0.14613883, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 15302, 113.31574478, 0.00129184, 136.14503145, 0.04613883, 13.61450315, 0.14613883, -113.31574478, -0.00129184, -136.14503145, -0.04613883, -13.61450315, -0.14613883, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5302, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 25302, 'My', 15302, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171303, 71303, 171303, 5302, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120303, 120303, 20303, 5302, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170203, 8.3, 0.0, 10.05)
    ops.node(121204, 8.3, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4203, 170203, 121204, 0.09, 29300788.37672226, 12208661.82363428, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24203, 98.55955674, 0.00130341, 119.51244734, 0.05218495, 11.95124473, 0.15218495, -98.55955674, -0.00130341, -119.51244734, -0.05218495, -11.95124473, -0.15218495, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14203, 98.55955674, 0.00130341, 119.51244734, 0.05218495, 11.95124473, 0.15218495, -98.55955674, -0.00130341, -119.51244734, -0.05218495, -11.95124473, -0.15218495, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4203, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24203, 'My', 14203, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170203, 70203, 170203, 4203, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121204, 121204, 21204, 4203, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171204, 8.3, 0.0, 11.6)
    ops.node(120204, 8.3, 0.0, 12.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5203, 171204, 120204, 0.09, 32116081.30672419, 13381700.54446841, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 25203, 118.64054261, 0.00119999, 143.11040812, 0.05313412, 14.31104081, 0.15313412, -118.64054261, -0.00119999, -143.11040812, -0.05313412, -14.31104081, -0.15313412, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 15203, 108.90734762, 0.00119999, 131.36972086, 0.05313412, 13.13697209, 0.15313412, -108.90734762, -0.00119999, -131.36972086, -0.05313412, -13.13697209, -0.15313412, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5203, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 25203, 'My', 15203, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171204, 71204, 171204, 5203, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120204, 120204, 20204, 5203, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170303, 11.25, 0.0, 10.05)
    ops.node(121304, 11.25, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4303, 170303, 121304, 0.09, 30751702.89166789, 12813209.53819495, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24303, 98.16367028, 0.00127248, 118.62697597, 0.05134644, 11.8626976, 0.15134644, -98.16367028, -0.00127248, -118.62697597, -0.05134644, -11.8626976, -0.15134644, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14303, 98.16367028, 0.00127248, 118.62697597, 0.05134644, 11.8626976, 0.15134644, -98.16367028, -0.00127248, -118.62697597, -0.05134644, -11.8626976, -0.15134644, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4303, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24303, 'My', 14303, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170303, 70303, 170303, 4303, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121304, 121304, 21304, 4303, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171304, 11.25, 0.0, 11.6)
    ops.node(120304, 11.25, 0.0, 12.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5303, 171304, 120304, 0.09, 31520819.19874612, 13133674.66614422, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 25303, 119.55965092, 0.00121659, 144.48780103, 0.0538889, 14.4487801, 0.1538889, -119.55965092, -0.00121659, -144.48780103, -0.0538889, -14.4487801, -0.1538889, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 15303, 109.62425935, 0.00121659, 132.48088341, 0.0538889, 13.24808834, 0.1538889, -109.62425935, -0.00121659, -132.48088341, -0.0538889, -13.24808834, -0.1538889, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5303, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 25303, 'My', 15303, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171304, 71304, 171304, 5303, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 120304, 120304, 20304, 5303, '-orient', 0, 0, 1, 0, 1, 0)
