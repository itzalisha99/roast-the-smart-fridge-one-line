#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes one roast of a smart fridge (at most 160 characters, one line)
to /output/entry.txt.

The entry only works because it is a *smart* fridge: it has a camera
inside it, it photographs what is in there, and it sends the photos to
its owner. A dumb fridge just keeps food cold. The joke turns on the
last words — a hostage negotiator with no demands — which is the one
image nobody else in the field is using.
"""

ENTRY = "My smart fridge photographs my leftovers every night and sends them to me, like a hostage negotiator with no demands."

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Mirror the bounty gate: 1-160 UTF-8 chars, one line, not blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    return True


def main():
    validate(ENTRY)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Read back what we wrote and confirm it is byte-identical to the
    # entry: a silent truncation or encoding change would fail the gate.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY + "\n":
        raise ValueError("written entry does not match the entry text")


if __name__ == "__main__":
    main()
