import random

nums =[1,2,3,4,5,6,7,8,9]
small_words =[
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
capital_words =[
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
input_from_user = int(input("Enter a num for pass lenght>>"))
lenght = random.randint(8,input_from_user)
pre_password =[]



for i in range(1,lenght+1):
    int_or_str = random.randint(1,2)


    if int_or_str ==1:
        chose_nums = random.randint(1,len(nums))
        pre_password.append(chose_nums)

    elif int_or_str ==2:

        capital_or_small =random.randint(1,2)

        if capital_or_small ==1:
            index_of_capital_words = random.randint(1,len(capital_words))
            chose_capital_words = capital_words[index_of_capital_words]
            pre_password.append(chose_capital_words)

        elif capital_or_small ==2:
            index_of_small_word = random.randint(1,len(small_words))
            chose_small_words = small_words[index_of_small_word]
            pre_password.append(chose_small_words)

password =""
for j in pre_password:
    password+= str(j)

print(f"The generated pass word is :{password}")

