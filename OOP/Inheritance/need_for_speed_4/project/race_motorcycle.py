# from Inheritance.need_for_speed_4.project.motorcycle import Motorcycle
from project.motorcycle import Motorcycle
# from Inheritance.need_for_speed_4.project.vehicle import Vehicle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = RaceMotorcycle.DEFAULT_FUEL_CONSUMPTION

# s_c = RaceMotorcycle(1000, 100)
# Vehicle.drive(s_c, 50)
# print(s_c.fuel_consumption)
# print(s_c.fuel)