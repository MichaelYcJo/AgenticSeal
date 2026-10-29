# Implementation Plan: 1793251203-seal-pact-passes-near-misses-of-an-anchor

Approved 2026-10-29 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phases 1 and 2.

## Summary

`seal pact` reads a near miss of an anchor as no anchor. Two readings close
the anchor table's class by facts rather than spellings. A row naming a
remote the signer does not declare is refused. A row outside the anchor
table that names a declared remote and a clause is refused, whatever header
it stands under. The inline token is matched in any case, and the one
spelling prose also writes, a space beside the colon, is stated as a limit.
All of it is in `skills/verify/scripts/pact_check.py` and its test module.
Two phases, in order.

## Technical context

**What this builds on, by coordinate (read at `28edee12`).**

- `pact_check.py#check` (`:524`). Per signer, `declared_pacts` gives
  `pacts` as `[(as written, normalised)]` (`:636`), and `check` goes on
  only where one of them is this pact (`:639`). Per frame, `first_table`
  (`:658`) reads the anchor table with `beside=True`, a refusal starting
  `holds no ` is dropped (`:659` to `:661`), and each row is judged:
  `one_remote` (`:666`), then `named != ours` passes the row over (`:670`),
  then `heading_parts` and the hash shape. Then `INLINE_TOKEN` is searched
  over `checker.unquoted(body)` (`:683` to `:686`).
- `pact_check.py#first_table` (`:267`) returns `(rows, refusals)`, where
  each row is `(line number, cells)`. Phase 1's scan excludes those line
  numbers.
- `hooks/lib/config.py#unfenced` (`:239`) yields `(index, line)` for the
  lines a fence or a comment block does not hide; `first_table` already
  walks it for its second-header scan (`:282`). `config.table_cells`
  (`:949`) needs a line written `| … |`.
- `tests/conftest.py:1299` to `:1440`, the pact world: `PACT_URL`,
  `SIGNER_URL`, `signer_config`, `anchor_table`, `World.cite` and
  `World.run`. `world.web`'s `seal/config.md` declares `PACT_URL` alone.
- `tests/skills/test_pact_check.py#Test_check`:
  `test_accepts_a_signer_citing_the_current_clause` (`:527`) holds rows
  naming `git@example.com:org/billing.git` and
  `https://example.com/org/orders-api-legacy`, neither declared, and pins
  that both pass. `test_refuses_a_row_it_cannot_grade_at_its_line` (`:707`)
  and `test_refuses_the_inline_anchor_naming_the_row_to_write` (`:723`)
  are the cases S1 and S6 extend.

