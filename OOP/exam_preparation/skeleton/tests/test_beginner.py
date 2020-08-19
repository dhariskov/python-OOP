import unittest
# from exam_preparation.skeleton.project.player.beginner import Beginner
from project.player.advanced import Beginner


class TestBeginner(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Beginner("Test")
        # self.player = Beginner("")

    def test_account_creation_happyCase(self):
        self.assertEqual(self.player.username, "Test")
        self.assertEqual(self.player.health, 50)
        self.assertEqual(self.player.__class__.__name__, "Beginner")
        self.assertEqual(self.player.card_repository.__class__.__name__, "CardRepository")

    def test_account_creation_unhappyCase(self):
        with self.assertRaises(ValueError) as ex:
            test = Beginner("")
        self.assertEqual(str(ex.exception), "Player's username cannot be an empty string.")

    def test_health_setter_greaterThanZero(self):
        self.player.health -= 10
        self.assertEqual(self.player.health, 40)

    def test_health_setter_equalThanZero(self):
        self.player.health -= 50
        self.assertEqual(self.player.health, 0)

    def test_health_setter_greaterThanZero(self):
        with self.assertRaises(ValueError) as ex:
            self.player.health -= 300
        self.assertEqual(str(ex.exception), "Player's health bonus cannot be less than zero.")

    def test_is_dead_false(self):
        result = self.player.is_dead
        self.assertEqual(result, False)

    def test_is_dead_True(self):
        self.player.health -= 50
        result = self.player.is_dead
        self.assertEqual(result, True)

    def test_take_damage_valueLessThanZero(self):
        with self.assertRaises(ValueError) as ex:
            self.player.take_damage(-100)
        self.assertEqual(str(ex.exception), "Damage points cannot be less than zero.")

    def test_take_damage_valueGreaterThanZero(self):
        self.player.take_damage(20)
        self.assertEqual(self.player.health, 30)




if __name__ == '__main__':
    unittest.main()