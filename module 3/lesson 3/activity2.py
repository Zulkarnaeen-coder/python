n =int(input("Please enter a num >>>"))

if n%20==0:
    print("Twist")

elif n%15==0:
    pass

elif n%5==0:
    print("Fizz")

elif n%3==0:
    print("Buzz")

else:
    print(n)