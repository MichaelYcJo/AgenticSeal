# Review round 2: 1795397629-git-runs-through-thirty-hand-written-helpers

```seal
target: 64a28d00f8713082e8bd45b24e8b881cb81d8389, fixes 236289e3e..64a28d00f
```

This is a verifying round. Its code range is the two fix commits after `236289e3e`, `ad35f21e4` and `26f8de01a`, and its record range adds `e2379886f`, `dd9233aad` and `64a28d00f`, which touch the work item's records alone. Beside that range, this round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md` whole at the target. No `pr.<lang>.md` stands, since the commit language is English. `seal/parity.json` is not declared.

Carried from round 1 and not established again: the 14-handler census by `git grep` (round 1, finding 1), the ten `check=True` sites (round 1, finding 2), and the S10 to S12 searches (round 1, *Confirmations*). The fix diff adds no handler, no `check=True` site and no process call, so none of those checks is due again.

All four closes hold. One new finding comes from the records the fix pass changed: `gaps.md` *Not verified* does not name the fix pass's cases, which ran on macOS alone.

## Findings

### 1. gaps.md names no Windows row for the fix pass's cases

```seal
severity: should
location: `seal/threads/1795397629-git-runs-through-thirty-hand-written-helpers/gaps.md:13`, `tests/skills/test_test_layout.py:1218`, `tests/github/test_roll_flow_measurement_issue.py:1162`
evidence: read `seal/threads/1795397629-git-runs-through-thirty-hand-written-helpers/gaps.md:5-13` and the close blocks of `trail/rounds/round-1.md` findings 1 and 2
```

Why it matters: `gaps.md` *Not verified* gives one row for each phase, naming the cases that ran on macOS alone and the pull request's Windows leg as their answerer, and the pull request body carries the table to the reviewer. The fix pass added three cases and stated no platform. The phase 5 row (`gaps.md:13`) now misdescribes one of them: it says the new cases of `test_test_layout.py` "make one git or `gh` call time out around real git". `Test_main::test_refuses_a_listing_git_refused_in_one_line` (`test_test_layout.py:1218`) times nothing out. It writes four junk bytes over a real `.git/index` and asserts git's exit 128 and the first words of its `fatal:` line, two facts of git on the platform it runs on. The round 1 close blocks claim red runs, and both name macOS commands alone. The `rule_changes_read` row of S8 falls under the phase 4 row's "the S8 cases", and the two `roll_flow_measurement_issue.py` rows find `gh` through `shutil.which`, as the list case does, so the one row this omission leaves untrue is phase 5's. The fix touches the work item's records alone.

```markdown
<!-- gaps.md, a row after the phase 5 row of *Not verified* -->
| Round 1's fix pass, on the Windows leg: `tests/skills/test_test_layout.py#Test_main::test_refuses_a_listing_git_refused_in_one_line` writes four bytes over a real `.git/index` and asserts that git exits 128, and `tests/github/test_roll_flow_measurement_issue.py#Test_module::test_a_close_or_the_last_create_gh_refuses_stops_the_release` finds `gh` through `shutil.which`. Each ran on macOS alone | the pull request's CI run on its Windows leg |
```

```seal
verdict: fixed 5fa72e29b
answer: The finding holds. The orchestrator inserted the round's row, as given, after the phase 5 row of `gaps.md` *Not verified*; the phase 5 row stays, as its cases do make one call time out. The fix touches the work item's records alone, so the sealer reads it.
```

## Confirmations

```seal
confirms: round-1#1
```

What holds: `chain_check.py:1396-1397` re-raises `GITCMD.Failed` ahead of the `(OSError, SyntaxError, ImportError, SystemExit)` clause, and the docstring of `rule_changes_of` says why. The new S8 row (`test_chain_check.py:4051`, id `rule_changes_read`) asks for the same call the round 1 probe asked for and asserts S8's line, so the row stands in for the probe, which contract rule 7 runs once and this round did not write again. Executed: the ten S8 rows pass at the target. Executed in a scratch clone at the target: `seal mutate` dropping the two re-raise lines is red on `[rule_changes_read]` alone, failing on `chain-check: the rule-changes reader would not load (...)`, the line round 1 found.

```seal
confirms: round-1#2
```

What holds: `test_roll_flow_measurement_issue.py:1155-1184` holds `close_issue`'s and the last create rung's `check=True`, and `test_test_layout.py:1218-1232` holds `_tracked`'s. Each asserts the command and the `Exited` line rather than the snippets' suffix alone. The close row stops at `gh issue close 89`. The create row stops at `gh issue create`, so `find_baseline_issue` and the two best-effort rungs answered through `_ladder_harness` before it. Executed: `tests/github/test_roll_flow_measurement_issue.py` and `tests/skills/test_test_layout.py` pass whole at the target, 127 cases. Executed in the scratch clone: `seal mutate` with `check=False` on the close and on the last rung gave two mutants, both red. With the flag taken out of `_tracked`, the case is red on `assert 1 == 2`, the exit code it names. The `_tracked` paragraph is gone from `gaps.md` *Not done*, and the other two paragraphs stand as round 1 accepted them.

```seal
confirms: round-1#3
```

What holds: read at the target, `frame/design.md:115` no longer names `seal_stamp.py#_git`, `:117` names `seal_stamp.py#main` under `--guarantee`, `:58` says `_git` goes, and `frame/questions.md` Q2's status reads `answered 2026-11-23 by the work: each phase's ruling, in trail/phases/phase-1.md to phase-6.md`. Each matches round 1's text. The six phase records hold the Q2 headings they cite.

