#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes one complete six-word story to /output/entry.txt.
"""

import os

STORY = "The twins argued; only one survived."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
