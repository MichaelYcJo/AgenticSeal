# Phase 2: 1794465691-the-orchestrator-polls-ci-by-hand

## What this phase found

**The frame holds against the tree at `035bd8ad0`.** The two paragraphs
`frame/design.md` *Grounding* G3 names stood at
`skills/code-review/orchestration.md:266-313`, and the pin at
`tests/text/test_the_rules_have_one_owner.py:318`, with the strings
*Removes* row 4 lists (read). G4's search, run again outside `seal/threads/`
for `pr checks`, `headRefOid`, `state,mergeable`, `pr-wait`, `pr_wait`, and
case-blind for `wait on CI`, `waits on CI`, `two minutes`, `MERGEABLE`,
`CONFLICTING` and `checks reported`, found the wait in those two places
alone. Its other hits were phase 1's registration files and `pr_wait.py`'s
own tests (executed).

**The pin was seen red before the paragraph changed.** With the new strings
in the case and the old paragraphs in place, the case failed on its first
string, `` `seal pr-wait <N> --once` `` (executed). After the paragraph was
rewritten, `bin/test -q tests/text/test_the_rules_have_one_owner.py` passed
all 25 cases (executed).

**Each pinned string was seen red with the paragraph's copy of it broken.**
`seal mutate skills/code-review/orchestration.md` ran one mutant per string
at `06ac413c2`, each against
`bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -x -k test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge`.
All ten read `red`, and each run's failing line named the string the
mutant broke (executed):

| String broken in the paragraph | How it was broken | The failing line names |
|---|---|---|
| `` `seal pr-wait <N> --once` `` | deleted | `` '`seal pr-wait <N> --once`' `` |
| `` `seal pr-wait <N>` `` | deleted | `` '`seal pr-wait <N>`' `` |
| `\| 0 \|`, `\| 1 \|`, `\| 2 \|`, `\| 3 \|`, one mutant each | the exit code taken out of its row | that row's string |
| `` \| 4 \| `state` is `MERGED` \| `` | `MERGED` written as plain `merged` | that row's string |
| `` \| 5 \| `state` is `CLOSED` \| `` | `CLOSED` written as plain `closed` | that row's string |
| `` \| 6 \| `state` is `OPEN` and `mergeable` is `CONFLICTING` \| `` | `CONFLICTING` written as plain `conflicting` | that row's string |
| `` `--no-merges` `` | deleted | `` '`--no-merges`' `` |

**Five decisions the frame left to the build.**

- **The paragraph names each command once.** After the opening sentence it
  calls them "the wait" and "the read before a push". `seal mutate` writes a
  break only where its text occurs exactly once, and a string that occurs
  twice cannot be shown red by deleting one copy, which `frame/plan.md`
  *Phases* row 2 asks for. Judged against `skills/verify/seal-mutate.md` and
  `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만
  읽히게 쓴다*, which asks that a value stand in one place.
- **The pin holds exits 4 to 6 with their states, and exits 0 to 3 by their
  rows.** A row string such as `` | 4 | `state` is `MERGED` | `` goes red
  where the code and the state are swapped, which the bare state strings
  the pin held before did not. Exits 0 to 3 have no one-word outcome to hold
  beside the code, so the pin holds that each row exists, and the act in
  each row is the proofer's to read. Judged against *Scope* item 5 and
  contract rule 14.
- **The paragraph does not give the two-minute value.** It says the
  command's one limit is on the start, and that once a check is listed the
  wait has no limit, which *Scope* item 4 asks for. *Removes* row 3 puts the
  limit in `pr_wait.py`'s code and docstring, and a value written in two
  places is changed in one. Judged against `skills/core/SKILL.md` *The rule
  a mechanism is kept against*: a fact has one source.
- **The reasons behind the states left with the two paragraphs.** The
  sentences on why a push after a merge reaches no pull request, why
  `CONFLICTING` runs no `pull_request` CI, and why `UNKNOWN` is read again
  are gone. *Scope* item 4 keeps only the commands, the table, the reason the
  wait reads every workflow's checks, and the unlimited wait after the
  start. The command reads `UNKNOWN` again by itself, and the pin's
  docstring keeps the history of the read under #945 and #1200. Judged
  against *Scope* item 4 and *Removes* row 1.
- **The changelog fragment holds the command, its exit codes and the two
  results `--watch` passes, and the process row holds the orchestrator's
  new step.** *Scope* item 6 names an `### Added` entry and one process
  row. The release note lifts the process row into its own table, so the
  fragment's prose does not restate the step. The fragment names no version,
  since #1516 carries the move.

**A removal the frame's *Removes* did not name.** Row 4 lists the pin's
strings for the poll and the watch. The pin also dropped
`` `gh pr view <N> --json state,mergeable` ``, the read that row 1 removes
from the paragraph, and its bare `` `MERGED` ``, `` `CLOSED` `` and
`` `CONFLICTING` ``, which now stand inside the rows for exits 4 to 6.

**Contract rule 12's census of the statements this phase changes.** The
rule this phase rewrites is the orchestrator's step after a push. The
search above for its commands and its words is whole for the commands'
spellings and a sample for a wait described in prose without a command, as
G4 says. Two places state the rule, the paragraph and the pin, and both
changed. `pr_wait.py`'s docstring cites the section by its heading, which
did not change. The `check:` lines that name
`tests/text/test_the_rules_have_one_owner.py`, in
`docs/forms/the-round-record.md`, `docs/running/the-run.md`,
`skills/code-review/SKILL.md` and `skills/implement/fold-and-reframe.md`,
cite the file for other rules (read).
