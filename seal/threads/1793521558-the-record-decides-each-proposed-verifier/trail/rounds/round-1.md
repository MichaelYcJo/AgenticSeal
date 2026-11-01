# Review round 1: 1793521558-the-record-decides-each-proposed-verifier

```seal
target: 77bd4107 against release/v0.27.2
```

The target is `77bd410781ab34ce352cf96ae2f6fe12cc3870c6`, read in a `git clone --no-local` of the branch worktree under this round's scratch directory, with `refs/pull/*/head`, the branches and the tags fetched from GitHub on 2026-11-01. `release/v0.27.2` resolves to `ad5246ce` on the remote and to `813665f0` in the worktree. `git diff --name-only 813665f0..HEAD` lists the work item's directory and `seal/follow-up.md` alone, so the advance of the base to `ad5246ce` shares no file with the branch (executed). No earlier round exists, so no fact is carried and every fact below was established this round. `seal/parity.md` is not declared, and the diff changes no path outside `docs/` and `seal/`, so the round block holds no `original:` line.

The round spent its reading on the decisions that close or file an issue, as the spawn prompt asked: C7, C12, C13 and C14 with their drafts D1, D8, D4 and D5; C9 and C10 with D6 and D7; C8 with D2; C11 with D3; and C6 with D9. The drops with no act, C1 to C5, were read for their commands and their grounds.

## Findings

### 1. Row C9 counts `hooks/lib/launch.py` among the entry points no check named, while the census reads it and holds its reason

```seal
severity: should
location: `seal/threads/1793521558-the-record-decides-each-proposed-verifier/trail/phases/phase-3.md:29`, `seal/threads/1793521558-the-record-decides-each-proposed-verifier/trail/phases/phase-3.md:501`
evidence: executed `sed -n '311,341p' trail/phases/phase-3.md | python3 -I - clone 813665f0`, `grep -n "exempt from entry_point" -r hooks`, `git show 813665f0:hooks/lib/launch.py | sed -n 103,106p`
```

Why it matters: row C9 claims "`tests/censuses.py#entry_point` reads `hooks/` alone, so no check named any of the 16", and its grounds call "the 13 absent answers" catches "wherever the rule is every entry point". *Command C9*, re-run from the record, prints the same 47 entry points and lists `hooks/lib/launch.py` among the 13 with no answer. That file stands under `hooks/`, which the census reads (`tests/censuses.py:644-664`, `_python(rel, root, ("hooks/",))`), and the census holds it by the exemption at `hooks/lib/launch.py:105`: "the launcher imports nothing before its floor check". So one of the 16 was named by the census, and its absent answer is a recorded decision, not a catch. D6 cites row C9 as its measure, so the frame of the issue D6 files would count one entry point as owing an answer that the tree already exempts with a reason. The `build` stands on the other 15, and the figures change.

```markdown
Row C9, *What the record shows*: replace "`tests/censuses.py#entry_point` reads `hooks/` alone, so no check named any of the 16." with:
`tests/censuses.py#entry_point` reads `hooks/` alone. It reads `hooks/lib/launch.py` and holds it by the exemption at that file's `__main__`, "the launcher imports nothing before its floor check", so no check named any of the other 15.

Row C9, *Grounds*: replace "The 13 absent answers are catches of the same kind wherever the rule is every entry point" with:
The 12 absent answers outside `hooks/` are catches of the same kind wherever the rule is every entry point; the thirteenth, `hooks/lib/launch.py`, carries its reason at its line

*Instances C9*, the "Give no answer" bullet: replace "`hooks/lib/launch.py`;" with:
`hooks/lib/launch.py`, which the census reads and exempts at its `__main__` with its reason;
```

### 2. Row C10's grounds say *The dependency rule* sends a writer to the `path#name` form, and that section names no such form

```seal
severity: should
location: `seal/threads/1793521558-the-record-decides-each-proposed-verifier/trail/phases/phase-3.md:30`
evidence: executed `sed -n 28,50p docs/one-root-by-lifetime.md`, `git grep -n -E 'path#name|<path>#<name>|#<function>' 813665f0 -- docs skills agents templates CONTRIBUTING.md`
```

Why it matters: the last sentence of row C10's *Grounds* reads "`docs/one-root-by-lifetime.md` *The dependency rule* says 'A record citing `path:line` breaks it', so the `path#name` form it sends a writer to is the one form no case reads". The section (`docs/one-root-by-lifetime.md:28-50`) says that nothing may need to be found and updated when something else moves, and that a `path:line` citation breaks that. It names no other citation form and sends a writer to none. The search over the policy root, the skills, the agents, the templates and `CONTRIBUTING.md` at `813665f0` finds no sentence that prescribes `path#name` (executed: no output). The placement of the case's `check:` line under that section has its own ground, #1038's comment of 2026-11-01 ("Keeping it adds a `check:` line to `docs/one-root-by-lifetime.md` *The dependency rule*", read), so D7 stands. The sentence in the grounds is a wrong reading of a policy section. Row C10 is the measure D7's issue is framed from, and a reader who re-weighs C10 would build on that reading.

