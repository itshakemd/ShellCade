"""Small regression suite for the Snake rules."""

import unittest

from game import Game


class FixedRandom:
    def choice(self, values):
        return values[0]


class SnakeRulesTests(unittest.TestCase):
    def new_game(self):
        return Game(rng=FixedRandom())

    def test_snake_moves_without_growing(self):
        game = self.new_game()
        initial_length = len(game.snake)
        game.step()
        self.assertEqual(len(game.snake), initial_length)
        self.assertEqual(game.score, 0)

    def test_eating_food_grows_and_scores(self):
        game = self.new_game()
        head_x, head_y = game.snake[0]
        game.food = (head_x + 1, head_y)
        game.step()
        self.assertEqual(len(game.snake), 4)
        self.assertEqual(game.score, 10)
        self.assertEqual(game.food_eaten, 1)

    def test_wall_collision_ends_game(self):
        game = self.new_game()
        game.snake = [(0, 0), (1, 0), (2, 0)]
        game.direction = "LEFT"
        game.next_direction = "LEFT"
        game.step()
        self.assertTrue(game.game_over)
        self.assertEqual(game.death_reason, "You hit the wall.")


if __name__ == "__main__":
    unittest.main()
