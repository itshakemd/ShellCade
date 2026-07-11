import unittest

from constants import PLAYER_Y
from game import InvadersGame


class InvadersTests(unittest.TestCase):
    def test_player_stays_inside_bounds(self):
        game = InvadersGame()
        for _ in range(100):
            game.move_player(-2)
        self.assertEqual(game.player_x, 2)

    def test_firing_creates_one_player_shot(self):
        game = InvadersGame()
        game.fire()
        game.fire()
        self.assertEqual(len(game.projectiles), 1)
        self.assertEqual(game.projectiles[0].y, PLAYER_Y - 1)

    def test_hit_removes_invader_and_scores(self):
        game = InvadersGame()
        enemy = game.alive_enemies[0]
        game.projectiles = [type("Shot", (), {"x": enemy.x, "y": enemy.y, "owner": "player"})()]
        game.resolve_hits()
        self.assertFalse(enemy.alive)
        self.assertGreater(game.score, 0)

    def test_enemy_hit_costs_a_life(self):
        game = InvadersGame()
        game.projectiles = [
            type("Shot", (), {"x": game.player_x, "y": PLAYER_Y, "owner": "enemy"})()
        ]
        game.resolve_player_hits()
        self.assertEqual(game.lives, 2)

    def test_pause_freezes_tick(self):
        game = InvadersGame()
        game.paused = True
        position = [(enemy.x, enemy.y) for enemy in game.alive_enemies]
        game.tick()
        self.assertEqual(position, [(enemy.x, enemy.y) for enemy in game.alive_enemies])

    def test_wave_respawns_after_last_invader(self):
        game = InvadersGame()
        game.enemies[0].alive = False
        for enemy in game.enemies[1:]:
            enemy.alive = False
        game.tick()
        self.assertEqual(game.wave, 2)
        self.assertEqual(len(game.alive_enemies), 32)


if __name__ == "__main__":
    unittest.main()
