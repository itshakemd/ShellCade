"""Blessed terminal presentation helpers for Tetris."""

from blessed import Terminal


def create_terminal():
    return Terminal()


def terminal_frame(term, content):
    return term.home + term.clear + term.bold_cyan(content)
