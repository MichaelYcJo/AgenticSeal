# 1791384152-a-reader-declares-its-input-class — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 33d0b0ca |
| Ran by | smith on Opus, as `handoff.md`'s State row records the spawn |

## What this phase was asked

`tests/test_a_reader_declares_its_input_class.py`: the `Reads:` grammar
reader, the census reader, the contradiction check, R1–R4, R8, R9 and R10;
`tests/undeclared_readers.txt` committed from phase 1's walker at this
phase's tree; `py_spans` and `content_hash` imported from
`evidence_check.py`. No reader's body changes. R8 seen red twice, once with a
census line deleted and once with a census hash altered, and the texts of
R1–R4, R7 and R10 pinned.

## What this phase found

**The census holds 1,587 lines at 33d0b0ca**, one per population unit
undeclared at the landing. That is phase 1's count exactly: the walker's own
17 units are tracked now and every one declares, so none is on the census.

**The check refused its own author first.** Thirteen of the walker's
declarations wrapped the line or ran prose past the direction word
(`; unknown passed, because …`), and R8 named all thirteen as `direction
(none)`. The grammar reads the direction as the last word of the one line,
so a declaration is one line and its explanation is the paragraph under it.
That is what `spec.md` §*The vocabulary* says (*One line per unit*), and the
walker's docstrings were moved to it rather than the grammar widened to a
paragraph: a paragraph reader would have had to decide where a wrapped
declaration ends, which is a reader of a person's prose. `Reads: guess;
unknown passed`, with no separator, is refused for the same reason — its
class word is `guess;`.

**The two module bodies K1 selects declare in their module docstrings.**
`tests/conftest.py` had no module docstring and now has one; the pytest
recorder's gained one paragraph. Neither change moves a unit's hash, and
`bin/evidence-check --strict` stayed at exit 0 across both.

**Seen red (§15), each through `bin/mutation-check` against 33d0b0ca, every
verdict `red`:** R8 with `hooks/gate.py#lines@7b805b42` deleted from the
census, R8 with its hash altered by one digit, and R8 with
`tests/conftest.py`'s module declaration removed; and one break per new unit
of the test module — `undeclared`, `malformed_declaration`,
`declared_twice`, `census_unit_changed`, `census_line_names_nothing`,
`module_undeclared`, `judge_declaration`, `findings` (three branches: a
changed census unit, a module body's contradiction, the deleted-file
liveness half), `registry_findings`, `failure` and the `GONE` cause. The R9
pins are what each text break turned red.

## What this phase removes

| Removed item | Where it must land |
|---|---|
| none | none |
