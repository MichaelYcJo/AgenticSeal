# Implementation Plan: whether a ledger or record line is live has seven rules with four failure directions (#872)

<!-- seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-13 by the orchestrating session, under the owner's `automation` answer, when `smith` was spawned.

## Summary

Seven units decide whether a ledger or record line is live, and they fail in
four directions. The tree already tied each direction to a consequence —
1790260566's D1 split the EXCUSING readers from the HOLDING ones, and the
two policy statements in `docs/the-evidence-ledger.md` state one direction
each — but the rule is written in no one place, none of the seven units
declares which answer it gives, and nothing pins the seven side by side. No
issue since 0.18.0 traces to any of them, so no reader's behaviour moves.
Three phases: the statement in `docs/` with the direction table that enforces
it; the seven `Reads:` lines with the released rows they drift re-read into
this work item's fragment; the record.

## Technical context

Coordinates at a8db6161, this branch after its routing commit, on
`release/v0.21.1` at 321e9de1.

**The seven, and what each feeds.**

- `skills/evidence-check/scripts/evidence_check.py#quoted_lines` (366): the
  indices inside a fence that closes, by `fence_rule` (the shared delimiter
  pair, or the vendored pair where the checker ships alone). `unquoted` (432)
  blanks those lines to spaces, offsets kept, and every `.md` region the
  checker hashes or walks reads `gfm_lines(unquoted(text))` (596, 1666,
  1921, 2072, 2855, 2937, 3965, 4023, 4488, 5776); `--migrate` (3246) leaves a
  fenced row byte for byte. An unclosed fence and an HTML comment are read.
- `evidence_check.py#claim_lines` (5580): `[(number, text)]` for a record's
  claim lines — a closed fence is a quotation, a line-start comment that
  closes is an aside to its `-->` position, an unclosed fence or comment is
  held and read at the end, `NAME NOT IN TREE` exempts its line. Read by
  `stated_names` (5718), `stated_coordinates` (5735), the stamp arm (5975) and
  the Removes reader (6046).
- `skills/settle/scripts/settle.py#anchored_rows` (587): every line of every
  ledger the checker names, `ANCHOR_RE` per line, superseded rows skipped,
  the freeze read through `frozen_from`. Read by `survey` (792), `retire`
  (1125) and `--retire-process` (1437).
- `.github/scripts/rider_check.py#quoted_lines` (231): the indices inside a
  fence that closes where `hooks/blocks.py#walk` is sure; read by
  `comment_blocks` (336) for `.md` files that carry the marker.
- `skills/verify/scripts/unverified_check.py#live_lines` (649): `(line,
  flag)` with `_liveness` (455) run twice and ANDed. Read by `folded_items`
  (1302, 1353), `settle.py#coordinates` (409, 423), `fold_ledger.py`
  (226, 251), `gather_changelog.py` (140, 223), `fold_check.py` (221, 365,
  375), `survivor_check.py#gathered_fragments` (1005) and `#ledger_rows`
  (1164, 1234).
- `hooks/config.py#hidden_lines` (185): `{index: "fence" | "comment"}` where
  the walk is sure, `blocks.fence_only` where it is not, and the first
  unclosed opener. Read by `fence_map` (176) and through `unfenced` by
  `config_rows`, `refusal`, `seal.py#table_span`, `routing.py#shown` and
  `broad_gate.py` (976).
- `unverified_check.py#readable` (733): `blank_fences(strip_comments(
  gfm_lines(text)))`. Read by `check_text` (901), `chain_check.py` (22
  sites), `round_record.py` (19 sites), `broad_gate.py` (2900),
  `release_seal.py` (376), `survivor_check.py#exemptions` (1948) and
  `hooks/review-history-guard.py#is_closed` (146). No caller hands it a
  ledger file.

**What pins each today**, so phase 1 does not re-plant an edge:
`tests/test_a_merge_cannot_silently_drop_a_correction.py` and
`tests/test_the_hooks_hide_what_a_renderer_hides.py` (the two
`quoted_lines`, `hidden_lines`); `tests/test_a_record_states_what_the_tree_has.py`
(`claim_lines`); `tests/test_settle_reads_before_it_removes.py` and
`tests/test_settle_retires_the_process_record.py` (`anchored_rows`);
`tests/test_unverified_rows_close.py` and five more (`live_lines`);
`tests/test_chain_hooks.py#reader_blanking_passes` and 36 more modules
(`readable`).

