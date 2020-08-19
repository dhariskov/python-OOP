# from Inheritance.need_for_speed_4.project.car import Car
from project.car import Car
# from Inheritance.need_for_speed_4.project.vehicle import Vehicle


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = SportCar.DEFAULT_FUEL_CONSUMPTION

# s_c = SportCar(1000, 100)
# Vehicle.drive(s_c, 50)
# print(s_c.fuel_consumption)
# print(s_c.fuel)