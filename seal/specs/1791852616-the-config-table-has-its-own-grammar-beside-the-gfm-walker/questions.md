# the config table is read by the walker cmark-gfm holds (#871) — questions for the planner

## Judgments the issue left open that the tree answered

Listed so nobody reopens one; the grounds are in `plan.md` §*Summary* and
§*Alternatives considered*, and the measurement in `spec.md` §*Data &
interfaces*. This run was pressed `automation`, so nothing below waits on a
person: the two decisions the issue left open are decided by the frame, with
the grounds where the owner can overturn them at the approval.

1. **The migration for installed configs the walker refuses is the
   refusal's remedy, and no file is rewritten.** Three shapes GitHub renders
   are refused — a non-blank line directly above the header — and the
   walker's own sentence names the edit, *leave a blank line above the
   header*. `seal.py#NEW_CONFIG` and `templates/config.md` already put the
   blank line there, so only a hand-written config can be refused, and once.
   A rewrite was weighed and rejected (`plan.md` §*Alternatives*).
2. **The prompt budget of a refusal that reaches a hook is zero.**
   `hooks/mode-gate.py#undeclared` reads `declared_mode`'s `"refused"`
   as answered and stays silent (#867, pinned by
   `test_a_mode_row_written_twice_is_silence_not_a_question` and
   `test_a_config_nobody_can_open_is_silence_not_a_deny`); the evidence
   advisor keeps naming the frozen repair. Commands exit 2 with the sentence.
3. **A refusal is per item, not whole-table** — a row the walk read is a
   value, an item it did not read is a refusal naming the stopping line —
   because that is the shape #867 gave a doubled row and because a row the
   walk read is a row GitHub shows.
4. **The three shapes the measurement shows GitHub rendering and the walker
   refusing (rows 1, 2, 11) stay refused**: a config header gets no
   exception to the rule PR #749 rounds 1 and 2 measured.
5. **The vendored twin follows the walker's table grammar on lines it can
   judge alone and refuses where it lacks block state**, never reading what
   the plugin refuses; it does not carry `hooks/blocks.py`.
6. **A hook prints no line on a refused table.** Weighed as the cheaper way
   for a person to hear before the sealer; rejected because a line from a
   `PreToolUse` hook is a change to what a person sees on every call, which
   #867 drew the line at. The owner is who can reopen it, and it costs
   nothing to reopen after this ships.
7. **`pact_check.py#path_map` keeps the retired grammar** for a different
   file; filed rather than widened (`plan.md` §*Operational impact*).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | What cmark-gfm renders for each shape `config_rows` reads today and `gfm_table` would answer differently | a measurement | the table in `spec.md` §*Data & interfaces*: 16 shapes, each with the renderer's cells, today's rows and the walker's answer | — | ✅ executed 2026-10-13 under `cmarkgfm==2025.10.22`, a probe importing the renderer and the standard library alone, deleted after |
| Q2 | Whether an installed config the walker refuses is migrated by a rewrite, by a refusal with its remedy, or by reading the shape anyway | a person, decided by the frame under `automation` | rewrite: a person's file is edited on a guess about block state; refusal: one stop, once, naming the line and the one-line edit; read anyway: a second grammar inside the walker for one header | refusal with the remedy (`plan.md` §*Summary* 1) | ✅ decided by the frame 2026-10-13; the owner overturns it at the approval by naming another row of the alternatives table |
| Q3 | The prompt budget of a refusal that reaches a hook | a person, decided by the frame under `automation` | zero, hooks silent as for an unreadable file; one line printed from the mode gate; a deny or an ask | zero (`plan.md` §*Summary* 2) | ✅ decided by the frame 2026-10-13, on #867's line; the owner overturns it the same way |
| Q4 | Which released ledger rows the stop rule's removal moves, and which take a `Corrected ·` row rather than a `Re-read ·` | the work | phase 4's `evidence-check --strict .` names each drifted or broken row; a row whose claim still holds under the walker is re-read, one whose claim was the stop rule is corrected | read, not executed, from `seal/releases/*.md` on 2026-10-13: 0.5.0's S8, 🟡 6 / 🟡 5 (the stop rule's own rows); 0.9.1's Q1; 0.12.0's three rows on the escape, the writer and the refusal; 0.12.1's R2 and R5; 0.15.3's F5, F6; 0.16.0's P3-1, P2-2; 0.18.2's two `Re-read ·` rows citing `config_rows@7b56abb5` and O1; 0.19.0's O1; 0.21.0's K1, K7, K8, K10 — about twenty citations, fewer distinct rows | ⬜ |
| Q5 | Whether `gfm_table` exposes the header's and delimiter's line indices for the writer, or the writer re-finds them through `table_cells` over `unfenced` | the work | expose: one more value from the walk, read by one caller; re-find: four lines in `seal.py` over the walker's own primitives, no grammar of its own either way | the builder's call in phase 2; `spec.md` §*Data & interfaces* names both and forbids a third grammar | ⬜ |
| Q6 | Whether any shape in the oracle's enumerated corpus, run with the config header, yields rows the walker reads and cmark-gfm does not render | a measurement | none: S1 holds for the config header as for the three pact headers; one: the walker gains a refusal for it, with the oracle's answer as the ground | the corpus is header-agnostic by construction, so none is expected; phase 1's pass executes it | ⬜ |
| Q7 | Whether a pact line written `\| … \|` below a config table whose walk read no `Ledger frozen from` row above it stops `evidence-check --reverify` on the freeze row at exit 2, as S2 makes every unread item a refusal, or still reaches the pact reader's `LEFT` line at exit 1, as S6 of work item 1791128260 pinned | a person | exit 2: one rule for every item, the run judges nothing and writes nothing, the sentence names the table line; exit 1: the freeze row read as absent past a refused table for this one command, which is the silent default #415 was opened about | exit 2, the spec's rule; ten cases of `tests/test_a_signer_records_a_pact_change.py` re-pinned to it in round 2's fix pass (`overview.md`) | ⬜ |

**`Who can answer` takes one of three values and nothing else.** They were one
shape on the page before this, and #84's second comment measured all three
inside a single run's four rows.

- **a person** — what the product should be, or a value somebody has to be
  accountable for. This is the file's stated purpose, and the only kind of row
  that blocks the build.
- **a measurement** — a probe, a command or a count settles it, so asking a
  person is the wrong instrument and queueing it behind one wastes a round
  trip. Measured: six probes at about three seconds each answered a row that
  had been written into the human batch, and they showed the ticket's own
  instruction was wrong.
- **the work** — unknowable at framing time. The phase that meets it decides
  it there and records a divergence row; it does not travel back to the
  framer, which would spend the interruption the framing phase exists to spend
  once.

**The framer opens rows and does not own their answers.** A row is a question
put to somebody else, so opening one costs little and closes nothing — and the
`Status` column is ticked by whoever answered, never by whoever asked. Q2 and
Q3 are the exception this run's `automation` answer makes: a frame that could
ask nobody decided them, said so in the cell, and left the owner the
approval as the place to overturn either.

Answered rows feed back into docs/ (policy clause or open-questions section)
before this directory's work merges.
