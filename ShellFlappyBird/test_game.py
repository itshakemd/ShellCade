import unittest

from constants import GROUND_Y
from game import FlappyGame


class FixedRandom:
    def randint(self, low, high):
        return (low + high) // 2


class FlappyTests(unittest.TestCase):
    def test_game_starts_before_first_flap(self):
        game = FlappyGame(rng=FixedRandom())
        game.tick()
        self.assertFalse(game.started)
        self.assertEqual(game.bird.y, 12)

    def test_flap_starts_game_and_sets_velocity(self):
        game = FlappyGame(rng=FixedRandom())
        game.flap()
        self.assertTrue(game.started)
        self.assertLess(game.bird.velocity, 0)

    def test_gravity_moves_started_bird_down(self):
        game = FlappyGame(rng=FixedRandom())
        game.flap()
        old_y = game.bird.y
        game.tick()
        self.assertNotEqual(game.bird.y, old_y)

    def test_pipe_collision_ends_round(self):
        game = FlappyGame(rng=FixedRandom())
        game.flap()
        pipe = game.pipes[0]
        game.bird.x = int(pipe.x)
        game.bird.y = 1
        game.tick()
        self.assertTrue(game.game_over)


if __name__ == "__main__":
    unittest.main()
