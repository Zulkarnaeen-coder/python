temp = float(input("Please Enter a Temperature >>>"))
#For 35-infinite deg.
if temp > 35 :
    temp = round(temp,2)
    print("The weather is too hot and the temp is ",temp,"and you should wear very soft dress!")

#For 34-29 deg.
elif temp <= 34 and temp > 29:
    temp = round(temp,2)
    print("The weather is hot and the temp is ",temp,"and you should wear soft dress!")
#For 29-25 deg.
elif temp < 29 and temp > 25 :
    temp = round(temp,2)
    print("The weather is quite hot and the temp is ",temp,"and you should wear normal soft dress!")
#For 24-20 deg.
elif temp < 24 and temp > 20 :
    temp = round(temp,2)
    print("The weather is quite cold and the temp is ",temp,"and you should wear soft huddyies!")
#For 20-0 deg.
elif temp < 20 and temp > 0 :
    temp = round(temp,2)
    print("The weather is cold and the temp is ",temp,"and you should wear hot or normal hoddies!")
#for below O deg.
else :
    temp = round(temp,2)
    print("The weather is too cold and the temp is ",temp,"and you have to wear big and hot sweater and under the sweather you should wear hoddies!")