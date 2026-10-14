# 1791940762-the-record-of-truth-is-tests-not-coordinates — phase 6

| Field | Value |
|---|---|
| Phase | 6 |
| Commit | 8b137510 |
| Ran by | smith on Opus 5.5, as the attribution line in the spawn prompt names it |

## What this phase was asked

The step `plan.md` names *Decided after phase 5, to build before review*.
First, `seal.py`'s export and import still carried `ledger/<id>.md` through
`LEDGER_DIR`: delete that path and its constant, delete the cases that exist
only for it, and keep what a case guards where it only mentions the ledger
in passing. Second, the owner's decision of 2026-10-14, overturning
alternative G: the kernel leaves `skills/evidence-check/` for a home named
for what it does, resolving `path#unit` coordinates, by default
`skills/verify/scripts/coordinates.py`, confirmed against the import graph.
Each of the 16 importers is checked first for what it still uses, and an
import the ledger left unused is deleted rather than moved. The rest move
with the wrappers, the tests and the docs, `skills/evidence-check/` stops
existing, and S9 holds at zero. Then this record, and `plan.md`'s Status and
`overview.md` rewritten in place. Narrow runs with the census and
one-reader modules after each step, `bin/rules` and the budget check.

## What this phase found

**The frame holds, with two corrections to the spawn's picture.**

- `seal.py`'s ledger path was smaller than *about 60 test references*
  suggests. The code held one constant and one branch of `work_item_of`,
  which counted `ledger/<id>.md` as part of its work item for the release
  reminder. The export and import walk the root whole, so they never moved
  the fragment through `LEDGER_DIR`. The 60 references were the module's
  fixture, which used `ledger.md` and `ledger/<id>.md` as ordinary records.
- No case existed only for the ledger path. Every case that named a ledger
  file guards something else: the zip's members, a collision, a link, a
  size bound, the manifest. The fragment branch had no case of its own,
  because the one reminder case that removed a fragment also removed the
  item's `specs/` files (read, not probed). So nothing was deleted and all
  96 cases stay. The fixture now carries `follow-up.md` where it carried
  `ledger.md`, `specs/<id>/plan.md` where it carried `ledger/<id>.md`, and
  `seal/specs/w/spec.md` where a zip member was `seal/ledger/w.md`. The
  design record's import bullet, in both editions, names
  `<name>.incoming<ext>` where it named a fragment's `<id>.incoming.md`.

**The 16 importers were 16 at `a8d83663`, and 5 load the kernel now.** At
`a8d83663`, 16 files outside `tests/test_*.py` named the kernel's path. Nine
stopped in phases 2 to 4, deleted with the ledger or cut from it:
`fold_ledger.py`,
`correction_check.py`, `survivor_check.py`, `settle.py`, `broad_gate.py`,
`hooks/blocks.py`, `evidence-advisor.py`, `ledger-migrate.py` and
`root-migrate.py`. Of the seven left, `hooks/config.py` and
`unverified_check.py` named it only in comments and docstrings. Each of the
five loaders still uses the kernel, read off its attribute accesses, so none
was deleted:

| Loader | What it uses |
|---|---|
| `.github/scripts/rider_check.py` | `resolve_unit`, `content_hash`, `py_spans`, `gfm_lines`, `ANCHOR_LOCATOR`, `ANCHOR_HASH` |
| `skills/code-review/scripts/chain_check.py` | `PACT_ANCHOR_RE`, `unquoted`, for the pact anchors in a declared work item's `spec.md` |
| `pact_check.py` | `content_hash`, `gfm_lines`, `heading_level`, `heading_path`, `HEADING_SEP`, `markdown_lines`, `PACT_ANCHOR_RE`, `unescape`, `unquoted` |
| `skills/settle/scripts/fold_check.py` | `named_unit` |
| `tests/reader_registry.py` | `py_spans`, `content_hash`, `gfm_lines` |

Inside the kernel every top-level name has a reader, counted by `git grep`
over the tree: nothing in it was left unused either.

**The graph confirms `skills/verify/scripts/coordinates.py`.** The kernel
has one dependency, the shared reader `unverified_check.py`, which already
lives in `skills/verify/scripts/`; beside it, the loader path is a sibling's.
Its loaders sit in four different directories, so none of them argues for
its own. `.github/scripts/` does not ship with the plugin and `pact-check`
does. `pact_check.py` loads the kernel as a sibling and had to leave
`skills/evidence-check/` too, so it moved beside the kernel, and
`bin/pact-check` and its `.cmd` twin point there; `pact-check` is typed as
before.

