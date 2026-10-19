# Implementation Plan: CI runs once, when the pull request opens (#943, parts 1 and 2)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved <date> by <who>, when `smith` was spawned.

## Summary

The workflows stop paying for draft state: `tests` drops its two draft events, and a newer run cancels an older one for the same pull request. The shipped orchestration then states one rule in its one owner section: build and review with the branch pushed and no pull request open, open the pull request ready once the sealer has sealed, and let CI run then. Every carrier of the old *draft before round 1* order is rewritten in the same commit. The cost is stated as a limit: a defect that shows on one platform alone is met at the pull request. No mechanism is built for it.

## Technical context

- **Triggers.** `.github/workflows/test.yml:6-14` holds the draft events and the copied paragraph. `.github/workflows/hygiene.yml:4-17` holds hygiene's own copy of the paragraph, plus `edited` for the issue-claims step. `hygiene.yml:183` runs `chain_check.py`, which reads the draft state from the event payload or from `gh pr view --json isDraft` (`chain_check.py:695-754`).
- **The case.** `tests/test_ci_gives_the_checks_what_they_need.py:406-425` requires both events on every workflow with `pull_request` in its code lines. `strip_comments` (`:40-53`) drops comment lines first. The new case reads the steps the same way: a workflow "runs `chain_check.py`" when that name appears in its comment-stripped text.
- **The owner section.** `skills/code-review/orchestration.md:157-309`. Its first two paragraphs (`:159-176`) are the old rule and the #296 history. `:178-230` is the broad run, the sealer and the repair path, which the stated limit reuses. `:289` is the `Broad gate` refusal. `:301-309` is the phase re-run the heading's second half names.
- **The carriers.**
  - `skills/implement/orchestration.md:36-42` is the order, and its acts-table row is at `:639`. `tests/test_every_orchestrator_act_names_its_delivery.py` matches every `Orchestrator:` heading to a row.
  - `skills/verify/SKILL.md:403-404` cites the heading.
  - `agents/sealer.md:4`, `:36-39` and `:67` say how the sealer is spawned and where it reads the body.
  - `docs/the-broad-gate.md:5` dates the broad run.
  - `CONTRIBUTING.md:3-27` is §*Opening a pull request*.
  - `skills/verify/scripts/broad_gate.py:3082-3084` is `CELL_UNCOMMITTED`.
- **Pins.**
  - `tests/test_the_rules_have_one_owner.py:43-46`, `:76-80`, `:161-190`;
  - `tests/test_a_parallel_agent_names_its_scratch_after_the_work_item.py:89`;
  - `tests/test_broad_gate_rule.py:361-363`;
  - `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:2319`, which splits on the heading's first words;
  - `tests/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py:578`;
  - `tests/test_the_seal_is_taken_once_by_the_sealer.py:3133`, `:3223`.
