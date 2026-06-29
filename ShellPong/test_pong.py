import unittest

from pong import PongGame


class PongTests(unittest.TestCase):
    def test_paddles_stay_inside_court(self):
        game = PongGame()
        for _ in range(100):
            game.move_left(-1)
        self.assertEqual(game.left.y, 1)

    def test_point_increases_score(self):
        game = PongGame()
        game.ball.x = -1
        game.tick()
        self.assertEqual(game.right_score, 1)


if __name__ == "__main__":
    unittest.main()
