# Review round 3: 1795339519-the-thread-layout-has-one-spelling

```seal
target: 26570fcb, fixes a66fe67f..26570fcb
```

This is a verifying round over `git diff a66fe67f..26570fcb`. The range holds round 2's record (`ed9d6e67`), the fix `7318f0d4` and the close block of `26570fcb`. The code review stays inside that diff: one comment in `skills/verify/scripts/broad_gate.py#rounds_rows` and one test docstring in `tests/skills/test_broad_gate.py`. Beside it, this round read `routing.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/rounds/round-1.md` and `trail/rounds/round-2.md` whole at `26570fcb`. The work item has no `frame/` and no `trail/phases/`. `Commit and pull request language` is English, so no `pr.<lang>.md` is owed. No `seal/parity.json` is declared.

Facts carried from rounds 1 and 2 and not established again: the issue's table and the reading of its first *Done when* item, the twelve test files behind the 1983 of `gaps.md:10`, the 2041 of the run after round 1's fix pass, the walk of 46 constants behind `gaps.md:14`, and that `seal.py:193-196` loads `lib/core.py` at import. The fix diff changes no executable line, so none of those facts can have moved. Round 1's three `## Not judged` rows stay with the orchestrator and are not written again. Round 2's note on the two glosses of SPECS in `settle.py` docstrings is not written again either.

## Findings

This round opens no finding.

## Confirmations

```seal
confirms: round-2#1
```
What holds: the claim was that the fix applied round 2's snippet at both sentences. `broad_gate.py:1773-1776` now reads the snippet word for word, and so does the docstring at `tests/skills/test_broad_gate.py:1612-1614` (read). I checked each clause of the new comment against the code beside it. "The deferred row beneath never stops a run that passed" holds. An absent `chain_check.py` is caught as `sibling.Absent` inside `going_on` and said in its own stderr line (`:1777-1785`). A load that raises or exits is caught as `Refused` or `SystemExit` (`:1786-1787`). An unreadable record is skipped (`:1795-1796`). `stamp_module()` at `:1788` cannot stop the run here, because `panel` loads it at its first line, before it calls `rounds_rows` at `:1914`, which is the one caller (read). "`lib/routing.py` ... absent, it is the loader's sentence and exit 2" holds as well. The probe points the loader at a `lib/` without `routing.py`, and `rounds_rows` ends with the loader's `cannot read .../lib/routing.py` sentence and `SystemExit 2`. With the tree's `lib/routing.py` and no `chain_check.py` under the root, it prints the "deferred findings are not counted" line and returns `[('rounds', '0')]` (executed, `## Probes`). "as every other `lib/` module does" matches the policy comment at `broad_gate.py:154-156` (read). The test docstring's "a check that raises or exits while it loads leaves the count alone beneath it" is what its two parameters, `ValueError` and `SystemExit(3)`, assert at `:1625` (read). The close's answer says a `git grep -n -i` for "label never stops" and "never stops on a label" finds the phrase only in records. At `26570fcb` that search finds it in `seal/threads/1794390764-scripts-load-a-reader-from-its-sibling/` and in this work item's round 2, and nowhere else (executed).

What matched: I ran a wider search, `git grep -n -i "never stops"` over `skills`, `lib`, `bin`, `hooks`, `docs` and `tests`. It finds four lines: the two sentences of the fix, the bounded docstring at `broad_gate.py:314`, and `lib/lines.py:485` (executed). `lib/lines.py:485` is outside the fix diff. I judged it myself rather than carry round 2's verdict. Its "`broad_gate.py`'s label, which never stops a run that passed" sits in a paragraph about a table that an unclosed fence hides, so it speaks of what a record holds, not of an absent module. An absent `seal_stamp.py` already stopped the panel at the base: `panel` called `stamp_module()` at `0eca6e77`'s `broad_gate.py:1931` (executed, `git show`). So the sentence stays as true as it was before this work item, and no finding is owed (read).

What matched: the fix diff touches no file under the work item except `trail/rounds/round-2.md`, which gains only its close block (executed, `git diff --name-only a66fe67f..26570fcb`). So `routing.md`, `gaps.md`, `changelog.md` and `pr.md` stand as round 2 read them, and the code they describe changed only in a comment. Reading each one whole at `26570fcb`, I found no sentence the target contradicts. `changelog.md:3`'s "A plugin copy without `lib/routing.py` now ends `seal gate --record` at exit 2 with `lib/sibling.py`'s sentence" is what this round's probe printed (executed). Both `pr.md` quotes stand word for word, with whitespace collapsed, at `routing.md` and `gaps.md` (executed, a whitespace-collapsed substring test). Round 2's record states its own target's coordinates, so its `broad_gate.py:1773-1774` is no contradiction of the four comment lines now at `:1773-1776`.

What matched: the handed run. I ran `bin/test -q tests/text tests/behaviour tests/skills/test_broad_gate.py` at `26570fcb`, and it exited 0 with 1351 passed and 10 skipped, the count handed over (executed). `bin/test -q tests/skills/test_broad_gate.py` exited 0 with 266 passed and 1 skipped (executed). `uvx ruff check` and `uvx ruff format --check` over the two changed files each exit 0 (executed). The fix adds no case and changes no assertion, so no new test is read against its group, and no seen-red run is owed.

This round leaves nothing open. What comes due is the orchestrator's broad run at HEAD, and the sealer's spawn after it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at 26570fcb, which no agent runs (contract rule 2) | `seal/config.json` `Broad gate` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `python3 -I test_tmp_lib_absent.py <clone> <scratch>` at 26570fcb. The probe is written again from round 2's row. It copies `lib/` without `routing.py`, points `sibling.ROOT` at the copy and calls `broad_gate.rounds_rows` on an empty directory. It then hands `rounds_rows` the tree's `lib/routing.py` with the root still moved, so only `chain_check.py` is absent | case A: the loader's `cannot read .../lib/routing.py` sentence and `SystemExit 2` (`Absent`). case B: the "deferred findings are not counted" line naming `chain_check.py`, and `[('rounds', '0')]` |
| `bin/test -q tests/text tests/behaviour tests/skills/test_broad_gate.py` at 26570fcb | exit 0, 1351 passed, 10 skipped |
| `bin/test -q tests/skills/test_broad_gate.py` at 26570fcb | exit 0, 266 passed, 1 skipped |
| `uvx ruff check` and `uvx ruff format --check` over `skills/verify/scripts/broad_gate.py` and `tests/skills/test_broad_gate.py` | exit 0 and exit 0 |
