# from Inheritance.restaurant_5.project.beverage.beverage import Beverage
from project.beverage.beverage import Beverage


class ColdBeverage(Beverage):
    def __init__(self, name, price, milliliters):
        Beverage.__init__(self, name, price, milliliters)
