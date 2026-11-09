# Review round 2: 1794178393-the-batching-bars-are-met-or-removed

```seal
target: 826a2194, fixes a7260040..826a2194
```

This is the verifying round after round 1's fix pass. The code under review is the diff from `a7260040` to `826a2194`: the record commit `597e4219`, the frame fold `bf515c32`, the fix `9f2bea10` and the close commit `826a2194`. It was read in a scratch clone at `826a2194`. The work item's present-tense records (`routing.md`, the three frame files, `gaps.md`, `changelog.md` and `pr.md`) were read whole at the target. `seal/parity.md` is not declared, so no parity comparison applies.

Carried from round 1 and not searched again: where each removed unit stood in `skills/verify/scripts/session_cost.py`, the base advisory block at `:2199-2206` of `94d04d30`, the two docstring coordinates of finding 1, and the pin at `tests/text/test_the_verifying_round_is_bounded_not_cheapest.py:93-108` of `a7260040`. Every verdict below was reached again on the target.

The orchestrator's account was read as a claim. It said `826a2194` only appends the close blocks. `git show 826a2194` adds 20 lines to `trail/rounds/round-1.md`, the four close blocks, and changes nothing else (read). It said `bf515c32` folds finding 4 into the frame. That commit changes the *Removes* count line, adds the one row before the settle's row, and adds one *Judgments of the run* row (read, `git show bf515c32`).

## Findings

No finding this round.

## Confirmations

```seal
confirms: round-1#1
```
What holds: `9f2bea10` removed "under every threshold the printed advisory has" from the docstring of `test_a_cycle_is_divided_by_its_own_turns_and_not_the_runs` (`tests/skills/test_session_cost.py:2930-2932`). It removed "That is the cause #640 fixed twice for the tools-per-turn ratio, on a duration." from `test_the_delegated_note_follows_the_minute_the_column_prints`, whose paragraph now ends at the parenthetical with its mark, code point U+1F7E1 (`:3191-3193`). Neither case's assertions changed (read, `git show 9f2bea10`). The close claims a `git grep` for the class now finds nothing. Re-run as `git grep -n -i "printed advisory\|#640 fixed\|tools-per-turn ratio\|batching advisory\|one at a time"` outside `seal/` and `docs/running/`, it found five "one at a time" hits in `mutation_check.py`, `test_release_seal.py`, `test_session_cost.py:40`, `test_a_segment_feeds_the_flow_log.py` and `test_the_rules_claude_md_names_have_one_home.py`. None of them concerns tools per turn or the advisory, so the class holds no statement at the target (executed).

```seal
confirms: round-1#2
```
What holds: `changelog.md:3` now reads "Writing the instruction to batch into the framer's definition and contract rule 10 in 0.17.0 did not move the Opus readings toward a bar." The issue body places #696 in 0.17.0 and says "Neither moved the reading" (executed, `gh issue view 1440 --json body,comments`). `git tag --contains 48e08e2d`, the #696 commit, lists `v0.17.0` first (executed). The *Why* cell at `changelog.md:13` gives the Opus medians 1.31 and 1.12 against bars of 1.4 and 1.8, which are the figures at `frame/design.md:21` and the bars at `frame/design.md:10` (read). Neither sentence now contradicts the Fable framers the grounds record.

```seal
confirms: round-1#3
```
What holds: `changelog.md:4` says the line printed below 1.2 and said "independent calls were going out one at a time" only at 1.00 or under. The base block gates on `round(data["tools_per_turn"], 2) < 1.2` and chooses the one-at-a-time wording where `data["tools_per_turn"] <= 1.0`, and "most turns send a single call" otherwise (executed, `git show 94d04d30:skills/verify/scripts/session_cost.py`, lines 2199-2206).

```seal
confirms: round-1#4
```
What holds: `test_the_verifying_bar_is_grounded_on_neither_cost_nor_size` is gone from `tests/text/test_the_verifying_round_is_bounded_not_cheapest.py`, and the module keeps its three other cases, its `os` import and `ROOT` (read, the whole module at the target). `chain_check.py` run against the branch worktree no longer prints the notice round 1 quoted for that module at `frame/design.md:68` (executed). The module's own docstring speaks of the carriers and the phrase, not of the verifying row, so the deletion left no sentence there that stood on the case. Outside `seal/`, the only file that names the module is `agents/proofer.md:149`, as a `check:` target. The module still exists and holds the cases that line cites it for (executed, `git grep -n "the_verifying_round_is_bounded_not_cheapest"`). The removed case's name stands only in `.test_durations:5892` and in the work item's records, and the frame leaves `.test_durations` to its census (executed). The frame half is folded at `bf515c32`. *Removes* holds 11 rows, matching its count line at `frame/design.md:78`, and the new row stands before the settle's row at `:91` (read).

