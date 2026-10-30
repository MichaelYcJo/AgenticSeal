# Handoff: 1793273065-the-core-reaches-no-users-repository (#1177)

Written 2026-10-30 by the orchestrator, when the owner moved the work to
another session after phase 8's build commits. The branch is
`feat/1177-the-core-reaches-no-users-repository`, PR #1186, base
`release/v0.25.0`. Where the work stands is read from `frame/plan.md`'s
Status column, `gaps.md` and `trail/phases/`; this file holds only what
those do not.

## The first acts of the next session

1. Put question 1 through `AskUserQuestion`, alone, before the first spawn
   (`skills/implement/orchestration.md` *Question 1*: a run resumed in a new
   session). This session skipped it before the framer's spawn and put it
   before phase 5's.
2. Read this file, and delete it in the next commit you make, as
   `skills/implement/orchestration.md` *Orchestrator: the order inside a
   ticket* says.

## Where the run stands

- The frame was reframed after round 5 to A5, a plugin `SessionStart` hook
  (`85e61e11`), after the owner reversed `frame/questions.md` Q1
  (`346cd01d`). The owner's later decisions of 2026-10-30 are folded into
  `frame/design.md` *Scope* items 9 to 12 (`4d436388`, `445b4dd4`,
  `6ebfada5`, `7c783b64`, `2b1d7ce8`).
- Phases 5 to 7 are closed. Phase 8 is built and not closed:
  `02a34267`, `ac5eae67`, `769a1413` and `a5dbf0a2` are its commits, no
  `trail/phases/phase-8.md` exists, and its Status cell is empty. Phases 9
  and 10 are open.
- `trail/gate.md` and `guarantee.md` describe the A1 build at `3943873d`.
  They are stale, so PR #1186's checks fail on the pushed branch until the
  broad run and the seal are taken again.

## Phase 8: what closes it

- **The behaviour suites stopped after two agents (owner, 2026-10-30).**
  `evals/` holds both sides and the compare record for the framer and the
  sealer, old side at `6ebfada5` and new side at `769a1413`. The sealer's
  verdict is pass. The framer's is fail on rule 5 alone: tokens read rose
  from 7,070,907 to 8,367,258 and per call from 21,623.6 to 26,147.7, while
  the preload fell by 48 B and the spend from 26.74 to 26.37 USD; rules 1 to
  3 passed. The proofer's new side was stopped after 27 minutes and left no
  output. No crafter side ran.
- **The owner's grounds for not running the rest.** The phase changes prose
  and adds scope sentences; two runs per case catch gross breakage, not a
  shift in meaning; of 27 compare records in the history, 14 failed, most on
  rule 5 or on rule 3 read from one run (the history's own work item
  `1792363189-rule-3-decides-on-the-agent-not-one-run` was cut for the
  second). The proofer's reading of the diff, S12, judges meaning.
- **A fresh crafter closes the phase.** It writes `trail/phases/phase-8.md`
  from the four commits and the `evals/` records, fills the Status cell, and
  adds two `gaps.md` *Not verified* rows: S11 for the proofer and the
  crafter, not run by the owner's decision; and the framer side's rule 5
  result, diagnosed from the raw sides with no re-run.
- **The orchestrator adds one comment to #1038**, which decides whether the
  plugin needs verification beyond its commands and tests: whether
  `evals/README.md`'s rule that a preload rewrite is proved by the
  behaviour suite stays, with this phase's numbers and the history above.

## Left for later phases by the crafters' hand-backs

- Phase 9: `tests/skills/test_payload_meter.py#test_an_import_that_is_not_a_file_is_a_missing_row`
  still names A1's import path as its dangling import, and `README.md:267`
  is the `seal payload` row the phase rewrites.
- Phase 10: `gaps.md`'s *Not verified* row for `/agentic:preset-setup`, a
  command phase 7 deleted, its *Why this work exists* line and its *Not
  done* section still describe the `@` import.
- After the rounds settle: `.test_durations` still names case ids phase 7
  retired.

## For round 1

- The rounds count from 1 again, because the reframe is a design change
  (`docs/the-review-record.md` *The run*).
- Phase 8's two divergences are in `gaps.md`. The second, the routing
  sentence naming where its gate judges, closes a contradiction the scope
  sentence opened. The first removes the core's list of its source
  documents and keeps the citation of `skills/implement/SKILL.md` *1. Read
  the documents that outrank the code first*. The orchestrator flagged it:
  an agent that does not open that section no longer reads the order.
- The owner accepted the core's size after phase 8, a body of 6,059 B and a
  hook output near 6.2 KB, and chose not to tighten it further for size.
  The owner also chose that the hook prints the core in every session,
  with no detection of a `seal/` root, for stability over about 1,650
  tokens a session.

## The machine and the release

- The installed plugin is 0.24.2, so an agent spawned here receives no core
  through `skills:` and no session receives the hook's output. `CLAUDE.md`
  *The core* tells a session here to open the tree's core once.
- 0.25.0 ships #1177 alone. The owner cut 0.25.x into five releases on
  2026-10-30 by the rule the `release: 0.25.0` milestone description states,
  and #1148 starts only once 0.25.0 is installed.
- The framer's probes may have added an entry for a scratch project path to
  `~/.claude.json`; that file is the owner's to clean.
