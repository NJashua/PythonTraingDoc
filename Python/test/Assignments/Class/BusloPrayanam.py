class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def vehicleFair(self):
        return self.capacity * 100

class Bus(Vehicle):
    def busfair(self):
        bus_extra_charge = super().vehicleFair()
        if "bus" in self.name:  
            total_ammount = bus_extra_charge + (bus_extra_charge * 0.10)   
        return f"The total bus fare is {total_ammount}"        


obj1 = Bus("bus", 25, 50)

print(obj1.busfair())