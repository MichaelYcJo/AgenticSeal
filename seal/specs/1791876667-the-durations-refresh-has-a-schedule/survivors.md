# Survivors — the durations refresh has a schedule

`survivor-check --range origin/release/v0.22.0...HEAD` at 64e4b38e reported
six places that still carry wording this branch removed from
`CONTRIBUTING.md`, `docs/release-checklist.md` and the shard module's
docstring. All six stand. Five are the frames of shipped work items, which
record what those items built and are history rather than a rule anyone
follows; `settle --retire-process` takes them out after their release. The
sixth is a released ledger row in a frozen file, which phase 3 corrects with
a `Corrected ·` row in this item's fragment, as
`docs/the-evidence-ledger.md` §*A released row is read again in the
branch's fragment* says.

| Path | Quote | Grounds |
|---|---|---|
| `seal/specs/1791852613-the-test-durations-are-refreshed-and-say-when-next/plan.md` | `step after it with` | #874's plan for its one measuring run, shipped in 0.21.1. It describes that run, and the step it names is now every Windows shard's |
| `seal/specs/1791852613-the-test-durations-are-refreshed-and-say-when-next/plan.md` | `A release that skips it meets the case the next time the suite grows past a twentieth` | #874's plan, explaining the box this branch removes. History of 0.21.1 |
| `seal/specs/1791852613-the-test-durations-are-refreshed-and-say-when-next/plan.md` | `**The planned refresh is a box at every release's preparation**` | #874's plan, the same box |
| `seal/specs/1791852613-the-test-durations-are-refreshed-and-say-when-next/spec.md` | `Dead entries are not counted: the division never reads them, so they cost nothing but bytes.` | #874's frame. Its scenario shipped as written; this branch adds the seconds side, which its own `spec.md` S4 records |
| `seal/specs/1791384162-the-macos-test-leg-runs-in-shards/spec.md` | `in the refresh recipe, *because the matrix has no shards*` | #864's frame, naming a sentence of the recipe as it stood in 0.21.0 |
| `seal/releases/0.21.1.md` | `§Running the checks says the file is refreshed at each release's preparation` | A released row. `seal/config.md` declares `Ledger frozen from`, so the file never changes; phase 3 writes its `Corrected ·` row in `seal/ledger/1791876667-the-durations-refresh-has-a-schedule.md` (`spec.md` §*Data & interfaces*) |
