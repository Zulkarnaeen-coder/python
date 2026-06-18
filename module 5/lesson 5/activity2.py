class sq :
    def __init__(self,side):
        self.side = side

    def area(self):
        print(f"The area of square is {self.side**2}")


class rec:
    def __init__(self, side,side1):
        self.side = side
        self.side1 = side1

    def area(self):
        print(f"The area of rectungle is {self.side*self.side1}")


class cir:
    def __init__(self, r):
        self.r = r

    def area(self):
        print(f"The area of circle is {3.14*self.r**2}")


osq = sq(4)
orec = rec(5,4)
ocir = cir(6)

for f in (osq,orec,ocir):
    f.area()
