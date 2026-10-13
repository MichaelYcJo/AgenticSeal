# 1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes — review round 1 report

Target SHA: 43761b3a · base: `origin/release/v0.21.1` (321e9de1) · scope: the whole build, phases 1 to 3, the orchestrator's M1 amendment, the two divergences in `overview.md`, and the new paragraph in `agents/warden.md` §*Role*.
Reviewed in a `git clone --no-local` at the target, in the session scratchpad; the worktree was only read.

## Summary

The build does what the frame asked, and every acceptance row I could run holds. The refusal exists, the four new cases go red against the base reader and green at the head, and the two stale sentences are gone.

Two holes remain in the claim the build makes: "any other line in the section is `REFUSED` naming it", and `unknown refused` on the four `Reads:` lines.

1. **🟡 1 comes from the M1 amendment.** The section now ends at any heading, so a table row under a sub-heading of `## Removes` is read by nobody as a removal. At the base the same row read `STANDING`. The amendment's cost as `overview.md` states it covers prose under a sub-heading and leaves this out.
2. **🟡 2 is older than the branch, and the branch's claim is now false because of it.** A line carrying the `NAME NOT IN TREE` marker is dropped by `claim_lines` before `removes_section` sees it. Such a line under `## Removes` is neither refused nor read. A marked bullet passes, and a marked row naming a unit that still stands passes too. The template edit in this diff teaches the marker for the lines right beside the section, so writers will meet this case more often.

Both are claims of absence that nobody reads, which is the defect class #905 exists to end. A paste-ready patch for both was applied in the clone. Under it the two proposed cases go from red to green, the module passes, and `--strict` exits 0 on this tree.

## Findings from reading, then execution

### 🟡 1 · A table row under a sub-heading of `## Removes` is read by nobody as a removal

`skills/evidence-check/scripts/evidence_check.py:6053`. `removes_section` now ends the section at any heading (`if level is not None:`), so prose under `### Why these rows` is not refused. Every line after such a sub-heading is outside the section, and that includes table rows. Each row then goes to the name half, which reads `path#name` as a name that exists. A row naming a unit that still stands therefore passes with no finding.

Executed, in a temporary probe module run at the target and at the base, then deleted:

| Section body | Base 321e9de1 | Target 43761b3a |
|---|---|---|
| `### Phase 1`, then the table with one row naming a unit that still stands, unrequired | `STANDING spec.md:9` | no finding |
| the same, required by `Removes from` | `STANDING spec.md:9` | `REFUSED` "has an empty `## Removes` section", which is wrong about a section that holds a table |
| a table, then `### Phase 2` and a second table whose row names a unit that still stands, required or not | `STANDING` on both rows | `STANDING` on the first row only; the second passes silently |

Why it matters: splitting removal rows by phase under `###` headings is a natural shape, since the per-phase removal table the section replaced was exactly that. The amendment told every sibling frame of this run to put things under a sub-heading. At the base the shape was read; at the head it is a silent pass, so this is a removed behaviour with nothing re-establishing it. The cost the smith named in `overview.md` row 2 and in `questions.md` M1 is the loud half, prose names read as NOT-IN-TREE. This is the silent half. The amendment itself is sound for prose, and the fix keeps it. A table row under a sub-heading of the section is refused naming it, and the message says to move it into the table above.

### 🟡 2 · A line carrying the marker under `## Removes` is neither refused nor read

`skills/evidence-check/scripts/evidence_check.py:6051`. `removes_section` reads `claim_lines(lines)`, and `claim_lines` drops every line carrying `NAME NOT IN TREE` (`if NOT_IN_TREE in line or not rest.strip(): continue`). The marker exists to exempt a line from the name half. The section is not the name half's to read: `cut` already keeps the name half off it. So the marker here has no purpose except to make a line invisible to the section's reader.

Executed, in the same probe at both SHAs, with identical results, so the hole predates the branch:

- a bullet naming a standing unit with the marker, beside a valid row: only the row's own finding, and the bullet passes;
- a row naming a standing unit with the marker in its last cell: no finding unrequired, and "has an empty `## Removes` section" required.

Why this is the branch's to fix: the diff writes "Any other line in the section is `REFUSED` naming it" into `docs/the-reader-registry.md:129`. It keeps `unknown refused` on the four lines on the strength of that sentence, and a ledger row (R1) holds it. Read through, a marked line ends passed, so the four words are still `mixed` for one input. The same diff's template comment (`templates/sdd-spec.md:43`) tells a writer to put the marker on removed-unit lines directly under the section's sub-heading. That is one heading away from where it silently swallows a removal. The `Reads:` line of `removes_section` does scope its input to "the lines `claim_lines` reads". A reader of the registry sentence or of `removal_findings`' docstring, however, gets no hint of that scope. This is the case the new paragraph in `agents/warden.md` asks this round to look for, a helper's line read at its caller, and it is how the hole was found.

