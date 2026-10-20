# Feature Specification: CI runs once, when the pull request opens (#943, parts 1 and 2)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| #943 §1 (owner, 2026-10-15) | The rule: push the branch freely while building, open the pull request **ready** once the sealer has sealed, and CI runs then and on every later push. A platform-specific change runs `tests` by `workflow_dispatch` before the pull request. A new run of a workflow cancels the one still running for the same pull request |
| #943 §2 | `tests` drops `ready_for_review` and `converted_to_draft` and the paragraph it copied from `hygiene.yml`; the case requires the two events only where a workflow's result depends on draft state; `templates/hygiene.yml` keeps them |
| The owner, 2026-10-19 (spawn prompt) | A finding that the normal one-issue flow can meet only after the pull request opens, such as a defect on one platform, is a **stated limit**. No mechanism is built for it |
| `CLAUDE.md` §*The rule a mechanism is kept against* | One owner for the rule and a link from every other carrier. The text is rewritten in place, and every sentence, case and citation that stated the old rule is removed in the same commit (contract §19) |
| `docs/the-broad-gate.md` (policy) | The broad run is one act, after the rounds settle. Line 5 dates it by "before a pull request is marked ready", which this work rewrites, because no draft exists to mark |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | A change under `.github/workflows/` carries a case seen red, a failure direction, a prompt budget (none is added here), platform honesty, and what it removes (`## Removes` below) |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file* | The changelog entry goes in this directory's `changelog.md` |

**Facts this frame rests on, labelled.**

- The workflow the issue calls `tests.yml` is `.github/workflows/test.yml`, whose `name:` is `tests` (read, `test.yml:1`).
- `chain_check.py` is the only script a workflow runs that reads draft state (read: a `git grep` for `isDraft` and `"draft"` across `skills/*/scripts/`, `.github/scripts/`, `hooks/` and `bin/` finds only `chain_check.py:695-754`). `hygiene.yml:183` is the only workflow step that runs it (read).
- Neither `test.yml` nor `hygiene.yml` declares `concurrency:` (read, `git grep concurrency .github/`).
- `test.yml:276` (`release-report`) looks up the release tag's own `push` run on `main`. A `push` run on `main` must therefore never be cancelled (read).
- The sealer reads the pull request body by `gh pr view <N>` (`agents/sealer.md:67`), or from a file where no remote exists (`:38-39`). #990's sealer already read the body from a file, `976-pr.md` (read: `seal/specs/1792363231-a-local-mode-work-item-draws-no-stamp/guarantee.md:36-37`).
- The owner reports that this release's run followed the old rule once (#982, #983) and that #987, #989 and #990 ran the new way. The owner said this in the spawn prompt, and this frame did not open those runs.
- The issue's CI figures are #943 §1's numbers: 36 runs, 46–63 machine-minutes each, about 7,000 Linux-equivalent minutes. The issue is the source, and this frame did not re-measure them.

## Scope

**In.**

1. **Part 2, the workflows.** `test.yml`'s `pull_request` trigger drops the two draft events and the paragraph above `types:`. `hygiene.yml` keeps both events, and its comment keeps the reason (`chain_check.py` excuses a draft, so leaving draft state has to re-run it) but stops telling anyone to open a draft. `tests/test_ci_gives_the_checks_what_they_need.py` requires the draft events on a workflow **if and only if** it runs `chain_check.py`, so the reader is named once and the requirement follows the fact. The module docstring stops describing a draft as the normal state of an unfinished review.
2. **Part 1, concurrency.** `test.yml` and `hygiene.yml` each declare a `concurrency` group keyed on the pull request, with `cancel-in-progress` for `pull_request` events. A `push` to `main` and a `workflow_dispatch` are never cancelled. One case holds this.
3. **Part 1, the rule, rewritten in place.** It has one owner, `skills/code-review/orchestration.md`, in the section now headed *Orchestrator: the pull request opens before round 1, and a phase is re-run*. The heading becomes *Orchestrator: the pull request opens once the sealer has sealed, and a phase is re-run*. The second half stays, because the section's paragraph at `:301-309` (*A hand-back's verification claim is a claim*) is the re-run it names. The owner states:
   - push the branch freely, since a branch with no pull request runs nothing;
   - the pull request opens ready after `guarantee.md` reading `sealed` is committed, and CI runs then and on every later push;
   - a change whose risk is platform-specific (line ends, the shell, a Python version) is pushed after the build's last phase closes and runs `gh workflow run tests --ref <branch>`, and the orchestrator reads that run's result before its broad run;
   - **the stated limit**: a defect one platform alone shows is found when the pull request opens, after the sealer. Its fix is a commit outside the records, so it takes the repair path the section already has: a verifying round, the broad run again, and the sealer again. Nothing new is built for it;
   - a repository that still opens a draft is not refused, because `chain_check` prints on a draft and `hygiene`'s `ready_for_review` re-runs it. This sentence replaces the #296 paragraph.

   Every carrier that cites the heading or states the old order is rewritten in the same commit:
   - `skills/implement/orchestration.md` step 2 (`:37-42`) and the acts-table row at `:639`;
   - `skills/verify/SKILL.md:403-404`;
   - `agents/sealer.md`: spawned before the pull request exists, and the prompt names a file holding the pull request body;
   - `docs/the-broad-gate.md:5`;
   - `CONTRIBUTING.md` §*Opening a pull request*, in one contributor-facing paragraph that links to the owner;
   - the owner section's own sentences at `:209` (*keeps the pull request a draft*), `:267` (*before the pull request is marked ready*) and `:289` (*leave the pull request as a draft*);
   - `skills/verify/scripts/broad_gate.py:3083`, the printed line *commit it before the pull request is marked ready*. That line is text a person reads (contract §14).
   - the tests that pin any of the above.

