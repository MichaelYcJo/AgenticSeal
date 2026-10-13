# 1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes — review round 2 report

Target SHA: 2989accd · base: `origin/release/v0.21.1` (321e9de1) · scope: the fix range `e3ae4cb6..8d636bd1`, 3 commits, the verifying round.
Reviewed in a `git clone --no-local` at the target, in the session scratchpad; the worktree was only read. Every suite run below set `SPECSEAL_CASE_CEILING_S=600`.

## Summary

Both findings round 1 recorded as fixed are closed. Round 1's own reproductions now end `REFUSED`, the ten new cases go red against the reader at e3ae4cb6 and green at the head, and the four mutations the fragment names are red.

The fix wrote one new branch into `removes_section`, the one that reads a table row under a sub-heading. Nobody had reviewed it, and it carries two findings of its own:

1. **🟡 1 — the new branch knows a table's header by its first cell reading `Removes`.** A foreign table's header under the sub-heading is therefore refused as a row. A body row whose first cell reads `Removes` passes in silence, even when it names a unit that still stands. The docstring and ledger row F1 both state the opposite for the header. The section's own table, older than the branch, carries the same silent pass.
2. **🟡 2 — nothing pins where the new branch stops.** Its bound, "up to the next heading of level 2 or above", survives `level > 2` mutated to `level >= 2` in both modules and in the tree's own `--strict` run.

Both go beyond the paste-ready fix in the same two places the smith went beyond it: the header exemption, and the new branch's bound. ⬜ 3 is carried open and is not reported again.

## Findings from reading, then execution

### Round 1's two findings are closed

Read: `removes_section` now blanks `NAME NOT IN TREE` on a copy of the lines before `claim_lines` reads them, so a marked line under `## Removes` is read by the section's shapes. A level-3-or-deeper heading after the section sets `under`, and a table body row there is refused naming it and added to `cut`. The marker blanking cannot move a fence or comment boundary: `claim_lines` tests the marker only after it has decided a line's fence and comment state, so its state machine is the same for the blanked copy. The name half still reads the original lines, so a marked prose line under the sub-heading stays exempt, as the template says.

Executed:

- The head's ten new cases against `evidence_check.py` from e3ae4cb6: 10 failed. At the head they pass.
- Round 1's first reproduction input, `### Phase 1` then the table with one row naming a unit that still stands: unrequired, `REFUSED spec.md:9` with the strayed-row message. Required, the empty-section refusal and the same strayed-row refusal. At the base this input was a silent pass.
- Mutations through `bin/mutation-check`, each run against the two modules: the rule-row exemption under the sub-heading dropped, the header exemption dropped, the strayed row left out of `cut`, the marker kept in the lines, and `under = inside and level > 2`. All five are red, which matches the four the F1 and F2 rows name.

### 🟡 1 · A foreign table's header is refused, and a row whose first cell reads `Removes` passes

`skills/evidence-check/scripts/evidence_check.py:6076`. The new branch exempts a row from refusal when `cells[0] == REMOVES_HEADING`. That is a header test by content, and it is wrong in both directions.

Executed, in a temporary probe module at the target, deleted afterwards:

| Body under `### …` after the section's table | At 2989accd |
|---|---|
| `\| Before \| After \|`, a rule row, `\| a \| b \|` | `REFUSED` on the header row and on the body row. The header's message tells the writer to move it "into the table above". |
| `\| Removes \| `mod.py#old_reader` \| z \|`, naming a unit that still stands | no finding |
| the same row inside the section's own table | no finding; `STANDING` is owed |

Why it matters:

- The docstring at line 6052 says "A second table's header and rule rows name nothing and are not" refused. Ledger row F1 says the same. Both are false for any header that does not begin `Removes`.
- The second and third rows are a claim of absence nobody reads, which is the class #905 exists to end. The third row is older than the branch: line 6091 has had the same test since #835. The new branch copied it, so §12 puts both on this fix.

