# 1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes — review round 3 report

Target SHA: e6e236e4 · base: `origin/release/v0.21.1` (321e9de1) · scope: the fix range `683d9d55..de5adcb9`, 3 commits, the verifying round after the run's one reopening. This record ends the run whatever it finds.
Reviewed in a `git clone --no-local` at the target, in the session scratchpad, with a second clone at 321e9de1 for one mutation; the worktree was only read. Every suite run below set `SPECSEAL_CASE_CEILING_S=600`.

## Summary

Both findings round 2 recorded as fixed at b126895d are closed. The three header ids go red against the reader at 683d9d55 and green at the head, and the level bound's mutation is red on the new boundary case.

The smith's three sets (`cells_of`, `ruled`, `not_rows`) read every input the way round 2's nested `ruled()` reads it. That rests on reading and on 40,000 generated sections whose outputs were equal.

The header rule itself, which round 2 wrote and the smith built as given, opens one finding:

1. **🟡 1 — any row that a rule-shaped row follows is read as a header, even in the middle of a table.** So a body row followed by `| - | - | - |`, or by a repeated `|---|---|---|`, is skipped along with it. A row naming a unit that still stands now passes in silence. At 683d9d55 the same row read `STANDING` in the section and `REFUSED` under a sub-heading.

The surviving `all` → `any` mutation is a gap that predates this run. It also survives at 321e9de1 against #835's predicate. It is not a finding of this run, and the cases in 🟡 1's fix kill it. ⬜ 3 is carried open and is not reported again.

The run is capped, so 🟡 1 is reported as a deferral candidate and not as a fix to commission. Its `Location` is in `removes_section`, which round 2's range changed, so `round-record` will count it as the run's second fix of a fix.

## Findings from reading, then execution

### Round 2's two findings are closed

Read: the header test no longer looks at a row's first cell. A row is a header when the next claim line is a rule row, and `not_rows` covers it together with every rule row. Both branches, the section and the sub-heading, consult the same set. The docstring, the case docstring changed at de5adcb9, and ledger row F1 now say a header is "the row a rule row directly follows whatever it reads", which matches the code.

Executed:

- The two new cases against `evidence_check.py` from 683d9d55: the three ids of `test_a_header_is_the_row_a_rule_row_follows` failed, and the boundary case passed. This matches what F3 and F4 claim ("red at 683d9d55's reader, 3 of 3"; "green at 683d9d55 by design").
- `level > 2` mutated to `level >= 2`, run against the boundary case: red, 1 failed. Round 2's 🟡 2 survivor is pinned now.
- The section branch's exemption narrowed from `not_rows` to `ruled`: red, all three header ids. This is one of the mutations F3 names.

### The smith's three sets match the paste-ready rule

Read: `cells_of` holds claim lines only, so `number + 1 in ruled` holds exactly when the next claim line is line `number + 1` and is a rule row. That is the paste-ready test `after == number + 1`. The union `ruled | header` is the paste-ready `ruled(text) or number in header`.

Executed: a temporary probe module, deleted afterwards. It compared `removes_section` at the head with a transcription of round 2's paste-ready version over 40,000 random sections drawn from headings, tables, rule rows, dash rows, fences, comments, marked lines and `nothing` lines. Every output was equal.

### 🟡 1 · A row followed by a rule-shaped row is read as a header, and a standing unit on it passes

`skills/evidence-check/scripts/evidence_check.py:6077`, in `removes_section`.

**What is wrong.** `not_rows` takes in every row whose next line is rule-shaped, wherever that row sits in a table. GFM recognises a delimiter row only directly under a table's first row. Further down, `| - | - | - |` or `|---|---|---|` is an ordinary body row. The reader now drops two rows there: the rule-shaped row, which it already dropped since #835, and the body row above it, which is new at b126895d.

**Why it matters.** This is the silent direction the section exists to close. A removal claim naming a unit that still stands is read by nobody:

