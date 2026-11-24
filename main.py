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


def validate(text: str) -> str:
    """One line, 1-180 UTF-8 characters, not whitespace only."""
    line = text.strip()
    if not 1 <= len(line) <= 180:
        raise ValueError(f"excuse is {len(line)} chars, must be 1-180")
    if "\n" in line or "\r" in line:
        raise ValueError("excuse must be a single line")
    if not line.strip():
        raise ValueError("excuse must not be whitespace only")
    return line


def write_entry(text: str, out_dir: str) -> str:
    """Write the validated excuse to <out_dir>/entry.txt, return its path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main() -> None:
    text = validate(EXCUSE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    write_entry(text, out_dir)


if __name__ == "__main__":
    main()
