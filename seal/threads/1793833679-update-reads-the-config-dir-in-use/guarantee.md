# Guarantee: 1793833679-update-reads-the-config-dir-in-use

This audit read the branch at 8d6e9957 against `release/v0.32.2`, which
resolves to 2ecb8d4b through `release/v0.32.2@{upstream}` (executed).
`trail/gate.md` names the run at c438e454. That commit is an ancestor of
HEAD, and `git log --no-merges --name-only c438e454..HEAD ^2ecb8d4b` lists
only `trail/gate.md` of this work item (executed). `seal pr-body <item>
--body <file> --check` exited 0 (executed). `seal/parity.md` is not in git,
so no comparison with an original is owed. `seal/config.md` has no
`Record language` row, so this record is in English. Every re-run of a
`seen red` went in a clone at `<scratchpad>/<work-item-id>/at-base/`, which
was removed after its runs.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| S3, S4 and S5 seen red against the skill before the change: step 2b printed `9.9.0`, step 3 yielded `owner-home/repo-home`, the search named `~/.claude` | `trail/phases/phase-1.md:15` | in the at-base clone at 8d6e9957, `git checkout 2ecb8d4b -- skills/update/SKILL.md`, then `bin/test tests/behaviour/test_update_reads_the_config_directory_in_use.py -q -p no:xdist -k "step_2b_reads or step_3 or no_fixed"` | holds (executed): exit 1, 3 failed. Step 2b failed `'9.9.0' == '9.9.1'`, step 3 failed `'owner-home/repo-home' == 'owner-in-use/repo-in-use'`, and the search named the four fixed paths of `frame/design.md` G1 |
| S1 green before the change, shown red with step 4's argument rewritten to `"$HOME/.claude/CLAUDE.md"`, failing on the `set` branch | `trail/phases/phase-1.md:16` | in the at-base clone, HEAD's skill restored, the argument rewritten by one substitution asserted to match once, then `bin/test tests/behaviour/test_the_old_block_leaves_through_update.py -q -p no:xdist -k config_directory_in_use`; then unmutated | holds (executed): exit 1, the failing line is `AssertionError: set`, the config directory's `CLAUDE.md` still holding `<!-- agentic:start -->`. Unmutated: 1 passed, exit 0 |
| `test_step_2b_prints_no_repair_where_the_record_cannot_be_read` seen red against 7ab6c849's skill, at `assert 0 != 0`, with the `rsync` into `/` in its output | `trail/rounds/round-2.md`, finding 1's close | in the at-base clone, `git checkout 7ab6c849 -- skills/update/SKILL.md`, then `bin/test ... -k no_repair_where` | holds (executed): exit 1, `assert 0 != 0`, the output `mv '' .stale.bak`, an `rsync` whose target is `/`, and `mkdir -p /.in_use`. The block at 7ab6c849 only prints, so nothing ran but `printf` |
| `test_step_2b_prints_the_repair_with_this_sessions_paths` seen red against e4db4f10's skill at `3 == 2`, running nothing | `trail/rounds/round-1.md`, finding 1's close | in the at-base clone, `git checkout e4db4f10 -- skills/update/SKILL.md`, then `bin/test ... -k prints_the_repair_with` | holds (executed): exit 1 at `assert 3 == 2`, the line-count assertion that precedes `run_bash`, so the old repair was not run |
| The two modules of *Scope* 6 pass at HEAD with no case skipped, 17 passed | `trail/rounds/round-3.md`, *Probes* row 1 | in the at-base clone with every file at 8d6e9957, `bin/test tests/behaviour/test_update_reads_the_config_directory_in_use.py tests/behaviour/test_the_old_block_leaves_through_update.py -q -rs -p no:xdist` | holds (executed): 17 passed, exit 0, none skipped |
| S6: the two update cases of the hygiene module pass with no needle changed | `frame/design.md` S6; `trail/phases/phase-1.md:6` | `bin/test tests/behaviour/test_release_hygiene.py -q -p no:xdist -k "test_update_reads_the_installed_copy_before_it_summarises or test_update_shows_what_changed_from_the_github_releases"` at 8d6e9957 | holds (executed): 2 passed, exit 0. `git diff 2ecb8d4b...HEAD --stat` lists no change to that module (executed) |
| `uvx ruff check` and `uvx ruff format --check` over the two test modules exit 0 | `trail/phases/phase-1.md:19` | both commands at 8d6e9957 | holds (executed): exit 0 each |
| `.claude-plugin/plugin.json`'s `version` reads `0.32.2`, and no other copy of `0.32.1` stands | `trail/phases/phase-1.md:34`; `trail/rounds/round-1.md`, *Confirmations* | `python3 -c` reading the field; `git grep -n -F 0.32.1` outside `seal/threads/`, `CHANGELOG.md` and `.test_durations` | holds (executed): `0.32.2`; the search lists nothing |
| The diff touches only the skill, the two test modules, `plugin.json` and the work item's records | `frame/plan.md` *Phases*, phase 1's Verified by cell | `git diff --stat 2ecb8d4b...HEAD` | holds (executed): `skills/update/SKILL.md`, the two modules, `.claude-plugin/plugin.json` and files under the work item's directory |
| `## Removes`, row 1: no fixed `~/.claude` home of the plugins stands in the skill | `frame/design.md` *Removes* | a `python3 -c` run of `\S*/\.claude(?![-\w])\S*` over the skill at HEAD with `${CLAUDE_CONFIG_DIR:-$HOME/.claude}` removed | holds (executed): no hit |
| `## Removes`, row 2: `os.path.expanduser` and the `os` import leave step 2b's program | `frame/design.md` *Removes* | `git grep -n -E "expanduser\|import json,os" -- skills/update` | holds (executed): no hit |
| `## Removes`, row 3, and the phase's extra removal: `USER_FILE`, `assert args == USER_FILE` and `COMMAND`'s `args` group | `frame/design.md` *Removes*; `trail/phases/phase-1.md:44` | `git grep -n -E "USER_FILE\|P<args>\|args == " -- tests/behaviour/test_the_old_block_leaves_through_update.py`, and `git grep -n -F USER_FILE -- tests skills` | holds (executed): no hit in either |
| The changelog's removal: the repair the user typed from `$p` | `changelog.md:3` | `git grep -n -F -e 'mv "$p"' -e "rsync -a --exclude '.git'" -- skills` | holds (executed): no hit. The diff replaces the three lines with the printing block (read) |
| Run 41935909883 of `tests` concluded `success` at f8ed5efc on four Windows, three macOS and one ubuntu `pytest` legs | pull request body, line 19 | `gh run view 41935909883 --json headSha,conclusion,workflowName,jobs` | holds (executed): `tests`, `success`, head f8ed5efc, the eight `pytest` legs as the body counts them |
| The broad run's printed lines | pull request body, line 21 | read of the run's log beside the body file | holds (read): `BROAD GATE PASSED ... @ c438e454 against origin/release/v0.32.2 @ 2ecb8d4b`, `suite ✓ 6354 passed · 12 skipped`, `chain ✓ exit 0`. The count is the run's output, which this audit did not re-run (contract rule 2) |
| #1367 is open and names the readers of *Scope*'s first *Out* item | `frame/plan.md` *Judgments of the run*, the last row; pull request body, line 7 | `gh issue view 1367 --json title,state,body` | holds (executed): open, it names `hooks/lib/press.py:30`, `session_cost.py:83`, `payload_meter.py:405` and `:424`, and the two prose lines. Its body says `hooks/question-gate.py` and `hooks/routing-edit-gate.py` import `press`, which `git grep` confirms at `:48` and `:54` (executed), so the body's "two hooks" holds |
| This is the first pull request into `release/v0.32.2` | pull request body, line 9 | `gh pr list --base release/v0.32.2 --state all --json number,title,state,headRefName`; `gh pr view 1369 --json files,createdAt` | does not hold (executed): #1369, #1190's pull request, is open into `release/v0.32.2`, created 2026-11-04T23:39:07Z, and this work item's pull request is not yet open. #1369's files do not include `.claude-plugin/plugin.json` |
| #1368 is the frame-dating prevention home in this release | pull request body, line 15 | `gh issue view 1368 --json milestone,state`; `gh issue list --milestone "release: 0.32.2" --state all` | does not hold (executed): #1368 is open with no milestone, and the `release: 0.32.2` milestone holds #1184, #1185 and #1190 alone |
| The orchestrator's measurement under `CLAUDE_CONFIG_DIR="$HOME/.claude" claude -p` printed `Not logged in` | pull request body, line 17 | none | unverified: no record holds the run, and this audit did not repeat it. `gaps.md` keeps the inheritance question open for the orchestrator |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | Every command of `skills/update/SKILL.md` spells the directory `${CLAUDE_CONFIG_DIR:-$HOME/.claude}`. A sentence before step 1 says why. Cases 6a to 6f run each command under a scratch config directory. Three removals. An empty variable, an empty `installPath` and Windows are limits. The work item carries the version move | the issue's two *Done when* items, read against the tree: no fixed path is left in the skill (executed above), and `test_step_4_takes_the_block_out_of_the_config_directory_in_use` runs step 4 under a scratch `CLAUDE_CONFIG_DIR` and reads the block written there (executed above). G7 explains why the issue's "diff" is now step 4's take-out. The build, the rounds and the changelog | none of the parties. Its G10 cites `skills/implement/orchestration.md` *Which branch the pull request lands on is decided with the routing question* for the version move, a rule naming the first pull request into the branch. Which pull request carries the move is the framer's and the owner's choice (`routing.md`), not judged here |
| the build | The diff and `trail/phases/phase-1.md`: the four coordinates of G1 rewritten to the one spelling, the procedure sentence added, step 2b's repair printed by a block that reads the record behind `&&`, a table row for a read that raised, the cases of *Scope* 6 and the version move | the design's *Data & interfaces*, line for line (read in the diff). Every `seen red` sampled holds. Every removal is absent from the tree | none |
| the last round | `trail/rounds/round-3.md` at fbcd2f26: round 2's regression is closed, nothing is opened, and three gaps are named that are not findings | the tree: the `&&` at the read, the table's last row, the two modules green (executed above). c438e454 after it touches only `frame/design.md` and `frame/plan.md`, and it states round 3's two limits and S8's unpinned half as round 3 named them (read in `git show c438e454`) | none |
| the changelog | One `### Fixed` entry: under `CLAUDE_CONFIG_DIR` the update read files under `~/.claude`; every command now spells the config directory; the repair is printed with the paths written out, prints nothing on a failed read, and the table says to stop; an empty variable is a limit | the diff and the design. The base's skill held `mv "$p"` and the `rsync` to `"$p/"` (read in the diff), so "copied into `/`" states the base's defect | none |
| the orchestrator's part of the pull request body | Body lines 1-21: what the changelog says, the repair, #1367, the version move, the review chain, the platforms and the broad run | the changelog, the rounds, #1367, run 41935909883 and the broad run's log, each as the rows above give them | the tracker, twice. Line 9 says this is "the first pull request into `release/v0.32.2`", where #1369 is already open into that branch. Line 15 says #1368 is the prevention home "in this release", where #1368 carries no milestone and `release: 0.32.2` holds three issues, #1368 not among them |

