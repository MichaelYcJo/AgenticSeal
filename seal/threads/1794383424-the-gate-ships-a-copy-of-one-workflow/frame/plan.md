# Implementation Plan: the broad gate ships a copy of one workflow (#1483)

## Technical context

The tree as read at `5909a2776`.

`skills/verify/scripts/broad_gate.py` is 2,906 lines (executed: `wc -l`). The section this work removes stands at `:1722-2059`, and `frame/design.md` G4 places every other line that reads or states it. The gate's arms are the repository's command, the chain check and the mode check, listed in the module docstring at `:12-29` and run by `gate` at `:2678-2694` (read). Removing the section leaves all three, and changes no exit code and no line of `trail/gate.md`.

The work is one vertical slice. The deleted behaviour file is named by the check line at `docs/running/the-broad-gate.md:81`, and `skills/verify/orchestration.md:69` is pinned by `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:204`. So the code, its cases and the documents `frame/design.md` G7 names change in one commit, or the suite is red at the commit between them.

**What breaks in six months.** A step is added to `hygiene.yml`'s `release` job that the gate could have answered locally, and nothing says so. The gate passes, and CI refuses that step on the pull request: one CI round, the cost #468 recorded once. CI is the check of record, and the step's failure names itself there. In a user's repository nothing changes, because the section never read their workflow (`frame/design.md` G5).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Remove the section, its cases and the documents that state it (chosen) | The six-month scenario above: a locally answerable step goes unmirrored and costs one CI round when it fails. | Chosen. The issue's owner asks for it (G1), the table is a copy kept beside the tree (G3), and its one catch is #468 against the later changes G12 counts. |
| Keep the structure: the table and both-sides case, as they stand | Every edit to `hygiene.yml`'s `release` job keeps paying a row, every user's copy keeps the 338 lines of `:1722-2059`, which print nothing for them (G5), and the count keeps being printed with no party told to act on it (G12). | Rejected. The premise that keeps it is that the broad run must say what CI will say. Checked: CI runs every step on the pull request whatever the gate says, and the gate already says what it ran in its arm list. |
| Keep the table in the test alone, and drop the row and the line from the gate | The case still holds a hand copy of step names against the workflow, so each step edit still pays a row, and the copy answers no reader at run time. | Rejected. It keeps the copy G3 says goes, without the output that was its reason. |
| Read the job the user installed (`hygiene`) as well as this repository's `release` | A second partition is needed for the template's steps, and the gate ships both copies to every repository. | Rejected. It doubles the copy to make it print in a user's repository, and no party acts on the count. |
| Replace the regular-expression reader with a YAML parser | The gate runs with no third-party dependency (read: `broad_gate.py:1776-1777`). PyYAML would be pinned for tests only, by #1486. | Rejected. The reader is not the defect; the copy is. |
| `## Rule changes` holds a `remove` with a `from` for the `docs/running/the-broad-gate.md` rule | The rule's check line names the deleted file, and `seal rules --check` excuses nothing for a `remove` with a `from`, so the suite is red at HEAD until the settle (G8). | Rejected. The document is edited in place, as #1393 did on the same grounds. |
| Remove the `.test_durations` entries of the deleted cases | Modify/delete conflict with #1486, which removes the file in this release. | Rejected. G13 measures the entries under the file's stale share. |
| Rewrite the docstring of `test_the_workflow_is_not_a_step_of_the_release_job` and keep it | The case would assert a fact whose only stated reason, the partition, is gone. | Rejected. The case leaves (`frame/design.md` *Scope* item 6). |
| Keep the not-UTF-8 case and the no-workflow case as they stand | After the work the gate opens no workflow, so both pass against any gate that ignores the file and pin no guard. | Rejected. One case, S3's, takes a workflow that does carry a `release` job, which is red against the base. |
| Set `LABEL_WIDTH` to 6, the widest label left | The stamp a user's sealer draws moves its values one column left. | Rejected. The width is the owner's, and S1 keeps a user's output unchanged (G11). |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 to 9. | S3's case shown red against the base's `broad_gate.py`, then green. S4's `git grep` prints nothing. The narrow run: `bin/test tests/skills/test_broad_gate.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py tests/behaviour/test_a_release_publishes_its_note.py tests/test_conftest.py tests/skills/test_seal_stamp.py tests/github/test_rules.py tests/behaviour/test_this_repository_passes_its_own_checks.py tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py -q`. The broad gate is the orchestrator's (S2). | `a94a5ac72` |

