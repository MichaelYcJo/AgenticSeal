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
    assert not offenders, f"coordinate-tied rows in the schedulable list: {offenders}"


def test_the_header_says_what_belongs_and_what_does_not():
    text = read(FOLLOW_UP)
    assert "schedulable item in a repository with no tracker" in text
    assert "Anything tied to a coordinate" in text
    assert 'grep -rn "RIDER:"' in text


def test_the_header_says_a_rider_carries_no_stamp_and_no_checker():
    """`seal/follow-up.md` is where the convention is written down, and the
    stamps and their checker left in #964: a hash kept beside the tree to stay
    in step with it is the class `skills/core/SKILL.md` *The rule a mechanism
    is kept against* removes. Nothing else reads this header, so a sentence putting
    the stamp back, or naming the checker as though it ran, would be the one
    place the old convention survived. Seen red against the header as it
    stood at 74c7963a, which named both."""
    text = read(FOLLOW_UP)
    assert "A rider outliving its fix is the reader's finding" in " ".join(text.split())
    assert "Verified <date>" not in text, "the header describes a stamp again"
    assert "rider_check" not in text, "the header names a checker that is gone"


def test_the_record_says_why_target_sha_names_a_commit():
    """A round record's `target:` line names a commit although a squash
    orphans it after the merge, because it records a moment and the check
    reads it only while the branch that holds the commit is open. Leaving
    that unwritten re-opens #239's question for the one place a commit is
    still named. The case holds one clause `docs/branch-and-release.md:165`
    still names this module for."""
    text = " ".join(read(os.path.join(ROOT, "docs", "the-review-record.md")).split())
    # A phrase of the rule, not a fact: the last assert of this module that
    # reads the rule `docs/branch-and-release.md:165` closes, kept unchanged
    # until that line's change lands (#1233, `frame/design.md` Scope item 9).
    assert "`target:` names a commit, not a content anchor" in text


def test_the_header_stops_the_answerer_that_is_really_a_condition():
    """The file already forbade a deferral to nobody, and every one of its
    seventeen rows read `repository owner, next time X is opened` — a
    condition wearing a person's clothes. Issue #34 is that pair."""
    text = read(FOLLOW_UP)
    assert "no condition attached" in text
    assert "condition wearing a person's clothes" in text
    for row in rows("Schedulable items with nowhere else to go"):
        assert "next time" not in " ".join(row), row


def test_the_file_records_what_the_move_costs_and_that_it_can_be_overturned():
    """A judgment nobody can find is a judgment nobody can reverse."""
    text = read(FOLLOW_UP)
    assert "Nothing forces a rider to be deleted" in text
    assert "overturned" in text


def test_the_riders_exist_where_the_rows_said_they_would():
    """Every file a row said its rider went to.

    `hooks/dispatch.py` left the list when its rider was resolved: the
    silence it recorded is said now (#28, work item 1790635415), and a rider
    kept after its fix is the cost this file names. `hooks/lib/cmdline.py`
    left it when the `chdirs` its rider described left with the worktree
    guard, their one reader (#1049)."""
    for rel in (
        "hooks/lib/optin.py",
        "hooks/review-skill-gate.py",
    ):
        assert "# RIDER:" in read(os.path.join(ROOT, rel)), rel


def test_a_held_file_is_named_with_the_branch_holding_it():
    """A rider that cannot be planted has to say what unblocks it, or it is a
    deferral to nobody."""
    for target in rows("Riders waiting on a file another branch holds"):
        assert "held by" in target[0], target[0]
        assert target[-1].strip() not in ("", "—"), f"no answerer: {target}"
