d1 = {
    "Md.Hossain":780,
    "Munira":785,
    "Tasmia":790,
    "Mamun":760,
    "zulkar":770
}

print("The orginal dictonary",d1)
re =0
for v in d1.values():
    re +=v
    
avg = re/2
print("The average num :",avg)

print(d1)
user = input("Find the name from the dictonary>>")

s =d1.get(user,"cant found!!")

print(s)

