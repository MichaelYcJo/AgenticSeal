# 1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes — review round 2

| Field | Value |
|---|---|
| Target SHA | 2989accd21bced353f027a1e862852e68e36064f |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #915 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are written and no round has opened them |
| Fix range | `683d9d55b6dcfb5bd773cc48688f495d24577ee3..de5adcb99f96bc050e3944d645b5a8e497f9fda0`, 3 commits |
| Contract changes | none |
| New units | test_a_header_is_the_row_a_rule_row_follows (depth 1); test_a_table_in_the_next_section_is_no_strayed_row (depth 1) |
| Fix of a fix | first — 🟡 1 at skills/evidence-check/scripts/evidence_check.py#removes_section, a unit round-1's fixes changed; 🟡 2 at skills/evidence-check/scripts/evidence_check.py#removes_section, a unit round-1's fixes changed |
| Needs a fix | yes — 🟡 1 (a header is known by its first cell, so a foreign header is refused and a row reading `Removes` passes naming a standing unit) and 🟡 2 (the new branch's bound at level 2 is pinned by nothing) |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 2 of #905, the verifying round, target 2989accd: the diff of round 1's fixes, `e3ae4cb6..8d636bd1`. The reviewer was asked whether 🟡 1 and 🟡 2, recorded fixed at d93f700b, are closed; to treat `strayed`, `STANDING_ROW`, `GONE_ROW` and the two new cases as a finding surface; and to judge the smith's two additions past the paste-ready fix — a second table's header row not refused, and two surviving mutations made into cases.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | the new branch knows a header by its first cell reading `Removes`: a foreign table's header under the sub-heading is refused as a row, and a body row whose first cell reads `Removes` passes naming a standing unit; the section's own table has the same silent pass since #835; the docstring at line 6052 and ledger row F1 claim a second table's header is not refused | `skills/evidence-check/scripts/evidence_check.py:6076` | **fixed** `b126895d` | fixed at b126895d; probe at the target (executed); the patch below, applied in the clone and dropped (executed) |
| 🟡 2 | the new branch's stop at the next heading of level 2 or above is pinned by nothing: `level >= 2` survives both modules and the tree's `--strict` run | `skills/evidence-check/scripts/evidence_check.py:6069` | **fixed** `b126895d` | fixed at b126895d; `bin/mutation-check`, SURVIVED twice (executed); the proposed case red under the mutant (executed) |
| 🟢 | round 1's finding 1 is closed: a table row under a sub-heading of `## Removes` is refused naming it, required or not, and is not also read by the name half | `skills/evidence-check/scripts/evidence_check.py:6073` | confirmed | the 8 new ids red at e3ae4cb6's reader and green at the head; round 1's first input replayed; three mutants red (executed) |
| 🟢 | round 1's finding 2 is closed: a marked line under `## Removes` is read by the section's shapes, and the blanking moves no fence or comment boundary | `skills/evidence-check/scripts/evidence_check.py:6065` | confirmed | the 2 new ids red at e3ae4cb6's reader and green at the head; the marker-kept mutant red (executed); `claim_lines` read |
| 🟢 | the records and documents the fix range touched read clean | `seal/ledger/1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes.md` | confirmed | `bin/evidence-check --strict .` exit 0; `bin/fold-check --root .` exit 0 (executed) |

## Paste-ready fixes

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
```
    is handed back to be refused (round 1 of #905, 🟡 1). A table's header,
    the row a rule row directly follows whatever it reads, and its rule row
    name nothing and are not, there or in the section itself.
```
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

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `skills/evidence-check/scripts/evidence_check.py:6053` | round 1's 🟡 1 — fixed |
| round-1 | `skills/evidence-check/scripts/evidence_check.py:6051` | round 1's 🟡 2 — fixed |
| round-1 | `skills/evidence-check/scripts/evidence_check.py:6127` | round 1's ⬜ 3 — open |
| round-1 | `tests/test_a_record_states_what_the_tree_has.py` | round 1's 🟢 — confirmed |
| round-1 | `docs/the-reader-registry.md:154` | round 1's 🟢 — confirmed |
| round-1 | `seal/ledger/1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes.md` | round 1's 🟢 — confirmed |
| round-1 | `agents/warden.md:111` | round 1's 🟢 — confirmed |
| round-1 | PR #915 body | round 1's ❓ — out of verified scope |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

nothing to drain
