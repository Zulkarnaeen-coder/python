n = int(input("Please enter a num >>>"))

s = 0
temp = n

while temp >0:
    digit = temp%10
    s = s+digit**3
    temp = temp //10

if n == s:
    print(f"{n} is armstrong number")

else:
    print("not armstrong")