"""The main gameplay loop: input handling, gravity, rendering, game-over flow."""

import time

from display import clear_screen, print_centered
from game import Game
from scores import top_score


def run_game(scores):
    high_score_name, high_score = top_score(scores)
    game = Game()
    last_render = None
    last_fall = time.time()

    while not game.game_over:
        if time.time() - last_fall >= 0.6:
            game.gravity_tick()
            last_fall = time.time()

        frame = game.render(high_score_name, high_score)
        if frame != last_render:
            clear_screen()
            print_centered(frame)
            last_render = frame

    return scores
