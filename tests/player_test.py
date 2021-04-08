import unittest
from src.player import Player

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.player_1 = Player("Steven", "Rock")
        self.player_2 = Player("Kieran", "Paper")

    def test_player_name(self):
        self.assertEqual("Steven", self.player_1.name)