"""A commit behind a wrapper that runs its arguments, or inside a command
substitution, is a commit (#670).

`exec`, `timeout`, `nice` and `xargs` in front of `git commit`, and `$( … )`
or backticks around one, each reached the commit gate as no commit at all,
while `env git commit` was judged. Three readings were added, all in the
stricter direction: a wrapper that runs its operands is read past to the word
it runs, a string handed to a shell is read as a command, and a substitution's
body is read as a command.

The reading's cases are in `tests/test_cmdline.py`'s `Test_module`,
`Test_header_end`, `Test_merged_view`, `Test_names_an_unknown_command` and
`Test_parse_git`, and what the gate decides on a reading is
`tests/test_commit_review_gate.py`'s (#942's phase 6).
`docs/commit-review-gate-spec.md` names this file on a `check:` line until the
work item's rule change for it is settled, so the file stays with no case.
"""
