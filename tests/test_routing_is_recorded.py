"""The routing answer is recorded, so the gate stops re-deriving it.

The answer to "does this work go through the review chain" is given before the
first edit. Nothing received it, so the gate re-derived it at every commit from
the absence of a review mark -- a mark that only exists after a review passes.
Every commit of every round was stopped on its way to the reviewer the answer
had already named.

A declaration at `seal/specs/<work-item-id>/routing.md` is what the gate reads instead.
Enforcement does not disappear; it moves to the pull request, where CI checks a
branch that said "through the chain" against its review record.

Failure direction: a declaration that cannot be read is not a declaration. The
gate falls back to what it does today rather than falling silent, because a
gate a corrupt file switches off is the standing waiver the chain spec forbids.

This file holds no case. `hooks/routing.py`'s own cases, the parser's, are in
`tests/test_routing.py`, and the cases that run the commit gate over a
declaration are in `tests/test_commit_review_gate.py`'s `Test_main` (#942's
phase 6). A `check:` line names this file until the settle applies the work
item's rule change.
"""
