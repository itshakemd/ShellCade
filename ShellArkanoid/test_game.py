import unittest

from ShellArkanoid.game import ArkanoidGame


class ArkanoidGameTests(unittest.TestCase):
    def test_starts_with_full_brick formation(self):
        game = ArkanoidGame()
        self.assertEqual(game.remaining_bricks, 55)
        self.assertEqual(game.lives, 3)

    def test_paddle_stays_inside_board(self):
        game = ArkanoidGame()
        game.move_paddle(-1000)
        self.assertEqual(game.paddle.x, 0)
        game.move_paddle(1000)
        self.assertEqual(game.paddle.right, 75)


if __name__ == "__main__":
    unittest.main()