| Input under `## Removes` | 683d9d55 | head |
|---|---|---|
| header, rule, a row naming a standing unit, then `\| - \| - \| - \|` | `STANDING spec.md:7` | nothing |
| the same, closed by `\|---\|---\|---\|` | `STANDING spec.md:7` | nothing |
| under `### Phase 2`, a foreign table with a body row naming a standing unit, then a rule-shaped row | `REFUSED` on the body row (read, not run) | nothing |

The first two rows of that table were executed at both readers. The third ran at the head only, as a case red without the patch below.

**Where it does not reach.** A two-line table, a row naming a unit and then a rule-shaped row directly under a blank line, is a header and a delimiter in GFM too. The head reads it as GFM does, and the patch below keeps that reading.

**Why 🟡 and not 🔴.** Both shapes are uncommon. The first is a filler row of dashes, and the second is a second table pasted under the first with no blank line between them. Neither loses a record or crashes. Still, the release would ship a silent pass that 683d9d55 did not have, so it is a defect and not a note.

**The fix.** Only a table's first row is a header, so the header test also asks that the line above is not a row. A rule-shaped row anywhere else is then read as a body row. In the section that row is refused as "not a coordinate", and under a sub-heading it is refused as a strayed row. Both are the loud direction.

Executed with the patch applied in the clone, then dropped:

- the two modules: 236 passed;
- without the patch, the two rule-shaped-row ids fail (2 failed, 4 passed);
- with the patch, dropping the first-row conjunct is red on those two ids, and `all` → `any` is red on the header-without-rule id.

### The surviving `all` → `any` is older than the run

Executed:

- At the head, `all(RULE_CELL_RE.match(c) …)` in `ruled` mutated to `any`, run against the two modules: SURVIVED, 232 passed.
- At 321e9de1, #835's section predicate `all(RULE_CELL_RE.match(c) for c in cells) or cells[0] == REMOVES_HEADING` mutated the same way, run against that commit's two modules: SURVIVED, 206 passed.
- At the head, with the two dash-cell ids of the fix below added, the same mutation is red.

So the quantifier has been pinned by nothing since #835. What this run changed is its reach. Under `any`, a body row whose Why cell reads `-` vanished at 321e9de1. At the head the row above it vanishes too, because it becomes a header. That widening is the 🟡 1 mechanism again, and the cases in 🟡 1's fix pin the quantifier. It goes to the same home as 🟡 1, as a row of `## Deferred` and not as a finding of its own.

### The new units, judged as code

`test_a_header_is_the_row_a_rule_row_follows` and `test_a_table_in_the_next_section_is_no_strayed_row` (depth 1) are correct. Their line numbers match the bodies they build, they assert the whole finding list rather than a membership, and the first is red at 683d9d55 as stated. Their gap is the one in 🟡 1: no id puts a rule-shaped row under a body row.

## Regression tests to plant

In `tests/test_a_record_states_what_the_tree_has.py`, four more ids of `test_a_header_is_the_row_a_rule_row_follows`, as fenced below: a rule-shaped row under a body row in the section; the same under a strayed row of a foreign table; a row with one dash cell; a row with one dash cell directly under a header with no rule row. The first two are red at the head. The last two pin `all` against `any`, at the head and on the patch respectively.

## Facts for the evidence ledger

