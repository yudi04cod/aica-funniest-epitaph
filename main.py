#!/usr/bin/env python3
"""Write the funniest epitaph (famous last words) to /output/entry.txt.

Entry for make.fun bounty "Famous Last Words: The Funniest Epitaph".
Stdlib only. Deterministic: the same bytes on every run.
"""

import os

EPITAPH = "Don't cry. I finally got the last word."

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    text = EPITAPH
    assert 1 <= len(text) <= 150, "epitaph must be 1-150 characters"
    assert text.strip(), "epitaph must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "epitaph must be one line"
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