The input is unusual, since the first column describes the removed thing. The header half, though, is a shape the template invites: prose and its own tables go under `### Why these rows`.

The fix reads a header as what it is in markdown, the row a rule row directly follows, in both branches. Executed in the clone: the patch below plus three proposed cases. Unpatched, the 3 cases fail. Patched, the cases and both modules pass (233 passed), and `bin/evidence-check --strict .` exits 0. The patch was then stashed and dropped.

### 🟡 2 · Where the new branch stops is pinned by no case

`skills/evidence-check/scripts/evidence_check.py:6069`. `under = (inside or under) and level > 2` is what stops the strayed-row refusal at the frame's next section. Executed with `bin/mutation-check`:

- With `level >= 2`, `tests/test_a_record_states_what_the_tree_has.py` and `tests/test_a_reader_declares_its_input_class.py` still pass: 228 passed, SURVIVED.
- `bin/evidence-check --strict .` on this tree also passes under that mutant, so no live frame pins it either.

Under the mutant, every table body row in every section after `## Removes` is refused as a strayed removal row. That is loud rather than silent. It is still the stated bound of a unit no round had reviewed, and both the docstring and the registry sentence write it down. One proposed case kills the mutant: red under `>= 2`, green at the head.

The smith may answer this with grounds instead: the direction of the failure is loud. A paste-ready case is below for the other answer.

### What was judged and holds

- **The `strayed` helper, `STANDING_ROW`, `GONE_ROW`, and the two new cases** (read and executed). The helper pins the refusal whole, as §14 asks. Each parametrised id is the input it names. "A row under a second sub-heading" kills `under = inside and level > 2`, and "a row naming a unit that is gone" kills the strayed row left out of `cut`. Both were confirmed red above.
- **The second table's rule row and header** are exempt only for the template's own header, which the "whole second table" id pins. That id is the only header shape it pins, and 🟡 1 covers that.
- **The registry sentence, the template comment and the changelog items** (read) say what the code does, apart from 🟡 1's header claim, which sits in the docstring and F1 only.
- **The ledger fragment** (executed): `bin/evidence-check --strict .` exits 0 with 0 drifted and 0 refused on the records arm. `bin/fold-check --root .` exits 0. The re-hashed R1, R2 and D1 rows read.
- **A heading that carries the marker** now ends the section, where before it was dropped and the section ran on. That is the markdown reading, and probing it confirmed no finding.

### Carried

⬜ 3, the off-shape refusal's wording, is carried open from round 1 and closes at the run's end. It is not reported again.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | the new branch knows a header by its first cell reading `Removes`: a foreign table's header under the sub-heading is refused as a row, and a body row whose first cell reads `Removes` passes naming a standing unit; the section's own table has the same silent pass since #835; the docstring at line 6052 and ledger row F1 claim a second table's header is not refused | `skills/evidence-check/scripts/evidence_check.py:6076` | open | probe at the target (executed); the patch below, applied in the clone and dropped (executed) |
| 🟡 2 | the new branch's stop at the next heading of level 2 or above is pinned by nothing: `level >= 2` survives both modules and the tree's `--strict` run | `skills/evidence-check/scripts/evidence_check.py:6069` | open | `bin/mutation-check`, SURVIVED twice (executed); the proposed case red under the mutant (executed) |
| 🟢 | round 1's finding 1 is closed: a table row under a sub-heading of `## Removes` is refused naming it, required or not, and is not also read by the name half | `skills/evidence-check/scripts/evidence_check.py:6073` | confirmed | the 8 new ids red at e3ae4cb6's reader and green at the head; round 1's first input replayed; three mutants red (executed) |
| 🟢 | round 1's finding 2 is closed: a marked line under `## Removes` is read by the section's shapes, and the blanking moves no fence or comment boundary | `skills/evidence-check/scripts/evidence_check.py:6065` | confirmed | the 2 new ids red at e3ae4cb6's reader and green at the head; the marker-kept mutant red (executed); `claim_lines` read |
| 🟢 | the records and documents the fix range touched read clean | `seal/ledger/1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes.md` | confirmed | `bin/evidence-check --strict .` exit 0; `bin/fold-check --root .` exit 0 (executed) |