What matched: the narrow set the close names, `bin/test tests/skills/test_session_cost.py tests/text/test_the_handoff_before_round_one.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_the_verifying_round_is_bounded_not_cheapest.py -q`, passed with 495 cases and exit 0 at `826a2194`. That is the count the close of finding 4 gives (executed). `uvx ruff check` and `uvx ruff format --check` over the two changed test files exited 0 (executed).

What matched: `gaps.md:12` says `bin/test tests -q -k test_the_durations_file_prices_the_suite` passes with the removed cases' timings still in `.test_durations`. The fix pass removed one more case, and the case still passed at `826a2194`, 1 passed, exit 0 (executed). The statement holds at the target.

What matched: the chain check's one remaining notice at `frame/design.md:68` names `tests/text/test_the_chain_section_has_one_shape.py:79`. That case reads `skills/commit-pr-convention/SKILL.md` *Pull request bodies* (`:34`, `:37-48`) and not `docs/running/the-run.md`, so the settle's `remove` leaves it green. The notice is no finding, as round 1 also judged. This round re-read the case rather than carrying that verdict.

What matched: `pr.md`'s six quotes stand word for word, with runs of whitespace collapsed, at the sources their coordinates name: `changelog.md` four times, `frame/plan.md` *Judgments of the run* and `gaps.md` (executed, a comparison of each quote against its source at the target). The fix changed `changelog.md:3`, and the quote taken from that item, "Opus does batch its reads, but it chains them inside one Bash call, ...", is unchanged.

What matched: the new *Judgments of the run* row at `frame/plan.md:65` says findings 1 to 3 change no frame statement. Findings 2 and 3 change `changelog.md`. Finding 1 changes two docstrings that *Scope* item 5 (`frame/design.md:37`) already covers. The row's claim holds (read).

What matched: the *Phases* row at `frame/plan.md:42` delivers each *Removes* row the build owns, with `abc732f2` in Status. Row 10 was removed at `9f2bea10`, not at `abc732f2`. That is not a contradiction. Status records where the work item stands (`skills/implement/orchestration.md` *Where a work item stands is read from `plan.md`'s Status column*), the fold that added row 10 has its own judgment row, and round 1's close of finding 4 names `9f2bea10`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at the branch's head: the full suite, the repository-wide lint and the format check. Contract rule 2 keeps it from this round. The suite stays labelled `unverified` | `seal/threads/1794178393-the-batching-bars-are-met-or-removed/gaps.md:7` | the orchestrator, at the broad run, then the sealer's spawn |
| The transcript probe's figures and the six framers' readings of this release, carried from round 1's row as the framer's executed claims and not re-run | `seal/threads/1794178393-the-batching-bars-are-met-or-removed/frame/design.md:21-22` | the sealer, in its sample of re-run claims |
| The model the framer and the proofer run on, which the design marks `unverified` against a file | `seal/threads/1794178393-the-batching-bars-are-met-or-removed/frame/design.md:23` | the repository owner |
| How #1439 fits a `--segments` page with no grade block and rows with no `kind` or `bar` | `seal/threads/1794178393-the-batching-bars-are-met-or-removed/frame/plan.md:48` | the orchestrator, when #1439 rebases onto this branch |

This round leaves nothing open. What comes due is the orchestrator's broad run, then the sealer's spawn.

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_session_cost.py tests/text/test_the_handoff_before_round_one.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_the_verifying_round_is_bounded_not_cheapest.py -q` at `826a2194` | 495 passed, exit 0 |
| `bin/test tests -q -k test_the_durations_file_prices_the_suite` at `826a2194` | 1 passed, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over the two test files `9f2bea10` changed | exit 0 for both |
| `python3 skills/code-review/scripts/chain_check.py --baseline 94d04d30 --root <the branch worktree> --worktree`, before this record was written | exit 0. One test-pin notice at `frame/design.md:68`, naming `tests/text/test_the_chain_section_has_one_shape.py:79`, plus the four "verifying round is owed" notices and the absent gate and guarantee files |
| `git grep -n -i "printed advisory\|#640 fixed\|tools-per-turn ratio\|batching advisory\|one at a time" 826a2194 -- ':!seal/' ':!docs/running/'` | five "one at a time" hits, none about tools per turn |
