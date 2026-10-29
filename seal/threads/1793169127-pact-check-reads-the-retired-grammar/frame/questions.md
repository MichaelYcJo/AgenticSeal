# Questions for the planner: 1793169127-pact-check-reads-the-retired-grammar

**What issue #913 left open, and the tree answered.** Nobody reopens these;
the grounds are in `design.md` *Scope* and `plan.md` *Alternatives
considered*.

- **The map is read by `gfm_table` with its own header, `("Remote", "Path")`.**
  It is a GFM table under a header, the shape the walker exists for, and a
  second reader is how the first walker failed (`plan.md` A1 to A3).
- **A refusal of the machine-local map prints
  `REFUSED ~/.claude/agentic/pact-paths.md — the map <sentence>`, at exit 2.**
  The pact's own refusals read after the words `the pact` in the same
  shape, and the map's docstring already says a map that is there and will
  not read is a refusal (`design.md` *Scope* item 1).
- **The pact anchor's `:`, `/`, quotes and `@` are syntax a reader trips
  on; the anchor becomes a row of the anchor table.** The tree's own record
  of fifteen mistyped shapes and four review findings is the evidence
  (`plan.md` A4 to A6).
- **The anchor names the pact by its origin URL, not its last segment.**
  One meaning for *Pact* in a signer's two files, and the name's refusals
  go with the token they served (`plan.md` A7, A8).
- **The `#` of `path#unit` is a spelling every reader agrees on, and
  `templates/records/sdd-design.md`'s `## Removes` hint stays.** No shipped
  script reads it as grammar (`plan.md` A12, A13).
- **The `>` needs nothing.** It was the ledger's, which left with #944, and
  no live text holds it (`design.md` *Scope* item 2).
- **`templates/setup/pact.md`'s comment stays and states the table.** It is
  the only guidance in a consuming repository (`plan.md` A16, A17).
- **`coordinates.py`'s unit resolver and the census of the coordinate's
  hash go.** No caller since #944 (`plan.md` A14, A15).
- **`templates/records/sdd-design.md` carries no anchor table.** A pact is
  rare (`design.md` *Scope*, *Out, and whose*).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | What does `seal pact` do with an inline anchor, `pact:<name>/"<heading path>"@<hash>`, in a signer's frame after the upgrade? **Why the tree cannot answer:** the token is written in other repositories' trees, so the choice decides whether a consuming repository's in-flight work item is refused after it upgrades the plugin, and how long this repository keeps a grammar for them; that compatibility is the owner's to accept, as #1005's Q2 left the migration to the owner | a person | (a) **Refused**: every `pact:` token outside a closed fence is refused at its line, at exit 2, naming the anchor table's row to write. One pattern replaces the near-miss grammar, and phase 2 removes the old grammar whole. A signer with an in-flight frame rewrites one line per anchor; `seal pact` runs in no CI, so nothing automated stops. (b) **Graded for one release**: the old token is graded as before and `seal pact` prints a line naming the row to write, in no exit class, as it does for a pact headed `Signatory`. `PACT_ANCHOR_RE`, `PACT_MENTION_RE`, `near_miss` and their cases stay, and a later item the owner opens removes them. (c) **No change to the anchor**: the inline grammar is kept as a spelling, and phase 2 builds only *Scope* item 4's sentences; the anchor table, the URL in place of the name, and *Scope* item 5 are not built, and the near-miss reader stays | (a). Phase 2 is built on it, `design.md` *Rule changes* states it, and the pull request body names it | open |
| Q2 | Phase 2 edits `tests/conftest.py`, which #1058 also edits in parallel. **Why the tree cannot answer now:** which branch merges first is known only at the merge | the work | Phase 2 edits only the pact world, `tests/conftest.py:1420` to `:1515` at `977b6613` (`URL`, `ORDERS`, `LOCATOR`, `grounding_row`, `World.cite`), and nothing near #1058's fixtures at `:514` to `:536`; the branch that merges second rebases onto the first and re-runs the modules phase 2 names | That edit, in that block alone; the phase record names the lines it changed | open |
