import sys
dict_cars = {
        "Toyota Celica GT-four ST185": "1970",
        "Mazda Rx7": "1978",
        "Honda prelude": "1978",
        "Nissan 300ZX": "1978",
        "Toyota MR2 SW20": "1984",
        "Toyota AE86":"1985",
        "Toyota supra MK3": "1986",
        "Honda NSX": "1990",
        "Mitsubishi 3000 GT": "1991",
        "Lexus SC300": "1992",
        "Toyota supra MK4": "1994",
        "Nissan Silvia S14": "1994",
        "Subaru impreza WRX STI": "1994",
        "Nissan silvia S15": "1995",
        "Honda civic EK9": "1997",
        "Mazda miata MX-5": "1998",
        "Nissan GTR 34": "1998",
        "Subaru legacy B4 RSK": "1998",
        "Honda S2000": "1999",
        "Nissan 350Z": "2002",
        "Infiniti G35": "2003",
        "Mitsubishi evolution 9": "2005" }
def main():
        while True:
                yes_no = ["yes", "no"]
                ask_year = input("is your car made between 1970 - 1990? ")
                if ask_year not in yes_no:
                        continue
                elif ask_year == "yes":
                        cars_between_1970_1990()
                        sys.exit(0)
                elif ask_year == "no":
                        while True:
                                ask_year = input("is your car made between 1990 - 2000? ")
                                if ask_year not in yes_no:
                                        continue
                                elif ask_year == "yes":
                                        cars_between_1990_2000()
                                        sys.exit(0)
                                elif ask_year == "no":
                                        while True:
                                                ask_year = input("is your car made between 2000 - 2005? ")
                                                if ask_year not in yes_no:
                                                        continue
                                                elif ask_year == "yes":
                                                        cars_between_2000_2005()
                                                elif ask_year == "no":
                                                        break
                                break
                continue
def cars_between_1970_1990():
        while True:
                yes_no = ["yes", "no"]
                list_of_cars_1970_1990 = ["toyota", "mazda", "honda", "nissan"]
                ask_for_toyota = input("is your car " + list_of_cars_1970_1990[0] + "? ")
                if ask_for_toyota not in yes_no:
                        continue
                elif ask_for_toyota == "yes":
                        while True:    # edit for toyota
                                ask_for_celica = input("does it look like new hellcat? ")
                                if ask_for_celica not in yes_no:
                                        continue
                                elif ask_for_celica == "yes":
                                        print("your car is Toyota celica GT4")
                                        sys.exit(0)
                                elif ask_for_celica == "no":
                                        while True:
                                                ask_for_MR2 = input("does it have miata-like headlights? ")
                                                if ask_for_MR2 not in yes_no:
                                                        continue
                                                elif ask_for_MR2 == "yes":
                                                        print("your car is toyota MR2")
                                                        sys.exit(0)
                                                elif ask_for_MR2 == "no":
                                                        while True:
                                                                ask_for_AE86 = input("is it legendary trueno? ")
                                                                if ask_for_AE86 not in yes_no:
                                                                        continue
                                                                elif ask_for_AE86 == "yes":
                                                                        print("your car is toyota AE86")
                                                                        sys.exit(0)
                                                                elif ask_for_AE86 == "no":
                                                                        print("your car is Toyota supra MK3")
                                                                        sys.exit(0)
                elif ask_for_toyota == "no":
                        while True:
                                ask_for_mazda = input("is your car " + list_of_cars_1970_1990[1] + "? ")
                                if ask_for_mazda not in yes_no:
                                        continue
                                elif ask_for_mazda == "yes":
                                        print("your car is Mazda Rx7")
                                        sys.exit(0)
                                elif ask_for_mazda == "no":
                                        while True:
                                                ask_for_honda = input("is your car " + list_of_cars_1970_1990[2] + "? ")
                                                if ask_for_honda not in yes_no:
                                                        continue
                                                elif ask_for_honda == "yes":
                                                        while True:
                                                                ask_for_prelude = input("is it one of the most hated car? ")
                                                                if ask_for_prelude not in yes_no:
                                                                        continue
                                                                elif ask_for_prelude == "yes":
                                                                        print("your car is honda prelude")
                                                                        sys.exit(0)
                                                                elif ask_for_prelude == "no":
                                                                        print("your car is honda NSX")
                                                                        sys.exit((0))


                                                elif ask_for_honda == "no":
                                                        while True:
                                                                ask_for_nissan = input("is your car " + list_of_cars_1970_1990[3] + "? ")
                                                                if ask_for_nissan not in yes_no:
                                                                        continue
                                                                elif ask_for_nissan == "yes":
                                                                        print("your guess is Nissan 300ZX")
                                                                        sys.exit(0)
                                                                elif ask_for_nissan == "no":
                                                                        break
                                                break
                                break
                continue
