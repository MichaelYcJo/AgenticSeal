"""Every site in `session_cost.py` that converts a number to an int is
discharged — by a guard, or by an operand that cannot be a derived number.

Every case of this file moved to `tests/test_session_cost.py` in #942's
phase 6, with this file's docstring, its walk and its guard shapes.
`docs/measuring-a-run.md` names this file on a `check:` line until the
settle after the release applies `spec.md`'s item for it, so the file stays
until then with no case.
"""
