class employee :
    def __init__(self):
        print("Created successfully")

    def __delete__(self):
        print("Destructed ")

def creating():
    print("Making an object")
    obj = employee()
    print("Making successfully")

ob = creating()