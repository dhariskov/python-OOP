from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        ph = PowerHardware(name, capacity, memory)
        System._hardware.append(ph)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hh = HeavyHardware(name, capacity, memory)
        System._hardware.append(hh)

    # TODO tuk vnimavai
    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        if hardware_name not in [each.name for each in System._hardware]:
            return "Hardware does not exist"
        es = ExpressSoftware(name, capacity_consumption, memory_consumption)
        on_hw_to_install = [each for each in System._hardware if each.name == hardware_name][0]
        result = on_hw_to_install.install(es)
        if result == "Software cannot be installed":
            return "Software cannot be installed"
        System._software.append(es)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        if hardware_name not in [each.name for each in System._hardware]:
            return "Hardware does not exist"
        ls = LightSoftware(name, capacity_consumption, memory_consumption)
        on_hw_to_install = [each for each in System._hardware if each.name == hardware_name][0]
        result = on_hw_to_install.install(ls)
        if result == "Software cannot be installed":
            return "Software cannot be installed"
        System._software.append(ls)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hw = [each.name for each in System._hardware if each.name == hardware_name]
        sw = [each.name for each in System._software if each.name == software_name]
        if hw and sw:
            hw[0].uninstall(sw[0])
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        used_mem = sum([each.memory_consumption for each in System._hardware.software_components])
        total_mem = sum([each.memory_consumption for each in System._hardware])
        used_cap = sum([each.capacity_consumption for each in System._hardware.software_components])
        total_cap = sum([each.capacity_consumption for each in System._hardware])
        result = f"System Analysis\nHardware Components: {len(System._hardware)}\n"
        result += f"Software Components: {len(System._software)}\n"
        result += f"Total Operational Memory: {used_mem} / {total_mem}\n"
        result += f"Total Capacity Taken: {used_cap} / {total_cap}\n"

    @staticmethod
    def system_split():
        result = ""
        light_soft_comp = 0
        express_soft_comp = 0
        for each in System._hardware:
            result += f"Hardware Component - {each.name}\n"
        for each in System._software:
            if each.type == "Light":
                light_soft_comp += 1
            else:
                express_soft_comp += 1
        result += f"Express Software Components: {express_soft_comp}\n"
        result += f"Light Software Components: {light_soft_comp}\n"



