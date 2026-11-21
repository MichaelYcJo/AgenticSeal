# Guarantee: 1795276650-the-batch-spans-every-issue-of-the-request

The audit read the tree at `fe04a0bb4` against the base `release/v0.38.4`,
which `release/v0.38.4@{upstream}`, `origin/release/v0.38.4` and
`release/v0.38.4` each resolve to `f8056edde` (executed, `git rev-parse
--verify --quiet`). `trail/gate.md` names `run: daf926515 against
f8056edde`. `daf926515` is an ancestor of HEAD, and `git log --no-merges
--name-only daf926515..HEAD ^f8056edde` lists one commit, `fe04a0bb4`, which
touches `seal/threads/1795276650-the-batch-spans-every-issue-of-the-request/trail/gate.md`
alone (executed). `bin/seal pr-body <item> --body <the body file> --check`
exited 0 and printed that the file is `pr.md` above `## From the records`
and the records' text below it (executed). No `pr.<lang>.md` is owed, since
both language keys of `seal/config.json` read `English` (read). No
`seal/parity.json` stands, so no comparison with an original is owed
(executed, `ls seal/parity.json`: no such file). No earlier `guarantee.md`
stands, so this audit covers the whole range.

The issue was read with `gh issue view 1563` (executed, 2026-11-22), and
the diff, `frame/design.md`, `frame/plan.md`, `frame/questions.md`,
`routing.md`, `trail/phases/phase-1.md`, `trail/rounds/round-1.md`,
`trail/rounds/round-2.md`, `gaps.md`, `changelog.md`, `pr.md` and the body
file were read whole (read).

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| S7's narrow set passes, 259 passed | `trail/rounds/round-2.md` *Probes*, the crafter's count for `014c7e9e2`; `frame/design.md` S7 | `bin/test -q -p no:randomly` over the nine files S7 names, at `fe04a0bb4` | holds: 259 passed, exit 0 (executed) |
| S7's set opens the edited section: a line of the new scope paragraph padded past 88 columns turns `test_prose_stays_within_the_wrap_limit[skills/implement/orchestration.md]` red | `trail/phases/phase-1.md` *No case was written* (the `seal mutate` coverage probe) | in a scratch clone at `fe04a0bb4`, `skills/implement/orchestration.md:203` padded through `Edit`, then `bin/test -q -p no:xdist tests/behaviour/test_docs_line_wrap.py`; then the file restored and the same command | holds: padded, 1 failed, 50 passed, exit 1, the failing case the one named; restored, 51 passed, exit 0 (executed). The clone was removed |
| D1 to D7 stand in their files word for word | `trail/phases/phase-1.md` *D1 to D4 went in word for word*; the fix pass's closes in `trail/rounds/round-1.md` findings 1 to 3 | a `python3 -I` script that takes each fenced block of `frame/design.md` D1 to D7, splits it at blank lines, collapses whitespace and looks for each part in its file; run at `fe04a0bb4`, and at `f8056edde` with the work item's records restored from HEAD to show it can fail | holds: at HEAD every part of every block found (D1's four parts, D2 to D7 one each); at the base every part not found (executed) |
| The rewrap at `2c3c68807` changed no word | `trail/phases/phase-1.md` *D1 to D4 went in word for word* | `git diff -w --word-diff=plain 2c3c68807^ 2c3c68807 -- skills/implement/routing-question.md`, grepped for `[-` and `{+` | holds: no changed word, grep exit 1 (executed) |
| S5: the version is 0.38.4 and `.claude-plugin` names 0.38.3 nowhere | `trail/phases/phase-1.md` S5 | `grep -n '"version"' .claude-plugin/plugin.json`; `git grep -n '0\.38\.3' -- .claude-plugin` | holds: `4:  "version": "0.38.4",`; the grep printed nothing and exited 1 (executed) |
| S6: the diff outside the records changes the eight files S6 names and no other | `trail/rounds/round-2.md` *Probes*; `frame/design.md` S6 | `git diff --stat 5c4bdc8d5 HEAD -- skills .claude-plugin docs agents templates README.md README.ko.md CONTRIBUTING.md tests` | holds: `.claude-plugin/plugin.json`, `README.ko.md`, `README.md`, `skills/config/SKILL.md`, `skills/core/SKILL.md`, `skills/implement/SKILL.md`, `skills/implement/orchestration.md`, `skills/implement/routing-question.md` (executed) |
| `## Removes` rows 1 to 7, and the changelog's "Before" statements, stand nowhere in the tree | `frame/design.md` *Removes*; `changelog.md` entries 1, 4 and 5 | `git grep -n -F` outside `seal/threads` for "when it starts a work item", "the SDD set and the ticket", "routing answer was given for the release", "before the first edit, as", "A work item that starts", "asks for both before its first edit", "every time and even for a typo fix", "작업 항목을 시작할 때", "매번 묻고" and "before the next work item's first edit" | holds: each prints nothing but "when it starts a work item", whose one line is `skills/implement/merge-order.md:3`, the opening of that file's own section, not the batch. The row's coordinate, `skills/implement/SKILL.md:166`, no longer holds it (executed) |
| Both quotes of `pr.md` stand word for word in `frame/plan.md` | `trail/rounds/round-2.md` *Confirmations*, the records read whole | `grep -c -F` of each quote over `frame/plan.md` | holds: 1 and 1 (executed) |

No phase record claims `seen red`: phase 1 wrote no case, by `frame/plan.md`
*Alternatives considered* row 9, and the fix pass `014c7e9e2` added none
(executed, `git diff --stat f8056edde HEAD -- tests evals` prints
nothing). The broad run's own counts, 5719 passed and 10 skipped, are the
orchestrator's account and were not re-run here; `trail/gate.md` at HEAD is
the record this audit rests on (unverified for the counts; the orchestrator
answers them).

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | The batch section states one batch per request covering every issue, a later item asks nothing new, and an issue's "the owner decides" line is checked against the tree before it enters the batch; `skills/implement/SKILL.md` and `skills/core/SKILL.md` cite the section with the same scope; `routing-question.md` has a later item write the batch's language keys; the two READMEs and `skills/config/SKILL.md` ask once per request; the version moves to 0.38.4; no policy-root document changes | the issue's *Decision* bullets and *Done when* items 1 to 3 (read); the tree, through D1 to D7 found whole and the Removes rows gone (executed) | none |
| the build | Phase 1 (`2c3c68807`) built *Scope* items 1 to 5 and the fragment; the fix pass `014c7e9e2` built items 6 to 8 and corrected the fragment | the design, word for word (executed); the plan's *Phases* Status cell names `2c3c68807`, and `trail/phases/phase-1.md` stands for it, as `routing.md`'s `Implementation` `crafter` requires (read) | none |
| the last round | Round 2, at `cc31c3ee4`, opens no finding and confirms round 1's four `fixed 014c7e9e2` closes | the tree: each sentence it confirms stands at HEAD as it quotes it (read); its S6 and S7 probes re-run to the same results (executed); no commit after `cc31c3ee4` touches a path outside `seal/threads/1795276650-the-batch-spans-every-issue-of-the-request/` (executed, `git log --name-only cc31c3ee4..HEAD`) | none |
| the changelog | Five `### Changed` entries and the version line, and two `### Process changes` rows, one for the batch section and one for the core's sentence | the diff: each "Before" sentence quotes what `f8056edde` held and each "Now" sentence what HEAD holds (read against `git diff f8056edde...HEAD`); the core row names *The first value: efficient development through the AgenticSeal process*, the heading at `skills/core/SKILL.md:31` (read); `frame/plan.md` *Operational impact* names two rows | none |
| the orchestrator's part of the pull request body | `pr.md`: the title takes `fix:`, on the grounds that the section let a later issue's start stop a run and let an issue's "the owner decides" enter the batch unchecked; `Closes #1563` | `frame/plan.md` *Judgments of the run*, the title's row, word for word (executed); the issue, whose title opens `fix:` and whose body reports that behaviour (read) | none |
| `routing.md` *Why this way* (the orchestrator's account, under `agentic`) | A framer because the rule is stated in three files; a crafter because a rewritten sentence may be pinned by a case; the review chain because the text is acted on at every run's start; `Automation` `yes`; the version move to 0.38.4 | the diff, which changes prose in those three files, `routing-question.md` and `plugin.json`'s version line, and no script, hook or case (executed, S6). The two READMEs and `skills/config/SKILL.md` entered by round 1 finding 3's fold, recorded in `frame/plan.md` *Judgments of the run*, and are statements of the same rule a person reads; the grounds still describe the diff. Its citations `skills/implement/SKILL.md:163-168` and `skills/core/SKILL.md:95-99` span the rewritten sentences at HEAD (read) | none |

```seal
target: fe04a0bb4 against f8056edde
Verdict: sealed
```
