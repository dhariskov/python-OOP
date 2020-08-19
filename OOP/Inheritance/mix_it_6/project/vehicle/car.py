# from Inheritance.mix_it_6.project.vehicle.vehicle import Vehicle
# from Inheritance.mix_it_6.project.capacity_mixin import CapacityMixin
from project.vehicle.vehicle import Vehicle
from project.capacity_mixin import CapacityMixin


class Car(Vehicle):
    def __init__(self, available_seats, fuel_tank, fuel_consumption, fuel):
        Vehicle.__init__(self, available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self.__fuel = fuel

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, fuel):
        if fuel + self.__fuel > self.fuel_tank:
            self.__fuel = self.fuel_tank
        else:
            self.__fuel = fuel

    def drive(self, distance):
        if distance*self.fuel_consumption <= self.__fuel:
            self.__fuel -= distance*self.fuel_consumption
            return "We've enjoyed the travel!"

    def refuel(self, liters):
        temp = CapacityMixin.get_capacity(self.fuel_tank - self.__fuel, liters)
        if temp == "Capacity reached!":
            # self.__fuel = self.fuel_tank
            return self.__fuel
        else:
            self.__fuel += liters
            return self.__fuel



