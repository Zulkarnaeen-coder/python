import random

n =str(random.randint(0,9))
pl = True
print("I will generate a num . You'll guess th num!")
print("When you get the num ,you'll win")

while pl:
    guess = input("Enter your choice>>>")
    if guess == n:
        print("You guess the number!!")
        print("The number is",n)
        break
    else:
        print("Your guess is wrong .Try again!!")
        