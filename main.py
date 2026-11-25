"""Copy the pre-rendered front page to the output directory.

The image is drawn offline by draw.py; this program only places the
finished PNG where the scorer expects it, with no network and no
randomness, so every run writes the same bytes.
"""
import os
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SOURCE = os.path.join(BASE, "entry.png")
TARGET = os.path.join(TARGET_DIR, "entry.png")

os.makedirs(TARGET_DIR, exist_ok=True)
shutil.copyfile(SOURCE, TARGET)
