class IOstring:
    def __init__(self):
        self.st1 =""

    def g_string(self):
        self.st1 =input("Enter a string")
    
    def p_str(self):
        print("The Result :",self.st1.upper())



st = IOstring()

st.g_string()
st.p_str()