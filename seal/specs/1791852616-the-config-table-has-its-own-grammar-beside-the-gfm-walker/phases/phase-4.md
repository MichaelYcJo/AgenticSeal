# 1791852616-the-config-table-has-its-own-grammar-beside-the-gfm-walker — phase 4

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 0db85117 |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

The record: `changelog.md` naming what an installed config sees change,
shape by shape with its edit; `overview.md`; the ledger fragment with rows
for the new units and `evidence-check --reverify --into
seal/ledger/1791852616-….md --checked <date>` for every released row the
stop rule's removal moves — a `Corrected ·` row where the claim no longer
holds and a `Re-read ·` row where it does (`questions.md` Q4 lists the
candidates); `tests/undeclared_readers.txt` with every touched unit gone;
`tests/test_a_record_states_what_the_tree_has.py` green over this
directory. Verified by `evidence-check --strict .`, `correction-check
--range`, the records case. Mid-phase the coordinator added the owner's
rule: a shipped document rewrites what it states in place and does not
narrate the change.

## What this phase found

**Q4: sixteen corrections, the rest re-reads.** `evidence-check --strict .`
at d427badd named 58 coordinates drifted or broken across 83 released rows
citing them directly, and the Broad-gate section of `templates/config.md`
carried about forty more by its heading. Every row's claim was read. Sixteen
were the stop rule's, or named a unit it took with it, and each took a
`Corrected ·` row with the claim as it now holds: 0.12.0's escaped-pipe,
writer, sealer and mode-gate rows; 0.12.1's R1, R2, R3, R5, R6; 0.16.0's
P3-1 and R1-1; 0.21.0's K1, K6, K7, K8; and 0.5.0's 🟡 6 / 🟡 5. Every
other claim held — the Broad-gate rows are about the criterion, `cmd.exe`,
`&` and the preflight, none about the pipe's cost but 0.12.0's *three
documents*, which still holds of the rewritten documents — and
`--reverify --into` wrote their `Re-read ·` rows. The frame's Q4 list named
0.9.1's Q1, 0.12.1's R5, 0.15.3's F5 and F6, 0.16.0's P2-2, 0.18.2's O1 and
0.21.0's K10 as candidates: R5 is corrected; F6 cites no coordinate this
work moved and drifted nowhere; F5 is already superseded by 0.21.0's
`Corrected · F5`, whose family was re-read; the rest held and were re-read.

**A third document of S8's class.** Reading 0.12.0's row on *the three
documents that promised the old behaviour* found the bootstrap warning in
`skills/implement/orchestration.md` still saying a bare pipe parses as no
row; it is rewritten and its pin in `tests/test_first_setup_asks_once.py`
re-pinned (red against the old wording, green after).

**The frame named a unit that never stood.** `spec.md`, `plan.md` and
`questions.md` cited the mode gate's unit by a name that was never in
`hooks/mode-gate.py`, not at 3bb2ea42 either: `unanswered_root` · NAME NOT IN TREE
The unit at `hooks/mode-gate.py:128` is `undeclared`. The records arm named
the frame's spelling `NOT-IN-TREE`; it is corrected in place.

**The owner's rule on shipped documents** took the `(#871)` references out
of `templates/config.md`, `skills/config/SKILL.md` and
`skills/implement/orchestration.md`, and the `(#430)` beside the pipe row's
last sentence, so each states the rule and not its history.

Verified at 0db85117's tree:

- `bin/evidence-check --strict .`: exit 0 (the last run before the
  overview's one-line wording fix; the fix touches no coordinate);
- `bin/correction-check --range 321e9de1...HEAD`: exit 0 — no merge, and
  no released ledger file changed;
- `bin/test tests/test_a_record_states_what_the_tree_has.py -q`: exit 0,
  130 passed;
- `bin/unverified-check --baseline 321e9de1 seal/specs/`: exit 0, after the
  closing memo stopped writing an HTML comment opener literally in a table
  cell, which the check read as a one-cell row.