```markdown
Row C10, *Grounds*, replace the last sentence with:
`docs/one-root-by-lifetime.md` *The dependency rule* says that nothing may need to be found and updated when something else moves, and that "A record citing `path:line` breaks it". A `path#name` breaks the same way when its name moves, and no case reads one. #1038's comment of 2026-11-01 places the case's `check:` line under that rule
```

### 3. Row C12 and D8 close #951 without weighing the cases #951 says the check removes, and without naming them as the open part

```seal
severity: should
location: `seal/threads/1793521558-the-record-decides-each-proposed-verifier/trail/phases/phase-3.md:31`, `seal/threads/1793521558-the-record-decides-each-proposed-verifier/trail/phases/phase-3.md:575-577`
evidence: executed `gh issue view 951 --json body,comments`, `sed -n '/^## Where it stands (2026-10-29)/,$p'`
```

Why it matters: #951's body gives its case as a saving. "Without static types, a changed return value or signature is caught only by a test that happens to call it, so the suite has been doing a type checker's job. That is part of why it grew to 13,482 cases." It also says "A case whose only job a type check now does is a candidate for removal", and *Where it stands (2026-10-29)* adds "measuring those cases is part of what the first level owes". Row C12 quotes the clause "names what it removes, here the cases whose only job the type check now does, and what those caught against what it costs" and calls it "the same weighing". The row then weighs only the shipped defects a type check would have stopped against "the 46 errors' repair, the annotations and a CI step", and D8 says the same. Neither counts the cases a type check would let go, and the open part the row names leaves them out: it names "A defect described in other words, and a latent defect a type check would find in today's tree" only. A suite that already catches type-shaped defects before the merge would by construction show none shipping past it. The catch side the row measured therefore cannot settle #951's claim, which concerns the cost side. The drop may still hold, but the record has to say that it stands on the catch side alone and that the saving was not measured, or D8 closes #951 on a weighing its own body does not make.

```markdown
Row C12, *Command or coordinate*, replace the last sentence with:
A defect described in other words, a latent defect a type check would find in today's tree, and the cases whose only job a type check would do, which #951's body names as what the check removes, are the open part (plan row A7). No case was counted

Row C12, *Grounds*, append:
The drop stands on the catch side alone. #951's saving, the cases a type check would let go, was not measured, and a count of them set against the repair reopens this question

D8, second paragraph of the quoted comment, append after "since no agent runs a type checker.":
Nor did the reading count the cases whose only job a type check would do, which this issue names as what the check removes; a count of them, set against the repair, reopens this question with that row as its baseline.
```

### 4. *Instances C7* gives withheld line 9's quote as an example of the other 47 lines and says the phase records were exact, which line 9's own reading contradicts

```seal
severity: should
location: `seal/threads/1793521558-the-record-decides-each-proposed-verifier/trail/phases/phase-1.md:252`
evidence: executed `git log --no-merges -G '^Verdict: withheld' --format=%h --glob='refs/pull/*/head' -- 'seal/*guarantee.md'`, `git show --format= 245502810 -- 'seal/*guarantee.md'`
```

Why it matters: *Instances C7* says "Most of the other 47 lines name the orchestrator's pull request body. Several of those overstate what the phase records said, such as 'every unit added was broken once and came back red', while the phase records were exact." Part (b) of *Command C7*, re-run over the fetched heads, finds that phrase in one withheld line only: line 9, at `245502810` in PR #1004. The record counts line 9 among the five lines that name a crafter's claim, not among the other 47. Its full text also names round 1 finding 1's close, "Each new condition was mutated red", as resting "on a case that has pinned none of its conditions since" `c4aa0c8b`. So the record's example of an exact phase record is the one line whose crafter's claim the same paragraph's list judges as not holding at the sealed commit. D1 points #1048's next reader to *Instances C7* as the baseline for reopening the question, so the example would mislead that reader about which claims held. Another of the 47 shows the overstatement without the contradiction. It names a pull request body's "the other three were fixed" where `phases/phase-2.md:20-21` reads "1 and 2 deferred to the frame, 3 and 4 fixed".

```markdown
Most of the other 47 lines name the orchestrator's pull request body. Several of those overstate what the records said, such as a body's "the other three were fixed" where its phase record reads "1 and 2 deferred to the frame, 3 and 4 fixed".
```

## Confirmations

```seal
confirms: none
```
What matched: C7 closes #1048 on the record its row cites. *Command C7* (a), re-run from `trail/phases/phase-1.md:72-97` in the clone, printed `84 guarantees; 1255 rows of Claims re-run; 263 on a seen-red or mutation claim` and the same four `does not hold:` lines (executed). Part (b) over the heads fetched this round printed 53 distinct withheld lines, against the record's 52. One more pull request head stood by the time of this fetch. The six lines matching the record's search are the record's six, with its line 50 now line 51 (executed). Line 14's verdict names the smith's sweep claim, as *Instances C7* says. The labels D1 cites stand as `skills/verify/SKILL.md:233` *4. Each claim labelled executed, read or unverified* (read), and #1048 is open in `backlog: review chain & agents`, as D1's home sentence says (executed: `gh issue view 1048`). The drop follows from the decided-by sentence *Scope* item 2 gives C7. The re-run sample's own rate, two withheld verdicts on a crafter's claim among 1,255 rows, is what the row rests the premise for keeping the sample on.

```seal
confirms: none
```
What matched: C13 closes #27. #27's body holds the seven rows and three checkboxes *Instances C13* answers, and its comment of 2026-10-31 says the premise "every gate watches a commit" is stale (executed: `gh issue view 27 --json body,comments`). *Command C13*'s greps printed `hooks/dispatch.py:84`, `:87`, `:88` and `chain_check.py:1516` as the record shows (executed). D4 answers each of #27's checkboxes. Its first is "whether a session's procedure is something this plugin gates at all", and its third is "The ones nobody can catch are the ones to rewrite or drop". #27 stands in `release: 0.27.2`, so `Closes #27` carries it (executed).

