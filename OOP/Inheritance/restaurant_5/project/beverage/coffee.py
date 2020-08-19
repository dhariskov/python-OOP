# from Inheritance.restaurant_5.project.beverage.hot_beverage import HotBeverage
from project.beverage.hot_beverage import HotBeverage



class Coffee(HotBeverage):
    COFFEE_MILLILITERS = 50
    COFFEE_PRICE = 3.50

    def __init__(self, name, caffeine, price=COFFEE_PRICE, milliliters=COFFEE_MILLILITERS):
        HotBeverage.__init__(self, name, price, milliliters)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
