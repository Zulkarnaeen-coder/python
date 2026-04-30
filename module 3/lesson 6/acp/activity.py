import calendar

year =int(input("Enter a year >>>"))

for i in range (1,13):
    print(calendar.month(year,i))