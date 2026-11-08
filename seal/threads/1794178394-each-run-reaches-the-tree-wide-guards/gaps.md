# Closing memo: 1794178394-each-run-reaches-the-tree-wide-guards

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the format check at the branch's head; phase 1 ran `tests/text/`, `tests/behaviour/`, the ten test files it changed, `tests/skills/test_broad_gate.py` and `tests/skills/test_passages.py` in one command, and the lint and format check over the files it changed | the orchestrator, at the broad gate |
| whether a case that takes a temporary directory still reads this repository's tree through a command's default root without naming `ROOT`; phase 1's enumeration reads every case for the ways a case names the root, and every case that takes no temporary directory and runs a command, and no reading of a case's text rules the rest out short of running it (`trail/phases/phase-1.md`, the enumeration) | the proofer, at review, reading the cases the record lists as read by hand |

## Not done

`.test_durations` keeps the fourteen moved cases' stored prices under their
old ids, 36.3 s of the file's 1,599.8 s. `frame/plan.md` *Operational
impact* leaves them for the next release refresh, and #1444 makes the rule
that no work item commits that file, so phase 1 left it.
