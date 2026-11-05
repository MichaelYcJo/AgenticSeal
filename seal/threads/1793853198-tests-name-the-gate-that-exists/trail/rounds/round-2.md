# Review round 2: 1793853198-tests-name-the-gate-that-exists

```seal
target: 68a1b48e, fixes 19b4cf84..68a1b48e
```

This is a verifying round. The range is `19b4cf84..68a1b48e`: round 1's record `998015ba`, the orchestrator's fold `31044e32` (D1 row 20), the fix pass's `0149c852`, `cf0d7b50` and `09212a1b`, the close blocks `45dca8be`, and the fold `68a1b48e` (D1 row 21). It touches two files under `tests/` and five of the work item's records. No `seal/parity.md` is declared, and `seal/config.md` holds no `Pact` row and no `Record language` row, so the record is in English.

Carried from round 1 as coordinates, not re-searched: the comment above `ORCH` at `tests/behaviour/test_waiver_decided_at_start.py:41-46` of the base, the case at `:749-756` of the base, and the phase record's ruff sentence. Re-established this round: each `evidence: executed` command of round 1's two findings, run again at HEAD, and every verdict below.

The implementer's account, as claims, and what this round found:

- Claimed: `tests/behaviour/test_waiver_decided_at_start.py` gives 24 passed and `tests/text/test_a_moved_rule_leaves_its_definition.py` gives 189 passed, and ruff's check and format check are clean on both. Found: `bin/test tests/behaviour/test_waiver_decided_at_start.py tests/text/test_a_moved_rule_leaves_its_definition.py -q` gives 213 passed, exit 0, and `uvx ruff check` and `uvx ruff format --check` over the two files both exit 0 (executed, at HEAD).
- Claimed: `git diff --name-only 31558c76 HEAD -- tests` lists eight paths. Found: eight paths (executed).
- Claimed: `git grep -n -i "waiv" -- tests` was read hit by hit, as a sample. Found: the command prints 31 lines at HEAD (executed). Each hit was read. None but the two lines rows 20 and 21 rewrote stated the per-command waiver as standing. `tests/hooks/test_dispatch.py:1147-1157` says the gates that carried a waiver to git stay out, `tests/hooks/test_optin.py:483` tells issue #68's cost in the past, and the other hits name the standing-waiver policy or a test's own identifier. The class is open over spellings, so this read is a sample as well.
- Claimed: the full suite is `unverified`, answered by the orchestrator's broad run (`gaps.md`). That label is honest: no party ran it.

The diff adds no test, so no new case is read against its group. The case `test_the_crafters_four_rules_stand_with_their_enforcers` and the dict `CRAFTERS_FOUR_RULES` it walks keep "four" in their names while the dict holds three rules (`tests/text/test_a_moved_rule_leaves_its_definition.py:383-400`, `:433`). D1 row 21 puts the rename outside *Scope*, and a case's name is read by its next editor and by no party at a step, so this is no finding.

## Findings

### 1. The phase record counts 20 rows of D1 and records row 21 outside D1 as a drop, where the frame at HEAD holds 21 rows and gives row 21 as N

```seal
severity: should
location: `seal/threads/1793853198-tests-name-the-gate-that-exists/trail/phases/phase-1.md:7-30`, `seal/threads/1793853198-tests-name-the-gate-that-exists/trail/phases/phase-1.md:64`, `seal/threads/1793853198-tests-name-the-gate-that-exists/trail/phases/phase-1.md:66`
evidence: read `seal/threads/1793853198-tests-name-the-gate-that-exists/trail/phases/phase-1.md:7-30`, `seal/threads/1793853198-tests-name-the-gate-that-exists/trail/phases/phase-1.md:64-66`, `seal/threads/1793853198-tests-name-the-gate-that-exists/frame/design.md:60`, `seal/threads/1793853198-tests-name-the-gate-that-exists/frame/design.md:80-81`, `seal/threads/1793853198-tests-name-the-gate-that-exists/frame/design.md:102`, `seal/threads/1793853198-tests-name-the-gate-that-exists/frame/plan.md:42`; executed `git show 68a1b48e --stat`
regression: round-1#1
```

