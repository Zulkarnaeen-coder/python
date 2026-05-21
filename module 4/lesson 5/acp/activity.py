n =int(input("Enetr a num:"))
odd =[x for x in range(1,n+1) if x%2!=0]
print(f"The odd numbers is {odd}")



fruits =["banana","apple","qiwi","strawberry","pineapple"]
up_fruits =[]

print(f"\nThe orginal list {fruits}")

for f in fruits:
    up_fruits.append(f.capitalize())

print(up_fruits)

