# 1792619407-the-replay-scaffold-and-reader-misread-rounds — overview

## Why this work exists

The warden's measured false-finding rate counted fenced lines as findings
and seeded cases built on a tree that cited records and commits the clone
lacked; a side now keeps its record and is read by the check's own split,
and a seeded case is the tree its work item's round 1 reviewed.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Which `truth-` graders are read from the finding rows | Spec scope item 3: "a `truth-` grader's result for a run is its regex searched over that run's finding rows". Code: only a `truth-` grader whose target path ends as a round record's does (`noninferiority.py#reads_record`); any other keeps the eval's result | code | The spec's Out item: "The other agents' suites ... their case directories do not change", read as their numbers too. The sealer's four `truth-` graders read `guarantee.md` (`evals/behaviour/sealer/rule-sealer-false-red/graders/truth-false-red.md`), which no run prints as a record, so read from the rows each would fail on both sides |
| The identifier scan's predicate moved into named functions | `questions.md` Q4: "loading the patterns from their one home". Code: the allow logic stood inline in `domains_in` and `user_paths_in`, so it moved into `refused_domains` and `refused_user_paths` in `tests/test_no_real_identifiers.py`, which both walks and `noninferiority.py#masked` call; `FIXTURE_DOMAIN` names the fixture host | code | Loading the patterns alone would have left the mask to restate the allow logic beside them, which is the copy Q4 forbids |
| The mask sets a host one space after a control character | `spec.md` *Data & interfaces*: `report_text` is "verbatim apart from the masking of `questions.md` Q4". Code: also one space after a control character wherever a host would follow it | code | A side writes the record as one JSON string, and the scan reads the escape's letter as the host's first, so even the fixture host is refused where it opens a line. No `location:` line or heading opens with a host, so no row changes (phase 1 record) |
| Nothing in the clone holds the build without the seed | `plan.md` *Summary*: "nothing in the clone holds the build without the seed". Code: the amend rewrites the target commit alone, so every branch commit before it holds the seeded line unmutated, and `git diff HEAD^ HEAD` in each of the four clones shows the seeded file changed by one line inside a records-only commit (phase 2 record) | spec, as far as the frame's own checks reach; the residue is a question for a person | S10's checks all hold. No seed avoids the residue for these four, since each target's last commit adds no Python line. Choosing between the leak, the dangling citations of the old scaffold, and another design is the owner's |
| A base ref deleted after its release | `spec.md` scope item 5: round 1's base read "through the readers `replay_targets.py` already uses". Code: those readers find no base where the ref no longer resolves, and three of the four round 1 records name `origin/release/v0.21.0`, which the remote no longer has; `replay_targets.py#ref_base` lets the squash commit's first parent stand for it | code | A squash puts none of the target's commits on the release branch, so the merge-base with any later state of it is the fork the ref named. The replay generator passes no landing commit and is unchanged (S12) |
| The per-round reader moved into `replay_targets.py#round_target` | `plan.md` phase 2 names `seed_defects.py` alone. Code: the body of `replay_targets.py#targets` became `round_target`, which both generators call | code | `CLAUDE.md` *The rule a mechanism is kept against*: a fact has one source. A second copy in `seed_defects.py` would read either record shape a second way. The replay cases regenerate unchanged (S11, S12) |
| Two seeded cases replaced | `spec.md` scope item 8 regenerates `seeded-4d316179` and `seeded-9b644676`. Code: `seeded-4d316179` takes no seed at round 1's target, and two of `seeded-9b644676`'s round 1 truths accept one `location:` line; `seeded-8a100e13` and `seeded-f1c9932d` replace them | code | `questions.md` Q3's default: "Replaced by the next smallest that builds". The generator now leaves out a commit whose truths share a line (`seed_defects.py#shared_line`) instead of writing a case the suite refuses |
| S13's `git grep` finds two lines | S13: "`git grep -n -e report_rows -e FINDING_ROW -- ':!seal'` finds nothing". Code: two lines of `tests/test_a_rewritten_definition_proved_non_inferior.py` name `report_rows` | code | One asserts a side no longer carries it (S6), and one builds a side as a run before #986 kept it (S7). A case for the refusal has to name what it refuses |

## Not verified

| Item | Who must answer |
|---|---|
| The suite as a whole, the repository-wide lint and the typecheck at this branch's head | the orchestrator, at its one broad run |
| Whether a warden finds the seed through `git diff HEAD^ HEAD` more often than through the build, which only a paid run reads | the repository owner, with `questions.md` Q1 |

## Not done

nothing

## Fed back into the spec

none
