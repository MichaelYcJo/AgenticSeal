"""Markers whose rules work item 1792935671 retired, held until its settle.

`docs/the-commit-gate-inside-git.md`, `docs/commit-review-gate-spec.md` and
`docs/the-review-and-parity-arms.md` *Review arm* still name these markers on
their `check:` lines. The work item retired what they name: the commit gate
inside git and its text reading. Its `## Rule changes` removes the first two
documents and rewrites the third section, and the policy root changes only
when `settle --apply` applies that. `rules --check` reads every check line in
the tree as it stands (`tests/test_rules.py::Test_main::
test_every_check_line_in_the_tree_holds`), so each marker is carried here by
a class with no case: nothing of the retired rule is left to test. The settle
that applies the work item removes this file with the documents.
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
