# Review round 4: 1793273065-the-core-reaches-no-users-repository

target: ab614222, fixes 526504cd..ab614222

## Findings

This round opens no finding.

## Confirmations

confirms: none
The rename makes `Test_imports_of` hold the pair the test layout requires,
and it changes nothing else. The orchestrator claimed that `seal layout
--check tests` refused the class at `526504cd` and reads 0 refused after
`ab614222`. This round re-ran the layout reader's `check` on
`tests/skills/test_payload_meter.py` as it stands at each commit (executed,
*Probes*). At `526504cd` it refuses `class Test_imports_of has no
test_accepts_ case` and `has no test_refuses_ case`. At `ab614222` it
refuses nothing. `bin/seal layout --check tests` at HEAD exits 0 with "150
files read, 0 refused" (executed, *Probes*). Its `report:` lines name
functions of `payload_meter.py` with no class, such as `composition`. A
report is not a refusal, and this round did not judge those lines. The diff
is four `def` lines in `tests/skills/test_payload_meter.py:1001`, `:1018`,
`:1040` and `:1056`. No body, docstring or fixture changed (read `git diff
526504cd..ab614222`). Under `skills/verify/SKILL.md` *The narrow command
still has to be able to fail*, as `skills/code-review/SKILL.md` cites it, a
rename owes no new case and no mutation run. The rename adds no test, so
`seal layout --pairs` has no new case to read against its group.
`tests/skills/test_payload_meter.py` and `tests/skills/test_test_layout.py`
pass 118 at HEAD (executed, *Probes*). That is the count the orchestrator
reported.

confirms: none
Each new name says what its case asserts. The layout gives `test_accepts_`
to good input and `test_refuses_` to bad input (read `CONTRIBUTING.md`
*The test layout*, `skills/verify/scripts/test_layout.py:13-14`).

`test_refuses_an_import_past_the_fourth_hop` (`:1056-1070`) writes a chain
that runs from the top file through `h1.md` to `h5.md`, and `h5.md` imports
an `h6.md` that does not exist. The first assertion requires that the last
hop of each returned chain is exactly `h1.md` to `h4.md`. So `h5.md`, the
import past the fourth hop, has no row of any kind, not even a `missing`
row, and neither has `h6.md` past it. The second assertion pins the fourth
entry's whole chain. `payload_meter.py#imports_of` returns `[]` once
`depth` reaches 0 (`skills/verify/scripts/payload_meter.py:322-323`, read),
so the fifth file is never opened. "Refuses" fits: the docs cap the depth at
four hops, and a fifth hop is input the function declines to follow. The
case also asserts the fourth hop is kept, so it pins both sides of the
boundary. That makes it stricter than its name, not looser. Carried and not
re-run: phase 3's record says the "five hops" mutant of `seal mutate` was
red against this case (`trail/phases/phase-3.md:79-85`). The rename does
not change what the case kills.

The three `accepts` names keep what each case asserts.
`test_accepts_a_relative_path_against_the_importing_file` (`:1018`) asserts
`y.md` resolves to `inner/y.md`, with decoys beside the top file and in the
working directory. `test_accepts_a_symlink_as_its_target` (`:1040`) asserts
the row is the target's real path and bytes.
`test_accepts_a_tilde_path_as_the_home_it_was_given` (`:1001`) asserts that
`~/notes/a.md` resolves under the home passed to `imports_of`, with `HOME`
and `USERPROFILE` pointed elsewhere. Read beside the symlink case's "as its
target", "as the home it was given" could be read as taking the whole tilde
path to be the home, where the case takes `~` to be the home. This round
judges that no finding. The name keeps the claim that matters, the given
home and not the process's. The docstring beneath it states the meaning in
full. Nothing reads the name except the layout's prefix test.

confirms: none
`trail/phases/phase-3.md:67-72` still names the four cases by their old
names, and a `git grep` on the four old names finds them there and nowhere
else in the tree (executed, *Probes*). This round judges that no finding.
The record names its commit, `a7329570`, at `trail/phases/phase-3.md:6`,
and the names it gives are the names at that commit. Rounds 2 and 3 kept
phase records as measurements of their own commit on the same grounds. A
reader who follows a phase-3 name to HEAD finds the class by its name,
`Test_imports_of`, which did not change.

confirms: none
Rounds 1 to 3 read `Test_imports_of`, and none of them ran `seal layout`. A
`grep -n layout` over the three records and the phase records finds only
`docs/the-record-layout.md` and a quoted section name (executed, *Probes*).
The layout reader refuses this class of defect, a class missing its pair,
in one cheap command. The broad run caught it instead. Carried rather than
re-established: round 3's confirmations of round-2#1 and round-2#2. Round 3
closed nothing `fixed` or `rejected`, so this round owes it no `confirms:`
reference.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `ab614222` | the tree | the orchestrator, through `seal gate` |
| `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py::test_the_durations_file_prices_the_suite`, which the broad run at `526504cd` failed with 5.2% of cases unpriced, and the `.test_durations` refresh from `gh run` 40895243786 meant to repair it. Neither is in this round's diff | `.test_durations` | the orchestrator, through `seal gate` after the refresh |
| The `report:` lines `bin/seal layout --check tests` prints for `payload_meter.py` functions with no class, such as `composition` and `render`. They are reports, not refusals, and outside this fix diff | `tests/skills/test_payload_meter.py` | the orchestrator |
| Whether the pull request body gives the core's exact bytes as measured at the broad gate's HEAD. This is carried from round 3, and the body is not yet written | the pull request body | the orchestrator when it writes the body; the sealer when it reads it |
| Round 1's *Not judged* rows on the symlinked `~/.claude/CLAUDE.md`, `/agentic:update` under `CLAUDE_CONFIG_DIR`, the three-fix stop for an orchestrating session, and Q2. They are carried, outside this fix diff, and were not re-examined | `seal/threads/1793273065-the-core-reaches-no-users-repository/trail/rounds/round-1.md` | as round 1 names each: the orchestrator, the owner at #1148 |

## Probes

| Command | Result |
|---|---|
| `python3 -I -c` importing `skills/verify/scripts/test_layout.py` and calling `check({rel: src}, tracked, read)` on `git show <rev>:tests/skills/test_payload_meter.py` for `526504cd` and `ab614222` | `526504cd`: two refusals, `class Test_imports_of has no test_accepts_ case` and `has no test_refuses_ case`. `ab614222`: none |
| `bin/seal layout --check tests` | exit 0, "150 files read, 0 refused, 87 declare no TARGET", with `report:` lines only |
| `bin/test -q tests/skills/test_payload_meter.py tests/skills/test_test_layout.py` | exit 0, 118 passed |
| `git grep -n` on the four old case names and `Test_imports_of` | the old names at `trail/phases/phase-3.md:67-72` only; `Test_imports_of` at `tests/skills/test_payload_meter.py:996` |
| `grep -n layout` over `trail/rounds/round-*.md` and `trail/phases/*.md` | `round-2.md:183` (`docs/the-record-layout.md`) and `phase-4.md:12` (the same document); no run of `seal layout` |
