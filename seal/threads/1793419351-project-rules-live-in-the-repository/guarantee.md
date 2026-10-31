# Guarantee: 1793419351-project-rules-live-in-the-repository

| Field | Value |
|---|---|
| Target SHA | dd01c3f2 against f80f48e6; earlier run: 91dfbff2 withheld |
| Broad gate | e4e2d9ea against f80f48e6 |

The base `release/v0.26.0` resolved through `origin/release/v0.26.0` to
`f80f48e6`; `release/v0.26.0@{upstream}` and `release/v0.26.0` answer no
commit in this worktree (executed, `git rev-parse --verify --quiet`).
`trail/gate.md` names one run, `e4e2d9ea against f80f48e6`, an ancestor of
HEAD (`git merge-base --is-ancestor`, exit 0, executed). `git log --no-merges
--name-only e4e2d9ea..HEAD ^f80f48e6` names `91dfbff2` (`trail/gate.md`),
`df9880ad` (`guarantee.md`) and `dd01c3f2` (`frame/design.md`,
`frame/plan.md`), each under
`seal/threads/1793419351-project-rules-live-in-the-repository/` alone, and
`git diff --stat e4e2d9ea HEAD` changes those four files and nothing else
(executed). So the tree outside the work item's records is the tree the broad
run and the first audit read, and the claims the first audit re-ran on it at
`91dfbff2` stand without a re-run; the rows below re-run the claims whose
coordinates `dd01c3f2` touched and the body's rewritten sentences. The run's
counts, 6,199 passed and 9 skipped with the chain check at exit 0, are the
orchestrator's account (read; unverified, the orchestrator answers them from
the gate's log). No `seal/parity.md` is declared, so no `original:` line is
owed (read, as at the first audit).

