s = input("Please enter your own word : ")
c = input("Please enter your own Character : ")
i = 0
count = 0
#loop will to find the occurence of character
while(i < len(s)): #string operation

    if(s[i] == c): #condition 1
        count = count + 1
    i = i + 1

#Display the result
print("The total Number of Times ", c, " has Occurred = " , count)
