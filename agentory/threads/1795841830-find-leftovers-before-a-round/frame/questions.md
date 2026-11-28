# Questions for the planner: 1795841830-find-leftovers-before-a-round

The issue left these judgments open, and the tree answered each; the grounds stand where each line points.

- Which searches take a keep file: every search that keeps a line, not a rename's alone (`frame/plan.md` *Alternatives considered*, the row of the keep file for a rename's search alone).
- What a keep file is named: `frame/keep-<N>.txt` for every phase, with no special name for the last (`frame/plan.md` *Alternatives considered*, the row of #1658's names).
- Who edits a keep file during the build: the builder, following the kinds the design keeps and adding none (`frame/plan.md` *Alternatives considered*, the row of the framer alone editing it).
- Whether paths are searched: yes, by `git ls-files` into `frame/keep-<N>-paths.txt` (`frame/plan.md` *Alternatives considered*, the row of leaving paths out; `frame/design.md` *Grounding* G8).
- Which flags the content command carries: `--no-color --no-line-number` (`frame/design.md` *Grounding* G7).
- Where a keep file stands against `Document token ceiling`: outside it, since `diff` compares it and `agentic range` prints the lines a range changes in it (`frame/design.md` *Grounding* G5, G19 and G24, and its `## Rule changes`).
- How the builder's range file prints a keep file: by its changed lines, at their own lines (`frame/plan.md` *Alternatives considered*, the row of `agentic range` and a keep file's hunks).
- Whether a built-app suite joins a phase whose source change it exercises: only where the phase changes that suite's test file (`frame/design.md` *Grounding* G11).
- Whether this repository's eval harness is a suite a phase here owes: no (`frame/design.md` *Grounding* G12).
- What a split weighs beyond the issue's finding rounds: every round's read of the frame and the records (`frame/design.md` *Grounding* G14).
- How the issue's measurement is kept: one row of `agentory/follow-up.md` (`frame/design.md` *Grounding* G20, and *Scope* item 10).
- Whether this item carries the version move: no (`frame/plan.md` *Operational impact*).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Which test files outside `tests/text/` and `tests/behaviour/` open a file a phase changes, and so join its *Phase boundary* set | the work | A file whose cases open, import or load the changed file joins the set; a file that writes its name only into a fixture, a parameter or a docstring does not (`skills/verify/SKILL.md` *Scope: cheap and often, broad and once*). The framer could not settle it: a `git grep` of the changed files' names lists fifteen such test files at `bbb66b38` (`executed`), and only reading each case tells an open from a fixture, which the phase does once its diff is known | the crafter reads each file that `git grep` lists for a changed file's name, runs those whose cases open it, and names them in the phase record | answered 2026-11-28 by the work: phase 1 decided it in `trail/phases/phase-1.md` (*`frame/questions.md` Q1, decided by the work*), naming `tests/lib/test_gaps.py` alone |
| Q2 | Whether `frame/design.md`'s `## Rule changes` parses whole as `skills/settle/scripts/rule_changes.py` reads it | a measurement | Parsed whole, the settle reads its operations; refused at a line, the design joins no group and the settle reads it whole (`skills/settle/rule-changes.md` *Rule changes*). The framer runs none of the repository's checks, and `chain-check` asks that reader at the pull request | the block stands as written; the proofer, or `chain-check` at the pull request, answers | open |