**The failure scenario of the chosen approach, six months on.** A signer's
frame holds a table that lists repositories with a remote and the heading of
a policy section in one row, say a migration table, and `seal pact` refuses
it at exit 2 as an anchor nobody reads. The remedy is one edit, a code span
around the URL, which the scan does not read. The probe found no such row in
this repository at four revisions, and this repository signs no pact, so the
cost is unmeasured in a signer. Second: a frame writes the label
`**Pact:** the orders pact`, which the case-folded token refuses, as the
case-sensitive token already refuses `**pact:**`; the remedy is
`**Pact**:`. The probe found no such label at four revisions. Third: a row
that misses twice is passed over, as `## Rule changes` states.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. A header near miss is refused at the header's line by a list of spellings: case, emphasis, code spans, plural | Every spelling outside the list passes in silence. The probe found five such shapes the issue did not list (d12 reordered, d13 an extra column, d14 no outer pipes, d26 `Clauses`, d24 no header at all). Each new one is another branch, which is how #913 plan A4 describes the near-miss grammar it removed | Not taken |
| A2. The settle precedent: a header whose letters, case folded, are those of `Pact`, `Clause`, `Hash` is refused | Catches d07, d09 and d15, and misses d08 `Hashes`, which the issue names, with d12, d13, d14, d24 and d26. The precedent calls other letters another section, which here is another anchor nobody reads | Not taken |
| A3. A row outside the anchor table that names a declared remote in one cell and a heading path in another is refused at its line | It reads the row, so every header spelling the probe found is one case. It refuses a non-anchor table row of that shape, which the probe found nowhere here (*Technical context*). A row that misses twice passes, stated as a limit | **Taken** |
| A4. No header at all: any row naming a declared remote is graded as an anchor (replaces the structure) | The premise the header keeps is that `gfm_table` reads the table as GitHub renders it, and judges a second table, a stray row and a row of another width (#913 plan A1, A6). A header-free scan is a second grammar beside the walker. It also grades a near miss as if it were right, so a misspelt header is accepted forever instead of corrected | Not taken |
| A5. A `Pact` cell close to the pact's remote, by edit distance, is refused | A threshold is a guess from words. `pakt` against `pact` is one letter, and so is `org/a` against `org/b`, two real repositories. `CLAUDE.md` makes such a reading a report, not a gate | Not taken |
| A6. A row naming a remote the signer does not declare is refused at its line | Premise of the old pass checked: *another pact's row is that pact's to grade* holds only where the signer declares that pact, because otherwise that pact's `seal pact` reports the signer `ONE-SIDED` and reads none of its frames (`pact_check.py:639` to `:649`). So an undeclared row was graded by nobody. The cost is a frame in a signer citing a pact it does not declare, which is a one-sided relationship either way | **Taken** |
| A7. A row naming another remote is printed in no exit class | A typo prints one line and the exit is decided by the other signers alone, which is the silence #1132 reports. `docs/the-record-layout.md` wants a held anchor's wrong answer loud | Not taken |
| A8. `INLINE_TOKEN` takes `re.IGNORECASE` | `**Pact:**` as a label is refused (*Technical context*). Measured: no line at `HEAD`, `v0.22.0`, `v0.23.0` or `v0.24.0` matches the case-folded token that the exact one misses, except lines quoting R24 | **Taken** |
| A9. The token also allows spaces beside the colon | Measured: 6 more lines at `v0.22.0`, 1 at `v0.23.0` and 4 at `HEAD`, all prose. Each would be refused at exit 2 in a signer's frame | Not taken; stated as a limit |
| A10. No change to the token, and a limit sentence for all three spellings | A `PACT:` leftover reads as a signer citing nothing, for a one-flag change that measured no false positive | Not taken |
| A11. The row scan runs whether or not the walk refused | d06's row is refused twice, once by the walk and once by the scan, for one defect | Not taken: the scan runs where the walk refused nothing |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The anchor table's near misses (`frame/design.md` *Scope* items 1, 2 and 5): in `check`, a row whose `Pact` cell matches no declared remote is refused at its line; where the walk refused nothing, every line `config.unfenced` shows that is not a walked row, split by `config.table_cells` with outer pipes given where missing, is refused at its line when one cell is one remote URL matching a declared remote and another opens with a heading; two new sentences; the module docstring *What each frame is read for* and *Exit codes* rewritten; `test_accepts_a_signer_citing_the_current_clause` declares the remotes its rows name and gains the repositories table (S2, S4) | `tests/skills/test_pact_check.py`, `tests/behaviour/test_one_word_one_meaning.py`, `tests/behaviour/test_a_signer_declares_its_pact.py`, in one command; S1, S3 and S5 cases each seen red against `28edee12`; each new sentence pinned (contract rule 14) | ce323fe9 |
| 2 | The inline token (*Scope* items 3, 4 and 5): `INLINE_TOKEN` with `re.IGNORECASE`, its comment stating the case fold and the space limit, and the docstring's sentence on the token | the same three modules in one command; S6's new ids seen red against `28edee12`; S7's spellings in the passes case | 063644e5 |

Each phase runs the modules it names and no broad run: the full suite, the
repository-wide lint and the typecheck are the orchestrator's one broad gate
after the review rounds settle (contract rule 2).

## Operational impact

- **`seal pact` refuses more, at exit 2**, in a signer's frame: a row naming
  a remote the signer does not declare, a row naming a declared remote and
  a clause outside the anchor table, and a `PACT:` or `Pact:` token. Each
  was passed in silence. `seal pact` runs in no CI, so no pull request and
  no hook changes verdict. The changelog fragment names the three shapes.
- No question is put to a person: every refusal is printed and answered by
  an edit.
- No new dependency, no environment variable, no migration. No function
  changes its signature, and `hooks/lib/config.py` is not edited.