Why it matters: the unit is the phase record's paragraph on the fix pass's second line at `trail/phases/phase-1.md:64`, with the row table's lead at `:7` and the S6 line at `:66`, which `09212a1b` wrote while answering finding 1. The frame's phase 1 row in `frame/plan.md:42` delivers "the 21 rows of D1, and the phase record that lists each row", and `frame/design.md:102` (S6) passes only when the phase record shows each of the 21 rows "with its disposition and its replacement text"; the fix pass recorded the `cf0d7b50` docstring as prose "outside D1", judged against "D1 *D, drop*", and wrote "S6 is the table above, one row for each of D1's 20 rows"; the defect came from the fold `68a1b48e`, which made that docstring D1 row 21 with disposition N after the fix pass wrote the record, and which touched only `frame/design.md` and `frame/plan.md` (executed: `git show 68a1b48e --stat`).

So at HEAD the records disagree three ways. The table at `:9-30` has 20 rows, and `:7` and `:66` say D1 has 20. The paragraph at `:64` says the line is "outside D1". It also names its disposition as *D, drop*, where `frame/design.md:60` gives row 21 as N. The sealer reads S6 against the phase record, and the pull request body copies the phase record. A sealer that follows S6 finds no row 21 in the table and two dispositions for one line, and it has to judge which one the build followed.

Either disposition describes the edit. The rewrite drops "the waiver stays one sentence" and adds a sentence on what the case holds today (`tests/text/test_a_moved_rule_leaves_its_definition.py:434-436`). The frame is the ratified record, so the phase record follows it. The fix below uses N. If the fix pass judges D the right reading, the snippet's last sentence says so as a departure, and the orchestrator brings `frame/design.md:60` along.

```markdown
**Each of D1's 21 rows, at `e1e84f0ca`** (read: each rewrite at its line after the edit). Phase 1 built rows 1 to 19. Rows 20 and 21 joined D1 after round 1 (`31044e32`, `68a1b48e`), and round 1's fix pass built them in `0149c852` and `cf0d7b50`. Q2 of `frame/questions.md` is answered by the last column.

| 21 | `tests/text/test_a_moved_rule_leaves_its_definition.py:435-436` | N | "T3 of #967: S4's rules each keep their paragraph, their clauses and a `check:` line. #1027 retired the fourth, the waiver, and the case holds that it stays gone." and "These three have no eval case" (round 1's fix pass) |

**Round 1's fix pass found one more line of finding 1's class, which the fold at `68a1b48e` made D1 row 21: `tests/text/test_a_moved_rule_leaves_its_definition.py:435-436` at the base, the docstring of `test_the_crafters_four_rules_stand_with_their_enforcers`.** (the paragraph's middle stands as written) Judged against `frame/design.md` D1 *N, present*, since the rewrite names what the case holds today, and contract rule 12, which owes the fix to every instance the cause produced. The file is one phase 1 already touched, so the count stays eight.

**S6** is the table above, one row for each of D1's 21 rows.
```

The table row goes after row 20 at `:30`. The snippet covers every statement of the row count and of row 21's disposition in the phase record. `gaps.md:8` says round 1's read found D1 row 20 and does not name the fix pass's search or row 21. That is incomplete, not false, so the fix pass may leave it.

