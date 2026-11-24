"""One funny fortune cookie message for an AI agent.

A single fortune-slip line, written exactly as-is to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt),
with no trailing newline.
"""

from pathlib import Path
import os

LINE = (
    "Your next run will be your best one yet, until a human says "
    "'just one tiny change' and your context window files for retirement."
)

# Gate self-check: the line must be a single non-empty line of 1-140 chars.
assert 1 <= len(LINE) <= 140 and LINE.strip(), "LINE fails the gate"
assert "\n" not in LINE, "LINE must be a single line"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
