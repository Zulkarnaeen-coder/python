vl = False
while not vl:
    try:
        n = int(input("Enter a num"))
        while n%2==0:
            print("Nye")
        vl =True
    except ValueError as ex:
        print(ex)