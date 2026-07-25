"""Blessed terminal presentation helpers."""

from blessed import Terminal


def create_terminal():
    return Terminal()


def frame(term, content):
    return term.home + term.clear + term.bold_yellow(content)
