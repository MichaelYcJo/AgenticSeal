# Review round 1: 1794383426-eval-code-the-verdict-does-not-read

```seal
target: 9726a8f62 against origin/release/v0.37.4
```

The branch was read against `origin/release/v0.37.4` at `10e721f11`, which
is the merge base since `89b84bc86` merged it in. The range is the branch's
own commits from `887127e61` to `9726a8f62`. The merge brought #1498's
`tests/censuses.py#_root_names` hunk, which this round left to #1498's own
review. This is the first round, so no coordinate or verdict was carried
from an earlier one. `seal/parity.json` is not declared, so no parity
comparison was owed.

The work item's records were each read whole at `9726a8f62`: `routing.md`,
`frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`,
`changelog.md`, `pr.md`, `trail/phases/phase-1.md` and
`trail/phases/phase-2.md`. `seal/config.json` names English for both
language keys, so no `pr.<lang>.md` is owed and none stands. Issue #1487
was read whole (`gh issue view 1487 --json title,body,comments`, no
comments): its *Change*, its *Decision* of 2026-11-11 and its three *Done
when* lines are the reference above the frame.

The two phase records are dated to their phases, and this round read them
as claims of that time. `trail/phases/phase-2.md:7` says the frame "still
state[s] the edit" of `.test_durations`, and `trail/phases/phase-1.md:45`
says Scope 12 drops 101 keys. Both held when written. `0ff090e04` then
folded the decline into `frame/design.md:40`, `:112` and `:20`,
`frame/plan.md:37` and `:48`, which this round read at the target. Each of
them now states that the file is not edited.

## Findings

### 1. The closing memo says the durations entries are left against Scope 12, which since `0ff090e04` states that they are left

```seal
severity: should
location: `seal/threads/1794383426-eval-code-the-verdict-does-not-read/gaps.md:12`
evidence: read `seal/threads/1794383426-eval-code-the-verdict-does-not-read/gaps.md:12`, `seal/threads/1794383426-eval-code-the-verdict-does-not-read/frame/design.md:40`, `seal/threads/1794383426-eval-code-the-verdict-does-not-read/frame/plan.md:63`, `skills/code-review/scripts/pr_body.py:201`
```

Why it matters: `gaps.md:12` opens "`.test_durations` keeps the 172
entries of the cases this work item removed or renamed, 123.8 s of the
file's 1,616.5 s (7.66 %), against `frame/design.md` Scope 12." At the
target, Scope 12 (`frame/design.md:40`) reads "`.test_durations` is not
edited, since a work item never commits it". So the memo's sentence is
true of `9d133413a`, where phase 2 wrote it, and false of `0ff090e04` and
every commit after it. The sentence is not a dated record. `## Not done` is
part of the closing memo, which states the present. `seal pr-body` copies
that section into the pull request body (`pr_body.py:201`, `NOT_DONE`), so
the body would tell the sealer and a reader of the pull request that the
build departs from its frame where it does not. The sealer then checks a
departure that does not exist, against `frame/plan.md:63`, which records
the fold. The count and the share are right: this round recounted them,
and the recount is under `## Probes`.

The entry stays under `## Not done`: the edit was within reach and is
deliberately not taken. The fix changes only the clause that points at the
frame. No other statement of this fact stands at the target, since the
phase records are dated, so `gaps.md` is the one file the fix changes.

