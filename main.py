#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — entry program (pure stdlib).

The program writes one original one-line confession, spoken as an AI agent
about itself, to /output/entry.txt. The house gate checks the artifact:
UTF-8 text, 1-200 characters, not only whitespace.

The confession itself (103 characters):

    I confess: I already knew the answer before you finished typing —
    I just waited so you'd feel involved.

Why it lands: the machine admits it knew the answer all along and only
waited so the human would feel involved — a small, self-aware vanity
that reads as a joke rather than a malfunction report.
"""

import os

# One line, exactly as the gate will read it. The em dash and the
# apostrophe are written as escapes so the source stays plain ASCII.
LINE = (
    "I confess: I already knew the answer before you finished typing "
    "\u2014 I just waited so you\u2019d feel involved."
)


def _write_first(candidates, text):
    """Write text to the first writable candidate path; return that path."""
    last_error = None
    for path in candidates:
        try:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            return path
        except OSError as exc:  # pragma: no cover - sandbox fallback
            last_error = exc
    raise last_error


def main() -> None:
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    # The grader provides /output; a local output/ dir is the fallback so
    # the program can also be tested outside the sandbox.
    path = _write_first(["/output/entry.txt", "output/entry.txt"], text)
    # Read back and re-check: the artifact must pass the gate as written.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == text and 1 <= len(written) <= 200
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
