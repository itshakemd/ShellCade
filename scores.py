"""High score / leaderboard persistence.

Scores are stored one 'name,score' pair per line in HIGHSCORE_FILE.
If the same name appears more than once, only the highest score for
that name is kept.
"""

from constants import HIGHSCORE_FILE

MAX_LEADERBOARD_ENTRIES = 10


def load_scores():
    """Returns a list of (name, score) tuples sorted by score (desc)."""
    best = {}
    try:
        with open(HIGHSCORE_FILE, "r") as f:
            for raw_line in f:
                line = raw_line.strip()
                if not line:
                    continue
                name, _, score_str = line.partition(",")
                name = name.strip() or "Player"
                try:
                    score = int(score_str)
                except ValueError:
                    continue
                if name not in best or score > best[name]:
                    best[name] = score
    except FileNotFoundError:
        pass
    return sorted(best.items(), key=lambda kv: kv[1], reverse=True)


def save_score(name, score):
    """Adds/updates an entry in the leaderboard (keeping only the highest
    score per name), persists it, and returns the new sorted list."""
    scores = dict(load_scores())
    name = name.strip() or "Player"
    if name not in scores or score > scores[name]:
        scores[name] = score
    ranked = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
    ranked = ranked[:MAX_LEADERBOARD_ENTRIES]
    try:
        with open(HIGHSCORE_FILE, "w") as f:
            for n, s in ranked:
                f.write(f"{n},{s}\n")
    except OSError:
        pass  # if we can't write (e.g. read-only folder), just skip silently
    return ranked


def top_score(scores):
    """Returns the (name, score) at the top of the leaderboard, or a
    placeholder if it's empty."""
    return scores[0] if scores else ("---", 0)


def qualifies_for_leaderboard(scores, score):
    if len(scores) < MAX_LEADERBOARD_ENTRIES:
        return True
    return score > scores[-1][1]


def format_leaderboard_line(rank, name, score, width):
    """'name .......... score', right-aligned score, name padded with dots
    so everything lines up on one row."""
    prefix = f"{rank}. {name} "
    score_str = str(score)
    dots_len = width - len(prefix) - len(score_str)
    if dots_len < 1:
        dots_len = 1
        prefix = prefix[: max(0, width - len(score_str) - 1)] + " "
    return prefix + ("." * dots_len) + score_str
