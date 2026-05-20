d1 ={"Codingal": 2 , "Is" : 2 , "Best": 2 , "For" : 2 , "Coding" : 1}

k = 2 
result = 0

for key in d1:
    if d1[key] == k:
        result = result + 1

print(f"Frequency == {result}")
exit()