- F3 states that a header is "known by the rule row under it". After the fix it is a table's first row when a rule row directly follows it, and a rule-shaped row anywhere else is a body row. The row's evidence then adds the two ids red at e6e236e4, plus the mutations red on the patch (first-row conjunct dropped; `all` → `any`).
- F1's parenthesis "(corrected in round 2)" carries the same sentence and moves with F3.
- The docstring of `removes_section` at lines 6051–6053 makes the same claim, and its replacement is fenced below.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | any row a rule-shaped row follows is read as a header, even mid-table: a body row followed by a row of dashes or a repeated rule row is skipped with it, so a row naming a standing unit passes where 683d9d55 read `STANDING` (section) or `REFUSED` (sub-heading) | `skills/evidence-check/scripts/evidence_check.py:6077` | open | probe at both readers (executed); the patch below applied in the clone and dropped, its new ids red without it (executed); the run is capped, so this is a `deferred` candidate, see `## Deferred` |
| 🟢 | round 2's finding 1 is closed — a header is known by the rule row under it: a foreign table's header is not refused, and a row reading `Removes` is refused under the sub-heading and `STANDING` in the section | `skills/evidence-check/scripts/evidence_check.py:6072` | confirmed | the 3 header ids red against 683d9d55's reader, green at the head; the section's exemption narrowed to `ruled` red (executed) |
| 🟢 | round 2's finding 2 is closed — the strayed-row refusal's stop at the next level-2 heading is pinned | `skills/evidence-check/scripts/evidence_check.py:6085` | confirmed | `level > 2` to `level >= 2` red on the boundary case; the case green at 683d9d55's reader by design (executed) |
| 🟢 | the smith's three sets read every input as round 2's nested `ruled()` does | `skills/evidence-check/scripts/evidence_check.py:6073` | confirmed | read: `cells_of` holds claim lines only, so `number + 1 in ruled` is the paste-ready adjacency test; 40,000 generated sections, outputs equal (executed) |
| 🟢 | the two new cases are correct as code, and the records the range touched read clean | `tests/test_a_record_states_what_the_tree_has.py:2133` | confirmed | read; `bin/evidence-check --strict .` exit 0, `bin/fold-check --root .` exit 0 at e6e236e4 (executed) |

## Paste-ready fixes

### 🟡 1 — the header test, in `removes_section`

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

### 🟡 1 — the docstring, lines 6051–6053

```
    is handed back to be refused (round 1 of #905, 🟡 1). A table's header,
    its first row when a rule row directly follows it, and that rule row
    name nothing and are not, there or in the section itself; a rule-shaped
    row anywhere else is a body row (rounds 2 and 3). A
```

### 🟡 1 — four ids appended to `test_a_header_is_the_row_a_rule_row_follows`

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

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| 🟡 1 — a row followed by a rule-shaped row is read as a header, and a standing unit on it passes | candidate: a new issue labelled `from-review` in milestone 0.21.1 (rung 3), carrying the paste-ready fix above; rung 1 also fits, because the branch wrote the unit, but the reopening bound lets this record commission no fix pass | the repository owner, who decides whether 0.21.1 ships the header rule with this hole or takes the fix before the release |
| the rule-row predicate's `all` is pinned by nothing: `any` survives the two modules at e6e236e4 and at 321e9de1 | the same issue as 🟡 1; the gap has existed since #835, and the cases in 🟡 1's fix pin it | the repository owner, with 🟡 1 |

Needs a fix: yes — 🟡 1 (a row followed by a rule-shaped row is read as a header, so a row naming a standing unit passes); the run is capped, so it takes the ladder in `## Deferred`

Loses a record or crashes: no

## Proof block

Opened: `skills/evidence-check/scripts/evidence_check.py` (`removes_section`, `removal_findings`, `cell_rule`, `claim_lines`, `RULE_CELL_RE`) at e6e236e4, 683d9d55 and 321e9de1; `tests/test_a_record_states_what_the_tree_has.py` (the fixtures and the cases of the range); `seal/ledger/1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes.md`; `docs/the-reader-registry.md` (the `Enforced by:` line); `templates/sdd-spec.md` (the `## Removes` comment); `rounds/round-1.md`, `rounds/round-2.md`, `rounds/round-2-report.md`; `docs/review-chain-spec.md` (the ladder and the reopening bound); `skills/code-review/scripts/round_record.py` (usage text); `bin/test`, `bin/mutation-check`. Carried rather than re-established: round 1's and round 2's coordinates; ⬜ 3 at `skills/evidence-check/scripts/evidence_check.py:6127`, still open, closes at the run's end.