**The census and the released rows.** All seven stand in
`tests/undeclared_readers.txt` (lines 163, 398, 971, 1039, 1190, 1493, 1501
at a8db6161). The released rows anchored on them: `quoted_lines` 0.15.3
P2-1, P2-3; `claim_lines` 0.9.0 R5, 0.15.0 A4, 0.15.3 P4-1, P4-2;
`anchored_rows` 0.14.0 G3, 0.18.0 L8 and its re-read, 0.21.0 K12, K16 and
two re-reads; `live_lines` and `_liveness` 0.13.0 R11; `readable` 0.9.2 T2,
0.15.3 P1-4, 0.16.0 G1; `hidden_lines` 0.16.0 P3-1; the rider's
`quoted_lines` 0.16.0 P5-1 names the unit in prose and anchors where the
builder reads it. `Ledger frozen from` is 1790993141, so each drifted row is
answered by a `Re-read ·` row in this work item's fragment.

**The registry's grammar.** One docstring line, `Reads: <class> — <what>;
unknown <direction>`, the class the word after `Reads:`, the direction the
last word; a wrapped line has no last word. The check is
`tests/test_a_reader_declares_its_input_class.py`, and a changed census unit
is refused until it declares and its line is removed.

**What breaks in six months.** A reader redesigned from one answer to
another keeps its old `Reads:` line and its old row in the direction table
until somebody moves them — the registry's limit 5, a stale line. What
bounds it: the direction table is a test, so a redesign that changes an
answer on any shape goes red there, and a redesign that changes none changes
nothing a reader acts on. The second: a new eighth reader is not in the
table. What bounds it: a new unit must declare, and its `Reads:` line is read
at review against the statement, which names the three answers and says a
reader of a new kind of line is a fourth answer somebody has to argue.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| One rule with one bias for all seven | the HOLDING bias drops nothing but parks a fold marker quoted in an example as a real fold, which excuses a removal nothing absorbed (#584, the shape `live_lines` was built against); the EXCUSING bias drops a parked ledger row in silence (#444's direction rule; D4); `readable`'s bias would blank 46 rows in eight release files (read, #867's frame). Each bias is wrong for two of the three kinds of line | rejected — three answers, each tied to its consequence |
| Merge the checker's `quoted_lines` with the rider's | the checker ships alone in a user's `tools/` where `hooks/blocks.py` is not beside it (Q6 of 1790260566, the vendored pair); a walk-aware checker needs a vendored walk and a second equality case, for a difference measured at zero rows — the released ledgers carry no fence line (P2-3) | rejected |
| Build `claim_lines`' fence arm on `quoted_lines` | inside a never-closed fence a closed line-start comment would become an aside, moving the stated judgment *read rather than drop* on a malformed record; four released rows (R5, A4, P4-1, P4-2) and no issue | rejected — a merge for symmetry |
| Read `anchored_rows` through the checker's rule | a directory the checker would not break is removed at the next retirement; D2 decided this ahead of #444 and `test_a_fenced_anchor_still_keeps_the_directory` pins it | rejected |
| Read `hidden_lines` through `live_lines` | the hook path loads a skill module on every Bash call (D8); a `<!--` nobody closed would hide every config row below it, which turns a `Broad gate` row into no row and stops the sealer | rejected |
| Read `readable` through `live_lines` | a flag is not a blanked line: 37 test modules and 40-odd call sites read lines with indices intact, and `reader_blanking_passes` refuses a pass added or removed; the working tree and the base must count the same table, which a flag per line does not give | rejected |
| Build the positional scanner for `claim_lines` (Q1 (b)) | a code-span state got wrong drops every claim to the next `-->` in silence; `live_lines` paid five rounds for the same state; no issue since reports a mid-line comment | rejected; the grounds in `spec.md` §*Scope*, the row the owner's |
| State the rule in `docs/` only, declare nothing | the rule lives one file away from every unit it governs; a reader changing a unit meets no sentence, which is the stale-copy failure the registry was built to end | rejected — the units declare |
| Declare only, no statement and no table | seven sentences with no common text to be held to; the next reader of a new kind of line has nothing to argue a fourth answer against | rejected |
| A statement in `docs/the-reader-registry.md` instead of the ledger document | the registry is about declaring, not about what a line is; the ledger document already holds both direction statements, and a session asking whether a row is live opens it | rejected — the ledger document, beside its two siblings |
| The table as a parametrised case inside each reader's existing module | seven modules, no row where the seven stand together; a change to one direction is visible in one module only | rejected — one module |

## Phases

Vertical slices — each phase ends with something runnable and verified. A
case is planted only after it has been seen red (`agent-contract` §15), each
phase states its direction and its prompt budget in its phase record
(`CONTRIBUTING.md` §*What a change to a gate must carry*), and the budget is
zero in every phase because no verdict moves.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The rule and its pin. The direction table test (`tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py` or a name the builder judges truer), one corpus of the six shapes in `spec.md` §*Data & interfaces*, seven adapters, the stated answer per cell; seen red under one mutation per bias (an unclosed fence hidden by `quoted_lines`, a disagreement read live by `live_lines`, an unclosed fence left unblanked by `readable`), the mutation and its output in the phase record. The statement in `docs/the-evidence-ledger.md` under this work item's marker, bold opening, one `Enforced by:` line naming the table's cases. One sentence in `skills/evidence-check/SKILL.md` §*What counts as a claim*. Direction: nothing a gate answers moves | S1, S2, S4; the new module; `bin/fold-check`; `tests/test_a_folded_statement_names_what_enforces_it.py`; `tests/test_docs_line_wrap.py` | 78237f6a |
| 2 | The seven declare. A `Reads:` line and one consequence sentence in each of the seven docstrings, from the table in `spec.md` §*Data & interfaces*, each settled at the unit; the seven census lines removed; `evidence-check --strict .` names each drifted row, `--reverify --into seal/ledger/<this id>.md --checked <date>` writes the `Re-read ·` rows, each read by the builder; the probe re-deriving the issue's two figures (S7), `test_tmp_*`, deleted; the before/after counts of S6. Direction: hash moves on seven units, no verdict moves | S3, S5, S6, S7; `tests/test_a_reader_declares_its_input_class.py`; `evidence-check --strict .` exit 0 and `correction-check --range` exit 0 on the branch; the per-reader modules named in §*Technical context* green | |
| 3 | The record. `changelog.md`, `overview.md` (§*Not verified* with its rows or `none — <why>`), ledger fragment rows for the statement, the new test module and the two figures with their moment; `## Removes` rows read as gone by the records arm; any rider on a touched unit answered or re-stamped | `evidence-check --strict .` records arm over this directory; `tests/test_a_record_states_what_the_tree_has.py`; `unverified-check`; the hygiene modules a phase touched; the broad gate is the sealer's | |

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true, which is the failure the evidence ledger exists to prevent.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past one
— someone can open it — which is the same trick that lets a round record live
beside the contract rather than in tool state.

