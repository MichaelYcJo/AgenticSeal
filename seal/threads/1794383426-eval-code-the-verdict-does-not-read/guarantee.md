# Guarantee: 1794383426-eval-code-the-verdict-does-not-read

Audited at `e543f9ef1` against `origin/release/v0.37.4`, which resolves to
`10e721f11` (`git rev-parse --verify --quiet 'release/v0.37.4@{upstream}'`).
`trail/gate.md` names `cf0a708c2 against 10e721f11`, an ancestor of HEAD,
and `git log --no-merges --name-only cf0a708c2..HEAD ^10e721f11` lists
`trail/gate.md` alone, a path under `seal/threads/<item>/`.
`seal pr-body seal/threads/1794383426-eval-code-the-verdict-does-not-read --body <scratch>/pr-body.md --check`
exits 0. Every re-run below was made in two `git clone --no-local` copies
of HEAD under the sealer's scratch directory: `at-base`, with the changed
code restored from `10e721f11`, and `at-head`, where a guard was removed
for one run and restored with `git checkout` after it. The tree under
audit was not changed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| S1: `regrade` is refused by argparse with exit 2 | `trail/phases/phase-1.md` *S1*; `changelog.md` *Removed*, second item | `python3 evals/scripts/noninferiority.py regrade --side a.json --suite-rev HEAD --out b.json`, exit read directly, at HEAD | holds (executed): exit 2, `invalid choice: 'regrade' (choose from 'run', 'compare', 'check', 'model')` |
| Seen red against the old code: *Test_compare* `test_accepts_a_side_read_before_986` failed on exit 2 against 0 | `trail/phases/phase-1.md`, the seen-red list | HEAD's case with `noninferiority.py` and the three removed files restored from `10e721f11`, `bin/test -p no:xdist -q <case>` | holds (executed): `assert 2 == 0` from `NI.main(['compare', ...])` |
| Seen red against the old code: *Test_side_numbers* `test_accepts_a_truth_over_a_round_record_as_the_eval_recorded_it` failed on `['truth', 0, 1]` against `['truth', 1, 1]` | `trail/phases/phase-1.md`, the seen-red list | same run | holds (executed): the same two values on the assert line |
| Seen red against the old code: *Test_annotate* `test_accepts_each_runs_cost_and_calls_and_the_sides_meta` failed on `report_text` left in the run | `trail/phases/phase-1.md`, the seen-red list | same run | holds (executed): `Left contains 1 more item: {'report_text': ''}` |
| Seen red against the old code: *Test_main* `[the removed regrade]` failed on `FileNotFoundError` from the old `regrade` | `trail/phases/phase-1.md`, the seen-red list | same run | holds (executed): `FileNotFoundError: ... 's'`; the other eight *Test_main* cases passed |
| *Test_check* `test_accepts_a_record_written_before_1487_as_it_was_judged` passes against the old code, so it was shown red by making `parse_record` refuse a record carrying `Baseline report rows` | `trail/phases/phase-1.md`, the `seal mutate` list | (a) the same base run; (b) at HEAD, `parse_record` made to raise `ValueError` where `header_field(text, "Baseline report rows")` is not None, then the case alone | (a) does not hold as written (executed): against the old code the case fails in `merged` on `KeyError: 'rows'`, because HEAD's `side()` fixture carries no `rows`, so it was neither green nor red on its guard there. (b) holds (executed): red on `assert 1 == 0` from `NI.main(['check', ...])`, the line the guard names. The case pins its guard, so the misstatement changes no fact of the tree. |
| S8: the evaluated-words case names a rule case's word and does not read a recorded case, shown red with its `RECORDED_CASE` guard alone removed | `trail/phases/phase-2.md` *S8* | at HEAD, `hits`'s `RECORDED_CASE.match(...)` test made false, then `test_a_rule_cases_word_is_named_and_a_recorded_case_is_not_read` alone | holds (executed): red on `At index 0 diff: ('proofer/replay-1-r2/prompt.md', 2, 'judged')` |
| *Test_main* `test_accepts_an_out_directory_and_writes_the_proofer_case_with_both_truths` went red with `uncovered` left out of the loop | `trail/phases/phase-2.md`, the two new `Test_main` cases | at HEAD, `rule_cases.py`'s loop over `(shout,)` alone, then the case alone | holds (executed): red on `assert ['truth-shout-twice.md'] == [...]`, `truth-shout-twice-uncovered.md` missing |
| S6: the generator writes all 17 rule cases byte for byte as committed, and the comparison can go red | `trail/phases/phase-2.md` *S6*; `frame/design.md` S6 | at HEAD, `python3 evals/scripts/rule_cases.py --out <scratch>/s6`, then `diff -rq` per case against `evals/behaviour/<agent>/<case>`; again with the mutant of the row above | holds (executed): exit 0, 17 written, 17 committed, 0 differing; under the mutant `diff -rq` of `proofer/rule-proofer-one-finding` exits 1, `Only in evals/behaviour/...: truth-shout-twice-uncovered.md` |
| S7: `evals/scripts/` holds three scripts alone and the cases are unchanged | `trail/phases/phase-2.md` *S7*; issue *Decision*, the eight proofer cases stay frozen | `git ls-files evals/scripts`; `git diff --stat 887127e61 HEAD -- evals/behaviour/`; `git diff --stat 10e721f11 HEAD -- evals/behaviour/` | holds (executed): `behaviour.py`, `noninferiority.py`, `rule_cases.py`; both diffs empty, exit 0 |
| S9: `evals/README.md` names no removed command, file or row | `trail/phases/phase-2.md` *S9* | `grep -n 'regrade\|replay_targets\|seed_defects\|recurred_truths\|report_text\|false rows\|true find' evals/README.md` | holds (executed): nothing printed, exit 1 |
| The touched modules pass at HEAD, S10's citation case among them | `trail/phases/phase-2.md` *Phase boundary*; `frame/design.md` S10 | `bin/test -q tests/evals tests/text/test_no_case_tells_the_agent_it_is_evaluated.py tests/test_censuses.py tests/behaviour/test_evals_layout.py tests/behaviour/test_a_cited_section_stands_in_its_file.py` at HEAD | holds (executed): 498 passed, exit 0. The full suite is the broad gate's, recorded in `trail/gate.md` at `cf0a708c2` (read) |
| Every `## Removes` row and every removal the changelog names stands nowhere in the tree | `frame/design.md` *Removes*; `changelog.md` *Removed* | `test -e` on the six removed files; `git grep -n -w` of every removed unit, file and constant name outside `seal/threads/`, `evals/behaviour/`, `.test_durations` and `CHANGELOG*`; `git grep` of `report rows`, `false rows`, `true find` in `evals` and `tests` | holds (executed): no file stands; every hit is an unrelated word (`apart`, `masked`, `differs`, `READ` in other modules), `docs/checks/the-pull-request-check.md:62` and `:66`, which the *Rule changes* `from` holds whole (a whitespace-collapsed `in` test printed `True`), the `side_numbers` docstring saying a pre-#1487 `report_text` is not read, and `tests/evals/test_noninferiority.py`'s pre-#1487 record case, which plants the old rows on purpose. `scalar`, `SCALAR` and `grader_from` stand in `evals/scripts/behaviour.py:21`, `:53`, `:65`, where the *Removes* row lands them |
| Scope 12: `.test_durations` and `docs/` are not edited | `frame/design.md` Scope 12 and `## Rule changes`; `gaps.md` *Not done* | `git diff --stat 10e721f11 HEAD -- .test_durations docs/` | holds (executed): empty |
| Round 1's finding 1 `fixed ba7c101ed`: `gaps.md:12` reads the replacement paragraph, and the commit touched nothing outside the work item's records | `trail/rounds/round-1.md`, finding 1's close block | `git show --stat ba7c101ed`; a `python3` `in` test of the round's replacement paragraph against `gaps.md` at HEAD | holds (executed): one file, `gaps.md`, 1 line in and 1 out; the paragraph stands whole |
| `pr.md`'s four quotes stand word for word at their coordinates | `pr.md` | a `python3` `in` test of each quote against `frame/plan.md` at HEAD | holds (executed): 4 of 4 found |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | `frame/design.md` and `frame/plan.md`: remove the two generators, `recurred_truths.json`, `regrade`, the reader of the printed round record and the row counts, with their tests; move `scalar` and `grader_from` to `behaviour.py`; keep the cost figures #1254 kept, truth graders as a kind, and every case under `evals/behaviour/` byte for byte; leave `.test_durations` (Scope 12, since `0ff090e04`) and hand `docs/checks/the-pull-request-check.md` to the settle | the issue's *Change* and *Decision*: the owner stopped reporting recall and the false-finding rate and kept the eight proofer cases frozen. Its reading of the first *Done when* line, which keeps spend, tokens, calls, seconds and preload bytes, is recorded with its grounds in `frame/plan.md` *Alternatives considered* and quoted at the head of the pull request body for the owner | none |
| the build | the diff `10e721f11...e543f9ef1` and `trail/phases/phase-1.md`, `phase-2.md`: Scopes 1 to 11 built at `7d718955b` and `88a1d8a6d`; Scope 12 declined against `CONTRIBUTING.md` *Running the checks* and folded into the frame at `0ff090e04`; removals the *Removes* table did not name, each standing on a removed unit | the design at HEAD, every claim sampled above, and the tree. `routing.md` reads `crafter`, and each phase whose Status cell holds a commit (1 at `7d718955b`, 2 at `88a1d8a6d`) has its record | none of the tree's facts. `phase-1.md`'s remark that the pre-#1487 *Test_check* case passes against the old code does not hold as written (row above); the case's seen-red rests on the mutant, which holds |
| the last round | `trail/rounds/round-1.md` at `9726a8f62`: one `should` finding in `gaps.md:12`, `fixed ba7c101ed`; every Scope and S1 to S9 confirmed | the design, the build, the changelog and `pr.md`, as its *Confirmations* state and the re-runs above reproduce; its fix touched `gaps.md` alone and reads as the finding asked | none |
| the changelog | `changelog.md`: the record drops the four row counts and both `tokens per true find` rows and keeps the truth rows in `## Graders`; `regrade` exits 2; `run` keeps no `report_text`; `compare` accepts a pre-#986 side; old records still pass `check` and `model`; the generators and the no-two-truths case go; the evaluated-words case passes over recorded cases through `RECORDED_CASE` | the diff (`noninferiority.py:345`, `:471`, `:705`, `:760`; `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py:49`) and the re-runs of S1, the #986 case and the pre-#1487 case above. "#1356" is `f93d70ea4`, whose subject names `(#1254) (#1356)` | none |
| the orchestrator's part of the pull request body | `pr.md`, above `## From the records`: four quotes of `frame/plan.md` and `Closes #1487.`; `seal/config.json` names English for both language keys, so no `pr.<lang>.md` is owed and none stands | the design, whose text each quote is word for word; the issue it closes | none |

`routing.md` *Why this way* gives the orchestrator's grounds under `agentic`
for each row. The diff they describe, about 3,500 removed lines of code and
tests (the six removed files hold 3,546) and a document left citing a
removed command, is the diff at HEAD: it changes `evals/scripts/`, its
tests, `tests/censuses.py`, `tests/test_censuses.py`, one `tests/text/`
case and `evals/README.md`, and no hook, gate or agent definition.
`seal/parity.json` is not carried by git, so no parity comparison is owed.

```seal
target: e543f9ef1 against 10e721f11
Verdict: sealed
```
