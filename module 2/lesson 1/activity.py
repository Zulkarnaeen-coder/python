medical_cause = input("Do you have any medical cause (Y/N) >>>")

if medical_cause == "Y" :
    print("You are allowed for exam")

else :
    attendence = int(input("Please enter your attendance >>>"))

    if attendence >= 75:
        print("You are allowed for exam")

    else:
        print("You are not allowed for exam")