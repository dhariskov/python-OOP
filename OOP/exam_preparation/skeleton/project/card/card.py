from abc import ABC, abstractmethod


class Card(ABC):
    @abstractmethod
    def __init__(self, name, damage_points, health_points):
        self.name = name
        self.damage_points = damage_points
        self.health_points = health_points

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Card's name cannot be an empty string.")
        self._name = name

    @property
    def damage_points(self):
        return self._damage_points

    @damage_points.setter
    def damage_points(self, damage_points):
        if damage_points < 0:
            raise ValueError("Card's damage points cannot be less than zero.")
        self._damage_points = damage_points

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, health_points):
        if health_points < 0:
            raise ValueError("Card's HP cannot be less than zero.")
        self._health_points = health_points