```seal
target: 8d6e9957 against 2ecb8d4b
Verdict: withheld reason: the orchestrator's part of the pull request body states two things the tracker contradicts. Line 9 says this pull request moves the version "as the first pull request into release/v0.32.2", where gh pr list --base release/v0.32.2 shows #1369 already open into that branch, created 2026-11-04T23:39:07Z, without .claude-plugin/plugin.json, and frame/plan.md Phases, the line's own citation, says only that this work item carries the move. Line 15 says "its prevention home in this release is #1368", where #1368 has no milestone and the release: 0.32.2 milestone holds #1184, #1185 and #1190 alone. Every other claim sampled and every other party holds at 8d6e9957
```

## Re-audit at 530928d9

This audit read the branch at 530928d9 against `release/v0.32.2`, which
resolves to 2ecb8d4b through `release/v0.32.2@{upstream}` (executed).
`trail/gate.md` still names the run at c438e454, an ancestor of HEAD, and
`git log --no-merges --name-only c438e454..HEAD ^2ecb8d4b` lists only
`trail/gate.md` at 8d6e9957 and `guarantee.md` at 530928d9, both of this
work item (executed). `seal pr-body <item> --body <file> --check` exited 0
on the repaired body (executed). `git diff --stat 8d6e9957 530928d9` lists
`guarantee.md` alone (executed), so no coordinate of the earlier run's
claims changed, and those claims stand as the block above records them
without a re-run. The repair touched the body file, so this run re-runs the
body's two corrected sentences and reads every party again.

### Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| This work item carries the release's version move, cited to `frame/design.md` G10 | pull request body, line 9 | read of `frame/design.md:18` (G10) and `routing.md` *Why this way* | holds (read): G10 says "This work item carries the version move to 0.32.2", and `routing.md` says the same. The body no longer says this is the first pull request into the branch |
| #1190 and #1185 leave the version alone | pull request body, line 9 | `gh pr view 1369 --json files`; `git diff --name-only 2ecb8d4b...fix/1190-a-first-input-seal-core-reads-as-no-such-session -- .claude-plugin` (local and `origin` both at 2bc9d32f); the same over `fix/1185-payload-charges-an-import-inside-a-fence` (local at 9696913a, no remote branch) | holds (executed): #1369's files are `core_check.py`, its test and #1190's records, and neither branch's diff touches `.claude-plugin/`. G10 states the half of this that the frame read: #1190 holds `core_check.py` and #1185 holds `payload_meter.py` |
| The dating of the frame's pre-build coordinates is a row of `frame/plan.md` *Judgments of the run* | pull request body, line 15 | read of `frame/plan.md:40` | holds (read): the row of 2026-11-05 dates the coordinates to 475d018c and states its grounds |
| The same fold recurred on #1190 in this run | pull request body, line 15 | `git show fix/1190-a-first-input-seal-core-reads-as-no-such-session:seal/threads/1793833680-a-transcript-not-yet-written-is-named/frame/plan.md` | holds (executed): its *Judgments of the run* row of 2026-11-05, at line 41, dates that frame's coordinates to 920a9584 on the same grounds |
| The orchestrator filed #1368 as that fold's prevention home, and the issue's body names both work items | pull request body, line 15 | `gh issue view 1368 --json number,title,state,milestone,body,author,createdAt` | holds (executed): #1368 is open, created 2026-11-04T23:29:59Z, and its body names #1190 and #1184 and both work items' `frame/plan.md`, and asks where the prevention belongs. It is filed under the account the run works under, so who typed it is not read from the tracker. The body no longer says "in this release", and #1368 still has no milestone |
| The orchestrator's attempt under `CLAUDE_CONFIG_DIR="$HOME/.claude" claude -p` printed `Not logged in` | pull request body, line 17 | none | unverified: the spawn prompt says the orchestrator ran it in this session, and no record holds the run. This audit did not repeat it, since `claude -p` starts a session and contract rule 6 withholds spawning one. The orchestrator answers it. The sentence reports a measurement not made, and `gaps.md` keeps the inheritance question open for the orchestrator |

