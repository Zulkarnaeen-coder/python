n = int(input("Enter a row>>>"))

for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()