class Car():

    total_car = 0

    def __init__ (self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1                                  #Class Variable

    def getbrand(self):                                     #Encapsulation
        return self.__brand

    # def full_name (self):
    #     return f"{self.__brand} {self.__model}"

    def get_fuletype(self):                                 #Polymorphism
        return "Petrol or Disel"
    
    @staticmethod                                           #Decorators
    def description():
        return "Baaj bno baaj, LaundiyaBaaj nhi"            #StaticMethod
    
    @property                                               #Property Decorator
    def getmodel(self):
        return self.__model
    

class ElectricCar(Car):                                     #Inheritance
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def get_fuletype(self):                                 #Polymorphism
        return "Electric Charge"
    

my_first_car = Car("BMW","X5")
my_second_car = Car("Morris Garage","Altroz")

tesla = ElectricCar("Tesla", "Series S", "25kWh")

print(my_first_car.getbrand)
# print(tesla.full_name())
print(Car.total_car)
print(Car.description())

print(isinstance(tesla, Car))                             #Instance
print(isinstance(tesla, ElectricCar))
