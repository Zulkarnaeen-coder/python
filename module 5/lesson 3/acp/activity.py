class vehicle:
    def __init__(self,capasity):
        self.capasity  = capasity

    def fare(self):
        return self.capasity *100
    
    def display(self):
        print(f"The capasity of the vehicle is {self.caspasity}")
    

class bus(vehicle):
    def __init__(self, capasity,color,name):
        super().__init__(capasity)
        self.color =color
        self.name =name


    
    def fare(self):
        b_fare = super().fare()
        m_charge = b_fare*0.10
        total = m_charge + b_fare
        return total

ob = bus(50,"Red","School Bus")
print(f"The name of the vehicle is {ob.name} and its color is {ob.color}")
print(f"The fare of the vehicle is {ob.fare()}")        
        