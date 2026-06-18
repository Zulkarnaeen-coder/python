from abc import ABC, abstractmethod

class abcd(ABC):
    def print(self,x):
        print(f"The value of x is {self.x}")

    @abstractmethod
    def test(self):
        print('This is an abstraction method')



class abs_test(abcd) :
    def task(self):
        print("This is a sub class")

ob = abs_test()
ob.task()
ob.print(100)