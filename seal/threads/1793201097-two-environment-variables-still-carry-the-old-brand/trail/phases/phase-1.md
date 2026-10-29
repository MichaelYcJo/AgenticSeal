# Phase 1: 1793201097-two-environment-variables-still-carry-the-old-brand

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | c20b45dc |

## What this phase was asked

Build phase 1 of `frame/plan.md` against the frame at `0c451b8c`, under the
owner's automation answer. `frame/questions.md` Q1 stands on its default
(a): this work does not touch `chain_check.py#OLD_TRAILER` or
`hooks/lib/routing.py#OLD_BY_CRAFTER`. Q2 stands on its default. The phase
removes `SPECSEAL_LINT`: its read in `hooks/lint-python.py#main`, its
docstring sentence, its case in `tests/hooks/test_lint_python.py`, its row
and clause in both READMEs, and its item in `tests/censuses.py#KEPT_OLD_NAMES`,
whose comment then speaks for the `_LANG` item alone. Each case is seen red
before its code lands.

## What this phase found

**The frame holds against the tree (read, at `0c451b8c`).** Every
coordinate of `frame/plan.md` *Technical context* and `frame/design.md`
*Removes* resolves to the text it names. `hooks/lint-python.py` holds the
docstring sentence at line 14 and the read at lines 93 and 94. The case is
at `tests/hooks/test_lint_python.py:203-207`. The census items are at
`tests/censuses.py:1030-1035`. The README rows are at `README.md:186` and
`:287`, and at `README.ko.md:180` and `:280`.

**The defaults this phase built on.** Q1 (a): `chain_check.py` and
`hooks/lib/routing.py` are not touched. Q2 does not reach phase 1.

**How the phase was seen red (executed).** The census item for
`SPECSEAL_LINT` was removed first, with every use of the name still in place.
`bin/test -q -p no:xdist tests/hooks/test_lint_python.py::test_census
tests/test_censuses.py::Test_module::test_every_file_no_module_file_declares_meets_every_census`
exited 1 with both cases red. The old-name census named seven lines, and
these are the seven lines *Removes* names: `hooks/lint-python.py:14` and
`:93`, `README.md:186` and `:287`, `README.ko.md:180` and `:280`, and
`tests/hooks/test_lint_python.py:207`. With the uses removed, the same two
cases, `tests/hooks/test_lint_python.py` whole and
`tests/test_censuses.py::test_census` passed, 18 cases, exit 0.

**S1 holds (executed).** `grep -n environ hooks/lint-python.py` prints
nothing, exit 1. The module still imports `os`, which `uses_ruff` and the
path setup use. After the commit, `git grep -n SPECSEAL_LINT` lists
`changelog/0.23.0.md` and three files under `seal/threads/` and nothing
else, as `frame/plan.md`'s phase 1 *Verified by* cell says.

**A parameter left with the case.** `tests/hooks/test_lint_python.py#_ran`
took an `env` mapping that only the deleted case passed. The parameter and
its loop are removed in the same commit, because nothing else calls `_ran`
with it (executed, `grep -n "env=" tests/hooks/test_lint_python.py`).
`frame/design.md` *Removes* does not name it. It is part of the case the
frame does name, so this phase records no divergence for it.

**No unit was added, so no mutant was run.** The phase removes a read, a
sentence, a case, two rows and a census item. Its red is the census above.
