# from Inheritance.mix_it_6.project.technology.technology import Technology
# from Inheritance.mix_it_6.project.capacity_mixin import CapacityMixin
from project.capacity_mixin import CapacityMixin
from project.technology.technology import Technology


class SmartPhone(Technology):
    def __init__(self, memory, memory_taken):
        Technology.__init__(self, memory, memory_taken)

    def install_apps(self, app, app_memory):
        temp = CapacityMixin.get_capacity(self.memory-self.memory_taken, app_memory)
        if temp == "Capacity reached!":
            return f"You don't have enough space for {app}!"
        self.memory_taken += app_memory
        return temp


# sm = SmartPhone(10, 0)
# print(SmartPhone.install_apps(sm, "Tashaci" , 11))