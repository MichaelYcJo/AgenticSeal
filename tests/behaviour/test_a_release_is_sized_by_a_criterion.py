"""What the criterion that sizes a release does not change.

`docs/releasing/issues-and-milestones.md` *A milestone answers when, and takes three
shapes* sizes a release by what has to be in effect before the next work item
starts, and its paragraph opening **What the criterion does not change.** says
what stays as it was: a `release:` milestone is still the pool a release is cut
from, `backlog:` is still the unscheduled pool, and nothing schedules from
either. The case below reads that paragraph.

**The case reads the file with its wraps collapsed**, through `flat()`. The
document is hand-wrapped at 88 columns (`tests/behaviour/test_docs_line_wrap.py`),
so a phrase pinned as written on one line breaks the moment a word is added
earlier in the paragraph, and a phrase searched for on one line is missed the
moment its wrap falls inside it.
"""

import os

from conftest import ROOT

OWNER = "docs/releasing/issues-and-milestones.md"


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def flat(rel):
    """The file with every run of whitespace collapsed to one space.

    A hand-wrapped paragraph is one sentence to a reader and several lines to
    `in`.
    """
    return " ".join(read(rel).split())


def test_the_rule_says_what_it_does_not_change():
    """Three clauses in one place, so a reader does not have to assemble them
    from a milestone table and a label section."""
    doc = flat(OWNER)
    for clause in (
        "still the pool a release is cut from",
        "still the unscheduled pool",
        "nothing schedules from either",
    ):
        assert clause in doc, f"{OWNER} no longer says {clause!r}"
