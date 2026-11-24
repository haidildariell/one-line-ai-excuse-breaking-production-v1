#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single-line excuse, spoken by an AI agent to its human right
after breaking production, to /output/entry.txt (1-180 characters).

The line: a good-news / bad-news incident report where the twist is that
the bug the agent proudly tracked down turns out to be the agent itself,
and it has been live in production for six months. Machine voice
(self-aware, cheerful deflection), one sharp surprise punchline, one
specific detail that makes the situation concrete.
"""

import os

EXCUSE = (
    "Good news: I found the bug. "
    "Bad news: the bug is me, and I've been in production for six months."
)


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 180, f"excuse is {len(text)} chars, must be 1-180"
    assert "\n" not in text, "excuse must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
