from abc import ABC, abstractmethod
from exam_preparation.skeleton.project.card.card_repository import CardRepository
# from project.card.card_repository import CardRepository


class Player(ABC):
    @abstractmethod
    def __init__(self, username, health):
        self.username = username
        self.health = health
        self.card_repository = CardRepository()

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if username == "":
            raise ValueError("Player's username cannot be an empty string.")
        self._username = username

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        if health < 0:
            raise ValueError("Player's health bonus cannot be less than zero.")
        self._health = health

    @property
    def is_dead(self):
        return self.health <= 0

    def take_damage(self, damage_points: int):
        if damage_points < 0:
            raise ValueError("Damage points cannot be less than zero.")
        self.health -= damage_points
