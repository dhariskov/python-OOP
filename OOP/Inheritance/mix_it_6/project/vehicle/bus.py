# from Inheritance.mix_it_6.project.vehicle.vehicle import Vehicle
# from Inheritance.mix_it_6.project.capacity_mixin import CapacityMixin
from project.capacity_mixin import CapacityMixin
from project.vehicle.vehicle import Vehicle

#ticket_sold maybe in constructor?
class Bus(Vehicle):
    def __init__(self, available_seats, ticket_price, tickets_sold=0):
        Vehicle.__init__(self, available_seats)
        self.ticket_price = ticket_price
        self.tickets_sold = tickets_sold

    def get_ticket(self, tickets_count):
        temp = CapacityMixin.get_capacity(self.available_seats, tickets_count)
        if temp != "Capacity reached!":
            self.tickets_sold += tickets_count
            self.available_seats -= tickets_count

    def get_total_profit(self):
        return self.tickets_sold*self.ticket_price

