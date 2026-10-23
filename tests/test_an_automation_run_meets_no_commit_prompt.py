"""In a session whose person pressed `automation`, the commit gate puts no
question to anybody: every stop is a `deny` addressed to the model.

The cases are in `tests/test_commit_review_gate.py`'s `Test_automation_pressed`,
which runs `main` with `hooks/worktree_consent.py`'s own reader over a
transcript each case writes, and the reader's own case is in
`tests/test_worktree_consent.py`'s `Test_automation_answered` (#942's phase 6).
`docs/commit-review-gate-spec.md` names this file on a `check:` line until the
work item's rule change for it is settled, so the file stays with no case.
"""
