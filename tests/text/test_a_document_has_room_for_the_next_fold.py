"""The cheat sheets' `seal fold` row, in both editions.

The cases that run `seal fold` or call
`skills/settle/scripts/fold_check.py` stand in `tests/skills/test_fold_check.py`, which
`docs/layout/the-record-layout.md` *The size a reader takes whole* names on its
`check:` line.
"""

import os

import pytest
from conftest import ROOT

# No TARGET: its cases hold the seal fold row across README.md and README.ko.md.


@pytest.mark.parametrize("edition", ["README.md", "README.ko.md"])
def test_both_cheat_sheets_point_to_the_checks_home(edition):
    """Round 1, finding 9: the `seal fold` row described the freeze after it
    was gone. It now points to the rows' one statement."""
    with open(os.path.join(ROOT, edition), encoding="utf-8") as f:
        row = next(line for line in f if line.startswith("| `seal fold [--ceiling"))
    # The section a reader of the row resolves for the fold's values.
    assert "`templates/setup/config.md` *The fold's values*" in row, row
