# Review round 1: 1794178393-the-batching-bars-are-met-or-removed

```seal
target: a7260040 against release/v0.36.0
```

The branch was read against `94d04d30` in a scratch clone at `a7260040`. This is the first round, so no fact is carried from an earlier record. Every verdict below was reached on the code and the records at the target. `seal/parity.md` is not declared, so no parity comparison applies.

## Findings

### 1. Two kept docstrings in the script's test module still cite the advisory and #640's two fixes, which this branch removed

```seal
severity: should
location: `tests/skills/test_session_cost.py:2931-2932`, `tests/skills/test_session_cost.py:3194-3195`
evidence: executed `git grep -n -i -E "threshold|one at a time|tools.per.turn|per turn" -- tests skills/verify agents` and `grep -n "#640" tests/skills/test_session_cost.py`; read `tests/skills/test_session_cost.py:2925-2933`, `tests/skills/test_session_cost.py:3188-3196`, `seal/threads/1794178393-the-batching-bars-are-met-or-removed/frame/design.md:37`, `seal/threads/1794178393-the-batching-bars-are-met-or-removed/trail/phases/phase-1.md:11`
```

Why it matters: `frame/design.md:37` (*Scope* item 5) says kept cases whose docstrings cite the bars, the grade or the advisory are rewritten in place. Two kept cases still cite them. `test_a_cycle_is_divided_by_its_own_turns_and_not_the_runs` says the misdivided ratio reads 0.43, "under every threshold the printed advisory has" (`tests/skills/test_session_cost.py:2931-2932`). No printed advisory exists after `abc732f2`. `test_the_delegated_note_follows_the_minute_the_column_prints` ends a paragraph with "That is the cause #640 fixed twice for the tools-per-turn ratio, on a duration" (`tests/skills/test_session_cost.py:3194-3195`). The phase record claims that class was enumerated: it removed this same clause from the `report_spawns` comment, because "both fixes were in the code this phase removes" (`trail/phases/phase-1.md:11`). The test module's copy of the clause stayed. The test file is in the branch's own diff, so it lies inside the closed set of contract rule 12. A statement the closed set held that the account missed is a finding on the method. A reader who looks for the advisory, or for #640's two fixes, in `session_cost.py` finds neither.

The search above listed every statement of the class in `tests/`, `skills/verify/` and `agents/`. These two are the only ones left. The `#640` mentions at `tests/text/test_the_handoff_before_round_one.py:102` and `:109` concern the framer's opening, which stays (`frame/design.md:42`), so they are outside the class.

For `tests/skills/test_session_cost.py:2930-2933`:

```python
        Cycle 2 sent three calls over three turns, so its ratio is 1.00. Divided
        by the run's seven turns it reads 0.43, and every other number in the
        row stays right, which is what would make it survive a reading."""
```

For `tests/skills/test_session_cost.py:3194-3195`, delete the sentence "That is the cause #640 fixed twice for the tools-per-turn ratio, on a duration." The paragraph then ends at the parenthetical before it, "(#701; #640's round 3, ... 10).", and that parenthetical stays as it is, including its mark (code point U+1F7E1). Neither case's assertions change.

### 2. The changelog says no segment kind met its bar since 0.17.0, and the work item's own grounds record framers that did

```seal
severity: should
location: `seal/threads/1794178393-the-batching-bars-are-met-or-removed/changelog.md:13`, `seal/threads/1794178393-the-batching-bars-are-met-or-removed/changelog.md:3`
evidence: read `seal/threads/1794178393-the-batching-bars-are-met-or-removed/changelog.md:3`, `seal/threads/1794178393-the-batching-bars-are-met-or-removed/changelog.md:13`, `seal/threads/1794178393-the-batching-bars-are-met-or-removed/frame/design.md:19`, `seal/threads/1794178393-the-batching-bars-are-met-or-removed/frame/design.md:21`, `seal/threads/1794178393-the-batching-bars-are-met-or-removed/frame/design.md:27`; executed `gh issue view 1440 --json body,comments`
```

