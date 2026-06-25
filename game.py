"""Core game state and rules for terminal Snake."""

import random

from constants import HEIGHT, WIDTH


DIRECTIONS = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0),
}
OPPOSITE = {
    "UP": "DOWN",
    "DOWN": "UP",
    "LEFT": "RIGHT",
    "RIGHT": "LEFT",
}


class Game:
    def __init__(self, rng=None):
        self.rng = rng or random
        center = (WIDTH // 2, HEIGHT // 2)
        self.snake = [
            center,
            (center[0] - 1, center[1]),
            (center[0] - 2, center[1]),
        ]
        self.direction = "RIGHT"
        self.next_direction = "RIGHT"
        self.food = None
        self.score = 0
        self.level = 1
        self.food_eaten = 0
        self.game_over = False
        self.death_reason = ""
        self.quit_requested = False
        self.paused = False
        self.place_food()

    def place_food(self):
        open_cells = [
            (x, y)
            for y in range(HEIGHT)
            for x in range(WIDTH)
            if (x, y) not in self.snake
        ]
        self.food = self.rng.choice(open_cells) if open_cells else None

    def change_direction(self, direction):
        if direction not in DIRECTIONS:
            return
        if direction != OPPOSITE[self.direction]:
            self.next_direction = direction

    def collides(self, position, body):
        x, y = position
        return not (0 <= x < WIDTH and 0 <= y < HEIGHT) or position in body

    def step(self):
        if self.game_over or self.paused:
            return
        self.direction = self.next_direction
        dx, dy = DIRECTIONS[self.direction]
        head_x, head_y = self.snake[0]
        new_head = (head_x + dx, head_y + dy)
        eating = new_head == self.food
        body_to_check = self.snake if eating else self.snake[:-1]

        if self.collides(new_head, body_to_check):
            self.game_over = True
            self.death_reason = (
                "You hit the wall."
                if not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT)
                else "You hit your own tail."
            )
            return

        self.snake.insert(0, new_head)
        if eating:
            self.score += 10
            self.food_eaten += 1
            self.level = 1 + self.score // 50
            self.place_food()
        else:
            self.snake.pop()

    def render(self, high_score_name, high_score):
        snake_cells = set(self.snake)
        lines = [
            "SNAKE".center(WIDTH * 2 + 2),
            "+" + "-" * (WIDTH * 2) + "+",
        ]
        for y in range(HEIGHT):
            row = "|"
            for x in range(WIDTH):
                if (x, y) == self.snake[0]:
                    row += "@@"
                elif (x, y) in snake_cells:
                    row += "[]"
                elif (x, y) == self.food:
                    row += "()"
                else:
                    row += "  "
            lines.append(row + "|")
        lines.extend([
            "+" + "-" * (WIDTH * 2) + "+",
            f"Score: {self.score}   Length: {len(self.snake)}   Level: {self.level}",
            f"Fruit: {self.food_eaten}   Next level: {50 - self.score % 50} points",
            f"Best: {high_score_name} - {high_score}",
        ])
        if self.paused:
            lines.append("*** PAUSED - press P to resume ***")
        lines.append("Arrows/WASD move  P pause  Q quit")
        return "\n".join(lines)
