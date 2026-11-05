# Implementation Plan: 1793853198-tests-name-the-gate-that-exists

## Technical context

The work edits text in eight files under `tests/` and removes one unit of code. The coordinates are `frame/design.md` *D1*, at `c54f0040`:

- `tests/conftest.py`: rows 1 and 2
- `tests/hooks/test_question_gate.py`: row 3
- `tests/hooks/test_routing.py`: rows 4 to 12
- `tests/behaviour/test_waiver_decided_at_start.py`: rows 13, 14 and 20
- `tests/behaviour/test_a_commit_names_its_repository.py`: row 15
- `tests/censuses.py`: rows 16 and 17
- `tests/hooks/test_launch.py`: row 18
- `tests/text/test_a_moved_rule_leaves_its_definition.py`: rows 19 and 21

The constraints:

- **No predicate changes.** Every line of D1 is a docstring, a comment, one assertion's failure message (row 7), or the dead helper (row 1). Acceptance S4 holds this by comparing the parsed modules.
- **Each present mechanism the rewrites name stands in the tree today.** That is `hooks/routing-edit-gate.py` and `routing.for_branch`, both read in *Grounding*. A rewrite does not list the readers of `hooks/lib/routing.py`, because such a list drifts with nothing to catch it.
- **Siblings share files.** #238 may edit `tests/conftest.py` on another branch. Rows 1 and 2 are lines 577-585 and 1716, and the phase leaves every other line of the file as it is. #1381 owns `tests/hooks/test_dispatch.py`, which this work does not open for edits. It also owns `hooks/dispatch.py`, whose `except` the clause at `tests/hooks/test_routing.py:533` cites, and this work does not touch that clause.
- **Edits go through the `Edit` tool** (contract rule 9). No line here is generated.

**Failure scenario of the chosen approach, six months on.** A new docstring describes a mechanism that a later release removes, and nothing refuses it. The proofer's read of the diff that removes the mechanism is the only defence, as it was for #1027. #1355's D2 accepted the same cost, for the same reason: a check of the spelling cannot tell present from past (A2).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. Per-sentence dispositions, as *D1* lists them: name the present mechanism, drop the clause, or remove the dead text | A rewrite that names the edit check can be wrong about what the edit check does for one shape. Rows 8, 10, 13 and 14 claim the edit check refuses the next edit when a declaration does not parse. `hooks/routing-edit-gate.py`'s docstring states this for every way the declaration cannot be read (read) | **Chosen.** It is the issue's own three options, applied with #1355's precedent |
| A2. Add a case or census that refuses "commit gate" under `tests/` | It would refuse the nine correct lines that say the gate is gone or tell its past, unless it grew an exemption list. A writer it refuses would move to "the gate", which it does not read. On the day it lands it has caught nothing | Rejected. `skills/core/SKILL.md` *The rule a mechanism is kept against* rules it out: a script does not re-encode a judgment of meaning as a grammar rule, and the mechanism has no catch to set against its cost. #1317's A2 and #1355's D2 rejected the same kind of check |
| A3. Replace the structure: cut `tests/hooks/test_routing.py`'s module docstring to one line and send the reader to `hooks/lib/routing.py`'s docstring | That docstring still speaks of "the gate" in the present (design *Scope*, out). The reader would be sent from one stale text to another. The test docstring's failure-direction sentences are the grounds the cases pin | Rejected. The premise that keeps the structure was checked by reading `hooks/lib/routing.py:1-25`: the module's own docstring does not yet say what the test docstring would defer to |
| A4. Widen to `hooks/` and every other shipped file that speaks of the commit gate | It edits shipped hook code docstrings under a `test:` patch whose issue and milestone name `tests/` and `.github/scripts/`. It also brushes #1381's ground in `hooks/` | Rejected for this item. Q1 asks whether `hooks/lib/routing.py` joins, and its default is no |
| A5. Also rewrite the past-tense narrations, `tests/hooks/test_optin.py:82` and `tests/hooks/test_routing.py:533` | Each is the case's grounds: the defect the case exists for, told as what happened. A rewrite that names today's hook would falsify the history, and a drop would cut the grounds. History does not drift, so the milestone's "nothing to catch its drift" does not reach it | Rejected. They do not describe the gate as present, which is the issue's class |
| A6. Leave the failure message at `tests/hooks/test_routing.py:62` with the assertions the issue puts out | A person reads the message exactly when the case fails, and today it sends that person after the commit gate | Rejected. The issue's *Out* is "the cases' assertions", that is, what is asserted. The message changes no predicate, and S4 shows it |
| A7. Keep `tests/conftest.py#fired` and correct its docstring | A helper with no caller costs its lines on every read of `conftest.py`, and nothing would catch a second drift of its docstring | Rejected. The milestone removes text that costs lines with nothing to catch its drift before correcting it. Its last caller left with #1160 (executed) |
| A8. Change `tests/censuses.py#matches`'s example and `tests/test_censuses.py:788`'s input together, so they name the same path | The case's input is a string the glob function is driven with. That is assertion data, which the issue puts out, and the case holds whether the path exists or not | Rejected. Only the docstring's example changes (row 17). The case keeps its input |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Design *Scope* items 1 and 2: the 21 rows of D1, and the phase record that lists each row with the three methods rerun at the phase's commit | acceptance S1 to S6: the three `git grep` commands at the phase's commit, the `ast` comparison probe over each file's blob at both commits, the touched modules run narrow, and the phase record read against D1 | cebd347f |

## Operational impact

None. No migration, environment variable, dependency or compatibility break. `tests/conftest.py#fired` is removed, and nothing in the tree imports it.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-05 | Round 1's finding 1 joins the frame as D1 row 20, built by round 1's fix pass rather than a new phase | The sentence is the same class as rows 13 and 14 in a file the phase already edited, found by the proofer reading the diff's files, which the frame named as its method for spellings M3 did not cover | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, a decision after the frame is folded before the next crafter spawns |
| 2026-11-05 | The docstring round 1's fix pass rewrote at `cf0d7b50` joins the frame as D1 row 21, with two `## Removes` rows for it and row 20 | The crafter found it reading finding 1's class across `tests/`; it is the same stale statement of #1027's retired waiver, in a file row 19 already edits, and it adds no mechanism | `skills/core/SKILL.md` *The rule a mechanism is kept against*, "in the same commit removes what stood on the old fact" |
