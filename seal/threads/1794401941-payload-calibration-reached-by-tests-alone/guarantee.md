# Guarantee: 1794401941-payload-calibration-reached-by-tests-alone

The audit read the tree at `83f965689`, against the base
`release/v0.37.4@{upstream}`, which resolves to `52f87b8d3`. The local
`release/v0.37.4` ref resolves to `18a7e18fb` and was not used.
`trail/gate.md` names the run at `482bf293a`. That commit is an ancestor of
HEAD, and the only commit after it, `83f965689`, touches
`seal/threads/1794401941-payload-calibration-reached-by-tests-alone/trail/gate.md`
alone (executed: `git log --no-merges --name-only 482bf293a..HEAD ^52f87b8d3`).
`seal pr-body <item> --body <the orchestrator's body file> --check` exited 0
(executed). Every re-run below ran in `<scratch>/at-base/`, a
`git clone --no-local` of the branch at `83f965689`. Each edit made there
for a mutant was restored with `git checkout HEAD -- <file>`, and
`git status --short` printed nothing afterwards (executed). The tree under
audit was not changed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The three cases that pin the printed label and the pair line failed against the base's labels (`seen red`) | `trail/phases/phase-1.md:52-61` | base `payload_meter.py` and `release_report.py` restored from `52f87b8d3`, HEAD's tests kept; `bin/test tests/skills/test_payload_meter.py -q -p no:xdist -k "harness_share or session_as_an_object or reads_estimated_at_the_assumed"` | holds: exit 1, 3 failed. The pair-line case failed on "… nothing calibrated) — inside every agent's prefix, the baseline's included". The session case failed on "from assumed — no transcript calibrates a session". The token case failed on "from assumed — nothing calibrated". Each failing line is the label the case names. |
| `test_refuses_a_root_that_defines_no_agent` was shown red with its one guard removed (`seen red`) | `trail/phases/phase-1.md:33-37` | HEAD's code, `if not data["agents"]:` in `main` replaced by `if False:`; `bin/test tests/skills/test_payload_meter.py -q -p no:xdist -k test_refuses_a_root_that_defines_no_agent` | holds: exit 1, failed on `assert done.returncode == 1` with a return code of 0, which is the guard the case names. The case passes at HEAD with the guard in place (exit 0). |
| The two stamp cases that call the moved `strip_ansi` depend on it (`executed`) | `trail/phases/phase-2.md:45-50` | `tests/skills/test_seal_stamp.py#strip_ansi` body replaced by `return s`; `bin/test tests/skills/test_seal_stamp.py -q -p no:xdist -k "test_accepts_the_owners_reference_cell_for_cell or test_accepts_a_value_as_wide_as_the_panel_at_eighty_columns"` | holds: exit 1, both failed, the first on `len(text) == len(twin)` (140 against 68), the second on `widest == 80` (715). The helper's `SGR` pattern at `tests/skills/test_seal_stamp.py:43` is the literal the base body at `seal_stamp.py:497` wrote (read). |
| S1: each removed flag is refused with exit 2 and no table (`executed`) | `trail/phases/phase-1.md:73-75` | `bin/seal payload` with `--calibrate x`, `--baseline-agent x`, `--baseline x` and `--sections`, each exit code read directly | holds: exit 2 each, 0 bytes on stdout, stderr ending `unrecognized arguments: <the flag>`. |
| S2: the JSON names no removed path, every row is its bytes over 3.2, every total the sum of its rows, one basis label (`executed`) | `trail/phases/phase-1.md:76-79`; `changelog.md:3` | `bin/seal payload --json`, read with `python3 -I -c` | holds: exit 0; top-level keys `agents`, `measured_at`, `root`, `session`; six tables, each holding `files` and `total` alone; no row holds `sections`; every row `round(bytes / 3.2)`; every total the sum of its rows' tokens; the one basis `estimated (3.2 B/token, an assumed ratio)`. |
| The `CLAUDE.md` pair line is the sum of the pair's file figures and ends "inside every agent's prefix" (`executed`) | `changelog.md:3`; `trail/rounds/round-3.md`, the confirmation of round-2#1 | `bin/seal payload`, its text read | holds: exit 0; the session rows read 362 and 488 tokens, and each of the five pair lines reads 2,717 bytes and 850 tokens, ending `— inside every agent's prefix`. |
| S3: the release report prints the same table at the base and at the build (`executed`) | `trail/phases/phase-1.md:79-85`; `changelog.md:3`; issue #1484 *Done when* | `git archive v0.37.3` unpacked to `<scratch>/sealer/at/`; `python3 .github/scripts/release_report.py --against v0.37.3 --at <that dir>` at `83f965689` and at `52f87b8d3` in the clone, then `diff` | holds: both exit 0, 3,056 bytes each, `diff` exit 0. The five preload rows read crafter 30,828, framer 35,884, proofer 31,474, sealer 31,866 and tracer 24,148 bytes, each `+0`, as design G5 gives. |
| S4: vulture names none of the five symbols (`executed`) | `trail/phases/phase-2.md:67-71`; issue #1484 *Done when* | `uvx vulture --min-confidence 60 agents bin evals hooks lib skills .github` at `83f965689` and at `52f87b8d3` in the clone | holds: exit 3 at both; 20 lines at HEAD naming none of the five, 25 at the base, where the five extra lines are exactly `closed_fence_lines`, `parity_config`, `stray_rounds`, `DISC_COLOURS` and `strip_ansi`. |
| The plan rows' narrow runs pass (`executed`) | `frame/plan.md` *Phases*, rows 1 and 2 | `bin/test` over the eleven files the two rows and the rider case name, `-q` | holds: exit 0, 567 passed. |
| Every `## Removes` row of `frame/design.md` and every removal `changelog.md` names stands nowhere in the tree | `frame/design.md:86-104`; `changelog.md:7-8` | `git grep -n -w <name> -- ':!seal/threads'` for each removed unit, constant, fixture and test name the rows list (37 names), and `grep -n -w 'def stamp\|itertools\|transcript'` over the meter and its test file | holds: no hit for any removed name. Three hits are other modules' own names and not the removed units: `_rows` in `tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py` and `sections_of` at `skills/code-review/scripts/chain_check.py:688`, `:700` (read). `strip_ansi` stands only at `tests/skills/test_seal_stamp.py:275`, `:821` and `:862`, where *Scope* item 12 and the issue put it. Every `--baseline` hit outside the meter is `chain_check.py`'s own flag (read). `docs/running/the-agent-set.md:163` still says "split at headings"; it changes through the design's `## Rule changes` at the settle, not in this diff (read). |

