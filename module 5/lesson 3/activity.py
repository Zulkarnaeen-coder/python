class dad :
    def __init__(self,eye,height):
        self.eye = eye 
        self.height = height

    def display(self):
        print("Your eyes are ",self.eye)
        print("You are ",self.height,"inch tall")


class son(dad):
    def __init__(self,name,age, eye, height):
        self.name = name
        self.age = age
        dad.__init__(self,eye, height)


ob = son("Hasan",14,"Brown",15)
print(f"Your name is {ob.name} and you are {ob.age} years old and your eyes are {ob.eye} and you are {ob.height} inch tall")

ob.display()