"""Core state and rules for ShellSpaceInvaders."""

from constants import (
    ENEMY_COLUMNS,
    ENEMY_ROWS,
    ENEMY_START_Y,
    ENEMY_X_GAP,
    ENEMY_Y_GAP,
    HEIGHT,
    PLAYER_START_X,
    PLAYER_Y,
    WIDTH,
)
from entities import Enemy, Projectile


class InvadersGame:
    def __init__(self):
        self.player_x = PLAYER_START_X
        self.enemies = []
        self.projectiles = []
        self.score = 0
        self.lives = 3
        self.wave = 1
        self.game_over = False
        self.paused = False
        self.enemy_direction = 1
        self.enemy_tick = 0
        self.spawn_wave()

    def spawn_wave(self):
        self.enemies = [
            Enemy(8 + column * ENEMY_X_GAP, ENEMY_START_Y + row * ENEMY_Y_GAP, row)
            for row in range(ENEMY_ROWS)
            for column in range(ENEMY_COLUMNS)
        ]
        self.projectiles = []

    @property
    def alive_enemies(self):
        return [enemy for enemy in self.enemies if enemy.alive]

    def move_player(self, amount):
        self.player_x = max(2, min(WIDTH - 3, self.player_x + amount))

    def fire(self):
        if not any(shot.owner == "player" for shot in self.projectiles):
            self.projectiles.append(Projectile(self.player_x, PLAYER_Y - 1, -1, "player"))

    def move_enemies(self):
        living = self.alive_enemies
        if not living:
            return
        left = min(enemy.x for enemy in living)
        right = max(enemy.x for enemy in living)
        if left <= 2 or right >= WIDTH - 3:
            self.enemy_direction *= -1
            for enemy in living:
                enemy.y += 1
        for enemy in living:
            enemy.x += self.enemy_direction
