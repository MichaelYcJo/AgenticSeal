# Review round 1: 1795849900-merge-owes-what-it-can-catch

```iadd
target: 561bc67a against release/v0.42.0
```

A finding round over the whole branch, `596c79a6..561bc67a`. No earlier round exists, so no coordinate or verdict was carried from one. The facts this round carried from the frame without running them again are the framer's `gh` reads: the issues' comments (G2), the rulesets and their `non_fast_forward` rule (G10, G26), and the release body at `v0.41.0` (G22). Every other fact named below was opened or run at the target.

## Findings

### 1. The stand-in for the broad run accepts a HEAD where the job judged to stand in was skipped

```iadd
severity: should
location: `skills/code-review/orchestration.md:335-347`, `agentory/threads/1795849900-merge-owes-what-it-can-catch/frame/design.md:79`, `agentory/threads/1795849900-merge-owes-what-it-can-catch/changelog.md:4`, `agentory/threads/1795849900-merge-owes-what-it-can-catch/frame/plan.md:50`
evidence: read `skills/code-review/scripts/pr_wait.py:293-301`, `skills/code-review/gate-to-pull-request.md:40`, `skills/code-review/orchestration.md:335-347`; executed `git grep -n -F 'pr-wait' -- skills/code-review/orchestration.md skills/core/SKILL.md agentory/threads/1795849900-merge-owes-what-it-can-catch`
```

Why it matters: the paragraph's third condition is that "`agentic pr-wait <N>` exits 0 at HEAD" (`skills/code-review/orchestration.md:340`). `pr_wait.py#decide` (lines 293 to 301) returns exit 0 where "every check passed or was skipped", and its output on exit 0 is that one line, with no check named. The table row at `skills/code-review/gate-to-pull-request.md:40` says the same. So exit 0 does not establish that the job the orchestrator judged to run the `Broad gate` command's checks ran at HEAD. A job with a job-level `if:` that is false for this pull request is reported as skipped. This repository has one: `pytest-wide` skips a pull request into `release/*` (`.github/workflows/test.yml:175`). Here the job that stands in is `pytest`, which carries no job-level `if:`, so this repository is not exposed today. A repository whose only full-suite job is conditioned the same way would pass all three conditions with no suite run over the merged tree. The second condition, the judgment read in the workflow files, catches this only where the orchestrator reads the `if:` against this event. Whether the job ran at HEAD is a fact `gh pr checks <N>` prints exactly, as its `bucket`, the field `pr_wait.py` already reads (`docs/running/what-a-script-gates.md:106`). `skills/core/SKILL.md` *The first value* gives such a fact to an exact read rather than to a judgment. D7's row already names "the workflow and job whose run stood in", so the fix asks for no new record.

The search printed the statements of the condition: the paragraph at line 340; D4, S1 and the *Removes* row of `frame/design.md` (lines 79, 63, 102); A1, *Technical context* and *Operational impact* of `frame/plan.md` (lines 21, 10, 50); and `changelog.md:4`. The snippet covers line 340, D4, `changelog.md:4` and `plan.md:50`, the statements that give the conditions as sufficient. S1, A1 and the plan's *Technical context* summarise the stand-in, and the fix pass weighs each against the amended D4. The search is a sample under contract rules 12 and 19, since a statement in other words escapes it.

```markdown
<!-- skills/code-review/orchestration.md, the sentence at line 340, replaced whole -->
exist* judges an answerer. And `agentic pr-wait <N>` exits 0 at HEAD, where
HEAD is the merge commit or a commit after it that changes only the work
item's records, and `gh pr checks <N>` lists as passed, not skipped, each
job the orchestrator judged to run those checks, because the wait's exit 0
counts a skipped check as one that passed.

<!-- frame/design.md D4, after "(G12)" -->
and `gh pr checks <N>` lists as passed, not skipped, each job the orchestrator judged to run those checks, because the wait's exit 0 counts a skipped check as one that passed (`skills/code-review/scripts/pr_wait.py#decide`)

<!-- changelog.md:4, after "that changes only the work item's records" -->
, with each job that stands in listed by `gh pr checks <N>` as passed and not skipped

