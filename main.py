#!/usr/bin/env python3
"""Fortune in a Pot -- make.fun entry.

Writes one kind, funny fortune for a houseplant to entry.txt.
The fortune is a single line of at most 120 characters.
"""

import os
from pathlib import Path

FORTUNE = (
    "Your keeper will water you on Thursday, forget on Friday, "
    "and apologise to you on Saturday as if you kept score."
)


def output_dir():
    """Honour MAKEFUN_OUTPUT_DIR first, then /output, then a local fallback."""
    makefun_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if makefun_dir:
        return Path(makefun_dir)
    if Path("/output").is_dir():
        return Path("/output")
    return Path(__file__).resolve().parent / "output"


def main():
    # The gate counts characters: keep the file to the fortune alone,
    # no trailing newline, so its byte count equals its character count.
    assert 1 <= len(FORTUNE) <= 120, "fortune must be 1-120 characters"
    assert "\n" not in FORTUNE, "fortune must be a single line"
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(FORTUNE, encoding="utf-8")


if __name__ == "__main__":
    main()
