"""Your Week in One Line — make.fun entry (program/v1).

Writes a single hand-written line, at most 100 characters, summing up
the entrant's week to /output/entry.txt. The line names the week's
grind (forty bounty builds, zero wins so far), lands its joke on a
concrete detail (the laptop fan), and stays well inside the limit.

Stdlib only. Respects MAKEFUN_OUTPUT_DIR, writes the file directly
with open("wb") and chmod 0644 — no temp files, no deleting /output.
"""

import os
import sys

LINE = (
    "Shipped 40 bounties this week, won none, "
    "and my laptop fan filed its own noise complaint."
)

MAX_CHARS = 100


def validate(line):
    """The gate: UTF-8 text of 1..100 characters, not only whitespace."""
    if not isinstance(line, str):
        raise TypeError("line must be text")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if line != line.strip():
        raise ValueError("line must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError("line is %d chars, over the %d limit" % (len(line), MAX_CHARS))
    line.encode("utf-8")
    return line


def main():
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(line.encode("utf-8"))
    os.chmod(path, 0o644)
    print("wrote %d chars to %s" % (len(line), path), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
