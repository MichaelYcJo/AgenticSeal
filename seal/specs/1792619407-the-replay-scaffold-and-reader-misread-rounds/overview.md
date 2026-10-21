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
| The mask sets a host one space after a control character | `spec.md` *Data & interfaces*: `report_text` is "verbatim apart from the masking of `questions.md` Q4". Code: also one space after a control character wherever a host would follow it | code | A side writes the record as one JSON string, and the scan reads the escape's letter as the host's first, so `example.com` after a line break is refused as `nexample.com`. No `location:` line or heading opens with a host, so no row changes (phase 1 record) |
| S13's `git grep` finds two lines | S13: "`git grep -n -e report_rows -e FINDING_ROW -- ':!seal'` finds nothing". Code: two lines of `tests/test_a_rewritten_definition_proved_non_inferior.py` name `report_rows` | code | One asserts a side no longer carries it (S6), and one builds a side as a run before #986 kept it (S7). A case for the refusal has to name what it refuses |

## Not verified

| Item | Who must answer |
|---|---|
| The suite as a whole, the repository-wide lint and the typecheck at this branch's head | the orchestrator, at its one broad run |

## Not done

nothing

## Fed back into the spec

none