**The census follows a path and refuses a hash.** The lines of the two moved
files keep their hashes under the new path, in sorted place. Four units
whose bodies changed declare a `Reads:` line and leave the census:
`rider_check.py#load_checker`, `coordinates.py#unbounded`,
`fold_check.py#coordinates` (renamed from `evidence`) and
`unverified_check.py#heading_level`. `seal.py#work_item_of` and
`#linked_path` did the same in the first step.

**Phase 4 left three things naming what it deleted.**

- `coordinates.py#unbounded`, the refusal a bare symbol in a file with no
  bounding rule reads, ended *`--reverify` fills the hash* and offered a
  ledger coordinate with a placeholder hash. `--reverify` left in phase 4.
  The sentence now names the quoted-line locator alone. Its pin was red
  against a mutation putting the old ending back (executed, 22 cases red).
- `agents/warden.md` §Report told the reviewer an evidence checker reads
  its committed report for names not in the tree, with a per-line marker and
  a rule that the marker never goes inside a fence. That checker left in
  `9c9b99fb`, and the fence rule contradicted
  `skills/code-review/SKILL.md`'s paste-ready convention. Both paragraphs
  leave; the identifier rule and its domain arm stay. The pin's two needles
  for them go, red against the edited file first (executed).
  `preload:warden` is lowered from 102,229 to 99,690 and
  `unenforced:agents/warden.md` from 17 to 16, both as measured.
- `.github/ISSUE_TEMPLATE/gate-misfired.md` listed the evidence check among
  the gates.

**The first step's narrow run missed a rider.** Re-pointing the fixture
changed `test_a_manifest_field_of_the_wrong_type_does_not_raise`, which a
rider is anchored on, and `test_a_rider_reaches_its_file.py` was not in that
step's run. It was red at `a5e426a3`. The rider still asks for an
`exported_at` row and is unanswered; the drift was the fixture, so it is
re-read and re-stamped in `0d8e34c8`. The module has run after every step
since.

**rider_check's missing-kernel sentence is pinned now.** It names the new
path, and `test_a_missing_kernel_is_a_sentence_naming_where_it_ships` holds
it whole. The case was red against a mutation putting `evidence_check.py`
back (executed).

**S9 holds for the ledger and the sweep.** Its grep over `agents skills
templates docs hooks .github CLAUDE.md CONTRIBUTING.md README*.md` finds no
`seal/ledger`, `seal/releases`, `evidence-check`, `Re-read ·` or
`Corrected ·` line. The 15 lines left are the mutation word *survivor* in
`arm_check.py`, `round_record.py` and `skills/verify/SKILL.md`, the
exclusion `overview.md` already records (executed).

**What left, by commit.**

| Commit | What |
|---|---|
| a5e426a3 | `LEDGER_DIR` and `work_item_of`'s fragment branch; `seal.py`'s docstrings, the module's fixture and both editions of the design record's import bullet |
| 0d8e34c8 | the rider re-stamp |
| b9a02b97 | the move to `skills/verify/scripts/coordinates.py` with `pact_check.py`, both wrappers, the loaders, the census, `.test_durations` (two ids carry their prices), three docs, `hooks/config.py`'s comments, the `unbounded` sentence and the new case |
| 7387126d | the warden's two paragraphs, the pin's two needles, two budget rows |
| a55ac12d | the issue template |
| 8b137510 | seven `.test_durations` entries for ids no case collects, each naming the old directory, its wrapper or its two skills |

**Verification, executed at the phase's tip unless named.** After the first
step, `test_the_records_can_be_carried_out_and_in.py`, the census and
one-reader modules, and the seven modules reading the design record: 96,
80 and 185 passed. After the move, the 19 modules it touched: 3,491 passed,
7 skipped, after three red ones were fixed (the rider above and one
`OUT_OF_CLASS` key naming the old path). The 77 modules that name a changed
file: 7,955 passed, 8 skipped. After the warden edit, the 38 modules that read
`agents/warden.md`: one red, `test_the_trees_budgets_hold`, for the two rows
above, then 163 passed for that module and the pin's. The durations share
over the collected suite, 611 of 12,267 unpriced before the two carried
prices: `test_the_durations_file_prices_the_suite` passed. `budget_check.py`
exit 0 on the tree and against `origin/release/v0.22.0`; `fold-check` exit 0
(158 statements, 18 documents); `bin/rules docs/the-record-layout.md` exit 0;
`rider_check.py` exit 0 (16 ok); `bin/pact-check --help` exit 0;
`uvx ruff check` and `ruff format --check` on every Python file changed.
`unverified-check --baseline origin/release/v0.22.0`, `chain_check.py
--baseline origin/release/v0.22.0` and `settle` exit 0 at `48c59749`, and the
nine modules that read work-item records, 436 passed. After the prune, the
budget check on the tree and against the base and the durations case again.
The full suite is the sealer's.
