"""Markers whose rules work item 1792935671 retired, held until its settle.

`docs/the-commit-gate-inside-git.md`, `docs/commit-review-gate-spec.md` and
`docs/the-review-and-parity-arms.md` *Review arm* still name these markers on
their `check:` lines. The work item retired what they name: the commit gate
inside git and its text reading. Its `## Rule changes` removes the first two
documents and rewrites the third section, and the policy root changes only
at the settle that writes those sections. `rules --check` reads every check line in
the tree as it stands (`tests/test_rules.py::Test_main::
test_every_check_line_in_the_tree_holds`), so each marker is carried here by
a class with no case: nothing of the retired rule is left to test. Nothing
removes this file on its own, because `settle` touches no file under
`tests/`: the pull request that settles this work item deletes it, with the
five caseless files `docs/` names for it, as issue #1028 asks.
"""

import pytest


@pytest.mark.rule("review-arm-asks")
class Test_review_arm_asks:
    """`docs/the-review-and-parity-arms.md` *Review arm*: the review arm
    asked at the commit. The routing check at the edit tools holds the
    routing now, `tests/test_routing_edit_gate.py`."""


@pytest.mark.rule("judged-inside-the-commit")
class Test_judged_inside_the_commit:
    """`docs/the-commit-gate-inside-git.md`: git judged a commit inside the
    commit. No hook of this plugin runs inside git now."""


@pytest.mark.rule("text-reading-stands-aside")
class Test_text_reading_stands_aside:
    """`docs/the-commit-gate-inside-git.md`: the text reading stood aside
    where git decided. The text reading is gone."""


@pytest.mark.rule("sealed-off-the-branch-refused")
class Test_sealed_off_the_branch_refused:
    """`docs/the-commit-gate-inside-git.md`: `pre-commit` refused the commit
    of a `sealed` over a commit the branch does not hold. The stamp's writer
    refuses it at the write now, under `refused-sealed-leaves-a-record`."""
