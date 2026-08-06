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

    def test_missed_ball_costs_one_life_and_resets(self):
        game = ArkanoidGame()
        game.ball.y = 23
        game.ball.dy = 1
        game.tick()
        self.assertEqual(game.lives, 2)
        self.assertEqual((game.ball.x, game.ball.y), (38, 21))

    def test_pause_freezes_physics(self):
        game = ArkanoidGame()
        game.toggle_pause()
        position = (game.ball.x, game.ball.y)
        game.tick()
        self.assertEqual(position, (game.ball.x, game.ball.y))

    def test_ball_reflects_from_side_wall(self):
        game = ArkanoidGame()
        game.ball.x = 75
        game.ball.dx = 1
        game.ball.y = 20
        game.tick()
        self.assertEqual(game.ball.dx, -1)

    def test_final_missed_ball_ends_round(self):
        game = ArkanoidGame()
        game.lives = 1
        game.ball.y = 23
        game.ball.dy = 1
        game.tick()
        self.assertTrue(game.game_over)


if __name__ == "__main__":
    unittest.main()
