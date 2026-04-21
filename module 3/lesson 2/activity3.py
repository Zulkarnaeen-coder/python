def fact(n):
    
    if n==0 or n==1:
        return 1
    
    else:
        return n*fact(n-1)
    
print("The fact of 0 is ",fact(0))
print("The fact of 10 is ",fact(10))
print("The fact of 100 is ",fact(100))