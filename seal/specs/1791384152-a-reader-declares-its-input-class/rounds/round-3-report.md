# Round 3 report — a reader declares its input class (#835)

This is the verifying round for round 2's fixes. I reviewed the fix range
`6b108d36..6c5d4529` at the target `1bbed1a1`, in a `git clone --no-local` of
the worktree, against `origin/release/v0.21.0` at `c38f97d7`. Coordinates were
carried from `round-2.md`, `round-2-report.md`, `round-2-fixes.md` and
`round-1-fixes.md`. Every verdict below is my own. I read the fix report's
claims in full and checked each one against the code or a probe. The one fact
the orchestrator executed, `round_record.py close` exit 0 at the target, was
not re-run.

## How the findings relate

```
asked 1  🟡 1's fix, this tree only ....................... closed; default-repo and absent-map rows answer right
                                                             ⬜ 1  an in-tree directory named like a map is refused
asked 2  ⬜ 2's fix, a path through `..` .................. closed; escape still first, round 1's text unchanged
                                                             ⬜ 2  a trailing `/` still reads as gone
asked 3  the record corrections ........................... R7, the changelog and the document all hold
                                                             ⬜ 3  `Enforced by:` lacks the `..` case
asked 4  depth ............................................ nothing found inside either depth-1 case
cleanup  .................................................. ⬜ 4  `default_repo` is now a dead parameter
```

⬜ 1 and ⬜ 2 both sit in `removal_findings`, the unit round 2's fixes
changed. Neither reads a row the wrong way silently in a case a frame will
meet, which is why both stay ⬜. ⬜ 2 is the class ⬜ 2 of round 2 belonged to:
the fix closed one spelling of it.

## What each asked item came to

**1. A `--map` prefix is matched against the declared maps, and an in-tree
directory with a map's name is refused.** Executed through `check_records`,
with the arguments `main` passes.

- The test at `evidence_check.py:6134` is the same test `place` makes at
  `evidence_check.py:1292`: the names of `--map` arguments, compared whole or
  as `name/`. Nothing is guessed from the path's shape. `legacyx/a.py#k` under
  `--map legacy=…` reads `STANDING`.
- `old.py#k`, absent here and present in the `--default-repo` checkout, is no
  finding. The same row with `old.py` in this tree too is `STANDING`. Round
  2's two wrong answers are both gone.
- `legacy/a.py#k` under `--map legacy=…`, where the mapped checkout is absent,
  is `REFUSED` with the new text.
- The orchestrator's question gets a no. An ordinary in-tree row whose first
  segment equals a map's name **is** refused (⬜ 1).

**2. A path through `..` is refused, and the escape refusal still comes
first.** Executed and read.

- `missing/../kept.py#k` and `pkg/../kept.py#k` (with `pkg/` present) are
  both `REFUSED` with the new text. `../outside.py#k` keeps the escape text.
- The order is pinned. Round 1's case,
  `test_a_coordinate_that_does_not_read_is_refused_never_read_as_gone`, asserts
  the escape text for `../outside.py#f`. Moving the `..` check ahead of `place`
  would give that row the `..` text and turn the case red. Read.
- Round 1's pinned texts are unchanged. The diff to the test module only adds
  lines after line 1776.
- A trailing `/` is another spelling the kernel and `contained` disagree
  about (⬜ 2).

**3. The three record corrections hold.**

- R7. `evidence-check` narrowed to this item's ledger reads 81 rows OK, D1's
  new hash `3b360e2b` among them. The three mutations the corrected cell
  cites went red through `bin/mutation-check`: the name fallback narrowed,
  the `os.open` row removed and the `re.split` row removed. Executed. My
  narrowing of the fallback, `target is None`, approximates the build's rule
  rather than restoring it byte for byte.
- The changelog's `--reverify` sentence is true. `--reverify` calls
  `frozen_from` alone (`evidence_check.py:6658`) and returns at `:6791` or `:6823`, before
  `check_records`. `cutoff_row` for `Removes from` is called only from
  `check_records` (`:6347`). At the base `c38f97d7`, `frozen_from` already
  refused a file that will not read. Read.
- The document's list now names every row refusal the arm makes, seven in
  all, the `..` and `--map` ones included.
  `fold-check` exits 0 and holds 19 documents under 1000 lines. Executed. The
  `Enforced by:` line names round 1's case and round 2's `--map` case, and not
  the `..` case (⬜ 3).
- The test docstring is right. `os.open` and `re.split` are rows of
  `K1_FUNCTIONS` that round 1 added, and `ast.walk` and
  `pathlib.Path.read_text` reach K1 through `K1_METHODS`. Read.

