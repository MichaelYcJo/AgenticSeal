# 1791382684-every-reader-and-record-is-inventoried — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 681fa7b1 |
| Ran by | smith on opus, as the run-level `handoff.md` §*Starting on a new machine* item 4 names the spawn |

## What this phase was asked

The mapping at the build's tree, by the six rules of `plan.md` §*Technical
context*, read with `reader_registry.population()`: the rowed, clean, stale,
conflicting and unparsed counts, and the Q1 sets (a) to (c) with their
re-read counts, each beside the frame's reading at 57e2bc13. The per-unit
listing stays out of this record except as counts and the names of the
hand-read units. No tree edit. The spawn added: Q1 is answered (c), the
units no ledger row cites; `hooks/worktree-guard.py` is phase 4's and is not
touched; a one-shot script is deleted after use and named here.

## What this phase found

**Every number below was read at 7608d82c**, the branch head before this
record. 7608d82c differs from 57e2bc13 only in this work item's own
`spec.md`, `plan.md`, `questions.md` and `handoff.md` (`git diff --stat
57e2bc13 7608d82c`), so a difference below is the rule's application, not
the tree. The probe was `test_tmp_inventory_map.py`, run once from the
scratchpad with the runner's `.venv` interpreter and deleted; its JSON output
fed phase 2's writer and was deleted with it. Before it ran,
`bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py`
passed, 76 cases.

| Count | Frame, at 57e2bc13 | Build, at 7608d82c |
|---|---|---|
| population units / census lines | 1,607 / 1,584 | 1,607 / 1,584 |
| reader rows in parts 1 to 6 | 1,467 | 1,467 (part 2's second table under `## Readers`, the payload table, has four columns and is not a reader row) |
| rows in `tests/test_*.py` / on `bin/` and workflows / naming no population unit | 760 / 10 / 23 | 760 / 10 / 23 |
| rows naming one unit / several | 508 / 166 | 508 / 166 |
| distinct units rowed | 912 | 912 |
| stale (hash moved since 5623d728) / of them declared by #835 | 123 / 3 | 123 / 3; `evidence_check.py` 22, `chain_check.py` 16, `round_record.py` 16, `commitgate.py` 8, `broad_gate.py` 8, `seal.py` 6, `worktree-guard.py` 5, `commit-review-gate.py` 4, the rest fewer |
| clean, one class, rows agree | 759 | 759 |
| rows disagree: two classes / two directions | 6 / 1 | 6 / 1 |
| `Class` cell starts with no class word | 23 | **0** |
| `Class` cell names two classes (`owned + observed`, `owned/observed`) | not counted | **4** |
| `Unknown` cell starts with no direction word (`—`, `n/a`) | not counted | **19** |

**The frame's 23 are a parse of `\|`, not cells that name no class.** Read
with the escape honoured, as GFM does and as `questions.md` Q4 says the line
takes the cell, every one of the 912 rowed units has a `Class` cell that
begins with `owned`, `observed` or `guess`. 91 reader rows hold an escaped
pipe, and the ones that name a population unit name units in exactly the
files Q3 lists (`hooks/config.py`, `hooks/routing.py`,
`hooks/review-history-guard.py`, `hooks/tokens.py`, `hooks/cmdline.py`,
`chain_check.py`, `round_record.py`, `correction_check.py`,
`evidence_check.py`, `arm_check.py`, `broad_gate.py`, `session_cost.py`,
`unverified_check.py`), and in `survivor_check.py`. A split on every `|`
moves their `Class` column. Q3's question is answered by the cells
themselves: each names its class in its first word.

**What the frame did not count, and what the hand-read set is instead.** A
unit is read by hand where its rows do not hand over one class word and one
direction word. That is 30 units, by a different composition from the
frame's 7 + 23:

- **Rows disagree (7):** `hooks/answers.py#given` (observed, guess; both
  refused), `hooks/ledger-migrate.py#main` (observed, owned; passed),
  `hooks/worktree-guard.py#lease_owner_alive` (observed mixed, guess passed),
  `skills/code-review/scripts/round_record.py#measure` (observed, guess;
  passed), `skills/implement/scripts/seal.py#import_` (observed, guess;
  refused), `skills/verify/scripts/arm_check.py#run_arms` (observed; refused,
  mixed), `skills/verify/scripts/unverified_check.py#check_text` (owned
  refused, guess mixed).
- **A `Class` cell naming two classes (4):**
  `skills/evidence-check/scripts/evidence_check.py#pact_change_item`
  (`owned + observed`), `skills/implement/scripts/seal.py#install_workflow`,
  `#plugin_workflow` and `#unsafe` (`owned/observed`).
- **An `Unknown` cell with no direction word (19):** the eleven
  `hooks/cmdline_base.py` units of part 1 row 49 (`_hands_a_string`,
  `reparsed_texts`, `_is_the_program`, `command_strings`,
  `names_an_unknown_command`, `_heredoc_end`, `_paren_end`,
  `substitution_bodies`, `heredoc_bodies`, `split_segments`, `compose`;
  `What it reads` is `—` too), `main` of `hooks/git/pre-commit.py`,
  `post-commit.py` and `reference-transaction.py` (part 2 rows 72 to 74),
  `evidence_check.py#content_hash` and `#normalise` (E11),
  `evidence_check.py#released_drift` (E49), and `fold_check.py#markers` and
  `#marker_digest` (F8).

Seven more cells carry one class word and a parenthesis (`observed (GFM
rule)`, `owned (subset of GFM)`, `owned (delegated)`); they name one class
and are read as that class.

**The Q1 sets, by the same rules.** The frame's columns are its own: (a) is
its 759 clean units. The build's (a) is every unit the rules decide — the 759,
the 7 disagreeing and the 4 two-class units, each taking the weakest — and
leaves the 19 with no direction word out, because the line's last word is the
direction and no row grounds one.

| Set | Frame, at 57e2bc13: units / `Re-read ·` rows owed (anchors) / live rows (anchors) | Build, at 7608d82c |
|---|---|---|
| (a) all decided units | 759 / 687 (1,093) / 24 (35) | 770 / 700 (1,127) / 23 (36) |
| (b) the `guess` units | 275 / 247 (388) / 14 (15) | 281 / 261 (411) / 13 (16) |
| (c) no released row cites the unit | 245 / 0 / 1 | 241 / 0 / 1; 93 `guess` |

The one live row under (c) cites `hooks/worktree-guard.py#_first_finding_in`
(`seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md`,
its S25 row), so it is phase 4's, and phases 2 and 3
owe no live re-stamp.

**The frame does not hold for `hooks/cmdline_base.py`.** That file is pinned
byte for byte below its rider to `86256492:hooks/cmdline.py`
(`tests/test_the_frozen_reading_never_grows.py#test_the_bytes_below_the_rider_are_86256492s`,
read): a docstring line on any unit in it fails that case. 29 of its units
are decided, and 27 of them are in (c). They stay on the census, and their
census lines stay with them; the only way to declare them is to delete that
case first, which is the frozen reading's own rule and not this build's to
take.

**So phase 2 writes 189 units in 44 files**: (c)'s 241, less the 25 in
`hooks/worktree-guard.py` (phase 4) and the 27 in `hooks/cmdline_base.py`.
By class, observed 76, owned 61, guess 52; by direction, passed 105, refused
64, mixed 20.
