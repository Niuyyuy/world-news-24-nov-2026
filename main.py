"""Publish the finished 24 November 2026 front page.

The artwork itself is produced elsewhere; this script only places the
already-rendered picture where the harness expects it. It takes the
committed ``entry.png`` that sits next to this file and copies it into
the output folder, unchanged, so the published image is exactly the
one that was reviewed. Nothing is fetched from the network and nothing
about the picture is altered, which keeps repeated runs identical.
"""

from pathlib import Path
import os
import shutil


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"

    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)

    destination = target_dir / "entry.png"
    shutil.copyfile(source, destination)

    # Guard: the published copy must be a faithful copy of the source.
    copied = destination.stat().st_size
    original = source.stat().st_size
    if copied != original:
        raise SystemExit(
            f"Copy mismatch: {destination} is {copied} bytes, "
            f"expected {original} bytes from {source}"
        )
    print(f"Published {source} -> {destination} ({destination.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
