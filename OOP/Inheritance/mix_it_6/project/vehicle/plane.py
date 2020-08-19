# from Inheritance.mix_it_6.project.vehicle.vehicle import Vehicle
# from Inheritance.mix_it_6.project.capacity_mixin import CapacityMixin
from project.capacity_mixin import CapacityMixin
from project.vehicle.vehicle import Vehicle

class Plane(Vehicle):
    def __init__(self, available_seats, rows, seats_per_row):
        Vehicle.__init__(self, available_seats)
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats_available = {}

    def buy_tickets(self, row_number, tickets_count):
        # if self.seats_available == {}:
        #     self.seats_available = {row: self.seats_per_row for row in range(1, self.rows + 1)}
        if not (0 < row_number <= self.rows):
            return f"There is no row {row_number} in the plane!"
        if row_number not in self.seats_available:
            self.seats_available[row_number] = self.seats_per_row
        temp = CapacityMixin.get_capacity(self.seats_available[row_number], tickets_count)
        if temp != "Capacity reached!":
            self.available_seats -= tickets_count
            self.seats_available[row_number] -= tickets_count
            return tickets_count
        return f"Not enough tickets on row {row_number}!"
