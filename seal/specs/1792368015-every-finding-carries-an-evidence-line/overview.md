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
| A sixth reader the plan's reader table does not name | `plan.md` §*Technical context* lists five readers of round records. `evals/scripts/replay_targets.py#labelled_round` is a sixth. It read every labelled record in the working tree and the last two release tags through the tree's `chain_check.round_of`, and left out a record the check refused. With the row, every labelled record written before it was refused, and `--list` named 13 targets with truth where it had named 31 (executed, before and after the row). Phase 1 left it unchanged and raised it for the owner | each record is read through the `chain_check.py` of the commit that last wrote it (0a843334, 0a5d3445), and `--list` names the same 31 targets as before the row (executed) | The owner, 2026-10-19: "read each record with the grammar of its own time". Each record is judged by the grammar in force when it was written, which is not a second grammar. The owner's example was the release tag a record shipped in. The build reads the commit that last wrote the record instead. v0.22.2's items have records in the tree and no tag yet, and v0.22.2's tag will hold the `evidence:` row, so judging those records at that tag would refuse them. `release_seal.py` is unchanged, under Q2 |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck at the build's last commit | the orchestrator's `broad-gate` run |
| Whether the warden writes the line on every finding and keeps earlier records' missing lines out of its findings (`questions.md` Q4) | phase 3's paid side, scheduled by the orchestrator |
| closed Whether `replay_targets.py` losing every labelled record written before the row is accepted, as Q2 accepted the release panel's `not read` | the owner answered on 2026-10-19 that each record is read with the grammar of its own time. Built in 0a843334, and `--list` names 31 targets again (executed) |

## Not done

nothing

## Fed back into the spec

none
