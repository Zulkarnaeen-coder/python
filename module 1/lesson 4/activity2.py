amount = int(input('Please enter a amount : '))

tk_100 = amount//100
tk_50  = (amount%100)//50
tk_10 = ((amount%100)%50)//10

print("The notes of 100 tk :",tk_100)
print("The notes of 50 tk :",tk_50)
print("The notes of 10 tk :",tk_10)
