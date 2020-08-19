import unittest
# from exam_preparation.skeleton.project.card.trap_card import TrapCard
# from exam_preparation.skeleton.project.card.card import Card
from project.card.card import Card
from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):
    def test_if_MagicCardInheritsCard(self):
        self.assertTrue(issubclass(TrapCard, Card))

    def test_card_creation(self):
        card = TrapCard("Test")
        self.assertEqual(card.name, "Test")
        self.assertEqual(card.damage_points, 120)
        self.assertEqual(card.health_points, 5)

    def test_card_creation_nameEqualToSpace(self):
        with self.assertRaises(ValueError) as ex:
            card1 = TrapCard("")
        self.assertEqual(str(ex.exception), "Card's name cannot be an empty string.")

    def test_card_damagePoints_lessThanZero(self):
        card = TrapCard("Test")
        with self.assertRaises(ValueError) as ex:
            card.damage_points -= 10000
        self.assertEqual(str(ex.exception), "Card's damage points cannot be less than zero.")

    def test_card_damagePoints_GreaterThanZero(self):
        card = TrapCard("Test")
        card.damage_points += 10
        self.assertEqual(card.damage_points, 130)

    def test_card_health_points_LessThanZero(self):
        card = TrapCard("Test")
        with self.assertRaises(ValueError) as ex:
            card.health_points -= 1000
        self.assertEqual(str(ex.exception), "Card's HP cannot be less than zero.")

    def test_card_health_points_GreaterThanZero(self):
        card = TrapCard("Test")
        card.health_points += 10
        self.assertEqual(card.health_points, 15)


if __name__ == '__main__':
    unittest.main()
