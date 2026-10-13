### Fixed

- **A line under a frame's `## Removes` that is neither a row nor a
  `nothing — <why>` line is refused, naming it (#905).** Before, the records
  arm of `evidence-check` dropped such a line without a word. A removal
  written as a bullet was therefore a claim of absence that nobody read, and
  the four `Reads:` lines that hand the section's reading on said `unknown
  refused` where it passed.

  1. Each such line is now `REFUSED` at its own line, required or not,
     beside a row or alone. The refusal says the section holds table rows or
     one `nothing — <why>` line, and that prose about the rows goes under a
     sub-heading after the table, such as `### Why these rows`.
  2. The section now ends at the next heading of any level. A sub-heading's
     lines are read as the rest of the frame is, so a unit the work removes,
     named there in backticks, needs `NAME NOT IN TREE` on its line. A table
     row under that sub-heading is refused naming it, because only the table
     above it is read as removals.
  3. The marker exempts no line of the section itself. Before, a line under
     `## Removes` carrying it was skipped, so a marked bullet passed and a
     marked row naming a unit that still stands was never read.
  4. A required section that is empty is refused as before, in the same
     words.

- **Two sentences that said something untrue are corrected (#905).**
  `docs/the-reader-registry.md` named the warden as the reader of a stale
  helper `Reads:` line that, by its own account, the warden's diff does not
  show. It now says the warden opens a helper's line where the diff changes
  its caller, and `agents/warden.md` tells the warden to. The broad gate's
  pytest recorder called a record it cannot write *the strict side*. Since
  #836 the gate reads a missing record as not measured where the suite
  failed and as existence alone on the ledger arm, so a run whose suite
  passed still seals.
