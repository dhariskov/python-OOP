from polymorphism.vehicles_1 import Truck, Car
import unittest


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car(100, 2)

    def test_drive_not_enough_fuel(self):
        self.car.drive(40)
        self.assertEqual(self.car.fuel_quantity, 100)

    def test_drive_enough_fuel(self):
        self.car.drive(10)
        self.assertEqual(self.car.fuel_quantity, 71)

    def test_refuel(self):
        self.car.refuel(50)
        self.assertEqual(self.car.fuel_quantity, 150)


class TestTruck(unittest.TestCase):
    def setUp(self):
        self.truck = Truck(100, 10)

    def test_truck_drive_not_enough_fuel(self):
        self.truck.drive(100)
        self.assertEqual(self.truck.fuel_quantity, 100)

    def test_truck_drive_enough_fuel(self):
        self.truck.drive(2)
        self.assertEqual(self.truck.fuel_quantity, 76.8)

    def test_truck_refuel(self):
        self.truck.refuel(10)
        self.assertEqual(self.truck.fuel_quantity, 109.5)


if __name__ == '__main__':
    unittest.main()
