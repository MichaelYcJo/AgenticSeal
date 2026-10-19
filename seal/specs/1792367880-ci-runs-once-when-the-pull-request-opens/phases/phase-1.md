# 1792367880-ci-runs-once-when-the-pull-request-opens — phase 1

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 34d1533d |


## What this phase was asked

Build S1 to S3 of `spec.md`. In `.github/workflows/test.yml`, drop the two
draft events and the paragraph copied at `:7-13`. Keep a `pull_request:`
trigger with no `types:`, and add a `concurrency` block that cancels a run in
progress only for `pull_request` events. A push to `main` is never
cancelled, because `release-report` reads it. In
`.github/workflows/hygiene.yml`, keep the draft events and the reason for
them, remove only the instruction to open a draft, and add the same block. In
`tests/test_ci_gives_the_checks_what_they_need.py`, rewrite the draft-events
case so that a workflow which runs `chain_check.py` carries the two events
and one which does not carries none. Add the concurrency case, and fix the
module docstring. Each case is seen red first. The spawn named four places
not to touch: `chain_check.py`, `docs/the-review-record.md` (#985's),
`agents/sealer.md` (phase 2, held) and `skills/implement/orchestration.md:381`,
`:416` (#968's). None of them was touched.

## What this phase found

**The frame holds except for the concurrency group's fallback, and it missed
one sentence.**

- **The spec's group would hold and cancel pushes to `main`.** `spec.md`
  §*Data & interfaces* keys the group on
  `github.event.pull_request.number || github.ref`. GitHub keeps one pending
  run per concurrency group and cancels any older pending run, whatever
  `cancel-in-progress` says. The default `queue: single` behaves this way
  (read: docs.github.com, *Control the concurrency of workflows and jobs*,
  2026-10-19). With `github.ref` as the fallback, every push to `main` shares
  one group. The second push's run would wait behind the first, and a third
  push would cancel it while it waited. That breaks the guarantee
  `plan.md` rested on, that a push to `main` is never cancelled. The build
  falls back to `github.run_id`, the fallback GitHub's own example uses. A
  run that is not a pull request's therefore always has a group of its own.
  The concurrency case requires the fallback in a workflow that runs on any
  other event. `cancel-in-progress` still reads
  `${{ github.event_name == 'pull_request' }}` in `test.yml`, as the spec
  says, so that changing the group back alone does not cancel a push run.
- **The group names the workflow, and the case requires it.** A concurrency
  group is shared by the whole repository. Without `github.workflow` in it,
  one pull request's `tests` and `hygiene` runs would cancel each other.
- **`hygiene.yml:176-177` also stated the old order.** "A review still running
  opens its pull request as a draft" was in the comment above the
  `chain_check.py` step, and `spec.md` §*Removes* names only `:7-11`. The
  build rewrote it to "On a draft every refusal prints and none fails". That
  keeps what the check does and drops the order. This is a removal the frame
  did not name, so `overview.md` records it.
- **The cases key on facts in the workflow, not on a list of names.** A
  workflow "reads draft state" when its comment-stripped text names
  `DRAFT_READER`, `chain_check.py`. A workflow owes the concurrency block when
  its `on:` block has a `pull_request` key. Only where `pull_request` is the
  sole event may `cancel-in-progress` read `true`. Three helpers do the
  reading: `top_level`, `events` and `concurrency`. They read the `on:` block
  by indent, so the trigger is no longer sliced from `pull_request:` to
  `jobs:`. That old slice would now have included `workflow_dispatch:` and
  the concurrency block.
- **How each case was seen red.** Both new cases failed against the tree as
  it stood (executed). `test.yml` listed `ready_for_review` without running
  `chain_check.py`, and `hygiene.yml` declared no `concurrency:`. After the
  commit, `mutation-check` ran eleven mutations (executed), and the cases
  caught every one:
  - the draft events put back into `test.yml` (S1);
  - `ready_for_review` deleted from `hygiene.yml` (S2);
  - the block deleted from `hygiene.yml` (S3);
  - `cancel-in-progress: true` written in `test.yml` (S3);
  - the fallback changed to `github.ref`;
  - `github.workflow` taken out of the group;
  - `cancel-in-progress: false` in `hygiene.yml`;
  - each of the three helpers broken;
  - `DRAFT_READER` renamed.
- **For phase 2.** The sweep `plan.md` gives phase 2 includes
  `.github/workflows` in its `git grep` for "as a draft" and "marked ready".
  After this phase that grep finds nothing in the workflows, so every
  remaining hit lies outside them.
