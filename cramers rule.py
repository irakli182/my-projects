from multiprocessing.connection import answer_challenge
import re
import math
import nums_from_string
from fractions import Fraction

print()
print("===================== RULES =====================")
print()
print('1. The first number must be "x"' )
print('2. The second number must be "y"')
print('3. The answer must be a number')
print('4. Equation must have a following structure: Nx + Ny = N, N == R')
print()
print("===================== RULES =====================")
print()
print("equation: ")
print()
while True:
    mag1 = input("{ ")

    mag1_split_from_x_right = mag1.partition("x")[2]
    mag1_split_from_x_left = mag1.partition("x")[0]
    mag1_split_from_y_left = mag1.partition("y")[0]
    answer1 = mag1.split("=",1)[1]
    if answer1.isalpha():
        print("enter only number as answer")
        continue    
    if mag1[0] == "-" and mag1_split_from_x_left[-1].isdigit() and mag1_split_from_y_left[-1].isdigit() and mag1_split_from_x_right[0] == "-":
        mag1 = mag1.replace("x", '')
        mag1 = mag1.replace("y", '')
    elif mag1[0] == "-" and mag1_split_from_x_left[-1].isdigit() and mag1_split_from_y_left[-1].isdigit() and mag1_split_from_x_right[0] == "+":
        mag1 = mag1.replace("x", '')
        mag1 = mag1.replace("y", '')
    elif mag1[0].isdigit() and mag1_split_from_x_left[-1].isdigit() and mag1_split_from_y_left[-1].isdigit() and mag1_split_from_x_right[0] == "-":
        mag1 = mag1.replace("x", '')
        mag1 = mag1.replace("y", '')
    elif mag1[0].isdigit() and mag1_split_from_x_left[-1].isdigit() and mag1_split_from_y_left[-1].isdigit() and mag1_split_from_x_right[0] == "+":
        mag1 = mag1.replace("x", '')
        mag1 = mag1.replace("y", '')
    
    elif mag1[0] == "-" and mag1_split_from_x_left[-1] == "-" and mag1_split_from_y_left[-1] == "-" and mag1_split_from_x_right[0] == "-":
        mag1 = mag1.replace("x", "1")
        mag1 = mag1.replace("y", '1')
    elif mag1[0] == "-" and mag1_split_from_x_left[-1] == "-" and mag1_split_from_y_left[-1] == "+" and mag1_split_from_x_right[0] == "+":
        mag1 = mag1.replace("x", "1")
        mag1 = mag1.replace("y", '1')
    elif mag1[0] == "x" and mag1_split_from_y_left[-1] == "-" and mag1_split_from_x_right[0] == "-":
        mag1 = mag1.replace("x", "1")
        mag1 = mag1.replace("y", '1')   
    elif mag1[0] == "x" and mag1_split_from_y_left[-1] == "+" and mag1_split_from_x_right[0] == "+":
        mag1 = mag1.replace("x", "1")
        mag1 = mag1.replace("y", '1')

    elif mag1[0] == "-" and mag1_split_from_x_left[-1].isdigit() and mag1_split_from_y_left[-1] == "-" and mag1_split_from_x_right[0] ==  "-":
        mag1 = mag1.replace("x", '')
        mag1 = mag1.replace("y", "1")
    elif mag1[0] == "-" and mag1_split_from_x_left[-1] == "-" and mag1_split_from_y_left[-1].isdigit() and mag1_split_from_x_right[0] == "-":
        mag1 = mag1.replace("x", "1")
        mag1 = mag1.replace("y", '')   

    elif mag1[0] == "-" and mag1_split_from_x_left[-1].isdigit() and mag1_split_from_y_left[-1] == "+" and mag1_split_from_x_right[0] == "+":
        mag1 = mag1.replace("x", '')
        mag1 = mag1.replace("y", "1")
    elif mag1[0] == "-" and mag1_split_from_x_left[-1] == "-" and mag1_split_from_y_left[-1].isdigit and mag1_split_from_x_right[0] == "+":
        mag1 = mag1.replace("x", "1")
        mag1 = mag1.replace("y", '')    

    elif mag1[0] == "x" and mag1_split_from_y_left[-1].isdigit() and mag1_split_from_x_right[0] == "-":
        mag1 = mag1.replace("x", "1")
        mag1 = mag1.replace("y", '')
    elif mag1[0] == "x" and mag1_split_from_y_left[-1].isdigit() and mag1_split_from_x_right[0] == "+":
        mag1 = mag1.replace("x", '1')
        mag1 = mag1.replace("y", '')
    elif mag1[0].isdigit and mag1_split_from_x_left[-1].isdigit and mag1_split_from_y_left[-1] == "+" and mag1_split_from_x_right[0] == "+":
        mag1 = mag1.replace("x", '')
        mag1 = mag1.replace("y", "1")
    elif mag1[0].isdigit and mag1_split_from_x_left[-1].isdigit and mag1_split_from_y_left[-1] == "-" and mag1_split_from_x_right[0] == "-":
        mag1 = mag1.replace("x", "")
        mag1 = mag1.replace("y", "1")     
    break

