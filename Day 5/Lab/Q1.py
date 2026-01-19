# Base class
class Vehicle:
    vehicle_count = 0

    def __init__(self, name):
        self.name = name
        Vehicle.vehicle_count += 1

    def start(self):
        print(f"{self.name} is starting...")

# Single Inheritance: Car inherits from Vehicle
class Car(Vehicle):
    def __init__(self, name, brand):
        super().__init__(name) 
        self.brand = brand

    def car_info(self):
        print(f"Car Name: {self.name}, Brand: {self.brand}")

# Multilevel Inheritance: ElectricCar -> Car -> Vehicle
class ElectricCar(Car):
    def __init__(self, name, brand, battery_capacity):
        super().__init__(name, brand)
        self.battery_capacity = battery_capacity

    def battery_info(self):
        print(f"{self.name} has a battery capacity of {self.battery_capacity} kWh")

# -------- Demonstration --------

# Vehicle object
v1 = Vehicle("Truck")
v1.start()
print("Total vehicles:", Vehicle.vehicle_count)
print()

# Car object (Single Inheritance)
c1 = Car("Sedan", "Toyota")
c1.start()       # Inherited from Vehicle
c1.car_info()
print("Total vehicles:", Vehicle.vehicle_count)
print()

# ElectricCar object (Multilevel Inheritance)
e1 = ElectricCar("Model S", "Tesla", 100)
e1.start()        # Inherited from Vehicle
e1.car_info()     # Inherited from Car
e1.battery_info()
print("Total vehicles:", Vehicle.vehicle_count)