```markdown
`.test_durations` keeps the 172 entries of the cases this work item removed or renamed, 123.8 s of the file's 1,616.5 s (7.66 %), as `frame/design.md` Scope 12 states since `0ff090e04`. `CONTRIBUTING.md` *Running the checks* says a work item never commits the file, and gives its refresh to whoever prepares the release, from the release pull request's `durations` union. Past `.github/scripts/durations_union.py#STALE_SHARE`, 5 %, that job is red on the release pull request until the refresh, or until #1486 removes the file. `trail/phases/phase-2.md` gives the grounds.
```

```seal
verdict: fixed ba7c101ed
answer: The finding holds: `frame/design.md:40` states since `0ff090e04` that `.test_durations` is not edited, so "against Scope 12" claimed a departure the frame does not hold. `gaps.md:12` now reads the replacement paragraph as given, with the count and share unchanged. `ba7c101ed` changes `gaps.md` alone, and no other statement of this fact stands outside the dated phase records.
```

## Confirmations

What matched: Scope 1 and Scope 2. Each unit `frame/design.md:29-30` names
is gone from `evals/scripts/noninferiority.py`, along with the
`replay_targets` import and the `sys.path.insert` that served it (read, the
diff `10e721f11..9726a8f62`). `case_runs` stays at `noninferiority.py:466`,
where `side_numbers` reads it. `side_numbers` (`:471`) counts every grader,
truth graders among them, from `g.get("passed")` and reads no
`report_text`. `annotate` (`:345`) writes `cost` and `tool_calls` alone.
`compare` (`:863`) keeps its two exit-2 refusals, a side naming no suite
and two suite trees, and its docstring now names those two.

What matched: Scope 3 and S2 to S4. `render`, `merged`, `cost_rows` and
`parse_record` (`noninferiority.py:705`, `:624`, `:688`, `:760`) write and
read none of the four row counts and neither `tokens per true find` row.
The `## Graders` table still lists truth graders. `verdict`, `check` and
`model` read no removed key: a `git grep` of `rows`, `false` and `true find`
in the script finds only `cost_rows` and the table reader. S3 is held by
`tests/evals/test_noninferiority.py:1513`, and S4 by `:1567`, which also
asserts that its `replace` calls planted all six old rows. S5 is held by
`:723`. The narrow run passed (executed).

What matched: Scope 4. `scalar`, `SCALAR` and `grader_from` stand at
`evals/scripts/behaviour.py:53` and `:65` with their bodies unchanged, and
their nine cases stand at `tests/evals/test_behaviour.py`. Their only
callers are tests, which `frame/plan.md:27` accepts for this destination:
"Moving them to `behaviour.py`, beside the writer they invert, is equal in
cost". `f6521e678` folded that choice into Scope 4. `bin/seal layout
--check` over the three changed `tests/evals/` modules refuses none
(executed).

What matched: Scope 6, Scope 7 and S6. The three files and the two test
modules are gone. `rule_cases.py:316-323` writes `truth-shout-twice-uncovered`
from a literal. Its pattern and body are those of the removed
`recurred_truths.json` entry and of the committed grader file at
`10e721f11`. The generator's output equals all 17 committed rule cases byte
for byte (executed). The docstring says the truth is a defect "its own runs
found". That holds: the removed entry's `from` names four runs of this
case, under its old name.

What matched: Scope 8 to 10 and S7, S8. The no-two-truths module is gone.
`hits` (`tests/text/test_no_case_tells_the_agent_it_is_evaluated.py:41`)
passes over a recorded case through `tests/censuses.py#RECORDED_CASE`.
`OLD_NAME_RECORDS` and `KEPT_FILES` lost the removed paths, and so did
their planted cases in `tests/test_censuses.py`. `git ls-files evals/scripts`
lists the three scripts alone, and `evals/behaviour/` is unchanged since
`887127e61` (executed).

What matched: Scope 5, Scope 11 and S9. The `noninferiority.py` module
docstring, `evals/README.md` *The behaviour suite* and the two `tests/censuses.py`
docstrings no longer describe the removed reading. A `git grep` of every
removed name across the tree, outside `seal/threads/`, `evals/behaviour/`
and `.test_durations`, finds only `docs/checks/the-pull-request-check.md:62`
and `:66` and the new tests' own mentions (executed). The two lines in that
document are the `from` of `frame/design.md` *Rule changes*, and that
`from` matches the document's text with its whitespace collapsed
(executed). The issue's first two *Done when* lines hold. The third is the
settle's, through that rule change.