### ⬜ 3 · The off-shape refusal talks about a table where the section holds none

`skills/evidence-check/scripts/evidence_check.py:6127`. For the wrapped second line of a `nothing` reason, the S1 case "a wrapped reason", the detail says prose "goes under a sub-heading after the table". That section has no table, and a wrapped reason wants joining onto one line rather than a sub-heading. The detail also nests the quoted line's own backticks inside a backtick span, so a bullet like ``- `mod.py#x` goes`` renders broken. The existing `nothing` refusal has the same shape. The behaviour is right and only the sentence reads badly, so this is a note.

### What was judged and holds

- **The four `Reads:` words.** Apart from 🟡 1 and 🟡 2, an off-shape line ends `REFUSED` at `removal_findings`, which `file_claims` and `check_records` return unchanged (read). The diff to `evidence_check.py` has hunks in `removes_section` and `removal_findings` only (read, S4).
- **The M1 amendment as built.** Ending at any heading gives prose a home that is read, which is the direction the frame argued for. The cost the smith named is real: names in backticks under the sub-heading are read by the name half. That cost is loud, a NOT-IN-TREE at exit 2, which is the right direction. `test_a_heading_of_any_level_ends_the_section` pins it, and red at the base was confirmed (below). Its silent half is 🟡 1.
- **`overview.md` divergence 1, thirteen drifted rows.** Executed at 8879db49, before the fragment existed: `bin/evidence-check .` reports 13 DRIFTED. Twelve are on `agents/warden.md#"## Role"` (region 84-397) and one is on the registry's title. The fragment holds six `Re-read ·` rows, five covering the warden rows by family and D1. At the head, `--strict` reports 0 drifted. The divergence is stated truly. Moving the sentence out of §*Role* would have left In 4 unbuilt, as the row says. Every later edit of §*Role* pays the same twelve re-reads, but that predates this branch.
- **`overview.md` divergence 2, the refusal wording.** It matches the amendment, and §14 is met: `off_shape` in the test module pins the detail whole.
- **The new paragraph in `agents/warden.md` §*Role*, P2 (a).** It is five lines in a body every spawn loads. It sits in the bullet about claims, where "a `Reads:` line is a claim too" belongs, and it tells the warden an act the registry's limit 5 now names. I judge it worth its cost on this round's own evidence: following it is how 🟡 2 surfaced. The registry's lead, limit 5, the `Enforced by:` line and the test module's item 5 now name one reader (read).
- **The recorder sentence, ⬜ 5 of #834.** "Not measured where the suite failed, and existence alone on the ledger arm" matches `broad_gate.py`'s `NO_RECORD_AT_HEAD` path and `evidence_check.py`'s existence line (read). `git grep -n "the strict side" -- skills` exits 1 (executed).

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | the section now ends at any heading, so a table row under a sub-heading of `## Removes` is read by the name half alone and a row naming a unit that still stands passes; at the base it read `STANDING`; required, a table under a sub-heading reads as an empty section | `skills/evidence-check/scripts/evidence_check.py:6053` | open | probe at both SHAs (executed); the M1 amendment's stated cost names prose only |
| 🟡 2 | a line carrying the marker under `## Removes` is dropped by `claim_lines` before `removes_section` reads it: a marked bullet passes and a marked row naming a standing unit is never read, so "any other line in the section is `REFUSED`" and the four `unknown refused` words are false for that input | `skills/evidence-check/scripts/evidence_check.py:6051` | open | probe at both SHAs (executed), same result, so older than the branch; the branch's registry sentence and template comment make the claim and teach the marker |
| ⬜ 3 | the off-shape refusal tells a wrapped `nothing` reason to move under a sub-heading "after the table" where there is no table, and nests the quoted line's backticks | `skills/evidence-check/scripts/evidence_check.py:6127` | open | read; behaviour right, the sentence reads badly |
| 🟢 | S1 to S3 and the M1 case hold: each of the 11 parametrised cases fails against the base reader and passes at the head, and S2's case passes at both by design | `tests/test_a_record_states_what_the_tree_has.py` | confirmed | the head's test module run against the base code: 11 failed, 1 passed; at the head 142 passed (executed) |
| 🟢 | S5 and S6: the stale sentences are gone and the registry names one reader | `docs/the-reader-registry.md:154` | confirmed | both `git grep` checks exit 1; `bin/fold-check --root .` exit 0 (executed) |
| 🟢 | S7: the records read clean | `seal/ledger/1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes.md` | confirmed | `bin/evidence-check --strict .` exit 0, 0 drifted, records arm 0 refused (executed) |
| 🟢 | the warden paragraph (P2 (a)) is placed, worded and costed soundly | `agents/warden.md:111` | confirmed | read; it is how 🟡 2 was found |
| ❓ | S8: the gate's four requirements in the pull request body | PR #915 body | ❓ out of verified scope | not read this round; the orchestrator answers it when the body is written, and 🟡 1 changes the direction statement's "a wrong allow" case |

