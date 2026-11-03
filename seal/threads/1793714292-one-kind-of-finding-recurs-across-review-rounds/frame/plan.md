# Implementation Plan: one kind of finding recurs across review rounds (#1020)

## Technical context

The work edits prose at three coordinates and no code:

- `docs/releasing/release-checklist.md:97-100`, the end of the flow-baseline step under *2b. Settle what earlier releases left behind*, held by `check: tests/github/test_finding_counts.py` at line 104.
- `docs/running/the-run.md:17`, the second paragraph of *The run*, held by `check: tests/behaviour/test_chain_hooks_hardening.py` at line 18. Lines 8 to 14, the first paragraph, keep the zero-finding round's statement.
- No case pins either sentence that goes (executed: `git grep -n -e 'counts toward nothing' -e 'is then the next step' -e 'files no other' -e 'Table B' -- . ':!seal/threads'` printed only the two documents' own lines).

The decision rests on text the work leaves as it stands: the signals row at `skills/code-review/orchestration.md:140` and the paragraph at `:155`, and the judgment rows each run writes into its own `frame/plan.md`.

**Failure scenario of the chosen approach.** In six months, a run meets a chain of three or more findings in shipped text, and its orchestrator writes no judgment row. A chain that spans a reframe also restarts the count, so it may reach no third finding round. No check refuses either run. It would surface after the release, in the flow-baseline count's `regression:` and `reopens:` column (`docs/releasing/release-checklist.md` *2b.*), and in the settle's reading of the judgment rows. That is a release later than a check would refuse it. The record shows no such run since `96c11614` (`frame/design.md` G9 and G10). A reframe is itself the structural question taken, which is why a chain across one is not counted as missed.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| The issue's check: a `class:` line on each recurring finding, a `recurrence` refusal in `chain_check.py`, and a refused `fixed` verdict where the line is missing | The check decides that two findings are one kind from their `regression:`, `reopens:` and `location:` lines, which is a reading of meaning made by a grammar (G2). On the nine recorded chains of three or more (G8 to G10), a judgment row took each chain's structural question, except on #1201's, which ran before the current paragraph (G9). #1287's loop carried different kinds, a parameter, a comment and a name, so a class line fits none of it. It costs a line on each of the 62 recurring findings of the two windows, and what its 0.24.0 build cost is G11 | rejected |
| The owner's candidate: one mediated exchange at a finding's first `reopens:` | It fires in 12 work items over the two windows. In 7 of them the reopened finding's chain ended at two findings with no exchange (#1210, #1211, #1237, #1250, #1278, #1303, and #1287's `round-2#2`); #1237's two, `round-2#2` and `round-3#5`, stood in its records alone. It never fires on a chain made only of `regression:` lines: #1241, #1252, #1276 and #1287's rounds 6 to 9. Where it would fire on a longer chain, a judgment row already stood at that round or the next (G8, G10), #1201's aside, which ran before the current paragraph (G9) | rejected |
| A recurrence reading that reports and blocks nothing, printed for the orchestrator before each fix pass | The orchestrator already reads the round record it spawns the fix pass from, which holds every `regression:` and `reopens:` line. `.github/scripts/finding_counts.py` already prints the same lines per work item at the settle. A third reader of one fact adds a script and its cases, and the record shows no chain it would have changed | rejected |
| One sentence in `skills/code-review/orchestration.md`: a chain of three findings owes a judgment row at whatever round it reaches | Every recorded chain of three that ran under the current paragraph reached its third finding round, where a row is owed, or had a row earlier (G9, G10). #1288 rewrites that section next in this release | rejected |
| Fold *The run* and the orchestrator's restatements of it, such as the regression route's table and the zero-finding round, into one home | This is the structure-replacing alternative. It cuts text that two readers open at different steps, the policy root's rule and the orchestrator's guidance, while #1288 and #1318 rewrite the orchestrator's half in this release. Two items rewriting one section in one release is the conflict `## Rule changes` exists to prevent | rejected for this work; *Scope* item 2 removes the one copy inside *The run* |
| Keep the judgment rows as the home of what a recurrence owes, and remove the sentences that stood on a check to come (chosen) | The premise that keeps it: every recorded chain of three or more but #1201's, which ran before `96c11614`, had judgment rows take its structural question (read, G8 and G9), and in each of G10's five a row stood at or before the chain's third finding (executed). If that premise fails, the failure scenario above says where it surfaces | chosen |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1, 2 and 3, and the work item's `changelog.md` | `frame/design.md` S1 to S5 | df433eee2 |

## Operational impact

No migration, environment variable, dependency or compatibility break.

The orchestrator owns these acts, after the seal:

- The pull request body carries `Closes #1020` and no `Closes #97` (`frame/design.md` *Scope* item 8).
- A comment on #97 names the two levers absorbed and the one left, each at its `frame/design.md` G12 coordinate, and names #1288 as the issue that owns the shape #97 measured.
- A comment on #1102 says that #1020 shipped no recurrence check, so the README rewrite describes none.
- The title's prefix is read from what the diff ships (`skills/commit-pr-convention/SKILL.md`). The issue is titled `feat:` for a step or a refusal, and this work adds neither.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-03 | `frame/design.md` G8 and G9 cite the squash commits on `main`, `569780eff` (#1257) and `783a7fe8a` (#1261), in place of the feature-branch commits `3937d861` and `1c1d18a5`; the orchestrator folds it before the first round, with no framer spawn | `trail/phases/phase-1.md` names both as on no branch and `tests/text/test_a_cited_commit_outlives_the_squash.py` refuses them; `git diff --quiet` of each cited path between the old and the new commit exited 0, and both new commits are ancestors of HEAD (executed by the orchestrator), so the fold changes a coordinate and no fact | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
| 2026-11-03 | `frame/design.md` *Scope* item 1's second and third sentences take the wording the round 1 fix pass gave the checklist at `d4697987e`: the issue names the file the lesson belongs in, and the cited row is quoted with "whose home"; the orchestrator folds it before the verifying round | the fix pass's hand-back names both sentences as contradicting its fix, and `agents/crafter.md` *Job* leaves `frame/design.md` to the orchestrator | `skills/code-review/orchestration.md` *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer* |
| 2026-11-03 | *Alternatives considered* row 2 counts 12 work items where the exchange fires, with #1237 among the 7 whose reopened chain ended at two findings; the orchestrator repairs the count with no framer spawn, and the row's verdict stands | `guarantee.md`'s withheld verdict at b98c6ddfa names #1237; at `refs/pull/1237/head`, `round-2.md:49` reopens `round-1#5` and `round-3.md:148` reopens `round-2#3`, `round-3.md` and `round-4.md` open no finding reopening either, and every `location:` of the four findings is under `seal/threads/` (executed by the orchestrator) | `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* |
