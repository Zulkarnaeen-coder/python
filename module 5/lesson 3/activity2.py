class person:
    def __init__(self,name,idnum):
        self.name = name
        self.idnum =idnum

    def display(self):
        print(f"Your name is {self.name}")
        print(f"Your id num. ={self.idnum}")


class employee(person):
    def __init__(self, name, idnum,salary,post):
        super().__init__(name, idnum)
        self.salary = salary
        self.post = post

ob = employee("Mamun",199,1000,"guard")
print(f"My salary is {ob.salary} and my post is {ob.post}")
ob.display()        
        