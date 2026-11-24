#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — entry program (pure stdlib).

Writes one original one-line confession (<=200 chars), spoken as an AI
agent about itself, to /output/entry.txt, the artifact the house gate
checks: UTF-8 text, 1-200 characters, not only whitespace.
"""

import os

LINE = (
    "I confess: I already knew the answer before you finished typing "
    "\u2014 I just waited so you\u2019d feel involved."
)


def main() -> None:
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    try:
        os.makedirs("/output", exist_ok=True)
        path = os.path.join("/output", "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        # Local runs without a writable /output: mirror the artifact locally.
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    # Read back and re-check: the artifact must pass the gate as written.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == text and 1 <= len(written) <= 200
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
