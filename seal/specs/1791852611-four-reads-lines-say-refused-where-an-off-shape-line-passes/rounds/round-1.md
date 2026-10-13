# 1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes — review round 1

| Field | Value |
|---|---|
| Target SHA | 43761b3ac43e4617e2403523b0c527988ff3f918 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #915 |
| Broad gate | not yet |
| Fixes checked by | round-2 |
| Fix range | `e3ae4cb685094d4aee755627f6ae7d9d92c15def..8d636bd164cca6cb7b657040af3410df943185ea`, 3 commits |
| Contract changes | removes_section → round-1-report.md, round-1.md, removal_findings |
| New units | strayed (depth 1); STANDING_ROW (depth 1); GONE_ROW (depth 1); test_a_table_row_under_a_sub_heading_of_removes_is_refused (depth 1); test_the_marker_exempts_no_line_of_the_removes_section (depth 1) |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1 (a table row under a sub-heading of `## Removes` is read by nobody as a removal) and 🟡 2 (a marked line under `## Removes` is neither refused nor read) |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 1 of #905, target 43761b3a against `origin/release/v0.21.1` at 321e9de1, over the whole build, phases 1–3. The reviewer was asked to judge the orchestrator's amendment as built — the `## Removes` section ends at a heading of any level and the refusal sends prose to a sub-heading, because 4 of 5 frames of this run wrote prose under their table — including the cost the smith named (a backticked name in a sub-heading's prose is read by the name half); the divergences in `overview.md` (twelve more released rows drifted through `agents/warden.md#"## Role"`, re-read with `--reverify --into`; the refusal wording); and the paragraph `agents/warden.md` §Role gains, a cost every warden spawn pays.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | the section now ends at any heading, so a table row under a sub-heading of `## Removes` is read by the name half alone and a row naming a unit that still stands passes; at the base it read `STANDING`; required, a table under a sub-heading reads as an empty section | `skills/evidence-check/scripts/evidence_check.py:6053` | **fixed** `d93f700b` | fixed at d93f700b; probe at both SHAs (executed); the M1 amendment's stated cost names prose only |
| 🟡 2 | a line carrying the marker under `## Removes` is dropped by `claim_lines` before `removes_section` reads it: a marked bullet passes and a marked row naming a standing unit is never read, so "any other line in the section is `REFUSED`" and the four `unknown refused` words are false for that input | `skills/evidence-check/scripts/evidence_check.py:6051` | **fixed** `d93f700b` | fixed at d93f700b; probe at both SHAs (executed), same result, so older than the branch; the branch's registry sentence and template comment make the claim and teach the marker |
| ⬜ 3 | the off-shape refusal tells a wrapped `nothing` reason to move under a sub-heading "after the table" where there is no table, and nests the quoted line's backticks | `skills/evidence-check/scripts/evidence_check.py:6127` | answered | the refusal sentence it names is redesigned by the reframe this run ends in, so its wording is settled there rather than patched in a stopped run; read; behaviour right, the sentence reads badly |
| 🟢 | S1 to S3 and the M1 case hold: each of the 11 parametrised cases fails against the base reader and passes at the head, and S2's case passes at both by design | `tests/test_a_record_states_what_the_tree_has.py` | confirmed | the head's test module run against the base code: 11 failed, 1 passed; at the head 142 passed (executed) |
| 🟢 | S5 and S6: the stale sentences are gone and the registry names one reader | `docs/the-reader-registry.md:154` | confirmed | both `git grep` checks exit 1; `bin/fold-check --root .` exit 0 (executed) |
| 🟢 | S7: the records read clean | `seal/ledger/1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes.md` | confirmed | `bin/evidence-check --strict .` exit 0, 0 drifted, records arm 0 refused (executed) |
| 🟢 | the warden paragraph (P2 (a)) is placed, worded and costed soundly | `agents/warden.md:111` | confirmed | read; it is how 🟡 2 was found |
| ❓ | S8: the gate's four requirements in the pull request body | PR #915 body | ❓ out of verified scope | not read this round; the orchestrator answers it when the body is written, and 🟡 1 changes the direction statement's "a wrong allow" case |

## Paste-ready fixes

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
```
under a sub-heading after the table, where it is read as the rest of the
frame is; a table row under that sub-heading is `REFUSED` too, and the
marker exempts no line of the section. The names on the section's lines are
```
```python
                f"`{text}` — a line under `## Removes` is a table row or one "
                "`nothing — <why>` line, written on one line; prose about the "
                "rows goes under a sub-heading after the section, such as "
                "`### Why these rows`",
```

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

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
