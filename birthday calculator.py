import random
import collections
import sys
def ask():
    while True:
        ask = input("do you want to play? yes/no ")
        if ask == "yes":
            game()
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
def game():
    while True:
        try:
            print()
            print("----------------------------------")
            print()
            number_bday = int(input("how many birthdays shall i generate? "))
            if number_bday <= 0:
                continue
            else: 
                list_months = ["jan", "feb", "march", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
                list_bdays = []  # list of all dates
                for i in range(number_bday):
                    date =random.choice(list_months) + " " + str(random.randint(1,31))
                    list_bdays.append(date)
                list_duplicates = [item for item, count in collections.Counter(list_bdays).items() if count > 1] # list of duplicates
                c = -1
                dup_count_list = []
                for i in range(len(list_duplicates)):
                    dup_count = str(list_bdays.count(list_duplicates[c+1]))
                    dup_count_list.append(int(dup_count))
                    c = c + 1
                print()
                print("here are " + str(number_bday) + " bdays:")
                print()
                print(*list_bdays, sep = ', ')
                print()
                if not dup_count_list:
                    print("oops, there are no duplicates")
                    print()
                    print("---------------------")
                    print()
                    game()
                elif len(set(dup_count_list)) == 1:
                    date_to_operate = random.choice(list_duplicates) 
                    print()
                    print("in this simulation " + str(dup_count_list[-1]) + " people have birthday on " + str(date_to_operate))
                    print()
                    probability = int(dup_count_list[-1]) * 100 / int(number_bday)
                    print("probablity of " + str(dup_count_list[-1]) + " people be born on this date is " + str(probability) + "%")
                    print()
                    ask()
                elif len(set(dup_count_list)) != 1:
                    k = -1
                    for i in range(len(dup_count_list)):
                        dup_count_list_sorted = sorted(dup_count_list)
                        if dup_count_list[k + 1] == dup_count_list_sorted[-1]:
                            date_to_operate = list_duplicates[k+1]
                        k = k + 1  
                    print("in this simulation " + str(dup_count_list_sorted[-1]) + " people have birthday on " + str(date_to_operate))
                    probability2 = int(dup_count_list_sorted[-1]) * 100 / int(number_bday)
                    print()
                    print("probablity of " + str(dup_count_list_sorted[-1]) + " people be born on this date is " + str(probability2) + "%")
                    print()
                    ask()      
            break
        except ValueError:
            continue
        except IndexError:
            continue
game()