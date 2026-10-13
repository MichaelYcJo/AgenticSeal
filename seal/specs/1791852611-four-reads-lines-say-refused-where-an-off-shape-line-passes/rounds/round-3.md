# 1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes — review round 3

| Field | Value |
|---|---|
| Target SHA | e6e236e4cf9391c20b02c36922238c443ffaa028 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #915 |
| Broad gate | not yet |
| Fixes checked by | no fixes to check |
| Fix range | `e6e236e4cf9391c20b02c36922238c443ffaa028..e6e236e4cf9391c20b02c36922238c443ffaa028`, 0 commits |
| Contract changes | none |
| New units | none |
| Fix of a fix | second — 🟡 1 at skills/evidence-check/scripts/evidence_check.py#removes_section, a unit round-2's fixes changed; the fix passes stop here and the work item goes back to its framer |
| Needs a fix | yes — 🟡 1 (a row followed by a rule-shaped row is read as a header, so a row naming a standing unit passes); the run is capped, so it takes the ladder in `## Deferred` |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 3 of #905, the verifying round after the run's one reopening, target e6e236e4: the diff of round 2's fixes, `683d9d55..de5adcb9`. The reviewer was asked whether round 2's 🟡 1 and 🟡 2, recorded fixed at b126895d, are closed; to check the smith's three sets against the paste-ready nested function; and to say whether the surviving `all` → `any` mutation is this run's finding or a gap that predates it. The run ends at this record.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | any row a rule-shaped row follows is read as a header, even mid-table: a body row followed by a row of dashes or a repeated rule row is skipped with it, so a row naming a standing unit passes where 683d9d55 read `STANDING` (section) or `REFUSED` (sub-heading) | `skills/evidence-check/scripts/evidence_check.py:6077` | deferred the frame | the frame — the second fix of a fix in this run; the header rule of `removes_section` is redesigned by the reframe rather than patched a third time; probe at both readers (executed); the patch below applied in the clone and dropped, its new ids red without it (executed); the run is capped, so this is a `deferred` candidate, see `## Deferred` |
| 🟢 | round 2's finding 1 is closed — a header is known by the rule row under it: a foreign table's header is not refused, and a row reading `Removes` is refused under the sub-heading and `STANDING` in the section | `skills/evidence-check/scripts/evidence_check.py:6072` | confirmed | the 3 header ids red against 683d9d55's reader, green at the head; the section's exemption narrowed to `ruled` red (executed) |
| 🟢 | round 2's finding 2 is closed — the strayed-row refusal's stop at the next level-2 heading is pinned | `skills/evidence-check/scripts/evidence_check.py:6085` | confirmed | `level > 2` to `level >= 2` red on the boundary case; the case green at 683d9d55's reader by design (executed) |
| 🟢 | the smith's three sets read every input as round 2's nested `ruled()` does | `skills/evidence-check/scripts/evidence_check.py:6073` | confirmed | read: `cells_of` holds claim lines only, so `number + 1 in ruled` is the paste-ready adjacency test; 40,000 generated sections, outputs equal (executed) |
| 🟢 | the two new cases are correct as code, and the records the range touched read clean | `tests/test_a_record_states_what_the_tree_has.py:2133` | confirmed | read; `bin/evidence-check --strict .` exit 0, `bin/fold-check --root .` exit 0 at e6e236e4 (executed) |

## Paste-ready fixes

```python
    ruled = {
        number
        for number, cells in cells_of.items()
        if cells is not None and all(RULE_CELL_RE.match(c) for c in cells)
    }
    # Only a table's FIRST row is a header, and only the rule row under it
    # is no row: a rule-shaped row anywhere else is a body row, as GFM reads
    # it, so it hides neither itself nor the row above it (round 3 of #905).
    header = {
        number
        for number, cells in cells_of.items()
        if cells is not None
        and number + 1 in ruled
        and cells_of.get(number - 1) is None
    }
    not_rows = header | {number + 1 for number in header}
```
```
    is handed back to be refused (round 1 of #905, 🟡 1). A table's header,
    its first row when a rule row directly follows it, and that rule row
    name nothing and are not, there or in the section itself; a rule-shaped
    row anywhere else is a body row (rounds 2 and 3). A
```
```python
        (
            REMOVES_TABLE.replace(
                "| x | `gone.py#x` | y |", "| x | `mod.py#old_reader` | y |"
            )
            + "| - | - | - |\n",
            [("STANDING", "spec.md:7"), ("REFUSED", "spec.md:8")],
        ),
        (
            REMOVES_TABLE
            + "\n### Phase 2\n\n| A | B | C |\n|---|---|---|\n"
            + "| x | `mod.py#old_reader` | z |\n|---|---|---|\n",
            [("REFUSED", "spec.md:13"), ("REFUSED", "spec.md:14")],
        ),
        (
            REMOVES_TABLE.replace(
                "| x | `gone.py#x` | y |", "| x | `mod.py#old_reader` | - |"
            ),
            [("STANDING", "spec.md:7")],
        ),
        (
            "| Removes | Coordinate | Why |\n| x | `mod.py#old_reader` | - |\n",
            [("REFUSED", "spec.md:5"), ("STANDING", "spec.md:6")],
        ),
