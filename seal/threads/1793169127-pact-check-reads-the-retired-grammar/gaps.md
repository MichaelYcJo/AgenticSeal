# Overview: 1793169127-pact-check-reads-the-retired-grammar

## Why this work exists

`seal pact` read two tables with grammars of its own, so a map line the
walk did not read vanished silently and a mistyped pact anchor needed a
second grammar to be named; both are now read by the one table walker, or
refused.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| A second map header the walk already refuses | `design.md` *Scope* item 1: "a second `\| Remote \| Path \|` header in the file, named at its line". The code names it in its own sentence only where the walk refused nothing; where the walk refused, its stray-row sentence names that line | The code | The walk's sentence already says "it and every row below it would go unread", so a second sentence would print one fault twice. `hooks/lib/config.py#read_table` takes the same course for the old pact header: it is "not added where the walk's stray-row refusal already names the old header" |
| When `coordinates.py#unescape` goes | `plan.md` phase 2: "`PACT_ANCHOR_RE`, `PACT_NAME`, `unescape`, … go". The code removes `unescape` in phase 3 | Phase 3 | After phase 2 its one caller was `resolve_unit`, which phase 3 removes; removing it in phase 2 would have meant editing a unit the next phase deletes. The end state is the frame's |
| Six resolver cases that pinned the heading rule | `design.md` *Removes*: "the cases of `tests/skills/test_coordinates.py` that call a removed unit" go. Six of them now ask `heading_path` directly, in *Test_heading_path*, with every value unchanged | The code | They were the only cases asking `heading_path` where a section ends, how a path narrows, and how a fenced or indented heading reads, and `pact_check.py#clause_hash` stands on each answer. Removed, those rules would have had nothing behind them. `design.md` S12 asks that the cases reading `heading_path` pass |

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the typecheck over this branch | executed by the orchestrator's broad gate at `0cd4d4ac` against `c825fd2c`, passed (`trail/gate.md`), and this repository declares no typecheck (`seal/config.md` *Broad gate*; #951 would add one) |

## Not done

nothing

## Fed back into the spec

- Inferred during implementation, and narrowed by rounds 1 and 2 of
  review: `seal pact` refuses at exit 2 every refusal the table walk
  returns for a signer frame's anchor table, except that the frame holds
  none, printed after `the frame`. A row the walk does not reach would
  read as a signer citing nothing. Another table below the anchor table is
  no such row: a line after the table's end that opens a table of its own,
  a header with a delimiter row of its width directly under it, is no
  refusal, whatever stands above it (`hooks/lib/config.py#gfm_table`'s
  `beside`, set by the anchor reader alone). The walk steps over that
  table, and a `| … |` line after it and before the next heading is still
  refused. A frame's section holds other tables, such as the policy table
  `templates/records/sdd-design.md` writes under `## Grounding`. A second
  anchor table is still refused, wherever it stands. `design.md` S8 names three row shapes and `plan.md`
  a second table; neither names the walk's own refusals.
  `docs/the-pact.md` *The pact anchor*'s `to:` text in `## Rule changes`
  does not say it either, so the settle may add it.
