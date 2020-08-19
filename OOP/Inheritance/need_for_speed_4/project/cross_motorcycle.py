# from Inheritance.need_for_speed_4.project.motorcycle import Motorcycle
from project.motorcycle import Motorcycle
from project.vehicle import Vehicle
# from Inheritance.need_for_speed_4.project.vehicle import Vehicle


class CrossMotorcycle(Motorcycle):
    def __init__(self,fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION

# s_c = CrossMotorcycle(1.25, 1000)
# Vehicle.drive(s_c, 1)
# print(s_c.fuel_consumption)
# print(s_c.fuel)