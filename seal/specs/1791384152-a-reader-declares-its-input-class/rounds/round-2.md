# 1791384152-a-reader-declares-its-input-class — review round 2

| Field | Value |
|---|---|
| Target SHA | 9159ae931405bd49782295dab44795b1f882e238 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | 895 |
| Broad gate | not yet |
| Fixes checked by | round-3 |
| Fix range | `6b108d367c7e27dccbce4002ce2976627840faa2..6c5d4529ad4eaec39ebd14f870370d0151796cbe`, 2 commits |
| Contract changes | none |
| New units | test_a_removal_is_read_in_this_tree_never_in_another_checkout (depth 1); test_a_path_through_dot_dot_is_refused_never_read_as_gone (depth 1) |
| Fix of a fix | first — 🟡 1 at skills/evidence-check/scripts/evidence_check.py#removal_findings, a unit round-1's fixes changed |
| Needs a fix | yes — 🟡 1 (a `## Removes` row is read through `--default-repo` and `--map`, so a removal that happened reads `STANDING` and a row in an absent checkout reads as gone) |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 2 of #835 (PR #895), target 9159ae93. It verifies round 1's fixes at 8f3d912e..f21f151f (`rounds/round-1-fixes.md`). Attack in this order:

1. **🟡 1's fix (e6843d9a, 88b5a690).** A method now matches by its attribute name on every receiver, module receivers included. Does K1 now over-select? K1 is a contradiction list: a unit declaring `nothing` that calls `.walk` on `ast` is refused. Count which declarations flipped from `nothing` to `observed` because of this, `tests/reader_registry.py#bindings` being one, and check each one is truly a reader. Then check the new K1 count, 632 at 2fc65bea, in `docs/the-reader-registry.md` and `overview.md`.
2. **🟡 2's fix (20c4e993).** A Removes path that escapes the root, or exists and will not read, is `REFUSED`. Only a truly absent file reads as removed. Check a symlink, a path with `..` that stays inside the root, and a path in a declared external repository through `place()`. The mutation that removed the escape refusal went red through a crash on joining a `None` repository, not through an assertion. Is the case asserting the refusal, or only that something raised?
3. **🟡 3's fix (978aa43a).** Re-read K7's corrected claim, the `cutoff_row@dc04c433` anchors on K7, C1 and 1791384159's Corrected row, and the changelog's upgrade note. The smith found no released row carrying K7's false sentence. Verify that by grep.
4. **⬜ 4's fix and the two answered notes (⬜ 5, ⬜ 6).** Judge whether each answer's grounds stand.
5. **Depth:** the one new unit, `test_a_coordinate_that_does_not_read_is_refused_never_read_as_gone`, is depth 1. Any finding inside it is a fix-of-a-fix.

Facts arriving as coordinates, executed by the orchestrator: `round_record.py close` exit 0 at 9159ae93. Everything else in the smith's fix report is the smith's, unverified.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | a `## Removes` row is placed through `--default-repo` and `--map`: a removal from this tree reads `STANDING` when the original holds the path, and a mapped row whose checkout is absent reads as gone | `skills/evidence-check/scripts/evidence_check.py:6131` | **fixed** `5dfefd3b` | fixed at 5dfefd3b; executed through `check_records`: `STANDING` for the default-repo row, no finding for the mapped row; spec S1/S2 read at HEAD |
| ⬜ 2 | a `..` through a missing directory, or through a file, reads as gone while the file it names holds the unit | `skills/evidence-check/scripts/evidence_check.py:6142` | **fixed** `5dfefd3b` | fixed at 5dfefd3b; executed: two rows, no finding, `kept.py` defining the unit; `contained` resolves by `realpath`, the read by the kernel |
| ⬜ 3 | the R7 row says `ast.walk` is no primitive and cites a mutation of the receiver set the fix removed | `seal/ledger/1791384152-a-reader-declares-its-input-class.md:25` | answered | corrected at 6c5d4529; read against `tests/reader_registry.py:198` and the moved test row; a correction under `seal/ledger/` |
| ⬜ 4 | the document's and the changelog's lists of `## Removes` refusals stop at three, and the `Enforced by:` line does not name the new case | `docs/the-reader-registry.md:119` | **fixed** `6c5d4529` | fixed at 6c5d4529; read; the general clause stays true |
| ⬜ 5 | the upgrade note says `--reverify` already stopped on a doubled `Removes from` | `seal/specs/1791384152-a-reader-declares-its-input-class/changelog.md:46` | answered | corrected at 6c5d4529; read: `--reverify` returns before `check_records`; a correction under `seal/specs/` |
| ⬜ 6 | a test docstring calls its last two rows round 1's, and those are `ast.walk` and `pathlib` | `tests/test_a_reader_declares_its_input_class.py:493` | **fixed** `6c5d4529` | fixed at 6c5d4529; read |
| 🟢 | round 1's first finding is closed — K1 judges a module's method by its name, `os.open` and `re.split` are refused, one declaration moved and it is true | `tests/reader_registry.py:198` | confirmed | executed: three readings over every unit at both trees; module test 76 passed |
| 🟢 | round 1's second finding is closed — an escaping path, a symlink out, a directory and a dangling link are `REFUSED`, and the case pins each text | `skills/evidence-check/scripts/evidence_check.py:6132` | confirmed | executed: planted probes; three `mutation-check` runs red through the case's assertion |
| 🟢 | round 1's third finding is closed — K7's note, the three `cutoff_row` anchors and the changelog's note | `seal/ledger/1791384156-config-rows-coordinates-and-headings-have-one-reader.md:24` | confirmed | executed: hashes recomputed at the target; read: no released row carries the sentence |
| 🟢 | round 1's fourth note is closed — the item's `## Removes` names both pins | `seal/specs/1791384152-a-reader-declares-its-input-class/spec.md:513` | confirmed | read: neither test is in the tree, so both rows read as gone |
| 🟢 | round 1's fifth note's answer stands | `skills/code-review/scripts/survivor_check.py:142` | confirmed | read: the predicate excludes `phases/` whatever a record holds |
| 🟢 | round 1's sixth note's answer stands | `tests/reader_registry.py:461` | confirmed | read: the writer runs only where no census exists, and the bad line is refused loudly |

