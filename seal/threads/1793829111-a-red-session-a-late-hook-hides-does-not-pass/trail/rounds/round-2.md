# Review round 2: 1793829111-a-red-session-a-late-hook-hides-does-not-pass

```seal
target: 6b96900d, fixes 5fa9a306..6b96900d
```

This is a verifying round. It reviewed the diff of round 1's fixes: c9a1b1bf (the frame fold), 9a5386d6 (the phase record and the closing memo) and 6b96900d (round 1's close blocks). The diff touches only the work item's records. `git diff --stat 5fa9a306..6b96900d` lists six files, all under `seal/threads/1793829111-a-red-session-a-late-hook-hides-does-not-pass/`, so the code and the tests are the ones round 1 reviewed at b5d3d85. `seal/parity.md` is not declared, so no parity comparison applies.

Facts carried from round 1 rather than re-established: G2's reading of pytest's `_main` at `.venv/lib/python3.13/site-packages/_pytest/main.py:365-371`; that `tests/skills/test_broad_gate.py:1561-1573` (S5's case) writes its `end` lines by hand through `end()` and starts no pytest; and that no `SKIPPED` line in the log of run 41924200504 names a new case. Round 1 executed the last one, against the same run. Facts re-established this round: rule 3's text at `templates/setup/config.md:371`, the four `LATE_ACTS` shapes at `tests/skills/test_broad_gate.py:2493-2511`, the recorder's plain `pytest_sessionfinish` at `skills/verify/scripts/pytest_record/agentic_pytest_record.py:381`, the frame's text at e06313c5 and at b5d3d855, and the jobs of run 41924200504.

## Findings

None. Both closes hold, and the new units of the diff hold against the tree.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the `to:` item of `frame/design.md` `## Rule changes` (`design.md:93-116`) is round 1's paste-ready text, character for character (executed, the containment check under `## Probes`). It no longer lists the acts after the run loop. It keeps the reason in one clause ("what runs after the loop can change the row's exit and not that one") and sends the reader to rule 3 for the acts and for the configure-time stop. The crafter's close claims that rule 3 at HEAD already names both, so `templates/setup/config.md:371` needs no change. That claim holds. Rule 3 reads "Such an act is a hook that sets the session's exit status, a later `pytest_sessionfinish` hook that raises `pytest.exit()`, a `pytest_unconfigure` hook that ends the process, or a part of the row after pytest, such as `; true` or a pipe". It also says the gate "reads the run as though that session never started: it judges the run on the row's exit and on the records the row's other sessions left". The finding named `config.md:371` as the second copy, not as a defect of its own. The copy the finding asked to remove stood in `design.md`, and c9a1b1bf removed it there. No fix commit touched `templates/setup/config.md` (`git diff --stat 5fa9a306..6b96900d -- templates` is empty), and none needed to. After the settle, rule 3 is the one place that lists the acts. Read.

```seal
confirms: round-1#2
```
What holds: the three sentences round 1 gave are in place, verbatim (executed, the containment check under `## Probes`): `frame/plan.md:16`, `frame/questions.md:11` and Q1's question cell at `frame/questions.md:15`. Each is true at HEAD. `early-exitstatus-0` is a `tryfirst` `pytest_sessionfinish` that sets `session.exitstatus = 0` (`tests/skills/test_broad_gate.py:2500-2505`). The recorder's own `pytest_sessionfinish` carries no ordering mark (`agentic_pytest_record.py:381`), so that hook runs before it. On a pytest that hands later hooks the live `session.exitstatus`, the recorder would read 0 and the case would turn red. `late-pytest-exit-0` is `trylast` (`test_broad_gate.py:2494-2499`) and raises after the recorder wrote. S5's case starts no pytest. So the sentences now name the one case that meets that release, and they say why the other two do not. Q1's question cell now spells the shape as the escaped `\|\|` row, which is how S2 (`design.md:57`) and `row-or-interpreter` (`test_broad_gate.py:2510`) spell it. The same commit also changed Q1's options cell from "the `; true` shape" to "the shell-composition shape", which is the same fact one cell over. Read.

What matched: Q1's Status, the one part of the fix the orchestrator wrote itself, reads `answered 2026-11-05 by the orchestrator`, which is the spelling `skills/implement/SKILL.md:264` gives. Its facts hold. Run 41924200504 is the `tests` workflow on b5d3d8550d95, it completed with conclusion `success`, and its `pytest` jobs are four Windows legs, three macOS legs and one ubuntu leg, each `success` (executed, `gh run view 41924200504 --json headSha,status,conclusion,workflowName,jobs`). Between b5d3d855 and HEAD only the work item's records changed, so that run measured the code under review.

What matched: the closed row of `gaps.md` (`gaps.md:7`) opens with the word `closed`, and its second cell says what closed it, as `skills/implement/SKILL.md:365-366` gives the form. `seal unverified` reports one open row and one closed row for this work item (executed). The open row left is the broad gate's, which is the orchestrator's. The cell says the run "concluded `success` on every job". That is close but not exact: the `release-report` job was skipped, and the other twelve jobs ended `success`. The run's conclusion and every `pytest` leg are as the row says, and nothing a party does turns on the skipped job, so this round opens no finding for it.

What matched: the corrections 9a5386d6 made to `trail/phases/phase-1.md` hold against git. At e06313c5, *Scope* 3 read "The session either stopped part-way or ended with exit 1, and something after pytest's run loop chose the row's exit". S2 named "a row ending `; true`" and a plain `pytest_sessionfinish` hook. At b5d3d855, *Scope* 3 gives each cause its own branch, and S2 names the `tryfirst` hook, the `pytest_unconfigure` hook and the escaped `\|\|` row (executed, `git show e06313c5:` and `git show b5d3d855` over `frame/design.md`). So each sentence now names the commit whose state it reports, and HEAD contradicts none of them. The phase record's added sentence about run 41924200504 matches the run.

`frame/questions.md:17` still says "the pull request's CI test job answers it". What answered Q1 was a run of the same `tests` workflow dispatched on the branch, and Q1's Status names that run. The line gives the question's reason, and no party acts on it once the Status is answered, so this round opens no finding for it.

What matched: the chain check accepts the round 1 close blocks of 6b96900d. Before this record was written, it named only the two closes as owing a verifying round, and the gate record and the guarantee as not yet written (executed, under `## Probes`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD; the suite stays `unverified`. This round leaves nothing open, so the next step is the orchestrator's broad run, then the sealer's spawn | `seal/config.md` `Broad gate` row | the orchestrator's broad run, then the sealer |
| The crafter's claim that the record checks over the corrected records ran 58 passed. The claim names no modules, so it was not re-run as stated. This round's own narrow run is under `## Probes` | the crafter's hand-back | the sealer's sample |

## Probes

| Command | Result |
|---|---|
| `git diff --stat 5fa9a306..6b96900d` | six files, all under the work item's directory |
| A `python3` containment check of each of round 1's four paste-ready blocks in `frame/design.md`, `frame/plan.md` and `frame/questions.md` | each block found, in the file its finding named |
| `gh run view 41924200504 --json headSha,status,conclusion,workflowName,jobs` | `tests` on b5d3d8550d95, completed, `success`; eight `pytest` jobs, `lint`, `durations` and two `arms-grammar` jobs `success`; `release-report` skipped |
| `bin/seal unverified` | exit 0; one open row and one closed row for this work item |
| `bin/test tests/behaviour/test_the_set_a_work_item_always_has.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py -q` | 107 passed, exit 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline release/v0.32.1 --root <the worktree> --worktree`, before the record was written, with the tree's copy and with the installed plugin's copy | exit 0 from each; it notices round 1's two closes as owing a verifying round, and no notice at a line of `frame/design.md` |
| The same chain check, with this record written | exit 0 from each copy; the notice about the two closes is gone, and only the gate record and the guarantee are named as not yet written |
| `bin/test tests/text/test_the_record_is_written_in_words.py -q`, with this record written | exit 0 |
