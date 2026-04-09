# দশমিক সংখ্যা ইনপুট নেওয়া
n = input("Enter a number(flaot): ")
dn = int(n)

bn = ""

if dn == 0:
    bn ="0"


while dn > 0:
    re = dn % 2  
    bn = str(re) + bn
    dn = dn // 2 

print("Binary:", bn)

