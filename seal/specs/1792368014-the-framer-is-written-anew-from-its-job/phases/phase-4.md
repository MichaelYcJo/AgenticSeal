# 1792368014-the-framer-is-written-anew-from-its-job — phase 4

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 5cfc4c3e |


## What this phase was asked

Close the work on the records. The tasks were:

- write `changelog.md` with the framer's row in #967's shape;
- compare the read set's sha256 at the branch head with the measured
  commit before the pull request;
- close `overview.md`.

Phase 3 does not run, because phase 2 passed, so this phase follows
phase 2 directly.

## What this phase found

**The read set at the branch head is the read set that was measured**
(`executed`). Each file was hashed with `git show <rev>:<path> | shasum -a
256`, at the measured commit b434e145 and at 5cfc4c3e. These are the seven
files every run reads, and the four a frame opens where it calls for them.

| File | b434e145 | 5cfc4c3e |
|---|---|---|
| `agents/framer.md` | `f70b2eb37f0e` | `f70b2eb37f0e` |
| `skills/agent-contract/SKILL.md` | `642b0da67c67` | `642b0da67c67` |
| `skills/implement/SKILL.md` | `dbff9bdf37f2` | `dbff9bdf37f2` |
| `skills/writing-style/SKILL.md` | `5e1a12a78c70` | `5e1a12a78c70` |
| `templates/sdd-spec.md` | `19d19fbc928c` | `19d19fbc928c` |
| `templates/sdd-plan.md` | `ac33400f75b8` | `ac33400f75b8` |
| `templates/sdd-questions.md` | `a4c7561e9e6e` | `a4c7561e9e6e` |
| `skills/confidence-check/SKILL.md` | `dc082bb4599b` | `dc082bb4599b` |
| `skills/feature-planner/SKILL.md` | `26b36ddb43d0` | `26b36ddb43d0` |
| `templates/config.md` | `bedc01bb3349` | `bedc01bb3349` |
| `docs/the-review-record.md` | `fbed2e753399` | `fbed2e753399` |

`docs/the-review-record.md` §*The run* hashes `204f7f6e3fd0` at both
commits. `origin/release/v0.22.2` stands at 2ff7b963, which HEAD already
contains (`git merge-base --is-ancestor`, exit 0). So no merge or rebase is
owed before the pull request, and no re-measure is owed (S12, Q2).

**The fragment's figures equal the record's** (`executed`, the rows of
`evals/framer-phase-2.md` at 5dc581c9).

- Preload bytes: 86353 → 26027.
- Tokens per tool call: 29894.6 → 17190.9.
- Spend USD: 16.1196 → 14.7490.
- Tool calls: 109 → 172.
- Tokens read, every model: 3258508 → 2956842.
- Graders: 64 of 64 on both sides.
- Verdict: `pass`.

`tests/test_the_changelog_is_gathered_at_release.py` exits 0 with the
fragment in place (`executed`).

**`overview.md` is closed** (`executed`,
`bin/unverified-check --baseline 4403c194`, exit 0). The eval-side row is
marked `closed` with phase 2's commit. One row stays open: the full suite,
the lint and the typecheck, which the orchestrator's broad gate answers.
Three divergence rows were added: the two merges, the emptied exemption
with the preload case, and the check phase 1 turned red. `## Not done`
names the replace-or-keep grader that `questions.md` Q5 holds for the
owner.

**Addendum: review round 1's fix pass (5bdad9db).** Round 1 found three
`should`s, and 5bdad9db fixes all three in `agents/framer.md`, with a pin
for each.

- Step 4's two reading rules are restored.
- The reframe rule gains the clause *new phase rows for the redesign, every
  closed phase keeping its commit*.
- Step 8 labels what a command gave `executed`.

Each pin was seen red on the definition before the fix and turned red again
under a `mutation-check` of its sentence (`executed`).

`bin/payload-meter --agent framer` now reads 10,001 bytes for
`agents/framer.md`, against 9,424 at b434e145, and 16,603 for the contract.
So the fix adds 577 bytes, and the preload that ships is 26,604 bytes
(`executed`). The orchestrator decided not to take a second side, under the
owner's word that a side is not run again for the measurement alone. The
measured side stays b434e145, and the changelog row says the fix was not
re-measured. The rest of the read set is as the table above records it.
