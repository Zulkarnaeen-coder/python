class myclass :
    __x = 24


    def __mymet(self):
        print("This is private")

    def myfunc(self):
        print(myclass.__x)


ob = myclass()

ob.myfunc()
ob.__mymet()