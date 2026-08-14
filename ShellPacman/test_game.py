import unittest

from ShellPacman.game import PacmanGame


class PacmanGameTests(unittest.TestCase):
    def test_starts_with_pellets_and_lives(self):
        game = PacmanGame()
        self.assertGreater(len(game.pellets), 0)
        self.assertEqual(game.lives, 3)

    def test_walls_block_movement(self):
        game = PacmanGame()
        game.pacman.x, game.pacman.y = 1, 1
        game.set_direction((-1, 0))
        game.tick()
        self.assertEqual((game.pacman.x, game.pacman.y), (1, 1))

    def test_pellet_increases_score(self):
        game = PacmanGame()
        game.pacman.x, game.pacman.y = 2, 1
        game.set_direction((-1, 0))
        game.tick()
        self.assertEqual(game.score, 10)

    def test_power_pellet_starts_frightened_mode(self):
        game = PacmanGame()
        game.pacman.x, game.pacman.y = 2, 1
        game.set_direction((-1, 0))
        game.tick()
        self.assertGreater(game.frightened_ticks, 0)
        self.assertEqual(game.score, 50)


if __name__ == "__main__":
    unittest.main()
