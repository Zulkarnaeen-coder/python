class dog :
    spc ="Dog"
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    
bulldog = dog("Bulldog",10)
Pug = dog("Pug",15)

print(f"The first dog is {bulldog.name} and he is a {bulldog.spc} and he is {bulldog.age} years old;.")
print(f"The second dog is {Pug.name} and he is a {Pug.spc} and he is {Pug.age} years old;")