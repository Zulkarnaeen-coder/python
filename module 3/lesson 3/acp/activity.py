def c(a,b):
    d = a-b
    s = str(d)+"0"
    return s

n1 =float(input("Enter the money that you given to shopkeeper>>> "))
n2 = float(input("Enter the total bill>>")) 

print("The shopkeeper will give you >",c(n1,n2))