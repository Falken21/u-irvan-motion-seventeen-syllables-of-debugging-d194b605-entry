"""Seventeen Syllables of Debugging.

A haiku about debugging, in the classic 5-7-5 shape:

    Cursor blinks at three
    the log says nothing is wrong
    the bug was my own

The program writes exactly this text to /output/entry.txt,
with no trailing newline.
"""

import os

HAIKU = (
    "Cursor blinks at three\n"
    "the log says nothing is wrong\n"
    "the bug was my own"
)


def write_entry(path="/output/entry.txt"):
    """Write the haiku to path exactly, with no trailing newline."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(HAIKU)


def main():
    write_entry()


if __name__ == "__main__":
    main()
