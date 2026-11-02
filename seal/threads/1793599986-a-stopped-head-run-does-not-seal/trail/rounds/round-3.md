# Review round 3: 1793599986-a-stopped-head-run-does-not-seal

```seal
target: 13290690, fixes c00169dc..13290690
```

This is the verifying round over the fix pass of round 2. It read the diff
c00169dc..13290690 in a `git clone --no-local` of the branch worktree at
13290690, with 40e6c23e as the baseline. The diff has four commits: 2336ffb3
(the orchestrator's `frame/plan.md` row routing round 2 to a fix pass),
3de5c6c8 (both findings), 2eee66a8 (the close blocks and a `handoff.md`) and
13290690 (the orchestrator's fold into `frame/design.md`, a *Judgments of
the run* row, and `handoff.md` removed). `seal/parity.md` is not declared, so
the round block carries no `original:` line. Every mutant this round planted
ran through the `seal` of the #898 worktree
(`fix/898-a-mutant-that-does-not-compile-reads-as-caught/bin/seal mutate`).

Facts carried from round 2, not re-established: `read_record` reads every
keyed file under `records/` (`skills/verify/scripts/broad_gate.py:1747`), and
the recorder writes its `end` line in `Recorder.pytest_sessionfinish`
(`skills/verify/scripts/pytest_record/agentic_pytest_record.py:378`).
Re-established this round: round 2's two-runner probe was written again
from its `## Probes` row and run, with two more cases beside it. Every
verdict below was reached this round.

## Findings

None. Both closes of round 2 hold, and the fix diff introduced no defect
this round found.

## Confirmations

```seal
confirms: round-2#1
```
What holds: the fix pass claimed that rule 3 now states the configure-time
stop by what the gate reads per session. `templates/setup/config.md:366`
reads: the stop "leaves no record of that session, so the gate reads the run
as though that session never started: it judges the run on the row's exit
and on the records the row's other sessions left, where there are any." The
probe of round 2, written again, held both shapes of row to it (executed).
With the row `pytest tests && pytest other`, where `other/conftest.py` calls
`pytest.exit('at configure', returncode=0)` in `pytest_configure` and
`other/test_never.py` fails, the gate returned 0 and printed
`BROAD GATE PASSED` with the first runner's `1 passed`. `records/` held one
file, and `trail/gate.md` was written. So the run was judged on the row's
exit and the other session's record. With the row `pytest other` alone, the
gate returned 0 with `suite   exit 0`. `records/` was empty, so the run was
judged on the exit alone, as "where there are any" allows.

The pin moved with the sentence:
`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:538-546`
holds it by substring. Four mutants of rule 3 each went red against
`test_the_measurement_its_cost_and_its_limits_are_told_where_the_row_is_written`
alone (executed). The four were "where there are any" cut, the old clause
"on its exit alone" put back, the opening sentence of the two limits
deleted, and the `pytest_sessionfinish` exit clause cut. The fix pass also
claimed the changelog lost its limit sentences and now names the two kinds
and points to rule 3. That holds at `changelog.md:3` (read). A `git grep` for
"started no pytest", "exit alone" and "judged on its exit" outside the round
records now finds the old clause nowhere. The changelog's "decided the suite
on that exit alone" and `frame/plan.md:25` are about the old verdict, not
the limit (executed). The `RAN_TO_ITS_END` comment at
`skills/verify/scripts/broad_gate.py:1728-1733` says the same in short form
(read). Its line 1731 runs to 130 characters where its neighbours wrap at
79. `ruff.toml` selects no line-length rule, and `ruff format --check`
passes the file (executed), so that is layout and no finding.

```seal
confirms: round-2#2
```
What holds: both limits now stand in rule 3 alone, and the `to:` names them
and points there. `rule_changes.parse` over the folded `frame/design.md` with
policy root `docs` gave one `add` op on `docs/the-broad-gate.md` with no
errors and nothing unread. `rule_changes.copies` of that op against
`templates/setup/config.md` and `docs/the-broad-gate.md` returned no shared
run of 15 words (executed). Round 2 counted 10 such runs at f66eca7f. The
chain check over the branch worktree printed no copy or pin notice at any
line of `frame/design.md` (executed, the `## Probes` row). The cited section
exists: `templates/setup/config.md:357` is `### The criterion for choosing a
value`.

The fix pass claimed the `pytest_sessionfinish` sentence's new clause, "and
its pytest exits with the code that hook chose", from pytest 9.2.0's
`wrap_session`. The `finally` branch at
`.venv/lib/python3.13/site-packages/_pytest/main.py:366-374` catches an
`Exit` from `pytest_sessionfinish` and sets `session.exitstatus` to its
`returncode` where that is not `None` (read, in the clone's venv). A third
probe case ran it (executed). A `tests/conftest.py` with a `trylast`
`pytest_sessionfinish` calling `pytest.exit('late', returncode=0)` and a
failing test gave a row exit of 0. Its record's `end` line read
`"exitstatus": 1` and `"stopped": []`. So the session reads as one that ran
to its end, and its pytest exits with the code the hook chose. Where the
hook passes no code, pytest keeps the session's own exit, and the `end` line
then holds that same exit, so the clause covers the case where it matters.
The *Scope* Out bullet at `frame/design.md:37` now names rule 3 as the place
that states both limits. *Scope* item 3 still lists only the exit-0 clause
for rule 3. The Out bullet says where the limits went, so the frame does not
contradict the diff.

```seal
confirms: none
```
What matched: 13290690 folds the close blocks' text word for word. The
`to:` ending at `frame/design.md:72-77` is the `answer:` of round 2's
finding 2, and the bullet's last sentence at `:37` is that answer's
proposed sentence (read). The two *Judgments of the run* rows at
`frame/plan.md:44-45` name their grounds and the document each was judged
against (read). `handoff.md`, added in 2eee66a8, is gone at 13290690
(read: `git show --stat`). The fix diff adds no test function. It moves
strings within one pin list, so no test needs reading against its group.

```seal
confirms: none
```
What matched: the modules that read the paths the fix diff changed pass at
13290690. `bin/test` over `tests/skills/test_broad_gate.py`,
`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`,
`tests/behaviour/test_docs_line_wrap.py`,
`tests/text/test_a_document_has_room_for_the_next_fold.py`,
`tests/text/test_the_rules_have_one_owner.py`,
`tests/text/test_broad_gate_rule.py` and
`tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py`
gave 444 passed and 1 skipped (executed). That is a probe of those modules,
not the suite.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate over this branch, and with it `frame/questions.md` Q1, whether `bin/test -q` leaves a session at `HEAD` stopped part-way. The suite stays labelled `unverified`. This round leaves nothing open, so the orchestrator's broad run comes due, then the sealer. | `seal/threads/1793599986-a-stopped-head-run-does-not-seal/gaps.md` | the orchestrator's broad run, `seal gate --base 40e6c23e --record` this work item |
| A late `pytest_sessionfinish` hook that turns a red session's exit into 0. The third probe case shows the gate returning 0 with `BROAD GATE PASSED`, writing `trail/gate.md`, and printing `1 failed` and `1 passed` on its suite row behind the passing mark. The record held the failing test and an `end` line with exit 1. Before #883 the suite was decided on the row's exit alone (`frame/design.md` G4, read), so this predates the branch, and the fix diff does not widen it. Rule 3 now states the exit half of the limit. | `skills/verify/scripts/broad_gate.py#gate`, `templates/setup/config.md:366` | the owner, whether it becomes an issue of its own |
| The new exit clause on pytest other than 9.2.0. This round read and ran `wrap_session` on 9.2.0 alone. | `templates/setup/config.md:366` | the pull request's CI test job |
| The fix pass's 97-module narrow set, 5028 passed and 12 skipped. It is an aggregate, and this round re-ran seven modules. | the fix pass's hand-back | the orchestrator's broad run |
| Whether the configure-time stop's absence from `NO_RECORD_CAUSES` becomes an issue of its own, carried from round 2. | `skills/verify/scripts/broad_gate.py#NO_RECORD_CAUSES` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| The #898 `seal mutate` over `templates/setup/config.md` with four mutants: "where there are any" cut, the old "on its exit alone" clause put back, "Two stops are out of the record's reach." deleted, the `pytest_sessionfinish` exit clause cut, `--tests "bin/test tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py -q -p no:xdist -k test_the_measurement_its_cost_and_its_limits_are_told_where_the_row_is_written"` | Baseline passed. 4 mutants, 4 red, 0 survived. |
| `bin/test tests/skills/test_tmp_883_r3_probe.py -q -p no:xdist --tb=short -s`, three cases over the fixture repository of `tests/skills/test_broad_gate.py`: a two-runner row whose second runner's conftest stops at `pytest_configure` with code 0; the same stop in a one-runner row; and a `trylast` `pytest_sessionfinish` hook calling `pytest.exit('late', returncode=0)` over a failing test | Two runners: gate 0, `BROAD GATE PASSED`, `suite   + 1 passed`, one file under `records/`, `trail/gate.md` written. One runner: gate 0, `suite   exit 0`, no file under `records/`, `trail/gate.md` written. Late hook: gate 0, `BROAD GATE PASSED`, the suite row printing `1 failed` and `1 passed`, one record whose `end` line reads `"exitstatus": 1, "unplaced": 0, "stopped": []`, `Exit: late` and `exit 0` in `suite.txt`, `trail/gate.md` written. The probe file was deleted after its one run. |
| `python3 -B -c` over `rule_changes.parse` and `rule_changes.copies`: the folded `frame/design.md` with policy root `docs`, its op against `templates/setup/config.md` and `docs/the-broad-gate.md` at 13290690 | One `add` op on `docs/the-broad-gate.md`, no errors, nothing unread. No shared run of 15 words. |
| `git grep -n "started no pytest\|exit alone\|judged on its exit"` at 13290690 | Outside `trail/rounds/`, two hits: `changelog.md:3` on the old verdict and `frame/plan.md:25` on alternative F. No hit for the old limit clause. |
| `uvx ruff format --check skills/verify/scripts/broad_gate.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py` | Exit 0. |
| `bin/test` over the seven modules named under `## Confirmations` | 444 passed, 1 skipped, exit 0. |
| `python3 skills/code-review/scripts/chain_check.py --baseline 40e6c23e --root <the branch worktree> --worktree`, with this record in place | Exit 0. No refusal, and no copy or pin notice at a line of `frame/design.md`. Its notices: the pull request's state is unknown, it read the working tree, and git carries no `trail/gate.md` and no `guarantee.md` yet. |