### The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | as the earlier block's row: `frame/design.md` is unchanged since 8d6e9957 (executed, `git diff --stat 8d6e9957 530928d9`) | as the earlier block's row, and G10 now with the body's line 9 | none |
| the build | as the earlier block's row: no file of the diff outside `guarantee.md` changed since 8d6e9957 (executed, the same command) | as the earlier block's row | none |
| the last round | `trail/rounds/round-3.md` at fbcd2f26, unchanged | as the earlier block's row | none |
| the changelog | `changelog.md`, unchanged: one `### Fixed` entry, read again in full | the diff and the design, as the earlier block's row; the body's line 1 and line 5, which copy its sentences | none |
| the orchestrator's part of the pull request body | Body lines 1-21, with line 9 and line 15 rewritten. Read again in full against the records | the changelog (lines 1, 5), `frame/design.md` *Out* and #1367 (line 7), G10, `routing.md` and the two sibling branches (line 9), `frame/plan.md` *Alternatives considered* and *Judgments of the run* and the three rounds (lines 12-15), `gaps.md` (line 17), run 41935909883 and the broad run's log as the earlier block records them (lines 19, 21) | none. Line 17's attempt is unverified, as the row above says, and no record or fact contradicts it |

```seal
target: 530928d9 against 2ecb8d4b
Verdict: sealed
```