while True:
    mag2 = input("{ ")

    mag2_split_from_x_right = mag2.partition("x")[2]
    mag2_split_from_x_left = mag2.partition("x")[0]
    mag2_split_from_y_left = mag2.partition("y")[0]
    answer2 = mag2.split("=",1)[1]
    if answer2.isalpha():
        print("enter only number as answer")
        continue     
    if mag2[0] == "-" and mag2_split_from_x_left[-1].isdigit() and mag2_split_from_y_left[-1].isdigit() and mag2_split_from_x_right[0] == "-":
        mag2 = mag2.replace("x", '')
        mag2 = mag2.replace("y", '')
    elif mag2[0] == "-" and mag2_split_from_x_left[-1].isdigit() and mag2_split_from_y_left[-1].isdigit() and mag2_split_from_x_right[0] == "+":
        mag2 = mag2.replace("x", '')
        mag2 = mag2.replace("y", '')
    elif mag2[0].isdigit() and mag2_split_from_x_left[-1].isdigit() and mag2_split_from_y_left[-1].isdigit() and mag2_split_from_x_right[0] == "-":
        mag2 = mag2.replace("x", '')
        mag2 = mag2.replace("y", '')
    elif mag2[0].isdigit() and mag2_split_from_x_left[-1].isdigit() and mag2_split_from_y_left[-1].isdigit() and mag2_split_from_x_right[0] == "+":
        mag2 = mag2.replace("x", '')
        mag2 = mag2.replace("y", '')
    
    elif mag2[0] == "-" and mag2_split_from_x_left[-1] == "-" and mag2_split_from_y_left[-1] == "-" and mag2_split_from_x_right[0] == "-":
        mag2 = mag2.replace("x", "1")
        mag2 = mag2.replace("y", '1')
    elif mag2[0] == "-" and mag2_split_from_x_left[-1] == "-" and mag2_split_from_y_left[-1] == "+" and mag2_split_from_x_right[0] == "+":
        mag2 = mag2.replace("x", "1")
        mag2 = mag2.replace("y", '1')
    elif mag2[0] == "x" and mag2_split_from_y_left[-1] == "-" and mag2_split_from_x_right[0] == "-":
        mag2 = mag2.replace("x", "1")
        mag2 = mag2.replace("y", '1')   
    elif mag2[0] == "x" and mag2_split_from_y_left[-1] == "+" and mag2_split_from_x_right[0] == "+":
        mag2 = mag2.replace("x", "1")
        mag2 = mag2.replace("y", '1')

    elif mag2[0] == "-" and mag2_split_from_x_left[-1].isdigit() and mag2_split_from_y_left[-1] == "-" and mag2_split_from_x_right[0] ==  "-":
        mag2 = mag2.replace("x", '')
        mag2 = mag2.replace("y", "1")
    elif mag2[0] == "-" and mag2_split_from_x_left[-1] == "-" and mag2_split_from_y_left[-1].isdigit() and mag2_split_from_x_right[0] == "-":
        mag2 = mag2.replace("x", "1")
        mag2 = mag2.replace("y", '')   

    elif mag2[0] == "-" and mag2_split_from_x_left[-1].isdigit() and mag2_split_from_y_left[-1] == "+" and mag2_split_from_x_right[0] == "+":
        mag2 = mag2.replace("x", '')
        mag2 = mag2.replace("y", "1")
    elif mag2[0] == "-" and mag2_split_from_x_left[-1] == "-" and mag2_split_from_y_left[-1].isdigit and mag2_split_from_x_right[0] == "+":
        mag2 = mag2.replace("x", "1")
        mag2 = mag2.replace("y", '')    

    elif mag2[0] == "x" and mag2_split_from_y_left[-1].isdigit() and mag2_split_from_x_right[0] == "-":
        mag2 = mag2.replace("x", "1")
        mag2 = mag2.replace("y", '')
    elif mag2[0] == "x" and mag2_split_from_y_left[-1].isdigit() and mag2_split_from_x_right[0] == "+":
        mag2 = mag2.replace("x", '1')
        mag2 = mag2.replace("y", '')

    elif mag2[0].isdigit and mag2_split_from_x_left[-1].isdigit and mag2_split_from_y_left[-1] == "+" and mag2_split_from_x_right[0] == "+":
        mag2 = mag2.replace("x", '')
        mag2 = mag2.replace("y", "1")
    elif mag2[0].isdigit and mag2_split_from_x_left[-1].isdigit and mag2_split_from_y_left[-1] == "-" and mag2_split_from_x_right[0] == "-":
        mag2 = mag2.replace("x", "")
        mag2 = mag2.replace("y", "1")     
    break

