# 1791384152-a-reader-declares-its-input-class — review round 3

| Field | Value |
|---|---|
| Target SHA | 1bbed1a123a09106b9ec365bb5667ca23431f8d4 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | 895 |
| Broad gate | 63580c62 against c38f97d7; earlier run: 10a0d2ba against c38f97d7 |
| Fixes checked by | no fixes to check |
| Fix range | `93898214653d7038bcdbbb3692290b2ae7247389..dcde8e56909abbd7f7a3102b98b706cdec273c84`, 4 commits |
| Contract changes | removal_findings → file_claims |
| New units | test_a_path_spelled_another_way_is_read_as_the_file_it_names (depth 1) |
| Fix of a fix | no |
| Needs a fix | no |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 3 of #835 (PR #895), target 1bbed1a1, verifying round 2's fixes at 6b108d36..6c5d4529 (`rounds/round-2-fixes.md`). Attack in this order:

1. **🟡 1's fix (5dfefd3b):** `removal_findings` calls `place(root, {}, None, raw_path)`, and a `--map`-prefixed row is `REFUSED`. Check how a `--map` prefix is recognised. Is it matched against the declared maps, or guessed from the path's shape? Check that an ordinary in-tree row whose first segment happens to equal a map's name is not refused.
2. **⬜ 2's fix:** any path with a `..` segment is `REFUSED`. Confirm the wording and the escape refusal's order, and that round 1's pinned text is unchanged.
3. **The record corrections (6c5d4529):** R7's corrected claim and grounds, the changelog's rewritten `--reverify` sentence (check `--reverify`'s actual return path), and the refusal list in `docs/the-reader-registry.md` with its `Enforced by:` names.
4. **Depth:** the two new units, `test_a_removal_is_read_in_this_tree_never_in_another_checkout` and `test_a_path_through_dot_dot_is_refused_never_read_as_gone`, are depth 1. A finding inside either one is a fix-of-a-fix.

Facts arriving as coordinates, executed by the orchestrator: `round_record.py close` for round 2 exit 0 at 1bbed1a1. Everything else in the smith's report is the smith's, unverified.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| ⬜ 1 | an in-tree row whose first segment equals a `--map` name is refused, and the remedy says to write the path in this tree, which it already is; `./` reads it in this tree and is written nowhere | `skills/evidence-check/scripts/evidence_check.py:6134` | answered | corrected at cbab19d1 — the `--map` refusal and `docs/the-reader-registry.md` name the `./<path>` spelling that reads the row in this tree; executed through `check_records`: `REFUSED` with the map absent and present; `./legacy/a.py#k` `STANDING`; the test is `place`'s own |
| ⬜ 2 | a trailing `/` (`kept.py/#k`, `kept.py/.#k`) reads as gone while the file holds the unit; round 2's ⬜ 2 by another spelling | `skills/evidence-check/scripts/evidence_check.py:6173` | answered | corrected at a5c543d0 — the row's path is normalised before it is read and resolved, so `kept.py/#k` and `kept.py/.#k` read `STANDING`; a case pins both and the `./` route; executed: no finding for both rows; `contained` judges by `realpath`, the read and `lexists` by the kernel |
| ⬜ 3 | the document's `Enforced by:` line does not name the `..` case, and line 123 runs past the wrap | `docs/the-reader-registry.md:130` | answered | corrected at 3eafec0c — the `Enforced by:` line names `test_a_path_through_dot_dot_is_refused_never_read_as_gone`; line 123's re-wrap rode cbab19d1; read; `fold-check` exit 0 |
| ⬜ 4 | `removal_findings` keeps a `default_repo` parameter nothing reads | `skills/evidence-check/scripts/evidence_check.py:6066` | answered | corrected at dcde8e56 — `removal_findings` takes no `default_repo`, and `file_claims` hands it none; read: the name occurs only in the signature |
| 🟢 | round 2's first finding is closed — a removal is read in this tree only: the original never answers, and a `--map` prefix is refused | `skills/evidence-check/scripts/evidence_check.py:6148` | confirmed | executed: `old.py#k` no finding with the original holding it, `STANDING` with this tree holding it, the mapped row `REFUSED`; two mutations red through the case's assertion |
| 🟢 | round 2's second note is closed — a path through `..` is refused, after the escape refusal | `skills/evidence-check/scripts/evidence_check.py:6159` | confirmed | executed: `missing/../` and `pkg/../` refused, `../outside.py` keeps the escape text; one mutation red; read: round 1's case pins the order |
| 🟢 | round 2's third note is closed — R7 says what K1 does since round 1 | `seal/ledger/1791384152-a-reader-declares-its-input-class.md:25` | confirmed | executed: the three cited mutations red, 81 rows OK |
| 🟢 | round 2's fourth note is closed — the document and the changelog list every refusal | `docs/the-reader-registry.md:119` | confirmed | read; the `Enforced by:` gap is ⬜ 3 |
| 🟢 | round 2's fifth note is closed — the changelog's `--reverify` sentence is true | `seal/specs/1791384152-a-reader-declares-its-input-class/changelog.md:46` | confirmed | read: `--reverify` calls `frozen_from` alone and returns before `check_records`, the only caller of `cutoff_row` for `Removes from` |
| 🟢 | round 2's sixth note is closed — the docstring says which rows are round 1's | `tests/test_a_reader_declares_its_input_class.py:492` | confirmed | read: `os.open` and `re.split` are `K1_FUNCTIONS` rows round 1 added |
| 🟢 | round 1's second finding stays closed under round 2's fixes — the escape and unreadable refusals keep their texts | `skills/evidence-check/scripts/evidence_check.py:6149` | confirmed | executed: round 1's case passes at the target; the test module's diff only adds lines |

## Paste-ready fixes

```python
# skills/evidence-check/scripts/evidence_check.py — removal_findings, the
# --map refusal's text; the pinned text in
# test_a_removal_is_read_in_this_tree_never_in_another_checkout moves with it.
                    f"`{cell}` — the path names another checkout through "
                    "`--map`, and a frame names what its work removes from "
                    "this tree — write the path in this tree, as "
                    f"`./{raw_path}` where this tree's own directory carries "
                    "the map's name",
```
```python
# skills/evidence-check/scripts/evidence_check.py — removal_findings, in place
# of `full = os.path.join(repo, rel)`. Open the path `contained` judged, so a
# trailing `/` or `/.` cannot read as gone; `..` is refused above, so the
# lexical normalisation never crosses a symlink.
        full = os.path.join(repo, os.path.normpath(rel))
```

## Executed probes

| What was run | Result |
|---|---|
| a probe module in the round directory (deleted), planting `## Removes` rows through `check_records`: in-tree `legacy/a.py` under `--map legacy` with the checkout absent and present, `./legacy/a.py` both ways, `legacy/../kept.py`, `legacyx/a.py`, `old.py` with `--default-repo` two ways, `./kept.py`, `.//kept.py`, `kept.py/`, `kept.py/.`, `../outside.py`, `pkg/../kept.py`, `gone/x.py`, `a/./kept.py` | executed: `REFUSED`, `REFUSED`; `STANDING`, no finding; map `REFUSED`; `STANDING`; no finding, `STANDING`; `STANDING`, `STANDING`; no finding, no finding; escape `REFUSED`; `..` `REFUSED`; no finding; no finding |
| `bin/mutation-check` on `removal_findings`: the `--map` refusal off, `place` handed `maps` and `default_repo` again, the `..` refusal off | executed: all three red through the new cases' `AssertionError`, file restored |
| `bin/mutation-check` on `tests/reader_registry.py#k1_call` and its table: the name fallback narrowed to `target is None`, the `os.open` row removed, the `re.split` row removed | executed: all three red, each failing the parametrised row it names, file restored |
| `bin/test tests/test_a_record_states_what_the_tree_has.py`, narrowed with `-k` to the removal, `..`, unreadable, `Removes`, standing and cutoff cases | executed: 17 passed, exit 0 |
| `bin/evidence-check` narrowed with `--ledger` to this item's fragment | executed: 81 ok, 0 drifted, 0 broken; records arm 0 refused; exit 0 |
| `bin/fold-check --root` | executed: 185 statements in 19 documents, 0 over 1000 lines, exit 0 |
| `round_record.py close` at `1bbed1a1` | not run in this round; the orchestrator's executed fact, exit 0 |
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
| round-2 | `skills/evidence-check/scripts/evidence_check.py:6131` | round 2's 🟡 1 — fixed |
| round-2 | `skills/evidence-check/scripts/evidence_check.py:6142` | round 2's ⬜ 2 — fixed |
| round-2 | `seal/ledger/1791384152-a-reader-declares-its-input-class.md:25` | round 2's ⬜ 3 — answered |
| round-2 | `docs/the-reader-registry.md:119` | round 2's ⬜ 4 — fixed |
| round-2 | `seal/specs/1791384152-a-reader-declares-its-input-class/changelog.md:46` | round 2's ⬜ 5 — answered |
| round-2 | `tests/test_a_reader_declares_its_input_class.py:493` | round 2's ⬜ 6 — fixed |
| round-2 | `tests/reader_registry.py:198` | round 2's 🟢 — confirmed |
| round-2 | `skills/evidence-check/scripts/evidence_check.py:6132` | round 2's 🟢 — confirmed |
| round-2 | `seal/specs/1791384152-a-reader-declares-its-input-class/spec.md:513` | round 2's 🟢 — confirmed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

nothing to drain
