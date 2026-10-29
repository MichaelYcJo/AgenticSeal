# Questions for the planner: 1793232075-the-living-text-still-calls-the-design-a-spec

## Answered by the tree, not to be reopened

- **The word is "design", written with its owner or as the path.** It is
  the file's name since 0.23.0 and the word `v0.23.1:seal/process/0.23.0.md`
  row 2 uses. `plan.md` *Alternatives considered* A1a to A1d weighs it
  against "the frame", the bare path and keeping "spec".
- **Checker vocabulary that stays: `<!-- specs/<work-item-id> -->` and the
  config key `Reference specs`.** `templates/setup/config.md` *What no row
  governs* lists the marker, and `hooks/lib/config.py#REFERENCE_ROW` reads
  the key. Neither names the design.
- **`spec` keeps its other meanings**: a policy document, a reference root,
  the methodology's name in "spec-driven" and SDD, and history.
  `frame/design.md` *The term* says how a reader tells each from the design.
- **Identifiers stay.** `CLAUDE.md` *The rule a mechanism is kept against*
  names an identifier renamed across files as `no work item` work (`plan.md`
  A2a).
- **`tests/` prose and `evals/` stay.** The issue's table counts no `tests/`
  path, and `evals/README.md` says a scaffold change asks the agent
  something its recorded runs never answered (`plan.md` A7a).
- **No census case reads a new agent name inside a longer word**, and none
  refuses the word `spec`. Both would read a word to guess a meaning, which
  `CLAUDE.md` calls a report (`plan.md` A3a and A4a). C5 reads this work's
  own risk of that class at each phase's close.
- **#1045's words stay**: `templates/records/sdd-gaps.md:11`, `:13`, `:15`
  and `skills/implement/SKILL.md:421`. The issue leaves them to #1045, which
  is open (read with `gh issue view 1045`).
- **#1040 and #1041, which the issue orders first, have merged** into
  `release/v0.24.0` as `5287dd42` (#1120) and `fdfb20d5` (#1137) (executed
  `git log`), so this branch builds on them.
- **The re-pointed guarantee case passes on the committed records.** Each
  of the 18 `guarantee.md` files under `seal/threads/` holds exactly one
  line that `chain_check.py#MEANT_VERDICT` matches (executed, a Python read
  of the pattern over each file at `884b6ba8`). No `pr.*.md` mirror stands
  under `seal/threads/` (executed `ls`), so the mirror case lists none.
- **The released records keep their words.** `seal/process/0.23.0.md` was
  removed by #1117 and is read at `v0.23.1`. Everything under
  `seal/threads/`, the replayed and seeded eval cases, and the history paths
  in `frame/design.md` *Occurrences kept, and why* are history
  (`tests/censuses.py#OLD_NAME_RECORDS`).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | #1020 has not merged into `release/v0.24.0` when phases 1 and 2 close. The tree cannot answer it: whether #1020 has merged is a fact of that moment, and phase 3 edits #1020's files (`CLAUDE.md`, `skills/code-review/`, `agents/proofer.md`), which this work item may not touch before then | the work | (a) Wait. The orchestrator holds phase 3, and the review rounds, until #1020 merges, then merges `release/v0.24.0` into this branch and spawns phase 3; one review run covers all three phases, and nothing of this work lands until #1020 does. (b) Split. The orchestrator takes phases 1 and 2 through review to the pull request, and files phase 3's rows as a new issue in `release: 0.24.0`, with the phase 3 rows of `frame/design.md` *Living occurrences this work rewrites* as its body; until that issue lands, #1020's files, the step-1 heading and the stage name still say "spec". (c) Edit #1020's files now: a merge conflict with #1020's build, which the spawn prompt forbids | (a) while #1020 is open in `release: 0.24.0`. (b) if the release's preparation pull request is opened before #1020 merges, so this work does not hold the release | open |
| Q2 | C1, C2 or C3 prints a line that neither table of `frame/design.md` *The class, enumerated* lists. The tree cannot answer it at framing: a merge from `release/v0.24.0` before phase 3, or #1020's own build, can add lines | the work | (a) The line names a work item's design or the closing memo: the phase that meets it rewrites it, as its file's row would. (b) It names something else: it stays, and the phase record names its kind from *Occurrences kept, and why*. (c) It fits neither: it stays, and the phase record says so for the review | (a) or (b) by *The term*; (c) recorded in the phase record | open |
