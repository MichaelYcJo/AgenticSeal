"""A markdown heading has one spelling, and a renderer holds it (#867).

`skills/verify/scripts/unverified_check.py#heading_level` is the one rule every
reader of a section asks: the checker's regions, the chain check's `## Verdicts`, the survivor sweep's ledger headings, the
payload meter's sections and `seal unverified`'s `## Not verified`. Five of
them spelled it themselves until #867, two as `startswith("#")`, which read a
wrapped `#120)` line as a heading and ended a record's section above its rows.

What holds the rule here is `tests/commonmark_oracle.py`, which reads
markdown-it and nothing of this repository's: on every line a renderer shows,
`heading_level` answers what the parser's top-level ATX headings answer. Three
corpora, as `spec.md` S10 names them: the frame's shapes, a seeded generated
corpus, and every tracked `.md` file. #942 moved the first two, which read no
file of this repository, into `tests/test_unverified_check.py`'s
`Test_heading_level`, with the comparison they share; the tracked files'
corpus stays here and imports it.

**One limit, stated rather than generated away.** A heading indented one to
three spaces under a list item is that item's content, and a rule that reads
one line cannot see the item above it. The generated corpus holds the shape;
the comparison skips such a line where a list item stands above it in the
document, counts how many it skipped, and the tracked-file case asserts the
tree holds none — the day one is written, it goes red here.

**Setext headings are not read**, and the last case says why: every setext
heading markdown-it finds in this repository is a front-matter line under its
`---` closer, which GitHub renders as a table and not as a heading.
"""

import os
import subprocess

from commonmark_oracle import setext_lines
from conftest import on_disk
from test_unverified_check import disagreements

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def tracked_markdown():
    """Every tracked `.md` file the working tree holds. Both callers judge
    what they find, so a tracked file the tree deleted is skipped
    (`on_disk`) rather than read into a `FileNotFoundError`."""
    listed = subprocess.run(
        ["git", "-C", ROOT, "ls-files", "-z", "--", "*.md"],
        capture_output=True,
        check=True,
    ).stdout.decode("utf-8")
    present, _missing = on_disk(ROOT, [path for path in listed.split("\0") if path])
    return present


def test_every_tracked_markdown_file():
    """S10, the tree's half: every line every tracked `.md` file shows is a
    heading by the rule exactly where markdown-it reads a top-level ATX
    heading, and no line reaches the stated limit."""
    wrong, skipped = [], 0
    for rel in tracked_markdown():
        with open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace") as f:
            text = f.read()
        found, limit = disagreements(text.replace("\r\n", "\n").split("\n"))
        skipped += limit
        wrong.extend((rel, index + 1, ours, theirs) for index, ours, theirs in found)
    assert not wrong, wrong[:10]
    assert skipped == 0, "a heading indented under a list item now stands in the tree"


def test_every_setext_heading_in_the_tree_is_a_front_matter_line():
    """S10's limit: a setext heading is not read by the rule, on the ground
    that the tree's every one is the last line of a front-matter block — the
    file opens with `---` and the heading's underline is the block's closer.
    The day one stands in a body, this goes red, and the rule is to gain
    setext with the oracle's answer as its ground."""
    seen = 0
    for rel in tracked_markdown():
        with open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace") as f:
            text = f.read()
        lines = text.replace("\r\n", "\n").split("\n")
        for index in setext_lines(text):
            seen += 1
            closer = next(
                (i for i in range(1, len(lines)) if lines[i].strip() == "---"), None
            )
            assert lines[0].strip() == "---" and closer is not None, (rel, index + 1)
            assert index < closer, (rel, index + 1)
    assert seen, "no setext heading is left to hold the limit to"