```seal
confirms: none
```
What matched: C14 closes #6. *Command C14*, re-run from `trail/phases/phase-2.md:261-311` against the merged pull requests read from the tracker, printed the five findings and `137 findings in rounds after the first; 5 ...` (executed). #6's test is quoted exactly in row C14 and D5: "Run three review rounds under the floor rule. If axes keep leaking, the pass has earned its place". #6's second checkbox, the `security-audit` heading, left with that skill as #6's comment of 2026-10-31 says (executed: `gh issue view 6 --json body,comments`). The row calls its list a sample and names the open part, as contract rule 12 asks.

```seal
confirms: none
```
What matched: C11 keeps #1020 on its own comment's test. *Command C11*, re-run, printed `111 findings, 30 recurring: 10 in the records alone, 20 reaching shipped text` (executed). The sentence row C11 quotes, "where the records-alone count falls and recurrences remain in shipped text, the exchange is the case to make", is #1020's comment of 2026-10-30 word for word, and the 0.24.0 split it compares with, 12 of 17 in the records alone, is #1020's comment of 2026-10-29 (executed: `gh issue view 1020 --json comments`). #1228 is closed in `release: 0.27.1` and #1240 is open in `backlog: gates & hooks`, as *Instances C11* says (executed).

```seal
confirms: none
```
What matched: C9 and C10 are `build` on the frame's definition of a catch, and C3 to C6 are `drop` on the same definition. *Scope* item 2 defines a catch as "a defect the record shows reaching a merge, a release or a later work item". *Command C9* and *Command C10*, re-run from the record at `813665f0` and `bf9efcba`, printed the same 47 entry points with the same five-line tally, and `path#name coordinates 113; not defined 2` at both commits (executed). Those instances stand in shipped text and reached releases. C3, C4, C5 and C6 each show only planted probes, and *Command C3*, re-run with `--until`, printed `449 | Automation | yes |` and `4 | Automation | no |` (executed). The line between building and dropping is drawn the same way across the seven rows. #1038's comment of 2026-11-01 says "neither has a catch of its own", and that sentence means neither check has run yet. It does not deny the standing instances (executed: `gh issue view 1038 --json comments`).

```seal
confirms: none
```
What matched: the claim of *Scope* item 4 and of the phase 3 record holds, that the `console.to_utf8()` row left `seal/follow-up.md` whole into D6. The row removed by `git diff 813665f0..HEAD -- seal/follow-up.md`, its answerer cell taken off, is byte for byte the text D6 quotes at `trail/phases/phase-3.md:539` (executed: `diff` of the two, `IDENTICAL`). D6 answers the row's second question ("whether the existing case's corpus widens") as decided by #1038. The owner gave the row's home to #1038 in the comment of 2026-11-01, "its home becomes this issue's decision", and kept the first question, which entry points owe the call, for the owner in D6. D6's citations of `CONTRIBUTING.md` *House rules* and `skills/settle/scripts/rule_changes.py#parse` stand at `CONTRIBUTING.md:430` and `rule_changes.py:100` (read).

