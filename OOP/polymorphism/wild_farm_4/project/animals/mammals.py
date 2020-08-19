# from polymorphism.wild_farm_4.project.animals.animal import Mammal
# from polymorphism.wild_farm_4.project.food import Vegetable, Fruit, Meat
from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def __init__(self, name, weight, living_region, food_eaten=0):
        Mammal.__init__(self, name, weight, living_region, food_eaten)

    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food):
        if not (isinstance(food, Vegetable) or isinstance(food, Fruit)):
            return f"{self.__class__.__name__} does not eat {type(food).__name__}!"
        self.food_eaten += food.quantity
        self.weight += 0.10 * food.quantity


class Dog(Mammal):
    def __init__(self, name, weight, living_region, food_eaten=0):
        Mammal.__init__(self, name, weight, living_region, food_eaten)

    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {type(food).__name__}!"
        self.food_eaten += food.quantity
        self.weight += 0.40 * food.quantity


class Cat(Mammal):
    def __init__(self, name, weight, living_region, food_eaten=0):
        Mammal.__init__(self, name, weight, living_region, food_eaten)

    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food):
        if not (isinstance(food, Vegetable) or isinstance(food, Meat)):
            return f"{self.__class__.__name__} does not eat {type(food).__name__}!"
        self.food_eaten += food.quantity
        self.weight += 0.30 * food.quantity


class Tiger(Mammal):
    def __init__(self, name, weight, living_region, food_eaten=0):
        Mammal.__init__(self, name, weight, living_region, food_eaten)

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {type(food).__name__}!"
        self.food_eaten += food.quantity
        self.weight += 1.00 * food.quantity