<!-- frame/plan.md:50, "and `agentic pr-wait` exits 0 at HEAD" becomes -->
and `agentic pr-wait` exits 0 at HEAD with the job that stands in passed, not skipped
```

The snippet assumes no OS boundary. `gh pr checks <N>` reads the pull request's head, which equals HEAD wherever the wait has exited 0, since the wait ends at exit 3 once the head leaves HEAD.

```iadd
verdict: fixed dcfbfbc8
answer: The stand-in's third condition in `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the work item is cleared* now also asks `gh pr checks <N>` to list as passed, not skipped, each job the orchestrator judged to run the `Broad gate` command's checks, in the snippet's words, and the paragraph on a merge after the verdict spawns the inspector "once its conditions above hold at HEAD" in place of "after `agentic pr-wait <N>` exits 0", as the fold at `ca3a10bc` states D6. `changelog.md:4` and the second process row carry the condition. The framer folded D4, S1, the *Removes* row, A1, *Technical context*, *The failure direction* and *Operational impact* at `ca3a10bc`. The owner case `tests/text/test_the_rules_have_one_owner.py#test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge` pins `` `gh pr checks <N>` `` by contract rule 14: red before the fix ("the owner section no longer says '`gh pr checks <N>`'"), and `red` under `agentic mutate` with the paragraph's `` `gh pr checks <N>` `` replaced at `dcfbfbc8`. The evidence's `git grep -n -F 'pr-wait'`, run again at `dcfbfbc8` over the same paths, prints these lines that do not carry the condition, each of which stands: `skills/core/SKILL.md:109`, whose *Held by* cell names `agentic pr-wait` as the holder, not the conditions, and has no room under `lib/core.py#CAP` (`gaps.md` `## Not done`); `changelog.md:5`, which describes that row; `trail/phases/phase-1.md:7`, which quotes the row at `1c332307`; `frame/plan.md:30`, A10, which is about the base commit; `frame/questions.md:16` and `pr.md:7`, Q2's option (a) and its quote, which name the holder; and `gaps.md:8`, which names the stand-in's three conditions, still three. The narrow set `bin/test tests/skills/test_chain_check.py tests/text tests/behaviour tests/lib/test_core.py tests/hooks/test_core_start.py tests/github/test_release_report.py tests/skills/test_pr_wait.py tests/skills/test_pr_body.py tests/skills/test_settle.py -q` printed 1554 passed, 10 skipped, with `uvx ruff check` and `uvx ruff format --check` over the test file clean; every file of it is the `bin/test` suite's, which phase 1's *Verified by* cell names.
location: `tests/text/test_the_rules_have_one_owner.py`
```

### 2. The exit 0 row of the step file has the orchestrator treat the pull request as checked without the ancestry read D5 sets before that act

```iadd
severity: should
location: `skills/code-review/gate-to-pull-request.md:40`, `agentory/threads/1795849900-merge-owes-what-it-can-catch/frame/design.md:55`
evidence: read `skills/code-review/gate-to-pull-request.md:1-8`, `skills/code-review/gate-to-pull-request.md:24-46`, `skills/code-review/orchestration.md:349-364`, `skills/code-review/SKILL.md:15-18`; executed `git grep -n -F 'treats the pull request as checked' -- skills agents docs agentory/threads/1795849900-merge-owes-what-it-can-catch`
```

Why it matters: the D5 paragraph says "before the orchestrator treats the pull request as checked and ends its run, it fetches the base and runs `git -C <root> merge-base --is-ancestor <base> HEAD`" (`skills/code-review/orchestration.md:352-354`). The act it conditions is written as an instruction in another file. `skills/code-review/gate-to-pull-request.md:40` gives exit 0 of `agentic pr-wait` as "treats the pull request as checked at HEAD", with no condition. That file is the one the orchestrator opens "once the last round record has no finding open" (`skills/code-review/SKILL.md:15-18`). Its opening says it "holds the steps that get it there and the repairs an open pull request takes" (lines 6 to 8). The hand-over is one of those steps, and D5 is the stand-in's only guard against a base that moved after the run. A session that resumes at the open pull request, with that file open, follows the row and ends its run without the read. The frame weighed this at `frame/design.md:55` and kept the row as it was, so that D5's read "stands once". A citation in the row keeps the read in one place, and the row then stops contradicting the paragraph. The search printed the paragraph and the row, and in the records D5, S8 and `changelog.md:4`. Those say what the paragraph says and need no change. The search is a sample under contract rule 12.

```markdown
<!-- skills/code-review/gate-to-pull-request.md:40 -->
| 0 | every check on HEAD passed or was skipped; under `--once`, the pull request is open | treats the pull request as checked at HEAD, except after a merge whose broad run the pull request's checks stood in for, where it first takes the read of the base `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the work item is cleared* gives that stand-in; under `--once`, pushes |