## Overlap with the release

The spawn names nine other items. #1481 (`skills/settle/`) and #1487 (`evals/scripts/`) change no file this work changes and read nothing it removes. #1498 changes `tests/censuses.py#_root_names` alone, and `tests/skills/test_broad_gate.py` keeps its census line as it is, so the two do not meet; #1498 merges first, as the spawn states, with the version move. #1489 builds after #1488 and changes no file this work changes. The items that meet it:

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1486 | `tests/behaviour/test_a_release_publishes_its_note.py`: this work removes the case at `:228-234`, #1486 rewrites `:124-149`. `tests/conftest.py:126`, `:144` and `tests/test_conftest.py:422`: this work rewrites their docstrings, and #1486 may replace those workflow readers with PyYAML. `.test_durations`: this work leaves it, and #1486 deletes it. | #1483 | This diff removes and rewrites docstrings, and is the smaller. #1486 moves CI jobs and owes measurements before and after, so it is less likely to be sealed first. Merged after this, #1486 meets at most a docstring conflict in a reader it may delete anyway. |
| #1488 | `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:170-205`, and the literal asserts of `tests/behaviour/test_the_gate_names_every_step_ci_runs.py`, which this work deletes. | #1483 | #1488 counts literal asserts before and after. Merged after this, it counts a tree without the asserts this work deletes, and edits none of them. |
| #1485 | `skills/verify/scripts/broad_gate.py`'s docstrings and comments. | #1483 | #1485's issue builds after #1483. This work changes only the sentences that state the section's facts, and #1485 then rewrites the history on a file without the section. |
| #1484 | `skills/verify/scripts/seal_stamp.py`: this work changes `:521-529` and `:592-593`, and #1484 removes `DISC_COLOURS` at `:129` and touches `strip_ansi` at `:497`. | #1483 | #1484 has not started, and builds after #1482. `DOT` would be a symbol nobody reads after this work, which this work removes rather than leaving for #1484. |
| #1482 | `broad_gate.py#load`, a by-path loader at `:205-225`, and `tests/skills/test_broad_gate.py:51` may be among #1482's loaders. This work edits neither line. | #1483 | #1482 has not started. The files meet and the lines do not. |

## Operational impact

None for a user's repository: `seal gate` prints what it printed before (S1). In this repository the gate's report loses its `CI also` row and its stderr loses the coverage line (S2). No migration, environment variable or dependency. This pull request moves no version: #1498 carries the move to 0.37.4.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-11 | Phase 1's hand-back named three frame statements HEAD left incomplete, and the orchestrator folded them into `frame/design.md` in its own commit: the preflight clause at `broad_gate.py:107` (G4 and *Scope* item 2), the `Test_panel` rename (*Scope* item 4), and S3 reading the panel the gate prints | They record what the build changed, not what the work is | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph opening **The framer writes a decision's fold** |
| 2026-11-11 | Round 1's two `should` findings located in frame files go to the framer to fold: finding 1, *Scope* item 2's clause naming `moved_line` as the one reader of `base.given`, which `gate()`'s refusal also reads (`broad_gate.py:2246` at `27bbbdd75`); finding 2, the frame naming `main` where the lines stand in `gate()` (`def gate` at `:2571-2803` of `5909a2776`) | The orchestrator opened both coordinates and confirmed them (executed, `grep -n` on `.given` and on `def gate`/`def main`) | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph opening **The framer writes a decision's fold** |
| 2026-11-11 | The title takes `refactor:`, as the issue's title does | The gate's verdict and every user's output are unchanged; the work removes a copy and its readers | `~/.claude/skills/commit-pr-convention/SKILL.md` *커밋 메시지* |
