# Phase 1: 1793599986-a-stopped-head-run-does-not-seal

## What this phase found

### The frame, checked before the build

The frame holds for phase 1, with one sentence corrected below. I opened
every coordinate `frame/plan.md` *Technical context* gives at `cedf93b7`,
and each stood as stated (read). `Check.failed` is at
`broad_gate.py:1200-1202`, `RunRecord` at `:1628`, `RAN_TO_ITS_END` at
`:1731` with its comment above it, and `read_record` at `:1739`. The
`unended` count is at `:1805-1809`. `gate` starts at `:2895`, and its
failures loop opens at `:3014` with `failures = []`. `failure_lines` starts at `:2699` and appends
`UNENDED_HERE` at `:2746-2747`. `UNENDED_HERE` is at `:2785`. In
`tests/skills/test_broad_gate.py`, `_repo_template` is at `:2304`,
`Test_failure_lines` at `:2208` and its exit-1 case at `:2248`.
`tests/conftest.py#repo` is at `:799`. Rule 3's pin in
`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py` is at
`:526-528`. The handoff says the tree equals the 0.28.0 release. For
the gate, `git diff --stat 40e6c23e cedf93b7` lists only the four
files of this work item (executed). So "seen red at 40e6c23e" and
"seen red at `cedf93b7`" are the same measurement for
`broad_gate.py`.

The corrected sentence is in `frame/design.md` *Scope* item 1: "The base
is not run, because the record holds no failing file to compare". That is
true where no test failed before the stop, which is the case in G1 and G2.
A test that fails before a later test calls `pytest.exit("...",
returncode=0)` leaves the row at exit 0 with a failing file in the record.
The loop's existing path then runs `compare_at_base` for that file, as it
does for any failing suite (read: `gate`'s failures loop, where `files`
comes from `head.failing`). I left that path as it is, because the base
words for a failing file mean the same thing whatever the exit was. The
loop's comment says it: the base runs only where a test failed before the
stop. No case covers this combination, as `gaps.md` *Not done* records.

### Decision: the suite's verdict is decided in the loop, and `Check` stays as it is

`frame/design.md` *Data & interfaces* left this to the build. The loop in
`gate` now skips a check only where `not check.failed and not (name ==
SUITE and head.unended)`. `Check.failed` stays `code != 0`. Grounds: the
chain and mode arms have no record, so their exit is the only thing to
read (`frame/plan.md` *Alternatives considered*, row F). A `Check` that
carried the record's verdict would give every arm a field that only one
arm fills. The loop already reads `head` for the suite's files and counts,
so the stop is read in the same place. Judged against `frame/design.md`
*Data & interfaces* and `skills/core/SKILL.md` *The rule a mechanism is
kept against* ("Less text means nothing said twice").

### Decision: the new line comes directly after the check's first lines

*Scope* item 2 places the line "after `exit 0` and the first lines, ahead
of `UNENDED_HERE`". The verdict heading and the file list can also fall
between those two, where a test failed before the stop. I put the line
before them, directly under the first lines. Grounds: it says why an exit
of 0 failed, so it belongs beside the exit and is read before the file
list. Judged against `frame/design.md` *Scope* item 2. The constant is
`broad_gate.py#STOPPED_AT_EXIT_0`. Its text is pinned verbatim in
`tests/skills/test_broad_gate.py` (contract rule 14), the same way that
module pins `NO_RECORD_HERE`.

### Decision: the line's condition tests no check name

The first form of the condition tested `check.name == SUITE` as well as
the exit and the record. `seal mutate` showed that mutant survive (below).
No run reaches `failure_lines` with a record for any check but the suite:
the function's docstring says the record is None for every other check,
and the loop hands `head` only to the suite. A case for a non-suite check
holding a record would pin a state `gate` cannot produce. So commit
`944c1463` removed the name test, and a comment states why it is not
needed. Judged against `skills/core/SKILL.md` *The rule a mechanism is
kept against*.

### Every sentence that states when the gate passes, listed at this phase's HEAD

Method: `git grep` on `BROAD GATE PASSED`, `unended`, `UNENDED_HERE` and
`part-way` outside `tests/` and `seal/threads/` at `56e81a6c`. I widened it
with one more search on `gate passe`, `run that passes`, `passing run`,
and `exit 0` near `pass` or `seal`. This is a sample by wording (contract
rule 12). A sentence that says when the gate passes in other words is
outside it.

Rewritten in place, as `frame/design.md` *Scope* item 3 lists:
`broad_gate.py`'s module docstring, the paragraph that says what a run
that passes and a run that fails print; the `record.unended` paragraph of
`failure_lines`' docstring; the comment in `gate`'s failures loop;
`templates/setup/config.md` *The criterion for choosing a value* rule 3,
with its pin; and the `On the broad run's exit 1 spawn nothing` paragraph
of `skills/code-review/orchestration.md`.

