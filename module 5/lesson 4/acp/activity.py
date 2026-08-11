class rev:
    def __init__(self,s):
        self.s = s


    def reversed(self):
        st = "".join(reversed(self.s))
        prev_st = "".join(reversed(st))
        if self.s == prev_st :
            return st

        

string = input("Please input a str to reverse the str>>>")
ob = rev(string)
print(ob.reversed())



for i in range(90):
    