# Survivors — a unit the extractor cannot bound is refused

`survivor-check --range origin/release/v0.21.0...HEAD` names each place that
still carries wording this item's range removed. Each row below was read at
the branch's head, and its grounds say why the standing text stays.

| Path | Quote | Grounds |
|---|---|---|
| `seal/ledger/1791384156-config-rows-coordinates-and-headings-have-one-reader.md` | `seal/releases/0.16.0.md#"### 1790635414-follow-up-names-are-checked-and-a-re-read-is-dated">"H1 · every split"@098baf93` | #867's `Re-read · H1` row, a reading dated 2026-10-08 at the hashes it held then. The family is superseded by this item's `Corrected · H1` row in `seal/ledger/1791384159-a-unit-the-extractor-cannot-bound-is-refused.md` (2026-10-12), whose coordinates `--strict` reads OK; re-stamping an older reading would rewrite what #867 recorded |

The redesign (phases 5–8) deletes shipped sections — the bracket walk, its
lexer, the block rule, the declaration rule and their cases and documents —
so it takes one row for the range. Read 2026-10-12 at the head of phase 8,
the sweep named 38 places beside the H1 row above: 36 of the kinds the row
below lists, and two that were not (a test docstring and #867's rider row, both
still naming a resurrection), which were corrected instead.

| Range | Grounds |
|---|---|
| `origin/release/v0.21.0...HEAD` | the places left are (1) fixture strings in test modules — `def handler(x)` bodies, two-definition fixtures, a C# overload — that share tokens with fixtures this range deleted and are code, not claims; (2) released ledger rows frozen by `Ledger frozen from`, each superseded by a `Corrected ·` row that states what holds now: `0.4.0.md` lines 20, 51, 58, 66 and 67, each by this item's own `Corrected ·` row citing it; `0.4.0.md` line 59 and `0.19.0.md` line 202, by this item's `Corrected ·` row citing 0.19.0's `"never writes onto"`; `0.9.1.md` line 172, by #867's `Corrected · S1`, corrected in place in phase 8 (round 2's 🟡 3 found lines 20 and 66 excused here with no such row); (3) other work items' records (1791240748's `spec.md`, 1791163980's `spec.md` and `post-review-check-2.md`), records of their own time; (4) true sentences about constants and rounds in `evidence_check.py#py_spans`, `tests/test_a_row_points_by_content.py`'s constant case and `skills/verify/scripts/broad_gate.py`; (5) `.test_durations`, whose entries for the deleted cases drop no case from the shards and leave with the next refresh |
