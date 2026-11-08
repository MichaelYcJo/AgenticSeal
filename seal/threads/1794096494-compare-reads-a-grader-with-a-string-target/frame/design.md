# Design: 1794096494-compare-reads-a-grader-with-a-string-target

## Grounding

The tree as read at `f096614f6`.

| Policy clause | What it fixes for this work |
|---|---|
| `skills/implement/orchestration.md` *Orchestrator: when a work item is required*, the first rung | The fix changes what `evals/scripts/noninferiority.py compare` prints for a side holding a grader whose target is a string, from a traceback to the `Verdict:` line and the record a person reads, so it alters observable behaviour and takes a design and a plan. The paths it touches leave `dist` by `.gitattributes` (`/evals/ export-ignore`, `/tests/ export-ignore`, read), so no installed plugin runs the changed code, and that sizes the frame to one phase and not the rung. |
| The policy root, `docs/` (no `Policy root` row in `seal/config.md`, read) | No section of the policy root states a rule of `noninferiority.py`: `git grep -n 'regrade\|noninferiority\|non-inferior' -- docs` prints nothing (executed). The rule the code breaks stands in `evals/README.md` *The behaviour suite*: "A `truth-` grader over the round record is graded on those findings", and every other grader keeps the result the eval recorded. A grader whose target is `files` reads the fixture's files and no round record, so the README already says what the fixed reader does, and this work edits no README sentence. |
| The unsettled designs' `## Rule changes` under `seal/threads/` (read) | None of them names `evals/` or a section about the behaviour suite. |
| `seal/follow-up.md` *Schedulable items with nowhere else to go* (read) | No row is about `noninferiority.py`, and `grep -n 'RIDER:'` over `evals/scripts/noninferiority.py` and `tests/evals/test_noninferiority.py` prints nothing (executed), so no item rides on this work. |
| The reader, `evals/scripts/noninferiority.py#reads_record` (read) | Line 361 reads `path = (config.get("target") or {}).get("path") or ""`, which calls `.get` on a string target. `git grep -n 'reads_record'` lists one caller, `side_numbers` at line 710 (executed). `compare` calls `side_numbers` on each side, and `regrade` calls it last, at line 1497, after it has written its output file (read). `regraded` and `unreproduced` do not call it (read). `git diff --quiet 4531133b7 f096614f6 -- evals/scripts/noninferiority.py tests/evals/test_noninferiority.py` exits 0 (executed), so the defect at the issue's commit is the defect at this frame's commit. |
| The class of the defect: a grader target that is not a mapping, built from what produces a target and from every committed grader file | Two producers write a target. `evals/scripts/behaviour.py:56` writes `{"source": "file", "path": path}`. `evals/scripts/rule_cases.py#shape_regex` passes its `target` argument through, and its one string caller is the `no-probe-left` grader at `evals/scripts/rule_cases.py:428` with `"files"` (executed: `grep -n -A2 'shape_regex('` and `grep -rn 'target=' evals/scripts/*.py`). Over every grader file under `evals/behaviour/*/*/graders/`, the `target:` lines hold two shapes: a flow map with `source` and `path`, and the string `'files'` (executed: `grep -rhn '^target:'` piped to `sort` and `uniq -c`). The string stands in the `shape-no-probe-left.md` grader of five crafter cases, `rule-crafter-count-words`, `rule-crafter-is-palindrome`, `rule-crafter-rename`, `rule-crafter-slugify` and `rule-crafter-truncate` (executed: `grep -rln "^target: 'files'"`), two more than the spawn prompt named. No `truth-` grader carries a string target. Every other grader file names no target. A grader with no target already reads as one that reads no record (`tests/evals/test_noninferiority.py#Test_reads_record`, id `no target`, read). |
| What a side records as a grader's `config` (read) | `evals/scripts/noninferiority.py#grader_from` builds a grader "in the shape a side records it", with `config` holding every front-matter field but `type` and `weight`, and `scalar` reads `'files'` as the string `files`. So a side whose case holds `shape-no-probe-left` carries `config.target == "files"`. No side is committed in the tree (`git grep -l '"target": "files"'` prints nothing, executed), so the shape of a real side is read from the code that mirrors it and from the issue's traceback, and nobody here opened a paid side. |
| Probe at `4531133b` in a `git clone --no-local` under the scratchpad (executed) | `reads_record` on a `shape-` regex grader with `target: "files"` raised `AttributeError: 'str' object has no attribute 'get'`, and `side_numbers` on a one-run side holding it raised the same. With `reads_record` wrapped to return False for a target that is not a `dict`, `reads_record` returned False and `side_numbers` counted the grader as `['shape', 1, 1]`, the eval's recorded result. `compare --agent crafter --phase 1` on two such sides with one suite tree raised the same `AttributeError` as is, and printed `Verdict: pass` and exited 0 with the wrapper. Command: `python3 -I test_tmp_probe.py <clone>` and `python3 -I test_tmp_compare.py <clone> <dir> [guarded]`, both deleted with the clone before hand-back. |
| The issue's run on the paid pair of #1178, at `33ced573b` and `4531133b7` | The `Verdict: pass` with every reach and shape grader 1 of 1 on both sides is the issue author's claim. The sides are not in the tree, and nobody here re-ran them (`frame/questions.md` Q1). |
| `docs/releasing/branch-and-release.md` *Cutting a release*, and the unsettled change to it in `seal/threads/1793966252-a-sentence-is-read-before-the-sealer/frame/design.md` | The version moves in the first pull request into `release/v0.34.1`, in the commit that adds the release's first work item's changelog fragment, written by the party that builds it. `.claude-plugin/plugin.json` holds `0.34.0` at `f096614f6`, and `origin/release/v0.34.1` stands at `8c2d60e14`, the 0.34.0 merge, so no pull request into the branch has landed (executed). Issue #1421's milestone is `release: 0.34.1` (executed: `gh issue view 1421`). |

