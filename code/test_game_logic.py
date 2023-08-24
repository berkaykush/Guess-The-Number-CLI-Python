import unittest

from unittest.mock import patch
from game_logic import (
    GameLogic,
)


class TestGameLogic(unittest.TestCase):
    @patch("builtins.input", side_effect=["42"])
    def test_check_entered_guess_valid(self, mock_input):
        game = GameLogic()
        guess = game._GameLogic__check_entered_guess()
        self.assertEqual(guess, 42)

    @patch("builtins.input", side_effect=["abc", "23"])
    def test_check_entered_guess_invalid_then_valid(self, mock_input):
        game = GameLogic()
        guess = game._GameLogic__check_entered_guess()
        self.assertEqual(guess, 23)

    def test_is_out_of_bounds_true(self):
        game = GameLogic()
        self.assertTrue(game._GameLogic__is_out_of_bounds(0))
        self.assertTrue(game._GameLogic__is_out_of_bounds(101))

    def test_is_out_of_bounds_false(self):
        game = GameLogic()
        self.assertFalse(game._GameLogic__is_out_of_bounds(42))
        self.assertFalse(game._GameLogic__is_out_of_bounds(1))
        self.assertFalse(game._GameLogic__is_out_of_bounds(100))

    def test_is_guess_close_true(self):
        game = GameLogic()
        game._GameLogic__selected_num = 50  # Set a specific selected number for testing
        self.assertTrue(game._GameLogic__is_guess_close(45))
        self.assertTrue(game._GameLogic__is_guess_close(55))
        self.assertTrue(game._GameLogic__is_guess_close(49))
        self.assertTrue(game._GameLogic__is_guess_close(51))

    def test_is_guess_close_false(self):
        game = GameLogic()
        game._GameLogic__selected_num = 50  # Set a specific selected number for testing
        self.assertFalse(game._GameLogic__is_guess_close(39))
        self.assertFalse(game._GameLogic__is_guess_close(61))

    def test_is_current_guess_closer_than_prev_guess_true(self):
        game = GameLogic()
        game._GameLogic__selected_num = 50
        self.assertTrue(
            game._GameLogic__is_current_guess_closer_than_prev_guess(45, 56)
        )
        self.assertTrue(
            game._GameLogic__is_current_guess_closer_than_prev_guess(54, 45)
        )

    def test_is_current_guess_closer_than_prev_guess_false(self):
        game = GameLogic()
        game._GameLogic__selected_num = 50
        self.assertFalse(
            game._GameLogic__is_current_guess_closer_than_prev_guess(45, 55)
        )
        self.assertFalse(
            game._GameLogic__is_current_guess_closer_than_prev_guess(55, 45)
        )

    @patch("builtins.input", side_effect=["Y"])
    def test_check_continue_yes(self, mock_input):
        game = GameLogic()
        self.assertEqual(game.check_continue(), "Y")

    @patch("builtins.input", side_effect=["N"])
    def test_check_continue_no(self, mock_input):
        game = GameLogic()
        self.assertEqual(game.check_continue(), "N")

    def test_reset(self):
        game = GameLogic()
        game._GameLogic__num_guesses = 5
        game._GameLogic__num_chances = 2
        game._GameLogic__selected_num = 42
        game.reset()
        self.assertEqual(game._GameLogic__num_guesses, 0)
        self.assertEqual(game._GameLogic__num_chances, 7)
        self.assertNotEqual(game._GameLogic__selected_num, 42)


if __name__ == "__main__":
    unittest.main()
