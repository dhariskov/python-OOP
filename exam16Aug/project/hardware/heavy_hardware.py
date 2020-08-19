from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name, capacity, memory):
        Hardware.__init__(self, name, "Heavy", int(capacity*2), int(0.75*memory))

# test = HeavyHardware("HDD", 200, 200)
#
# print(test.name, test.type, test.capacity, test.memory)