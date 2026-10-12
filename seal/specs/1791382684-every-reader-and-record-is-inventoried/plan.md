# Implementation Plan: every reader and record is inventoried (#834) — the backfill

<!-- seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-12 by the repository owner, when `smith` was spawned.

`questions.md` Q1 was answered (c) by the owner with that approval.

## Summary

The inventory read 912 units of the population at 5623d728 and gave each a
class. The build moves those classes into the code as `Reads:` lines and takes
the units off the census, for the units whose row still describes the code
and whose line the ledger lets this release afford. The frame measured both
conditions at 57e2bc13 (`spec.md` §*The build*): 759 units are clean, and
writing all 759 owes 687 `Re-read ·` rows under the freeze, so the default is
the 245 units no ledger row cites — zero re-reads — and the rest wait for the
owner's answer to Q1 or for 0.22.0's ledger rework. The build changes no
reader's body, adds no mechanism, and leaves the inventory where it is.

## Technical context

**The grammar and the check** are landed: `docs/the-reader-registry.md`
§*The four classes and the line that declares one*,
`tests/reader_registry.py` (`declarations`, `population`, `census_lines`,
`CENSUS_LINE`) and `tests/test_a_reader_declares_its_input_class.py`
(`test_every_unit_of_shipped_python_declares_or_is_on_the_census`,
`test_a_census_line_naming_no_undeclared_unit_is_refused`). A unit that gains
a line and keeps its census line is refused by the second; a census line
whose unit is gone is refused the same way. The census only shrinks:
`write_census` refuses to run where the file exists, so every line leaves by
an edit.

**The mapping, stated so phase 1 reproduces it.** The inventory's reader
rows are the table under `## Readers` in `inventory/1-…` to `6-…`, columns
`# | File | Unit | What it reads | Decides | Class | Unknown | Duplicates |
Note`.

- `File` → path. Part 1 uses the short names its head states (`cl` =
  `hooks/cmdline.py`, `cb` = `hooks/cmdline_base.py`, `tk` = `hooks/tokens.py`,
  `oh` = `hooks/one_heredoc.py`, `gt` = `hooks/gate.py`, `cg` =
  `hooks/commitgate.py`, `crg` = `hooks/commit-review-gate.py`, `wg` =
  `hooks/worktree-guard.py`, `wc` = `hooks/worktree_consent.py`, `dp` =
  `hooks/dispatch.py`). Part 2 names the file under `hooks/`, `git/…`
  included. Part 3: `CC` = `skills/code-review/scripts/chain_check.py`, `RR`
  = `round_record.py`, `SC` = `survivor_check.py` beside it. Part 4 names the
  file; the six live under `skills/evidence-check/scripts/`,
  `skills/settle/scripts/` and `skills/implement/scripts/`. Part 5: `bg` =
  `skills/verify/scripts/broad_gate.py`, a bare `.py` name is under
  `skills/verify/scripts/`, `pytest_record` is
  `skills/verify/scripts/pytest_record/specseal_pytest_record.py`, and a
  `bin/` or `.yml` row is out. Part 6 names the path; only a file outside
  `tests/test_*.py` is in.
- `Unit` → units. Every backticked name in the cell, its head before any
  `.`, matched against the names `reader_registry.population()` gives for
  that file. A name that is no top-level unit (a constant, a nested function,
  a method) matches nothing. **Corrected after rounds 1 and 2 (🟡 1, ⬜ 6;
  ⬜ 4):** a unit takes the row's `What it reads` as its prose only where its
  own body, or a unit of the same file its body calls, makes every read that
  cell names: the K1 call, the `open`, the `git` or `gh` command, the AST
  walk. Being named first in the cell does not make a unit that one, and
  where no one unit makes all the reads, none does. Every other unit the row
  names is read on its own body: its prose says what that body reads, its
  class is the class of that, and its direction is what that body does with
  an input it does not understand — `refused` where it raises or stops,
  `passed` where it hands back a default for its caller to judge, `mixed`
  where it does both. A unit that cannot be read that way stays on the
  census. A test of whether a file this plugin writes exists is `observed`,
  whatever the row's `Class` cell says (round 1 ⬜ 4): part 1 row 114, the
  guard's `already_asked`, says `owned`, and its body is `os.path.exists` on
  its marker. Phase 2 gave every named unit the row's prose; rounds 1 and 2
  found 46 lines describing another unit, and the round-2 fix pass read every
  unit three enumerations selected (`rounds/round-2-fixes.md`). Phase 4 and any
  later rerun apply this rule instead.
