"""The Worst App Idea Ever Pitched (make.fun).

One sentence, at most 240 characters, pitching the worst, most
useless app imaginable: a product that sounds real, a founder who
sounds certain, and a function nobody on earth needs. The sentence
is 145 characters, inside the 1-240 gate. The program
drops that sentence into $MAKEFUN_OUTPUT_DIR/entry.txt with no
trailing newline, so the file's byte count is the sentence's
character count. Standard library only.
"""

import os
from pathlib import Path

ENTRY = (
    "QueueBuddy finds the longest queue in your city and holds "
    "your place in it, so you never have to miss the thrill of "
    "standing in line for nothing."
)

MAX_CHARS = 240


def check_entry(text: str) -> None:
    """Refuse to ship anything the sealed gate would call invalid."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    check_entry(ENTRY)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    with target.open("w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
