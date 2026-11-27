# Review round 2: 1795759278-the-cores-margin-depends-on-the-path

```seal
target: 5590dddf0, fixes bce10d4a1..5590dddf0
```

This is a verifying round. Its code bound is the fix range `bce10d4a1..5590dddf0`: the round-1 record (`57e97bcd6`), the framer's fold of finding 1 (`24e3b8af8`), the orchestrator's prefix row and `pr.md` quote (`28bb8d08f`), the crafter's fix pass (`20f375340`, `d72b9e4d6`, `be5df7b9a`) and the close blocks (`5590dddf0`). The round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/rounds/round-1.md` whole at `5590dddf0`. Both language keys name English, so no `pr.<lang>.md` is owed. `seal/parity.json` is not declared.

Carried from round 1 and not re-established: what `lib/core.py#rendered`, `#closing` and `#whole` do (round 1's first confirmation, `lib/core.py:136-175`, outside the fix range but for the docstring), the measurements of `changelog.md:3`, the reading of `frame/questions.md` Q1, and that the output past the cap names the plugin's root twice for the plugin's own core (round 1, finding 2's grounds, `lib/core.py:175`).

## Findings

### 1. The `named` hook row's note is not pinned whole: a note stating the opposite condition passes the module

```seal
severity: should
location: `tests/skills/test_payload_meter.py:435-440`, `skills/verify/scripts/payload_meter.py:526-532`
evidence: executed `bin/test tests/skills/test_payload_meter.py -q -p no:xdist` in a `git clone --no-local` at `5590dddf0` with "would reach `lib/core.py#CAP`" in the note at `skills/verify/scripts/payload_meter.py:529` replaced by "stays under `lib/core.py#CAP`", 46 passed; executed the paste-ready fix below in the same clone, green against the meter at `5590dddf0` and red against the same mutant; read `seal/threads/1795759278-the-cores-margin-depends-on-the-path/frame/design.md:51`
regression: round-1#1
```

Why it matters: the unit is the case `test_a_core_past_the_cap_is_a_hook_row_marked_as_naming_the_core`, added by `20f375340` and narrowed by `be5df7b9a`. *Scope* item 9 (`frame/design.md:51`) says a `named` row's note says three things: that the hook prints one line naming the core's file and the closing line where the whole output would reach `lib/core.py#CAP`, that the session opens the core itself, and that the row does not count it. The fix built the note with all three, and the case holds two: the phrase "one line naming the core's file and the closing line" and the middle sentence (`tests/skills/test_payload_meter.py:436-439`). No case holds the condition. A mutant that makes the note say the hook prints this line where the output "stays under" `CAP` passes all 46 cases of the module. That note would tell a person reading `seal payload` the reverse of when the row stops counting the core. Contract rule 14 asks the case that pins a rendered line to pin what the line says.

The commit `be5df7b9a` is titled "the named hook row's note is pinned whole". The round-1 close says more narrowly that `be5df7b9a` "pins that sentence whole", meaning the middle sentence, and that holds. The commit title's claim does not hold. The note stands as a single literal at `skills/verify/scripts/payload_meter.py:528-531`, so the case can hold it whole by its end. `rows_of` strips each cell (`tests/skills/test_payload_meter.py:168`). The fix covers both phrase assertions it replaces and leaves the absence assertion standing.

```python
        note = by_first[f"`{HOOK_ROW}`"][4]
        assert note.endswith(
            " — what the `SessionStart` hook prints where the whole output "
            "would reach `lib/core.py#CAP`: one line naming the core's file "
            "and the closing line. The session opens the core itself, and "
            "this row does not count it"
        ), note
        assert "the core below its frontmatter" not in note, note
