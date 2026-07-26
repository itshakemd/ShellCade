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


if __name__ == "__main__":
    unittest.main()
