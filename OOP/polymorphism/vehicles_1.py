from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        Vehicle.__init__(self, fuel_quantity, fuel_consumption)

    def drive(self, distance):
        if self.fuel_quantity >= self.fuel_consumption*distance + distance*0.9:
            self.fuel_quantity -= self.fuel_consumption*distance + distance*0.9

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        Vehicle.__init__(self, fuel_quantity, fuel_consumption)

    def drive(self, distance):
        if self.fuel_quantity >= self.fuel_consumption * distance + distance * 1.6:
            self.fuel_quantity -= self.fuel_consumption * distance + distance * 1.6

    def refuel(self, fuel):
        self.fuel_quantity += fuel*0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

