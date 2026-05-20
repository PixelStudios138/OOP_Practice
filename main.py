class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):    
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
    def get_info(self):
        return f"{super().get_info()} with {self.num_doors} doors"
    
class ElectricCar(Car):
    def __init__(self, make, model, year, num_doors, battery_size):
        super().__init__(make, model, year, num_doors)
        self.battery_size = battery_size
    def get_info(self): 
        return f"{super().get_info()} and a {self.battery_size}-kWh battery"

class HyperCar(Car):
    def __init__(self, make, model, year, num_doors, top_speed):
        super().__init__(make, model, year, num_doors)
        self.top_speed = top_speed
    def get_info(self):
        return f"{super().get_info()} and a top speed of {self.top_speed} mph"
    
chiron = HyperCar("Bugatti", "Chiron", 2025, 2, False)
print(chiron.get_info())