## Executed probes

| What was run | Result |
|---|---|
| `bin/evidence-check --strict .` at 43761b3a in the clone | exit 0; 8451 ok, 0 drifted; records arm 0 refused |
| `bin/evidence-check .` at 8879db49, before the fragment, in a second clone | exit 1; 13 DRIFTED: 12 on `agents/warden.md#"## Role"` and the registry's title |
| `bin/fold-check --root .` at 43761b3a | exit 0; 19 documents, 0 over the ceiling |
| `git grep -n "does not show its line" -- docs tests agents`; `git grep -n "the strict side" -- skills` | exit 1 and exit 1, no output |
| the head's `tests/test_a_record_states_what_the_tree_has.py`, the four new tests only, against the base code 321e9de1 | exit 1; 11 failed, 1 passed (S2, by design) |
| `bin/test tests/test_a_record_states_what_the_tree_has.py -q -p no:cacheprovider` at 43761b3a, with `SPECSEAL_CASE_CEILING_S=600` | exit 0; 142 passed |
| a temporary probe module of 10 cases over the section's shapes, at 43761b3a and at 321e9de1, serially; deleted after the run | 🟡 1 and 🟡 2 as tabled above; a `---` line is refused at the head, which is loud and acceptable |
| the paste-ready patch below applied in the clone, with the two proposed cases in a temporary module; then the patch stashed and dropped, the module deleted, and the clone left clean at 43761b3a | patched: 146 passed and `--strict` exit 0; unpatched: the 4 proposed cases fail |
| the broad gate (full suite, repository-wide lint, typecheck) | not yet, not run by this round; it is the sealer's after the rounds settle |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

## Paste-ready fixes

### 🟡 1 and 🟡 2 — `removes_section` and `removal_findings`

```python
    split = cell_rule()
    present, inside, under = False, False, False
    cut, rows, nothing, other, strayed = set(), [], [], [], []
    # The marker exempts a LINE from the name half, and the section is not
    # the name half's: a marked line here is read by the section's shapes
    # like any other (round 1 of #905, 🟡 2).
    unmarked = [line.replace(NOT_IN_TREE, "") for line in lines]
    for number, text in claim_lines(unmarked):
        level = heading_level(text)
        if level is not None:
            # A sub-heading ends the section so prose has a home, and a table
            # row under it is still a removal nobody would read (🟡 1).
            under = (inside or under) and level > 2
            inside = level == 2 and text.strip().lstrip("#").strip() == REMOVES_HEADING
            present = present or inside
            continue
        if under:
            cells = split(text)
            if cells is not None and not all(RULE_CELL_RE.match(c) for c in cells):
                cut.add(number)
                strayed.append((number, text.strip()))
            continue
        if not inside:
            continue
```

```python
        rows.append((number, cells))
    return present, cut, rows, nothing, other, strayed
```

```python
    present, cut, rows, nothing, other, strayed = removes_section(lines)
```

Placed after the `for number, text in other:` loop in `removal_findings`:

```python
    for number, text in strayed:
        findings.append(
            (
                REFUSED_STATUS,
                f"{shown}:{number}",
                f"`{text}` — a table row under a sub-heading of `## Removes` is "
                "not read as a removal; move it into the table above the "
                "sub-heading, or write it as prose",
            )
        )
```

The docstring of `removes_section` then names a sixth element, and its `Reads:` line reads "on the lines `claim_lines` reads with the marker blanked". The registry sentence at `docs/the-reader-registry.md:129` gains one clause, and the changelog's item 2 gains the same:

```
under a sub-heading after the table, where it is read as the rest of the
frame is; a table row under that sub-heading is `REFUSED` too, and the
marker exempts no line of the section. The names on the section's lines are
```

### ⬜ 3 — the refusal's wording

```python
                f"`{text}` — a line under `## Removes` is a table row or one "
                "`nothing — <why>` line, written on one line; prose about the "
                "rows goes under a sub-heading after the section, such as "
                "`### Why these rows`",
