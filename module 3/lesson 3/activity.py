word = input("Enter any word>>>")

for i in word:
    if (i =="A" or i == "a"):
        print("A has been found")
        break
    else:
        print("A hasn't benn found")