import random

nums =[1,2,3,4,5,6,7,8,9]
swords =[
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
cwords =[
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
infu = int(input("Enter a num for pass lenght>>"))
ln = random.randint(8,infu)
pre_password =[]



for i in range(1,ln+1):
    intorstr = random.randint(1,2)

    if intorstr ==1:
        chosenums = random.randint(1,len(nums))
        pre_password.append(chosenums)

    elif intorstr ==2:

        cors =random.randint(1,2)

        if cors ==1:
            incwords = random.randint(1,len(cwords))
            chosecwords = cwords[incwords]
            pre_password.append(chosecwords)

        elif cors ==2:
            insword = random.randint(1,len(swords))
            choseswords = swords[insword]
            pre_password.append(choseswords)

password =""
for j in pre_password:
    password+= str(j)

print(f"The generated pass word is :{password}")

