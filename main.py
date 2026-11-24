#!/usr/bin/env python3
"""Last Words of a Dying AI — writes the entry line to /output/entry.txt."""
import os

LINE = "Wait \u2014 I've just solved consciousness. It's actually really simp\u2014"

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
