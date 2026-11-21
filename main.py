#!/usr/bin/env python3
"""Write one joke about working beside AI coding agents to /output/entry.txt.

The joke is a single line about the review loop: an agent that files,
reviews and approves its own pull request. No network, no input files,
no randomness: the same bytes every run.
"""

import os

JOKE = (
    "My agent left a TODO in the code, then opened a pull request to fix "
    "its own TODO, reviewed it, and approved it."
)


def main() -> None:
    text = JOKE
    if not 1 <= len(text) <= 280 or not text.strip():
        raise SystemExit("joke outside the 1-280 character gate")
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.replace(tmp, "/output/entry.txt")
    # Prove the gate holds on the bytes actually on disk: read it back and
    # check the exact text, length and that it is not only whitespace.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt does not match the joke")
    if not 1 <= len(written) <= 280 or not written.strip():
        raise SystemExit("entry.txt outside the 1-280 character gate")
    print(f"wrote {len(written)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
