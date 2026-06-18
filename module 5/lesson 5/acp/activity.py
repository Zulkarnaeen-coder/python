class bmw:
    def mx_speed(self):
        print("The max speed of Bwm is 250km/h")

    def fuel_tp(self):
        print("The fuel type of BMW is diesel")


class Ferrari:
    def mx_speed(self):
        print("\nThe max speed of Ferrari is 211km/h")

    def fuel_tp(self):
        print("The fuel type of Ferrari is gasoline")

ob = bmw()
of = Ferrari()

for i in (ob,of):
    i.mx_speed()
    i.fuel_tp()