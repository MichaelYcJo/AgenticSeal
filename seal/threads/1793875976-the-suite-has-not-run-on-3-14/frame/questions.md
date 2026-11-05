# Questions for the planner: the suite runs on Python 3.14 (#1065)

The ticket and the spawn left these judgments open, and the tree answered each one. Each line points at where its grounds are, so nobody reopens them:

- Where 3.14 runs: one more `pytest` matrix entry, on every event the workflow runs on. `plan.md` *Alternatives considered*, A against B, C, D.
- On which system: ubuntu alone. `plan.md` *Alternatives considered*, F.
- How `.test_durations` splitting interacts with it: it does not, because the entry carries no `split` and no `store`. `frame/design.md` G7, and `plan.md` *Alternatives considered*, J.
- What the first run is expected to find, and how a red is handled: `frame/design.md` G12 and G10, and Scope 5.
- Whether 3.13 keeps a leg: no. `plan.md` *Alternatives considered*, G.
- Whether the leg blocks, floats, or is required: it blocks, is pinned, and is not required. `plan.md` *Alternatives considered*, E and H, and `frame/design.md` G11.
- The leg's `timeout`: ubuntu's 15. `frame/design.md` Scope 1.
- The release table: the new leg gets its own row. `plan.md` *Alternatives considered*, K and L.
- Whether a case requires the 3.14 entry: no. `plan.md` *Alternatives considered*, M.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Should the newer-Python leg run 3.14, as milestone #89 names it, or 3.15? Python 3.15.2 is a stable release in `actions/python-versions` and `python3` on the owner's machine is 3.15.0 (both executed 2026-11-05). The milestone's sentence names 3.14, and whether CI follows the newest Python is a choice about what this repository promises its users, which no document of the tree states. So the tree cannot settle it and no probe can | a person | 3.14 as named: closes `#1065` as written. Nothing runs 3.15, so a 3.15-only defect is found by a user, as #684 was on 3.14. 3.15 in place of 3.14: covers the newest release, and 3.12 and 3.15 bracket 3.14. `cmarkgfm==2025.10.22` has no `cp315` wheel (executed: PyPI), so each run builds it from source, and #1065's own record would then be about 3.15 rather than 3.14. Both: one more ubuntu job of about 2 minutes per run. Each option changes one matrix entry's `python` value or adds one entry, and with it the two `test.yml` comments and `CONTRIBUTING.md`'s sentence that name the version | 3.14, as the owner named it. Changing it later is the matrix entry, the two `test.yml` comments and `CONTRIBUTING.md`'s sentence that name the version, and the release report's row follows by itself | open |
| Q2 | What does the whole suite do on 3.14: which cases fail, which skip, and in how many minutes? A framer runs no test module (`skills/agent-contract/SKILL.md` contract rule 2), and the first run on CI is the record the issue asks for | a measurement | Green: phase 3 records the run and closes the issue. Red: phase 3 repairs each red in this work item and records both runs (`frame/design.md` Scope 5) | Phase 3's dispatched run answers it | answered 2026-11-05 by crafter (phase 3, `trail/phases/phase-3.md`): run 42019408766 at `b1669859`, whose 3.14 job concluded `success` in 1 m 44 s with 6208 passed, none failed and 10 skipped |
