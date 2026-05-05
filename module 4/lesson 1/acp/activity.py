squared =[]
even =[]
odd =[]
org =[]
stn = int(input("Please enter the first number(for range)>>"))
edn = int(input("Please enter the last number(for range)>>"))


for i in range(stn,edn +1):
    org.append(i)

for j in range(stn,edn + 1):

    j = j**2
    squared.append(j)

    if j % 2==0:
        even.append(j)

    else:
        odd.append(j)

print(f"The original numbers {org}")
print(f"The squared numbers {squared}")
print(f"The Even numbers {even}")
print(f"The Odd numbers {odd}")

