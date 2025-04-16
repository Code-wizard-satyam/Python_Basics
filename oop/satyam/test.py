class Car():
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model

    def full_name (self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    

my_first_car = Car("BMW","X5")
my_second_car = Car("Morris Garage","Altroz")

tesla = ElectricCar("Tesla", "Series S", "25kWh")

print(my_first_car.full_name())
print(tesla.full_name())