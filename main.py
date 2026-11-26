"""Fortune Cookie Funnies for Engineers — entry program.

Writes the tournament-winning one-line fortune cookie message for a
software engineer to /output/entry.txt.

Winning line (96 characters, verified <= 120, single line, UTF-8):
    Your TODO comment will turn five years old this week. Nobody will remove it. It is load-bearing.

Method: 38 candidate lines generated against the judge persona's criteria
in order (real engineer fortune > funny on first read > sounds like a
fortune cookie > fresh > tight with the funniest word at the end), scored,
then head-to-head tournament in both orders, several rounds. Winner beat
#14 (typo in the comment explaining the bug), #26 (own question from 2019),
#6 (temp variable outlives career) and #20 (minor fix, 47 files) 4/4 games.
Collision-checked against all 50 live titles: no duplicate or
near-duplicate (no live title mentions TODO, load-bearing, or aging comments).
See tournament.md for the full bracket and README.md for methodology.
"""

import os

WINNING_LINE = (
    "Your TODO comment will turn five years old this week. "
    "Nobody will remove it. It is load-bearing."
)


def main() -> None:
    line = WINNING_LINE.strip()
    assert 1 <= len(line) <= 120, f"entry must be 1-120 chars, got {len(line)}"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Read-back verification: re-check the exact winning line and char count
    # from the file on disk, so a write error or truncation can never pass
    # silently. The gate counts characters (not bytes); the file must hold
    # exactly one line, 1-120 chars, non-whitespace, byte-identical to the
    # tournament winner.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line + "\n", "entry.txt does not match the winning line"
    assert 1 <= len(written.strip()) <= 120, (
        f"entry.txt char count out of gate: {len(written.strip())}"
    )
    assert written.strip(), "entry.txt must not be only whitespace"


if __name__ == "__main__":
    main()