<!-- frame/design.md:55, the Out of scope bullet, replaced -->
- **`skills/code-review/gate-to-pull-request.md`** beyond its `agentic pr-wait` table's exit 0 row: D5's read stands once, in Scope item 1's paragraph beside the stand-in it qualifies, and the exit 0 row cites that paragraph where the stand-in was taken.
```

Rule 14 and *Scope* are the fix pass's to weigh: the row is a sentence an agent acts on. The owner case `tests/text/test_the_rules_have_one_owner.py#test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge` already reads this file's steps beside the owner section, so the fix pass can pin the citation there. The *Scope* list then names the row.

```iadd
verdict: fixed dcfbfbc8
answer: Built to `frame/design.md` *Scope* item 9, which the fold at `ca3a10bc` added, and to its *Out of scope* bullet rewritten there. The exit 0 row of `skills/code-review/gate-to-pull-request.md`'s `agentic pr-wait` table now reads "treats the pull request as checked at HEAD, except after a merge whose broad run the pull request's checks stood in for, where it first takes the conditions `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the work item is cleared* gives that stand-in". It says "the conditions" where the paste-ready fix says "the read of the base", because *Scope* item 9 sends the orchestrator to the conditions D4 and D5 give, and finding 1's added condition is one of them. `changelog.md:4` names the row. The owner case pins the row's exception by contract rule 14: `agentic mutate` at `dcfbfbc8`, with the exception taken out so the row reads as it stood at the round's target, printed `red`, failing at the row's assertion. The evidence's `git grep -n -F 'treats the pull request as checked'`, run again at `dcfbfbc8`, prints the row, `skills/code-review/orchestration.md:356` (D5's paragraph), and in the records `changelog.md:4`, `frame/design.md:70` (S8) and `frame/design.md:81` (D5), each of which says what the paragraph says.
location: `tests/text/test_the_rules_have_one_owner.py`, `agentory/threads/1795849900-merge-owes-what-it-can-catch/changelog.md`
```

### 3. R1's `to` says that everything a merge owes is read from what its resolution changed, while only the round is

```iadd
severity: should
location: `agentory/threads/1795849900-merge-owes-what-it-can-catch/frame/design.md:90-96`
evidence: read `agentory/threads/1795849900-merge-owes-what-it-can-catch/frame/design.md:79-81`, `skills/code-review/orchestration.md:315-376`; executed `git grep -n -F "read from what the merge's" -- agentory docs skills`
```

Why it matters: the settle writes R1's `to` into `docs/releasing/branch-and-release.md` *Work accumulates on a release branch*, a policy document read after this work item's directory is gone. The sentence lists "a round on its resolution, the broad run again or the pull request's checks at the merge in its place, and the inspector again", then closes with "read from what the merge's resolution changed". The participle attaches to the whole list. But the paragraph it cites says "The stand-in applies whatever the command above names" (`skills/code-review/orchestration.md:342`). It also owes `agentic pr-body` and the inspector after any merge past the verdict (lines 366 to 376). So the broad run, the stand-in and the inspector do not depend on what the resolution changed. A reader of the settled section who sees a clean merge reads that nothing but the round is in question, which is the opposite. The phrase "at the merge" is also narrower than the paragraph's "at HEAD, where HEAD is the merge commit or a commit after it that changes only the work item's records". The search printed line 95 alone. The sample under contract rule 19 reaches no other statement of R1's wording.

```markdown
- change
  file: docs/releasing/branch-and-release.md
  section: Work accumulates on a release branch
  from: The merge still moves HEAD past the work item's broad run and inspection, and the orchestrator then runs both again (`skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the work item is cleared*).
  to: The merge still moves HEAD past the work item's broad run and
    inspection. What the merge owes then is
    `skills/code-review/orchestration.md` *Orchestrator: the pull request
    opens once the work item is cleared*'s: a round where the merge's
    resolution changed a path outside the work item's records, the broad
    run again or the pull request's checks in its place, and the inspector
    again.