```seal
verdict: fixed d6008c3a
answer: The finding holds: at 68a1b48e `frame/design.md:60` gives row 21 as N, and the phase record counted 20 rows and called the docstring a drop outside D1. N is the right reading, because the rewrite states what the case holds today besides dropping the clause, so no departure is recorded and `frame/design.md:60` stands. d6008c3a applies the paste-ready text, with the paragraph's middle kept as it was: the lead at `:7` counts 21 rows built in `0149c852` and `cf0d7b50`, the table gains row 21 as N, the paragraph at `:65` names the fold and judges against D1 *N, present*, and S6 counts 21 rows. `gaps.md:8` now also names the fix pass's `git grep -n -i "waiv" -- tests` and row 21. Reading the work item's records against HEAD found no other sentence the fold made stale; `:35`'s "outside D1's lines" names the `cebd347f` comment, which D1 still holds no row for.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the sentence "The per-command waiver stays in `SKILL.md`, because the implementer is who types the command." is gone, and the comment above `ORCH` ends "and no crafter spawn preloads it." (`tests/behaviour/test_waiver_decided_at_start.py:42-46`, read). Round 1's evidence was re-run at HEAD (executed). `git grep -n -i -E "no-review|no-parity|per-command|review mark|has_marker|waives? (one|a) (command|commit)" -- tests` prints four lines: `test_waiver_decided_at_start.py:749` and `:755`, and `tests/text/test_review_axes.py:143` and `:148`. Each line is a case or a comment that holds the waiver gone, and the comment at `:45` is no longer among them. `grep -n -i "waive\|no-review\|per-command"` over `skills/implement/SKILL.md` and `skills/implement/orchestration.md` still prints only `orchestration.md:410` and `:412`. D1 row 20 at `frame/design.md:59` matches the edit. Its coordinate `:44-46` at `c54f0040` covers the comment's last three lines, and the sentence stood at `:45-46` (executed: `git show c54f0040:tests/behaviour/test_waiver_decided_at_start.py`). Phase record row 20 at `trail/phases/phase-1.md:30` quotes the removed sentence and the new ending as they stand. The module passes, as the claims list above records.

```seal
confirms: round-1#2
```
What holds: `frame/plan.md:5` reads "eight files under `tests/`", and `trail/phases/phase-1.md:60` reads "over the eight touched files exit 0" (read). `git diff --name-only 31558c76 HEAD -- tests` lists eight paths (executed). The fix pass also rewrote the same paragraph's scope sentence from "the eight touched modules but `tests/conftest.py`" to "the six touched test modules". That is correct: `tests/censuses.py` defines no `test_` function (executed: `grep -n "^def test_\|^    def test_" tests/censuses.py` prints nothing). This round ran the set as `:60` now describes it, the six touched test modules with the nine modules it names, through `bin/test -q`, and it gave 763 passed, 2 skipped, exit 0 at HEAD (executed). That is the count the record claims at `cebd347f`, and the range since then changes only a comment and a docstring.

What matched: D1 row 21's text holds against the code. `tests/text/test_a_moved_rule_leaves_its_definition.py:434-440` says #1027 retired the fourth rule, the waiver, and that the case holds it gone. The case asserts `crafter_rule("The waiver is one command's.") == ""` at `:450-451`, and `CRAFTERS_FOUR_RULES` at `:383-400` holds three leads (read). The comment at `:380-382` says the same fourth rule was retired "with the gate it waived", so the docstring and the comment agree. Row 21's coordinate `:435-436` at `c54f0040` holds "and the waiver stays one sentence", and the base assertion stands at `:450-451` as the phase record says (executed: `git show c54f0040:tests/text/test_a_moved_rule_leaves_its_definition.py`).

What matched: the fold `68a1b48e` reads 21 in each count of the frame: `frame/design.md:80`, `:81` and `:102`, and `frame/plan.md:42` (read). The plan's file list at `frame/plan.md:10` and `:14` names rows 20 and 21 against their files. The two new `## Removes` rows at `frame/design.md:122-123` name the coordinate each sentence left from. The plan's two Judgments rows each name a source document (read).

What matched: `changelog.md:3` says "twenty-one places", and its new clause "said its per-command waiver stands" covers rows 20 and 21 (read). The rest of the fragment is unchanged from round 1's target.

What matched: the phase record's rewritten coordinates for row 16 and for S3 (`trail/phases/phase-1.md:5`, `:36`) now say which commit each statement was true at, and both agree with the fold `19b4cf84` (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD | `seal/config.md` `Broad gate` row | the orchestrator's broad run, then the sealer's spawn after it |
| Whether `hooks/lib/routing.py`'s module docstring, which still speaks of "the gate" in the present, joins this work item (`frame/questions.md` Q1, built on its default (b)) | `hooks/lib/routing.py:1-31` | a person, through the orchestrator's release report |
| A line under `tests/` that describes the commit gate, or its waiver, as present in words that none of M3's filter, round 1's searches or the `waiv` search holds | `tests/` | nobody's list reaches it; the class is open over spellings, as `frame/design.md` *The class* says |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_waiver_decided_at_start.py tests/text/test_a_moved_rule_leaves_its_definition.py -q` | 213 passed, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over the same two files | both exit 0 |
| `git diff --name-only 31558c76 HEAD -- tests` | 8 paths |
| `git grep -n -i "waiv" -- tests` | 31 lines, exit 0, each read; none states a standing per-command waiver |
| `git grep -n -i -E "no-review\|no-parity\|per-command\|review mark\|has_marker\|waives? (one\|a) (command\|commit)" -- tests` | 4 lines, exit 0, none a present-tense statement |
| `grep -n -i "waive\|no-review\|per-command" skills/implement/SKILL.md skills/implement/orchestration.md` | `orchestration.md:410` and `:412` only |
| `bin/test -q` over the six touched test modules, `tests/test_censuses.py`, `tests/test_conftest.py` and the seven modules `trail/phases/phase-1.md:60` names | 763 passed, 2 skipped, exit 0 |
| `git show 68a1b48e --stat` | `frame/design.md` and `frame/plan.md` only |
