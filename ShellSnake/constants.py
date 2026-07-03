"""Shared settings for the terminal Snake game."""

import os

WIDTH = 20
HEIGHT = 16

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HIGHSCORE_FILE = os.path.join(SCRIPT_DIR, "highscore.txt")
