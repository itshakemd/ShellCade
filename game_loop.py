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
            drop_interval = max(0.1, 0.6 - (game.level - 1) * 0.05)
            if time.time() - last_fall >= drop_interval:
                game.gravity_tick()
                last_fall = time.time()
        else:
            last_fall = time.time()  # don't accumulate fall time while paused

        frame = game.render(high_score_name, high_score)
        if frame != last_render:
            clear_screen()
            print_centered(frame)
            last_render = frame

    # game over
    made_leaderboard = qualifies_for_leaderboard(scores, game.score)
    is_new_top = game.score > high_score
    if made_leaderboard:
        player_name = get_text_input("NEW HIGH SCORE! Enter your name:" if is_new_top
                                      else "You made the leaderboard! Enter your name:")
        scores = save_score(player_name, game.score)
        high_score_name, high_score = top_score(scores)

    clear_screen()
    game_over_lines = [
        "GAME OVER",
        f"Final Score: {game.score}",
        f"Lines Cleared: {game.lines}",
    ]
    if made_leaderboard:
        game_over_lines.append("")
        game_over_lines.append("*** NEW HIGH SCORE! ***" if is_new_top else "*** MADE THE LEADERBOARD! ***")
    game_over_lines.append(f"Best: {high_score_name} - {high_score}")
    game_over_lines.append("")
    print_centered("\n".join(game_over_lines), vertical=False)
    input("Press Enter to return to menu...")
    return scores

