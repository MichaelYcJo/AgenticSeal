# Questions for the planner: a release branch requires its checks (#457)

The ticket left these judgments open, and the tree or a probe answered each. They are not reopened here:

- Which checks `release/**` requires: `lint` and `release`. See `plan.md` *Alternatives considered* rows 2 to 4, and `frame/design.md` *Grounding* G4, G5 and G9.
- What an override looks like: there is none. See `plan.md` *Alternatives considered* row 7.
- Whether a branch must be up to date before it merges: no. See `frame/design.md` *Grounding* G8, and `plan.md` row 5.
- Whether the checks hold where a release branch is created: no. See `frame/design.md` *Grounding* G7, and `plan.md` row 6.
- Which sentences state it, and whether the settle writes them: `docs/releasing/branch-and-release.md` *Work accumulates on a release branch* and `docs/releasing/release-checklist.md` *0. Before starting*, edited directly. See `frame/design.md` *Grounding* G1, G2, G11 and G12, and `plan.md` row 8.
- Whether the ticket's `CLAUDE.md` claim and `ledger` job still need work: neither is in the tree. See `frame/design.md` *Grounding* G2.

No row is open. The one behaviour no probe here could reach is whether GitHub would refuse a branch's creation with `do_not_enforce_on_create` `false`. The setting is `true` whatever the answer, so it stands as an assumption in `frame/design.md` *Grounding* G7 and is not a row.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
