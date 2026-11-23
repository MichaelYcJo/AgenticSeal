# Review round 2: 1795401822-the-broad-gates-verdict-depends-on-the-stamps-sprite

```seal
target: f4e0fb468ef18265f0beb5193de946f98f07c445, fixes 6b6ef8ba9..f4e0fb468
```

This is a verifying round over the fix range `6b6ef8ba9..f4e0fb468`. The range holds three commits. `50bd1999f` commits round 1's record. `c0ee3fc7c` is the fix: it changes two docstrings of `skills/verify/scripts/seal_stamp.py` and one row of `gaps.md`. `f4e0fb468` appends round 1's close block. `git diff --stat 6b6ef8ba9 HEAD` names only those three files (executed). The fix changes no statement of code, only docstring text, so it adds no new unit to review as code. The round worked in the branch worktree the spawn named. No `seal/parity.json` is declared, so no parity comparison was owed. `seal/config.json` has no `Pact` key, so no pact anchor was read.

Read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md`, `trail/phases/phase-2.md` and `trail/rounds/round-1.md`. `Commit and pull request language` is English, so no `pr.<lang>.md` is owed and none stands. The frame's coordinates are dated to `ee8a72583` and round 1's to `6b6ef8ba9`. The fix added two lines to the module docstring, so the lines below it moved down by two, for example `build`'s read, which is now `seal_stamp.py:321`. Those records state their own commits, so the move is no contradiction.

Facts carried from round 1 and not established again: the behaviour its probe row records for each entry of `seal stamp` beside a cut sprite. The fix changed no code, so that behaviour at the target is what round 1 ran at `6b6ef8ba9`. Also carried: the frame's G3, G11, G12 and G19, as round 1 carried them.

## Findings

None. This round opened no finding.

## Confirmations

```seal
confirms: round-1#1
```
What holds: both docstrings round 1 named now list the malformed sprite. The fix pass claimed it applied the snippet with one change to the module docstring: the sprite's exit 2 is said "for every command but `--guarantee` and `--stop`", where the snippet said "for the sample and `--from`". That change is correct. `main` returns from `--stop` before it draws (`seal_stamp.py:1527-1534`), and `--guarantee` returns from `queue_for_written_guarantee`, which draws nothing, before the drawing branch (`:1535-1548`). The other commands are the sample, `--shape`, `--from` and `--shape --from`, because `--shape` sits outside the mutually exclusive group (`:1505-1526`). Each of them reaches `stamp`, then `compose`, then `build`, then `read_sprite`, inside the `except ValueError` that returns 2 (`:1552-1559`, `:656-661`, `:632`, `:321`). So the snippet's wording would have left out `--shape`, and the fix's wording covers every command that draws (read). "Nothing was written on 2" still holds for the sprite's refusal: `drawn_from` draws before it claims (`:1579-1582`), and the sample writes no file (read). The `Stop` hook sentence, "a load that fails there, or a malformed sprite, draws nothing", matches round 1's probe row for `--stop` (carried). `drawn_from`'s docstring (`:1565-1570`) is the snippet's text word for word (read).

The fix pass listed the class by an `ast` walk of the functions that reach `read_sprite`. Its claim that only `build`, `read_sprite` and `drawn_from` list what they raise holds. A search of the callers of `build`, `compose`, `stamp` and `read_sprite` finds no reader outside that list: `disc_cells` takes `px` and calls nothing that reads the sprite (executed: `grep -n -E 'build\(\)|disc_cells|read_sprite\(|compose\(|stamp\(' skills/verify/scripts/seal_stamp.py`). The docstrings of `stamp`, `compose`, `admitted`, `fitted`, `drawings` and `drawn_at_stop` list no raise. `drawings` says a file "whatever it fails on, is left where it is", which already covers the sprite (read: `:617-711`, `:1417-1451`). The old wording stands nowhere else in the tree (executed: `git grep -n -e 'drawn already, unreadable' -e 'or a guarantee that could not be' -- .`, which printed only round 1's record and the new docstring). No other document states `seal stamp`'s exit codes (executed: `git grep -n -i -E 'stamp.{0,60}(exit|exits) [0-9]|(exit|exits) [0-9].{0,60}stamp' -- docs skills agents lib templates hooks README.md CONTRIBUTING.md`, which printed only the `Stop` hook's `|| exit 0` in `docs/checks/the-stamp.md:87` and `hooks/hooks.json:8`). The narrow run over the stamp's module passes at the target (executed, the `## Probes` row).

What matched: the `gaps.md` row the fix closed. Its Item cell opens with `closed`, in lower case, as `skills/implement/SKILL.md` *4. The closing memo* asks. The line diff removes one row and adds the same item closed, so no row left the memo (read: the diff of `c0ee3fc7c`). The cell's account claims that with no argument `seal stamp` exits 2 with empty stdout and the `SPRITE_MALFORMED` sentence, and that `--guarantee` exits 0, prints the queued line and writes one values file. Both claims state what round 1's `## Probes` row records (read: `trail/rounds/round-1.md:90`).

What matched: the records against the target. `pr.md`'s one quote stands word for word in `frame/plan.md` *Judgments of the run* (read). Each sentence of `changelog.md` holds at the target. Its second item names `seal stamp` and `seal stamp --from`, and `--shape` is an option of `seal stamp`, so the module docstring's wider list does not contradict it (read). `gaps.md` *Not done* still holds: `skills/code-review/orchestration.md:533-534` names only a `python3` that cannot load `seal_stamp.py` and a working directory outside the clone (read). The S1 case the second memo row names stands at `tests/skills/test_broad_gate.py:2118` (executed: `git grep`). Round 1's close block names `c0ee3fc7c`, which HEAD holds (executed: `git log`).

What matched: the suite's label. `gaps.md` still names the full suite, the repository-wide lint and the format check as unverified, with the orchestrator as their answerer. This round ran only the stamp's module (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at the target | `seal/config.json` `Broad gate` | the orchestrator, at the broad gate |
| The S1 case on Windows | `tests/skills/test_broad_gate.py:2118`, the `windows-latest` legs of `.github/workflows/test.yml` | CI, on the pull request |
| `frame/plan.md` *Overlap with the release*: what #1573 and #1579 change and the merge order. The spawn forbids opening their checkouts, so this round read neither frame | `frame/plan.md` *Overlap with the release* | the orchestrator |

This round leaves nothing open. What comes due next is the orchestrator's broad run at HEAD, and the sealer's spawn after it.

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/skills/test_seal_stamp.py`, in the branch worktree at the target | exit 0: 202 passed |
