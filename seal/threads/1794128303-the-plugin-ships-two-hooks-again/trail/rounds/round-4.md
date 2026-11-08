# Review round 4: 1794128303-the-plugin-ships-two-hooks-again

```seal
target: 4f6691149, fixes 9cec57f87..4f6691149
```

This is the verifying round. The code under review is the diff of round 3's
fixes, `9cec57f87..4f6691149`. It holds `7192e400c` (round 3's record),
`fc6405ddb` (the orchestrator's rewrite of three frame cells and the
`pr.md:8` quote), `d39edd697` (the fix pass's rewrite of the `lib/launch.py`
docstring) and `4f6691149` (round 3's two close blocks). No test is added
or changed in the range, so no new case is read against its group. Beside
the diff, the round read the work item's records that state the present,
each whole at `4f6691149`: `routing.md`, `frame/design.md`, `frame/plan.md`,
`frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`. It read
`trail/rounds/round-3.md` whole and the earlier rounds and phase records for
their coordinates.

Facts carried from earlier rounds and not re-derived: the parse of the hook
scripts under the 3.7 and 3.8 grammars (round 1), and round 3's
confirmation that each command in `hooks/hooks.json` ends with ` || exit 0`
and exits 0 where its script cannot be opened. Neither stands in this diff,
and `hooks/hooks.json` is unchanged in it. Re-derived this round: the cell
count of every table row in the work item's directory, the settle's read of
*Judgments of the run*, each `pr.md` quote in its source, and the docstring's
new reason against the code it names (`## Probes`).

The axes were the two closes and the units the diff adds. The first unit is
the four rewritten cells, read for what they say and for how a table reader
splits them. The second is the docstring paragraph at `lib/launch.py:33-40`,
read for each claim it makes against `lib/launch.py`, `ruff.toml` and
`CONTRIBUTING.md`, and for any other statement of the same reason in the
tree. The last is round 3's record and its close blocks, read as records.
The cell count covers every tracked file of the work item's directory plus
`lib/launch.py`, which is a closed set.

## Findings

None. Both of round 3's closes hold, and the units the fix diff adds hold
no defect this round found.

## Confirmations

```seal
confirms: round-3#1
```
What holds: round 3 claimed that `frame/design.md:23-24`, `frame/plan.md:68`
and the `pr.md:8` quote held an unescaped `||`. At `4f6691149` the three
cells read "ends with a closing `exit 0`" and "before their closing
`exit 0`", and no pipe stands in them (read: `frame/design.md:23`,
`frame/design.md:24`, `frame/plan.md:68`). A count of the cells of every
table row, split on unescaped pipes, against each table's header finds no
row off its header in any record that states the present (executed,
`## Probes`). `settle.py#plan_rows` over `frame/plan.md` now reads all five
rows, `:65` to `:69`, with nothing unread, where round 3 got three rows and
a refusal at `:68` (executed). Each of the nine quotes in `pr.md` stands word
for word in the source its coordinate names, with runs of whitespace
collapsed, `:8` against `frame/design.md:23` included (executed). The
reworded cells keep the fact: `hooks/hooks.json:8` and `:19` each end with
` || exit 0`, and "a closing `exit 0`" names that last part with no pipe in
it, as `gaps.md:12` and `changelog.md:3` already word it (read). The
acceptance row at `frame/design.md:69` spells the shape with escaped pipes,
`\|\| exit 0`, and its count matches its header (executed).

```seal
confirms: round-3#2
```
What holds: the fix pass claimed that the docstring now gives the floor as
the reason the hooks do not run through the launcher. `lib/launch.py:35-40`
says that each script `hooks/hooks.json` names runs on whatever `python3`
starts it, 3.9 on a stock Mac. It also says that the launcher refuses
anything below `FLOOR` before the script is read, and that behind the
closing ` || exit 0` that refusal would end in exit 0, so the core would not
print and the stamp would not draw. Each claim matches the code it rests
on. `FLOOR` is `(3, 12)` (`lib/launch.py:49`). The launcher exits 2 below it
before the script is read (`lib/launch.py:19-21`). The scripts the hook
commands run are linted at 3.9 because they run on whatever `python3` starts
them, and macOS ships 3.9 under that name (`ruff.toml:32-35`, `ruff.toml:44`,
`ruff.toml:46`, `CONTRIBUTING.md:118-121`). With `py` absent, a 2 from the
`python3` half falls through the failing `py -3` half to `exit 0`
(`hooks/hooks.json:8`, `:19`). The citation `ruff.toml` *per-file-target-version*
names the table at `ruff.toml:42` (read). The fix pass changed round 3's
"that refusal would reach nobody ... with nothing to say so" into "that
refusal would end in exit 0". Its grounds are that the tree records nothing
on whether Claude Code shows a hook's stderr at exit 0. That holds: round 3
itself left that question unrun (its *Observed, no finding* paragraph), and
the new clause claims only the exit, which the command shape decides. The
sentence holds one reason and no longer sets the closing ` || exit 0` beside
the exit 2 as though they still conflicted.

The fix pass also claimed that its wider search found no other statement of
the reason. The same `git grep` at `4f6691149` lists five lines (executed).
`lib/launch.py:35` is the docstring itself. `CONTRIBUTING.md:119` lists the
hook scripts among what runs before any floor, which is the same fact and
agrees. `.github/scripts/run_tests.py:80` and `tests/lib/test_launch.py:200`
are about `bin/test` and a wrapper. `tests/behaviour/test_chain_hooks_hardening.py:51`
names the floor derivation in the removal list. None states a reason that
contradicts the new one. No case pins the docstring's wording, and the
suite's modules that read the launcher pass: `tests/lib/test_launch.py` and
`tests/behaviour/test_chain_hooks_hardening.py`, 39 passed (executed).

What matched: the records that state the present, read whole at the target,
contradict nothing the target holds. `routing.md` names the branch under
review. `frame/questions.md:9` says both commands end with ` || exit 0` and
the second half runs wherever the first exits non-zero, which is how `sh`
runs `hooks/hooks.json:8` and `:19`. `gaps.md` keeps its six rows, the last
marked `closed` in place, and the range does not touch it (read:
`git diff --stat 9cec57f87..4f6691149`). `changelog.md:3` spells each command
as `hooks/hooks.json` holds it.

Observed, no finding: `trail/rounds/round-3.md:231`, round 3's own
`## Not judged` row on the Windows shell, holds an unescaped `||` inside a
code span. That is the class round 3's finding 1 named, and a GitHub
rendering cuts that row's *Location* and *Who answers* cells. A round
record states the commit it names and is no record of the present. No
script reads a `## Not judged` table (executed: `git grep -n "Not judged" --
'*.py'` lists only an eval fixture's heading). An agent reads the raw text,
where the row is whole. The question it names also stands as `gaps.md:8`
and `frame/questions.md` Q1. So the row loses no party anything at a step.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite, the repository-wide lint and the typecheck. This round ran two modules and `seal rules --check` only, and ruff did not run over `lib/launch.py`, since no `ruff` is on this machine's path. The suite is `unverified` at the target | the work item | the orchestrator, at its one broad run after the rounds settle |
| Whether the shell the harness uses on Windows runs the closing `exit 0` as `sh` does, and whether the `py -3` half starts there; carried from round 3, and this diff does not touch it | `hooks/hooks.json:8`, `hooks/hooks.json:19` | the owner, or a Windows user, with `frame/questions.md` Q1 |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/lib/test_launch.py tests/behaviour/test_chain_hooks_hardening.py -q -p no:randomly` | exit 0, 39 passed |
| `bin/seal rules --check` | exit 0 |
| one probe file under the round's scratch directory, run once with `python3 -I`, deleted afterwards: the cells of every table row in each tracked file of the work item's directory and `lib/launch.py`, split on unescaped pipes and counted against each table's header | one row off its header, `trail/rounds/round-3.md:231` (5 cells, header 3); none in the records that state the present |
| the same file: `settle.py#plan_rows` over `frame/plan.md`, loaded by path | five rows read, `:65` to `:69`, nothing unread |
| the same file: each quote of `pr.md`, looked up in its named source with runs of whitespace collapsed | nine of nine found |
| `git grep -n -i "run through it\|not run through\|through the launcher\|harness's word for keeping\|hooks.*launch\.py" -- . ':!seal/threads'` | five lines: `.github/scripts/run_tests.py:80`, `CONTRIBUTING.md:119`, `lib/launch.py:35`, `tests/behaviour/test_chain_hooks_hardening.py:51`, `tests/lib/test_launch.py:200` |