One departure from the list: I also rewrote the comment above `head =
read_record(...)` in `gate`. It listed what the failure loop takes from
the record, and the loop now takes the stop count from it as well.

Found and left as they stand, each still true:

- `skills/verify/orchestration.md:127` and `:140`. The first is about the
  base word `new?` for a base session that stopped. The second says that
  the failure form counts a session at `HEAD` that stopped part-way. The
  failure form still counts it, so both still hold.
- `docs/the-broad-gate.md:26-27`, `skills/verify/SKILL.md:275`,
  `skills/code-review/orchestration.md:450` and `:464`. Each names the two
  heads and says the run judges nothing. That is still true. Under
  `docs/`, the change is written by the settle from `frame/design.md`
  *Rule changes*, and this pull request does not edit it.
- `.github/scripts/release_seal.py:247-266`, the release seal's own
  refusal, which `frame/design.md` *Scope* Out keeps.
- `skills/implement/scripts/seal.py:1321` and `README.md:534`, which are
  about a copy that stops part-way, not the gate.

### Seen red (contract rule 15)

I wrote the three new cases before the code, and ran them against the
gate at `cedf93b7` (executed, `bin/test tests/skills/test_broad_gate.py
-q -p no:xdist -k ...`). Result: 3 failed, 1 passed.

- `Test_gate::test_refuses_a_suite_a_test_stopped_at_exit_0`, in both
  parametrizations, `pytest-exit-0` and `os-exit-0`, failed on its first
  assertion, `assert 0 == 1`. The gate returned 0, and the printed panel
  read `suite   + 1 passed`. This is G1 and G2 of `frame/design.md`
  reproduced inside the fixture repository.
- `Test_failure_lines::test_accepts_a_suite_that_exited_0_and_says_why_it_failed`
  failed on the list comparison, because the new line was missing. It
  compares against the test module's own copy of the text, so it did not
  fail on a missing attribute.
- The case at `:2248` passed. It gained `assert STOPPED_AT_EXIT_0 not in
  lines`, which holds at exit 1 both before and after the change. The
  mutants below show that assertion going red.

The assertion added in commit `6382f67c`, that an exit-0 suite whose record
counts no stopped session gets no line, I saw red only through a mutant:
mutant 3 of the second batch, and mutant 3 of the third batch below.

### `seal mutate`, and what each red rests on

The worktree's `bin/seal mutate` ran each batch, with each mutant's cases
after `-k` under `bin/test ... -q -p no:xdist` (executed). The handoff
says the installed copy reads a mutant that does not compile as red
(issue #898). I checked every mutant text separately with a scratch script
under `883-build/` in the scratchpad. The script compiles the mutated
source in memory and finds the function that holds the mutation site
(executed). Every mutant compiles, and every site is inside the body of
`gate` or `failure_lines`. So each mutated module imports exactly as the
unmutated one does, and no red below comes from a compile or import
failure.

- First batch, at `56e81a6c`, over `gate`'s loop, against the two
  stop cases, the green recorded run, `test_the_fixture_branch_passes`
  and the preflight case. Three mutants, three red. (1) The condition cut
  back to `if not check.failed:` turns the two stop cases red. (2) `not
  (name == SUITE)` fails every suite and turns the green runs red. (3)
  `(head.unended)` without the name test reads `head` for every arm. The
  preflight case goes red there, because a preflight leaves `head` at
  None (read: the order of `gate`).
- Second batch, at `6382f67c`, over `failure_lines`, against
  `Test_failure_lines` and the two stop cases. Four mutants, three red, one
  SURVIVED. The survivor removed `check.name == SUITE`. The decision
  above removed that test in `944c1463`.
- Third batch, at `944c1463`, over the condition as it now stands. The
  append replaced by `pass`, `check.code == 0` removed, and
  `record.unended` removed: three mutants, three red, none survived.

Each run restored the file from `seal mutate`'s held bytes. `git status
--short` was empty after each batch (executed).

### The phase-boundary run

One command through `bin/test` (contract rule 2) ran 77 modules (executed).
They are every test module that names `broad_gate`,
`templates/setup/config.md`, a `config.md` or an `orchestration.md`, plus
every module that globs `skills/`, `templates/` or `*.md` and `*.py` files.
The first run, before this record was written, gave 1 failed, 3811
passed, 12 skipped. The failure was
`tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
because `gaps.md` was not written yet. With this record, `gaps.md`,
`changelog.md` and the plan's Status cell written, the same command gave
3812 passed and 12 skipped (executed). A second command ran the 20
modules outside that list that read `seal/threads`, a `changelog.md`, a
`gaps.md` or a phase record: 1215 passed (executed).

### What the next reader needs

`frame/questions.md` Q1 is still open, and only the orchestrator's broad
run can answer it. With this branch, the gate fails this repository's own
broad run where any pytest session `bin/test -q` starts stops part-way.
The new arm reads `head.unended`, and that count is 0 for a run whose
every session wrote an `end` line with `"stopped": []` and an exit in
`RAN_TO_ITS_END`.