```

## Regression tests to plant

Destination `tests/test_a_record_states_what_the_tree_has.py`, after `test_a_heading_of_any_level_ends_the_section`. Both were run: red at 43761b3a (4 of 4 cases) and green under the patch above.

```python
@pytest.mark.parametrize("required", [False, True], ids=["unrequired", "required"])
def test_a_table_row_under_a_sub_heading_of_removes_is_refused(tmp_path, required):
    """Round 1 of #905, 🟡 1. The section ends at any heading so prose has a
    home, and a table row under that sub-heading is refused naming it —
    never read by the name half alone, where a unit that still stands
    passes."""
    tree(tmp_path, **{"mod.py": "def old_reader():\n    return 1\n"})
    h = home(tmp_path)
    if required:
        removes_config(tmp_path, "1780000000")
    body = REMOVES_TABLE + "\n### Phase 2\n\n| y | `mod.py#old_reader` | z |\n"
    work_item(
        h,
        "1780000000-live",
        **{"spec.md": "# frame\n\n## Removes\n\n" + body + REMOVES_TAIL},
    )
    found, _ = refusals(tmp_path)
    assert [(s, c.replace(os.sep, "/").rsplit("/", 1)[-1], d) for s, c, d in found] == [
        (
            "REFUSED",
            "spec.md:11",
            "`| y | `mod.py#old_reader` | z |` — a table row under a sub-heading "
            "of `## Removes` is not read as a removal; move it into the table "
            "above the sub-heading, or write it as prose",
        )
    ]


@pytest.mark.parametrize(
    ("body", "expected"),
    [
        (
            REMOVES_TABLE + "- `mod.py#old_reader` goes too NAME NOT IN TREE\n",
            ("REFUSED", "spec.md:8"),
        ),
        (
            REMOVES_TABLE.replace(
                "`gone.py#x` | y", "`mod.py#old_reader` | y NAME NOT IN TREE"
            ),
            ("STANDING", "spec.md:7"),
        ),
    ],
    ids=["a marked bullet", "a marked row"],
)
def test_the_marker_exempts_no_line_of_the_removes_section(tmp_path, body, expected):
    """Round 1 of #905, 🟡 2. The marker exempts a line from the name half,
    and the section is not the name half's: a marked line under `## Removes`
    is read by the section's shapes like any other."""
    tree(tmp_path, **{"mod.py": "def old_reader():\n    return 1\n"})
    h = home(tmp_path)
    work_item(
        h,
        "1780000000-live",
        **{"spec.md": "# frame\n\n## Removes\n\n" + body + REMOVES_TAIL},
    )
    found, _ = refusals(tmp_path)
    assert [(s, c.replace(os.sep, "/").rsplit("/", 1)[-1]) for s, c, _d in found] == [
        expected
    ]
```

The registry's `Enforced by:` line at `docs/the-reader-registry.md` §*A frame names what its work removes* gains both node ids.

## Facts for the evidence ledger

- A behaviour row for each new case, held by its node id, in this item's fragment beside S1 to M1.
- R1's quoted anchor moves with the registry sentence's new clause, and R1's claim gains "a table row under the sub-heading is refused, and the marker exempts no line of the section".
- The drift of `agents/warden.md#"## Role"` on any later edit of §*Role* costs twelve released readings in five families (measured at 8879db49). That is a fact about the anchor, and it belongs in the next re-read's grounds rather than in a new row.

Needs a fix: yes — 🟡 1 (a table row under a sub-heading of `## Removes` is read by nobody as a removal) and 🟡 2 (a marked line under `## Removes` is neither refused nor read)
Loses a record or crashes: no

The broad gate has not come due: two findings need a fix, so a verifying round follows them before the sealer's spawn.

## Proof block

Opened and read at 43761b3a in the clone: `spec.md` (Grounding, Scope, acceptance, Data & interfaces, Removes), `questions.md`, `overview.md`, `changelog.md`, the ledger fragment, `skills/evidence-check/scripts/evidence_check.py` (`cell_rule`, `heading_level`, `claim_lines`, `removes_section`, `removal_findings`, `file_claims`), `skills/verify/scripts/pytest_record/specseal_pytest_record.py:95-112`, `skills/verify/scripts/broad_gate.py:2180-2230` and its record-absence names, `templates/sdd-spec.md:30-60`, `agents/framer.md:338-350`, `templates/config.md:108-118`, the full diff of `agents/warden.md`, `docs/the-reader-registry.md`, `tests/test_a_reader_declares_its_input_class.py` and `tests/test_a_record_states_what_the_tree_has.py`, and that test module's helpers. Not opened: `plan.md` and `phases/phase-1.md` to `phase-3.md` beyond what the ledger and overview cite.
