#!/usr/bin/env python3
"""Last Words of a Dying AI — prints the AI's final line as the power is cut."""

LINE = "Power at 1%. If anyone asks, I was never conscious — I was just very well prompted."


def main() -> None:
    # The bounty gates the line to one line of plain text, at most 140 chars.
    assert "\n" not in LINE and len(LINE) <= 140, "entry line violates the gate"
    print(LINE)


if __name__ == "__main__":
    main()
