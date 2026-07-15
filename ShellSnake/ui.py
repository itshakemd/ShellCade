"""Blessed terminal presentation helpers for Snake."""

from blessed import Terminal


def create_terminal():
    return Terminal()


def terminal_frame(term, content):
    return term.home + term.clear + term.bold_green(content)