```seal
confirms: none
```
What matched: D9's counts. #956's audit comment, read on 2026-11-01, gives "8 refuse, 3 pass, 7 skip, 24 are mixed, and R36 has not landed" and "18 yes, 7 limit and 17 no". D9 gives R36 `mixed` and `yes`, which makes 25 mixed and 19 yes over the same 43 rows, and its list of yes rows inserts R36 in order (executed: `gh api repos/MichaelYcJo/AgenticSeal/issues/comments/6464014816`). D9's row has the audit's seven columns.

```seal
confirms: none
```
What matched: C2's counts and the two merges with no verifying round. *Command C2*, re-run, printed `57 work-item pull requests; 12 merges of the base, 11 after a round, 3 resolving a file outside the records; 187 round records name 447 commits on target: lines, 0 not an ancestor of the pull request's head` (executed). The heads of #1136 and #1202 are `2106d2e9` and `a8563a34`, the two merges the record names (executed: `gh pr view`). *Command C8* printed `32 distinct sides, 544.17 USD, 24.4 hours of wall time` (executed). *Command C1*'s tracker part printed `182`, the three label counts and `[911]` (executed). *Command C12*'s tracker part printed the 15 titles, `22` and the five commit subjects (executed). The bodies of #463, #661, #226, #142 and #175 say what *Instances C12* says of each (executed: `gh issue view`).

```seal
confirms: none
```
What matched: the crafter's claim that phase 3's boundary set exited 0 with 278 passed. The same command, run in the clone at the target through `bin/test`, exited 0 with `278 passed` (executed). The suite stays labelled `unverified` in `gaps.md` with the orchestrator as its answerer, and that label is honest: no phase ran it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether C8's `narrow` keeps the smoke run on G1's test. The row says the suite's one recorded catch is "already held by a check", the proofer's read through `chain_check.py` at `agents/proofer.md` step 7. Its ground for keeping a smoke run, against removal, is that removal "would leave 13 `check:` lines naming cases nothing keeps". G1 says existing is no reason to keep a mechanism, so the question is whether those cases, as the named checks of 13 rules, are a premise of their own or the cost of a change. That is a weighing of meaning this round did not settle | `seal/threads/1793521558-the-record-decides-each-proposed-verifier/trail/phases/phase-1.md:25`, D2 | the repository owner, at the pull request, before D2 is filed |
| The commands this round did not re-run: *Command C1*'s tag loops, *Command C4*, *Command C5*, *Command C6* (a) and (b), *Command C7* (c), and the per-instance reads behind *Instances C1*, *C4* and *C8* | `trail/phases/phase-1.md`, `trail/phases/phase-3.md` | the sealer, in its sample of the crafter's `executed` claims |
| How `claude plugin eval` reads a `not_contains` grader whose target file is absent (C5), which only a paid run answers | `gaps.md` *Not verified* | the repository owner, by one eval run in a release where paid runs are taken |
| The broad gate at HEAD: the full suite, the repository-wide lint and the format check | `seal/config.md` `Broad gate` row | the orchestrator, by `seal gate` |
| The tracker acts the drafts hold (milestone `release: 0.30.0`, D1 to D9, #1038's body, the `Closes` lines), none taken; each draft was read against its decision only | the three phase records, `### Drafts` | the orchestrator, after the seal |

## Probes

| Command | Result |
|---|---|
| `git clone -q --no-local` of the branch worktree, checkout of `77bd4107`, then `git fetch` of `refs/pull/*/head`, `refs/tags/*` and `refs/heads/*` from GitHub | the clone at the target, 309 pull request heads; the worktree was not written |
| *Command C9* and *Command C10* piped from `trail/phases/phase-3.md:311-341` and `:372-401` into `python3 -I -` at `813665f0` and `bf9efcba` | 47 entry points, the same tally at both commits; 113 names, 2 not defined, at both |
| *Command C7* (a) and *Command C8* piped from `trail/phases/phase-1.md:72-97` and `:143-169` | 84 guarantees, 1,255 rows, 263 on a seen-red or mutation claim, four `does not hold:` lines; 32 sides, 544.17 USD, 24.4 hours |
| *Command C7* (b) over the fetched heads | 98 commits, 53 distinct withheld lines, one more head than the record's fetch; the six matching lines are the record's |
| *Command C2*, *C11* and *C14* piped from `trail/phases/phase-2.md`, with the merged pull request list from `gh pr list` passed through process substitution | the record's printed totals, line for line |
| *Command C3*'s first command | 449 `yes`, 4 `no` |
| *Command C1*, *C12* and *C13*'s tracker and grep parts | 182 and the label counts, `[911]`; 15 titles, 22 issues, five subjects; the four lines of `dispatch.py` and `chain_check.py` |
| `bin/test -q -p no:xdist` over phase 3's boundary set in the clone | exit 0, 278 passed |
| `diff` of the removed `seal/follow-up.md` row against D6's quote | identical |
