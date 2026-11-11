# Implementation Plan: 1794383426-eval-code-the-verdict-does-not-read

## Technical context

The tree as read at `887127e61`.

`evals/scripts/noninferiority.py` (1,558 lines) runs the behaviour suite one side at a time (`run`), writes the record two sides give (`compare`), recomputes a record's verdict (`check`) and decides the sealer's model from a record (`model`). `regrade` (lines 1188-1501) and the reader of the proofer's printed round record (lines 234-411, with `side_numbers` at 685-758 calling it) serve recall and the false-finding rate alone. The verdict at lines 782-862 reads neither.

`noninferiority.py` imports `replay_targets` (line 81) for `record_reader` alone, at line 324, inside `finding_rows`. `rule_cases.py` imports it (line 59) for `truths_with` alone, at line 318. So phase 1 removes the first import with the reader it serves, and phase 2 removes the generator once `rule_cases.py` no longer reads it. Each phase leaves the suite whole: phase 1 leaves both generators and their tests standing, and they read nothing phase 1 removes but `grader_from`, which `tests/evals/test_rule_cases.py#truth_regex` then reads from its own module.

`tests/evals/test_rule_cases.py#case_graders` (line 297) reads every rule case's graders through `noninferiority.py#grader_from`, and its *Test_proofer_case*, *Test_sealer_case* and *Test_framer_case* stay. That is why Scope 4 moves the reader rather than deleting it.

The failure scenario of the chosen approach, six months on: a person wants to measure the proofer's recall again, for a model change. Re-cutting a case from a release tag and re-grading a paid side are gone. They take a paid run of the frozen cases and read each truth grader's row in `## Graders`, which the eval graded by its regex over the whole record, a fenced `location:` line included. That count can run higher than the one `finding_rows` gave, and the record no longer says so.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Remove what *Change* names (the generators, `regrade`, `recurred_truths.json` and their tests), move `record_reader` into `noninferiority.py`, and keep `finding_rows`, the row counts and `report_text` | The record still reports the false-finding rate and re-grades recall each run, which the owner stopped reporting. `evals/scripts/` keeps the masking, `apart` and the census import, about 200 lines whose values the verdict does not read, against the issue's first *Done when* line. | Rejected. The owner's decision retires the values, and this keeps their producer. |
| Remove what *Change* names and everything that produces recall or the false rows, by following what reads `report_text`, the row counts and the truth re-grading (chosen) | The failure scenario above. A paid side keeps no printed record in its JSON, so a later reader opens `<out>.raw/`. | Chosen. It meets all three *Done when* lines and leaves the token figures #1254 kept. |
| Read the first *Done when* line literally: also remove spend, tokens, tool calls, seconds, preload bytes and their collection in `run` | `model` loses the spend it decides on, and #1254's decision that the token figures are written is reversed without anyone deciding it. | Rejected. The owner's decision names recall and the false-finding rate, and #1254 kept the rest. |
| Keep `tokens per true find` as a token figure | It divides tokens by the true-find count, which is recall's numerator, so the record keeps reporting recall in another unit. | Rejected. |
| Drop truth rows from the proofer's `## Graders` table as well | `model` reads every grader's row, and the record would need a per-agent filter. The frozen cases still carry their truth graders, which the eval runs whatever `compare` writes. | Rejected. The table lists what the eval graded and computes no rate. |
| Drop `truth-shout-twice-uncovered` from `rule-proofer-one-finding` with `recurred_truths.json` | The proofer's suite tree changes, so `compare` refuses every pair of a side taken before and one taken after (`noninferiority.py#compare`, the suite check), and a new paid baseline is owed. | Rejected. Scope 7 keeps the case's bytes. |
| Keep the generator-text exemption by copying the generators' `prompt` and `scaffold` into the test | A removed generator's text lives on in a test, kept in step with eight cases no one regenerates. | Rejected. The frozen cases are records, as `tests/censuses.py#RECORDED_CASE` already treats them. |
| Keep the frozen cases under the word check with their present hits listed as exemptions | A stored list kept beside the tree, which `skills/core/SKILL.md` *The rule a mechanism is kept against* refuses. | Rejected. |
| Keep `scalar` and `grader_from` in `noninferiority.py` | The script carries code no command calls, read by tests alone. | Rejected; they move to their one reader. Moving them to `behaviour.py`, beside the writer they invert, is equal in cost, and the build may take it where the move to the test module proves awkward, recording why in the phase record. |
| Add a standing case that every rule case equals the generator's output | A new mechanism with no catch on record; the one comparison this work needs is a single executed run. | Rejected. Phase 2 records the run. |
| Keep the test that no two truths accept one location | It guards recall's count against one finding counted twice. With recall not computed and the cases frozen, it guards nothing. | Rejected. |
| Edit `docs/checks/the-pull-request-check.md` in this pull request | This work item's subject is the code, so its policy sentence goes to `## Rule changes` (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*). | Rejected. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope 1, 2, 3, 4, 5 | `tests/evals/test_noninferiority.py` and `tests/evals/test_rule_cases.py`, each changed case seen red first (contract rule 15); S1 with its exit code read directly; S2 to S5 | `7d718955b` |
| 2 | Scope 6, 7, 8, 9, 10, 11, 12 | `tests/evals/test_rule_cases.py`, `tests/behaviour/test_evals_layout.py`, `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py`, `tests/test_censuses.py`; S6 with each case's `diff -rq` recorded in the phase record; S7, S8 and S9 | |

S10 rests on the full suite, which the orchestrator's broad gate runs.

## Overlap with the release

The items read are #1498, #1481, #1483, #1486 and #1488, as the spawn names them; none has a committed frame. #1481 (`skills/settle/scripts/settle.py`) and #1483 (`skills/verify/scripts/broad_gate.py` `PARTITION` and its test) change no file this work changes and read nothing it removes. The items not started, #1482, #1484, #1485 and #1489, were not read.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1498 | `tests/censuses.py`: #1498 changes `#_root_names`; this work changes the module docstring, `#refused_domains`'s docstring, `#OLD_NAME_RECORDS` and `#KEPT_FILES` (Scope 5 and 10) | #1498 | The spawn names #1498 first, as it carries the version move to 0.37.4. The hunks are apart, so this work's merge from the release branch takes #1498's change without a conflict. |
| #1486 | `.test_durations`: #1486 removes the file; this work removes the entries of the cases it deletes (Scope 12) | #1487 | Whichever merges second meets one modify/delete conflict, settled by keeping the deletion, so neither order costs more there. #1487 first leaves the release branch with no dead durations past `STALE_SHARE` while #1486 is open. In the other order Scope 12 drops out, and the phase record says so. |
| #1488 | `tests/behaviour/test_no_two_truths_of_a_proofer_case_accept_one_location.py`, which this work deletes, and `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py`, which this work edits; #1488 counts and removes literal-phrase asserts across `tests/text/` and `tests/behaviour/` | #1487 | #1488 records its counts before and after, and builds after the items that remove their own pins so none is counted twice (#1488 *Done when*). #1487 first removes these files' asserts before #1488 counts them. |

## Operational impact

- `noninferiority.py regrade` is gone. A maintainer who ran it re-grades nothing now.
- A side `run` writes keeps no `report_text`. A side written before still reads, and the key is ignored.
- A record `compare` writes lacks the rows Scope 3 names. A record written before still passes `check` and `model`.
- `compare` accepts a side taken before #986, which it refused. Its record holds only what the eval recorded.
- No dependency, environment variable or migration changes. The version moves with #1498, not here.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
