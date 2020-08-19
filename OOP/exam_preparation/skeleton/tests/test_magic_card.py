import unittest
# from exam_preparation.skeleton.project.card.magic_card import MagicCard
# from exam_preparation.skeleton.project.card.card import Card
from project.card.card import Card
from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def test_if_MagicCardInheritsCard(self):
        self.assertTrue(issubclass(MagicCard, Card))

    def test_card_creation(self):
        card = MagicCard("Test")
        self.assertEqual(card.name, "Test")
        self.assertEqual(card.damage_points, 5)
        self.assertEqual(card.health_points, 80)

    def test_card_creation_nameEqualToSpace(self):
        with self.assertRaises(ValueError) as ex:
            card1 = MagicCard("")
        self.assertEqual(str(ex.exception), "Card's name cannot be an empty string.")

    def test_card_damagePoints_lessThanZero(self):
        card = MagicCard("Test")
        with self.assertRaises(ValueError) as ex:
            card.damage_points -= 10000
        self.assertEqual(str(ex.exception), "Card's damage points cannot be less than zero.")

    def test_card_damagePoints_GreaterThanZero(self):
        card = MagicCard("Test")
        card.damage_points += 10
        self.assertEqual(card.damage_points, 15)

    def test_card_health_points_LessThanZero(self):
        card = MagicCard("Test")
        with self.assertRaises(ValueError) as ex:
            card.health_points -= 1000
        self.assertEqual(str(ex.exception), "Card's HP cannot be less than zero.")

    def test_card_health_points_GreaterThanZero(self):
        card = MagicCard("Test")
        card.health_points += 10
        self.assertEqual(card.health_points, 90)


if __name__ == '__main__':
    unittest.main()