Not re-run, by choice of the sample: phase 1's five `seal mutate` mutants of
`payload_meter.py` (`trail/phases/phase-1.md:63-71`), which the three
label cases and the refuses case above cover in part; phase 2's boundary
run counts (`trail/phases/phase-2.md:73-95`), which the broad gate at
`482bf293a` answers. Both are `unverified` here. The Windows run of
`test_refuses_a_root_that_defines_no_agent`, which every round left to the
Windows leg of CI, is `unverified`, and the orchestrator answers it from
that leg.

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | `seal payload` loses `--calibrate`, `--baseline-agent`, `--baseline` and `--sections` with every unit only they reach; one basis label; `composition` takes four arguments; the five symbols go, `strip_ansi` into the test file; `## Removes` lists 15 rows | the issue's *Decision* and title, which put `--baseline` inside the cut (G2); the diff (read: `git diff 52f87b8d3...HEAD`); the tree, per the `## Removes` row above | none |
| the build | phase 1 builds *Scope* items 1 to 7 at `2ec7b9776`, phase 2 items 8 to 12 at `1e3c11fb7`; each departure from the frame is named with its grounds (the added refuses case, the `SGR` body, the rider case and the docstring sentence) and was folded at `bb11563b9` | the design after that fold; the diff; the re-runs above. `routing.md` names `crafter`, and both phases whose Status cell holds a commit have their record (read). Both Status commits exist with their phases' subjects (executed: `git log -1`) | none |
| the last round | round 3 at `248d1fd5a`: no finding, and it confirms round 2's close. It holds no `fixed` finding, so no fix pass waits on this audit | the tree: S1, S2, S3 and S4 hold here as rounds 1 to 3 recorded them, and the pair line and totals are sums as round 3 states | none |
| the changelog | four flags refused with exit 2; JSON keys removed; one estimate per file, the pair line and totals as sums; README rows name `--json`, `--agent <name>` and `--root <dir>`; the release report prints the same table and calls `composition` with four arguments; the five symbols go | the S1, S2, S3 and S4 re-runs; the README diff and `release_report.py:148` (read) | none |
| the orchestrator's part of the pull request body | nine quotes of `frame/plan.md` and `Closes #1484.`; no sentence of its own account. No `pr.<lang>.md` stands, and none is owed, since `seal/config.json` names English for both language keys | `frame/plan.md`: all nine quotes found word for word, whitespace collapsed (executed: `python3 -I -c` over `pr.md`); `routing.md` *Why this way*, whose grounds name a removal touching the path `release_report.py` reads, which the diff does at one call | none |

`seal/parity.json` is not carried by git (executed: `git ls-files`), so no
comparison with an original is owed.

```seal
target: 83f965689 against 52f87b8d3
Verdict: sealed
```
