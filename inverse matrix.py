from fractions import Fraction
while True:
    try:
        print()
        X1 = input()
        X2 = input()
        X3 = input()

        splitedX1 = X1.split()
        splitedX2 = X2.split()
        splitedX3 = X3.split()

        x11 = int(splitedX1[0])
        x12 = int(splitedX1[1])
        x13 = int(splitedX1[2])

        x21 = int(splitedX2[0])
        x22 = int(splitedX2[1])
        x23 = int(splitedX2[2])

        x31 = int(splitedX3[0])
        x32 = int(splitedX3[1])
        x33 = int(splitedX3[2])

        det = (x11 * x22 * x33) + (x12 * x23 * x31) + (x21 * x32 * x13) - (x13 * x22 * x31) - (x12 * x21 * x33) - (x23 * x32 * x11) 
        det_rev = Fraction(1, det)
        print()
        print("determinant: ")
        print()
        print(det)
                                                                       
        break
    except ValueError:
        print("enter numbers only")
        continue

L_up11 = (x22 ,x23)
L_dn11 = (x32, x33)

L_up12 = (x21, x23)
L_dn12 = (x31, x33)

L_up13 = (x21 ,x22)
L_dn13 = (x31, x32)

L_up21 = (x12, x13)
L_dn21 = (x32, x33)

L_up22 = (x11, x13)
L_dn22 = (x31, x33)

L_up23 = (x11, x12)
L_dn23 = (x31, x31)

L_up31 = (x12, x13)
L_dn31 = (x22, x23)

L_up32 = (x11, x13)
L_dn32 = (x21, x23)

L_up33 = (x11, x12)
L_dn33 = (x21, x22)
print()
print("minors:  ")
print()
print((L_up11),  (L_up12),  (L_up13))
print((L_dn11),  (L_dn12),  (L_dn13))
print()
print((L_up21),  (L_up22),  (L_up23))
print((L_dn21),  (L_dn22),  (L_dn23))
print()
print((L_up31),  (L_up32),  (L_up33))
print((L_dn31),  (L_dn32),  (L_dn33))
print()
print("determinants from minors: ")
print()
a11 = x22 * x33 - x23 * x32
a12 = x21 * x33 - x23 * x31
a13 = x21 * x32 - x22 * x31

a21 = x12 * x33 - x13 * x32
a22 = x11 * x33 - x13 * x31
a23 = x11 * x32 - x12 * x31

a31 = x12 * x23 - x13 * x22
a32 = x11 * x23 - x13 * x21
a33 = x11 * x22 - x12 * x21
print((a11, a12, a13))
print()
print((a21, a22, a23))
print()
print((a31, a32, a33))
print()
print("above matrix with right '+' '-'")
print()
print((a11, a12 * -1, a13))
print()
print((a21 * -1, a22, a23 * -1))
print()
print((a31, a32 * -1, a33))
print()
print("above matrix in order for formula: formula = /A/^-1 * (matrix)")
print()
print((a11, a21 * -1, a31))
print()
print((a12 * -1, a22, a32 * -1))
print()
print((a13, a23 * -1, a33))
print()
print("/A/^-1 = " + str(det_rev) + " * " + "above matrix = : ")
print()
print()
print((a11 * det_rev), ((a21 * -1) * det_rev), (a31 * det_rev))
print()
print(((a12 * -1) * det_rev), (a22 * det_rev), ((a32 * -1) * det_rev))
print()
print((a13 * det_rev), ((a23 * -1) * det_rev), (a33 * det_rev))
print()
print()
