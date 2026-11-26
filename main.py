"""Write the houseplant out-of-office entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, standard library only, no network. The entry is one line,
at most 120 characters, as if a fern sent its own out-of-office auto-reply.
"""

import os
import sys

ENTRY = (
    # The fern has been ignored since March; neglect is the whole joke.
    "Out of office: I'm a fern. You haven't watered me since March, "
    "so now I'm drinking your unread emails. Good luck."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # The grader reads entry.txt as another user; under umask 0007 a plain
    # open() leaves mode 0660, which the grader cannot read (run_completes
    # FAIL). Force world-readable so any user can read the output.
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
