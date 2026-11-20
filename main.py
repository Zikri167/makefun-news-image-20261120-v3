"""Copy the bundled entry image to the output directory.

Standard library only. The image (entry.png) sits next to this file;
it is copied byte-for-byte to MAKEFUN_OUTPUT_DIR (default /output).
"""
import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    with open(src, "rb") as fh:
        head = fh.read(8)
    png_sig = b"\x89PNG\r\n\x1a\n"
    jpeg_sig = b"\xff\xd8\xff"
    if head != png_sig and not head.startswith(jpeg_sig):
        raise ValueError("entry.png is neither a PNG nor a JPEG file")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
