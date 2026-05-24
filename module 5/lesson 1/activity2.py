class parrot :
    spc ="Bird"
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    
blu = parrot("Blu",10)
Woo = parrot("Woo",15)

print(f"The first parrot is {blu.name} and he is a {blu.spc} and he is {blu.age} years old;.")
print(f"The second parrot is {Woo.name} and he is a {Woo.spc} and he is {Woo.age} years old;.")