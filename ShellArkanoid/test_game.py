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

    def test_ball_bounces_from_paddle(self):
        game = ArkanoidGame()
        game.ball.x = game.paddle.x + 4
        game.ball.y = 20
        game.ball.dy = 1
        game.tick()
        self.assertEqual(game.ball.dy, -1)

    def test_brick_collision_adds_score(self):
        game = ArkanoidGame()
        brick = game.bricks[0]
        game.ball.x = brick.x
        game.ball.y = brick.y - 1
        game.ball.dy = 1
        game.tick()
        self.assertFalse(brick.alive)
        self.assertEqual(game.score, 50)


if __name__ == "__main__":
    unittest.main()
