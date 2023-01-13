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
        print()
        print("determinant: " + str(det))
        print()
                                                                       
        break
    except ValueError:
        print("enter numbers only")
        continue