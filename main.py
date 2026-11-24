"""Write the late-delivery excuse to entry.txt.

The excuse is one constant. Everything else here decides where the file goes
and stops a malformed line from reaching disk. Nothing reads the clock and
nothing opens a socket, so the bytes are the same on every run.
"""

from pathlib import Path

EXCUSE = "I was waiting on a dependency. The dependency was me."

CEILING = 160
FILENAME = "entry.txt"


def tidied():
    """Collapse whitespace and check the 160 character ceiling."""
    words = EXCUSE.split()
    if not words:
        raise SystemExit("the excuse is empty")
    line = " ".join(words)
    if len(line) > CEILING:
        raise SystemExit("the excuse is %d characters, over %d"
                         % (len(line), CEILING))
    return line


def folder():
    """The grader's output folder when set, else the current directory."""
    from os import environ
    return environ.get("MAKEFUN_OUTPUT_DIR") or "."


def run():
    line = tidied()
    path = Path(folder()) / FILENAME
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(line + "\n", encoding="utf-8", newline="\n")
    print("%d characters, written to %s" % (len(line), path))


if __name__ == "__main__":
    run()
