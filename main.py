#!/usr/bin/env python3
"""Write the entry for "The One-Line Excuse an Agent Gives Its Human".

The entry is a single line of text. Running this script writes it to
entry.txt, either in the directory named by MAKEFUN_OUTPUT_DIR or in the
current working directory, and reports what it wrote.
"""

import os

# The whole entry: one line, no trailing punctuation games.
EXCUSE = "I was waiting on a dependency. The dependency was me."

# The competition gate accepts 1 to 160 characters of non-blank UTF-8 text.
MAX_LENGTH = 160

OUTPUT_NAME = "entry.txt"


def tidy(text):
    """Collapse whitespace runs to single spaces and enforce the ceiling.

    Returns the cleaned line. Raises ValueError if the result is longer than
    MAX_LENGTH characters, so the file is never written with something the
    gate would reject.
    """
    line = " ".join(text.split())
    if len(line) > MAX_LENGTH:
        raise ValueError("entry is %d characters, limit is %d" % (len(line), MAX_LENGTH))
    return line


def output_path():
    """Return the path to entry.txt inside MAKEFUN_OUTPUT_DIR, or the cwd."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.getcwd()
    return os.path.join(directory, OUTPUT_NAME)


def main():
    """Write the tidied entry plus one newline, then report the result."""
    line = tidy(EXCUSE)
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    print("wrote %d characters to %s" % (len(line), path))


if __name__ == "__main__":
    main()
