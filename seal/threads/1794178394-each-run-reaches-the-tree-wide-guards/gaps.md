# Closing memo: 1794178394-each-run-reaches-the-tree-wide-guards

## Not verified

| Item | Who must answer |
|---|---|
| closed the full suite, the repository-wide lint and the format check at the branch's head; phase 1 ran `tests/text/`, `tests/behaviour/`, the ten test files it changed, `tests/skills/test_broad_gate.py` and `tests/skills/test_passages.py` in one command, and the lint and format check over the files it changed; phase 2 ran `tests/text/` and `tests/behaviour/` in one command and changed no Python file | answered by the work item's broad gate, `trail/gate.md` `run: 7e58aec6 against c7bb14ca`, which names no failing case and on which `guarantee.md` sealed |
| closed whether any test file outside `tests/text/` and `tests/behaviour/` reads `skills/verify/SKILL.md`, `agents/crafter.md` or `CONTRIBUTING.md`; phase 2 read each line a `git grep` for those paths and their path parts matched, and a file that reaches one by a spelling no search tried is the part it did not reach (`trail/phases/phase-2.md`, the phase boundary) | a measurement no record asks for: the answer would decide whether `CONTRIBUTING.md` *The test layout*'s tree-wide set misses a reader, which would show as a later work item's broad gate failing on a case its narrow runs did not reach; no such failure, open issue or other work item's rule is on record, and nothing is opened |
| closed whether a case that takes a temporary directory still reads this repository's tree through a command's default root without naming `ROOT`; phase 1's enumeration reads every case for the ways a case names the root, and every case that takes no temporary directory and runs a command, and no reading of a case's text rules the rest out short of running it (`trail/phases/phase-1.md`, the enumeration) | a measurement no record asks for: the answer would decide whether a tree-wide case is still left in a file a narrow run skips; no broad-gate failure of that kind, open issue or other work item's rule is on record, and nothing is opened |
| closed whether a test file outside `tests/text/` and `tests/behaviour/` reads this repository's own `.claude-plugin/plugin.json` beyond the eight `trail/phases/phase-2.md` lists; round 2's fix pass walked up from the eight shipped readers a search for the manifest's spellings found, and a shipped reader that builds the path some other way, or a test file that reaches a reader under a name no search spelled, is the part it did not reach (`trail/phases/phase-2.md` *Scope item 7*) | a measurement no record asks for: the answer would decide whether a version move can fail a case no narrow run reaches; no such failure, open issue or other work item's rule is on record, and nothing is opened |

## Not done

`.test_durations` keeps the fourteen moved cases' stored prices under their
old ids, 36.3 s of the file's 1,599.8 s. `frame/plan.md` *Operational
impact* leaves them for the next release refresh, and #1444 makes the rule
that no work item commits that file, so phase 1 left it.
