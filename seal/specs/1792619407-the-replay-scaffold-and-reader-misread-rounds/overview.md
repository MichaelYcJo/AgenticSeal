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
| The mask sets a space beside an escape the scan refuses in the side's JSON form | `spec.md` *Data & interfaces*: `report_text` is "verbatim apart from the masking of `questions.md` Q4". Code: also one space beside each character the side's JSON writes as an escape, where the scan's own functions refuse a host or a user path in that JSON form and the match takes in part of the escape (`noninferiority.py#apart`) | code | A side writes the record as one JSON string. The scan reads an escape's letter as a host's first, so even the fixture host is refused where it opens a line, and it reads an escape's backslash as a user name, so a user root before a line break or a quote is refused (round 1 finding 3). No `location:` line or heading opens with a host or a user path, so no row changes |
| A seeded clone keeps no remote | `spec.md` scope item 6: the scaffold "fetches the target and the base, removes no file, and leaves no copy of the unmutated commit". Code: it also removes `origin` and writes round 1's base ref again | code | The orchestrator's direction in round 1's fix pass, from the round's Not judged: with `origin` and its default fetch kept, a warden's `git fetch` brings back the release branches, which hold the shipped, unmutated code. The base ref the record names still resolves. What the removal closes and what it leaves is stated once, in `seed_defects.py`'s module docstring. The replay scaffold keeps its remote, since a replay holds no seed and its tree did not change (S12) |
| A seeded scaffold's line check reads a carriage return as the line's end | `spec.md` *Data & interfaces* gives the scaffold's steps and says nothing of line ends. Code: the mutation script compares the checked-out line without a trailing carriage return and keeps it on the mutated line (`seed_defects.py#MUTATE`) | code | The orchestrator relayed `tests` run 39691387210 at 4875eb7b: on a Windows split, `sh scaffold.sh` exited 1 with `a.py:40 is not '    return b != 2'`, because git for Windows checks files out with CRLF line ends and the seed's text, read through git with universal newlines, has none. A real Windows user running a seeded case meets the same refusal. `test_the_seeded_scaffold_mutates_a_line_that_ends_with_crlf` holds both shapes on every platform, an LF file checked out under `core.autocrlf=true` and a file stored with CRLF; each was red against 729cea97 with the same message (executed) |
| Nothing in the clone holds the build without the seed | `plan.md` *Summary*: "nothing in the clone holds the build without the seed". Code: the amend rewrites the target commit alone, so every branch commit before it holds the seeded line unmutated, and `git diff HEAD^ HEAD` in each of the four clones shows the seeded file changed by one line inside a records-only commit (phase 2 record) | spec, as far as the frame's own checks reach; the residue is a question for a person | S10's checks all hold. No seed avoids the residue for these four, since each target's last commit adds no Python line. Choosing between the leak, the dangling citations of the old scaffold, and another design is the owner's |
| A base ref deleted after its release | `spec.md` scope item 5: round 1's base read "through the readers `replay_targets.py` already uses". Code: those readers find no base where the ref no longer resolves, and some round 1 records name a ref the remote no longer has (which ones, `spec.md` scope item 5); `replay_targets.py#ref_base` lets the squash commit's first parent stand for it | code | A squash puts none of the target's commits on the release branch, so the merge-base with any later state of it is the fork the ref named. The replay generator passes no landing commit and is unchanged (S12) |
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
