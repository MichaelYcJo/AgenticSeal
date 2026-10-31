# Questions for the planner: 1793343707-each-document-serves-one-reader

The judgments the issue left open that the tree, the policy or a probe
answered, each in one line naming where its grounds stand, so nobody
reopens them.

- **Does a record restatement block?** No record is removed whole, and a
  restatement is answered by removing the copy; which record lines are
  findings is `frame/design.md` *Scope* item 5 and the `## Rule changes`
  item on *The round record*.
- **Which record goes whole?** None: `frame/plan.md` A2 and A3.
- **`gaps.md`'s writer, trigger and test.** The first phase writes it;
  `frame/plan.md` A6a to A6c.
- **The three-fix rule's home.** `skills/implement/SKILL.md` *2.*, with the
  crafter's application; not the core: `frame/plan.md` A7a to A7c.
- **A fix touching only the records.** No verifying round; the sealer reads
  it: `frame/plan.md` A8a to A8c.
- **The pull request body's shape.** The orchestrator's part first, the
  records in one fold: `frame/plan.md` A9a to A9d; the boundary line reads
  `## From the records`: `frame/design.md` *Data & interfaces*.
- **The acts table and the multi-repository section.** Moved, not deleted:
  `frame/plan.md` A10a, A10b and A11.
- **Where the routing rows' reasoning goes.** The policy root, through
  `## Rule changes`: `frame/plan.md` A12a to A12d.
- **`## Open questions` and `## Summary`.** Nothing in code reads either
  (executed, `frame/design.md` *Removes*); both go.
- **`severity:` and `Seal-Routing:`.** Kept, each with its reader:
  `frame/design.md` Table C and `frame/plan.md` A14a and A14c. The
  trailer's record is 24 failed hygiene runs with no refusal (executed), so
  the tree answers "not weighable yet"; the settle after 0.25.x weighs it.
- **`Approved`.** Removed after phase 1: nothing in code reads it and its
  whole history in the round records is findings about its own shape
  (executed); `frame/design.md` Table C and `frame/plan.md` A14b. This work
  item's own `plan.md` keeps its line as history under the old rule.
- **A check for the direction of references.** Not built: `frame/plan.md`
  A13; the proofer runs the `git grep` the new rule names.
- **The guarantee's `## The parties` table.** Unchanged: `frame/plan.md`
  A16.
- **`gaps.md`'s name.** Kept: `frame/plan.md` A15.
- **"Removes more lines than it adds".** Read outside `seal/threads/`,
  since this frame alone adds several hundred lines there: `frame/design.md`
  *Scope* item 11, verified in phase 6.
- **The measure.** Four counts per work item at this repository's settle,
  posted to the `flow-baseline` issue; its home after round 3 is
  `docs/release-checklist.md` *2b*, not the plugin's settle procedure:
  `frame/design.md` *Scope* item 7 and `frame/plan.md` A20a to A20c. The
  commands and #1177's reading, 10, 3, 1 and 8, are `frame/design.md`
  *Data & interfaces*.
- **Where a paste-ready fix is read before it is applied.** The fix pass,
  in `agents/crafter.md`: `frame/design.md` *Scope* item 13 and
  `frame/plan.md` A21a to A21c.
- **#1045's other half.** The settle's fourth kind of row is a settle rule
  and stays on its issue: `frame/design.md` *Scope*, out.
- **The version.** This pull request is the first into `release/v0.25.1`,
  so phase 6 moves `.claude-plugin/plugin.json` in the fragment's commit
  (`skills/implement/orchestration.md` *Which branch the pull request lands
  on*).
- **Posting the records' table on the issue.** The orchestrator's act, after
  the frame is committed; an agent posts nothing (contract rule 6).
- **GitHub's rendering of `<details>` with a blank line after `<summary>`.**
  The owner's statement, which no probe here can render; the orchestrator
  reads the first body this change writes, and phase 6 writes the
  `## Not verified` row.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Is the behaviour suite (`evals/scripts/noninferiority.py run` on both sides, then `compare`) run for the four agent definitions this work changes (`agents/framer.md` gains a rule, `agents/crafter.md` loses a rule's statement, `agents/proofer.md` loses a citation, `agents/sealer.md` rewords two steps)? `evals/README.md` *The behaviour suite* says a preload rewrite is proved not worse by it; the tree cannot say whether it applies to a change of this size, and no probe can: the suite is a paid run of twelve to twenty-four agent sessions per agent, which the owner decided against for #1177's phase 8 on 2026-10-30 on the grounds that two runs per case catch gross breakage and not a shift in meaning (`seal/threads/1793273065-the-core-reaches-no-users-repository/gaps.md`, the S11 rows) | a person: the owner | **Run it**: one more phase after phase 5, four agents on both sides at the merge base and HEAD, each record under this work item's `evals/`, several hours and the tokens of the runs; a `fail` on rule 5 alone, as #1177's framer side gave on cache reads, would need the owner to read the record. **Do not run it**: the proofer reads each changed sentence against the rule it moves or states, in the shape #1177's S12 took, and the rounds hold the definitions as they hold any shipped text | not run; the proofer's reading at stage 1 stands in for it, on the owner's 2026-10-30 grounds; the owner overturns this at the pull request by asking for the phase | open |
| Q2 | The issue's last *Done when* reads "the change removes more lines than it adds", and `frame/design.md` S10 reads it outside `seal/threads/`. At `16056d31` the diff outside `seal/threads/` adds 1,128 lines and removes 988 (executed by round 1, `git diff --shortstat fba13ab2...HEAD -- . ':(exclude)seal/threads'`); the shipped files outside `tests/` net 80 fewer lines (567 added, 647 removed), and `tests/` nets 220 more (561 added, 341 removed), `tests/behaviour/test_waiver_decided_at_start.py` alone 133 more. Does the shortfall stand, or does a phase cut it? The tree cannot answer it: the criterion is the owner's, no policy says when it may fail, and which pins to cut is a product judgment, not a measurement | a person: the owner | **Accept the shortfall**: S10 stays as written and fails, round 1's finding 6 closes `deferred frame/questions.md Q2`, and the orchestrator's part of the pull request body states the three counts, so the owner reads a miss and not a pass. **Cut 141 or more lines outside `seal/threads/`**: one more phase after the fix pass, trimming the phrase-only cases this work added where #1146's reading would cut them, the candidates being the new cases of `tests/behaviour/test_waiver_decided_at_start.py` and `tests/text/test_the_rules_have_one_owner.py`, each removal weighed against contract rule 14, then a verifying round, the broad run and the sealer again | accept; the pull request body states the counts, and S10 is not rewritten to pass | open |