```

No precondition at an OS boundary: the case reads the rendered table.

### 2. `frame/design.md` *Removes* still says the root the closing line's paths carried stands once, which the output past the cap contradicts

```seal
severity: should
location: `seal/threads/1795759278-the-cores-margin-depends-on-the-path/frame/design.md:93`
evidence: executed `grep -rn -i -e "root once" -e "stands once" -e "occurs once" seal/threads/1795759278-the-cores-margin-depends-on-the-path/` at `5590dddf0`; read `lib/core.py:175`, `seal/threads/1795759278-the-cores-margin-depends-on-the-path/trail/rounds/round-1.md:93`
reopens: round-1#2
```

Why it matters: the close of round 1's finding 2 does not reach every statement of the fact it repaired. The finding named the class: a sentence saying the plugin's root stands once in the output, with no limit to a printed core. `d72b9e4d6` limits `lib/core.py:14` and `changelog.md:3`, and those two now hold. The close then reports what the finding's two searches print after `be5df7b9a`, ending with "`frame/design.md:29`, `:31`, `:47` and `:67`". Run again at `5590dddf0`, the work item's search also prints `frame/design.md:93`, which the close leaves out. Its list is a sample handed back as the whole output. Round 1 missed the same row at `bce10d4a1`, where it stood at line 89.

The row's third cell reads "The relative paths of *Scope* item 1. The root they carried stands once, in the first line or in the closing line's sentence". The *Removes* table states what the work concludes, so it is read against the target. For the plugin's own core past the cap, `rendered` returns `TOO_LONG` naming `<root>/skills/core/SKILL.md` as its first line, and then `closing(plugin_root)`, whose sentence names `<root>` (`lib/core.py:175`). So the root stands in the first line and in the closing line's sentence, not once in either. The other lines the search prints hold. `frame/design.md:29` and `:31` are probes dated to `7f388fa1f`. `:47` says `closing(<root>)` holds the root once, and `:67` is S3, a whole output. `frame/plan.md:13` and `:21` and `frame/questions.md:6` each go on to what a longer root receives. `trail/phases/` and `trail/rounds/` are history. The search is a sample under contract rules 12 and 19, since a statement in other words escapes it. The row is the framer's, and its fix touches the work item's records alone.

```markdown
| The two absolute paths of the closing line, and the two joins that build them | `lib/core.py#rendered`, the `START.format(...)` call and the two `os.path.join(plugin_root, ...)` calls it holds | The relative paths of *Scope* item 1. Where the core is printed, the root they carried stands once, in the first line or in the closing line's sentence |
```

```seal
verdict: fixed 76a15fa3c
answer: The framer folded the round's text into the third cell of `## Removes`, so the root stands once where the core is printed, and limited *Scope* item 1's bold title the same way, a line the finding did not name, at `76a15fa3c`.
```

### 3. `pr.md` quotes that the title takes `fix:` and not why, nor the kind that came closest

```seal
severity: should
location: `seal/threads/1795759278-the-cores-margin-depends-on-the-path/pr.md:4`
evidence: read `skills/commit-pr-convention/SKILL.md:256-258`, `skills/code-review/orchestration.md:369-375`, `seal/threads/1795759278-the-cores-margin-depends-on-the-path/frame/plan.md:60`; executed `bin/seal pr-body --body <scratch>/pr-body-probe.md seal/threads/1795759278-the-cores-margin-depends-on-the-path` in the clone with the quote below added, exit 0
```

Why it matters: `skills/commit-pr-convention/SKILL.md:256-258` reads "Why the title takes its prefix, and the kind that came closest where one did, is one row of `frame/plan.md` *Judgments of the run*, which `pr.md` quotes." `skills/code-review/orchestration.md:369-375` names it among what the owner must see before the fold. `28bb8d08f` claims "the body quotes it", but `pr.md:4` quotes only the row's judgment cell, "The title takes `fix:`". The why, and `perf:` as the kind that came closest, stand in the row's grounds cell (`frame/plan.md:60`) and reach the body only below the fold, inside the plan. A reader of the body's first part learns the prefix, which the title already shows, and not the reason for it. Other work items' `pr.md` files quote the prefix row both ways, the judgment cell alone or the grounds as well. So this round does not read the rule from that precedent. The grounds cell's text stands word for word in the file, and `seal pr-body` accepted the quote below in this round's clone. The fix touches the work item's records alone.

```markdown
- "The title takes `fix:`" (`frame/plan.md` *Judgments of the run*, the second row of 2026-11-27)
- "The hook's output passed the harness's cap where the plugin was installed under a home directory longer than about 20 characters, so a session there received a cut core with no word of it, and the tree's case failed at a long checkout path for a reason that was not the core's size (`frame/design.md` *Grounding*); `perf:` came closest, for the shorter closing line" (`frame/plan.md` *Judgments of the run*, the second row of 2026-11-27, its grounds)
```

```seal
verdict: fixed de6976b4e
answer: The orchestrator added to `pr.md` the round's quote of the prefix row's grounds cell, which names why the title takes `fix:` and that `perf:` came closest, at `de6976b4e`; `seal pr-body` composed the body there without refusing it (executed).
```


## Confirmations

```seal
confirms: round-1#1
```
What holds: `skills/verify/scripts/payload_meter.py#session_composition` keeps the row's count as what `core.rendered` returned, and sets `named` to true where that text opens with `core.TOO_LONG` formatted for the same `path` and `core.CAP` (`:396-402`). `rendered` formats `TOO_LONG` with the `path` it was given (`lib/core.py:175`), and the meter passes it that same variable, so the comparison cannot miss on a path spelt two ways. `_core()` loads the running plugin's `lib/core.py` (`:120-123`), so `TOO_LONG` is always the constant `rendered` used. `#_session_lines` writes the new note for a `named` row (`:526-532`), and the module docstring (`:16-21`) and the docstring of `#session_composition` (`:381-390`) carry the clause *Scope* item 9 asks for (read). In this round's clone, 177 characters deep, `bin/seal payload --agent proofer` prints the hook row at 932 bytes with the new note, and `--json` carries `"named": true`. In this worktree the row reads 9,935 bytes with the whole-core note and no `named` (executed). The claim that the new case was seen red holds. With `payload_meter.py` checked out at `bce10d4a1` in the clone, `Test_measure` failed that case alone, on `KeyError: 'named'` at `tests/skills/test_payload_meter.py:427` (executed). The close's re-run of the finding's search prints the lines it lists (executed). `:504`, the session table's opening sentence, still says the table carries "the core the plugin's `SessionStart` hook prints". Round 1 left that sentence out of the fix it owed, and the row's own note now qualifies it, so this round opens nothing on it. The gap in the new case's pins is finding 1 above.

