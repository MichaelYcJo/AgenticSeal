# 1791382684-every-reader-and-record-is-inventoried — overview

## Why this work exists

The inventory found that the readers which kept being reopened were the ones
guessing at text they did not control; the build moves the inventory's class
for each unit it still describes into that unit's docstring, so
`grep -rn "Reads: guess"` lists them and the census of undeclared units
shrinks.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| `hooks/cmdline_base.py` | `spec.md` §*Which units, measured* counts its units in the backfill set; 27 of them are in Q1's (c). The file's bytes below its rider are pinned to `86256492:hooks/cmdline.py`, and a docstring line fails `tests/test_the_frozen_reading_never_grows.py#test_the_bytes_below_the_rider_are_86256492s` | the code: no line, the census lines stay | the frozen reading's own docstring: "a change has to delete a case here first", which is not this build's to take |
| the 23 units whose `Class` cell "starts with no class word" | `spec.md` and Q3 count 23 and ask the work to read each cell. Read with `\|` unescaped, every one starts with a class word | the cells: each takes its first class word | the frame's count was a split on every pipe (`phases/phase-1.md`) |
| units whose `Unknown` cell names no direction (`—`, `n/a`) | spec silent: the frame took the direction to be the cell's first word and did not count the cells where that word is none. 19 units; 3 of them are in (c) outside the pinned file, the `main`s of the three git hooks | no line; they stay on the census | the line's last word is the direction, and no row grounds one (`phases/phase-2.md`) |
| a `Class` cell naming two classes (`owned + observed`, `owned/observed`) | spec counts disagreement between rows, not inside one cell; 4 units | the weaker, `observed`, by the registry's rule for a unit reading several inputs; one of them, `seal.py#plugin_workflow`, is in (c) | `docs/the-reader-registry.md` §*The four classes and the line that declares one*: "A unit reading several inputs declares the weakest" |
| `inventory/` gained a marker on 10 lines | `spec.md` §*The inventory's fate*: "Nothing in the build moves or edits it." The ledger fragment makes the item live, and `evidence-check`'s records arm then refused 14 names the inventory read at 5623d728 and siblings have since removed, exit 2 | each line ends `· NAME NOT IN TREE`; no cell's reading changes | the finding's own remedy, and the plan's phase 3 is verified by `evidence-check` exit 0 (`phases/phase-3.md`) |
| `# RIDER:` stamps | the frame counted the ledger's rows as what a docstring line drifts; three rider stamps carry the same unit hash | each read beside its unit's diff and re-stamped by `rider_check.py --reverify --only` | the rider still says what the unchanged code does (`phases/phase-2.md`) |
| `Reads:` prose of 32 units named beside a reader in one row | `spec.md` acceptance row 4: the line carries the row's `What it reads` | each line says what its own unit reads; the class and direction kept except `short_commit`'s direction, now `passed` | `docs/the-reader-registry.md` §*The four classes and the line that declares one*: the prose between the two words is what the unit reads, and a false one is §*What neither check can read* limit 1; round 1 🟡 1 |
| a marker file this plugin wrote, asked whether it exists | four units declared it two ways, two `owned` and two `observed` | `observed` for all four | the registry's `owned` is "a format this repository's own writer produces, or a vocabulary its own checker defines", and a presence test reads no format; `observed` is "a fact asked of the system", and K1 lists existence tests with the process boundary; round 1 ⬜ 4 |
| five cells holding a backslash | Q4: the cell as written, `\|` unescaped | each line says in words what the regular expression matches | a docstring without an `r` prefix reads the backslash as an escape; the five are named in `phases/phase-2.md` |

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, lint and typecheck over the build's tree | the sealer, after the review rounds settle |
| that each of the 189 `Reads:` lines says what its unit reads today: each is the inventory's reading of 2026-10-07 carried over for a unit whose hash has not moved since, and was not read against the code again | the warden, reading the diff's `Reads:` lines |
| phase 4, `hooks/worktree-guard.py`'s units | phase 4, after #894 and #896 land |

## Not done

The 529 decided units (`phases/phase-1.md`; the frame read 514) a released ledger row cites wait, by Q1's answer (c),
for the ledger rework or a later answer; `plan.md` §*Technical context*
holds the mapping rules that rerun then. The 123 stale units declare when
next touched.

## Fed back into the spec

none
