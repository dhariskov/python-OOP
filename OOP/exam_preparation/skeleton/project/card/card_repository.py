from exam_preparation.skeleton.project.card.card import Card
# from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        if card.name in [c.name for c in self.cards]:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        for c in self.cards:
            if c.name == card:
                self.cards.remove(c)
                self.count -= 1

    def find(self, name: str):
        for c in self.cards:
            if c.name == name:
                return c
