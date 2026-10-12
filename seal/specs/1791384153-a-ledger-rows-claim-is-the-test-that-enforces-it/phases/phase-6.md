# 1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it — phase 6

| Field | Value |
|---|---|
| Phase | 6 |
| Commit | 2b501fd8 |
| Ran by | smith on Opus 5.5 |

## What this phase was asked

The reframe after round 2 (`spec.md` §*Reframed after round 2*, D2, D11):
the static reader of a test row keeps only existence. The units that read a
test file to predict pytest — collected, TEST_FILE_RE, never_fails,
unconditional, NEVER_FAILS, NEVER_RUNS — and `node_finding`'s two
calls leave `evidence_check.py`; a `def` or `class` defined once is OK, a
constant and a name defined twice are BROKEN. The three collection cases
and `NEVER` leave the new module, and S4's name-prefix cases become OK
cases. The orchestrator added that the release branch had not moved since
the merge at df42a36c, so no merge was owed before this phase.

## What this phase found

**NOT_A_TEST left too**, beside the six units `spec.md` D11 lists: once
collected was gone it had no caller, and its sentence (*pytest does not
collect by default*) is the prediction the reframe removes.

**A constant's BROKEN detail says what the name is**: *no def or class
named CONSTANT in tests/test_held.py — it is a constant*, the first half the
words the missing-unit detail already uses.

**S4 is two cases now.** `test_a_unit_that_exists_resolves_without_a_record`
holds the six shapes the old reader refused — a `def` not named `test…`, a
class not named `Test…`, a method of such a class, a function in
`tests/helpers.py`, one in `tests/conftest.py`, a method of a class with an
`__init__` — each OK with no record. The case named
test_a_unit_pytest_does_not_collect_is_no_test keeps its name for this phase and holds the constant alone, as BROKEN; its
name and the documents that cite it are phase 9's, so that the documents
change in one range, as `plan.md` §*The reframe's order* asks.

**The tree is red for existence between this phase and phase 9, and says
so itself.** `bin/evidence-check --strict .` at 2b501fd8 exits 2 with three
BROKEN findings: the fragment's T15 and `docs/the-evidence-ledger.md`
statement 1 name the three removed cases, and the test rows report them
gone — the mechanism catching its own removal. `bin/fold-check` names the
same three targets. Phase 9 rewrites both.

**Seen red (§15).** Against ec48b584's checker, a probe in the scratchpad
planted the three file shapes (a helper module, a `conftest.py`, a class
with `__init__`) and read `3 malformed`, each *pytest does not collect by
default*; the head reads `3 ok`. Through `bin/mutation-check` against
2b501fd8, with the module as its cases: the constant check removed, red (2
failed); the defined-twice check removed, red (2 failed); OK answered
MALFORMED, red (24 failed).

Executed, output read: the new module, 66 passed; `uvx ruff check` and
`uvx ruff format --check` on both files.

## What this phase removes

| Removed item | Where it must land |
|---|---|
| in `evidence_check.py`: collected, TEST_FILE_RE, never_fails, unconditional, NEVER_FAILS, NEVER_RUNS, NOT_A_TEST | the sealed run's record, read in phase 7 (`spec.md` D9) |
| three collection cases and `NEVER` in `tests/test_a_ledger_row_is_held_by_its_test.py` | phase 7's cases over a record the real recorder wrote (S15–S18) |
