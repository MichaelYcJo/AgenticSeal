"""A root nobody chose a mode for is a state something names.

Issue #151, reported from a monorepo on its first work item under SpecSeal:
the session created `seal/` and started working. Nothing asked about shared or
local mode, and nothing asked the migration question.

This file holds no case since #942's phase 6. The gate's cases are in
`tests/test_mode_gate.py`, the reader's, the cases of `hooks/config.py`, in
`tests/test_config.py`, and the writer's, `skills/implement/scripts/seal.py`'s
`write_row` and `with_row` with `seal.py`'s re-export of the reader, in
`tests/test_seal.py`. `docs/one-root-by-lifetime.md` and its Korean edition
each name this file on a `check:` line, so it stays until the settle that
applies the work item's rule changes. `tests/test_first_setup_asks_once.py`
pins the half that points at the question: the preset sentence, and the
bootstrap the sentence sends a session to.
"""
