print("Please choose a ride !")
print("1.Bike")
print("2.Car")
choose = int(input("Please enter (only 1-2) >>>"))
if choose == 1 :
    print("Which type of bike you want?")
    print("1.Scooter")
    print("2.Scooty")

    choose2 = int(input("Please enter (only 1-2) >>>>"))

    if choose2 == 1 :
        print("You have choose a Scooter ")

    if choose2 == 2:
        print("You have choose a Scoter")

else :
    print("Which type of car you want?")
    print("1.Xuv")
    print("2.ROllS ROYALS")

    choose2 = int(input("Please enter (only 1-2) >>>>"))

    if choose2 == 1 :
        print("You have choose a Xuv ")

    if choose2 == 2:
        print("You have choose a Rolls Royals")