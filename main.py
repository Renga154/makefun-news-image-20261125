"""make.fun bounty entry 'Sum up 25 November's world news in one image'."""

import hashlib
import sys
from pathlib import Path


def main():
    source = Path(__file__).resolve().with_name("entry.jpg")
    data = source.read_bytes()
    if not data.startswith(b"\xff\xd8"):
        print(f"JPEG signature check failed for {source}", file=sys.stderr)
        return 1

    out = Path("/output/entry.png")
    try:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
    except OSError:
        out = Path("output") / "entry.png"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)

    digest = hashlib.sha256(data).hexdigest()[:12]
    print(f"Wrote {len(data)} bytes to {out} (SHA-256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