Why it matters: the *Process changes* row gives as its reason "No segment kind met its bar since 0.17.0" (`changelog.md:13`). The design's *Grounding* records the 0.22.0 framers at 2.7 to 3.7 against the framing bar of 1.4 (`frame/design.md:19`, #935). It also records 49 of 50 Fable framers and 23 of 65 Opus framers at or above 1.4 (`frame/design.md:21`). The corrected issue body states the same: "Two readings met the bar." The release note would tell a reader something the work item's own records contradict. The design's conclusion is narrower: "Opus has not met the bars since #696 wrote the instruction" (`frame/design.md:27`). `changelog.md:3` says "No release since 0.17.0 moved a reading toward a bar". It has two readings, a release whose readings rose and a release whose change raised them, and only the second holds. The fix scopes both sentences to what the grounds support. `pr.md` quotes neither sentence, so it needs no change.

For `changelog.md:3`, replace the sentence "No release since 0.17.0 moved a reading toward a bar, although 0.17.0 wrote the instruction to batch into the framer's definition and contract rule 10." with:

```markdown
Writing the instruction to batch into the framer's definition and contract rule 10 in 0.17.0 did not move the Opus readings toward a bar.
```

For `changelog.md:13`, the *Why* cell:

```markdown
| 2026-11-09 | Contract rule 10 asks every agent to batch independent reads and no longer names a bar its segment is judged by | Opus framers read a median of 1.31 and Opus proofers 1.12 against bars of 1.4 and 1.8, and Opus chains its reads inside one Bash call, which the ratio cannot see | https://github.com/MichaelYcJo/AgenticSeal/issues/1440 |
```

### 3. The changelog says the advisory claimed one-at-a-time calls everywhere below 1.2, and the base code said so only at 1.00 and under

```seal
severity: should
location: `seal/threads/1794178393-the-batching-bars-are-met-or-removed/changelog.md:4`
evidence: executed `git show 94d04d30:skills/verify/scripts/session_cost.py | grep -n "one at a time\|most turns send\|< 1.2:"`; read `seal/threads/1794178393-the-batching-bars-are-met-or-removed/changelog.md:4`
```

Why it matters: `changelog.md:4` says the plain reading "printed one below 1.2 tools per turn, saying that independent calls were going out one at a time". At the base, the block at `skills/verify/scripts/session_cost.py:2199` printed "independent calls are going out one at a time" only when the ratio was 1.00 or less (`:2204`). Between 1.00 and 1.2 it printed "most turns send a single call" (`:2206`). The release note misstates what the removed line said for that range. The falsity it names, which is a segment that chains its reads in one call, applies to the claim at 1.00 and under.

```markdown
- **The plain reading, `seal cost <transcript>`, no longer prints a `batching` line.** It printed one below 1.2 tools per turn, and at 1.00 or under it said that independent calls were going out one at a time, which is false for a segment that chains its reads inside one call. The `nothing obvious` line now prints wherever no check was re-run. The ratio and its denominator stay in `--json` as `tools_per_turn` and `call_turns`.
```

### 4. A pin of the bars table's verifying row is left standing, and the settle's `remove` turns it red

```seal
severity: should
location: `tests/text/test_the_verifying_round_is_bounded_not_cheapest.py:93-108`, `seal/threads/1794178393-the-batching-bars-are-met-or-removed/frame/design.md:78`
evidence: executed `python3 skills/code-review/scripts/chain_check.py --baseline 94d04d30 --root <the branch worktree> --worktree` and `git grep -n -E "refusal threshold|repeats = 0|a lens|run-level table|\| verifying \||\| reviewing \||\| framing \||\| implementing \||batching advisory" -- tests`; read `tests/text/test_the_verifying_round_is_bounded_not_cheapest.py:93-108`, `docs/running/the-run.md:85-105`, `seal/threads/1794178393-the-batching-bars-are-met-or-removed/frame/design.md:78-91`
```

Why it matters: the check's notice at the `remove` reads: "seal/threads/1794178393-the-batching-bars-are-met-or-removed/frame/design.md:68  a test pins text this operation takes out of `docs/running/the-run.md`: `tests/text/test_the_verifying_round_is_bounded_not_cheapest.py:97` holds "| verifying | exempt |", and the `to` does not". `test_the_verifying_bar_is_grounded_on_neither_cost_nor_size` opens `docs/running/the-run.md` and asserts that exactly one line starts with `| verifying | exempt |`. That line is the verifying row of the table under *The per-segment bars* (`docs/running/the-run.md:95`), which `## Rule changes` removes whole. After the settle the case finds 0 rows and fails. Nothing remains to repoint it to, because the bars leave and no other document states a verifying bar. The case also pins wording, namely that the row's *Grounds* cell holds no cost or size word, and `docs/running/what-a-script-gates.md` *The checks* says a case that pins wording goes. *Removes* (`frame/design.md:78-91`) names the pins of the bars in two modules and misses this one. The plan's census grep cannot list it either, because its pattern holds no word of the verifying row. The build removed the other pins of the same section before the settle (`#test_the_protocol_names_a_bar_per_segment_kind` among them), so this one goes with them.

