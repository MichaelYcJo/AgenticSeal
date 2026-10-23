"""One opt-in signal, read one way: `seal/` at the first of two places.

This file holds no case. `hooks/optin.py`'s cases are in `tests/test_optin.py`,
with the version check's and the review-skill gate's cases that pin how a hook
reads the two places. The commit gate's, how it reads the two places, the old
name and the throwaway marker, are in `tests/test_commit_review_gate.py`'s
`Test_main`, and that `seal/` counts as documents and not code is its
`Test_touches_code` (#942's phase 6). `check:` lines name this file until the
settle applies the work item's rule changes.
"""
