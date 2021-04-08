import unittest
from src.player import Player

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.player_1 = Player("Steven", "Rock")
        self.player_2 = Player("Kieran", "Paper")

    def test_player_name_1(self):
        self.assertEqual("Steven", self.player_1.name)

    def test_player_choice_1(self):
        self.assertEqual("Rock", self.player_1.choice)

    def test_player_name_2(self):
        self.assertEqual("Kieran", self.player_2.name)

    def test_player_choice_2(self):
        self.assertEqual("Paper", self.player_2.choice)