## Scope

In:

1. `evals/scripts/noninferiority.py#reads_record` reads `config.target` as a mapping only where it is one. A target of any other value, the string `files` among them, names no path, so the grader reads no round record and keeps the result the eval recorded. The docstring says so in one sentence. The guard tests for a mapping and not for a string, so a target of any shape the eval adds later reads the same way.
2. `tests/evals/test_noninferiority.py#Test_reads_record::test_refuses_any_other_grader` gains a case: a `truth-` regex grader whose target is the string `files` is refused. The grader is a `truth-` one so the case also refuses a fix that only reorders the kind test before the target read.
3. `tests/evals/test_noninferiority.py#Test_compare` gains a case that hands `compare` two sides, each holding a `shape-` regex grader whose target is `files` in the shape `grader_from` gives, with one suite tree. It asserts exit 0, the record written, and the printed `Verdict:` line. It is seen red against `reads_record` as it stands at `4531133b7`, with the guard of item 1 removed and nothing else.
4. The work item's `changelog.md`, written by the builder.

Out:

- A `regrade` case. `regrade` reaches `reads_record` only through its last call, `side_numbers(out)`, which item 3 reaches through `compare`, so a `regrade` case would pin the guard that items 2 and 3 already pin. The fragment states that `regrade` read such a side only up to that line.
- The `truths` list in `side_numbers`, which counts every `truth-` regex grader against the findings whatever its target. No `truth-` grader carries a string target (*Grounding*, the class row), so no side meets it today.
- Re-running `compare` on the paid pair of #1178 (`frame/questions.md` Q1).
- The plugin directory work of issue #1420 and the stamp launcher of issue #1426, out by the spawn.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A crafter pair | Given two sides whose cases hold `shape-no-probe-left` with target `files`, run on one suite. When `noninferiority.py compare` reads them. Then it writes the record, prints its `Verdict:` line and exits 0. | *Scope* item 3, red at `4531133b7` with only the guard removed, green after |
| A truth grader with a string target | Given a `truth-` regex grader whose target is `files`. When `reads_record` reads it. Then it returns False and raises nothing. | *Scope* item 2, red the same way |
| A truth grader over a round record | Given a `truth-` regex grader whose target maps `path` to a round record. When `reads_record` reads it. Then it returns True, as before. | `tests/evals/test_noninferiority.py#Test_reads_record::test_accepts_a_truth_regex_over_a_round_record`, unchanged and green |

## Data & interfaces

`reads_record(grader)` keeps its signature and its True cases. `grader["config"]["target"]` is a mapping `{"source": "file", "path": ...}` or a value that is not a mapping, such as the string `files`, which the eval reads as every file of the fixture. Only a mapping names a path.

## Rule changes

- nothing
  why: no section of the policy root states a rule of `noninferiority.py`, and the rule this work brings the code to stands in `evals/README.md` *The behaviour suite* already (*Grounding*, the policy root row).

## Removes

- nothing
  why: the work adds no mechanism, so nothing is owed in return. It rewrites the one line of `evals/scripts/noninferiority.py#reads_record` that read the target in place, and no other sentence, case or citation states that a target is a mapping (*Grounding*, the class row).

Framed 2026-11-08 by framer, before the build.
