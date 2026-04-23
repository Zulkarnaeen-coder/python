try:
    n =int(input("Enter a num>>"))
    print("The num you entered is >",n)

except ValueError as ex:
    print("Exception",ex)