import os

print("Do you want to shut down your laptop or pc or desktop?(y/n)")

choose = input("Y/N>>>")
if choose =="Y"or choose=="y":
    os.system("shutdown /s /t 0")

elif choose=="N" or choose =="n":
    print()