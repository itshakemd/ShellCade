"""Arkanoid title and controls screens."""

from blessed import Terminal


def show_menu(term: Terminal) -> bool:
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        print(term.home + term.clear, end="")
        print(term.center(term.bold_yellow + "S H E L L  A R K A N O I D" + term.normal))
        print()
        print(term.center("Break every brick and keep the ball alive."))
        print()
        print(term.center("[ENTER] Play    [I] Instructions    [Q] Quit"))
        while True:
            key = term.inkey(timeout=None).lower()
            if key in ("q", "\x03"):
                return False
            if key in ("i",):
                print(term.home + term.clear + term.center("A/D or arrow keys: move paddle") + "\n")
                print(term.center("P: pause    R: restart after game over    Q: quit"))
                print(term.center("Press any key to return."))
                term.inkey(timeout=None)
                return show_menu(term)
            if key.name == "KEY_ENTER" or key == "\n":
                return True
