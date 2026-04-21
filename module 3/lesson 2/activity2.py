def by_3(n):
    if n%3==0:
        return cb(n)
    else:
        return False
    
def cb(n):
    return n*n*n

n =int(input("Please enter a num>>>"))

print(by_3(n))