**Out, each with its reason.**

- **#943 §3, which legs a pull request runs.** It moved to #984 in 0.22.3 (owner, 2026-10-19).
- **`skills/code-review/scripts/chain_check.py`'s draft handling.** It stays unchanged. Other repositories run `templates/hygiene.yml` and may open drafts, and for them the draft excuse with `ready_for_review` re-running the check is what keeps a draft from being a permanent way past the check. It is also #985's file in this release.
- **`docs/the-review-record.md`**, which belongs to #985. Its draft sentences (`:152`, `:254`) describe what the check does, and that stays true.
- **`skills/implement/orchestration.md:381` and `:416`**, which belong to #968. Nothing this work changes is on those lines.
- **`templates/hygiene.yml`.** It keeps its draft events, as the issue says. Its comment describes draft behaviour rather than prescribing a draft, so it stays true. It gets no `concurrency` block either, because #943 is about this repository's minutes and the template is what other repositories run.
- **`README.md:204`, `:605`, `README.ko.md` and `docs/the-review-and-parity-arms.md:100`.** Each describes what `chain_check` does on a draft. That behaviour stays, so the sentences stay true. The sweep found no README sentence stating the old order (read: a flattened search for *opens before round 1*, *as a draft*, *marked ready* and *Ready for review* over `README*.md`).
- **`.github/scripts/gather_changelog.py:10`** already says "before the pull request opens", which agrees with the new order.
- **The other three workflows** (`close-issues-on-release`, `label-merged-on-release-branch`, `publish-release`) run on `push` only (read, their `on:` blocks), so neither case touches them.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 `tests` ignores draft state | Given `test.yml`, when a draft is marked ready, then `tests` does not start, because its `pull_request` trigger names neither draft event | `test_ci_gives_the_checks_what_they_need.py`, the rewritten draft-events case; seen red by putting the two events back into `test.yml` |
| S2 the reader of draft state keeps its events | Given a workflow whose steps run `chain_check.py`, when it lacks either draft event, then the case fails naming it. A workflow that does not run it fails when it lists one | the same case; seen red by deleting `ready_for_review` from `hygiene.yml`, and separately by leaving it in `test.yml` |
| S3 a newer run cancels an older one | Given `test.yml` and `hygiene.yml`, each declares `concurrency` with a group keyed on the pull request and `cancel-in-progress` true for `pull_request` events. A workflow that also runs on `push` does not cancel unconditionally | a new case in the same module; seen red by deleting the block from one workflow, and by writing `cancel-in-progress: true` in `test.yml` |
| S4 the owner states the new rule | Given `skills/code-review/orchestration.md`, the renamed section opens with the sentence `The pull request opens ready, once the sealer has sealed, and CI runs then.` and states the `workflow_dispatch` step and the stated limit | `test_the_rules_have_one_owner.py`, rule 6 rewritten to that sentence; seen red with the sentence deleted |
| S5 the order has no draft | Given `skills/implement/orchestration.md` step 2, it reads smith → warden rounds → preflight → broad run → sealer → the pull request opens, naming the owner section, and holds no `draft` | `test_the_rules_have_one_owner.py`, the order case rewritten (it replaces `test_the_order_opens_the_draft_between_the_build_and_the_rounds`); seen red against the current step |
| S6 every citation names the new heading | Given the heading rename, every carrier and test quoting the old title quotes the new one, and the acts table has the row | `test_every_orchestrator_act_names_its_delivery.py`, `test_a_parallel_agent_names_its_scratch_after_the_work_item.py`, `test_broad_gate_rule.py`, `test_the_stamp_reaches_the_person_it_is_drawn_for.py`, rule 6's links; and `git grep -n "opens before round 1"` returns nothing outside `seal/specs/`, `.test_durations` and the changelog |
| S7 no shipped sentence tells an orchestrator to open or keep a draft | Given the owner section, a non-`sealed` verdict and a `Broad gate` row refusal each say to open no pull request | `test_the_broad_gate_row_is_asked_for_and_runs_as_written.py:578` repointed to the new sentence; seen red against the old |
| S8 the sealer is spawned before a pull request exists | Given `agents/sealer.md`, its description and its read list say the prompt names a file holding the pull request body, and they no longer say "once per ready pull request" | a case asserting both, in `tests/test_the_sealer_guarantees.py` or the module the builder finds already reading `agents/sealer.md`; seen red against the current file |
| S9 the broad run's printed line names no draft | Given a green `broad-gate --record` with `broad-gate.md` uncommitted, the printed line tells the reader to commit it without "marked ready", and stays true for a pull request already open and for a repository that opens drafts | the two pins in `test_the_seal_is_taken_once_by_the_sealer.py` (`:3133`, `:3223`) moved to the new text; seen red against the old string |
| S10 a contributor reads the same rule | Given `CONTRIBUTING.md` §*Opening a pull request*, it says to open the pull request when the work is done, ready, because every push to one runs the suite on three platforms, and it links to the owner | rule 6's links gain `CONTRIBUTING.md` |