```seal
confirms: round-1#4
```

What holds: read at the target, `frame/plan.md:72` is round 1's row on what a gate change carries, and `pr.md:2` quotes its judgment word for word at the coordinate it names. The row's six gates and `seal mode`'s exit 1 match `changelog.md` *Fixed*, and the platform and removal clauses point to rows that stand in `gaps.md` *Not verified* and `changelog.md` *Removed*.

What matched, read against the target: the fix code contradicts no sentence of the seven records read whole. The changelog's line that `chain-check` "now writes its name and the runner's line" holds again on the rule-changes path, and design S8 holds over every row of its case. Each new test covers a unit or a world its group did not cover. The roll rows are the close and the last create, beside the list case that already stood. The layout case is a non-zero listing, beside the `tracked` row that times the same call out. The installed chain check over the working tree printed no notice at a line of `frame/design.md` naming a test pin or a copy.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite, the lint and the typecheck over the whole tree, which this round did not run (contract rule 2) | the `Broad gate` key of `seal/config.json` | the orchestrator's broad run after the rounds settle |
| The five rows of round 1's *Not judged* stand as round 1 wrote them, since the fix diff touches none of their coordinates | `trail/rounds/round-1.md`, *Not judged* | the answerers round 1 names |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the repository into `<scratchpad>/1795397629-git-runs-through-thirty-hand-written-helpers/round-2/clone`, checked out at `64a28d00f` | the clone; `git status --short` in it printed nothing after the three runs below |
| `bin/seal mutate skills/code-review/scripts/chain_check.py --replace` with the two re-raise lines replaced by nothing, `--tests "bin/test -q -p no:xdist -x tests/skills/test_chain_check.py -k rule_changes_read"`, in the clone | red: `[rule_changes_read]` failed on `chain-check: the rule-changes reader would not load (...)`, and the other 18 selected cases passed |
| `bin/seal mutate .github/scripts/roll_flow_measurement_issue.py`, with `check=True` replaced by `check=False` in `close_issue` and then in the last create rung, `--tests "bin/test -q -p no:xdist tests/github/test_roll_flow_measurement_issue.py -k test_a_close_or_the_last_create_gh_refuses_stops_the_release"`, in the clone | `2 mutants, 2 red, 0 SURVIVED` |
| `bin/seal mutate skills/verify/scripts/test_layout.py --replace` with `check=True` taken out of `_tracked`, `--tests "bin/test -q -p no:xdist tests/skills/test_test_layout.py -k test_refuses_a_listing_git_refused_in_one_line"`, in the clone | red: `AssertionError: assert 1 == 2` |
