"""The main gameplay loop: input handling, timing, rendering, and scores."""

import time

import msvcrt

from display import clear_screen, print_centered
from game import Game
from keyboard_input import get_text_input
from scores import qualifies_for_leaderboard, save_score, top_score


KEY_DIRECTIONS = {
    b"w": "UP",
    b"W": "UP",
    b"s": "DOWN",
    b"S": "DOWN",
    b"a": "LEFT",
    b"A": "LEFT",
    b"d": "RIGHT",
    b"D": "RIGHT",
}
ARROW_DIRECTIONS = {
    b"H": "UP",
    b"P": "DOWN",
    b"K": "LEFT",
    b"M": "RIGHT",
}


def run_game(scores):
    high_score_name, high_score = top_score(scores)
    game = Game()
    last_render = None
    last_step = time.time()

    while not game.game_over:
        frame_start = time.time()
        while time.time() - frame_start < 0.03:
            if msvcrt.kbhit():
                ch = msvcrt.getch()
                if ch in (b"\x00", b"\xe0"):
                    arrow = msvcrt.getch()
                    if not game.paused and arrow in ARROW_DIRECTIONS:
                        game.change_direction(ARROW_DIRECTIONS[arrow])
                elif ch in (b"p", b"P"):
                    game.paused = not game.paused
                elif ch in (b"q", b"Q"):
                    game.quit_requested = True
                    break
                elif not game.paused and ch in KEY_DIRECTIONS:
                    game.change_direction(KEY_DIRECTIONS[ch])
            time.sleep(0.01)

        if not game.paused:
            step_interval = max(0.07, 0.18 - (game.level - 1) * 0.015)
            if time.time() - last_step >= step_interval:
                game.step()
                last_step = time.time()
        else:
            last_step = time.time()

        frame = game.render(high_score_name, high_score)
        if frame != last_render:
            clear_screen()
            print_centered(frame)
            last_render = frame

    if game.quit_requested:
        clear_screen()
        return scores

    made_leaderboard = qualifies_for_leaderboard(scores, game.score)
    is_new_top = game.score > high_score
    if made_leaderboard:
        prompt = "NEW HIGH SCORE! Enter your name:" if is_new_top else (
            "You made the leaderboard! Enter your name:"
        )
        player_name = get_text_input(prompt)
        scores = save_score(player_name, game.score)
        high_score_name, high_score = top_score(scores)

    clear_screen()
    game_over_lines = [
        "GAME OVER",
        game.death_reason,
        f"Final Score: {game.score}",
        f"Snake Length: {len(game.snake)}",
    ]
    if made_leaderboard:
        game_over_lines.extend([
            "",
            "*** NEW HIGH SCORE! ***" if is_new_top else "*** MADE THE LEADERBOARD! ***",
        ])
    game_over_lines.extend([
        f"Best: {high_score_name} - {high_score}",
        "",
    ])
    print_centered("\n".join(game_over_lines), vertical=False)
    input("Press Enter to return to menu...")
    return scores
