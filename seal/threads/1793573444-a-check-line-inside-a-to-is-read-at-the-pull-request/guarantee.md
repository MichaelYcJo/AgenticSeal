# Guarantee: 1793573444-a-check-line-inside-a-to-is-read-at-the-pull-request

| Field | Value |
|---|---|
| Broad gate | 33419ffe5 against 57d6665b5 |

The base `origin/release/v0.28.0` resolves to 57d6665b5 (executed: `git rev-parse --verify --quiet origin/release/v0.28.0`). 33419ffe5 is an ancestor of HEAD e416e4b4b, and `git log --no-merges --name-only 33419ffe5..HEAD ^57d6665b5` lists one commit, e416e4b4b, touching only `seal/threads/1793573444-a-check-line-inside-a-to-is-read-at-the-pull-request/trail/gate.md` (executed). `seal pr-body <item> --body <file> --check` exited 0: the body below `## From the records` is the records' text (executed). Git carries no `seal/parity.md` (executed: `git ls-files`), so no `original:` line is owed.

## Claims re-run

Every `seen red` was re-run in a `git clone --no-local` of HEAD under the scratchpad, at `1793573444-a-check-line-inside-a-to-is-read-at-the-pull-request/at-base/`, with `skills/code-review/scripts/chain_check.py`, `.github/scripts/rules.py` and `skills/settle/scripts/rule_changes.py` restored from 57d6665b5 and the tests kept at HEAD, run with the main clone's `.venv/bin/python -m pytest -p no:xdist`. The clone was removed after the runs.

