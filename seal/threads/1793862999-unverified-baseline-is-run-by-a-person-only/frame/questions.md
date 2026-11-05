# Questions for the planner: `seal unverified --baseline` leaves (#1240)

The tree settled these judgments, which the ticket left open:

- Which `docs/` sentences change, and how they change: design `## Rule changes`, and plan *Alternatives considered* row 7.
- Whether the predicates that `chain_check.py` uses stay in `unverified_check.py`: plan *Alternatives considered* row 3.
- Whether the plain run's exit-0 states stay: plan *Alternatives considered* row 4.
- How `overviews` reads an argument once the base is gone: plan *Alternatives considered* row 5, and design *Grounding*, the row on how the scan read its arguments before #1225.
- What happens to the seeded eval `seeded-55b66958`: plan *Alternatives considered* row 6.
- Whether the relaxed reading of a record at a ref stays: plan *Alternatives considered* row 8.
- Where the marker `a-settle-is-no-deletion` goes: design *Grounding*, the markers row, and design *Scope* item 6.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does any kept plain-run case of `tests/skills/test_unverified_check.py` assert a path that `overviews` used to give as named and now gives as its real path? The answer comes only from running the cases, and the framer runs no test module of the repository. | the work | None found: phase 1 changes no plain-run assertion. One found: the phase decides whether the assertion pinned a reading the base needed, in which case it goes, or one the plain run needs. Under the second answer, `overviews` keeps that reading for that shape alone, and the phase record says why. | `overviews` reads each argument at its real path (design *Scope* item 3) | answered 2026-11-05 by the crafter: none found. All 302 cases of `tests/skills/test_unverified_check.py` pass with `overviews` reading `os.path.realpath`, so `overviews` reads each argument at its real path (`trail/phases/phase-1.md` *What this phase found*, the paragraph opening "Q1 is answered") |
