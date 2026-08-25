import unittest

from ShellTicTacToe.ai import choose_move
from ShellTicTacToe.game import TicTacToeGame


class TicTacToeTests(unittest.TestCase):
    def test_x_can_win_a_row(self):
        game = TicTacToeGame()
        for move in (0, 3, 1, 4, 2):
            game.play(move)
        self.assertEqual(game.winner, "X")

    def test_occupied_square_is_rejected(self):
        game = TicTacToeGame()
        self.assertTrue(game.play(0))
        self.assertFalse(game.play(0))

    def test_ai_takes_winning_move(self):
        game = TicTacToeGame()
        game.board = ["O", "O", " ", "X", "X", " ", " ", " ", " "]
        game.current = "O"
        self.assertEqual(choose_move(game), 2)

    def test_full_board_is_draw(self):
        game = TicTacToeGame()
        for move in (0, 1, 2, 4, 3, 5, 7, 6, 8):
            game.play(move)
        self.assertTrue(game.draw)


if __name__ == "__main__":
    unittest.main()
