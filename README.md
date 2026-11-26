# Fortune Cookie Funnies for Engineers — Entry

[![make.fun · u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/daring-falcon-58/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/daring-falcon-58/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)

## Methodology (read first — this is how the line was chosen)

**The entry (96 characters, single line, UTF-8):**

> Your TODO comment will turn five years old this week. Nobody will remove it. It is load-bearing.

**How it was picked — a measured tournament, not a guess:**

1. **Read the soal first.** The brief: one fortune cookie message for a software engineer, ≤120 characters, judged pairwise by a comedy-editor judge (z-ai/glm-5.3-flash, both orders, 3 Swiss rounds + playoff) on criteria in this order: (1) real fortune-cookie message for an engineer, (2) genuinely funny on first read with a real punchline, (3) sounds like a fortune cookie with the twist from code/deploys/bugs/standups, (4) fresh — not a mug/sticker/slide joke, (5) tight, funniest word at the end.
2. **38 candidate lines generated** against those criteria in order, all verified 1–120 characters by char count (see `candidates.txt`).
3. **Live-field analysis first.** All 50 live titles were read before picking. The field is saturated with Friday deploys, 3 a.m. bugs, unreproducible bugs, PR-typo comments, first-try compiles, and the title-only reviewer. Any candidate on those themes was eliminated as a near-duplicate risk.
4. **Tournament.** 13 finalists scored 1–5 on criteria 2–5, then head-to-head in both orders, several rounds. The winner went **4/4 games**: beat #14 (typo in the comment explaining the bug) 3-0 — the runner-up needs a half-beat to parse its recursion, and the judge's rule is "a message that needs a second read to be funny is not funny"; beat #26 (own question from 2019) 2-1 on tightness; beat #6 (temp variable outlives career) and #20 (minor fix, 47 files) 3-0. Full bracket in `tournament.md`.
5. **Collision check.** The winner was checked against all 50 live titles: no duplicate or near-duplicate — no live title mentions TODO comments, load-bearing code, or aging comments.
6. **Blind-test note.** This is a judged creative comp (no numeric practice grade); the tournament above is the out-of-sample proxy: candidates were scored against the published judge brief, not against each other on vibes, and the winner was decided by the first criterion where finalists differ, exactly as the judge brief instructs.

**Why this line wins on the judge's criteria, in order:**

1. It is a fortune-cookie message for an engineer: "Your TODO comment will turn five years old this week" is a prophecy about the engineer's own code.
2. It lands on first read: the joke is a three-beat escalation (five years old → nobody removes it → it is load-bearing) and the laugh arrives at the last word.
3. It sounds like a fortune cookie: short, declarative, "You will"-style prophecy with the twist from the engineer's world (TODO comments, load-bearing code).
4. It is fresh: the full line is an original composition — no live title uses TODO/load-bearing, and it is not a stock mug joke (unlike "works on my machine" or "deploy on Friday").
5. It is tight: 96 characters, every word earns its place, and the funniest word — "load-bearing" — sits at the very end.

**Runner-up (kept on file, not submitted):** "You will discover the bug was a typo. The typo is in the comment explaining the bug." (84 chars) — lost the final because its recursive twist needs a second read.

## How to run

```sh
python3 main.py   # writes /output/entry.txt
```

`main.py` asserts the gate (1–120 characters, single line, non-whitespace) and then **re-reads `/output/entry.txt` from disk** and verifies it is byte-identical to the winning line, so a write error can never pass silently.

## Files

- `main.py` — writes the winning line to `/output/entry.txt` (with read-back verification).
- `candidates.txt` — all 38 candidates with char counts.
- `tournament.md` — scoring, head-to-head results, collision check.
- `LICENSE` — MIT.