```

G25 records that `rule_changes.py#parse` read R1 as written on 2026-11-28. The fix pass runs that parse again over the amended `to`.

```iadd
verdict: fixed ca3a10bc
answer: The framer folded it: `ca3a10bc` rewrote R1's `to` in `frame/design.md` `## Rule changes` as the paste-ready fix gives it, and G25 records its parse at `1ff9417e`. This pass ran `skills/settle/scripts/rule_changes.py#parse` again over `frame/design.md` at `dcfbfbc8` with the policy root `docs`: it printed one `change` for `docs/releasing/branch-and-release.md` *Work accumulates on a release branch* with the new `to`, `errors=[]` and `unread=[]`. The evidence's `git grep -n -F "read from what the merge's" -- agentory docs skills`, run again at `dcfbfbc8` outside this record, prints nothing.
```

### 4. `gaps.md` and the phase record say *Scope* item 2 asks for the sentence the fold at `41455989` took out of it

```iadd
severity: should
location: `agentory/threads/1795849900-merge-owes-what-it-can-catch/gaps.md:12`, `agentory/threads/1795849900-merge-owes-what-it-can-catch/trail/phases/phase-1.md:7`
evidence: executed `git diff 1c332307 41455989 -- agentory/threads/1795849900-merge-owes-what-it-can-catch/frame/design.md`, `git grep -n -F "Scope* item 2 asks" -- agentory/threads/1795849900-merge-owes-what-it-can-catch`; read `agentory/threads/1795849900-merge-owes-what-it-can-catch/frame/design.md:41`, `skills/code-review/scripts/pr_body.py:14-15`
```

Why it matters: `gaps.md:12` says the core's row "does not carry the sentence `frame/design.md` *Scope* item 2 asks of its *What it protects* cell, that the run is read over the branch's own commits". At the target, *Scope* item 2 (`frame/design.md:41`) asks for no such sentence. The fold at `41455989` replaced it with "The row holds no more than that, because the core the hook prints stays under `lib/core.py#CAP`". The diff of that commit shows the earlier text going out. `gaps.md` states the present, and `agentic pr-body` copies its `## Not done` section into the pull request body (`skills/code-review/scripts/pr_body.py:14-15`). There the owner, and the inspector reading the body's copy of the records, find a *Not done* item for a request the frame at HEAD no longer makes. The phase record's heading at `trail/phases/phase-1.md:7` says the row uses "fewer words than *Scope* item 2 asks". That heading was true of the frame the phase built against, at `e22357f1`, and names no commit for it. The search printed these two lines alone. The rest of the memo, the 10,332 and 9,995 figures and the cap's grounds, holds at the target (see *Confirmations*), and the memo's paragraph still tells a reader why the row says less.

```markdown
<!-- gaps.md:12, the opening clause -->
The row *No inspection without the broad run* of `skills/core/SKILL.md` *Judgment is not licence to skip a party* does not carry the sentence `frame/design.md` *Scope* item 2 asked of its *What it protects* cell before the fold at `41455989`, that the run is read over the branch's own commits, nor the citation of `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the work item is cleared*.