Fill it in as each phase closes, not at the end. A phase reconstructed
afterwards is reconstructed from the diff, which is where it already was.

What a phase discovers while it is being built, and needs the next phase to
know, does not fit in this table's cells. Write it to
`seal/specs/<work-item-id>/phases/phase-N.md`, from `templates/sdd-phase.md`,
when the phase closes.

One caveat, so nobody builds on it, and it has two halves. Where feature
branches squash, these commits stop resolving at the merge — and **a rebase
during the work does the same thing earlier and far more quietly**, because the
orphaned object still answers `git cat-file` in the worktree that wrote it.
The quiet half is the one that bites: this column was wrong on its own first
use, nine SHAs deep, and only a reviewer opening them found it. **Re-read the
column after any rebase**, or it names commits that resolve in one clone and
nowhere else. That is tolerable because nothing measures from this column.
The evidence ledger had the same problem and no such tolerance. It no longer
has it at all: a ledger row names a symbol and a content hash, so there is no
commit in it for a rebase to orphan.

## Seams with the sibling frames of 0.21.1

The other work items of milestone 59 are not read by this frame beyond their
ids; a sibling that touches one of the seven units touches a docstring this
work rewrites, and whichever lands second rebases on the other's docstring.
The census file is shared by every work item that declares a unit, and two
removals of different lines merge cleanly.

## Operational impact

- **What a user sees change.** Nothing a gate answers. Seven docstrings gain
  a line and a sentence; `docs/the-evidence-ledger.md` gains one statement;
  `skills/evidence-check/SKILL.md` gains one sentence. A user whose own
  ledger cites one of the seven units by hash sees that row drift once and
  repairs it with their own `--reverify`, the same way every docstring change
  to the checker has.
- **The vendored checker.** `tools/evidence_check.py` picks up the two
  docstrings at the next `/specseal:evidence-ci`, as every change to the
  checker does; nothing it decides moves.
- **No new dependency.** The table test reads the shipped modules by path,
  the way the per-reader modules already do.
- **Prompt budget.** Zero: no hook, gate or command asks anything it did not
  ask before.
- **Nothing to file.** Every candidate the issue named is decided in
  `spec.md` §*Scope* or in §*Alternatives considered* above; Q1 of
  1790260566 stays the owner's row in that file.
