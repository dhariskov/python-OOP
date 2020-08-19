# from Inheritance.need_for_speed_4.project.car import Car
# from Inheritance.need_for_speed_4.project.vehicle import Vehicle
from project.car import Car
from project.vehicle import Vehicle


class FamilyCar(Car):

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)



# f_c = FamilyCar(3, 100)
# Vehicle.drive(f_c, 1)
# print(f_c.fuel_consumption)
# print(f_c.fuel)
