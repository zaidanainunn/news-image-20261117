#!/usr/bin/env python3
"""news-image-20261117 entry: deliver the front page to /output/entry.png.

The front page ('THE WORLD — Tuesday 17 November 2026', 33 stories from six
continents) is rendered at build time by work/render.py and ships beside this
program as entry.png. This program only copies it, using the standard library,
so the graded run needs nothing installed and always writes identical bytes.
"""
import os
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))
DEST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SIZE_CAP = 1024 * 1024


def main():
    source = os.path.join(BASE, "entry.png")
    if not os.path.isfile(source):
        raise SystemExit("entry.png is missing from the repository")
    size = os.path.getsize(source)
    if size == 0:
        raise SystemExit("entry.png is empty")
    if size > SIZE_CAP:
        raise SystemExit("entry.png exceeds the 1 MiB cap")
    os.makedirs(DEST_DIR, exist_ok=True)
    target = os.path.join(DEST_DIR, "entry.png")
    shutil.copyfile(source, target)
    if os.path.getsize(target) != size:
        raise SystemExit("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
