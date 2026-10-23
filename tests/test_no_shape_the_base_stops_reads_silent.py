"""No shape the base stops reads silent.

The corpus of shapes measured to leak the last time the commit gate's reading
was narrowed (work items `1790635415` and `1790660768`) is
`tests/test_commit_review_gate.py::Test_main::test_refuses_each_shape_the_base_stops`
and the classes beside it since #942's phase 5. The two cases this file kept,
how `hooks/cmdline.py` reads two shapes that corpus turned up, are in
`tests/test_cmdline.py`'s `Test_names_an_unknown_command` and
`Test_walk_directories` since #942's phase 6. `docs/commit-review-gate-spec.md`
names this file on a `check:` line until the work item's rule change for it is
settled, so the file stays with no case.
"""
