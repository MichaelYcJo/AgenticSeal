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

## Not verified

| Item | Who must answer |
|---|---|
| GitHub runs `hygiene` and not `tests` when a draft is marked ready, a second push cancels the first push's `tests` and `hygiene` runs, and a push to `main` is neither held nor cancelled | the orchestrator, by `gh run list --branch <branch>` on this work item's pull request (`questions.md` Q1) |

## Not done

Nothing.

## Fed back into the spec

None.
