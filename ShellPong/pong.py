"""Pong domain model: paddles, ball physics, scoring, and match state."""

from dataclasses import dataclass

from constants import HEIGHT, PADDLE_HEIGHT, PADDLE_X_MARGIN, WIDTH, WINNING_SCORE


@dataclass
class Paddle:
    x: int
    y: float
    speed: float = 1.0

    def move(self, amount):
        self.y = max(1, min(HEIGHT - PADDLE_HEIGHT - 1, self.y + amount * self.speed))


@dataclass
class Ball:
    x: float
    y: float
    vx: float
    vy: float


class PongGame:
    def __init__(self, two_player=False):
        self.two_player = two_player
        self.left = Paddle(PADDLE_X_MARGIN, HEIGHT / 2 - PADDLE_HEIGHT / 2)
        self.right = Paddle(WIDTH - PADDLE_X_MARGIN - 1, HEIGHT / 2 - PADDLE_HEIGHT / 2)
        self.left_score = 0
        self.right_score = 0
        self.round_over = False
        self.match_over = False
        self.paused = False
        self.reset_ball(direction=1)

    def reset_ball(self, direction=1):
        self.ball = Ball(WIDTH / 2, HEIGHT / 2, direction * 1.0, 0.35)
        self.round_over = False

    def move_left(self, amount):
        self.left.move(amount)

    def move_right(self, amount):
        self.right.move(amount)

    def _paddle_hit(self, paddle, moving_right):
        in_paddle_range = paddle.y <= self.ball.y < paddle.y + PADDLE_HEIGHT
        if not in_paddle_range:
            return False
        if moving_right:
            return self.ball.x >= paddle.x - 1
        return self.ball.x <= paddle.x + 1

    def _score_point(self, left_player):
        if left_player:
            self.left_score += 1
        else:
            self.right_score += 1
        self.match_over = max(self.left_score, self.right_score) >= WINNING_SCORE
        self.reset_ball(direction=-1 if left_player else 1)

    def tick(self):
        if self.paused or self.match_over or self.round_over:
            return
        self.ball.x += self.ball.vx
        self.ball.y += self.ball.vy
        if self.ball.y <= 1 or self.ball.y >= HEIGHT - 2:
            self.ball.vy *= -1
        if self.ball.vx < 0 and self._paddle_hit(self.left, False):
            self.ball.vx = abs(self.ball.vx) + 0.04
        elif self.ball.vx > 0 and self._paddle_hit(self.right, True):
            self.ball.vx = -abs(self.ball.vx) - 0.04
        if self.ball.x < 0:
            self._score_point(False)
        elif self.ball.x >= WIDTH:
            self._score_point(True)

    def ai_move(self):
        target = self.ball.y - PADDLE_HEIGHT / 2
        if target < self.right.y:
            self.right.move(-1)
        elif target > self.right.y:
            self.right.move(1)

    def render(self):
        lines = ["SHELLPONG".center(WIDTH), f"{self.left_score}  -  {self.right_score}".center(WIDTH)]
        lines.append("+" + "-" * (WIDTH - 2) + "+")
        for y in range(1, HEIGHT - 1):
            row = [" "] * WIDTH
            if int(self.left.y) <= y < int(self.left.y) + PADDLE_HEIGHT:
                row[self.left.x] = "|"
            if int(self.right.y) <= y < int(self.right.y) + PADDLE_HEIGHT:
                row[self.right.x] = "|"
            if int(self.ball.y) == y and 0 <= int(self.ball.x) < WIDTH:
                row[int(self.ball.x)] = "O"
            lines.append("|" + "".join(row[1:-1]) + "|")
        lines.append("+" + "-" * (WIDTH - 2) + "+")
        return "\n".join(lines)
