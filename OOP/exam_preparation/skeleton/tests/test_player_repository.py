import unittest
# from exam_preparation.skeleton.project.player.player_repository import PlayerRepository
# from exam_preparation.skeleton.project.card.magic_card import MagicCard
# from exam_preparation.skeleton.project.player.advanced import Advanced

from project.player.player_repository import PlayerRepository
from project.card.magic_card import MagicCard
from project.player.advanced import Advanced


class TestPlayerRepository(unittest.TestCase):
    def setUp(self) -> None:
        # self.card1 = Advanced("Test")
        # self.card2 = MagicCard("Test2")
        # self.card3 = MagicCard("Test")
        self.player1 = Advanced("Test")
        self.player2 = Advanced("Test2")
        self.player3 = Advanced("Test")
        self.repository = PlayerRepository()

    def test_add_player(self):
        self.repository.add(self.player1)
        self.assertEqual(self.player1.username, "Test")
        self.assertEqual(self.repository.count, 1)
        with self.assertRaises(ValueError) as ex:
            self.repository.add(self.player1)
        self.assertEqual(str(ex.exception), "Player Test already exists!")
        self.assertEqual(self.repository.count, 1)

    def test_remove_player(self):
        self.repository.add(self.player1)
        self.repository.add(self.player2)
        self.repository.remove("Test")
        self.assertEqual(self.repository.count, 1)
        with self.assertRaises(ValueError) as ex:
            self.repository.remove("")
        self.assertEqual(str(ex.exception), "Player cannot be an empty string!")
        self.assertEqual(self.repository.count, 1)
        self.repository.remove("NoPlayer")
        self.assertEqual(self.repository.count, 1)

    def test_find_player(self):
        self.repository.add(self.player1)
        result = self.repository.find("Test")
        self.assertEqual(result.username, "Test")



if __name__ == '__main__':
    unittest.main()

