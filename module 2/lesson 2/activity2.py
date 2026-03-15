str1 = input("Enter a word  >>>")

str2 = ""

for rv in str1:
    str2 = rv + str2

print(f"The reversed word {str2}")