"""Core Flappy Bird simulation."""

import random

from constants import (
    BIRD_START_Y, BIRD_X, FLAP_VELOCITY, GRAVITY, GROUND_Y, HEIGHT,
    PIPE_GAP, PIPE_SPACING, PIPE_WIDTH, WIDTH,
)
from entities import Bird, Pipe


class FlappyGame:
    def __init__(self, rng=None):
        self.rng = rng or random
        self.bird = Bird(BIRD_X, BIRD_START_Y)
        self.pipes = []
        self.score = 0
        self.best_score = 0
        self.game_over = False
        self.paused = False
        self.started = False
        self.death_reason = ""
        self.spawn_pipe(WIDTH + 8)

    def spawn_pipe(self, x):
        margin = 3
        gap_y = self.rng.randint(margin, GROUND_Y - PIPE_GAP - margin)
        self.pipes.append(Pipe(x, gap_y))

    def flap(self):
        if not self.game_over:
            self.started = True
            self.bird.velocity = FLAP_VELOCITY

    def advance_bird(self):
        if not self.started or self.game_over:
            return
        self.bird.velocity += GRAVITY
        self.bird.y += self.bird.velocity

    def move_pipes(self):
        if not self.started or self.game_over:
            return
        for pipe in self.pipes:
            pipe.x -= 1
        if self.pipes[-1].x <= WIDTH - PIPE_SPACING:
            self.spawn_pipe(WIDTH)
        self.pipes = [pipe for pipe in self.pipes if pipe.x > -PIPE_WIDTH]

    def collides_with_pipe(self, pipe):
        inside_x = pipe.x <= self.bird.x < pipe.x + pipe.width
        outside_gap = not (pipe.gap_y <= self.bird.y < pipe.gap_y + PIPE_GAP)
        return inside_x and outside_gap

    def check_bounds(self):
        return self.bird.y < 1 or self.bird.y >= GROUND_Y

    def resolve_scoring(self):
        for pipe in self.pipes:
            if not pipe.scored and pipe.x + pipe.width < self.bird.x:
                pipe.scored = True
                self.score += 1
                self.best_score = max(self.best_score, self.score)

    def tick(self):
        if self.paused or self.game_over:
            return
        self.advance_bird()
        self.move_pipes()
        self.resolve_scoring()
        if self.check_bounds() or any(self.collides_with_pipe(pipe) for pipe in self.pipes):
            self.game_over = True

    def render(self):
        rows = [[" "] * WIDTH for _ in range(HEIGHT)]
        for pipe in self.pipes:
            x = int(pipe.x)
            if 0 <= x < WIDTH:
                for y in range(1, GROUND_Y):
                    if not (pipe.gap_y <= y < pipe.gap_y + PIPE_GAP):
                        rows[y][x] = "#"
                        if x + 1 < WIDTH:
                            rows[y][x + 1] = "#"
        bird_y = int(self.bird.y)
        if 0 <= bird_y < HEIGHT:
            rows[bird_y][self.bird.x] = "@"
        rows[GROUND_Y] = ["="] * WIDTH
        lines = ["SHELL FLAPPY BIRD".center(WIDTH),
                 f"Score: {self.score}  Best: {self.best_score}".center(WIDTH)]
        lines.extend("".join(row) for row in rows)
        return "\n".join(lines)
