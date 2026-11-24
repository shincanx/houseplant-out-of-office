#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun bounty entry.

Writes one out-of-office auto-reply, as if a houseplant had written it, as
a single line to /output/entry.txt and prints it to stdout. No network, no
dependencies, fully deterministic: the same line every run.
"""

import os

LINE = (
    "Out of office: I'm the fern. Last watered in March. Your email "
    "joins everything else I'm quietly letting die."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