| Claim | Source | Command | Result |
|---|---|---|---|
| `test_each_value_line_carries_its_line_in_the_design` seen red against the base with `AttributeError: 'Op' object has no attribute 'lines'` | `trail/phases/phase-1.md:19` | `pytest tests/skills/test_rule_changes.py -k test_each_value_line_carries_its_line_in_the_design`, base code | holds: 4 failed, each `AttributeError: 'Op' object has no attribute 'lines'` (executed) |
| `Test_refused_lines` seen red against the base, no `refused_lines` | `trail/phases/phase-1.md:20` | `pytest tests/github/test_rules.py::Test_refused_lines`, base code | holds: 2 failed, `module 'agentic_rules' has no attribute 'refused_lines'` (executed) |
| S1, S3 and S6 seen red against the base, exit 0 where the case asserts 1 | `trail/phases/phase-1.md:21` | `pytest tests/skills/test_chain_check.py::Test_check_lines_in`, base code | holds: the three cases failed on `assert 0 == 1`; the `add` case failed the same way; S4 and the exit-2 case failed on a missing attribute; S2 and S5 passed at the base, as the record claims them red only under a mutant (executed) |
| S5 seen red under the mutation that reads every field of an `add` or `change` as its `to` | `trail/phases/phase-1.md:24` | `check_lines_in` set, with the `Edit` tool, to read the lines of every field in `op.lines`; `pytest tests/skills/test_chain_check.py::Test_check_lines_in` at HEAD code | holds: 1 failed, `test_reads_no_check_line_in_a_from`, 7 passed (executed) |
| The new cases pass at HEAD | `trail/phases/phase-1.md:15-27`, `trail/rounds/round-3.md:58` | `pytest tests/skills/test_chain_check.py::Test_check_lines_in tests/github/test_rules.py::Test_refused_lines tests/skills/test_rule_changes.py`, HEAD code | holds: 77 passed, exit 0 (executed) |
| `seal rules --check` holds at HEAD and prints what the base's reader prints over the same tree (design S7) | `trail/phases/phase-1.md:13`, `gaps.md` S7 row | `bin/seal rules --check` in the main clone at HEAD; in the scratch clone, the base's `rules.py --check --root .` over the HEAD tree | holds: both exit 0, both `seal rules: all 283 check lines in 55 rule files hold.` (executed) |
| The design's own `to` values pass their own read (design S8) | `trail/phases/phase-1.md:37` | `python3 -I skills/code-review/scripts/chain_check.py --baseline origin/release/v0.28.0 --worktree` in the main clone at HEAD | holds: exit 0; no line for `frame/design.md`; one notice, no `guarantee.md` yet (executed) |
| The arm refuses the defect the issue names: lines 211, 236, 241 and 313 of the v0.27.0 design `1793411151-judgment-where-meaning-is-the-question` | design G6, `trail/rounds/round-1.md:113` | `git show v0.27.0:<design>` to a scratch file; `python3 -I` loading HEAD's `chain_check.py` and `rule_changes.py`, `parse(text, "docs")`, then `check_lines_in` | holds: 22 operations, no parse error; refusals at 211, 236, 241 and 313, each with the grammar's reason; no notice (executed) |
| No tracked file outside `seal/threads/` names `0.27.3` | `trail/phases/phase-2.md:11` | `git grep -n '0\.27\.3' -- ':!seal/threads'` | holds: no match, exit 1 (executed) |
| No other fragment opens with a `<!-- specs/... -->` marker, and the release note writes it | `trail/phases/phase-2.md:5` | `head -1` over every `seal/threads/*/changelog.md`; `.github/scripts/publish_release_note.py:285-296` | holds: each opens with `### Changed` or `### Fixed` (executed); `section` prepends `<!-- specs/{item} -->` (read) |
| `## Removes` names nothing, and the changelog names no removal | `frame/design.md:117-120`, `changelog.md` | read | holds: nothing is to be absent from the tree (read) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | `chain-check` reads each check line inside an `add` or `change` `to` through `rules.py#refused_lines` and `#unread_lines`, refuses at the design line, names a near line as a notice, reads no `from`, ends at exit 2 where the reader will not load or read; `Op.lines` carries the coordinates; the version moves to 0.28.0; removes nothing | the issue's two *Done when* items; the diff (`chain_check.py#check_lines_in`, `rules.py#refused_lines`, `rule_changes.py#value_lines`); the re-runs above | the plan's phase-2 *Verified by* cell says the fragment opens with a `<!-- specs/... -->` marker; the tree contradicts the cell (`publish_release_note.py` writes the marker; no fragment carries one), and the build followed the tree, which phase 2 states and round 1 confirmed. *Scope* item 2 says one case for `refused_lines`; the tree holds two, which round 3 read against `CONTRIBUTING.md`. Neither changes what the work is |
| the build | the diff above, with three names beyond *Data & interfaces* (`CHECK_LINES_READER`, `Unreadable` and `WRITES_A_TO`), each named in phase 1; the class renamed `Test_check_lines_in` in 871a937d5; `ruff.toml` lints `rules.py` at py39 in c990a5fee | the design, the issue, the re-runs | none |
| the last round | round 3 at 871a937d5: no finding; the floor and layout fixes hold; four modules pass, 333 passed | rounds 1 and 2, the build, the re-runs; its target 871a937d5 is followed only by record commits 33419ffe5 and e416e4b4b (executed: `git show --stat`) | none |
| the changelog | `chain-check` reads each check line inside an `add` or `change` `to` through `rules.py`, refuses at its line, names a near line as a notice, reads no `from`, ends at exit 2 where `rules.py` will not load or cannot read; `seal rules --check` reads and prints as before; `Op` carries its lines and `rules.py` gains `refused_lines` | the design, the build, the re-runs (S7 output identical, the exit-2 case passing at HEAD) | none |
| the orchestrator's part of the pull request body | `Closes #1215`; the same change; first pull request into `release/v0.28.0` moving `plugin.json` to 0.28.0; the reader shared, not copied; rounds 1 to 3 as recorded; b0107c66 and 40d08933 add the judgment rows, 40d08933 folds round 1's `to` and closes two `gaps.md` rows; broad run at 33419ffe against 57d6665b | the records: `git show --stat` of b0107c661 (`frame/plan.md`) and 40d089338 (`frame/design.md`, `frame/plan.md`, `gaps.md`), ff6e32dd6 (`plugin.json`, `changelog.md`), c990a5fee (`ruff.toml`) and 871a937d5 (the two test files) (executed); `trail/gate.md` (read) | none |

```seal
target: e416e4b4b against 57d6665b5
Verdict: sealed
```
