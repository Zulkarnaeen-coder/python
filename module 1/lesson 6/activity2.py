height = float(input("Please enter you height in C.M >>>"))
weigth  = float(input("Please enter you weight  in K.G >>>"))

bmi = weigth /(height /100)**2
print("Your bmi is",bmi)

if bmi <= 18.4:
    print("You are underweight")

elif bmi <= 24.9:
    print("You are healthy")

elif bmi <= 29.9:
    print("You are overheight")

elif bmi <=34.9:
    print("You are obeses")

else:
    print("You are several obeses")