answer_matrix1 = mag1.split("=",1)[1]
answer_matrix2 = mag2.split("=",1)[1]

mag_without_answer1 = mag1.split("=",1)[0]
mag_without_answer2 = mag2.split("=",1)[0]

list_nums1 = nums_from_string.get_nums(mag_without_answer1)
list_nums2 = nums_from_string.get_nums(mag_without_answer2)


matrix_A_11 = list_nums1[0]
matrix_A_12 = list_nums1[1]
matrix_A_21 = list_nums2[0]
matrix_A_22 = list_nums2[1]

det_A = (matrix_A_11 * matrix_A_22) - (matrix_A_12 * matrix_A_21)
det_X = (int(answer1) * matrix_A_22) - (matrix_A_12 * int(answer2))
det_Y = (matrix_A_11 * int(answer2)) - (int(answer1) * matrix_A_21)

last_answer1 = Fraction(det_X, det_A)
last_answer2 = Fraction(det_Y, det_A)
print("=================")
print()
print("matrix A: ")
print()
print("(" + str(matrix_A_11), str(matrix_A_12) + ")")
print("(" + str(matrix_A_21), str(matrix_A_22) + ")")
print()
print("-----------------")
print()
print("matrix B: ")
print()
print("(" + str(answer1) + ")")
print("(" + str(answer2) + ")")
print()
print("-----------------")
print()
print("matrix X:")
print()
print("(" + str(answer1), str(matrix_A_12) + ")")
print("(" + str(answer2), str(matrix_A_22) + ")")
print()
print("-----------------")
print()
print("matrix Y:")
print()
print("(" + str(matrix_A_11), str(answer1) + ")")
print("(" + str(matrix_A_21), str(answer2) + ")")
print()
print("-----------------")
print()
print("determinant matrix A = " + str(det_A))
print()
print("determinant matrix X = " + str(det_X))
print()
print("determinant matrix Y = " + str(det_Y))
print()
print("-----------------")
print()
print("answer 1 = detX/detA")
print()
print("answer 1 = " + str(last_answer1))
print()
print("-----")
print()
print("answer 2 = detY/detA" )
print()
print("answer 2 = " + str(last_answer2))
print()
print("-----------------")
print()
print("final answer: " + str(last_answer1) + "; " + str(last_answer2))
print()
print()
print("===================== END =====================")
print()
print()