**4. Nothing was found inside the depth-1 units.** Both cases assert each
finding's whole text and their full list. Each went red through its own
`AssertionError` under the mutation it answers: the `--map` refusal turned off,
`place` handed `maps` and `default_repo` again, and the `..` refusal turned
off. Executed. The second of these went red on the `old.py` row, so the case
pins the `--default-repo` half, not only the `--map` half.

## Findings

### ⬜ 1 · An in-tree directory that carries a map's name is refused, and the remedy names no way out

`skills/evidence-check/scripts/evidence_check.py:6134`. With `--map legacy=…`,
a frame that removes `legacy/a.py` from this tree is refused, and the text
says *write the path in this tree*. That path already is the tree's path.
Executed: `REFUSED` whether the mapped checkout is absent or present.

The way out exists and nobody wrote it down. `./legacy/a.py#k` misses the
prefix test, `place` reads it in this tree, and it reads `STANDING` while the
file holds the unit. Executed.

Why ⬜ and not 🟡:

- The refusal is loud, at exit 2. Nothing is read as gone.
- It follows the resolver every arm shares. `place` says *a prefix named by
  --map wins*, so in that repository the ledger also reads `legacy/…` as the
  mapped checkout.
- The defect is the remedy sentence. The text and the document should name
  `./`.

### ⬜ 2 · A trailing `/` reads as gone while the file holds the unit

`skills/evidence-check/scripts/evidence_check.py:6173`. `kept.py/#k` and
`kept.py/.#k` give no finding while `kept.py` defines `k`. Executed.
`contained` resolves the path with `realpath`, which drops the trailing `/`, so
the row is inside the tree. The kernel will not open `kept.py/` (`ENOTDIR`),
and `os.path.lexists` answers `False` for the same reason. The row is
therefore read as a removal that happened.

This is round 2's ⬜ 2 by another spelling. The fix refused the `..` segment.
It did not change the cause, which is that the path the arm opens is not the
path `contained` judged. Nobody writes such a row on purpose, which is why
round 2 rated the first spelling ⬜, and this one gets the same rating.
Reading the normalised path closes every spelling at once. The fix below does
that and keeps the `./` way out that ⬜ 1 depends on.

### ⬜ 3 · The document's `Enforced by:` line does not name the `..` case

`docs/the-reader-registry.md:130`. The paragraph above it now lists *a path
that … walks through `..`*, and the line names round 1's case and the `--map`
case.
`tests/test_a_record_states_what_the_tree_has.py#test_a_path_through_dot_dot_is_refused_never_read_as_gone`
is the one case not on it. This is round 2's ⬜ 4 again, one case over. Line
123 also runs past the paragraph's wrap.

### ⬜ 4 · `removal_findings` keeps a `default_repo` it no longer reads

`skills/evidence-check/scripts/evidence_check.py:6066`. After `5dfefd3b`, the
parameter appears only in the signature, and `file_claims` still passes it at
`:6242`. A reader of the signature takes `--default-repo` for an input of the
arm, which is the reading 🟡 1 removed. The fix report says the function
*keeps its parameters* on purpose, to keep the contract. Dropping the
parameter changes one caller.

## Regression tests to plant

- `tests/test_a_record_states_what_the_tree_has.py`: `kept.py/#k` with
  `kept.py` defining `k` reads `STANDING` (⬜ 2). It is seen red by
  construction, because the probe above gave no finding for exactly this row
  at the target.
- The same module: `./legacy/a.py#k` under `--map legacy=…`, with the file in
  this tree, reads `STANDING`. This pins the way out ⬜ 1 relies on, so a later
  refusal of `.` segments cannot close it unseen.

## Facts for the evidence ledger

- At `1bbed1a1`, D1's heading hashes to `3b360e2b`, and `evidence-check`
  narrowed to this item's fragment reads 81 rows OK.
- At `1bbed1a1`, R7's three cited mutations are red through `bin/mutation-check`,
  each failing exactly the parametrised row it names.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| ⬜ 1 | an in-tree row whose first segment equals a `--map` name is refused, and the remedy says to write the path in this tree, which it already is; `./` reads it in this tree and is written nowhere | `skills/evidence-check/scripts/evidence_check.py:6134` | open | executed through `check_records`: `REFUSED` with the map absent and present; `./legacy/a.py#k` `STANDING`; the test is `place`'s own |
