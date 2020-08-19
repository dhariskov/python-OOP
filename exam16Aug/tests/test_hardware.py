class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):
        if self.can_install(software):
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software):
        self.software_components.remove(software)

    def get_light_software_components_count(self):
        return len([s for s in self.software_components if s.type == "Light"])

    def get_express_software_components_count(self):
        return len([s for s in self.software_components if s.type == "Express"])

    def can_install(self, software):
        has_space = sum([s.capacity_consumption for s in self.software_components]) + software.capacity_consumption <= self.capacity
        has_memory = sum([s.memory_consumption for s in self.software_components]) + software.memory_consumption <= self.memory
        return has_memory and has_space

    def __repr__(self):
        result = [f"Hardware Component - {self.name}",
                  f"Express Software Components: {self.get_express_software_components_count()}",
                  f"Light Software Components: {self.get_light_software_components_count()}",
                  f"Memory Usage: {sum([s.memory_consumption for s in self.software_components])} / {self.memory}",
                  f"Capacity Usage: {sum([s.capacity_consumption for s in self.software_components])} / {self.capacity}",
                  f"Type: {self.type}",
                  f"Software Components: {', '.join([str(s) for s in self.software_components]) if self.software_components else 'None'}"]

        return "\n".join(result)

class Software:
    def __init__(self, name:str, type:str, capacity_consumption:int, memory_consumption:int):
        self.name = name
        self.type = type
        self.capacity_consumption = capacity_consumption
        self.memory_consumption = memory_consumption

    def __repr__(self):
        return self.name

from project.software.software import Software


class ExpressSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, "Express", int(capacity_consumption), int(memory_consumption * 2))

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware

class Test:
    pass




import unittest

class TestHardware(unittest.TestCase):
    def setUp(self) -> None:
        self.hw = Hardware("Test", "Power", 100, 100)
        self.hw2 = Hardware("Test2", "Hevy", 200, 200)
        self.sw = ExpressSoftware("Sw", 10, 10)
        self.sw2 = ExpressSoftware("Sw1", 1, 1000)
        self.sw3 = ExpressSoftware("Sw2", 100000, 1)
        self.sw4 = ExpressSoftware("Sw3", 1000000, 1000000)

    def test_create_hardware(self):
        self.assertEqual(self.hw.name, "Test")
        self.assertEqual(self.hw.type, "Power")

    def test_create_ExpressSoftware(self):
        self.assertEqual(self.sw.name, "Sw")
        self.assertEqual(self.sw.memory_consumption, 20)
        self.assertEqual(self.sw.capacity_consumption, 10)

    def test_install(self):
        result = self.hw.install(self.sw)
        self.assertEqual(result, None)
        self.assertListEqual(self.hw.software_components, [self.sw])
        with self.assertRaises(Exception) as ex:
            self.hw.install(self.sw4)
        self.assertEqual(str(ex.exception), "Software cannot be installed")

    def test_uninstall(self):
        result1 = self.hw.install(self.sw)
        result = self.hw.uninstall(self.sw)
        self.assertEqual(result, None)
        self.assertListEqual(self.hw.software_components, [])


if __name__ == '__main__':
    unittest.main()