## Executed probes

| What was run | Result |
|---|---|
| `bin/test tests/test_a_record_states_what_the_tree_has.py -q -p no:cacheprovider -k "sub_heading_of_removes or marker_exempts or heading_of_any_level or off_shape"` at 2989accd | exit 0; 26 passed |
| the same module's new cases, `-k "sub_heading_of_removes or marker_exempts"`, with `evidence_check.py` taken from e3ae4cb6; the file restored after | exit 1; the 10 new ids failed, 5 other selected cases passed |
| `bin/mutation-check` on `evidence_check.py`, tests `bin/test` over the two modules: rule-row exemption under the sub-heading dropped; header exemption dropped; strayed row not added to `cut`; marker kept in the lines | red, red, red, red |
| `bin/mutation-check`, `under = inside and level > 2`, tests `-k sub_heading_of_removes` | red; 2 failed (the second sub-heading id) |
| `bin/mutation-check`, `level > 2` to `level >= 2`, tests the two modules | SURVIVED; 228 passed |
| `bin/mutation-check`, `level > 2` to `level >= 2`, tests `bin/evidence-check --strict .` | SURVIVED |
| a temporary probe module at 2989accd over a foreign table's header, a row whose first cell reads `Removes` under the sub-heading and in the section, a marked sub-heading, and round 1's first input; deleted after the run | as tabled under 🟡 1; the marked sub-heading ends the section with no finding; round 1's first input refused |
| the 🟡 1 patch applied in the clone with the proposed cases, then stashed and dropped | patched: 233 passed over the probe and the two modules, `--strict` exit 0; unpatched: the 3 header cases fail and the boundary case passes; under `level >= 2` the boundary case fails |
| `bin/evidence-check --strict .` and `bin/fold-check --root .` at 2989accd | exit 0 and exit 0 |
| the broad gate (full suite, repository-wide lint, typecheck) | not yet; not run by this round, it is the sealer's after the rounds settle |

## Paste-ready fixes

### 🟡 1 — a header is the row a rule row follows

In `removes_section`, replacing the loop's head and both header tests:

```python
    unmarked = [line.replace(NOT_IN_TREE, "") for line in lines]
    read = claim_lines(unmarked)

    def ruled(text):
        cells = split(text)
        return cells is not None and all(RULE_CELL_RE.match(c) for c in cells)

    # A header is the row a rule row directly follows, whatever its first
    # cell reads (round 2 of #905).
    header = {
        number
        for (number, text), (after, rule) in zip(read, read[1:])
        if after == number + 1 and split(text) is not None and ruled(rule)
    }
    for number, text in read:
        level = heading_level(text)
        if level is not None:
            under = (inside or under) and level > 2
            inside = level == 2 and text.strip().lstrip("#").strip() == REMOVES_HEADING
            present = present or inside
            continue
        if under:
            cells = split(text)
            if cells is not None and not (ruled(text) or number in header):
                cut.add(number)
                strayed.append((number, text.strip()))
            continue
```

```python
        if ruled(text) or number in header:
            continue
        rows.append((number, cells))
```

The docstring sentence at line 6052, and F1's claim in the same words:

```
    is handed back to be refused (round 1 of #905, 🟡 1). A table's header,
    the row a rule row directly follows whatever it reads, and its rule row
    name nothing and are not, there or in the section itself.
```

Destination `tests/test_a_record_states_what_the_tree_has.py`, after the marker test:

```python
@pytest.mark.parametrize(
    ("body", "expected"),
    [
        (
            REMOVES_TABLE
            + "\n### Why these rows\n\n| Before | After |\n|---|---|\n| a | b |\n",
            [("REFUSED", "spec.md:13")],
        ),
        (
            REMOVES_TABLE + "\n### Phase 2\n\n| Removes | `mod.py#old_reader` | z |\n",
            [("REFUSED", "spec.md:11")],
        ),
        (
            REMOVES_TABLE.replace(
                "| x | `gone.py#x` |", "| Removes | `mod.py#old_reader` |"
            ),
            [("STANDING", "spec.md:7")],
        ),
    ],
    ids=[
        "a foreign table's header",
        "a row reading Removes under the sub-heading",
        "a row reading Removes in the section",
    ],
)
def test_a_header_is_the_row_a_rule_row_follows(tmp_path, body, expected):
    """Round 2 of #905, 🟡 1. A header is known by the rule row under it,
    never by its first cell: a foreign table's header names no removal, and
    a body row whose first cell reads `Removes` is still a row."""
    tree(tmp_path, **{"mod.py": "def old_reader():\n    return 1\n"})
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"spec.md": "# frame\n\n## Removes\n\n" + body + REMOVES_TAIL},
    )
    found, _ = refusals(tmp_path)
    assert [
        (s, c.replace(os.sep, "/").rsplit("/", 1)[-1]) for s, c, _d in found
    ] == expected
```

### 🟡 2 — the new branch stops at the next section

Destination `tests/test_a_record_states_what_the_tree_has.py`, after the case above. Red under `level >= 2`, green at the head:

```python
def test_a_table_in_the_next_section_is_no_strayed_row(tmp_path):
    """Round 2 of #905, 🟡 2. A table row under a sub-heading of `## Removes`
    is refused up to the next heading of level 2 or above and no further: a
    table in the frame's next section is read as the rest of the frame is."""
    tree(tmp_path, **{"mod.py": "def old_reader():\n    return 1\n"})
    h = home(tmp_path)
    body = (
        REMOVES_TABLE
        + "\n### Why these rows\n\nProse.\n\n## Data & interfaces\n\n"
        + "| Unit | Why |\n|---|---|\n| `mod.py#old_reader` | z |\n"
    )
    work_item(
        h,
        "1780000000-live",
        **{"spec.md": "# frame\n\n## Removes\n\n" + body + REMOVES_TAIL},
    )
    found, _ = refusals(tmp_path)
    assert found == []
```

The registry's `Enforced by:` line in `docs/the-reader-registry.md` §*A frame names what its work removes* gains both node ids.

## Regression tests to plant

The two cases above, in `tests/test_a_record_states_what_the_tree_has.py`. Both were seen red: the header case against the reader at 2989accd (3 of 3), the boundary case under the `level >= 2` mutant.

## Facts for the evidence ledger

- F1's claim is corrected to the header rule above once the fix lands. As it stands, it states that a second table's header is not refused, and that holds only for a header beginning `Removes`.
- A behaviour row for each new case, held by its node id, beside F1 and F2.

Needs a fix: yes — 🟡 1 (a header is known by its first cell, so a foreign header is refused and a row reading `Removes` passes naming a standing unit) and 🟡 2 (the new branch's bound at level 2 is pinned by nothing)
Loses a record or crashes: no

The broad gate has not come due: two findings are open, so the sealer's spawn waits for their answer.

## Proof block

Opened and read at 2989accd: `rounds/round-1.md` and `rounds/round-1-report.md`; the full diff `e3ae4cb6..8d636bd1` (`evidence_check.py`, `docs/the-reader-registry.md`, `templates/sdd-spec.md`, the changelog fragment, the ledger fragment, the test module); in `evidence_check.py`, `cell_rule`, `heading_level`, `claim_lines` whole, `removes_section`, `removal_findings` to the coordinate checks, and the caller in `file_claims` that spends `cut`; in the test module, `tree`, `refusals`, `REMOVES_HEAD`, `REMOVES_TAIL`, `REMOVES_TABLE` and `off_shape`; the template's heading order. Not opened: `overview.md`, `plan.md` and the phase files, which the fix range does not touch.
