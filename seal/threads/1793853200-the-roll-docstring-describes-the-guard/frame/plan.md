# Implementation Plan: the roll docstring describes the guard

## Technical context

`.github/scripts/roll_flow_measurement_issue.py` (574 lines at `c9f08a03`) holds a 146-line module docstring that a person reads before changing the release roll. Two functions read `gh issue list` and retry an empty reading once after `RETRY_DELAY_SECONDS` (`:159`): `open_flow_measurement_issues` (`:315-327`), for `main`'s lookup, and `landed_create` (`:447-463`), the ladder's guard, which also excludes the issue `main` just closed. Both docstrings already point at the module docstring for the lag (`:318`, `:451`). So the module docstring is the one home both cite, and D1 keeps it as that home. The module docstring's lag paragraph (`:68-80`) states as an absolute that a lag never gives a reading with an extra issue in it. `landed_create` (`:450-453`, `:460`) exists because a lag behind a close does exactly that.

`tests/github/test_roll_flow_measurement_issue.py` holds the function cases. Its docstring at `:256-257` repeats the absolute. No case reads the script's docstring text (`frame/design.md` *Grounding*).

The work changes docstring text only, so it has one failure scenario worth naming. In six months somebody changes the retry in `open_flow_measurement_issues` or the guard in `landed_create` and leaves the module docstring as it is. Then the same drift recurs. Stating the rule once and having the function docstrings cite it rather than restate it shrinks that surface to one paragraph. Nothing catches a drift of prose against code. The milestone accepts that and adds no pin (A4).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. Correct only the two passages #146 names, `:68-80` and `:111-117` | `open_flow_measurement_issues`'s docstring keeps "a lag can only ever undercount", and the transaction paragraph keeps "never a lag artifact". The contradiction #146 is about moves to another docstring in the same file, and the next reader meets it there. Contract rule 12 owes the fix to every instance | rejected |
| A2. State the lag rule once in the module docstring, by kind of write; the function docstrings cite it and state their own decision; the guard paragraph names `landed_create` instead of restating its condition; the history clause is cut to its grounds (#109); the test docstring's absolute goes (`frame/design.md` D1) | A later edit to the retry or the guard leaves the one paragraph stale, and nothing catches it. The surface is one paragraph instead of four sentences in three places | **chosen** |
| A3. Replace the structure: take the lag rule and the guard rationale out of the module docstring and give them to the two function docstrings, with the module docstring pointing at them | The rule governs two functions and the transaction paragraph, so it would sit in one function and be cited from the other and from the module, or be stated twice. The retry-zero-not-two decision is the roll's design, read before a change to the roll (`routing.md` *Why this way*), and a function docstring is read only when that function is opened. The premise that keeps the structure: both functions already cite the module docstring for the lag (`:318`, `:451`, read) | rejected; the module docstring stays the home |
| A4. Add a case that pins the corrected sentences, or forbids the absolute's spelling | It refuses a spelling while the class is a kind of claim, and on the day it lands it has caught nothing, since this work removes the instances by hand. `skills/core/SKILL.md` *The rule a mechanism is kept against*, and the milestone's purpose, which removes text that costs lines with nothing to catch its drift | rejected |
| A5. Carry #146's two mutation cases, `RETRY_DELAY_SECONDS` at zero and the note dropped from the last rung | The milestone states the pins are not carried. Carrying them overrules an owner decision made in the milestone description | rejected, by the milestone |
| A6. Delete the lag and guard paragraphs outright, with no correction | The decision to retry zero but not two, and why the ladder re-reads before a retry, then stand nowhere a person reads before changing the roll. The transaction paragraph's reasoning leans on that decision | rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1, 2, 3 and 4, as `frame/design.md` D1 items 1 to 6 state them | S1, S2, S3 and S4 of `frame/design.md`; the phase record holds S1's and S3's output | |

## Operational impact

None. No behaviour, dependency, environment variable or workflow step changes.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
