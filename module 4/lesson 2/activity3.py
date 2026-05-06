weather =(1,0,0,0,1,0,1)
rain = 0
sun =0
for i in range(0,7):
    if weather[i]==1:
        rain +=1

    else:
        sun +=1


if sun>rain:
    print("Good weather")

else:
    print("bad weather")