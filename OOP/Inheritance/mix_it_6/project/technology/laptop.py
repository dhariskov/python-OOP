# from Inheritance.mix_it_6.project.technology.technology import Technology
# from Inheritance.mix_it_6.project.capacity_mixin import CapacityMixin
from project.capacity_mixin import CapacityMixin
from project.technology.technology import Technology


class Laptop(Technology):
    def __init__(self, memory, memory_taken):
        Technology.__init__(self, memory, memory_taken)

    def install_software(self, software, software_memory):
        temp = CapacityMixin.get_capacity(self.memory-self.memory_taken, software_memory)
        if temp == "Capacity reached!":
            return f"You don't have enough space for {software}!"
        self.memory_taken += software_memory
        return temp


# sm = Laptop(10, 0)
# print(Laptop.install_software(sm, "Tashaci" , 1))