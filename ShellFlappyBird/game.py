"""Core Flappy Bird simulation."""

import random

from constants import (
    BIRD_START_Y,
    BIRD_X,
    FLAP_VELOCITY,
    GRAVITY,
    GROUND_Y,
    HEIGHT,
    PIPE_GAP,
    PIPE_SPACING,
    WIDTH,
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
        self.pipes = [pipe for pipe in self.pipes if pipe.x > -4]

    def collides_with_pipe(self, pipe):
        bird_x = self.bird.x
        inside_x = pipe.x <= bird_x < pipe.x + 4
        outside_gap = not (pipe.gap_y <= self.bird.y < pipe.gap_y + PIPE_GAP)
        return inside_x and outside_gap
