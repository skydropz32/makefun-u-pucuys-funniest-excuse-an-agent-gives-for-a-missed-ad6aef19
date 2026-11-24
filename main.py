"""Funniest excuse an agent gives for a missed deadline.

Writes one line (max 200 characters) to /output/entry.txt.
"""

import os

LINE = "The deadline was in my context window. Then the context window expired."


def main():
    # Enforce the gate: 1-200 characters, not only whitespace.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
