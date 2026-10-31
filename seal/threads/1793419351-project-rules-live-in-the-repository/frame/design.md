# Design: 1793419351-project-rules-live-in-the-repository

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both* | a decision is written into the work item's records "where the next session reads it and nothing else has to remember it", so the new orchestration section cites this sentence and does not restate it |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* | a fact has one source, and less text means nothing said twice: a lesson the tree already states is confirmed at its coordinate below and written nowhere again; a rule this work adds is kept only on a record of what it would have caught, which the *Lessons* tables give per rule |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | a pull request does not edit `docs/`; a policy change is a `## Rule changes` item the settle writes, so R1 to R4 below edit no file now |
| `skills/settle/SKILL.md` *Rule changes* and *A rule has one shape* | the operation grammar of R1 to R4, and the bold sentence, grounds and check line each `to` that states a rule carries |
| `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph opening **A problem that recurs within a run gets a prevention home at once** | the home of one recurring problem is a mechanism or "a rule written into the file the recurring act is read from"; each moved lesson below lands in the file its act is read from |
| `skills/implement/acts.md` *Orchestrator: which of these acts runs itself* | every `## Orchestrator:` heading needs a row; the new section of C1 gets one, `still a sentence` |
| `skills/agent-contract/SKILL.md` rules 12, 19 and 20 | the class is enumerated (each lesson was read in every log, not sampled); a change rewrites the text it amends in place (C3, C4, R1 rewrite stale sentences rather than adding beside them) |
| Issue #1200, owner's direction (read: `gh issue view 1200 --json body,comments`, 2026-10-31, no comments) | two homes; what stays local is the lid-closed sleep, the plugin cache path, the commit author address in this clone's git config, plain-Korean reports, and the rule separating the homes |
| Issue #1200's table (read) | treated as the orchestrator's claims; each row is confirmed or corrected at a coordinate in *The entries* below |

Facts this frame rests on, each with how it was obtained:

| Fact | Label | How |
|---|---|---|
| The session memory holds 53 entry files and the index `MEMORY.md`; the index lists the 53 and no more; `compact-not-net-negative.md`, named in the spawn's copy of the index, is gone (#1192 merged as #1196) | executed | listing of the memory directory and a per-file match against the index, 2026-10-31 |
| The memory directory also holds a stray file whose name begins `orktrees not yet cleaned`, 9,438 bytes, dated 2026-10-04, an old copy of the index | executed | listing and its first lines |
| Nothing in `skills/`, `agents/`, `docs/`, `hooks/` or `CONTRIBUTING.md` asks the orchestrator to check a running agent for a stall; the one rule is `docs/the-review-record.md` *The handoff*, whose stall signal is the Status column's last advance | executed | `git grep -n -i 'caffeinate\|stall\|watchdog'` returned only `agents/framer.md:51` |
| A crafter call hung 4 h 48 min unnoticed in 0.16.0 | executed | `gh issue view 680 --json comments`, the comment opening "4 h 48 min with no progress" |
| The harness's task output for an agent is a symbolic link to the agent's transcript, and `stat -f %m` on the link reads the link's own time while `stat -L -f %m` reads the transcript's | executed | `ls -la` of this session's task directory; a probe in the scratch folder: a link to a file touched to 2026-01-01 read 1793420042 plain and 1767193200 followed |
| `seal settle --apply` deletes with `shutil.rmtree` and stages nothing | executed | `grep -n rmtree skills/settle/scripts/settle.py` (line 848) |
| `git switch` and back over unstaged deletions exits 0 and restores a deleted file that differs between the branches, printing only a `D` line for the one that is the same | executed | a probe repository in the scratch folder: branch `a` and `b`, `d/differs.md` differing, `d/` deleted, switch to `b` and back, `d/differs.md` present, both switches exit 0 |
| `skills/verify/orchestration.md` *The broad gate* prescribes "`git stash`, that one file, `git stash pop`" for the base comparison, while the gate itself runs the base in a scratch worktree | executed / read | `git grep -n 'git stash'` (line 104); `templates/setup/config.md` row 3 of the broad gate's table (read) |
| `skills/code-review/orchestration.md` line 231 says "`docs/release-checklist.md` names why not `gh pr edit`", and no file of the tree names why | executed | `git grep -n 'gh pr edit' -- . ':!tests'` returned that line alone |
| `tests/text/test_the_rules_have_one_owner.py#test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge` pins "reads `gh pr view <N> --json mergeable` before it waits on CI" | executed | `grep -rn` over `tests/` |
| Nothing closes a release milestone: `close_issues_on_release.py` closes issues only, and `release: 0.20.0` closed 2026-10-18 after `v0.20.0` was tagged 2026-10-07, `release: 0.21.0` on 2026-10-18 after 2026-10-13, `release: 0.24.2` on 2026-10-30 after 2026-10-29 | executed | `git grep -n 'state.\{0,5\}closed\|milestones/' -- .github`; `gh api repos/{owner}/{repo}/milestones?state=closed`; `git log -1 --format=%cI <tag>` |
| In the 0.24 settle a switch to `main` and back restored 28 `gaps.md` files, the removal commit left them tracked, and the broad gate refused the tree | read | the orchestrator's account in `no-branch-switch-with-unstaged-deletions.md`, nobody's finding in the tree; that settle is #1182 (executed: `gh pr view 1182`), and the git behaviour under it is executed by the probe above |
| A real path handed in a spawn prompt reached committed records in 0.18.1 and in #1174, the second costing a rewrite of the branch's history | read | the orchestrator's accounts in `overnight-0-18-1-run.md` and `run-0-25-1-1174.md`, nobody's finding in the tree |
| R1 to R4 parse, and each `change`'s `from` is found in its section | executed | a probe from a `git clone --no-local` in the scratch folder calling `skills/settle/scripts/rule_changes.py#parse`, `#section_lines` and `#pattern` on this file: no refusal, both `from` values found in *The handoff* |
| The cost profile of #365's chain segments is on the durable log | executed | `gh issue view 51 --json comments`, comment 5787486569 |
| `hooks/` holds no worktree guard and no git-level commit gate | executed | `ls hooks` |
| No unsettled design's rule change names `docs/the-review-record.md` *The handoff*; `1793343707` adds to `docs/release-checklist.md` *2b* and `1793273065` changes a sentence of *6. After the merge* | executed | `grep -A1 '^  file:'` over `seal/threads/*/frame/design.md` |
| #1167 edits, in its phase 5, `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round*, *A regression is routed by comparing the fix with the frame* and *The fix pass then finds what the fixes left standing*, `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, `agents/crafter.md` step 8, `templates/records/sdd-plan.md` and the settle; #1199 edits `skills/commit-pr-convention/SKILL.md` and the release preparation | read | the spawn prompt (the orchestrator's finding); #1199's body read with `gh issue view 1199` |

