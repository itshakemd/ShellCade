"""Blessed terminal presentation helpers for Space Invaders."""

from blessed import Terminal


def create_terminal():
    return Terminal()


def terminal_frame(term, content):
    return term.home + term.clear + term.bright_red(content)
