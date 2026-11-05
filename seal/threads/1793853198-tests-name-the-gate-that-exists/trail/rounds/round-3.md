# Review round 3: 1793853198-tests-name-the-gate-that-exists

```seal
target: 85268bdb, fixes 68a1b48e..85268bdb
```

This is a verifying round. The range is `68a1b48e..85268bdb`: round 2's record `2224ed7a`, the fix pass's `d6008c3a`, and the close block `85268bdb`. It touches three of the work item's records, `gaps.md`, `trail/phases/phase-1.md` and `trail/rounds/round-2.md`, and no file under `tests/` (executed: `git diff --name-only 68a1b48e 85268bdb -- tests` prints nothing). No `seal/parity.md` is declared, and `seal/config.md` holds no `Pact` row and no `Record language` row, so the record is in English.

Carried from round 2 as coordinates, not re-searched: `frame/design.md:60` (D1 row 21, disposition N), `:80-81` and `:102` (the counts of 21), and `frame/plan.md:42`. Carried as a result, because the range changes no file under `tests/`: round 2's narrow runs at `68a1b48e`, 213 passed over the two modules rounds 1 and 2 touched and 763 passed, 2 skipped over the set `trail/phases/phase-1.md:61` names. Re-established this round: the text the fix wrote, against the frame and the test file it describes, and every verdict below.

The implementer's account, as claims, and what this round found:

- Claimed: the work item's records were read whole against HEAD, and a search for count and location phrases (`outside D1`, `20 rows`, `twenty`, `D1's 19|20` and others) found nothing else the fold made false (executed). Found: this round read `routing.md`, `changelog.md`, `gaps.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md` and `trail/phases/phase-1.md` whole at HEAD (read). Its own search over those files, `git grep -n -i -E "outside D1|[0-9]+ rows|twenty|D1's [0-9]+|rows? (1|19|20|21)\b|rows 1 to|nineteen|D, drop|cf0d7b50|435-436"`, prints 15 lines (executed), and each was read. None states a count of D1 other than 21 or a disposition for row 21 other than N, except `trail/phases/phase-1.md:5`, weighed in the next item. The hit at `:35`, "outside D1's lines", names the `cebd347f` comment, for which D1 holds no row. The search is a sample over spellings, and the whole read is what covers the closed set.
- Claimed: `trail/phases/phase-1.md:5`'s "Each of D1's 19 coordinates holds the text its row names" stays as a statement of the phase's time (read). Found: that holds. D1 held 19 rows at `e1e84f0c`, the commit the sentence names as the phase's base (executed: `git show e1e84f0c:seal/threads/1793853198-tests-name-the-gate-that-exists/frame/design.md`, 19 numbered rows). The sentence's subject is the check made before the build, and `:7` says next that rows 20 and 21 joined D1 after round 1. HEAD does not contradict it.
- Claimed: the full suite is `unverified`, answered by the orchestrator's broad run (`gaps.md:7`). That label is honest: no party ran it, and this round did not.

The diff adds no test, so no new case is read against its group.

One sentence outside the fix diff was weighed and opens no finding. `frame/questions.md:16` answers Q2, the wording of each replacement, "by the work (phase 1, b965a9a8 and cebd347f; each sentence stands beside its row in `trail/phases/phase-1.md`)". Rows 20 and 21 were worded later, in `0149c852` and `cf0d7b50`. The status was true when written, and the file it points to holds all 21 sentences beside their rows (`trail/phases/phase-1.md:11-31`, read), so it is incomplete, not false.

## Findings

This round opens no finding.

## Confirmations

```seal
confirms: round-2#1
```
What holds: the phase record now agrees with the frame on D1's count and on row 21's disposition (read). `trail/phases/phase-1.md:7` reads "Each of D1's 21 rows" and names the two folds and the two fix commits. `:31` is row 21, with disposition N, as `frame/design.md:60` gives it. `:65` says the fold at `68a1b48e` made the docstring D1 row 21 and judges it against D1 *N, present*. `:67` counts 21 rows. The text matches round 2's paste-ready snippet line for line, and the paragraph's middle stands as it was (executed: `git diff 68a1b48e d6008c3a`). Each coordinate the new text names holds. `31044e32` and `68a1b48e` are the two folds, and each touches only `frame/design.md` and `frame/plan.md`. `0149c852` touches only `tests/behaviour/test_waiver_decided_at_start.py`, and `cf0d7b50` only `tests/text/test_a_moved_rule_leaves_its_definition.py` (executed: `git show --stat` on each). Row 21's quoted replacement is the docstring at `tests/text/test_a_moved_rule_leaves_its_definition.py:434-439` at HEAD, word for word (read). Its coordinate `:435-436` holds "and the waiver stays one sentence" at `e1e84f0c` (executed: `git show e1e84f0c:tests/text/test_a_moved_rule_leaves_its_definition.py`). The new sentence at `gaps.md:8` says the fix pass's `git grep -n -i "waiv"` found row 21: that search over the file at `c54f0040` prints `:436` among its hits (executed). The close block in `85268bdb` adds five lines to `trail/rounds/round-2.md` and changes nothing else in it (executed: `git diff 2224ed7a 85268bdb`). Its line references `:7`, `:65` and `:35` name the paragraphs they describe at HEAD (read). The fix pass judged N right and recorded no departure. That agrees with the frame, so `frame/design.md:60` needed no change.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD | `seal/config.md` `Broad gate` row | the orchestrator's broad run, then the sealer's spawn after it |
| Whether `hooks/lib/routing.py`'s module docstring, which still speaks of "the gate" in the present, joins this work item (`frame/questions.md` Q1, built on its default (b)) | `hooks/lib/routing.py:1-31` | a person, through the orchestrator's release report |
| A line under `tests/` that describes the commit gate, or its waiver, as present in words that none of M3's filter, round 1's searches or the `waiv` search holds | `tests/` | nobody's list reaches it; the class is open over spellings, as `frame/design.md` *The class* says |

This round leaves nothing open. What comes due is the orchestrator's broad run, and the sealer's spawn after it.

## Probes

| Command | Result |
|---|---|
| `git diff --name-only 68a1b48e 85268bdb -- tests` | nothing, exit 0 |
| `git diff 68a1b48e d6008c3a` | `gaps.md:8` and `trail/phases/phase-1.md:7`, `:31`, `:65`, `:67` only |
| `git diff 2224ed7a 85268bdb -- seal/threads/1793853198-tests-name-the-gate-that-exists/trail/rounds/round-2.md` | the five lines of the close block only |
| `git show --stat 31044e32 68a1b48e cf0d7b50 0149c852` | the folds touch `frame/design.md` and `frame/plan.md`; the fixes touch one test file each |
| `git show e1e84f0c:seal/threads/1793853198-tests-name-the-gate-that-exists/frame/design.md`, numbered rows counted | 19 |
| `git grep -n -i "waiv" c54f0040 -- tests/text/test_a_moved_rule_leaves_its_definition.py` | 12 lines, `:436` among them |
| `git grep -n -i -E` with the count and location pattern above, over the work item's records outside `trail/rounds/` at HEAD | 15 lines, exit 0, each read |
