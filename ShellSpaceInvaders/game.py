"""Core state and rules for ShellSpaceInvaders."""

from constants import (
    ENEMY_COLUMNS,
    ENEMY_ROWS,
    ENEMY_START_Y,
    ENEMY_X_GAP,
    ENEMY_Y_GAP,
    ENEMY_STEP_EVERY,
    ENEMY_FIRE_EVERY,
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
        self.shot_cooldown = 0
        self.shields = {(18, PLAYER_Y - 2), (19, PLAYER_Y - 2), (40, PLAYER_Y - 2), (41, PLAYER_Y - 2)}
        self.spawn_wave()

    def spawn_wave(self):
        self.enemy_direction = 1
        self.enemy_tick = 0
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
        if self.shot_cooldown == 0 and not any(shot.owner == "player" for shot in self.projectiles):
            self.projectiles.append(Projectile(self.player_x, PLAYER_Y - 1, -1, "player"))
            self.shot_cooldown = 8

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

    def move_projectiles(self):
        for shot in self.projectiles:
            shot.y += shot.dy
        self.projectiles = [
            shot for shot in self.projectiles if 0 < shot.y < HEIGHT
        ]

    def resolve_hits(self):
        remaining = []
        for shot in self.projectiles:
            hit = False
            if (shot.x, shot.y) in self.shields:
                self.shields.remove((shot.x, shot.y))
                continue
            if shot.owner == "player":
                for enemy in self.alive_enemies:
                    if enemy.x == shot.x and enemy.y == shot.y:
                        enemy.alive = False
                        self.score += 10 + (3 - enemy.row) * 5
                        hit = True
                        break
            if not hit:
                remaining.append(shot)
        self.projectiles = remaining

    def enemy_fire(self):
        living = self.alive_enemies
        if not living:
            return
        shooter = living[-1]
        self.projectiles.append(Projectile(shooter.x, shooter.y + 1, 1, "enemy"))

    def resolve_player_hits(self):
        survivors = []
        hit_player = False
        for shot in self.projectiles:
            if shot.owner == "enemy" and shot.x == self.player_x and shot.y >= PLAYER_Y:
                hit_player = True
            else:
                survivors.append(shot)
        self.projectiles = survivors
        if hit_player:
            self.lives -= 1
            if self.lives <= 0:
                self.game_over = True

    def tick(self):
        if self.paused or self.game_over:
            return
        self.shot_cooldown = max(0, self.shot_cooldown - 1)
        self.enemy_tick += 1
        if self.enemy_tick % ENEMY_STEP_EVERY == 0:
            self.move_enemies()
            if any(enemy.y >= PLAYER_Y - 1 for enemy in self.alive_enemies):
                self.game_over = True
        if self.enemy_tick % ENEMY_FIRE_EVERY == 0:
            self.enemy_fire()
        self.move_projectiles()
        self.resolve_hits()
        self.resolve_player_hits()
        if not self.alive_enemies:
            self.wave += 1
            self.spawn_wave()

    def render(self):
        rows = [[" "] * WIDTH for _ in range(HEIGHT)]
        rows[PLAYER_Y][self.player_x] = "A"
        for x, y in self.shields:
            rows[y][x] = "#"
        for enemy in self.alive_enemies:
            if 0 <= enemy.y < HEIGHT and 0 <= enemy.x < WIDTH:
                rows[enemy.y][enemy.x] = "W"
        for shot in self.projectiles:
            if 0 <= shot.y < HEIGHT and 0 <= shot.x < WIDTH:
                rows[shot.y][shot.x] = "|" if shot.owner == "player" else "!"
        lines = ["SHELL SPACE INVADERS".center(WIDTH),
                 f"Score: {self.score}  Lives: {self.lives}  Wave: {self.wave}".center(WIDTH),
                 "+" + "-" * (WIDTH - 2) + "+"]
        lines.extend("|" + "".join(row[1:-1]) + "|" for row in rows[1:-1])
        lines.append("+" + "-" * (WIDTH - 2) + "+")
        if self.paused:
            lines.append("PAUSED - press P to resume".center(WIDTH))
        elif self.game_over:
            lines.append("GAME OVER".center(WIDTH))
        return "\n".join(lines)
