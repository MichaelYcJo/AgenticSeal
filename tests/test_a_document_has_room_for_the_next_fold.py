"""What is left of `seal fold`'s old file: the two cases that read the
cheat sheets and the settle skill, which wait for #923.

#942's phase 6 placed the cases that run `seal fold` or call
`skills/settle/scripts/fold_check.py` in `tests/test_fold_check.py`, which
`docs/the-record-layout.md` *The size a reader takes whole* names on its
`check:` line.
"""

import os

import pytest

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))


@pytest.mark.parametrize("edition", ["README.md", "README.ko.md"])
def test_both_cheat_sheets_point_to_the_checks_home(edition):
    """Round 1, finding 9: the `seal fold` row described the freeze after it
    was gone. It now points to the rows' one statement and restates none."""
    with open(os.path.join(ROOT, edition), encoding="utf-8") as f:
        row = next(line for line in f if line.startswith("| `seal fold [--ceiling"))
    assert "`templates/config.md` *The fold's values*" in row, row
    assert "frozen" not in row and "고정" not in row, row


def test_settle_owns_the_placement_rule():
    """A11. The rule is settle's, in general form, and it sets no value."""
    with open(
        os.path.join(ROOT, "skills", "settle", "SKILL.md"), encoding="utf-8"
    ) as f:
        text = f.read()
    section = text.split("\n## A document past its ceiling is split, never trimmed\n")
    section = " ".join(section[1].split("\n## ")[0].split())
    for phrase in (
        "is recommended to be split by topic along its own headings",
        "nothing is cut to fit",
        "The plugin sets no ceiling",
    ):
        assert phrase in section, f"settle no longer says: {phrase!r}"
