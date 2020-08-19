from abc import ABC

from project.software.software import Software


class Hardware(ABC):
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        if self.capacity - (sum([soft.capacity_consumption for soft in self.software_components]) + software.capacity_consumption) >= 0 and self.memory - (sum([soft.memory_consumption for soft in self.software_components]) + software.memory_consumption) >= 0:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software:Software):
        if software in self.software_components:
            self.software_components.remove(software)

