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
