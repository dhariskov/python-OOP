from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name: str, capacity: int):
        Factory.__init__(self, name, capacity)
        self.name = name
        self.capacity = capacity
        self.ingredients = {}
        #todo below will be dict of dicts
        self.recipes = {}
        self.products = {}

    # todo LOOK AT THIS ONE ONCE AGAIN IN CASE OF ISSUES
    def add_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type in ["white chocolate", "dark chocolate", "milk chocolate", "sugar"] and self.can_add(
                quantity):
            if ingredient_type not in self.ingredients:
                self.ingredients[ingredient_type] = quantity
            else:
                self.ingredients[ingredient_type] += quantity
            self.capacity -= quantity
        elif ingredient_type not in ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")
        elif not self.can_add(quantity):
            raise ValueError("Not enough space in factory")

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type in self.ingredients and self.ingredients[ingredient_type] >= quantity:
            self.ingredients[ingredient_type] -= quantity
            self.capacity += quantity
        elif ingredient_type not in self.ingredients:
            raise KeyError("No such product in the factory")
        elif self.ingredients[ingredient_type] < quantity:
            raise ValueError("Ingredient quantity cannot be less than zero")

    def add_recipe(self, recipe_name: str, recipe: dict):
        #todo recipe is ingridient type and quantities
        self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name: str):
        if recipe_name in self.recipes:
            if recipe_name not in self.products:
                self.products[recipe_name] = 1
            else:
                self.products[recipe_name] += 1
            self.remove_ingredient(recipe_name, 1)
            # for k, v in self.recipes.items():
            #     self.remove_ingredient(k, 1)
        else:
            raise TypeError("No such recipe")

# chocalate_factory = ChocolateFactory("Nmee", 100)
# chocalate_factory.add_ingredient("white chocolate", 10)
# chocalate_factory.add_ingredient("dark chocolate", 10)
# # chocalate_factory.add_ingredient("none", 10)
# # chocalate_factory.add_ingredient("dark chocolate", 1000)
# chocalate_factory.remove_ingredient("white chocolate", 1)
# # chocalate_factory.remove_ingredient("white chocolate", 10)
# # chocalate_factory.remove_ingredient("none", 1)
# chocalate_factory.add_recipe("white chocolate", {1: 2, 2: 3})
# chocalate_factory.add_recipe("white chocolate", {})
# chocalate_factory.make_chocolate()
# print()