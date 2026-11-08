# Implementation Plan: 1794096494-compare-reads-a-grader-with-a-string-target

## Technical context

The tree as read at `f096614f6`.

`evals/scripts/noninferiority.py#reads_record` (lines 356 to 366) decides which `truth-` graders `side_numbers` grades again from a run's findings: a regex grader whose `config.target.path` ends in a round record's path, `RECORD_PATH` at line 90. Its target read at line 361 assumes a mapping. `side_numbers` builds its `read` map from it at line 710, and `compare` (line 1120) and `regrade` (line 1497) both reach it through `side_numbers`. `side_numbers` catches only `ValueError` around `grade`, and `compare` catches only `ValueError` from `side_numbers`, so the `AttributeError` escapes as a traceback.

The tests live in `tests/evals/test_noninferiority.py`: `Test_reads_record` at line 913 holds its accepting and refusing cases as parameters, and `Test_compare` at line 2033 builds sides with `eval_side`, which writes a one-run side holding a `shape-x` `file_exists` grader. The new compare case needs a side whose case holds a `shape-` regex grader with `config.target` the string `files`, so it builds its own side or widens `eval_side` with a graders argument, the crafter's choice.

The failure scenario of the chosen approach, six months out: the eval adds a target shape that is a mapping without `path`, such as `{source: 'transcript'}`. `reads_record` reads it as naming the path `""` and so as reading no record, which is the right reading for any target that names no round record. A `truth-` grader over a round record that the eval spells some other way, a mapping whose key is not `path`, would also read as no record and keep the eval's own result, so recall would be read from the whole file and not from the findings. That is quiet, and nothing in the tree spells a record target any other way today (`frame/design.md` *Grounding*, the class row).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. Read the target's `path` only where the target is a mapping, and read any other value as naming no path | The one in *Technical context*. | Chosen. It fixes the one reader of the target, for every shape that is not a mapping, and keeps the eval's recorded result for those graders, which is what `evals/README.md` *The behaviour suite* says. |
| 2. Test the grader's kind and type before reading its target, so a `shape-` grader never reaches the `.get` | A `truth-` regex grader whose target is a string still raises. The defect is the target's shape, not the grader's kind. | Rejected. *Scope* item 2 is a `truth-` grader so that this fix stays red. |
| 3. Normalise each grader's target to a mapping where `run` writes a side | Sides already paid for, the pair of #1178 among them, keep the string, so `compare` still raises on them. It also rewrites the eval's own record of what each grader read. | Rejected. |
| 4. Change the crafter graders `frame/design.md` *Grounding* lists in its class row to a mapping target | `files` is the eval's grammar for searching every file of the fixture, which `shape-no-probe-left` needs to find a probe file at any path. A mapping names one file. Paid sides keep the string either way. | Rejected. |
| 5. Replace the structure: decide which graders read a record from the suite's grader files at the side's `suite_rev`, through `grader_at`, and stop reading the side's recorded `config` | `compare` would read git once per case on every side. A side recorded with a suite tree and no reachable commit could not be read. It also judges a run by a grader text other than the one the eval graded it with, where the suite moved after the run. | Rejected. The structure is kept on the premise that a side records each grader's `config` as the eval read it, checked by reading `grader_from` and by the issue's traceback, which shows the side's own `config.target` reaching line 361. |
| 6. Catch `AttributeError` in `compare` and `regrade` and exit 2 naming the side | The crafter's sides stay unreadable, and the narrowed verdict of #1254 still never reads one. A refusal is the answer for a side no reader can read, and this side is readable. | Rejected. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1, 2, 3 and 4 | The cases of *Scope* items 2 and 3 seen red against `reads_record` with only the guard of item 1 removed, each failing on the `AttributeError` at the target read, then green. `bin/test tests/evals/test_noninferiority.py -q` passes. | e2803d29 |

## Operational impact

No migration, environment variable or dependency. The changed files leave `dist` (`frame/design.md` *Grounding*, the ladder row), and no command, skill or agent the plugin ships runs them, so no installed plugin changes behaviour.

This pull request is the first into `release/v0.34.1`, so phase 1's commit that adds `changelog.md` moves `.claude-plugin/plugin.json` from `0.34.0` to `0.34.1`, as `docs/releasing/branch-and-release.md` *Cutting a release* states. At `f096614f6` no pull request into the branch has landed (`frame/design.md` *Grounding*, the release row).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-08 | This work item carries the version move to 0.34.1. | Issue #1426, the other issue of milestone `release: 0.34.1`, was deferred by the owner on 2026-11-07 until whether the plugin's hooks return is decided, so this pull request is the first into `release/v0.34.1`. | `docs/releasing/branch-and-release.md` *Cutting a release* |
| 2026-11-08 | The pull request's title takes `fix:`, and the kind that came closest is `chore:`. | `compare` stopped on a traceback where `evals/README.md` *The behaviour suite* already said such a grader keeps the result the eval recorded, which is the table's `fix:` row. `chore:` came closest because the changed files leave `dist` and no installed plugin runs them, but a person running `compare` meets the change. | `skills/commit-pr-convention/SKILL.md` *Commit messages*, the prefix table, which *Pull request titles* uses |