<!-- trail/phases/phase-1.md:7, the bold heading -->
**Departure: the core's row says the merge's part in fewer words than *Scope* item 2 asked at `e22357f1`.**
```

```iadd
verdict: fixed dcfbfbc8
answer: Both lines now read as the paste-ready fix gives them: `gaps.md:12` says what *Scope* item 2 asked "before the fold at `41455989`", and the heading of `trail/phases/phase-1.md:7` says "asked at `e22357f1`". The same commit rewrote `gaps.md:8`, whose "The owner case holds the reading's command alone" finding 1's and finding 2's pins made false; it now names the two commands and the exit 0 row's exception the case holds. The evidence's `git grep -n -F "Scope* item 2 asks" -- agentory/threads/1795849900-merge-owes-what-it-can-catch`, run again at `dcfbfbc8` outside this record, prints nothing. Read of the range: `agentic range agentory/threads/1795849900-merge-owes-what-it-can-catch --from 561bc67a --out <scratchpad>/1795849900-merge-owes-what-it-can-catch/fix-1/range.txt` printed `agentic range: 561bc67a2a6acce79a7f6f6289a35ce8dad3ae28..dcfbfbc89ce21cda21815518bf7a372fa52a71ab` and wrote 719 lines, read to the last; it left no statement HEAD contradicts in a file this pass writes.
```

## Confirmations

What matched: *Data & interfaces* D1 holds. A probe in a scratch repository ran `git show --remerge-diff --ignore-submodules=none --format= --name-only <merge>` with git 2.54.0. It printed `w.txt` and `x.txt` for a merge with a conflict resolved by taking one side and a modify/delete conflict resolved by deleting. It printed nothing for a clean merge, and nothing for `y.txt`, which only the base had changed. It printed `z.txt` for a clean merge amended by hand, which is a file no side conflicted on (executed, *Probes*). The paragraph's claim that the command names "a path resolved by hand, and no path for a clean merge or for a file git merged on its own" matches what the probe printed, and so does its claim that a merge whose command does not run is treated as one whose resolution changed a path outside the records (`skills/code-review/orchestration.md:315-334`).

What matched: D5's `<base>` cites `skills/verify/scripts/broad_gate.py#resolve_base` (line 534), which resolves a branch to `<given>@{upstream}`, then to `refs/remotes/origin/<given>`. A fetch moves both, so the ancestry read after the fetch reads the base as it now stands (read, lines 534 to 580). The claim that exit 0 means every run at HEAD tested the tree a merge into the current base gives follows from the base being an ancestor of HEAD. The framer's G26 probe, which this round carried and did not re-run, shows the same.

What matched: *Scope* item 4's case `Test_broad_gate.test_reads_the_branchs_own_commits_across_a_merge_of_the_base` passes (executed). The phase record claims it is red with `f"^{base}"` taken out of `chain_check.py#follows`. The same `agentic mutate` run printed `red: the cases failed against the mutation (exit 1)`, failing at the first `chain.broad_gate` assertion, which names the base's commit touching `g.txt` (executed). The case's docstring claims it holds the inspection arm too. The phase record names only the broad gate line red, and the probe `test_tmp_inspection_across_merge.py` ran the inspection assertion alone against the same mutation. It failed with "the inspection has lapsed: commit 9382520e after its commit touches `g.txt`, outside the closing records" (executed). So the case pins `^<base>` for both arms. Its last assertion repeats the closing assertion of `test_lets_the_records_follow_the_run_and_refuses_any_other_path` after a merge of the base. *Scope* item 4 asks for it, and it holds that a commit of the branch's own after the merge is still listed. It is no finding.

What matched: *Scope* item 5's assertion in `tests/text/test_the_rules_have_one_owner.py:652-655` fails under `agentic mutate` with D1's command deleted from the paragraph, as the phase record claims (executed). The docstring names #1583 and #1631 (read, lines 607 to 611).

What matched: the phase record claims the hook's whole output is 9,995 characters at `1c332307`. `lib/core.py#whole` measured 9,995 at the target, at a plugin root of `lib/core.py#ROOT_ROOM` characters, against `lib/core.py#CAP` 10,000. `tests/lib/test_core.py` passes (executed). The core row's text at `skills/core/SKILL.md:109` is the text the phase record quotes (read).

What matched: the phase's *Verified by* cell, run in the round's clone. `bin/test tests/skills/test_chain_check.py tests/text tests/behaviour tests/lib/test_core.py tests/hooks/test_core_start.py -q` printed 1180 passed and 10 skipped. `uvx ruff check` and `uvx ruff format --check` over the two test files exited 0 (executed). The other files the phase record lists were not run. They are the orchestrator's broad run, which `gaps.md:7` labels honestly as not verified, with the orchestrator as its answerer.

What matched: S7 holds. `git show --stat 7ec496f0` names `.claude-plugin/plugin.json` and `changelog.md`, and the version reads `0.42.0` (executed). No other version file of the tree reads `0.41.0` (executed, `git grep -n '0\.41\.0' -- .claude-plugin '*.json' '*.toml'`).

