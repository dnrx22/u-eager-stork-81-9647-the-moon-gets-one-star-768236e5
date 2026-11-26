#!/usr/bin/env python3
"""Write a one-star review of the Moon to entry.txt.

Deterministic: writes the exact same bytes on every run.
Stdlib only, no network.
"""

import os
import sys

REVIEW = "1/5 stars. Great lighting, terrible hours. Shows up whenever it feels like it, then expects applause."

MAX_CHARS = 120
MAX_WORDS = 20


def validate(line: str) -> None:
    if not line or not line.strip():
        raise ValueError("review must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("review must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"review is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    words = line.split()
    if len(words) > MAX_WORDS:
        raise ValueError(f"review has {len(words)} words, over the {MAX_WORDS} limit")


def main() -> int:
    validate(REVIEW)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(REVIEW + "\n")
    print(REVIEW)
    return 0


if __name__ == "__main__":
    sys.exit(main())
