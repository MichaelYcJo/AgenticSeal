# Phase 1: 1794401941-payload-calibration-reached-by-tests-alone

## What this phase found

**The frame holds against the tree at `f6ef34a4d`, except the ground for
one rewrite in *Scope* item 6.** Every coordinate `frame/design.md`
*Removes* names for phase 1 stood where it says (read), and the five
callers and citations of *Data & interfaces* and G13 were the only ones
(executed: `git grep -n -w` on each removed name outside the meter and its
test file, with hits only for `heading_starts` at the four places G13
lists). *Scope* item 6 says `tests/skills/test_payload_meter.py` holds no
reader's line-end case after this work. It does:
`Test_measure::test_a_frontmatter_line_ends_only_where_yaml_ends_it` (#1198)
pins that a `skills:` entry holding U+2028 is one entry (read). So the
docstring of `tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py`,
which names that file among those holding a reader's own line-end case,
stays true, and this phase leaves it as it stands. Judged against
`skills/core/SKILL.md` *The rule a mechanism is kept against*: a change
removes what stood on the old fact, and nothing in that sentence stood on
the case this phase removes. The test file's own docstring named the
removed U+2028 heading case, and that sentence is rewritten.

**`Test_measure` gains one case the frame does not name,
`test_refuses_a_root_that_defines_no_agent`.** The class's only
`test_refuses_` case was `test_refuses_a_transcript_that_never_spawned_the_baseline_agent`,
which *Removes* takes. `bin/seal layout --check tests` then refused the file
with `class Test_measure has no test_refuses_ case` (executed: the phase
boundary run at `df51518a5` failed
`tests/behaviour/test_this_repository_passes_its_own_checks.py::Test_seal_layout::test_accepts_this_repositorys_tests`).
`CONTRIBUTING.md` *The test layout* asks each class for both cases. No case
held `main`'s exit 1 for a root without `agents/*.md` (executed:
`git grep -n 'no agents/\|returncode == 1'` over the meter's two test files,
no hit), so the new case covers what its group did not. It was seen red
with only its guard removed: `seal mutate` replaced `if not data["agents"]:`
in `main` with `if False:`, and the case failed on
`assert done.returncode == 1` with a return code of 0 (executed, verdict
`red`). `bin/seal layout --pairs tests/skills/test_payload_meter.py` names
four pairs, each between two `Test_imports_of` cases this phase did not
touch (executed).

**One basis label, and one helper that gives every row its estimate.**
`BASIS` reads `estimated (3.2 B/token, an assumed ratio)`. With the
calibration gone, the session's block that set each row's tokens and basis
and the agents' block did the same thing, so both call `_estimated`, which
sets each row's tokens to its bytes over `ASSUMED_RATIO` and sums the
total. Judged against *Scope* item 2, which asks for one label on every
token figure. The last loop of
`test_every_token_figure_reads_estimated_at_the_assumed_ratio` reads
`startswith(BASIS)` rather than *Scope* item 5's "`estimated` alone",
because S5 asks that every token cell's basis be the one label.

**The three cases that pin what a person reads were seen red against the
old labels before the meter changed** (executed: `bin/test
tests/skills/test_payload_meter.py -q -p no:xdist -k "harness_share or
session_as_an_object or reads_estimated_at_the_assumed"` at `f6ef34a4d`
with the edited cases, 3 failed). The pair line failed on
`pair_line[4] == f"{BASIS} — inside every agent's prefix"` against "…
nothing calibrated) — inside every agent's prefix, the baseline's
included". The session case failed on `row["basis"] == BASIS` against
"from assumed — no transcript calibrates a session", and the token case
on the same assert against "from assumed — nothing calibrated".

**Five mutants of the units that add behaviour each went red** (executed:
one `seal mutate` call over `skills/verify/scripts/payload_meter.py` with
`--tests "bin/test tests/skills/test_payload_meter.py -q -x -p no:xdist"`,
exit 0, 5 red). The mutants were the old wording in `BASIS`, the old pair
line, a ratio of 3 in `_estimated`, a plain total basis in `_estimated`,
and `measure` building an agent without `_estimated`. Run alone, the pair
line mutant failed only
`test_the_claude_md_pair_is_marked_as_the_harness_share` (executed). The
tree was clean after each restore (executed: `git status --short`).

**The scenarios, as run.** S1: `bin/seal payload` with `--calibrate x`,
`--baseline-agent x`, `--baseline x` and `--sections` each exited 2 with
argparse's `unrecognized arguments` line and printed nothing (executed).
S2: `--json` on this tree exited 0, its top-level keys were
`measured_at`, `root`, `session` and `agents`, each agent held `files` and
`total` alone, no row held `sections`, and every basis was `BASIS`
(executed, read with `python3 -c`). S3 was measured in the worktree, not in
two clones as the scenario words it: at `f6ef34a4d`, whose diff from
`918342dc0` is the three frame files, and at `df51518a5` with nothing
uncommitted, both against one `git archive v0.37.3` unpacked under this
phase's scratch directory. The two outputs were 3,056 bytes each and
`diff` printed nothing (executed). The preload rows matched G5. S6 passed
in the plan row's narrow run (executed). S7: each README's `seal payload`
row names `--json`, `--agent` and `--root` (executed: the `git grep`).

**What phase 2 needs.** The comment at `lib/lines.py:28-33` still names
`closed_fence_lines`, which phase 2 removes. `heading_starts` is gone from
it. Phase 2 can start from this phase's last commit.