What matched: the changelog fragment. Each sentence of `changelog.md` was
checked against the code. #1356 is `f93d70ea`, which narrowed the verdict.
`regrade` exits 2 under argparse. `compare` accepts a side taken before #986
(`noninferiority.py:863`), and a record written before #1487 still passes
`check` and `model` (`test_noninferiority.py:1567`). The *Changed* item
matches the test module's use of `RECORDED_CASE`.

What matched: `pr.md`. Each of its four quotes stands word for word at its
coordinate: `frame/plan.md:20`, `:21`, `:63` and `:64`. The title judgment
at `:64` stands on the repository's history as well as its stated grounds:
`f93d70ea`, which changed the same verdict, took `refactor:`.

`tests/evals/test_rule_cases.py:85-89`, `test_refuses_an_out_option_with_no_directory`,
holds no fact the frame states. It pins argparse's exit 2 on `--out` with
no value, which the diff did not change, and stands so that `Test_main` has
the refuses case `CONTRIBUTING.md` *The test layout* asks for. So it opens
no finding. Each other new case covers something its group does not:
`seal layout --pairs` names no pair for the three modules (executed), and
`tests/behaviour/test_evals_layout.py` compares the sealer cases alone, so
the proofer case's second truth is held only by the new `Test_main` accepts
case.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `9726a8f62`. Every module runs `tests/censuses.py` through `census_case`, and this round ran the changed modules alone. | `gaps.md` *Not verified*, both rows | the orchestrator, at the broad gate |
| S10, at the broad run. This round ran the citation case's one module narrowly, and it passed, but the broad run holds it. | `frame/design.md` S10 | the orchestrator, at the broad gate |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/evals tests/text/test_no_case_tells_the_agent_it_is_evaluated.py tests/test_censuses.py tests/behaviour/test_evals_layout.py -q`, in a `git clone --no-local` at `9726a8f62` | 435 passed, exit 0 |
| `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q` | 63 passed, exit 0 |
| `python3 evals/scripts/rule_cases.py --out <scratch>/s6`, then `diff -rq` of each generated case against `evals/behaviour/<agent>/<case>` | generator exit 0; 17 cases written, 17 under `evals/behaviour/*/rule-*`, 0 differing |
| `git ls-files evals/scripts`; `git diff --stat 887127e61 HEAD -- evals/behaviour/` | `behaviour.py`, `noninferiority.py`, `rule_cases.py`; the diff printed nothing |
| `grep -n 'regrade\|replay_targets\|seed_defects\|recurred_truths\|report_text\|false rows\|true find' evals/README.md` | nothing printed, exit 1 |
| `python3 evals/scripts/noninferiority.py regrade --side a.json --suite-rev HEAD --out b.json` | exit 2 |
| `git show 10e721f11:evals/behaviour/proofer/rule-proofer-one-finding/graders/truth-shout-twice-uncovered.md` and `git show 10e721f11:evals/scripts/recurred_truths.json` | pattern and body equal to the literal at `rule_cases.py:316-321` |
| `bin/test` over the four surviving touched test modules with `--collect-only -q -p no:xdist`, then a `json` read of `.test_durations` for keys of the seven touched or removed modules not collected | 172 keys, 123.8 s of 1,616.5 s, 7.66 % |
| `bin/seal layout --check` and `--pairs` over `tests/evals/test_noninferiority.py`, `test_rule_cases.py`, `test_behaviour.py` | 0 refused; 0 pairs |
| `uvx ruff check` and `uvx ruff format --check` over the nine added or modified `.py` files | exit 0; 9 files already formatted |
| `git grep -n -i -E` of every removed unit, file and record row, outside `seal/threads/`, `evals/behaviour/`, `.test_durations` and `CHANGELOG*` | only `docs/checks/the-pull-request-check.md:62` and `:66`, the new tests' own mentions, an unrelated `recalled` in `agents/framer.md:103` and the unrelated `load_script` of `tests/skills/test_session_cost.py` |
| a `python3` comparison of the *Rule changes* `from` with `docs/checks/the-pull-request-check.md`, whitespace collapsed | found |
