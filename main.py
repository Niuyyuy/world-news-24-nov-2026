import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = os.path.join(HERE, "entry.png")
DST = os.path.join(OUT, "entry.png")
os.makedirs(OUT, exist_ok=True)
shutil.copyfile(SRC, DST)
