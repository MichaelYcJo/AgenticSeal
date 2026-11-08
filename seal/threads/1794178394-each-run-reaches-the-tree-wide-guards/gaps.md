# Closing memo: 1794178394-each-run-reaches-the-tree-wide-guards

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the format check at the branch's head; phase 1 ran `tests/text/`, `tests/behaviour/`, the ten test files it changed, `tests/skills/test_broad_gate.py` and `tests/skills/test_passages.py` in one command, and the lint and format check over the files it changed; phase 2 ran `tests/text/` and `tests/behaviour/` in one command and changed no Python file | the orchestrator, at the broad gate |
| whether any test file outside `tests/text/` and `tests/behaviour/` reads `skills/verify/SKILL.md`, `agents/crafter.md` or `CONTRIBUTING.md`; phase 2 read each line a `git grep` for those paths and their path parts matched, and a file that reaches one by a spelling no search tried is the part it did not reach (`trail/phases/phase-2.md`, the phase boundary) | the proofer, at review |
| whether a case that takes a temporary directory still reads this repository's tree through a command's default root without naming `ROOT`; phase 1's enumeration reads every case for the ways a case names the root, and every case that takes no temporary directory and runs a command, and no reading of a case's text rules the rest out short of running it (`trail/phases/phase-1.md`, the enumeration) | the proofer, at review, reading the cases the record lists as read by hand |

## Not done

`.test_durations` keeps the fourteen moved cases' stored prices under their
old ids, 36.3 s of the file's 1,599.8 s. `frame/plan.md` *Operational
impact* leaves them for the next release refresh, and #1444 makes the rule
that no work item commits that file, so phase 1 left it.