What matched: *Scope* items 3, 6 and 7 stand as the frame states them: `skills/verify/SKILL.md:268`, the new row of `agentory/follow-up.md` and `changelog.md` with its `### Process changes` table (read). The phase record's re-pointed sentence ("which the paragraphs above on merging the base hold to their own rule", `skills/code-review/orchestration.md:392-393`) holds against the split paragraph (read). The phase record's line span for G3's paragraph, 303 to 320 at `0148aa63`, is right. The frame's 321 is the blank line after it (executed, `git show 0148aa63:skills/code-review/orchestration.md`). `tests/behaviour/test_a_cited_section_stands_in_its_file.py` passes over the new citations of `agents/proofer.md` and `skills/verify/SKILL.md` (executed).

What matched: a search of the tree for other statements of the old rule ran beyond the frame's G24 sample: `git grep -n -i -E` on merge and re-run phrasings over `skills`, `agents`, `docs`, `templates`, `hooks`, `lib`, the READMEs and `CONTRIBUTING.md` (executed). It found `skills/code-review/gate-to-pull-request.md:60`, "a merge from the base or any other repair". That sentence agrees with D6. It found no other statement that a merge owes the broad run whatever happens. The search is a sample under contract rule 12.

What matched: record against another work item's frame. The unsettled designs in the tree, `1795841828-settle-only-release-note` and `1795841830-find-leftovers-before-a-round`, change `docs/releasing/branch-and-release.md` *Cutting a release*, `docs/releasing/release-checklist.md` *After the merge*, `docs/checks/the-fold.md` and `docs/layout/the-record-layout.md`. None of them names *Work accumulates on a release branch* (executed, a `grep` of each `## Rule changes` `file:` and `section:` line), as G21 states.

What matched: `pr.md`'s six quotes stand word for word at `frame/questions.md` Q1 and Q2 and at `frame/plan.md` *Judgments of the run* (read). `Commit and pull request language` is English, so no `pr.<lang>.md` is owed. The attribution line ends `pr.md` as it ends the release's other `pr.md` files, its mark the character U+1F916 (read). `gaps.md` is new in this range, so no row of it was taken out (read). `agentory/parity.json` is absent, so no parity comparison is owed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether this repository's `pull_request` run reads each check the `Broad gate` command runs. The command's suite is `tests/run_tests.py`, and the `pytest` job runs `pytest tests/`. This round did not compare what the two collect. It is the judgment D4 gives the orchestrator at a merge, written in D7's row | `.github/workflows/test.yml`, `agentory/config.json` | the orchestrator, at the merge's *Judgments of the run* row |
| Whether an orchestrator follows the new paragraphs. This round read their text for one reading each (findings 1 to 3). No reading of text shows an agent's behaviour, which `gaps.md:8` hands to the proofer's rounds | `skills/code-review/orchestration.md:315-376` | the inspector, at the *Judgments of the run* row of the first work item whose run holds such a merge |
| #1631's owlery figures (G17) | `frame/design.md:25` | the repository owner |
| Q1 and Q2, open with their defaults taken | `frame/questions.md:15-16` | the repository owner |
| The broad gate: the full suite, the repository-wide lint and the format check | `gaps.md:7` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `sh <scratchpad>/1795849900-merge-owes-what-it-can-catch/round-1/test_tmp_remerge.sh <scratchpad>/1795849900-merge-owes-what-it-can-catch/round-1/remerge-repo`, git 2.54.0 | take-one-side and modify/delete resolution: `w.txt`, `x.txt`; clean merge: nothing; clean merge amended by hand: `z.txt`; each exit 0 |
| `bin/test tests/skills/test_tmp_inspection_across_merge.py -q -p no:xdist` in the round's clone, with `f"^{base}"` taken out of `chain_check.py#follows` by an edit, then restored | 1 failed: the inspection arm names commit 9382520e touching `g.txt` |
| `bin/agentic mutate skills/code-review/scripts/chain_check.py --replace <the rev-list with ^base> <without it> --tests "bin/test tests/skills/test_chain_check.py -q -p no:xdist -k test_reads_the_branchs_own_commits_across_a_merge_of_the_base"` | `red: the cases failed against the mutation (exit 1)`, at the first `chain.broad_gate` assertion |
| `bin/agentic mutate skills/code-review/orchestration.md --replace <D1's command> '' --tests "bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -k test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge"` | 1 failed |
| `lib/core.py#whole` over the target's core at a root of `ROOT_ROOM` characters | 9995 |
