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

    def test_pause_freezes_pacman(self):
        game = PacmanGame()
        game.toggle_pause()
        position = (game.pacman.x, game.pacman.y)
        game.set_direction((1, 0))
        game.tick()
        self.assertEqual(position, (game.pacman.x, game.pacman.y))

    def test_restart_restores_pacman_state(self):
        game = PacmanGame()
        game.score = 300
        game.lives = 1
        game.restart()
        self.assertEqual(game.score, 0)
        self.assertEqual(game.lives, 3)

    def test_ghosts_spawn_in_four_colors(self):
        game = PacmanGame()
        self.assertEqual([ghost.color for ghost in game.ghosts], ["red", "pink", "cyan", "orange"])

    def test_ghost_collision_costs_a_life(self):
        game = PacmanGame()
        game.ghosts[0].x, game.ghosts[0].y = game.pacman.x, game.pacman.y
        game._check_collisions()
        self.assertEqual(game.lives, 2)

    def test_direction_is_buffered_until_path_opens(self):
        game = PacmanGame()
        game.pacman.x, game.pacman.y = 1, 1
        game.pacman.direction = (0, 1)
        game.set_direction((1, 0))
        game.tick()
        self.assertEqual(game.pacman.direction, (1, 0))

    def test_frightened_collision_awards_bonus(self):
        game = PacmanGame()
        game.frightened_ticks = 5
        game.ghosts[0].x, game.ghosts[0].y = game.pacman.x, game.pacman.y
        game._check_collisions()
        self.assertEqual(game.score, 200)
        self.assertEqual(game.lives, 3)

    def test_last_ghost_collision_ends_game(self):
        game = PacmanGame()
        game.lives = 1
        game.ghosts[0].x, game.ghosts[0].y = game.pacman.x, game.pacman.y
        game._check_collisions()
        self.assertTrue(game.game_over)


if __name__ == "__main__":
    unittest.main()