- Stale or not. `reader_registry.unit_hash` over the file at HEAD against the
  same over `git show 5623d728:<path>`; a unit the base lacks is stale too.
- Class and direction. The first word of the `Class` cell in `owned`,
  `observed`, `guess`; the first word of the `Unknown` cell in `refused`,
  `passed`, `mixed`. A unit several rows name takes the weakest of what they
  say (`guess`; `mixed`), by `docs/the-reader-registry.md`'s rule for a unit
  reading several inputs.
- Drift. A whole-unit anchor `` `<path>#<unit>@<hash>` `` in a `|` row of
  `seal/ledger.md` or `seal/releases/*.md` is a released citation, in
  `seal/ledger/*.md` a live one; a `Class.method` anchor and a `>` anchor are
  not moved by a docstring line on the unit.

**The counts the frame read at 57e2bc13** are in `spec.md` §*Which units,
measured* and §*What a line costs*. Phase 1 reads them again at the build's
tree: #894 and #896 land on `hooks/worktree-guard.py` between the two trees,
so that file's stale set grows and its clean set shrinks.

**How the lines are written.** 245 to 759 docstrings across up to 57 files
is not an `Edit` call each. `skills/implement/SKILL.md` §2 allows a scripted
edit where every substitution asserts its landing, and that is the shape:
one throwaway script, run once from the mapping above, that for each unit
finds the docstring by `ast` (`node.body[0]` an `ast.Expr` holding a string,
or none), inserts the line after the summary line and a blank line, or writes
a docstring of the line alone, and raises where the docstring's text is not
found verbatim in the file once. The script is a probe under `agent-contract`
§7 — `test_tmp_*`, run once, deleted before the hand-over — and the diff it
leaves is what the warden reads. `uvx ruff format --check .` must stay green
after it: ruff does not reflow a docstring, and `E501` is not selected
(`ruff.toml`), so a long line is not a lint finding, but a line the cell
would make longer than about 110 characters is trimmed at a clause boundary
by hand, with the rest of the cell under it.

**The census edit** is the same script's: it removes exactly the lines whose
`path#unit` gained a line, and asserts each was present once.