The `git grep` above, over the section's distinctive phrases in `tests/`, finds no other pin of the section. The check's other notice at `frame/design.md:68` names `tests/text/test_the_chain_section_has_one_shape.py:79`. That case reads `skills/commit-pr-convention/SKILL.md` *Pull request bodies* and not `docs/running/the-run.md` (`tests/text/test_the_chain_section_has_one_shape.py:34`, `:37-48`). It shares the phrase "Measure the segment, and feed the flow log" with the section, so the settle leaves it green and the notice is no finding.

Delete `tests/text/test_the_verifying_round_is_bounded_not_cheapest.py:93-110`, the case and the two blank lines after it. The module's other three cases and its imports stay, because `flat` and `CARRIERS` still read `os` and `ROOT`. In `frame/design.md`, change line 78 and add a row to *Removes* before the settle's row:

```markdown
The table holds 11 rows. The build removes what the first 10 name, and the settle removes what the last names.
```

```markdown
| the pin of the bars table's verifying row | `tests/text/test_the_verifying_round_is_bounded_not_cheapest.py#test_the_verifying_bar_is_grounded_on_neither_cost_nor_size` | nothing. The row it pins leaves with *The per-segment bars* at the settle, and no other document states a verifying bar. The module's three other cases hold #639's wording in the carriers that stay. |
```

## Confirmations

What matched: *Scope* item 1 (`frame/design.md:33`). `SEGMENT_BARS`, `segment_kind`, `report_grades`, the `report_grades(rows)` call in `report_segments` and the `row.update(segment_kind(...))` loop in `measure_segments` are gone at `a7260040` (read, the diff of `skills/verify/scripts/session_cost.py`). The `token_totals` docstring no longer cites the bars (`skills/verify/scripts/session_cost.py:1883-1887`, read). A search of the script for `grade`, `bar`, `advisory`, `batching`, `#640` and `1.2` finds no leftover statement of the mechanism (executed).

What matched: *Scope* item 2 (`frame/design.md:34`). The `< 1.2` block and its comment are removed, and the `nothing obvious` gate is `if same <= 0:` (`skills/verify/scripts/session_cost.py:2202`, read). `tools_per_turn` stays in `analyse`'s return (`:1189`) and in both `t/turn` columns (`:2333`, `:2692`), read.

What matched: *Scope* items 3 and 4. Rule 10 ends at "which is where batching pays most." and keeps its `check:` line (`skills/agent-contract/SKILL.md:116-117`). Step 1 of `skills/verify/orchestration.md:243-244` lists the row's columns with no grade clause (read). The design claims rule 10 is still pinned through `test_no_definition_carries_a_sections_own_sentences`, which is parametrized over `sorted(SECTIONS)`. That is true at `tests/text/test_a_moved_rule_leaves_its_definition.py:159-161` (read).

What matched: *Scope* item 5 and *Removes* rows 7 to 9. Every case and helper the rows name is gone. `batched` stays, `graded_run` is renamed `spawned_run`, and `PROTOCOL` stays and is read by three kept cases (`tests/text/test_the_handoff_before_round_one.py:23`, `:30`, `:62`, `:84`), read. No file outside this work item names a removed case, apart from `.test_durations` (executed, `git grep` over the 24 removed names and `graded_run` and `TOOLS_PER_TURN`). Under `seal layout --pairs`, none of the three new cases is paired with another case (executed). Each new case pins a behaviour the diff changed, so none duplicates its group.

What matched: the phase record's claim that the three rewritten cases were seen red at the base. In a scratch clone at `94d04d30` with only the target's test module checked out, the three cases failed on the lines the record names: `assert "batching" not in out`, `assert "Tools per turn against each kind's bar" not in flat_out` and `assert "kind" not in row` (executed). The mutation runs at `trail/phases/phase-1.md:23-29` were not re-run. They are carried as the record's claim.

