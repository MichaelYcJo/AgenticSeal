# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 6ef6f36e, the last build commit; this record's commit follows it |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

`plan.md`'s row 2: the budget concept leaves, and `rules --check` and the
release table stay. `seal/budgets.md`, `.github/scripts/budget_check.py`, the
`budgets` CI job, the hygiene budget step, and every row, unit and case that
stood only on them removed, the four `Enforced by:`-resolution cases of
`tests/test_a_budget_ratchets.py` moved. `rules.py` taking `RULE_FILES`,
`shown_lines`, `targets_of`, the eval-case arm and `Unreadable` and gaining
`--check [--root DIR]`, exit 0 · 1 · 2, with one suite case over the tree and
no hygiene step. `.github/scripts/release_report.py` printing one table
against the last release tag, always exit 0 (2 when unreadable), in a
`release-report` job on a pull request into `main` only. Every sentence that
describes budgets, ceilings, price levels or `Budget raised:` lines
rewritten in place or removed, and #930's changelog fragment rewritten to
what 0.22.0 ships. The earlier `phases/phase-2.md` renamed first, and a
`phases/phase-1.md` written from phase 1's commits.

## What this phase found

**What left, counted against `spec.md` §*Removes*.** The counts there were
read at 2062d9b2; the tree grew before this phase, so each is restated as
removed.

| §*Removes* row | Removed |
|---|---|
| the budgets file | `seal/budgets.md`, 157 lines |
| the budget checker | `.github/scripts/budget_check.py`, 1,678 lines, 55 top-level units. `Unreadable`, `sibling`, `shown_lines`, `enforcer_lines`, `rule_files`, `targets_of`, `target_problem` and `measure_unresolved` (as `unresolved`) moved into `rules.py` with `RULE_CLOSER`, `RULE_FILES`, `EVAL_CASES` and `EVAL_CASE`; the preload and job-list readings are `release_report.py`'s own, through `payload_meter` |
| the budget cases | `tests/test_a_budget_ratchets.py`, 1,788 lines, 61 cases: 57 gone, 4 moved into `tests/test_the_rules_command_reads_each_rule_off_its_test.py` under their names, pointed at `--check` |
| the budget step and job | the hygiene step *every budget holds its ceiling, and a raised ceiling says why*; `test.yml#budgets`, now `release-report` |
| the seal's budget row | the `PARTITION` row; the `FEATURE_UNANSWERED` entry; the pins at `· 4 more steps` and `· 7 more steps`, 7 and 10 steps |
| the budget sentences | every coordinate the row lists, and the ones below that it does not |
| #930's changelog as written | rewritten to `rules --check` and the release table |

**The tree's rule files name targets from one glob only.** `rules --check`
read 435 targets in 61 rule files, all of them in `docs/*.md`; the one
`Enforced by:` line in a skill sits in a fence. So a scratch copy with one
target renamed cannot tell a walk of every glob from a walk of `docs/*.md`
alone. `test_every_enforced_by_target_in_the_tree_resolves` renames one real
target and also plants a gone target in a file of each of the other six
globs, and is red under a walk of `docs/*.md` alone.

**The budget concept reached further than the row's list of coordinates.**
Each of these described it or pinned a sentence that did, and each was
rewritten in place in the removal commit: `skills/verify/SKILL.md`'s two
step counts (`CI also · 4 more steps`, four of the seven; three steps with a
local answer, two running a script), `broad_gate.py`'s comment over
`PARTITION` (four of the seven exclusions), the pin of the first in
`tests/test_the_seal_is_taken_once_by_the_sealer.py`, the durations
refresh in `CONTRIBUTING.md` §*Running the checks* with the `REMEDY`
message and two cases in
`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` that
pinned the `--restate-price` step, the comment in
`tests/test_ci_gives_the_checks_what_they_need.py`, and the changelog
fragments of #931 and #944, which ship in 0.22.0 and described the price
level and the `enforced-unresolved` and `unenforced` rows.

**One case held a floor that the removed step had kept.**
`test_the_workflow_reader_finds_the_env_assignment_the_file_already_has`
asserted at least four base spellings in `hygiene.yml`; the budget step was
the fourth. It now compares the reader's count with an independent listing
of the file's code lines naming a base, and is red when the reader drops
the `BASE:` shape.

**The release table belongs to the release pull request, not to the
preparation commit.** `docs/release-checklist.md` read the budgets in §2,
before the release branch merges to `main`; the table prints only on that
pull request, so its paragraph is in §5.

**`.test_durations` keeps the removed module's 153 entries.** They are
46.4 s of 6,827.1 s, under the one second in twenty
`test_the_durations_file_prices_the_suite` allows, and that case is green;
the next refresh from the `test-durations` artifact drops them.

**The release table, run on this tree against v0.21.1** with the tag
commit's `tests` run (38360379166) as its job list, printed five preload
rows, the suite at 7,862 s against 6,827 s, the three legs at 10.0, 43.6 and
20.7 minutes for the tag, and 21 document rows, at exit 0.
