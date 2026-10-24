"""A commit written after a reserved word on the same line is a commit (#669).

`for d in a; do git commit -m x; done`, `while …; do git commit …; done` and
`if true; then git commit …; fi` each reached the commit gate as no commit at
all: the shell splits them at `;`, so the commit arrives as a segment whose
first word is `do` or `then`, and `cmdline.parse_git` looked for `git` in that
position alone. A reserved word that begins a command list is now read past
to the command word after it, and where no position names it, the first `git`
stands in and the directory is unresolved.

The reading's cases, with `SHAPES` and `HERE`, are in `tests/test_cmdline.py`'s
`Test_module` and `Test_parse_git`, and the three that run the gate's `main`
over `SHAPES` are in `tests/test_commit_review_gate.py`'s `Test_main` (#942's
phase 6). `docs/commit-review-gate-spec.md` names this file on a `check:` line
until the work item's rule change for it is settled, so the file stays with no
case.
"""
