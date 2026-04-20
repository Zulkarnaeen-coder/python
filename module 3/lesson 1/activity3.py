def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print("Select the operation!")
print("a.Add")
print("b.Subtraction")
print("c.Multiplycation")
print("d.Devision")

ch = input("Please enter a choice (a,b,c,d)>>")

n1 = int(input("Please enter the first num >>"))
n2 = int(input("Please enter the second num >>"))

if ch =="a":
    print(n1," + ",n2," = ",add(n1,n2))

elif ch =="b":
    print(n1," - ",n2," = ",sub(n1,n2))

elif ch =="c":
    print(n1," x ",n2," = ",mul(n1,n2))

elif ch =="d":
    print(n1," / ",n2," = ",div(n1,n2))


else:
    print("The choice is incorrect!")