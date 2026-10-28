"""The worktree guard asked once per worktree, so an unattended run stopped
at the first `git worktree add` and again at every one after it.

`hooks/worktree_consent.py`'s cases, the writer's and the routing answer's
reader's, moved to `tests/hooks/test_worktree_consent.py`, and the helpers other
files imported from here to `tests/conftest.py` (#942's phase 6). What stays
is the case that reads `skills/implement/orchestration.md`'s routing question,
which is #923's.
"""

import pathlib

from conftest import load_hook_module

wc = load_hook_module("worktree_consent.py", "wc_consent")


def test_the_labels_match_the_routing_question_the_orchestrator_asks():
    """The reader's constants against `skills/implement/orchestration.md`
    *Question 1*. Relabelling the question there turns this red instead of
    quietly bringing the guard's prompt back. Seen red by editing a
    constant."""
    root = pathlib.Path(__file__).resolve().parent.parent
    text = (root / "skills" / "implement" / "orchestration.md").read_text(
        encoding="utf-8"
    )
    section = text.split("\n### Question 1\n", 1)[1].split("\n### ", 1)[0]
    labels = [
        row.split("|")[2].strip().strip("*")
        for row in section.splitlines()
        if row.startswith("| ") and row.split("|")[1].strip().isdigit()
    ]
    assert tuple(labels) == wc.ROUTING_LABELS
    assert labels[0] == wc.PRESET
