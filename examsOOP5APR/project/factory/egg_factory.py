from project.factory.factory import Factory


class EggFactory(Factory):
    def __init__(self, name: str, capacity: int):
        Factory.__init__(self, name, capacity)
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

        # todo LOOK AT THIS ONE ONCE AGAIN IN CASE OF ISSUES

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type in ["chicken egg", "quail egg"] and self.can_add(
                quantity):
            if ingredient_type not in self.ingredients:
                self.ingredients[ingredient_type] = quantity
            else:
                self.ingredients[ingredient_type] += quantity
            self.capacity -= quantity
        elif ingredient_type not in ["chicken egg", "quail egg"]:
            #todo check for the space
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")
        elif not self.can_add(quantity):
            raise ValueError("Not enough space in factory")

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type in self.ingredients and self.ingredients[ingredient_type] >= quantity:
            self.ingredients[ingredient_type] -= quantity
            self.capacity += quantity
        elif ingredient_type not in self.ingredients:
            raise KeyError("No such ingredient in the factory")
        elif self.ingredients[ingredient_type] < quantity:
            raise ValueError("Ingredient quantity cannot be less than zero")

    @property
    def products(self):
        return self.ingredients
