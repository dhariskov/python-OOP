class Exaggerated(object):
    def __init__(self, value):
        self.real_value = value
    @property
    def value(self):
        return 10*self.real_value
    @value.setter
    def value(self, newvalue):
        raise ValueError("Denied!")

p = Exaggerated(1)
print(p.value)