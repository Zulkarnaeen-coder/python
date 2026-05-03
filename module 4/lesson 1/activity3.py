l =[43,214,42,2,68765,43,23445,75634,23456,47,352,1,314]
print(f"Original num = {l}")

sum =0
for num in l:
    sum = sum + num

print(f"The total = {sum}")

avg = sum /len(l)
avg =round(avg,2)

print(f"The average = {avg}")

l.sort()

print(f"The smallest num = {l[0]}")
print(f"The largest num = {l[-1]}")