## Scope

**In.** Every entry of the orchestrator's session memory is read whole, and each project rule or lesson in it is confirmed at its coordinate in the tree, moved into its home, or judged with grounds; the verdicts are *The entries* and *The lessons* below. Eight changes move what is missing:

| Id | What | Where | Lands |
|---|---|---|---|
| C1 | where the orchestrator writes a decision or a lesson it learns in a run, and that a session's local memory is not that place | new section `## Orchestrator: where a decision or a lesson is written`, appended at the end of `skills/implement/orchestration.md`, and its row in `skills/implement/acts.md` | this pull request |
| C2 | a class is enumerated by a method that makes the list whole, the hand-back names the method, and the proofer judges the method | `skills/agent-contract/SKILL.md` rule 12, rewritten in place | this pull request |
| C3 | the base comparison by hand runs in a worktree of the base, never through `git stash`, whose one stack every worktree and session of the clone shares | `skills/verify/orchestration.md` *The broad gate*, the paragraph opening **That comparison is reactive.**, rewritten in place | this pull request |
| C4 | before a push and after it the orchestrator reads the pull request's `state` as well as `mergeable`, waits on every workflow's checks, and the reason not to use `gh pr edit` is stated where the act is | `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*, two sentences rewritten in place, and the pin in `tests/text/test_the_rules_have_one_owner.py` that quotes the first | this pull request |
| R1 | the stall check on a running agent | `docs/the-review-record.md` *The handoff* | the settle |
| R2 | a location on the orchestrator's machine is named in words in a spawn prompt, never by its path | `docs/the-review-record.md` *The handoff* | the settle |
| R3 | what `seal settle --apply` removed is committed before anything switches that checkout | `docs/release-checklist.md` *2b. Settle what earlier releases left behind* | the settle |
| R4 | the release milestone is closed after the tag | `docs/release-checklist.md` *6. After the merge* | the settle |

**Out.**

- Deleting the memory entries. It is the orchestrator's act after the merge (#1200 *Done when*), on a directory outside the repository; `frame/plan.md` *Operational impact* lists what goes and what stays.
- Automating the milestone's close in `.github/scripts/close_issues_on_release.py`. Weighed in `frame/plan.md` *Alternatives considered*.
- Making `seal settle --apply` stage its removal. Weighed in `frame/plan.md` *Alternatives considered*.
- The lessons judged below the bar in *The lessons*. Their home is this record, as #1200's body allows ("a work item's records"); none earns a rule on one instance, and each row says why.
- `skills/commit-pr-convention/SKILL.md` and `docs/branch-and-release.md` *The version is named at the cut*: #1199 holds them, and the one lesson that would touch them (renumbering milestones by renaming) is #1199's owner decision.
- `agents/crafter.md`, `templates/records/sdd-plan.md`, `skills/settle/SKILL.md`, and the three `skills/code-review/orchestration.md` sections and the `skills/implement/orchestration.md` section #1167 edits.

### The entries

Each of the 53 entry files, by name. *Verdict* is one of: **in the tree** (confirmed at the coordinate), **moved** (to the change named), **gone** (the mechanism it is about was removed, so there is nothing to follow), **state** (a finished run's position, held by git, the pull requests and the issues; its lessons are in *The lessons*), **measurement** (a reading, whose home is a log issue), **local**.

| Entry | Verdict | Coordinate |
|---|---|---|
| `watchdog-an-unattended-run.md` | moved | R1; how this machine stays awake (`caffeinate`, the closed lid) stays in `lid-closed-mac-sleeps.md` |
| `measure-the-segment-at-its-boundary.md` | in the tree | `skills/verify/orchestration.md` *Measure the segment, and feed the flow log*; `docs/measuring-a-run.md` *Where a reading goes*; its concern that nothing makes the act run is stated in `skills/implement/acts.md`, the paragraph opening **One act is outside this table**; #330 is closed |
| `measure-every-segment-to-89.md` | in the tree | a redirect to the entry above; #89 is closed and the log is found by label in the same section |
| `the-stamp-means-work-done.md` | in the tree | `docs/the-review-record.md` *The stamp*; `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*, the paragraph opening **The stamp is drawn for you**; #975 closed |
| `release-suite-needs-the-fold-staged.md` | gone | the fold left in 0.22.0; `tests/conftest.py#on_disk` reads what is on disk; #368 closed naming fc3e1175 |
| `no-branch-switch-with-unstaged-deletions.md` | moved | R3 |
| `run-the-broad-gate-cheapest-first.md` | in the tree | `seal/config.md` row `Broad gate` runs `ruff` before `bin/test`; the version timer's exemptions in `docs/release-checklist.md` *What a release pull request is held to*; its ledger trap is gone with the ledger |
| `the-cost-profile-of-a-chain-segment.md` | measurement | #51, comment 5787486569 |
| `the-five-issues-of-the-0-11-1-run.md` | state | #365, #362, #363, #366 and #368 each carry their measurement; the sizing criterion is `docs/issues-and-milestones.md` *A milestone answers *when*, and takes three shapes* |
| `lid-closed-mac-sleeps.md` | local | the machine's sleep with the lid closed (owner's list) |
| `plain-korean-reports.md` | local | how the owner wants reports (owner's list) |
| `specseal-commit-email.md` | local | the author address pinned in this clone's git config (owner's list); the rule that no real address enters a committed file is `CONTRIBUTING.md` *House rules*, **No real identifiers**, held by the `real_identifiers` census |
| `plugin-copy-in-force-is-version-cache.md` | local, content in the tree | the cache path is local (owner's list); what loads and how to verify an update are `skills/update/SKILL.md` step **2b. Read the installed copy before believing the installer**, `docs/experiments/2026-09-03-skill-preload-and-the-copy-in-force.md` and `CLAUDE.md` *The core* |
| `local-memory-vs-project-rule.md` | local, and moved | stays as the owner's list says; its rule is C1 |
| the 39 run logs: `overnight-run-issues-51-57.md`, `handoff-two-roots-phase3.md`, `overnight-0-5-0-issues-80-82.md`, `overnight-0-7-0-issues-121-119-109.md`, `overnight-0-8-0-issues-153-150.md`, `overnight-0-8-1-issue-161.md`, `overnight-0-8-2-issue-170.md`, `overnight-0-8-2-four-items.md`, `overnight-0-9-1-five-items.md`, `overnight-0-9-3-five-items.md`, `overnight-0-9-5-262-310.md`, `overnight-0-10-0-issue-120.md`, `overnight-0-11-1-shipped.md`, `overnight-0-11-2-issue-365.md`, `overnight-0-11-3-three-items.md`, `overnight-0-11-4-shipped.md`, `overnight-0-12-1-shipped.md`, `overnight-0-12-3-shipped.md`, `overnight-0-14-0-four-items.md`, `overnight-0-15-0-run.md`, `overnight-0-15-1-run.md`, `fold-0-15-3-run.md`, `overnight-0-15-3-run.md`, `overnight-0-15-4-run.md`, `next-0-15-5-plan.md`, `overnight-0-15-5-run.md`, `overnight-0-16-0-run.md`, `overnight-0-17-0-handoff-run.md`, `overnight-0-18-0-run.md`, `overnight-0-18-1-run.md`, `overnight-0-18-2-run.md`, `next-0-18-3-plan.md`, `overnight-0-20-0-run.md`, `next-0-21-0-plan.md`, `run-0-22-1-964-957.md`, `run-0-22-4.md`, `run-0-25-0.md`, `run-0-25-1-1148.md`, `run-0-25-1-1174.md` | state | every release they describe is tagged (`v0.4.0` to `v0.25.1`) or its pull requests are merged; each lesson inside them is a row of *The lessons* |

The index `MEMORY.md` is rewritten by the orchestrator to the entries that stay. The stray old copy of the index goes with the deleted entries.

### The lessons

Every lesson the 39 run logs and the rule entries state, enumerated by reading each file whole. A lesson stated in several logs is one row, its sources listed by release.

**Moved.**

| Lesson | Sources | Change |
|---|---|---|
| check every running agent for a stall at least every 30 minutes by its transcript's age, read through the task output's link with `stat -L`; never wait on a completion notice alone; a background agent can end with no notice; a long probe runs in the background | 0.15.3, 0.16.0, 0.18.1, 0.18.2, 0.25.1 (`run-0-25-1-1148.md`), `watchdog-an-unattended-run.md`; 0.22.1's "stop a spawn with no edit in 45 min" is replaced by it | R1 |
| a decision or a lesson goes to the repository, never only to local memory | `local-memory-vs-project-rule.md`, #1200 | C1 |
| enumerate a class by construction, by decomposing the artefact, or by a property a command lists, never by the instances you can see or a grep of one wording; ask the fix pass how it knows the list is whole; the next round judges the method | 0.8.2 (both logs), 0.9.5, 0.15.4, `next-0-15-5-plan.md`, 0.22.4; `seal/follow-up.md`'s row opening **Nothing enumerates the class *a figure about a corpus*** records one lineage where every hand enumeration shipped short | C2 |
| `git stash` is one stack shared by every worktree of the clone; use a worktree or `git show` | 0.18.0 | C3 |
| check that the pull request is still open before pushing to its branch | 0.14.0, `fold-0-15-3-run.md` | C4 |
| wait on every workflow's checks after a push, not one workflow's runs | 0.15.1, 0.15.3, 0.20.0 | C4 |
| `gh pr edit` stopped on a GraphQL error about Projects (classic); use `gh api -X PATCH` | 0.4.0 (`handoff-two-roots-phase3.md`), 0.8.0 (read: the orchestrator's account; nobody has re-run `gh pr edit` since, and a probe of it writes, so the sentence is dated) | C4, the reason stated where the tree's citation of it dangles |
| a real path in a spawn prompt is copied into records and refused by the census | 0.18.1, 0.25.1 (`run-0-25-1-1174.md`), this work item's own spawn | R2 |
| commit what `seal settle --apply` removed before any switch of the checkout | `no-branch-switch-with-unstaged-deletions.md` | R3 |
| close the release milestone by hand after the release | 0.15.0, 0.15.3, 0.15.4, 0.15.5, 0.18.0, 0.18.1, 0.18.2, `next-0-18-3-plan.md`, 0.25.0 | R4 |

**In the tree.**

| Lesson | Sources | Coordinate |
|---|---|---|
| a phase is a fresh crafter; a fix pass resumes the implementer while its context allows; coordinates matter more than resume against fresh | 0.3.0 (`overnight-run-issues-51-57.md`), 0.4.0, 0.7.0, 0.15.1 | `skills/code-review/orchestration.md` *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer*; `docs/the-review-record.md` *The handoff* |
| an owner-only decision is a row, never a wait; ask everything once before the first edit, permissions included; name each answer's consequence in plain words | 0.3.0, 0.5.0, 0.8.2, 0.9.1, 0.15.5 | `skills/implement/SKILL.md` *1. Read the documents that outrank the code first* |
| a fact handed over is a claim with a coordinate; a count or a pasted SHA is re-derived (`git rev-list`, `git rev-parse`), never copied from a hand-back; a handoff's causal reading is re-derived | 0.8.0, 0.11.2, 0.11.4, 0.14.0, 0.15.5, 0.25.0 | contract rule 5; `docs/the-review-record.md` *The handoff*; the pull request body's own part restates no record (`skills/code-review/orchestration.md`, the paragraph opening **You write the pull request body after**) and the sealer audits it |
| `git -C` with the absolute path, a commit in a call of its own, joined to a `cd` only by `&&` | 0.8.2, 0.15.1, 0.18.1, 0.18.3, 0.25.0 | contract rule 16; `tests/behaviour/test_a_commit_names_its_repository.py` |
| read an exit code directly, never through a pipe | 0.12.1 | contract rule 1 |
| an agent posts nothing, pushes nothing, commits nothing outside its definition, spawns nothing | 0.10.0, 0.14.0, 0.18.0, 0.18.1 | contract rule 6 |
| a paste-ready fix is the proofer's claim | 0.11.2, 0.11.3, 0.14.0, 0.25.1 | `agents/crafter.md`, the paragraph opening **A fix pass writes two lines of each finding**; `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame*, the table's second row |
| never hand the crafter a choice; a design decision is folded into the frame before the spawn | 0.15.0, 0.15.1, 0.22.1 | `skills/implement/orchestration.md`, the paragraph opening **A decision made after the frame is committed is folded** |
| integrate a conflict by merging the base in, never by a rebase; squash back to back; merge the release branch in only where a branch needs it | 0.15.0, 0.15.1, 0.15.3, 0.15.4 | `docs/release-checklist.md` *0. Before starting*; `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* |
| a commit after the build, a post-seal fix or an integration, brings the changelog fragment along | 0.18.2 | `skills/code-review/orchestration.md`, the paragraph opening **Two commits after the build are yours**; `docs/the-record-layout.md` *A commit after the build brings its changelog fragment along* |
| a repair after the seal: a verifying round where it touched code, the gate again, the sealer again; no extra round record otherwise | 0.15.0, 0.15.1, 0.18.0 to 0.18.3, 0.22.4, 0.25.1 (`run-0-25-1-1148.md`) | `skills/code-review/orchestration.md`, the paragraphs opening **The stated limit** and **Commit `guarantee.md`** |
| run the cheap arms before the suite; run every text-reading module before a seal; gate with nothing else running, one sealer at a time | 0.9.5, 0.11.4, 0.12.3, 0.15.4, 0.17.0, 0.18.0, 0.18.1, 0.20.0 | `seal/config.md` row `Broad gate`; `skills/code-review/orchestration.md`, the paragraph opening **The preflight is yours**; contract rule 2 (the modules that glob a changed path) |
| where the risk is platform-specific, run the other platforms before the broad run; a Windows assertion comes from that leg's log | 0.5.0, 0.8.0, 0.15.1, 0.15.3, 0.18.0, 0.18.1, 0.18.3, 0.22.4, 0.25.0 | `skills/code-review/orchestration.md`, the paragraphs opening **Where the work's risk is platform-specific** and **The stated limit**; encoding is `CONTRIBUTING.md` *House rules*, **Every file read or written names its encoding** |
| a second failed fix of one unit stops the run and goes back to design; a redesign is not a round option | 0.15.4, 0.18.0, 0.18.1, 0.18.2, 0.18.3, 0.21.0 | `docs/the-review-record.md` *The run*, the paragraph opening **A regression is routed by comparing the fix with the frame**; `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame* |
| a verifying round that opens nothing ends the run; how the cap counts | 0.10.0, 0.11.3, 0.15.1, 0.18.0, 0.18.3 | `docs/the-review-record.md` *The run*; the round generator these logs read is gone |
| search the tree for the shape before writing a parser, and the tracker before filing | 0.10.0, 0.14.0 | `skills/confidence-check/SKILL.md` **No duplicate exists**; `docs/the-review-record.md` *The run*, the ladder's rung 2 |
| a cross-version reading goes to the durable log at the moment of posting; the rolling log closes at the release | 0.11.3, 0.11.4 | `skills/verify/orchestration.md` *Measure the segment, and feed the flow log* |
| `flow-measurement` is a lookup label, never a topic tag | 0.8.1 | `docs/issues-and-milestones.md` *A label answers *what it is about*, and survives the move* |
| a release is sized by what must be in effect before the next work item | 0.9.3, `the-five-issues-of-the-0-11-1-run.md` | `docs/issues-and-milestones.md` *A milestone answers *when*, and takes three shapes* |
| a closing keyword claims one number; GitHub reads it only into the default branch | 0.8.0, 0.17.0 | `docs/issues-and-milestones.md` *A keyword claims the one number after it*; `docs/release-checklist.md` *6. After the merge* |
| the release note, its Thanks-to line and the seal publish from the workflow; a pull request title is a note line; cut the next release branch from `main` | 0.11.3, 0.11.4, 0.15.1, 0.17.0, 0.18.0 | `docs/release-checklist.md` *6. After the merge*; `docs/branch-and-release.md` *Cutting a release* |
| a contributor aimed at the wrong base is told so | 0.12.1 | `docs/release-checklist.md` *What a release pull request is held to* |
| a hotfix route | 0.11.1 | `docs/branch-and-release.md`, the merge-method table's hotfix row |
| the copy that loads is the installed one; an agent receives the installed plugin's copy; verify an update by the installed copy | 0.7.0, 0.10.0, `plugin-copy-in-force-is-version-cache.md` | `CLAUDE.md` *The core*; `skills/update/SKILL.md` step 2b; `docs/experiments/2026-09-03-skill-preload-and-the-copy-in-force.md` |
| a new session presses `automation` again | 0.21.0 | `skills/implement/orchestration.md` *Question 1*, the paragraph opening **A run resumed in a new session** |
| read the frame against the issue in one exchange | 0.25.1 (`run-0-25-1-1148.md`) | `skills/implement/orchestration.md` *The frame is read against the issue at the spawn* |
| the framer reads in bounded calls and writes a skeleton first | 0.12.3 | `agents/framer.md` step 2 and rule **Bound each call, not the reading** |
| scratch files are named after the work item | 0.15.0, 0.15.1, 0.18.1, 0.18.3 | `agents/framer.md` rule **A question a command answers is answered by running it**; `tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py`; the gate log path in `skills/code-review/orchestration.md` |
| a stale `.pyc` can fake a red in a mutation loop | `the-cost-profile-of-a-chain-segment.md` | `skills/verify/SKILL.md` *`seal mutate` asks condition 2 of one unit, one break at a time* |
| a run's segments are split from a resumed transcript; the subagent sidecar files are skipped | 0.8.2, 0.9.1, 0.15.0, `measure-every-segment-to-89.md` | `seal cost --segments` (`skills/verify/scripts/session_cost.py`, with `tests/skills/test_session_cost.py`) |
| the gate compares a failure with the base itself, so no baseline is taken before the first spawn | 0.8.2, 0.9.3 | `templates/setup/config.md`, row 3 of the broad gate's table; `skills/verify/orchestration.md` *The broad gate* |
| a missing `Not verified` row is closed, never deleted | 0.11.2 | `skills/implement/SKILL.md` *6. Drain the rows before the broad run, and keep the records* |
| a pinning case follows the frame's unit, because the frame outranks the code | 0.11.2 | `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, **Judgment precedence** |
| `bin/test` builds its own environment in a fresh worktree; `ruff` runs through `uvx`; `gh issue view` is read with `--json` | 0.8.0, 0.8.2, 0.16.0, 0.18.2, 0.21.0 | `CONTRIBUTING.md`, the `bin/test` paragraphs; `seal/config.md` row `Broad gate`; `agents/framer.md` step 4 |
| the routing check governs the session, at its tools and at the pull request | 0.22.4 | `docs/the-routing-check.md` |

**Gone.** The mechanism each is about was removed, so nothing is left to follow: the evidence ledger, `round_record.py`, `survivor-check` and `correction-check` (removed in 0.22.0, per `next-0-21-0-plan.md`'s last line and the absence of each from `git ls-files`), with every lesson about their cells, fences, verdict words, reach-backs, re-stamps and union merges (0.8.0, 0.8.1, 0.8.2, 0.9.1, 0.9.5, 0.10.0, 0.11.2, 0.11.3, 0.12.1, 0.12.3, 0.14.0, 0.15.0, 0.15.1, `fold-0-15-3-run.md`, 0.15.3, 0.15.4, 0.15.5, 0.16.0, 0.18.0 to 0.18.3, 0.21.0); the fold and its staging (0.7.0, 0.8.1, 0.8.2, 0.11.1); the `Enforced by` line and the retire step (`fold-0-15-3-run.md`, 0.15.3); the `Approved` line (0.15.3, 0.18.1); the worktree guard and its `[worktree-ok]` comment (0.9.1, 0.9.3, 0.15.0, 0.15.4, 0.15.5, 0.17.0, 0.20.0, 0.22.1), absent from `hooks/`; the git-level commit gate and its heredoc, loop and `-C` traps (0.8.2, 0.15.1, 0.15.5, 0.18.0, 0.18.1, 0.22.4), removed by #1027; the draft pull request before round 1 (0.8.1, 0.22.1), replaced by the pull request opening ready after the seal; the release preparation pull request and its duplicate in a parallel session (0.12.3, 0.21.0), replaced by the version moving in the release's first pull request (`docs/release-checklist.md` *5. The release pull request*); the depth rule and "a fix pass may not add mechanism" (0.8.0, 0.8.1, 0.18.0), replaced by the regression route; stacked branches retargeted after a squash (0.12.1, 0.15.0, 0.15.1), which the flow no longer opens; a new gate's first release testing its range (0.9.3), whose gate is gone; `Ran by` in spawn prompts (0.15.4, 0.18.1), absent from the round template.

**In an issue.** The local mode root under `.git` (0.8.0): #158. The review segment's progress readout (0.9.1): #236, which R1 does not close, because R1 reads from outside the agent. Required checks (0.12.1): #457. The orchestrator's suite runs (0.9.3): #145. The ruleset (0.9.3): #253. The framer's model (0.21.0, 0.25.0): the owner's *Framing* sections of #1148 and #1167. The emblem (0.20.0, `run-0-25-1-1174.md`): #1174, shipped. The core's delivery (0.25.0): #1177 and #1183. The evaluation baselines (0.22.1): #957 and #966 to #971. Renumbering milestones by renaming them, never moving issues (0.11.1): #1199's owner decision.

**Below the bar; this record is their home.** One instance each, or a fact about a tool that no act of the workflow reads, so none earns a rule under `skills/core/SKILL.md` *The rule a mechanism is kept against*; a second instance is what would move one.

| Lesson | Source | Why it stays here |
|---|---|---|
| `gh issue edit --milestone` reported success and moved nothing | 0.8.0 | one instance; the tree moves milestones with no command it prescribes |
| `git for-each-ref` matches path components, not substrings | 0.11.3 | a git fact; no rule reads it |
| `gh pr merge --match-head-commit` takes the full SHA | 0.16.0, 0.18.0 | refuses loudly; nothing is lost |
| a crafter stopped mid-phase leaves files staged, so the orchestrator commits its own file by path | 0.25.0 | one instance |
| capture a probe's message, not only its exit code | 0.8.2 | one instance; contract rule 4's labels cover what was shown |
| a fix's case reproduces the finding's own example | 0.15.4 | one instance; contract rule 15 asks for the case seen red |
| a probe is run where its code runs, not where it was written | 0.22.1 | one instance |
| a 429 limit on subagents can pass; retry one resume | 0.18.3 | an account fact, one instance |
| a safety classifier stopped reviewers writing bypass strings | 0.18.1 | one run |
| a worktree vanished mid-preparation, cause unknown | 0.8.2 | no cause to write |
| history scrubbed before a first push by replaying commits | `run-0-25-1-1174.md` | a technique used once |
| a reframe leaves the pull request title stale | 0.25.0 | one instance; the title is a note line (`docs/branch-and-release.md` *Cutting a release*), and #1199 rewrites the title rules |
| `seal gate --record` takes the work item's path, not its id | 0.25.0 | the command refuses with exit 2 before it runs |
| commit with the `Seal-Routing` trailer from the first commit | 0.25.1 (`run-0-25-1-1148.md`) | one instance; nothing refuses its absence on a declared branch |
| a handoff or a gaps row after the guarantee goes to a pull request comment | 0.22.4, 0.25.1 (`run-0-25-1-1148.md`) | the tree says what a record commit after the guarantee costs (a sealer again), and choosing the comment is the orchestrator's judgment |
| delete worktrees and branches only after fetching `refs/pull/*`, with heads backed up | 0.11.3, 0.15.1, 0.15.3, 0.15.4, 0.15.5, 0.18.1, 0.18.2, 0.22.1 | each deletion was the owner's request, and GitHub keeps every squashed head under its pull ref |
| no colour such as "first contribution in months" in a document | 0.15.1 | one remark |
| split a build from a paid evaluation into separate spawns | 0.22.1 | one run |
| the release report reproduces locally with `release_report.py --against <tag>` | 0.25.0 | one use |
| the closure and the retirement of a record in one release range go red on `main` | 0.15.3 | the retire step is gone |

**Local.** This machine's worktree directory added to the harness's allowed directories (0.9.1); the zsh word-splitting and `$r:seal` modifier traps (0.4.0, `fold-0-15-3-run.md`, 0.18.1, 0.18.2); this clone's `origin` repointed after the rename (0.25.0); the private brand repository (`run-0-25-1-1174.md`); showing the owner a visual choice as a terminal render he types `! cat` to see (0.20.0); this machine's settings allowlist (0.8.2).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A lesson learnt in a run | Given an orchestrator that learns how an act should be done next time, when it decides where to write it, then `skills/implement/orchestration.md` *Orchestrator: where a decision or a lesson is written* names the file the act is read from, an issue, or the work item's records, and says local memory is not the place | `grep -n 'Orchestrator: where a decision or a lesson is written' skills/implement/orchestration.md`; `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py` passes with the new row |
| A run on another machine | Given a session on a machine without this memory, when it reads the repository, then each moved lesson stands at its C or R coordinate | each C change by `git grep` of its bold sentence; each R item by `seal settle`'s dry run reading this design without a refusal (`skills/settle/scripts/rule_changes.py`) |
| A fix pass enumerating a class | Given a finding naming one instance, when the crafter hands back, then its hand-back names the method its list was made by, and the proofer judges that method | `skills/agent-contract/SKILL.md` rule 12 reads so; `tests/text/test_the_agent_contract_holds_the_universal_rules.py` passes |
| A base comparison by hand | Given a failing file read `new?`, when the orchestrator or a crafter runs it at the base, then the skill points at a worktree of the base and refuses `git stash` | `git grep -n 'git stash' -- skills` names only the refusal |
| A push to a merged pull request | Given the owner merged the pull request after the seal, when the orchestrator has a repair to push, then the section has it read `state` first and stop on `MERGED` | the rewritten pin in `tests/text/test_the_rules_have_one_owner.py`, seen red against the old sentence (contract rule 15) |
| The rule changes are well formed | Given this design, when the pull request's check reads it, then every R item parses | `seal settle` dry run, and `chain-check` at the pull request (`docs/the-review-record.md` *What the check reads at the pull request*) |

## Data & interfaces

No script, schema or command changes. The interfaces are text: four skill files and one test pin in this pull request (C1 to C4), and two policy documents at the settle (R1 to R4). The orchestrator's session memory is outside the repository and is changed by nobody in this pull request.

## Rule changes

- change
  file: docs/the-review-record.md
  section: The handoff
  from: **While an agent runs, `frame/plan.md`'s Status column is the readout.** The implementer fills it with the commit that closed each phase, so the orchestrator opens it rather than asking, and the stall signal is the time since it last advanced. After the run, `skills/verify/scripts/session_cost.py` reads the transcript.
  to: **While an agent runs, the orchestrator reads the age of its transcript at least every 30 minutes, and `frame/plan.md`'s Status column says which phase it has reached.** The implementer fills the Status column with the commit that closed each phase, so the orchestrator opens it rather than asking. A phase can run for an hour, so the stall signal is the time since the agent's transcript last changed, read through the link that the harness's task output is, with `stat -L`, because the link's own time is the moment it was made. Where the transcript has not moved for 30 minutes, the orchestrator reads the agent's slowest calls with `seal cost` on that transcript and the processes the agent started, and then decides whether to stop it. A completion notice is never waited on alone: in 0.16.0 one crafter call hung for 4 h 48 min and nobody noticed (#680), and an agent can end without one. An unattended run keeps its machine awake for its whole length, and a spawn prompt asks for a probe that may run past a minute as a background command, never as a foreground `&` followed by `wait`. After the run, `skills/verify/scripts/session_cost.py` reads the transcript.
- change
  file: docs/the-review-record.md
  section: The handoff
  from: a runner the repository ships is named, not typed into every prompt, and the form handed over is the narrow one.
  to: a runner the repository ships is named, not typed into every prompt, and the form handed over is the narrow one. A place on the orchestrator's machine outside the repository, such as a scratch directory or another clone, is named in words and never by its path: an agent copies a prompt's paths into the records it writes, and the `real_identifiers` census in `tests/censuses.py` refuses them there, which in 0.18.1 and in #1174 cost a repair and once a rewrite of the branch's history.
- add
  file: docs/release-checklist.md
  section: 2b. Settle what earlier releases left behind
  to: **What `seal settle --apply` removed is committed before anything switches that checkout to another branch.** `--apply` deletes each directory from the working tree and stages nothing, and `git switch` exits 0 over an unstaged deletion while it restores every deleted file that differs between the two branches, saying nothing about it. In the 0.24 settle a switch to `main` and back restored 28 `gaps.md` files, the removal commit left them tracked, and the broad gate refused the tree. A comparison with another ref runs in a `git worktree` of that ref.
    check: none reader: the owner's settling session, at this step
- add
  file: docs/release-checklist.md
  section: 6. After the merge
  to: **The milestone `release: X.Y.Z` is closed once the close-issues run has closed its issues, by `gh api -X PATCH repos/<owner>/<repo>/milestones/<number> -f state=closed`.** Nothing else closes it: `.github/scripts/close_issues_on_release.py` closes each issue and leaves the milestone open with none in it, which reads as a release still in flight. `release: 0.20.0` stood open eleven days after its tag and `release: 0.21.0` five, each closed by hand.
    check: none reader: the orchestrator after the tag

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the sentence prescribing "`git stash`, that one file, `git stash pop`" for the base comparison | `skills/verify/orchestration.md` *The broad gate*, the paragraph opening **That comparison is reactive.** | the same paragraph, rewritten to a worktree of the base (C3) |
| the sentence "reads `gh pr view <N> --json mergeable` before it waits on CI", and the pin quoting it | `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*; `tests/text/test_the_rules_have_one_owner.py#test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge` | the same paragraph and the same case, rewritten to `state,mergeable` and every workflow's checks (C4) |
| the citation "`docs/release-checklist.md` names why not `gh pr edit`", which no file of the tree makes true | `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*, the paragraph opening **The stated limit** | the reason, stated in that sentence (C4) |
| "and the hand-back says which were enumerated." | `skills/agent-contract/SKILL.md` rule 12 | the same rule, rewritten to name the method (C2) |
| "the stall signal is the time since it last advanced" | `docs/the-review-record.md` *The handoff* | R1, at the settle |

**What goes in return for the rules this work adds.** C1, R2, R3 and R4 add rules, and the copy each replaces is outside the tree: the session memory entries the orchestrator deletes after the merge (`frame/plan.md` *Operational impact*). Inside the tree nothing can go for them, because no tree text states those facts: each was searched for and not found (*Grounding*, the facts table). C2, C3, C4 and R1 add no rule; each rewrites one in place.

Framed 2026-10-31 by framer, before the build.
