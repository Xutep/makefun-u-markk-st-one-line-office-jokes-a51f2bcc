"""One-line office joke entry for make.fun.

Writes a single-line joke about office life to /output/entry.txt.
Deterministic, stdlib-only: the same joke every run.
"""

import os

JOKE = "The printer jammed again, so I reported it to HR for creating a hostile work environment."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
