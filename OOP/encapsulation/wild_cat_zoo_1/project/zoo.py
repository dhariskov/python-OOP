# from encapsulation.wild_cat_zoo_1.project.caretaker import Caretaker
# from encapsulation.wild_cat_zoo_1.project.cheetah import Cheetah
# from encapsulation.wild_cat_zoo_1.project.keeper import Keeper
# from encapsulation.wild_cat_zoo_1.project.lion import Lion
# from encapsulation.wild_cat_zoo_1.project.tiger import Tiger
# from encapsulation.wild_cat_zoo_1.project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        if self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salaries = sum([w.salary for w in self.workers])

        if self.__budget >= sum_salaries:
            self.__budget -= sum_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_tends = sum([a.get_needs() for a in self.animals])
        if self.__budget >= total_tends:
            self.__budget -= total_tends
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        if amount > 0:
            self.__budget += amount

    def animals_status(self):
        lions = [a.__repr__() for a in self.animals if type(a).__name__ == 'Lion']
        tigers = [a.__repr__() for a in self.animals if type(a).__name__ == 'Tiger']
        cheetahs = [a.__repr__() for a in self.animals if type(a).__name__ == 'Cheetah']

        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        result += '\n'.join(lions) + "\n"
        result += f"----- {len(tigers)} Tigers:\n"
        result += '\n'.join(tigers) + "\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        result += '\n'.join(cheetahs)

        return result

    def workers_status(self):
        keepers = [a.__repr__() for a in self.workers if type(a).__name__ == 'Keeper']
        caretakers = [a.__repr__() for a in self.workers if type(a).__name__ == 'Caretaker']
        vets = [a.__repr__() for a in self.workers if type(a).__name__ == 'Vet']

        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        result += '\n'.join(keepers) + "\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        result += '\n'.join(caretakers) + "\n"
        result += f"----- {len(vets)} Vets:\n"
        result += '\n'.join(vets)

        return result

# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
# print(zoo.fire_worker("Mitko"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())
