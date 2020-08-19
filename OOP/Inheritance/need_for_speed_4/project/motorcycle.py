# from Inheritance.need_for_speed_4.project.vehicle import Vehicle
from project.vehicle import Vehicle


class Motorcycle(Vehicle):

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION


# s_c = Motorcycle(1.25, 100)
# Vehicle.drive(s_c, 1)
# print(s_c.fuel_consumption)
# print(s_c.fuel)
