"""The main gameplay loop: input handling, gravity, rendering, game-over flow."""

import random
import time

import msvcrt

from display import clear_screen, print_centered
from game import Game
from keyboard_input import get_text_input
from scores import qualifies_for_leaderboard, save_score, top_score


def run_game(scores):