What matched: the plan's narrow set, `bin/test tests/skills/test_session_cost.py tests/text/test_the_handoff_before_round_one.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/behaviour/test_a_cited_section_stands_in_its_file.py -q`, passed with 492 cases and exit 0 at `a7260040`. That is the count `trail/phases/phase-1.md:47` gives (executed). `uvx ruff check` over the four changed Python files exited 0 (executed). The census `git grep` of `frame/plan.md:42` returns only `.test_durations:5811`, as the folded Verified-by cell and `trail/phases/phase-1.md:43` say (executed).

What matched: *Rule changes* (`frame/design.md:66-74`). The `from:` text equals the sentence at `docs/running/measuring-a-run.md:7-9` with whitespace collapsed (read). No other file outside this work item cites *The per-segment bars* (executed, `git grep -n -i "per-segment bars"`). The rest of the bars' wording in `docs/` stands inside the section the `remove` takes out, `docs/running/the-run.md:85-105` (executed, `git grep -n -w -i -E "bars?|graded|ungraded"` over `docs`, `agents`, `skills`, `templates`, `README.md` and `CONTRIBUTING.md`). *Data & interfaces*' claim that no reader in the tree reads a segment row's `kind` or `bar` holds: the remaining `row["kind"]` reads in `session_cost.py` (`:2225`, `:2409`) are spawn-cycle rows (read).

What matched: the orchestrator's claim in `frame/plan.md:63` that the two *Grounding* rows on the ticket were true of the ticket the framer read. The issue's one comment was created at 2026-11-08T23:07:18Z, which is 08:07:18 +09:00. That is five seconds before the framing commit `03cbad55` (08:07:23 +09:00), and the comment says it follows the framer's read of #935 (executed, `gh issue view 1440 --json body,comments`; `git log --format='%h %cI'`). *Grounding* is dated to `9c1cde63` at `frame/design.md:5`, and the plan row records the decision with its grounds. The four folds of `3a9337fd` each agree with the target (read, `git show 3a9337fd`).

What matched: `pr.md`'s six quotes stand word for word at the sources their coordinates name: `changelog.md:3` twice, `changelog.md:4`, `changelog.md:7`, `frame/plan.md:64` and `gaps.md:8` (read).

What matched: `gaps.md` is new on this branch, so the diff removes no `## Not verified` row. Its broad-gate row names the orchestrator, which keeps the suite labelled `unverified` (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The transcript probe's figures (1046 metas, the per-model medians, the 72% of Bash calls that chain reads) and the six framers' readings of this release were not re-run. They ground the decision and are carried as the framer's executed claims | `seal/threads/1794178393-the-batching-bars-are-met-or-removed/frame/design.md:21-22` | the sealer, in its sample of re-run claims |
| The model the framer and the proofer run on, which the design marks `unverified` against a file | `seal/threads/1794178393-the-batching-bars-are-met-or-removed/frame/design.md:23` | the repository owner |
| The broad gate at the branch's head: the full suite, the repository-wide lint and the format check. Contract rule 2 keeps it from this round | `seal/threads/1794178393-the-batching-bars-are-met-or-removed/gaps.md:7` | the orchestrator, at the broad run after the rounds settle |
| How #1439, built side by side and merged after this branch, fits a `--segments` page with no grade block and rows with no `kind` or `bar`. This round read #1439 only as the spawn prompt's context | `seal/threads/1794178393-the-batching-bars-are-met-or-removed/frame/plan.md:48` | the orchestrator, when #1439 rebases onto this branch |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_session_cost.py tests/text/test_the_handoff_before_round_one.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/behaviour/test_a_cited_section_stands_in_its_file.py -q` at `a7260040` | 492 passed, exit 0 |
| `bin/test tests/skills/test_session_cost.py -q -p no:xdist -k "grades_none or carries_the_ratio_and_no_grade or names_no_batching"` in a scratch clone at `94d04d30` with `tests/skills/test_session_cost.py` checked out from `a7260040` | 3 failed, exit 1, each on the assertion the phase record names. The scratch clone was removed afterwards |
| `uvx ruff check` over the four changed Python files | exit 0 |
| `bin/seal layout --pairs` | exit 0. No pair names any of the three new cases |
| `git grep -n -E 'SEGMENT_BARS\|report_grades\|segment_kind\|per-segment bar\|framing bar\|reviewing bar' -- ':!seal/' ':!docs/running/'` | one hit, `.test_durations:5811` |