| ⬜ 2 | a trailing `/` (`kept.py/#k`, `kept.py/.#k`) reads as gone while the file holds the unit; round 2's ⬜ 2 by another spelling | `skills/evidence-check/scripts/evidence_check.py:6173` | open | executed: no finding for both rows; `contained` judges by `realpath`, the read and `lexists` by the kernel |
| ⬜ 3 | the document's `Enforced by:` line does not name the `..` case, and line 123 runs past the wrap | `docs/the-reader-registry.md:130` | open | read; `fold-check` exit 0 |
| ⬜ 4 | `removal_findings` keeps a `default_repo` parameter nothing reads | `skills/evidence-check/scripts/evidence_check.py:6066` | open | read: the name occurs only in the signature |
| 🟢 | round 2's first finding is closed — a removal is read in this tree only: the original never answers, and a `--map` prefix is refused | `skills/evidence-check/scripts/evidence_check.py:6148` | confirmed | executed: `old.py#k` no finding with the original holding it, `STANDING` with this tree holding it, the mapped row `REFUSED`; two mutations red through the case's assertion |
| 🟢 | round 2's second note is closed — a path through `..` is refused, after the escape refusal | `skills/evidence-check/scripts/evidence_check.py:6159` | confirmed | executed: `missing/../` and `pkg/../` refused, `../outside.py` keeps the escape text; one mutation red; read: round 1's case pins the order |
| 🟢 | round 2's third note is closed — R7 says what K1 does since round 1 | `seal/ledger/1791384152-a-reader-declares-its-input-class.md:25` | confirmed | executed: the three cited mutations red, 81 rows OK |
| 🟢 | round 2's fourth note is closed — the document and the changelog list every refusal | `docs/the-reader-registry.md:119` | confirmed | read; the `Enforced by:` gap is ⬜ 3 |
| 🟢 | round 2's fifth note is closed — the changelog's `--reverify` sentence is true | `seal/specs/1791384152-a-reader-declares-its-input-class/changelog.md:46` | confirmed | read: `--reverify` calls `frozen_from` alone and returns before `check_records`, the only caller of `cutoff_row` for `Removes from` |
| 🟢 | round 2's sixth note is closed — the docstring says which rows are round 1's | `tests/test_a_reader_declares_its_input_class.py:492` | confirmed | read: `os.open` and `re.split` are `K1_FUNCTIONS` rows round 1 added |
| 🟢 | round 1's second finding stays closed under round 2's fixes — the escape and unreadable refusals keep their texts | `skills/evidence-check/scripts/evidence_check.py:6149` | confirmed | executed: round 1's case passes at the target; the test module's diff only adds lines |

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

## Paste-ready fixes

### ⬜ 1

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

### ⬜ 2

```python
# skills/evidence-check/scripts/evidence_check.py — removal_findings, in place
# of `full = os.path.join(repo, rel)`. Open the path `contained` judged, so a
# trailing `/` or `/.` cannot read as gone; `..` is refused above, so the
# lexical normalisation never crosses a symlink.
        full = os.path.join(repo, os.path.normpath(rel))
```

Needs a fix: no

Loses a record or crashes: no

## Proof block

Opened at `1bbed1a1` in the review clone, or read through `git show` and
`git diff` over `6b108d36..6c5d4529`:

- `seal/specs/1791384152-a-reader-declares-its-input-class/rounds/round-2.md`,
  `round-2-report.md`, `round-2-fixes.md`, and the *Seen red* section of
  `round-1-fixes.md`; `changelog.md` lines 15–55
- `skills/evidence-check/scripts/evidence_check.py`: `read` (1143), `contained`
  and `place` (1253–1310), the config readers and `cutoff_row` and
  `frozen_from` (4300–4432), `removal_findings` (6066–6215), `file_claims`'
  call (6241), `check_records`' head (6306–6330), `main`'s `--map` parsing
  (6585–6595), the `--reverify` branch (6625–6830), and the records call
  (6880–6905); `frozen_from` at the base `c38f97d7`
- `tests/test_a_record_states_what_the_tree_has.py`: helpers (20–75, 175–195),
  `REMOVES_HEAD` and `frame` (1545–1580), the cases at 1740–1820
- `tests/test_a_reader_declares_its_input_class.py` (440–540)
- `tests/reader_registry.py`: `k1_call` (198–231) and the `K1_FUNCTIONS` rows;
  round 1's diff to it over `8f3d912e..f21f151f`
- `docs/the-reader-registry.md` (108–132)
- `seal/ledger/1791384152-a-reader-declares-its-input-class.md` (the diff, and
  the rows at 5 and 28–32)
- `bin/mutation-check`