```
```python
        "a rule-shaped row under a body row in the section",
        "a rule-shaped row under a strayed row",
        "a row with one dash cell",
        "a row with one dash cell under a header",
```

## Executed probes

| What was run | Result |
|---|---|
| `bin/test tests/test_a_record_states_what_the_tree_has.py -q -k "test_a_header_is_the_row_a_rule_row_follows or test_a_table_in_the_next_section_is_no_strayed_row"` with `evidence_check.py` taken from 683d9d55, restored after | exit 1; the 3 header ids failed, the boundary case passed |
| `bin/mutation-check`, `level > 2` to `level >= 2`, tests the boundary case | red; 1 failed |
| `bin/mutation-check`, the section's `if number in not_rows` narrowed to `if number in ruled`, tests the header case | red; 3 failed |
| `bin/mutation-check`, `all` to `any` in `ruled` at e6e236e4, tests the two modules | SURVIVED; 232 passed, baseline green |
| `bin/mutation-check`, `all` to `any` in #835's section predicate at 321e9de1, tests that commit's two modules | SURVIVED; 206 passed |
| a temporary probe module: the head against round 2's paste-ready transcription over 40,000 generated sections, and five shapes end to end at the head and at 683d9d55; deleted after the run | equal on every section; the rule-shaped-row shapes as tabled under 🟡 1 |
| the 🟡 1 patch and four ids applied in the clone, then dropped: the two modules; the ids without the patch; first-row conjunct dropped and `all` to `any` on the patch; `all` to `any` at the head with the two dash-cell ids | 236 passed; 2 failed, 4 passed; red and red; red |
| `bin/evidence-check --strict .` and `bin/fold-check --root .` at e6e236e4 | exit 0 and exit 0 |
| the broad gate (full suite, repository-wide lint, typecheck) | not yet; not run by this round, it is the sealer's after the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `skills/evidence-check/scripts/evidence_check.py:6053` | round 1's 🟡 1 — fixed |
| round-1 | `skills/evidence-check/scripts/evidence_check.py:6051` | round 1's 🟡 2 — fixed |
| round-1 | `skills/evidence-check/scripts/evidence_check.py:6127` | round 1's ⬜ 3 — answered |
| round-1 | `tests/test_a_record_states_what_the_tree_has.py` | round 1's 🟢 — confirmed |
| round-1 | `docs/the-reader-registry.md:154` | round 1's 🟢 — confirmed |
| round-1 | `seal/ledger/1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes.md` | round 1's 🟢 — confirmed |
| round-1 | `agents/warden.md:111` | round 1's 🟢 — confirmed |
| round-1 | PR #915 body | round 1's ❓ — out of verified scope |
| round-2 | `skills/evidence-check/scripts/evidence_check.py:6076` | round 2's 🟡 1 — fixed |
| round-2 | `skills/evidence-check/scripts/evidence_check.py:6069` | round 2's 🟡 2 — fixed |
| round-2 | `skills/evidence-check/scripts/evidence_check.py:6073` | round 2's 🟢 — confirmed |
| round-2 | `skills/evidence-check/scripts/evidence_check.py:6065` | round 2's 🟢 — confirmed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| 🟡 1 — a row followed by a rule-shaped row is read as a header, and a standing unit on it passes | candidate: a new issue labelled `from-review` in milestone 0.21.1 (rung 3), carrying the paste-ready fix above; rung 1 also fits, because the branch wrote the unit, but the reopening bound lets this record commission no fix pass | the repository owner, who decides whether 0.21.1 ships the header rule with this hole or takes the fix before the release |
| the rule-row predicate's `all` is pinned by nothing: `any` survives the two modules at e6e236e4 and at 321e9de1 | the same issue as 🟡 1; the gap has existed since #835, and the cases in 🟡 1's fix pin it | the repository owner, with 🟡 1 |
