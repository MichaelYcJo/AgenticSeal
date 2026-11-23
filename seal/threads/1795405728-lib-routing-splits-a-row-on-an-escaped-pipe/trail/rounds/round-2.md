# Review round 2: 1795405728-lib-routing-splits-a-row-on-an-escaped-pipe

```seal
target: 9603d3fed74c634ff7bfc78ffb93a6b9f8c447ce, fixes c47db7a14..9603d3fed
```

A verifying round. The range holds the round-1 record (`8ad946d10`), the
orchestrator's fix of findings 1, 2 and 4 (`9a06f602f`) and its close
blocks (`22f968ef6`), the crafter's fix of finding 3 (`b6425753e`) and its
close block (`feb1a87ee`), and the merge of `release/v0.38.6` after #1573
(`9603d3fed`). The work item's `routing.md`, `frame/design.md`,
`frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and
`pr.md` were read whole at the target.

Carried from round 1, not re-run: its probe `test_tmp_round1.py` for the
base's fence rule and the even-run row, its S7 probe, and its scans of the
tracked `.md` files. The fix commits change no code under `lib/` or
`skills/`, so none of those readings could move. The merge brings in
#1573's changes to `lib/routing.py`, `chain_check.py` and `pact_check.py`.
#1573's own rounds reviewed those changes. This round read only where they
meet this work's.

## Findings

None. Every finding round 1 closed holds, and the merge's resolution holds.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the three statements now name the even-run row. In
`frame/design.md:73`, *Data & interfaces* lists three shapes no committed
declaration holds, the even-run row among them. In `frame/plan.md:52`,
*Operational impact* says how `lib/gaps.py`, `fold_check.py#index_rows` and
`lib/routing.py` each now treat that row. `changelog.md:11` is the new
`### Changed` bullet. Each matches the code at the target:
`lib/tables.py#table_cells` still returns None on `EVEN_ESCAPED_PIPE`, and
the fix commits change no file under `lib/` (read,
`git diff c47db7a14 feb1a87ee`). The fix touches the work item's records
alone.

```seal
confirms: round-1#2
```
What holds: the Judgment cell of the row on what the gate change carries
now names each gate's direction (`frame/plan.md:59`). It says `seal pact`
and the settle's judgments reading allow more. It says `seal unverified`,
`settle --apply` and `seal fold` block more, and that `chain-check` moves
both ways. The Grounds cell answers *What it reads* (`CONTRIBUTING.md:410-418`)
by naming which readers name an unread line. It no longer cites
`skills/core/SKILL.md` for a ranking that passage does not make.
`pr.md:2` quotes the new Judgment cell word for word (read). The merge
changed none of the readers the row describes (read,
`git diff feb1a87ee 9603d3fed -- lib/routing.py`: only the `gitcmd`
import and `current_branch` changed).

```seal
confirms: round-1#3
```
What holds: `changelog.md:6` now says the four-space run hid the words
after it "up to the next line that holds nothing but a run of at least as
many backticks". That is the base's closing condition. A line matching
`FENCE`, of the opener's character, at least as long, and with nothing
else once stripped, closes the fence (read, `passages.py` at
`da7bd3968`). It also agrees with round 1's probe, where a ```` ```sh ````
line left the fence open and the bare line after it closed it. The pass
did not take round 1's own wording, and its close says why: "the next line
of backticks" would take in that `sh` line. The pass's wording is the
exact one. The S5 case's docstring carries the round's text, and its
history sentence is gone (`tests/skills/test_passages.py:140-143`, read).

```seal
confirms: round-1#4
```
What holds: `frame/plan.md:7` now says `TABLE_ROW` matches a row's start
alone and that `CELL` gains a third alternative. `frame/design.md:28` names
"`CELL`'s third alternative". Both match `lib/tables.py:63` and `:299` at
the target (read). The fix touches the work item's records alone.

What matched: the merge's one conflict is resolved for both sides
(`git show --cc 9603d3fed`, read). In
`tests/lib/test_routing.py#Test_module::test_a_reader_copied_without_the_walk_names_it`,
both parametrized rows take `gitcmd.py` beside their siblings. That
follows the target's import order in `lib/routing.py`: `gitcmd`, `optin`,
then `blocks` and `tables` each inside its own `try`. The docstring states
that order: `lib/tables.py` after all three. The narrow run below holds the
case.

What matched: the files both #1573 and this work changed are
`lib/routing.py`, `chain_check.py`, `pact_check.py` and their three test
files (executed, `comm` over the two name lists from the merge base
`da7bd3968`). Only `tests/lib/test_routing.py` conflicted. In
`lib/routing.py`, #1573's hunks touch the imports and `current_branch`,
apart from `shown` and `table_rows` (read). Round 1's *Not judged* row on
this conflict is answered by the merge.

What matched: the touched modules pass at the target. `bin/test -q` over
`tests/lib/test_routing.py`, `test_tables.py`, `test_gaps.py`,
`tests/skills/test_passages.py`, `test_pact_check.py`, `test_chain_check.py`
and `test_fold_check.py` gave 1142 passed (executed, in a clone at the
target). The suite as a whole stays `unverified`, and the orchestrator
answers it.

What matched: the fix commits add no new unit of code. Their one code-side
change is a docstring line removed from a case. So no unit is new to
review beyond the merge's resolution above.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate, the full suite, lint and format check, over the target | `seal/config.json`, `Broad gate` | the orchestrator, at the broad run now that the rounds leave nothing open |
| The Windows leg of CI over the readers' changes | `seal/threads/1795405728-lib-routing-splits-a-row-on-an-escaped-pipe/frame/plan.md:59` | CI, read by the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test -q` over the seven modules under *Confirmations*, in a clone at the target | 1142 passed |