- **Lines this work must not touch**: `chain_check.py`, `docs/the-review-record.md` (#985) and `skills/implement/orchestration.md:381`, `:416` (#968). No edit in this plan reaches them. A phase that finds it has to stops and reports the line rather than editing it.
- **What breaks in six months.** A later change adds a workflow step that reads draft state through a script other than `chain_check.py`. The case then does not require the draft events on that workflow, and a draft's green merges there. The case's docstring names this limit, and the reader it keys on is named once, so the fix is one string.
- **The other failure.** A platform-only defect reaches the pull request after the sealer and costs a verifying round, a broad run and a second sealer. The owner accepted this cost in #943 §1. It is the stated limit, and the `workflow_dispatch` step is how an orchestrator who expects it pays the cost earlier.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep the draft opening before round 1, and stop record-only commits from running `tests` with `paths-ignore: seal/**` | The draft flow and its double run on *Ready for review* both stay. A required check skipped by a path filter is reported as pending rather than passed, so a record-only push could block the merge. That GitHub behaviour comes from what the framer knows of it and was not opened here | rejected. The owner decided the order on 2026-10-15 |
| **Open the pull request ready after the sealer, run `workflow_dispatch` first where the risk is platform-specific, and cancel superseded runs** | A platform-only defect is found after the sealer and its fix repeats the tail of the run | **chosen** (#943 §1) |
| Open a draft only so the sealer can `gh pr view` the body | It brings back the draft and the run that marking it ready triggers, which is what this work removes | rejected. The body is a file the prompt names, as #990's sealer already read `976-pr.md` |
| The case names `hygiene.yml` in a tuple | The tuple is a list kept beside the tree. A second workflow that runs `chain_check.py` would be required to carry nothing | rejected |
| **The case requires the draft events where a workflow runs `chain_check.py`, and refuses them elsewhere** | Another reader of draft state goes unseen (see *What breaks*) | **chosen**. The reader is named once, and the requirement follows what the workflow runs |
| Drop the case and rely on `hygiene.yml`'s comment | A comment asking the next editor to remember is what the module's docstring says it exists to replace | rejected |
| Change `chain_check.py` to stop excusing drafts | Other repositories run `templates/hygiene.yml` and may open drafts. The file is also #985's | rejected, and out of scope |
| `cancel-in-progress: true` unconditionally in `test.yml` | Two quick pushes to `main` cancel the release tag's `push` run, which `release-report` (`test.yml:276`) reads for the tag's minutes | rejected. Only `pull_request` events cancel |
| Group on `github.ref` alone | A `pull_request` run's `github.ref` is `refs/pull/<N>/merge`, which works. Keying on `github.event.pull_request.number \|\| github.ref` says what it means and also gives `push` and `workflow_dispatch` runs their own group | chose the explicit key |
| Rename the heading's second half too | The section's `:301-309` paragraph is the phase re-run it names, so that half is still true | kept that half |

## Phases

Vertical slices — each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **The workflows and their cases (S1, S2, S3).** `test.yml`: drop the two draft events and `:7-13`, leave a bare `pull_request:` with a one-line comment pointing to `hygiene.yml`, and add the `concurrency` block from `spec.md` §*Data & interfaces*. `hygiene.yml`: rewrite `:5-11` so it states why the events are there without telling anyone to open a draft, keep `types:` as it is, and add the block with `cancel-in-progress: true`. `tests/test_ci_gives_the_checks_what_they_need.py`: rewrite the draft-events case to S2's if-and-only-if, add the concurrency case (S3), and rewrite the module docstring's *Which pull-request events run* paragraph to match | `bin/test tests/test_ci_gives_the_checks_what_they_need.py -q`. Each case is seen red the ways S1–S3 name, and the phase record says how | |
| 2 | **The rule, rewritten in place (S4–S10).** The owner section in `skills/code-review/orchestration.md` is renamed and rewritten as `spec.md` §*Scope* item 3 says, and every carrier and pin named in *Technical context* changes in the same commit. That includes `CELL_UNCOMMITTED`: its new text drops "marked ready" and stays true for a pull request already open, for example `CI reads HEAD, so commit it before you push`. The phase writes `changelog.md` in this directory | `bin/test` on `test_the_rules_have_one_owner.py`, `test_every_orchestrator_act_names_its_delivery.py`, `test_a_parallel_agent_names_its_scratch_after_the_work_item.py`, `test_broad_gate_rule.py`, `test_the_broad_gate_row_is_asked_for_and_runs_as_written.py`, the sealer module S8 lands in, and `test_the_stamp_reaches_the_person_it_is_drawn_for.py` and `test_the_seal_is_taken_once_by_the_sealer.py` with `-k` on the cases that read the changed text. Then `git grep -n -e "opens before round 1" -e "as a draft" -e "marked ready" -- skills agents docs CONTRIBUTING.md .github/workflows`, whose remaining hits are each named in the phase record with why they stay | |

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past one
— someone can open it — which is the same trick that lets a round record live
beside the contract rather than in tool state.

Fill it in as each phase closes, not at the end. A phase reconstructed
afterwards is reconstructed from the diff, which is where it already was.

What a phase discovers while it is being built, and needs the next phase to
know, does not fit in this table's cells. Write it to
`seal/specs/<work-item-id>/phases/phase-N.md`, from `templates/sdd-phase.md`,
when the phase closes.

One caveat, so nobody builds on it, and it has two halves. Where feature
branches squash, these commits stop resolving at the merge — and **a rebase
during the work does the same thing earlier and far more quietly**, because the
orphaned object still answers `git cat-file` in the worktree that wrote it.
The quiet half is the one that bites: this column was wrong on its own first
use, nine SHAs deep, and only a reviewer opening them found it. **Re-read the
column after any rebase**, or it names commits that resolve in one clone and
nowhere else. That is tolerable because nothing measures from this column.

## Operational impact

- **This repository's CI.** Marking a draft ready no longer starts `tests`. A push to an open pull request cancels that pull request's `tests` and `hygiene` runs still in progress. `push` to `main` and `workflow_dispatch` behave as before.
- **What the gate change carries** (`CONTRIBUTING.md` §*What a change to a gate must carry*):
  - *Failure direction*: the CI checks allow more, in one place only, because a draft's *Ready for review* no longer re-runs the suite on the same commit, whose result was the draft's. `hygiene` still re-runs, so `chain_check` never lets a draft's green through.
  - *Prompt budget*: none is added.
  - *Platform honesty*: the trigger and cancellation behaviour can be observed only on GitHub. Q1 in `questions.md` records who reads it.
  - *What it removes*: `spec.md` §*Removes*.
- **Other repositories.** `templates/hygiene.yml` is unchanged. An orchestrator following the plugin's skills elsewhere opens its pull request after the sealer from 0.22.2 on, and a repository whose people still open drafts keeps the draft excuse.
- No migration, environment variable or dependency.
