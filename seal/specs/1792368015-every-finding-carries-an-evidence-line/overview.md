# 1792368015-every-finding-carries-an-evidence-line — overview

<!-- The closing memo (implement skill, step 4). Not a summary of the work:
`git diff --stat` holds the file list and the diff holds the detail. Only what
the diff cannot show goes here, and each part is written when it happens rather
than reconstructed at the end. A rule that must outlive this work item goes
to its home under `docs/` with the test that holds it, not here. -->

## Why this work exists

A finding's claim now names what it rests on, on one `evidence:` line the
check refuses a finding without, so a claim nobody checked against the tree
stops at the pull request instead of reaching a release.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Where the S10 sentence stands | `spec.md` §*Scope* item 2 lists four parts of one paragraph in §*The round record*, the last "a record written before the row lacks the line, and that is no finding". The build put that part in §*What the check reads at the pull request*, in the paragraph item 3 rewrites, and gave the other three parts paragraphs of their own in §*The round record* | the build | The record-before-the-row sentence and the in-flight rule are one fact, which records the check reads again. One paragraph per rule also lets each carry its own `Enforced by:` line: the absence rule's is `nothing`, which cannot share a line with a case |
| A sixth reader the plan's reader table does not name | `plan.md` §*Technical context* lists five readers of round records. `evals/scripts/replay_targets.py#labelled_round` is a sixth: it reads every labelled record in the working tree and the last two release tags through the tree's `chain_check.round_of`, and leaves out a record the check refuses. With the row, every labelled record written before it is refused, and `replay_targets.py --list` lists 13 targets with truth where it listed 31 (executed, before and after the row) | left unchanged, and raised for a person | A reader that skips the missing line is a second statement of the grammar, which `docs/the-review-record.md` §*The round record* refuses and `questions.md` Q2 rejected for `release_seal.py`. Whether this loss is accepted the way Q2 accepted the panel's is the owner's, and the hand-back of phase 1 names it |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck at the build's last commit | the orchestrator's `broad-gate` run |
| Whether the warden writes the line on every finding and keeps earlier records' missing lines out of its findings (`questions.md` Q4) | phase 3's paid side, scheduled by the orchestrator |
| Whether `replay_targets.py` losing every labelled record written before the row is accepted, as Q2 accepted the release panel's `not read` | the owner |

## Not done

nothing

## Fed back into the spec

none
