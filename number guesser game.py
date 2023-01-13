import sys
import random as r

print("----------------------------------------------------")
print()
print("I am thinking of a 3-digit number, without any duplicate digits. Try to guess what it is.")
print("When i say:       That means:")
print("  almost        digit is correct but in the wrong position.")
print("  hit           digit is correct but in the right position.")
print("  miss          digit is not correct.")
print()
print("I've thought of a number")
print("you have 10 guesses, good luck!")
print()  
def ask():
    while True:
        ask = input("do you want to play again? (yes/no) ")
        if ask == "yes":
            game()
        elif ask == "no":
            print()
            print("bye.. :^)")
            print("=======================================")
            sys.exit(0)
        else:
            print()
            print("enter yes or no")
            print()
            continue
def game():
    print("=======================================")
    while True:
        a = r.randint(100,999)
        res = [int(x) for x in str(a)]
        if len(res) != len(set(res)):
            continue
        else:
            chafiqrebuli = ''
            for element in res:  
                chafiqrebuli += str(element)   
            break
    #print(chafiqrebuli)
    guess_number = 1
    c = -1
    for i in range(10):
        print()
        while True:
            gamocnoba = input("guess" + "#" + str(guess_number) + " ")
            if gamocnoba == "paroli":
                print(chafiqrebuli)
                sys.exit(0)
            if len(gamocnoba) != 3:
                continue
            elif gamocnoba.isalpha():
                continue
            elif gamocnoba == "paroli":
                print(chafiqrebuli)
                break
            else:
                break
        print()
        if chafiqrebuli == gamocnoba:
            print()
            print("you win")
            print()
            ask()
        c = -1
        for i in range(3):
            if chafiqrebuli[c+1] == gamocnoba[c+1]:
                print("hit")
            elif chafiqrebuli[c+1] != gamocnoba[c+1] and gamocnoba[c+1] in chafiqrebuli:         # zustad ar udris magram aris ricxvshi
                print("almost")
            elif gamocnoba[c+1] != chafiqrebuli[c+1] and gamocnoba[c+1] not in chafiqrebuli:
                if gamocnoba[c+1] < chafiqrebuli[c+1]:
                    print("miss (guss more)")
                elif gamocnoba[c+1] > chafiqrebuli[c+1]:
                    print("miss (guess less)")
            c = c + 1
        guess_number = guess_number + 1
    print()
    print("you lost.. :(")
    print()
    ask()
game()