import unittest
from src.player import Player
from src.game import *

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

    def test_player_1_name_not_string_return_error(self):
        self.assertEqual("error, please check your input", play_game(1, 'Rock', 'Kieran', 'Paper'))

    def test_player_2_name_not_string_return_error(self):
        self.assertEqual("error, please check your input", play_game("Steven", 'Rock', 3, 'Paper'))

    def test_player_3_name_not_string_return_error(self):
        self.assertEqual("error, please check your input", play_game(2, 'Rock', 3, 'Paper'))

    def test_choice_1_not_string_return_error(self):
        self.assertEqual("error, please check your input", play_game("Steven", 1, "Kieran", 'Paper'))

    def test_choice_1_rock(self):
        self.assertEqual("error, please check your input", play_game("Steven", "Sock", "Kieran", "Paper") )

    def test_for_draw(self):
        self.assertEqual("draw", play_game("Steven", "Rock", "Kieran", "Rock"))

    def test_for_paper_beats_rock(self):
        self.assertEqual("Player two has won", play_game("Steven", "Rock", "Kieran", "Paper"))
    