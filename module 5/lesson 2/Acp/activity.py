import math

pie = math.pi

class circul :
    def __init__(self,radius):
        self.radius = radius


    def area(self):
        return pie*(self.radius**2)
    
    def perimeter(self):

        return (2*pie)*self.radius



r = int(input("Enetr a number for radius>>"))

cc = circul(r)

a =cc.area()

p = cc.perimeter()

print(f"The perimeter of a circle is : {p}")

print(f"The area of a circle is : {a}")



