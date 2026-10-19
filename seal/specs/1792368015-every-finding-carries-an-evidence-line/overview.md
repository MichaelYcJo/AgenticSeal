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
| The warden's side is not shown not worse | `spec.md` S12 asks `noninferiority.py compare` to read `pass`, or a fail to stand under `questions.md` Q1, which covers a fail on rule 5 alone. The side at ba2a3187 fails rules 1 and 2: recall 19 to 13, false rate 0.558 to 0.641 (executed by the orchestrator, `evals/warden-phase-3.md`) | the fail stands as recorded, and the item ships with no second side | The owner, 2026-10-19: "노이즈로 기록하고 출시". The diagnosis in `phases/phase-3.md` grounds it: the baseline's 19 is the highest of six sides on af9c924b, the `replay-1791382684-r2` loss traces to the verifying-round rule this item did not change, and the other two drops were 0 of 2 on earlier sides too |
| Whether anything reads a merged record again (round 1) | `spec.md:48` "No check reads such a record again"; `plan.md:120` and `:138` say the same. Round 1's finding 1 showed two readers do: `release_seal.py#chain_counts` and `replay_targets.py` | `docs/the-review-record.md` names both readers and says the check judges no merged record at a pull request again (e4837c2b); the frame's sentences stay as the frame wrote them | the check's own reading at a pull request is what the frame's sentences meant, and it holds; the two other readers are named where the rule lives, and the frame is not rewritten after the build |

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the typecheck at the build's last commit | the orchestrator's `broad-gate --base release/v0.22.2 --record <item>` at 58a2100e, exit 0: 7598 passed, 14 skipped, chain exit 0 (`broad-gate.md`); the run at 12660916 failed on the encoding census, fixed at ffed3c38 and reviewed in round 3 |
| closed Whether the warden writes the line on every finding and keeps earlier records' missing lines out of its findings (`questions.md` Q4) | phase 3's side at ba2a3187: all 39 findings of its 18 records carry the line, 28 of them `executed`, and none raises a record written before the row (executed, `phases/phase-3.md`) |
| Whether a line-bounded search, which the absence rule asks for, costs finds in general: `traces/005.jsonl:153` of phase 3's raw output missed a phrase wrapped across two lines | a later warden measurement on #971's suite, after 0.22.2, scheduled by the orchestrator |
| closed Whether `replay_targets.py` losing every labelled record written before the row is accepted, as Q2 accepted the release panel's `not read` | the owner answered on 2026-10-19 that each record is read with the grammar of its own time. Built in 0a843334, and `--list` names 31 targets again (executed) |

## Not done

nothing

## Fed back into the spec

none
