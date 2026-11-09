# Phase 1: 1794187229-the-body-carries-the-seal-mark

## What this phase found

**The frame holds for this phase, with three line numbers off.** `d949a652`
differs from `857a7356`, the commit the frame read, only by the three frame
files (executed: `git log --oneline 857a7356..d949a652`). Three of the line
numbers that `frame/plan.md` *Technical context* gives are off by a few
lines in `skills/code-review/scripts/pr_body.py` at both commits (read).
`main` stands at line 832, not 836. `_check` stands at line 790, not 785.
The load of `chain_check.py` stands at line 140, not 141. Every unit stood
where the frame placed it otherwise.

**Decision: one refusal per run, naming every line of it, joined by
`, then `.** A body lacking the mark and the blank line under it is refused
on one line, `lacks ``, a fixed line, then `<img ...>`, a fixed line`. The
design's S1 asks for "one refusal at the body's line, reading `lacks` and
the mark line, and no other refusal". One cause per line of the run would
give two refusals at the same body line. A one-line run reads as it did
before, so every existing case's message stands unchanged. Judged against
`frame/design.md` *Scope* item 2 and S1.

**Decision: the part above the heading names its runs the same way.**
`_first_part` read the differ's opcodes by the same first-line rule as
`_check`, so a body lacking two lines of `pr.md` named the first alone. The
cause is the same, so the fix covers both functions (contract rule 12, built
from what produces the defect: each `get_opcodes` loop in the file, and
there are two). Judged against `frame/design.md` *Scope* item 2, which names
the refusal for a run without limiting it to the copy.

**Decision: `compared` returns `(note, causes)` and raises nothing.** The
pull request's check needs the sentence `seal_mark` says beside the causes,
and a `Refused` raised out of the comparison would drop it. The function
takes the work item's directory, the body's text or None, the repository
root and an optional manifest. It composes as `main` did and returns the
causes `Refused` carries. Judged against `frame/design.md` *Data &
interfaces*, "returning the causes `_check` raises as `Refused`".

**Departure: `main --check` reads the body file before it composes.** Where
the body file cannot be read and a record is refused too, the refusal now
names the body file and not the record. Before, the record's refusal came
first. Only that double fault changes order, and no case pins it (executed:
`tests/skills/test_pr_body.py` green unchanged).

**Seen red.** The four new parametrized rows were run against `_check` and
`_first_part` as they stood at `d949a652`, before the code changed
(executed). Each failed on its own message line. The mark case read
`refused: pr-body.md:5: lacks ``, a fixed line` and stopped there, without
the mark. That is G12's refusal, reproduced in a fixture. The copy's
two-line case read `reads `A line.`, which the records do not give`. The
first part's two cases read `lacks ``, which pr.md gives` and the first
added line alone.

**Mutations, all red** (executed, `bin/seal mutate` against `7252125d`, each
over the cases it names):

- `_run` returning the run's first line alone: red over the seven cases of
  the two run tests.
- `_check`'s insert run cut to `below[j1 : j1 + 1]`: red.
- `_check`'s delete run cut to `said[i1 : i1 + 1]`: red.
- `_first_part`'s delete run cut to its first line: red.
- `_first_part`'s insert run cut to its first line: red.
- `compared` returning no causes from a `Refused`: red over `Test_main`.

The working tree was clean after every run (executed: `git status
--short`).

**No unit was renamed or moved,** so no census is owed. The phase removed
nothing.

**The phase-boundary run.** One `bin/test` command ran
`tests/skills/test_pr_body.py`, `tests/evals/test_rule_cases.py` (it loads
`pr_body.py`), `tests/text` and `tests/behaviour`. Its first run failed one
case alone, `test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
because this record's `gaps.md` was not yet written (executed). With
`gaps.md` written, the same command exited 0, with 1886 passed and 8
skipped (executed).
