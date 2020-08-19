class Car:
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"

    def __str__(self):
        return self.get_info()


car = Car("Kia", "Rio", "1.3L B3 I4")
print(car.get_info())

car1 = Car("Tashaci", "na", "roqci")
print(car1.get_info())