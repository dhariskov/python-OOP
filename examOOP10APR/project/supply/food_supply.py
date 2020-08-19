from project.supply.supply import Supply


class FoodSupply(Supply):
    def __init__(self, needs_increase=20):
        Supply.__init__(self, needs_increase)

# f = FoodSupply(20)
# print(f.needs_increase)
