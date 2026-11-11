"""A deferral is either a rider or a schedulable item, and they live apart.

Thirteen rows sat in `.specseal/follow-up.md`. Classified by their answerer
column, most of them were not "someone should do this" at all — they were
*"if you open this file, do this too"*, which is worth exactly as much as its
chance of reaching the person who opens that file. A file nobody opens to find
out what to work on next has none.

So a rider goes to its coordinate as a `# RIDER:` comment, and
`grep -rn "RIDER:"` is the list. What stays in `follow-up.md` is the narrow
case issue #34 named in its own third checkbox: a schedulable item in a
repository with no tracker.

The failure this guards against is the file quietly refilling. A coordinate-
tied row written here is one nobody at that coordinate will ever see.
"""

import os
import re

from conftest import ROOT, read

# No TARGET: its cases hold the rider rule across seal/follow-up.md and the files a rider stands in.

FOLLOW_UP = os.path.join(ROOT, "seal", "follow-up.md")

# A coordinate is `path/to/file.ext:123` — the shape a rider is written at.
COORDINATE = re.compile(r"[\w./-]+\.(?:py|md|json|yml|yaml|sh):\d+")


def rows(section):
    """Table rows under one `## ` heading of follow-up.md."""
    text = read(FOLLOW_UP)
    body = text.split(f"## {section}", 1)[1].split("\n## ", 1)[0]
    out = []
    for line in body.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if set("".join(cells)) <= set(":- ") or cells[0] in ("Item", "Target"):
            continue
        out.append(cells)
    return out


def test_no_schedulable_row_carries_a_coordinate():
    """A row with a `file.py:120` in it is a rider filed where its reader is
    not. The rider list is `grep RIDER:`, and this section is not it."""
    offenders = [
        r
        for r in rows("Schedulable items with nowhere else to go")
        if COORDINATE.search(" ".join(r))
    ]
    # `seal/follow-up.md` *Anything tied to a coordinate is a `# RIDER:`
    # comment at the line it is about.*: a `path:line` coordinate, which the
    # file's reader would act on at a line nobody there will see.
    assert not offenders, f"coordinate-tied rows in the schedulable list: {offenders}"


def test_the_header_gives_the_command_that_lists_the_riders():
    text = read(FOLLOW_UP)
    # The command the header gives a reader for the list of riders.
    assert 'grep -rn "RIDER:"' in text


def test_the_riders_exist_where_the_rows_said_they_would():
    """Every file a row said its rider went to.

    A rider kept after its fix is the cost this file names. The command
    reader `cmdline.py` left it when the `chdirs` its rider described left
    with the worktree guard, their one reader (#1049). The review-skill gate
    left it with its rider when the gate went (#1376)."""
    for rel in ("lib/optin.py",):
        # The marker `grep -rn "RIDER:"` matches, at the file a row sent its
        # rider to.
        assert "# RIDER:" in read(os.path.join(ROOT, rel)), rel


def test_a_rider_waiting_on_a_held_file_names_who_answers_it():
    """A rider that cannot be planted names who answers it, or it is a
    deferral to nobody."""
    for target in rows("Riders waiting on a file another branch holds"):
        assert target[-1].strip() not in ("", "—"), f"no answerer: {target}"