def cars_between_1990_2000():
         while True:
                 yes_no = ["yes", "no"]
                 list_of_cars_1990_2000 = ["mitsubishi", "lexus", "toyota", "nissan", "subaru", "honda", "mazda"]
                 ask_for_mitsubishi = input("is your car " + list_of_cars_1990_2000[0] + "? ")
                 if ask_for_mitsubishi not in yes_no:
                         continue
                 elif ask_for_mitsubishi == "yes":
                         print("your car is Mitsubishi 3000 GT")
                         sys.exit(0)
                 elif ask_for_mitsubishi == "no":
                         while True:
                                 ask_for_lexus = input("is your car " + list_of_cars_1990_2000[1] + "? ")
                                 if ask_for_lexus not in yes_no:
                                         continue
                                 elif ask_for_lexus == "yes":
                                         print("your car is Lexus SC300")
                                         sys.exit(0)
                                 elif ask_for_lexus == "no":
                                         while True:
                                                 ask_for_toyota = input(
                                                         "is your car " + list_of_cars_1990_2000[2] + "? ")
                                                 if ask_for_toyota not in yes_no:
                                                         continue
                                                 elif ask_for_toyota == "yes":
                                                         print("your car is Toyota supra MK 4")
                                                         sys.exit(0)
                                                 elif ask_for_toyota == "no":
                                                         while True:
                                                                 ask_for_nissan = input(
                                                                         "is your car " + list_of_cars_1990_2000[3] + "? ")
                                                                 if ask_for_nissan not in yes_no:
                                                                         continue
                                                                 elif ask_for_nissan == "yes":
                                                                         ask_for_s14 = input("is it one of the best drift cars? ")
                                                                         if ask_for_s14 not in yes_no:
                                                                                 continue
                                                                         elif ask_for_s14 == "yes":
                                                                                 print("your car is Nissan siliva S14")
                                                                                 sys.exit(0)
                                                                         elif ask_for_s14 == "no":
                                                                                 while True:
                                                                                         ask_for_s15 = input("is it new gen of one of the best drift car? ")
                                                                                         if ask_for_s15 not in yes_no:
                                                                                                 continue
                                                                                         elif ask_for_s15 == "yes":
                                                                                                 print("your car is Nissan silvia S15")
                                                                                                 sys.exit(0)
                                                                                         elif ask_for_s15 == "no":
                                                                                                 print("your car is Nissan GTR 34")
                                                                                                 sys.exit(0)
                                                                 elif ask_for_nissan == "no":
                                                                         while True:
                                                                                 ask_for_subaru = input("is your car " + list_of_cars_1990_2000[4] + "? ")
                                                                                 if ask_for_subaru not in yes_no:
                                                                                         continue
                                                                                 elif ask_for_subaru == "yes":
                                                                                         while True:
                                                                                                 ask_for_wrx = input("is it one of the most loved Subaru? ")
                                                                                                 if ask_for_wrx not in yes_no:
                                                                                                         continue
                                                                                                 elif ask_for_wrx == "yes":
                                                                                                         print("your car is Subaru WRX STI")
                                                                                                         sys.exit(0)
                                                                                                 elif ask_for_wrx == "no":
                                                                                                         print("your car is Subaru legacy")
                                                                                                         sys.exit(0)
                                                                                 elif ask_for_subaru == "no":
                                                                                         while True:
                                                                                                 ask_for_honda = input(
                                                                                                         "is your car " +
                                                                                                         list_of_cars_1990_2000[
                                                                                                                 5] + "? ")
                                                                                                 if ask_for_honda not in yes_no:
                                                                                                         continue
                                                                                                 elif ask_for_honda == "yes":
                                                                                                         while True:
                                                                                                                 ask_for_civic = input("is your honda goofy looking? ")
                                                                                                                 if ask_for_civic not in yes_no:
                                                                                                                         continue
                                                                                                                 elif ask_for_civic == "yes":
                                                                                                                         print("your car is Honda civic")
                                                                                                                         sys.exit(0)
                                                                                                                 elif ask_for_civic == "no":
                                                                                                                        print("your car is Honda S2000")
                                                                                                                        sys.exit(0)
                                                                                                         sys.exit(0)
                                                                                                 elif ask_for_honda == "no":
                                                                                                         while True:
                                                                                                                 ask_for_mazda = input(
                                                                                                                         "is your car " +
                                                                                                                         list_of_cars_1990_2000[
                                                                                                                                 6] + "? ")
                                                                                                                 if ask_for_mazda not in yes_no:
                                                                                                                         continue
                                                                                                                 elif ask_for_mazda == "yes":
                                                                                                                        print("your car is Mazda miata")
                                                                                                                        sys.exit(0)
                                                                                                                 elif ask_for_mazda == "no":
                                                                                                                         break
                                                                                                 break
                                                                                 break
                                                                 break
                                                 break
                                 break
                 continue
def cars_between_2000_2005():
        while True:
                yes_no = ["yes", "no"]
                list_of_cars_2000_2005 = ["nissan", "mitsubishi", "infiniti"]
                ask_for_nissan = input("is your car " + list_of_cars_2000_2005[0] + "? ")
                if ask_for_nissan not in yes_no:
                        continue
                elif ask_for_nissan == "yes":
                        print("your car is Nissan 350Z")
                        sys.exit(0)
                elif ask_for_nissan == "no":
                        while True:
                                ask_for_mitsubishi = input("is your car " + list_of_cars_2000_2005[1] + "? ")
                                if ask_for_mitsubishi not in yes_no:
                                        continue
                                elif ask_for_mitsubishi == "yes":
                                        print("your car is Mitsubishi evolution 9")
                                        sys.exot(0)
                                elif ask_for_mitsubishi == "no":
                                        while True:
                                                ask_for_infiniti = input("is your car " + list_of_cars_2000_2005[2] + "? ")
                                                if ask_for_infiniti not in yes_no:
                                                        continue
                                                elif ask_for_infiniti == "yes":
                                                        print("your car is Infiniti G35")
                                                        sys.exit(0)
                                                elif ask_for_infiniti == "no":
                                                        break

                                break
                continue
main()