**Where it breaks in six months.** A line written from a row is a reading of
2026-10-07 carried into the docstring; nothing re-reads it (limit 5 of
`docs/the-reader-registry.md` §*What neither check can read*). A unit
redesigned from `guess` to `owned` keeps the old word until the diff's
reviewer moves it. That is the cost #835 accepted for the whole mechanism,
and the backfill adds 245–759 such lines at once.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| (a) write all 759 clean units now, as #835 Q7's default | 687 `Re-read ·` rows in one fragment, 1.9 times the whole run's 360; each carries `--checked <date>`, which asserts a reading, so either the smith reads 687 released rows that a docstring line cannot have falsified, or the fragment records 687 readings nobody made — the unread re-stamp `seal/follow-up.md` already names | not the default; Q1 option (a) |
| (b) write the 275 `guess` units only, the half the registry exists for | 247 re-reads for the same reason; `grep -rn "Reads: guess"` becomes complete for the inventory's clean readers, at 69% of the run's whole re-read output | not the default; Q1 option (b) |
| **(c) write the 245 units no ledger row cites; the 514 cited ones wait for Q1 or 0.22.0** | zero re-reads and one live re-stamp; the grep lists 95 of the 275 `guess` readers, and the biggest readers (`reverify`, `gate`, the `main`s) stay off it — they are stale anyway, and a stale unit stays on the census under every option | **chosen as the default**; the owner can widen it in Q1 |
| read the 123 stale units afresh and write their lines | 501 re-reads and 357 live re-stamps for a judgment no row grounds; the units the siblings rewrote declare when next touched by the rule's own transition | rejected; `spec.md` §*Which units, measured* |
| write the lines by hand, one `Edit` per unit | 245–759 tool calls for a mechanical insertion, each a chance to mistype the class word; a script that asserts each landing is the form `skills/implement/SKILL.md` §2 names for this | rejected |
| keep a mapping script in the tree so 0.22.0 reruns it | mechanism the build was told not to add; the mapping is six rules, stated above, and the inventory it reads is a reading of a moment that 0.22.0 may not want | rejected; the rules are in this file |
| retire `inventory/` with the process record now that its classes live in the code | the columns that did not move (`Decides`, `Duplicates`, `Note`) and the 123 stale rows are the only reading of those units anybody wrote; `settle --retire` takes the directory at the fold, and the tag keeps it | rejected; `spec.md` §*The inventory's fate* |
| write `Reads: nothing` lines on the unrowed 695 units from the inventory's silence | the inventory's agents did not judge those units `nothing`; they left them out, and a line on each would be 695 claims nobody made (#835's spec says this is #834's to weigh) | rejected |

## Phases

Vertical slices — each phase ends with something runnable and verified.
Phases 2 and 3 touch every population file except `hooks/worktree-guard.py`;
phase 4 is that file alone, after the release branch with #894 and #896 is
merged in, so the sibling fix passes never meet a docstring conflict.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The mapping at the build's tree, by the six rules above, read with `reader_registry.population()`: the rowed, clean, stale, conflicting and unparsed counts, the Q1 sets (a)–(c) with their re-read counts, each beside the frame's reading at 57e2bc13; the per-unit listing stays in the phase record's text only as counts and the names of the 30 hand-read units. No tree edit | `phases/phase-1.md` holds both readings with their SHAs; `bin/test tests/test_a_reader_declares_its_input_class.py` green before any edit | 681fa7b1 |
| 2 | The lines on every unit in Q1's answered set (default: the units no ledger row cites) in every file but `hooks/worktree-guard.py`, and the census lines of exactly those units removed, by the one-shot script, deleted after. The 30 hand-read units are decided here, the weakest class winning | the registry test green; `git diff --stat` on the census shows a line removed per unit written and no other; `bin/evidence-check .` reports no drifted released row under (c), and the live rows it names are re-stamped in place (`--reverify --checked <date>`, narrowed with `--ledger` to the fragments read); under (a) or (b) the `Re-read ·` rows are written with `--reverify --into` after each cited row is read | 36491ddb |
| 3 | The rows in `seal/ledger/1791382684-every-reader-and-record-is-inventoried.md`: one claim per acceptance row of `spec.md` §*User scenarios & acceptance* that a test holds, anchored on the test by #836's form where one holds it and on the census file's heading-less line count otherwise; the changelog fragment; `overview.md` opened with the divergences phase 2 met | `bin/evidence-check .` exit 0; `correction-check` clean; `survivor-check --range origin/release/v0.21.0...HEAD` clean | 8160ad69 |
| 4 | After `git merge origin/release/v0.21.0` with #894 and #896 landed: phase 1's mapping again for `hooks/worktree-guard.py` only, its clean units' lines by the same script, its census lines removed, and the merge's drift re-read; if either sibling has not landed when phase 3 closes, this phase waits and the pull request opens as a draft with the phase's row empty | the registry test green; the guard's own modules green (`tests/test_worktree_guard.py`, `tests/test_the_guard_asks_once_per_session.py`); `bin/evidence-check .` exit 0 | |

This table is also where the work records how far it got. There is no separate
task list. **Status is empty, or the commit that closed the phase.**

## Seams

- `hooks/worktree-guard.py` — 43 clean units at 57e2bc13, 24 of them uncited;
  #897 (#894) changes its `main` and the branch-switching block, and
  `fix/896-the-idle-session-rows-ask-nobody` changes 109 lines of it (read
  from `git diff --stat origin/release/v0.21.0...origin/fix/896-…`). Phase 4
  only.
- `tests/conftest.py` — 27 clean units, in the population as a helper module;
  its module docstring already declares for the body (#835). Lines go on the
  units, and the module line stays.
- `skills/evidence-check/scripts/evidence_check.py` — 62 clean units and 22
  stale; three rowed units already carry #835's own line (`check_records`,
  `file_claims`, `frozen_from`) and are skipped, the row's class matching the
  line in each.
- `tests/reader_registry.py` — not in the inventory (it did not exist at
  5623d728); every unit declares already.

## Operational impact

No migration, dependency or environment change. What a deployer meets:

- **The ledger fragment grows by what Q1 chooses** — 0 `Re-read ·` rows under
  the default, 247 under (b), 687 under (a) — and the fold at 0.21.0 carries
  them into `seal/releases/0.21.0.md`.
- **Any branch open against `release/v0.21.0` that edits a unit this build
  wrote a line on meets a docstring conflict at its merge.** At 57e2bc13 the
  only such branches are #894's and #896's, and phase 4 waits for them.
- **The census shrinks by 245 to 759 lines** and `grep -rn "Reads: guess"`
  grows by 95 to 275; the number in `docs/the-reader-registry.md` §*The counts
  at landing* is the reading of #835's moment and is not edited.