## Paste-ready fixes

```python
# skills/evidence-check/scripts/evidence_check.py — removal_findings, in place
# of `repo, rel = place(root, maps, default_repo, raw_path)`. A frame names
# what its work removes from THIS tree, so a row is never read in the
# original, and a row carrying a --map prefix names another checkout.
        if any(raw_path == name or raw_path.startswith(name + "/") for name in maps):
            findings.append(
                (
                    REFUSED_STATUS,
                    where,
                    f"`{cell}` — the path names another checkout through "
                    "`--map`, and a frame names what its work removes from "
                    "this tree — write the path in this tree",
                )
            )
            continue
        repo, rel = place(root, {}, None, raw_path)
```
```python
# tests/test_a_record_states_what_the_tree_has.py
def test_a_removal_is_read_in_this_tree_never_in_another_checkout(tmp_path):
    """S1/S2, round 2 of #835. A row is a claim about HEAD: one the original
    still holds is a removal that happened here, and one in a mapped checkout
    is refused rather than read as gone."""
    root = tmp_path / "r"
    tree(root, **{"kept.py": "def k():\n    return 1\n"})
    orig = tmp_path / "orig"
    tree(orig, **{"old.py": "def k():\n    return 1\n"})
    h = home(root)
    rows = "| x | `old.py#k` | y |\n| x | `legacy/a.py#k` | y |\n"
    work_item(h, "1780000000-live", **{"spec.md": REMOVES_HEAD + rows + REMOVES_TAIL})
    found, _read, _stamps = module().check_records(
        str(root), str(root / "seal"), {"legacy": str(tmp_path / "absent")}, str(orig)
    )
    assert [(s, d) for s, _c, d in found] == [
        (
            "REFUSED",
            "`legacy/a.py#k` — the path names another checkout through `--map`, "
            "and a frame names what its work removes from this tree — write the "
            "path in this tree",
        )
    ]
```

## Executed probes

| What was run | Result |
|---|---|
| K1 three ways — the target's rule, the build's receiver rule with the base table, the framed reading — over every unit at `9159ae93` and at `2fc65bea` | executed: 641 / 627 / 630 at the target; 632 / 620 / 621 at `2fc65bea`; 14 units newly selected at the target, 12 on the census, plus `bindings` and `k1_calls`; no `nothing` unit beside a K1 call |
| planted `## Removes` rows through `check_records`: symlink out, symlink in, dangling symlink, `..` three ways, `--map` to an absent and to a present checkout, `--default-repo` | executed: `REFUSED`, `STANDING`, `REFUSED`; `pkg/../` `STANDING` and the other two no finding; no finding and `STANDING`; `STANDING` |
| `bin/mutation-check` on `removal_findings`: the quiet skip put back, the unreadable refusal gated off, the unreadable refusal widened | executed: all three red through the case's `AssertionError`, file restored |
| `unit_hash` of `cutoff_row`, `frozen_from`, `config_rule`, and the D1 heading's hash | executed: dc04c433, 060d5968, 57d7f81f, 18207f51, each matching its row |
| `bin/test tests/test_a_reader_declares_its_input_class.py` | executed: 76 passed, exit 0 |
| `bin/test tests/test_a_record_states_what_the_tree_has.py`, narrowed with `-k` to the `## Removes`, cutoff and coordinate cases | executed: 35 passed, exit 0 |
| `round_record.py close` at `9159ae93` | not run in this round; the orchestrator's executed fact, exit 0 |
| the broad gate (full suite, lint, typecheck) | not yet; the sealer's, after the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `tests/reader_registry.py:209` | round 1's 🟡 1 — fixed |
| round-1 | `skills/evidence-check/scripts/evidence_check.py:6130` | round 1's 🟡 2 — fixed |
| round-1 | `seal/ledger/1791384156-config-rows-coordinates-and-headings-have-one-reader.md:24` | round 1's 🟡 3 — fixed |
| round-1 | `seal/specs/1791384152-a-reader-declares-its-input-class/spec.md:508` | round 1's ⬜ 4 — fixed |
| round-1 | `skills/code-review/scripts/survivor_check.py:142` | round 1's ⬜ 5 — answered |
| round-1 | `tests/reader_registry.py:461` | round 1's ⬜ 6 — answered |
| round-1 | `tests/undeclared_readers.txt` | round 1's 🟢 — confirmed |
| round-1 | `tests/reader_registry.py:403` | round 1's 🟢 — confirmed |
| round-1 | `skills/evidence-check/scripts/evidence_check.py:6032` | round 1's 🟢 — confirmed |
| round-1 | `agents/smith.md:181` | round 1's 🟢 — confirmed |
| round-1 | `seal/specs/1791384152-a-reader-declares-its-input-class/overview.md:26` | round 1's 🟢 — confirmed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

nothing to drain
