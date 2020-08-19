# from Inheritance.mix_it_6.project.parking_mall.parking_mall import ParkingMall
from project.parking_mall.parking_mall import ParkingMall


class Level3(ParkingMall):
    def __init__(self):
        ParkingMall.__init__(self, 80)
