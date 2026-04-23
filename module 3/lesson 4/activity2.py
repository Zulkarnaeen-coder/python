try:
    n1,n2 =eval(int(input("Enter two num,seperate by a comma >>>")))
    result = n1/n2
    print("The result is",result)
except ZeroDivisionError:
    print("Divided by zero is wrong!!")

except SyntaxError:
    print("There is a syntax error !!")

except:
    print("Wrong Value!! ")
else:
    print("No Error")
finally:
    print("This is no matter but execute this line")