`bin/seal pr-body seal/threads/1793419351-project-rules-live-in-the-repository
--body <the body file the spawn prompt names> --check` exited 0, "below `## From
the records` is the records' text", with the tree's command and with the
installed plugin's (executed). `python3
skills/code-review/scripts/chain_check.py --baseline f80f48e6 --sealing`
exited 0 at HEAD, printing only the guarantee arm, which this file answers
(executed).

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| R1 to R4 parse, and R1's and R2's `from` stand in *The handoff* | `frame/design.md` *Rule changes*, moved by `dd01c3f2` | `python3 -I` calling `skills/settle/scripts/rule_changes.py#parse`, `#section_lines` and `#pattern` on `frame/design.md` at HEAD | holds: `errors` empty, four operations (two `change`, two `add`), every section found, both `from` values found in *The handoff* (executed) |
| `## Removes`: every row is gone from the tree, or lands at the settle as its row says, the row the reframe added among them | `frame/design.md` *Removes*, the row "found with `git grep` on its words." added by `dd01c3f2` | each removed text, whitespace folded, searched over every tracked file outside `seal/threads/`: "`git stash pop`", "that one file, `git stash`", "`--json mergeable` before it waits on CI", "names why not `gh pr edit`", "the hand-back says which were enumerated", "the stall signal is the time since it last advanced", "found with `git grep` on its words" | holds: six stand nowhere; the stall sentence stands in `docs/the-review-record.md` alone, R1's `from` (row above), which the same search finding it shows can find (executed) |
| The reframed C2: three methods, a list none made is a sample, an unbounded domain has no whole list, the hand-back names the method and what it listed, calls a sample a sample and says where the open part of a sample or of such a class stands, the proofer judges the method, and rule 19's search is the least one whose list is a sample unless a method made it; rules 12 and 19 rewritten in place | `frame/design.md` *Scope*, the C2 row and the paragraph opening **C2 was reframed after round 4** | read `skills/agent-contract/SKILL.md:157-172` (rule 12) and `:228-236` (rule 19) at HEAD clause by clause against the row, and against `skills/code-review/SKILL.md:165-169`, which the reframe's new grounding row cites | holds: each clause of the row stands in rule 12 or rule 19, and neither rule says more than the row and its grounding row; "and the hand-back says so" is the grounding row's "the hand-back's duty to say so" (read) |
| The build already holds the reframed C2: rule 12 and rule 19 were built by `c5eec50b`, `9194dd0e`, `777ca4d8` and `4d63917c` | `frame/design.md` *Scope*, the same paragraph; `frame/plan.md`, the rule 12 bullet | `git show --stat` of the four commits; `git log -L '/^## 19/,+8:skills/agent-contract/SKILL.md' f80f48e6..HEAD` | holds: all four touch `skills/agent-contract/SKILL.md`; rule 19 was last changed by `9194dd0e`, after `c5eec50b` (executed) |
| The four rounds came from the undrawn boundary: round 1's finding 3, round 2's two regressions from round 1's paste-ready text, round 3 reopening the sample's definition, round 4's regression from round 2's rewrite dropping the duty | `frame/design.md` *Scope*, the two bullets under **C2 was reframed after round 4** | `grep` of the heading, `verdict:`, `regression:`, `reopens:` and `confirms:` lines over `trail/rounds/`; read `trail/rounds/round-2.md:19`, `:59`, `trail/rounds/round-4.md:19` | holds: round 2's findings 1 and 2 read `regression: round-1#3` and name round 1's paste-ready text; round 3's finding 1 reads `reopens: round-2#2`; round 4's finding 1 reads `regression: round-2#1` and names what `c5eec50b` dropped (executed, read) |
| "`hygiene.yml`'s `release` job runs 4 of its 6 steps for this base (the other 2 run only on a pull request into `main`). The broad run answered 2 of those 4, the chain and the mode steps; the issue-claims and the READMEs steps run in this pull request's CI." | the pull request body, *Other things to know*, last bullet | read `.github/workflows/hygiene.yml`'s `release` job; `python3 -I` printing `skills/verify/scripts/broad_gate.py#PARTITION`; read `#ONLY_AT_MAIN` and `#steps_for` | holds: six steps; `ONLY_AT_MAIN` holds the version and milestone steps, which `steps_for` leaves out where the base is not `main`; of the four left, `PARTITION` gives the chain step the `chain` arm and the mode step the `mode` arm, and the issue-claims and READMEs steps no arm (executed, read) |
| "rounds 2 to 5 verifying rounds, of which rounds 2 and 4 found regressions in contract rule 12 and round 3 reopened one; round 5 clean" | the pull request body, *The run beside the last one*, first row | the label `grep` above, and each finding's `location:` | holds: the regressions of rounds 2 and 4 are located in `skills/agent-contract/SKILL.md` rule 12 (round 2's finding 2 also rule 19 and two of #1167's files); round 3 reopens `round-2#2`; round 5 has no finding (executed) |
| "Round 4's regression went to a fix pass, and then to the framer ... reframed C2 after round 4 (dd01c3f2) ... the reframe touched the frame alone, after the gate record" | the pull request body, *Other things to know*, first bullet | `git show --stat dd01c3f2`; `tail` of `frame/design.md` | holds: `dd01c3f2` changes `frame/design.md` and `frame/plan.md` alone, after `91dfbff2`; the design ends `Framed 2026-10-31 by framer, before the build.` then `Reframed 2026-10-31 by framer, after round 4.`, which the chain check's frame arm reads without a problem (executed) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | As at the first audit for C1, C3, C4, R1 to R4 and the entries; since `dd01c3f2`, C2 names the three methods, the sample, the unbounded domain and rule 19's least search, rewrites rules 12 and 19 in place, removes rule 19's old sentence, and states that it was reframed after round 4 because round 4's finding 1 was a second regression on rule 12's unbounded-domain sentence after round 2's had gone to a fix pass, with the grounds that C2 as first framed drew no line against `skills/code-review/SKILL.md` *A finding is not closed too early* or rule 19; the build owes no change and the plan gains no phase | the issue's *Done when* as at the first audit (the issue is unchanged since, `updatedAt` 03:56Z before the reframe, read); the tree, every `## Removes` row and the C2 row re-run above; the route `skills/code-review/orchestration.md:167` and `docs/the-review-record.md:609-610` give a second regression on one unit, the framer, who wrote the `Reframed` line under the mark that route names (read, executed) | none. The route's first step, closing the open findings `deferred the frame`, has no finding to act on now, because round 4's finding 1 was already closed `fixed 4d63917c` by the fix pass the route would not have run; the design states that fix pass and why the redesign owes no build, so the route and its grounds now stand in the records, which is what the first audit found missing (read) |
| the build | Phases 1 and 2 and four fix passes, as at the first audit; nothing outside the records since `e4e2d9ea` | the reframed design: rules 12 and 19 at HEAD say what the C2 row says, clause by clause (read); every sampled `executed` and `seen red` claim the first audit re-ran on this same tree (executed at `91dfbff2`, the tree outside the records unchanged since, executed) | none |
| the last round | Round 5 at `4cfded90`: round 4's finding 1 holds as fixed at `4d63917c`, nothing opened; rule 12's two restored phrases read against `skills/code-review/SKILL.md:167-169`, rule 12 at `9ad3b9f9`, C2 and the lesson row | the tree: rule 12 at HEAD is the text round 5 read, and rule 19 the text round 4 read at `9194dd0e` (`confirms: round-3#1`), neither changed since (executed: `git log -L`, `git diff --stat e4e2d9ea HEAD`); what the reframe added to C2 is the source round 5 read the text against (read) | none. Round 5 read rule 12 against C2 as first framed, before the reframe; no round reads the text against the reframed row, and the rows above compare them instead and find them one (read) |
| the changelog | `### Fixed` as at the first audit, now also naming rule 19's least search and a sample's open part; `### Process changes`: four rows | the reframed C2 and the tree: rule 12's three methods, the sample, the unbounded domain's "the hand-back says so and where its open part stands", and rule 19's least search, each at `skills/agent-contract/SKILL.md:157-172` and `:228-236` (read) | none |
| the orchestrator's part of the pull request body | `Closes #1200`; the run's counts; the regression route taken late and then by the framer; rule 12's four rounds; the merge order beside #1167; the entries deleted after the merge; two `gaps.md` rows open; the process table adopted; 4 of 6 `release` steps for this base, 2 answered by the broad run | every rewritten sentence re-run above; the counts and the merge-order and after-merge items as at the first audit (executed, read). "The build at HEAD already holds the reframed C2, which round 5 confirmed" reads as round 5 confirming the build's text, which its record does; the reframe came after it (read). The measurement rows (commits, records' share, segments, tokens) count to the gate record, as their wall-clock row names, so the reframe's framer segment and this audit's are outside them (read) | none |

Verdict: sealed
