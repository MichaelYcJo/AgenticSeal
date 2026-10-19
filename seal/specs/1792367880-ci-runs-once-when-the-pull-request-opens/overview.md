# 1792367880-ci-runs-once-when-the-pull-request-opens — overview

<!-- The closing memo (implement skill, step 4). Not a summary of the work:
`git diff --stat` holds the file list and the diff holds the detail. Only what
the diff cannot show goes here, and each part is written when it happens rather
than reconstructed at the end. A rule that must outlive this work item goes
to its home under `docs/` with the test that holds it, not here. -->

## Why this work exists

Each pull request paid for CI more than once: marking a draft ready re-ran the whole suite on a commit it had already run, and a new push left the previous commit's runs going. After this work, CI runs when the pull request opens and on each later push.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The concurrency group's fallback (phase 1) | `spec.md` §*Data & interfaces*: `group: ${{ github.workflow }}-${{ github.event.pull_request.number \|\| github.ref }}`. The code falls back to `github.run_id` | code | GitHub's docs say "any existing `pending` job or workflow in the same concurrency group will be canceled" under the default `queue: single`. With `github.ref`, pushes to `main` share one group, and a third push cancels the second push's run while it waits. `plan.md` §*Alternatives considered* rests on that run never being cancelled, because `release-report` reads it |
| `hygiene.yml:176-177` (phase 1) | `spec.md` §*Removes* names `hygiene.yml:7-11` as the one draft instruction. `:176-177` said "A review still running opens its pull request as a draft" too, and the code rewrote it to "On a draft every refusal prints and none fails" | code | `spec.md` §*Scope* item 1: hygiene's comment "stops telling anyone to open a draft". The sentence at `:176-177` stated the old order, and what the check does on a draft stays stated |
| The owner section's heading (phase 2) | `spec.md` §*Scope* item 3: *Orchestrator: the pull request opens once the sealer has sealed, and a phase is re-run*. The code titles it *… opens once the sealer seals, and a phase is re-run* | code | The frame's heading is 89 columns as a Markdown line, and `tests/test_docs_line_wrap.py` holds `skills/code-review/orchestration.md` to 88. A heading cannot wrap. The S4 rule sentence keeps "once the sealer has sealed" |
| The sealer's spawn sentence in the owner section (phase 2) | `spec.md` §*Removes* names `agents/sealer.md:4`, `:67` and none of the owner section's spawn sentence. The code rewrote "the issue and the pull request" to "the issue and the file holding the pull request body" | code | `spec.md` §*Scope* item 3: the sealer is "spawned before the pull request exists, and the prompt names a file holding the pull request body". The orchestrator's spawn sentence is where that prompt is written |
| The framer route's `chain: reframed` label (round 1) | `spec.md` names neither the label step in `skills/code-review/orchestration.md` nor its paragraph in `docs/issues-and-milestones.md`; round 1's finding 1 showed the step runs mid-round, when no pull request exists under the new rule. The fix pass removed both (95ab5fd0) | code | nothing reads the label: no workflow, script or case (`git grep`), so moving it to the pull request's opening would keep a step that decides nothing; `CLAUDE.md`'s subtraction rule. The changelog fragment names the removal |
| `agents/sealer.md` cut by 302 bytes (round 1) | `spec.md` changes three sentences of the sealer and names no cut | code | the sealer side at 62c38876 failed rule 4 (preload 117 bytes longer, `evals/sealer-phase-3.md`); the fix pass removed three restatements, none a rule the sealer acts on (round 2 confirms), and the side at 95ab5fd0 passes rule 4 |

## Not verified

| Item | Who must answer |
|---|---|
| GitHub runs `hygiene` and not `tests` when a draft is marked ready, a second push cancels the first push's `tests` and `hygiene` runs, and a push to `main` is neither held nor cancelled | the orchestrator, by `gh run list --branch <branch>` on this work item's pull request (`questions.md` Q1) |
| closed The sealer's definition changed in three sentences (`phases/phase-2.md` names them), and its behaviour on the five-case suite was not measured | measured by the orchestrator twice against #976's side: at 62c38876 fail on rule 4 alone, at 95ab5fd0 fail on rule 5 alone by 0.9% with all 68 graders passing, recorded and shipped under the owner's rule for a rule-5-only fail (`evals/sealer-phase-3.md`, `evals/sealer-phase-3b.md`, `changelog.md`) |

## Not done

Nothing.

## Fed back into the spec

None.
