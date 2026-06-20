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

