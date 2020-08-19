from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory):
        Hardware.__init__(self, name, "Power", int(0.25*capacity), int(1.75*memory))
