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

    def test_ball_bounces_from_top_wall(self):
        game = PongGame()
        game.ball.y = 1
        game.ball.vy = -1
        game.tick()
        self.assertGreater(game.ball.vy, 0)

    def test_single_player_ai_tracks_ball(self):
        game = PongGame()
        game.ball.y = 3
        game.right.y = 10
        game.ai_move()
        self.assertLess(game.right.y, 10)


if __name__ == "__main__":
    unittest.main()
