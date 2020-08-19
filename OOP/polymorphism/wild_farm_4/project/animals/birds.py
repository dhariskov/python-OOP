# from polymorphism.wild_farm_4.project.animals.animal import Bird
# from polymorphism.wild_farm_4.project.food import Vegetable, Fruit, Meat
from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Meat


class Owl(Bird):
    def __init__(self, name, weight, wing_size, food_eaten=0):
        Bird.__init__(self, name, weight, wing_size, food_eaten)

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {type(food).__name__}!"
        self.food_eaten += food.quantity
        self.weight += 0.25 * food.quantity


class Hen(Bird):
    def __init__(self, name, weight, wing_size, food_eaten=0):
        Bird.__init__(self, name, weight, wing_size, food_eaten)

    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food):
        self.food_eaten += food.quantity
        self.weight += 0.35 * food.quantity


# owl = Owl("Pip", 10, 10)
# print(owl)
# print(type(owl).__name__)
# print(owl.__class__.__name__)
# hen = Hen("Harry", 10, 10)
# veg = Vegetable(3)
# fruit = Fruit(5)
# meat = Meat(1)
# print(hen)
# print(hen.make_sound())
# hen.feed(veg)
# hen.feed(fruit)
# hen.feed(meat)
# print(hen)