```seal
confirms: round-1#3
```
What holds: `gaps.md:13` states that `frame/design.md` *Scope* item 8 asks for no `### Process changes` table and cites the *Judgments of the run* row that opens "After phase 1 (`48f4fc57f`)" (`frame/plan.md:59`) (read). The close changed "this diff" to "this work item's diff", and that holds. `git diff --name-only origin/release/v0.39.3..HEAD` names no file of the list at `docs/layout/the-record-layout.md:52`, and `skills/verify/scripts/payload_meter.py` is not among them (executed).

What matched: the framer's fold at `24e3b8af8` against the code. *Scope* item 9, S8, the *Data & interfaces* bullet on the `named` key, the rewritten Out bullet and A12 describe what `20f375340` built (read). A12's 932 bytes in a 177-character clone is this round's figure too (executed). Item 9 says the places that read the hook row are `#session_composition`, `#_session_lines` and the JSON. A `git grep` for `["session"]` and for `payload_meter` names no other reader in shipped code: `.github/scripts/release_report.py` loads the meter for `composition`, not the session (executed, a sample).

What matched: the orchestrator's rows. The prefix row's grounds at `frame/plan.md:60` now say "a home directory longer than about 20 characters". That matches `frame/design.md:29`, "a home directory longer than 20", and `28bb8d08f` corrected "a plugin root" (read). The routing row at `frame/plan.md:61` cites `skills/implement/fix-pass.md` *A fix that needs a unit the frame does not name waits for the fold* (`:52`) and `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* (`:21`), and both headings stand (read). Its clause that `frame/design.md` *Scope* Out leaves `payload_meter.py` alone states the frame the row judged on its date. The fold rewrote that bullet afterwards, so this round opens nothing on it. `pr.md:4` quotes `frame/plan.md:60`'s first cell word for word, and `bin/seal pr-body` composes the body at `5590dddf0` (executed). What the quote leaves out is finding 3.

What matched: `changelog.md:4`'s new sentence. The meter counts the line naming the core and the closing line, marks the row `named` in its JSON, and its note says the session opens the core itself and the row does not count it (executed, the clone's run above).

What matched: the new case against its group. `bin/seal layout --pairs tests/skills/test_payload_meter.py` printed 4 pairs, all in `Test_imports_of`, and none with the new case (executed). The new case and `test_the_session_table_carries_the_hook_row_at_the_bytes_the_hook_prints` differ by the branch of `rendered` they reach. `bin/seal layout --check` on the file refused nothing (executed). `chain_check.py --worktree` printed no notice at a line of `frame/design.md` naming a test pin or a copy (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the suite is `unverified` at `5590dddf0` beyond the three modules this round ran | the `Broad gate` key of `seal/config.json` | the orchestrator's broad run, after the findings are closed |
| The `seal mutate` rows the round-1 close reports over `payload_meter.py`, other than the one this round's seen-red run repeats | `seal/threads/1795759278-the-cores-margin-depends-on-the-path/trail/rounds/round-1.md:59` | the orchestrator's broad run; no round runs them again |
| Carried from round 1: whether a fresh session takes the closing line's relative paths under the plugin's root (`frame/questions.md` Q1) | `seal/threads/1795759278-the-cores-margin-depends-on-the-path/gaps.md:7` | a measurement, run by the orchestrator or the repository owner |
| Carried from round 1: whether the closing line's paths keep `/` on Windows | `lib/core.py:85`, `seal/threads/1795759278-the-cores-margin-depends-on-the-path/gaps.md:8` | CI's Windows legs on the pull request |
| Carried from round 1: whether the harness counts the newline the hook writes after the output, at an output of 9,990 to 9,999 characters | `lib/core.py:52-56`, `hooks/core-start.py` | a measurement, run by the repository owner |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/lib/test_core.py tests/hooks/test_core_start.py tests/skills/test_payload_meter.py -q -p no:xdist`, in this worktree | 76 passed, exit 0 |
| `bin/seal payload --agent proofer`, and the same with `--json`, in a `git clone --no-local` at `5590dddf0` whose root is 177 characters long, and in this worktree | clone: hook row 932 bytes, the `named` note, `"named": true`; worktree: 9,935 bytes, the whole-core note, no `named` |
| `bin/test "tests/skills/test_payload_meter.py::Test_measure" -q -p no:xdist` in the clone with `skills/verify/scripts/payload_meter.py` checked out at `bce10d4a1`, then restored | 1 failed, `test_a_core_past_the_cap_is_a_hook_row_marked_as_naming_the_core`, `KeyError: 'named'`; 18 passed |
| `bin/test tests/skills/test_payload_meter.py -q -p no:xdist` in the clone with "would reach" in the note at `payload_meter.py:529` replaced by "stays under", then restored | 46 passed, exit 0 |
| The same new case in the clone with finding 1's fix applied, first against the meter at `5590dddf0`, then against the same mutant, then both restored | 1 passed; then 1 failed on the `endswith` assertion |
| `bin/seal pr-body --body <scratch>/pr-body.md seal/threads/1795759278-the-cores-margin-depends-on-the-path` in the clone at `5590dddf0`, then again with finding 3's added quote in `pr.md`, then restored | exit 0 both times |
| `bin/seal layout --pairs tests/skills/test_payload_meter.py` and `bin/seal layout --check tests/skills/test_payload_meter.py`, in this worktree | 4 pairs, all in `Test_imports_of`; 0 refused |
