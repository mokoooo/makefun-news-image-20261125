#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261125 competition.

The entry is one image summing up the world news of Wednesday
25 November 2026. The image ships in this repository as ``entry.png``
(drawn beforehand by a scripted PIL build; see README). This program
only places those exact bytes where the grader looks for them:

    <output dir>/entry.png

The output dir is ``$MAKEFUN_OUTPUT_DIR`` when set (local tests) and
``/output`` otherwise (the sandbox). No network, standard library
only, fully deterministic: the asset is copied byte for byte, so two
runs write identical files. The copy is atomic (temp file + rename)
and verified after writing.
"""

import os
import sys
from pathlib import Path

ASSET_NAME = "entry.png"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_ASSET_BYTES = 1_048_576  # competition cap: 1 MiB


def main() -> int:
    asset = Path(__file__).resolve().parent / ASSET_NAME
    if not asset.is_file():
        print(f"error: asset not found: {asset}", file=sys.stderr)
        return 1
    data = asset.read_bytes()
    if len(data) > MAX_ASSET_BYTES or not data.startswith(PNG_SIGNATURE):
        print(f"error: invalid PNG asset: {asset}", file=sys.stderr)
        return 1
    # The IHDR chunk follows the signature: width and height are the
    # big-endian uint32s at bytes 16..24. The gate caps images at
    # 1024x1024, so fail loudly rather than emit an ungradable file.
    if len(data) < 24:
        print(f"error: truncated PNG asset: {asset}", file=sys.stderr)
        return 1
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if width > 1024 or height > 1024:
        print(f"error: asset is {width}x{height}, over the 1024 cap",
              file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / ASSET_NAME
    tmp = out_dir / f".{ASSET_NAME}.tmp"
    try:
        tmp.write_bytes(data)
        os.replace(tmp, dest)
    except OSError as exc:
        tmp.unlink(missing_ok=True)
        print(f"error: could not write {dest}: {exc}", file=sys.stderr)
        return 1
    if dest.read_bytes() != data:
        print(f"error: copied file differs from asset: {dest}", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