## Data & interfaces

The concurrency block, as the build writes it into both workflows. `cancel-in-progress` reads `true` in `hygiene.yml`, which runs on `pull_request` alone:

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: ${{ github.event_name == 'pull_request' }}
```

`test.yml`'s trigger after the change is `pull_request:` with no `types:` list, so it runs on GitHub's default set (`opened`, `synchronize`, `reopened`). A one-line comment beside it says nothing here reads draft state and points to `hygiene.yml`, which does.

## Rule changes

- nothing
  why: written outside docs/: the pull request opens ready, in
    skills/code-review/orchestration.md and the workflows' own comments.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| `ready_for_review` and `converted_to_draft` in `tests`' trigger | `.github/workflows/test.yml#"types: [opened, synchronize, reopened, ready_for_review, converted_to_draft]"` | Nothing in `test.yml` reads draft state. Marking a draft ready re-ran the whole suite on the same commit (#943 §2, PR #937) |
| The paragraph copied from `hygiene.yml` | `.github/workflows/test.yml:7-13` | `hygiene.yml`'s own comment, the workflow it is true of |
| The instruction to open a draft while a review runs | `.github/workflows/hygiene.yml:7-11` (*Open the pull request as a draft … Two clicks, no commit.*) | The reason stays in the same comment. The order is the owner section's |
| The case's requirement on every `pull_request` workflow | `tests/test_ci_gives_the_checks_what_they_need.py#test_a_pull_request_workflow_reruns_when_a_draft_becomes_ready` | The same case, narrowed to workflows that run `chain_check.py` |
| The old rule and its measurement | `skills/code-review/orchestration.md#"The draft pull request opens at the end of the build, before round 1."` through `:165` | Replaced in place by the new rule. The measurement it argued from (three Windows-only defects after round 12) stays in git history |
| The #296 paragraph | `skills/code-review/orchestration.md#"That window used to be red and is not any more (#296)."` (`:167-176`) | One sentence in the same section: a draft is still tolerated. The window it described does not occur in the new order |
| The old heading | `skills/code-review/orchestration.md#"Orchestrator: the pull request opens before round 1, and a phase is re-run"` | The new heading. Every citation is repointed in the same commit (S6) |
| "the draft goes ready", "keeps the pull request a draft", "leave the pull request as a draft until they have", "before the pull request is marked ready" | `skills/code-review/orchestration.md:178-179`, `:209-210`, `:267`, `:289` | Each sentence rewritten to the new order where it stands |
| "→ the draft pull request opens (…)" and "the pull request is marked ready" | `skills/implement/orchestration.md:37-42` | The same step, reordered, naming the owner |
| "Spawn once per ready pull request" and `gh pr view <N>` as the body's only source | `agents/sealer.md:4`, `:67` | The same lines: the body comes from the file the prompt names |
| "before a pull request is marked ready" | `docs/the-broad-gate.md:5` | The same sentence: "before the pull request opens" |
| "commit it before the pull request is marked ready" | `skills/verify/scripts/broad_gate.py#CELL_UNCOMMITTED` | The same line in new wording (S9) |
| Rule 6's owner sentence and link, `test_the_order_opens_the_draft_between_the_build_and_the_rounds`, and `test_the_release_leg_is_no_longer_red_until_round_ones_record_commits`'s #296 assertions | `tests/test_the_rules_have_one_owner.py:43-46`, `:76-80`, `:161-190` | Rewritten to the new sentences (S4, S5). The draft-tolerance sentence keeps one assertion pair |
| The old string in two pins | `tests/test_the_seal_is_taken_once_by_the_sealer.py:3133`, `:3223`; `tests/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py:578` | The new strings |

## Open questions → questions.md

Anything a planner must answer lives in questions.md, not inline — unanswered
questions buried in prose read as decided.

Framed 2026-10-19 by framer, before the build.
