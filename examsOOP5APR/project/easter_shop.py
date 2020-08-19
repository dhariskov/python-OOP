from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop:
    def __init__(self, name: str, chocolate_factory: ChocolateFactory, egg_factory: EggFactory,
                 paint_factory: PaintFactory):
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = {}

    def add_chocolate_ingredient(self, type: str, quantity: int):
        self.chocolate_factory.add_ingredient(type, quantity)

    def add_egg_ingredient(self, type: str, quantity: int):
        self.egg_factory.add_ingredient(type, quantity)

    def add_paint_ingredient(self, type: str, quantity: int):
        self.paint_factory.add_ingredient(type, quantity)

    def make_chocolate(self, recipe: str):
        # self.chocolate_factory.make_chocolate(recipe)
        if recipe not in self.storage:
            self.storage[recipe] = 1
        else:
            self.storage[recipe] += 1

    def paint_egg(self, color: str, egg_type: str):
        if egg_type in self.egg_factory.ingredients and color in self.paint_factory.ingredients:
            if f"{color} {egg_type}" not in self.storage:
                self.storage[f"{color} {egg_type}"] = 1
            else:
                self.storage[f"{color} {egg_type}"] += 1

            self.egg_factory.remove_ingredient(egg_type, 1)
            self.paint_factory.remove_ingredient(color, 1)
        else:
            raise ValueError("Invalid commands")

    def __repr__(self):
        result = f"Shop name: {self.name}\nShop Storage:\n"
        for k, v in self.storage.items():
            result += f"{k}: {v}\n"
        return result

# chocalate_factory=ChocolateFactory("Choco_fact", 100)
# chocalate_factory.add_recipe("white chocolate", {1: 2, 2: 2})
# chocalate_factory.add_recipe("dark chocolate", {3: 4, 4: 5})
# egg_factory=EggFactory("Egg_fact", 10)
# paint_factory=PaintFactory("Paint_fact", 100)
# shop = EasterShop("Shop", chocalate_factory, egg_factory, paint_factory)
# shop.add_chocolate_ingredient("white chocolate", 10)
# shop.add_chocolate_ingredient("dark chocolate", 10)
# shop.make_chocolate("white chocolate")
# print(shop)
# chocalate_factory.add_ingredient("dark chocolate", 10)
