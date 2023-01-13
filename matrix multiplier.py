while True:
    try:
        print()
        print("enter martrix A: ")
        print()
        X1 = input()
        X2 = input()
        X3 = input()
        print("-----")
        print()
        print("enter matrix B: ")
        print()
        y1 = input()
        y2 = input()
        y3 = input()

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


        splitedy1 = y1.split()
        splitedy2 = y2.split()
        splitedy3 = y3.split()

        y11 = int(splitedy1[0])
        y12 = int(splitedy1[1])
        y13 = int(splitedy1[2])

        y21 = int(splitedy2[0])
        y22 = int(splitedy2[1])
        y23 = int(splitedy2[2])

        y31 = int(splitedy3[0])
        y32 = int(splitedy3[1])
        y33 = int(splitedy3[2])

        xy11 = (x11*y11) + (x12*y21) + (x13*y31) 
        xy12 = (x11*y12) + (x12*y22) + (x13*y32)
        xy13 = (x11*y13) + (x12*y23) + (x13*y33)

        xy21 = (x21*y11) + (x22*y21) + (x23*y31)
        xy22 = (x21*y12) + (x22*y22) + (x23*y32)
        xy23 = (x21*y13) + (x22*y23) + (x23*y33)

        xy31 = (x31*y11) + (x32*y21) + (x33*x31)
        xy32 = (x31*y12) + (x32*y22) + (x33*y32)
        xy33 = (x31*y13) + (x32*y23) + (x33*y33)
        print()
        print("-----")
        print("matrix A * matrix B //")
        print()
        print(xy11, xy12, xy13)
        print(xy21, xy22, xy23)
        print(xy31, xy32, xy33)
        print("-----")  
        print()                                                 
        break
    except ValueError:
        print("enter numbers only")
        continue