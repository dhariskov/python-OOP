# from Inheritance.mix_it_6.project.capacity_mixin import CapacityMixin
from project.capacity_mixin import CapacityMixin


class ParkingMall(CapacityMixin):
    def __init__(self, parking_lots):
        self.parking_lots = parking_lots

    def check_availability(self):
        temp = CapacityMixin.get_capacity(self.parking_lots, 1)
        if temp == "Capacity reached!":
            return "There are no more parking lots!"
        self.parking_lots -= 1
        return f"Parking lots available: {self.parking_lots}"

