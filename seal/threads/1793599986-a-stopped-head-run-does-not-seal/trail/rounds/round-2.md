# Review round 2: 1793599986-a-stopped-head-run-does-not-seal

```seal
target: f66eca7f, fixes 440652f5..f66eca7f
```

This is the verifying round over the fix pass of round 1. It read the diff
440652f5..f66eca7f in a `git clone --no-local` of the branch worktree at
f66eca7f, with `origin/release/v0.28.1` (40e6c23e) as the base. The diff has
five commits: cb60fc2e (all three findings), d43beea9 (two comments), 8ce09fc2
(a `gaps.md` row), 14f45140 (the close blocks) and f66eca7f (the
orchestrator's fold into the frame). `seal/parity.md` is not declared, so
the round block carries no `original:` line. Every mutant this round planted
ran through the `seal` of the #898 worktree
(`fix/898-a-mutant-that-does-not-compile-reads-as-caught/bin/seal mutate`),
which refuses a mutant that does not compile before it runs any case.

Facts carried from round 1, not re-established: a conftest's
`pytest_configure` runs ahead of the recorder module's, since a conftest is
registered after a `-p` plugin, and the single-runner gate run with such a
stop at exit 0 passes and writes `trail/gate.md` (round 1's second probe).
The recorder's hooks are at `skills/verify/scripts/pytest_record/agentic_pytest_record.py:274`
and `:395`. Every verdict below was reached this round.

## Findings

### 1. The new limit sentence says a stop before the recorder's first line makes the run read as one that started no pytest and judged on its exit alone, and a row that runs pytest twice is judged on the other session's record and passes

```seal
severity: should
location: `templates/setup/config.md:366`, `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:535-539`, `skills/verify/scripts/broad_gate.py:1731-1733`, `seal/threads/1793599986-a-stopped-head-run-does-not-seal/changelog.md:3`, `seal/threads/1793599986-a-stopped-head-run-does-not-seal/frame/design.md:76-79`
evidence: executed `bin/test tests/skills/test_tmp_883_r2_probe.py -q -p no:xdist --tb=short -s`
regression: round-1#2
```

Why it matters: the unit is the sentence cb60fc2e added to rule 3 of
`templates/setup/config.md` with its pin, and wrote the same way into the
changelog, the `RAN_TO_ITS_END` comment (d43beea9) and the folded `to:`
text. The frame (*Scope* Out, `frame/design.md:37`) says such a stop "leaves
no record"; the fix added that the run therefore "reads as one that started
no pytest and is judged on its exit alone"; that clause came from round 1's
own paste-ready text ("so the run reads as one that started no pytest and
passes on its exit"), which the fix pass carried into five places.

The clause holds only for a row that runs one pytest. The stop leaves no
record of its own session. Other pytest sessions in the same row still
leave theirs, and `read_record` reads every keyed file under `records/`
(`skills/verify/scripts/broad_gate.py:1746-1767`; its docstring already
names the case "where a row runs pytest twice"). Rule 3 names that shape
too: "where one runner loaded it and another did not".

The probe gave the fixture repository of `tests/skills/test_broad_gate.py`
the row `python -m pytest -q -p no:cacheprovider tests && python -m pytest
-q -p no:cacheprovider other`. `other/conftest.py` calls
`pytest.exit('at configure', returncode=0)` in `pytest_configure`, and
`other/test_never.py` fails. The gate returned 0. It printed
`BROAD GATE PASSED` with `suite   + 1 passed`, the first runner's count, and
wrote `trail/gate.md`. `records/` held one file. `suite.txt` holds
`Exit: at configure`. So the run did not read as one that started no
pytest, and it was not judged on its exit alone: it read as a run whose one
session ran to its end, and that record's counts are what the panel showed.

The outcome the limit warns of is the same: the stop passes. The sentence is
still a wrong statement of how the gate reads the run, in a rule text the
settle copies into `docs/the-broad-gate.md`. A reader who meets a
two-runner row is told the gate saw no pytest, and it did.

The fix rewrites the consequence clause per session in each place, and
moves the pin with it.

```text
templates/setup/config.md rule 3, and its pin at
tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:536-539:
  A stop raised before the recorder writes a session's first line, such as
  a `pytest.exit()` in a conftest's `pytest_configure`, leaves no record of
  that session, so the gate reads the run as though that pytest never
  started and judges it on its exit and on the records the row's other
  sessions left.

changelog.md, the same sentence:
  A stop raised before the recorder writes a session's first line, such as
  a `pytest.exit()` in a conftest's `pytest_configure`, leaves no record of
  that session, so the gate reads the run as though that pytest never
  started and judges it on its exit and on the records the row's other
  sessions left.

frame/design.md *Rule changes*, the end of the `to:` text (lines 76-79),
for the orchestrator to fold:
    end. A stop raised before the recorder writes a session's first line,
    such as a `pytest.exit()` in a conftest's `pytest_configure`, leaves no
    record of that session, so the gate reads the run as though that pytest
    never started and judges it on its exit and on the records the row's
    other sessions left.
```

```python
# skills/verify/scripts/broad_gate.py:1731-1733, the RAN_TO_ITS_END comment
# end. A stop raised before the recorder writes its `session` line, such as a
# `pytest.exit()` in a conftest's `pytest_configure`, leaves no record of that
# session, and the gate reads the run as though that pytest never started
# (#883 round 1). One
```

```seal
verdict: fixed 3de5c6c8
answer: The finding holds. `read_record` reads every keyed file under `records/` (`broad_gate.py:1746-1767`), so a stop before the recorder's `session` line removes only that session's record. The gate then judges the run on the row's exit and on the records the other sessions left. "Started no pytest" is true only where no other session left a record. I checked the record's replacement against that and wrote the consequence by what the gate reads per session: the stop "leaves no record of that session, so the gate reads the run as though that session never started: it judges the run on the row's exit and on the records the row's other sessions left, where there are any". That sentence is in `templates/setup/config.md` rule 3, and its pin in `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py` moved with it. The `RAN_TO_ITS_END` comment in `broad_gate.py` now says the same in short form. I removed the limit sentences from `changelog.md` instead of rewording them: the changelog now names the two kinds and points to rule 3, so the limit has one home. #898's `seal mutate` over `templates/setup/config.md` put the old clause "it judges the run on its exit alone." back in place of the new one; the pin went red (executed). `git grep` on "started no pytest", "exit alone" and "judged on its exit" now finds the old clause only in `frame/design.md:78-79` and the round records; every other hit is the separate list of reasons a run left no record. The frame sentence at `frame/design.md:72-79` is finding 2's to fold, and its replacement there replaces this finding's change to the `to:`.
```

### 2. The folded `to:` repeats the limit sentence rule 3 of `templates/setup/config.md` keeps, so after the settle one fact stands in two rule documents

```seal
severity: should
location: `seal/threads/1793599986-a-stopped-head-run-does-not-seal/frame/design.md:72-79`, `templates/setup/config.md:366`, `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:535-539`
evidence: executed `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.28.1 --root <the branch worktree> --worktree`, `python -B -c over rule_changes.parse and rule_changes.passages: the to text's 15-word runs found in templates/setup/config.md, at 7768896c and at f66eca7f`
regression: round-1#2
```

Why it matters: the unit is the limit sentence, which cb60fc2e wrote into
rule 3 of `templates/setup/config.md` and f66eca7f folded into the `to:`.
The frame's `## Rule changes` puts the rule into `docs/the-broad-gate.md`
at the settle, and *Scope* 3 gives rule 3 only "that a run whose row exited
0 fails where one did"; the fix wrote the limit into both; the copy came
from the fix pass adding to rule 3 the sentence round 1 asked for in the
`to:` and the changelog alone.

The chain check's run over the branch worktree prints this notice:

```text
seal/threads/1793599986-a-stopped-head-run-does-not-seal/frame/design.md:59  this `to` repeats a passage of `templates/setup/config.md`: 10 of its runs of 15 words stand there, one of them "a stop raised before the recorder writes a session's first line, such as a pytest.exit()"
```

The same count, run with `rule_changes.passages` over the `to:` text and
`templates/setup/config.md`, is 0 at 7768896c and 10 at f66eca7f
(executed). All ten runs lie in the one sentence that finding 1 rewords.
After the settle, `docs/the-broad-gate.md` and `templates/setup/config.md`
both state that limit, and the next change to it has two places to keep in
step. `skills/core/SKILL.md` *The rule a mechanism is kept against* gives a
fact one source.

The other limit, the `pytest_sessionfinish` stop, stands in neither
document today. So one way gives both limits one home: rule 3, beside the
recorder's other named limit, pinned by the test that already pins rule 3.
The `to:` then names the two kinds and points there. Where the fix pass
takes this finding, its `to:` text replaces finding 1's change to the
`to:`. Finding 1's rewording still applies to rule 3, its pin, the
changelog and the `RAN_TO_ITS_END` comment. The other way, removing the
sentence from rule 3, would leave rule 3 pointing at a section that holds
nothing until the settle.

```text
frame/design.md *Rule changes*, the end of the `to:` text (lines 72-79),
for the orchestrator to fold:
    says that the row exited 0 and how many sessions stopped. Two kinds of
    stop stay out of the record's reach: a `pytest.exit()` raised by a
    `pytest_sessionfinish` hook that runs after the recorder's, and a stop
    raised before the recorder writes a session's first line.
    `templates/setup/config.md` *The criterion for choosing a value*, rule
    3, says how the gate reads a run with each.

templates/setup/config.md rule 3, after the sentence finding 1 rewords,
and the same sentence added to the pin list at
tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:535-539:
  A `pytest.exit()` raised by a `pytest_sessionfinish` hook that runs after
  the recorder's comes after the session's `end` line, so that session
  reads as one that ran to its end.
```

```seal
verdict: fixed 3de5c6c8
answer: The finding holds. I took the first way: both limits are kept in `templates/setup/config.md` rule 3 alone, and the `to:` names them and points there. Rule 3 now opens the limits with "Two stops are out of the record's reach." The `pytest_sessionfinish` sentence follows, and I read it against pytest 9.2.0's `wrap_session` (`_pytest/main.py:366-373`, read). That code catches an `Exit` raised in `pytest_sessionfinish` and sets the session's exit status to its code, so the sentence ends "and its pytest exits with the code that hook chose", not only "reads as one that ran to its end". Finding 1's sentence comes after it. Both are in the rule 3 pin list. #898's `seal mutate` deleted the opening sentence in one mutant and the new exit clause in another; both went red against the pin (executed). I also wrote the exit clause into the `RAN_TO_ITS_END` comment. The orchestrator folds `frame/design.md:72-79`, the end of the `to:` text. Replace from "Two kinds of stop stay out of the record's reach." through "and is judged on its exit alone." with this text, the record's own wording, which I checked against the gate: "Two kinds of stop stay out of the record's reach: a `pytest.exit()` raised by a `pytest_sessionfinish` hook that runs after the recorder's, and a stop raised before the recorder writes a session's first line. `templates/setup/config.md` *The criterion for choosing a value*, rule 3, says how the gate reads a run with each." I measured it with `rule_changes.copies` against rule 3 as it stands at 3de5c6c8: it shares no run of 15 words (executed). The `to:` as folded at f66eca7f shares 17 runs with the same rule 3 (executed), which shows the measurement can find a copy. At `frame/design.md:37`, *Scope* Out, I propose replacing the last sentence, "Both stay the limits `RAN_TO_ITS_END`'s comment and the recorder's docstring name.", with "Both stay limits, stated in `templates/setup/config.md` rule 3 and named in `RAN_TO_ITS_END`'s comment and the recorder's docstring." *Scope* item 2 is unchanged.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the fix pass claimed one wording in every place the old clause
stood. `STOPPED_AT_EXIT_0` at `skills/verify/scripts/broad_gate.py:2814-2820`
and its verbatim pin at `tests/skills/test_broad_gate.py:2202-2208` now say
that a stop such as `pytest.exit()` or `os._exit()` chooses the exit code,
so an exit of 0 says neither that every collected test ran nor that nothing
failed. The module docstring (`broad_gate.py:84-88`), the `failure_lines`
docstring (`:2722-2728`), rule 3 with its pin
(`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:530-534`),
the changelog, and `frame/design.md:27` and `:59-63` say the same (read). The
line is true where it is said: it is said at exit 0 alone, and no stop that
lets pytest choose the code exits 0 (`-x` and `--maxfail` give 1, an
interrupt 2, per the `RAN_TO_ITS_END` comment at `broad_gate.py:1700-1722`).
A `git grep` for the old clause, "says only that nothing", finds it only in
round 1's own record (executed). Putting
the old text back into the constant went red against the new case alone, and
putting the old clause back into rule 3 went red against its pin (executed,
the #898 `seal mutate`).

```seal
confirms: round-1#2
```
What holds: the limit is now written by its cause, a stop raised before the
recorder writes a session's first line, and no longer as one instance. That
covers the `tryfirst` `pytest_sessionstart` instance round 1 read and did not
run, without claiming it was measured. Deleting the new rule 3 sentence went
red against its pin (executed). Finding 1 of this round is a separate defect
in the consequence clause of the same sentence.

The fix pass chose the limit sentence over the recorder change. That choice
holds against the frame and the issue. #883 asks that the gate "refuse to
seal a head session whose record says it stopped part-way", and a stop
before the first line leaves no record to say so. `frame/design.md` *Scope*
Out keeps the recorder as it is. The fix pass's third ground holds too.
pytest 9.2.0 runs `pytest_configure` with no session for `--help`
(`_pytest/helpconfig.py:175`) and `--markers` (`_pytest/mark/__init__.py:139`),
read in the clone's `.venv`. A recorder that wrote at configure would leave
an unended keyed file there. A recorder change would also not close the
class: a conftest hook marked `tryfirst` still runs before any write the
recorder makes, so the boundary moves and a limit stays. The second ground,
that a configure-time stop is a different shape of run from the issue's, is
weaker: the issue names "a plugin's stop that exits 0", and a stop at
configure is one. The first and third grounds carry the choice without it.

```seal
confirms: round-1#3
```
What holds: the case round 1 gave stands in `Test_failure_lines` at
`tests/skills/test_broad_gate.py:2285-2302`, with the record's body. Run
against that case alone with the #898 `seal mutate`, four mutants went red:
`check.code == 0` as `check.code != 1`, the same as `check.code in (0, 2)`,
the append moved below the verdicts block, and the old constant text
(executed). Read against its group: `test_accepts_a_failing_suite_compared_at_the_base_with_its_counts`
(`:2258`) watches exit 1 with files, and `test_accepts_a_suite_that_exited_0_and_says_why_it_failed`
(`:2268`) watches exit 0 without files. Only the new case watches exit 0
with files and exits 2, 3 and 4, so it covers what its group does not.
`seal layout --pairs` names no pair for it (executed). Its docstring's
exits match the `RAN_TO_ITS_END` comment: 2 an interrupt, 3 an internal
error, 4 a usage error after the session started.

```seal
confirms: none
```
What matched: d43beea9 changes comments only. The recorder's docstring at
`skills/verify/scripts/pytest_record/agentic_pytest_record.py:68-73` says
such a stop "leaves no file at all". That holds: the key leaves the
environment at import (`:145`), and the file opens in
`Recorder.pytest_sessionstart` (`:280`) (read). The `RAN_TO_ITS_END`
comment's last clause is part of finding 1.

```seal
confirms: none
```
What matched: the claim of the `gaps.md` row 8ce09fc2 added.
`NO_RECORD_CAUSES` at `skills/verify/scripts/broad_gate.py:1898-1903` names
three causes of a missing record, and a stop at configure that chooses a
non-zero code is none of them (read). That list was a sample before this
branch. The run fails at such an exit either way, so the gap is a message
that tells a person an incomplete list, not a seal over unrun tests. The row
names the orchestrator as the party who weighs it.

```seal
confirms: none
```
What matched: f66eca7f folds the four replacements the close blocks of
findings 1 and 2 wrote into `frame/design.md` at `:27`, `:37`, `:59-63` and
`:72-79`, word for word (read). `rule_changes.parse` over the folded design
with policy root `docs` returned one `add` op on `docs/the-broad-gate.md`
and no refusal (executed). The `frame/plan.md` *Judgments of the run* row
names the fold and its grounds (read).

```seal
confirms: none
```
What matched: the two modules the fix diff changed pass at f66eca7f.
`bin/test tests/skills/test_broad_gate.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py -q`
gave 341 passed and 1 skipped (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate over this branch, and with it `frame/questions.md` Q1, whether `bin/test -q` leaves a session at `HEAD` stopped part-way. The suite stays labelled `unverified`, and `gaps.md` *Not verified* names the orchestrator for it. | `seal/threads/1793599986-a-stopped-head-run-does-not-seal/gaps.md` | the orchestrator's broad run, `seal gate --base origin/release/v0.28.1 --record` this work item |
| The fix pass's 97-module narrow set, 5028 passed and 12 skipped. It is an aggregate, and this round re-ran only the two modules the diff changed. | the fix pass's hand-back | the orchestrator's broad run |
| The new case and the gate cases on Linux and Windows. This round ran them on macOS with pytest 9.2.0 only. | `tests/skills/test_broad_gate.py:2285-2302` | the pull request's CI test job |
| Whether the configure-time stop's absence from `NO_RECORD_CAUSES` becomes an issue of its own. | `skills/verify/scripts/broad_gate.py:1898-1903` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_broad_gate.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py -q` at f66eca7f | 341 passed, 1 skipped, exit 0. |
| The #898 `seal mutate` over `skills/verify/scripts/broad_gate.py` with four mutants (`check.code != 1`, `check.code in (0, 2)`, the `STOPPED_AT_EXIT_0` append moved below the verdicts block, the old constant text), `--tests "bin/test tests/skills/test_broad_gate.py -q -p no:xdist -k test_accepts_the_exit_0_line_above_the_files_and_at_no_other_exit"` | Baseline passed. 4 mutants, 4 red, 0 survived. |
| The same `seal mutate` over `templates/setup/config.md` with two mutants (the new limit sentence deleted, the old exit-0 clause put back), `--tests "bin/test tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py -q -p no:xdist"` | Baseline passed. 2 mutants, 2 red. |
| `bin/test tests/skills/test_tmp_883_r2_probe.py -q -p no:xdist --tb=short -s`: the gate over the fixture repository with a row that runs pytest on `tests`, then on `other`, whose conftest calls `pytest.exit('at configure', returncode=0)` in `pytest_configure` | Gate exit 0, `BROAD GATE PASSED`, `suite   + 1 passed`, `trail/gate.md` written, one file under `records/`, `Exit: at configure` in `suite.txt`. The probe file was deleted after its one run. |
| `rule_changes.parse` over the folded `frame/design.md` with policy root `docs` | One `add` op on `docs/the-broad-gate.md`, section *One act, one owner, and the owner is the orchestrator*, no refusal. |
| `bin/seal layout --pairs` | 129 lines, none naming `tests/skills/test_broad_gate.py`. |
| `python -B -c` over `rule_changes.parse` and `rule_changes.passages`: the `to:` text's 15-word runs that stand in `templates/setup/config.md`, at 7768896c and at f66eca7f | 0 at 7768896c. 10 at f66eca7f, all in the limit sentence of finding 1. |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.28.1 --root <the branch worktree> --worktree`, with this record in place | Exit 0. Notices: the copy finding 2 quotes, this record's finding 1 and 2 open for want of a close block, and no `trail/gate.md` or `guarantee.md` yet. |
