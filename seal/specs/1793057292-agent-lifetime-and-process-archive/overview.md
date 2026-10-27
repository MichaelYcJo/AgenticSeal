# Overview: an agent lives one phase, the orchestrator's steps sit where it acts, two re-checks leave, and each release records how the process changed (#945)

## Why this work exists

One smith was resumed across every phase and fix pass of a work item and
re-read all its earlier work on every turn, the orchestrator re-ran each
hand-back, and the unverified record's CI step caught nothing in 142 failed
runs. Now each phase is a fresh smith, a fix pass resumes the implementer
only below 806,241 tokens of context, the two re-checks are gone, and each
release can record how the way of working changed in `seal/process/`.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The shape of the new `session_cost.py` function | *Data & interfaces*: "a new function computing one slice's largest per-turn context from the slice's assistant messages" / `largest_context(path, cuts=())` reads a transcript once and returns one value per window of the coordinator's cuts | the code | a resumed file is opened once for the column rather than once per slice; `segment_slices` reads each kept slice's value at its window (`phases/phase-1.md`) |
| `tests/test_arm_check.py` | *Removes* and S10: the cases in `tests/test_broad_gate.py` and `tests/test_arm_check.py` that name the `unverified` arm / `tests/test_arm_check.py` names no such arm and is unchanged | the code | the module tests `arm_check.py`, the mutation-arm counter, and its word "arm" means a branch of code, not a broad-gate arm (`phases/phase-3.md`) |
| Removals *Removes* does not name | *Removes* lists the sites of phases 2 and 3 / these also left: the old rule's words pinned by `tests/test_review_axes.py#test_the_fix_pass_resumes_the_implementer`, rewritten in place; `broad_gate.py`'s `SPECS` constant; the two workflow parameters of `tests/test_unverified_rows_close.py#test_the_documents_state_the_merge_base_footing`; the assertion in `tests/test_first_setup_asks_once.py#test_the_template_runs_the_two_shipped_checks_from_the_plugin_at_its_tag` that the template runs `unverified_check.py`; three `.test_durations` entries for removed cases | the code | each stated the removed rule, step or arm, and contract rule 19 removes what stood on the old fact in the same commit (`phases/phase-2.md`, `phases/phase-3.md`) |
| What the comment census reads | S13: "When the template censuses run, Then it carries no comment" / `tests/test_a_record_carries_no_comment.py` read only `templates/sdd-*.md`, so `templates/process.md` was outside it; the census now reads `RECORD_TEMPLATES`, the `sdd-*.md` templates and `process.md` | the code | the template's file name is fixed by *Data & interfaces*, and without the change S13's case passes on a comment put into `templates/process.md` (`phases/phase-4.md`) |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and format check, and the typecheck at the branch head | the orchestrator, by `broad-gate --base <base> --record` before the sealer is spawned |
| The cases on Linux and Windows: every case of this work item ran on macOS only, and the removed step ran on `ubuntu-latest` | the orchestrator, from the `tests` workflow's legs on the branch or the pull request |
| The framer's line in `agents/framer.md` step 4: S14 names no case, and no case pins the line | the warden, at round 1 |
| The sentence that the orchestrator deletes the `plan.md` line naming the comments to fold, in the commit that folds them: no case pins it | the warden, at round 1 |
| Which work item the prevention-home rule's "a rule in the work item that rewrites the file the act is read from" and "that work item's issue" name: the one in progress, or whichever work item rewrites that file. `skills/implement/orchestration.md` copies *Scope* item 4's words, which carry both readings | the orchestrator, who folds the answer into the frame |

## Not done

The policy sentences of `spec.md` *Rule changes*. `docs/` is the policy root,
which this pull request does not edit; the settle after the release that
ships this work item applies them. Until then the process-archive step
stands in `spec.md` and not in `docs/release-checklist.md`, and the release
preparation reads it there as the policy in force.

The settle that applies this spec's `docs/release-checklist.md` items turns
one parameter red. Those items remove both sentences of that file that name
the merge base, and the parameter `docs/release-checklist.md-None-None` of
`tests/test_unverified_rows_close.py#test_the_documents_state_the_merge_base_footing`
asserts the file says *merge-base* or *merge base*. The settle session
removes that parameter in the settle's own commit (`phases/phase-3.md`).

No archive file for 0.22.0 to 0.22.3, by `questions.md` Q1's default (a).
The first file is written at the preparation of the release that ships this
work item, by whoever prepares it.

No rebase rule: a conflict is integrated by a merge, by `questions.md` Q2's
default (a), because `docs/release-checklist.md` *0. Before starting* forbids
rebasing a work item's branch.

The prices of the new and rewritten cases in `.test_durations`. The entries
of the removed cases went in phase 3. The new cases stay unpriced until the
next refresh.

A repository installed from an earlier release keeps the unverified step
until `seal pr-checks install` writes the file again, because the workflow is
pinned to the release that wrote it.

## The gate change, for the pull request

`CONTRIBUTING.md` *What a change to a gate must carry*, copied from
`phases/phase-3.md`:

- **Failure direction**: the gate allows more. A pull request that deletes a
  `## Not verified` row, or a whole `overview.md`, instead of closing it now
  passes CI and the broad gate. That is the cheaper mistake here: the step
  failed in none of 142 failed hygiene runs (`spec.md` *Scope* item 5). Its
  recorded issues are its own defects. A deleted row still meets the warden,
  who reads `overview.md` in the diff at stage 1, and the sealer. A wrong
  allow here costs a lost row of a record. It cannot break another session's
  tree.
- **Prompt budget**: zero. The change removes a CI step and a gate arm, and
  it asks nobody anything.
- **Platforms**: the cases ran on macOS only. The removed step ran on
  `ubuntu-latest`. Nothing here was run on Linux or Windows; CI on the pull
  request answers both.
- **What it removes**: the CI step in both workflows, the broad-gate arm with
  its constants (`UNVERIFIED`, `UNVERIFIED_NAME`, `SPECS`) and its
  `PARTITION` row, and the release-day ordering duty the step put on
  `docs/release-checklist.md`, through `## Rule changes`. It adds nothing.

## Fed back into the spec

Inferred during implementation, for a planner to overturn:

- `largest_context` counts every message carrying a `usage` block, whether or
  not it calls a tool, once by `message_key`, at the largest value each of
  the three input fields reached across its rows. A window with no message
  answers None, and the table prints a dash. Where there are cuts, a message
  whose stamp does not parse is dropped, as `segment_slices` drops a turn.
- The orchestrator is the party that folds a decision into the frame, and the
  line `plan.md` carries until the fold sits on a line of its own below the
  approval line.
- The `mergeable` paragraph names `MERGEABLE` as the answer under which CI is
  waited on, so all three values `gh` returns have a reading.
- `broad_gate.py#failed_form` pads to the widest failing name, a rule kept
  though no arm name is longer than 8 now.
- `templates/process.md` is a record template, and the comment census reads
  it beside the `sdd-*.md` templates.
- The framer reads the archive of the highest version, which is what
  *Scope*'s "the latest `seal/process/<X.Y.Z>.md`" is taken to mean.
