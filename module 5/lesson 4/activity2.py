class comp :
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(self.__maxprice)


    def setmaxprice(self,price):
        self.__maxprice = price


ob = comp()
ob.sell()

ob.setmaxprice(1200)
ob.sell()