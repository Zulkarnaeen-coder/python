class rm:
    rm_dict = {
        1000: "m",
        900: "cm",
        500: "d",
        400: "cd",
        100: "c",
        90: "xc",
        50: "l",
        40: "xl",
        10: "x",
        9: "ix",
        5: "v",
        4: "iv",
        1: "i",
    }

    def to_rm(self, num):
        result = ""

        for v, sym in self.rm_dict.items():
            while num >= v:
                result += sym
                num -= v

        return result


ob = rm()
nu = int(input("Enter number for convert into roman"))
ob.to_rm(nu)

