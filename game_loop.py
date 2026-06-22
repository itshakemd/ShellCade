"""The main gameplay loop: input handling, gravity, rendering, game-over flow."""

import random
import time

import msvcrt

from display import clear_screen, print_centered
from game import Game
from keyboard_input import get_text_input
from scores import qualifies_for_leaderboard, save_score, top_score


def run_game(scores):
    random.seed()
    high_score_name, high_score = top_score(scores)
    game = Game()
    last_render = None
    last_fall = time.time()

    while not game.game_over:
        start = time.time()
        while time.time() - start < 0.03:
            if msvcrt.kbhit():
                ch = msvcrt.getch()
                if ch in (b"\x00", b"\xe0"):
                    ch2 = msvcrt.getch()
                    if game.paused:
                        continue
                    if ch2 == b"H":  # up arrow
                        game.rotate()
                    elif ch2 == b"K":  # left arrow
                        game.move(-1, 0)
                    elif ch2 == b"M":  # right arrow
                        game.move(1, 0)
                    elif ch2 == b"P":  # down arrow
                        game.soft_drop()
                elif ch in (b"p", b"P"):
                    game.paused = not game.paused
                elif ch in (b"q", b"Q"):
                    game.game_over = True
                    break
                elif not game.paused:
                    if ch in (b"a", b"A"):
                        game.move(-1, 0)
                    elif ch in (b"d", b"D"):
                        game.move(1, 0)
                    elif ch in (b"s", b"S"):
                        game.soft_drop()
                    elif ch in (b"w", b"W"):
                        game.rotate()
                    elif ch == b" ":
                        game.hard_drop()
            time.sleep(0.01)

        if not game.paused:
                            game.gravity_tick()
                last_fall = time.time()
        else:
            last_fall = time.time()  # don't accumulate fall time while paused

        frame = game.render(high_score_name, high_score)
        if frame != last_render:
            clear_screen()
            print_centered(frame)
            last_render = frame