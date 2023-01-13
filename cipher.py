from distutils.dir_util import copy_tree
import string
import sys

from numpy import number

print("--------------------------------------")     
print()
print("Welcome to the Caesars encrpyther/decrypter..")
print()
def main():
    while True:
        print("--------------------------------------")
        print()
        print("do you want (e)ncrypt or (d)ecrypt? (to exit anytime, type 'exit ')")
        print()
        a = input("-- ")
        if a == "e":
            encrypt()     # if encrpyt: encrypt
        elif a == "d":
            decrypt()
        elif a == "exit":
            print()
            print("|--------------------|")
            print("|                    |")
            print("|      bye. :^)      |")
            print("|                    |")
            print("|--------------------|")
            print()
            sys.exit(0)
        else:
            continue
        
    
def encrypt():        
    number_encrypt = ask_for_num()    # runs ask_for_num() and saves return as "number_encrypt"

    list_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    print("enter sentence: ")
    sentence = input("-- ")

    k = -1

    encrypt_sentence = []

    for i in range(len(sentence)):
        while True:
            if sentence[k+1].isalpha():
                index_orig_sentence = list_alphabet.index(sentence[k+1])
                word = list_alphabet[index_orig_sentence + number_encrypt]
                encrypt_sentence.append(word)
                k = k + 1
                break
            elif sentence[k+1] == " ":
                encrypt_sentence.append(" ")
                k = k + 1
                break
            elif sentence[k+1] == ",":
                encrypt_sentence.append(",")
                k = k + 1
                break
            elif sentence[k+1] == ".":
                encrypt_sentence.append(".")
                k = k + 1
                break
            elif sentence[k+1] == "!":
                encrypt_sentence.append("!")
                k = k + 1
                break
            elif sentence[k+1] == "?":
                encrypt_sentence.append("?")
                k = k + 1
                break
            elif sentence[k+1] == ":":
                encrypt_sentence.append(":")
                k = k + 1
                break
            elif sentence[k+1] == '"':
                encrypt_sentence.append('"')
                k = k + 1
                break 
            elif sentence[k+1] == '"':
                encrypt_sentence.append('"')
                k = k + 1
                break           
            elif sentence == "exit":
                print()
                print("|--------------------|")
                print("|                    |")
                print("|      bye. :^)      |")
                print("|                    |")
                print("|--------------------|")
                print()
                sys.exit(0)

    print()
    print("encrypted sentence: ")
    print()
    print(*encrypt_sentence, sep = '')
    print()
    ask()





def decrypt():
    number_decrpyt = ask_for_num()    # runs ask_for_num() and saves return as "number_encrypt"

    list_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    print("enter sentence: ")
    sentence = input("-- ")
    list_rev = list(reversed(list_alphabet))
    k = -1

    encrypt_sentence = []

    for i in range(len(sentence)):
        while True:
            if sentence[k+1].isalpha():
                index_orig_sentence = list_rev.index(sentence[k+1])
                word = list_rev[index_orig_sentence + number_decrpyt]
                encrypt_sentence.append(word)
                k = k + 1
                break
            elif sentence[k+1] == " ":
                encrypt_sentence.append(" ")
                k = k + 1
                break
            elif sentence[k+1] == ",":
                encrypt_sentence.append(",")
                k = k + 1
                break
            elif sentence[k+1] == ".":
                encrypt_sentence.append(".")
                k = k + 1
                break
            elif sentence[k+1] == "!":
                encrypt_sentence.append("!")
                k = k + 1
                break
            elif sentence[k+1] == "?":
                encrypt_sentence.append("?")
                k = k + 1
                break
            elif sentence[k+1] == ":":
                encrypt_sentence.append(":")
                k = k + 1
                break
            elif sentence[k+1] == '"':
                encrypt_sentence.append('"')
                k = k + 1
                break 
            elif sentence[k+1] == '"':
                encrypt_sentence.append('"')
                k = k + 1
                break 
            elif sentence == "exit":
                print()
                print("|--------------------|")
                print("|                    |")
                print("|      bye. :^)      |")
                print("|                    |")
                print("|--------------------|")
                print()
                sys.exit(0)

    print()
    print("decrypted sentence: ")
    print()
    print(*encrypt_sentence, sep = '')
    print()
    ask()

def ask_for_num():       # asking number
    while True:
        try:
            print()
            number_encrypt = int(input("Please enter the key (0 to 25) to use: "))
            print()
            if number_encrypt < 0:
                continue
            elif number_encrypt > 25:
                continue
            else:
                return number_encrypt
        except ValueError:
            continue

def ask():
    while True:
        print()
        print("do you want to play? yes/no ")
        print()
        ask = input("-- ")
        if ask == "yes":
            main()
        elif ask == "no":
            print()
            print("|--------------------|")
            print("|                    |")
            print("|      bye. :^)      |")
            print("|                    |")
            print("|--------------------|")
            print()
            sys.exit(0)
        else:
            continue


main()   # starting program