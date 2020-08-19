import unittest
# from exam_preparation.skeleton.project.card.card_repository import CardRepository
# from exam_preparation.skeleton.project.card.magic_card import MagicCard
from project.card.magic_card import MagicCard
from project.card.card_repository import CardRepository


class TestCardRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.card1 = MagicCard("Test")
        self.card2 = MagicCard("Test2")
        self.card3 = MagicCard("Test")
        self.repository = CardRepository()

    def test_add_card(self):
        self.repository.add(self.card1)
        self.assertEqual(self.card1.name, "Test")
        self.assertEqual(self.repository.count, 1)
        with self.assertRaises(ValueError) as ex:
            self.repository.add(self.card3)
        self.assertEqual(str(ex.exception), "Card Test already exists!")
        self.assertEqual(self.repository.count, 1)

    def test_remove_card(self):
        self.repository.add(self.card1)
        self.repository.add(self.card2)
        self.repository.remove("Test")
        self.assertEqual(self.repository.count, 1)
        with self.assertRaises(ValueError) as ex:
            self.repository.remove("")
        self.assertEqual(str(ex.exception), "Card cannot be an empty string!")
        self.assertEqual(self.repository.count, 1)
        self.repository.remove("NoCard")
        self.assertEqual(self.repository.count, 1)

    def test_find_card(self):
        self.repository.add(self.card1)
        result = self.repository.find("Test")
        self.assertEqual(result.name, "Test")



if __name__ == '__main__':
    unittest.main()

