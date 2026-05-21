num1 =[1,2,3,4]
num2 =[5,6,7,8]

result = list(map(lambda x,y:x+y,num1,num2))
print(f"Adding = {result}")

def sq(n):
  return n*n
  
nums =[1,2,3,4,5,6,7,8]

re = list(map(sq,nums))

print("Mappping Value : ",re)