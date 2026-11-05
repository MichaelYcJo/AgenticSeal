# Review round 3: 1793853197-a-bare-commit-goes-or-states-its-reason

```seal
target: 9591cb4e, fixes 881fad6d..9591cb4e
```

This is a verifying round. It reads the range after the sealer withheld at
34f93a4a (`guarantee.md`, the last `Verdict:` line, committed at 881fad6d).
The range holds three commits. a9d9f64a merges `release/v0.32.4` at
703ab88c, #1382's squash, and this round read the lines that merge added.
caab8bc0 removes the seen-red sentence at
`tests/behaviour/test_chain_hooks_hardening.py:443` and counts the line in
`changelog.md`, `gaps.md` and an addendum to `trail/phases/phase-1.md`.
9591cb4e folds `frame/design.md` D1 row 47, *Scope*, *Grounding* and
`frame/plan.md`. Round 2 closed no finding, so no `confirms:`, `reopens:`
or `regression:` line is owed to an earlier finding.

The narrow runs at HEAD went through `bin/test` in the branch worktree,
which holds the local feature branch that contains 3538fd59, so the case
there reads the refs that refused the line. The runs at a9d9f64a went in a
`git clone --no-local` of the branch in the session scratchpad, under
`1793853197-a-bare-commit-goes-or-states-its-reason/round-3/`. The clone and
every file the round made there were removed before hand-back. The worktree
was not changed except by this record.

Carried, not re-established: round 1's and round 2's confirmations of the
branch up to 022242a0, since the range touches none of what they cover but
`tests/behaviour/test_chain_hooks_hardening.py`, which this round read. The
coordinate `:445` at 703ab88c came from `guarantee.md` and was opened again
here. Every claim about the merged tree below was run this round.

The implementer's account was read as claims. The addendum to
`trail/phases/phase-1.md` claimed that `git for-each-ref --contains
3538fd59` lists only a local feature branch, that the two narrow modules
gave 17 and 28 passed after the edit, that M1 and M2 on the merged tree list
the same 18 and 33 tokens as at 43b9b1be, and that the merge's added lines
outside `seal/` hold only 3538fd59 and the work item id 1790644505. Each is
answered under `## Confirmations` by what this round ran.

## Findings

### 1. The frame's other statements of D1's totals still give the counts from before row 47, so D2's catch record says 34 where the changelog says 35

```seal
severity: should
location: `seal/threads/1793853197-a-bare-commit-goes-or-states-its-reason/frame/design.md:29`, `seal/threads/1793853197-a-bare-commit-goes-or-states-its-reason/frame/design.md:92`, `seal/threads/1793853197-a-bare-commit-goes-or-states-its-reason/frame/design.md:103`, `seal/threads/1793853197-a-bare-commit-goes-or-states-its-reason/frame/design.md:174`, `seal/threads/1793853197-a-bare-commit-goes-or-states-its-reason/frame/design.md:184`, `seal/threads/1793853197-a-bare-commit-goes-or-states-its-reason/frame/plan.md:5`, `seal/threads/1793853197-a-bare-commit-goes-or-states-its-reason/frame/plan.md:7`, `seal/threads/1793853197-a-bare-commit-goes-or-states-its-reason/frame/plan.md:24`
evidence: read `frame/design.md:29`, `:86-88`, `:92`, `:103`, `:115`, `:174`, `:184`, `frame/plan.md:5`, `:7`, `:24`, `:48`, `changelog.md:3`, `trail/phases/phase-1.md:162`; executed `git for-each-ref --contains 3538fd59`
regression: round-2
```

Why it matters: the unit is `frame/design.md` D1 and D2, with
`frame/plan.md` *Technical context* and A2. The plan's third judgment row
(`frame/plan.md:48`) says the counts at `31558c76` stay as read, with row 47
counted on top. 9591cb4e added row 47 to D1's table and counted it on top in
D1's total paragraph (`frame/design.md:88`, "so the work rewrites 86
lines"), but nowhere else. The defect came from that fold, which changed the
table without listing every sentence that states the table's totals. No
round finding named this fix pass: it answered the sealer's withholding after
round 2, hence `round-2` on the `regression:` line.

Each statement below speaks of D1 as it now stands, not of a measurement at
a named commit, and each now gives the wrong figure.

- `frame/design.md:29`: "Each of the 115 lines takes one of four
  dispositions". The table below it holds 116.
- `frame/design.md:92`: "34 of the 44 bare tokens D1 rewrites name a commit
  no remote ref reaches". D1 now rewrites 45 tokens. 35 of them are
  unreached, row 47's 3538fd59 among them, which `git for-each-ref
  --contains` finds only in `refs/heads/docs/1382-the-readme-names-two-of-four-network-places`
  (executed). `changelog.md:3` says "Thirty-five", so the frame and the
  changelog disagree on the figure the sealer compares.
- `frame/design.md:103`: *Scope* item 1, "The 85 comment and docstring
  lines. Each line of D1 rows 1 to 40". No in-scope item names row 47. The
  out-of-scope bullet at `:115` exempts it only by exclusion.
- `frame/design.md:174`: *Removes*, "72 lines". The phase addendum and the
  changelog give 73 P lines. The "21 test modules" still holds, since
  `tests/behaviour/test_chain_hooks_hardening.py` was already in D1 rows 6
  and 7.
- `frame/design.md:184`: "The catch record it stands on is the 34 unreached
  tokens D1 rewrites". The settle weighs D2 on this sentence, by its own
  words ("Whether it keeps catching is what the settle weighs"). Row 47 is a
  35th, and the only one the case itself refused (the sealer's run on HEAD
  merged with 703ab88c, and this round's run at a9d9f64a). The sentence
  leaves out the best evidence the mechanism has.
- `frame/plan.md:5`: "D1 lists the 115 lines ... at `31558c76`'s line
  numbers ... 85 are rewritten in 29 files". D1 lists 116, one at 703ab88c's
  line numbers, and 86 are rewritten.
- `frame/plan.md:7`: "The phase finds each line by D1's token, which no
  sibling adds or removes". The sentence before it now says #1382's squash
  added one.
- `frame/plan.md:24`, A2: "That is how the 34 unreached tokens in D1
  accumulated". Row 47 is the 35th, and it is A2's failure scenario
  happening after the frame was written.

The statements dated at a measurement stay as they are, by the judgment
row: the *Grounding* rows at `frame/design.md:12` and `:17-20`, executed at
2a11993e and `31558c76`. *Scope* item 3, S1 and S5 also stay, since each
speaks of phase 1's commit, and the phase record keeps its 115 rows with the
addendum's 116th.

```markdown
frame/design.md:29
**D1. Each of the 115 lines at `31558c76`, and the one line row 47 adds from `703ab88c`, takes one of four dispositions, read for what its reader acts on today.**

frame/design.md:92
- **What it would have caught.** 35 of the 45 bare tokens D1 rewrites name a commit no remote ref reaches, so a reader in a fresh clone finds nothing: 34 of 44 at `31558c76`, and row 47's, which only #1382's local feature branch holds. The `<commit>:<path>` form, which the case already refuses when unreached, had none of that kind among #1355's 25 lines (*Grounding*, the comparison row). #1355's D2 could rest on the existing case catching the misdirection, and for the bare form nothing did.

frame/design.md:103
1. **The 86 comment and docstring lines.** Each line of D1 rows 1 to 40 and row 47 is rewritten as its row says, and so is each sentence of the same paragraph that only makes sense with the clause that goes (D1, P).

frame/design.md:174 (the third cell's figure only)
the clauses and sentences naming the commit a case was seen red or green at, 73 lines with the paragraphs that only make sense with them

frame/design.md:184 (the third sentence)
The catch record it stands on is the 35 unreached tokens D1 rewrites (*Grounding*, the reachability row, and D1 row 47); row 47's is one the case itself refused, on HEAD merged with `703ab88c`.

frame/plan.md:5 (the second and third sentences)
`frame/design.md` D1 lists the 115 lines that hold a bare commit at `31558c76`'s line numbers, and in row 47 one line at `703ab88c`'s, with each line's disposition. 86 are rewritten in 29 files, and 30 stay as data.

frame/plan.md:7 (the last sentence)
The phase finds each line by D1's token, which no sibling removes, and records the line it built at.

frame/plan.md:24 (the failure scenario cell's second sentence)
That is how the 35 unreached tokens in D1 accumulated, row 47's among them after this frame was written, while the form the case reads had none among 25 (`frame/design.md` *Grounding*, the comparison row)
```

## Confirmations

What matched, the docstring reads whole after the drop: at HEAD,
`test_the_hooks_that_reach_the_network_are_named_without_a_count`'s
docstring (`tests/behaviour/test_chain_hooks_hardening.py:436-443`) ends
"also names every place in `NETWORK_PLACES`." Its sentences state the three
things the case asserts at `:468-473`: the pinned sentence `said` stands in
each file, the count phrases in `gone` do not, and each edition's passage
names every place in `NETWORK_PLACES` (read). The removed sentence's
"whose passages named none of them" described the old READMEs, which the
sentence before it already states as "named those two hooks and no other
place". So D1's P rule, which keeps a description of the earlier code only
where the docstring states it nowhere else, keeps nothing here (read). The
line coordinates hold: `:445` at 703ab88c and `:443` at a9d9f64a (`git
show`, executed).

What matched, the merged tree holds no other token the module refuses: at
HEAD, `bin/test -q tests/text/test_a_cited_commit_outlives_the_squash.py
tests/behaviour/test_chain_hooks_hardening.py` gave 45 passed at exit 0 in
the worktree (executed), whose refs include the local branch that contains
3538fd59. That matches the addendum's 17 and 28. In the scratch clone at
a9d9f64a, where `refs/remotes/origin/docs/1382-the-readme-names-two-of-four-network-places`
contains 3538fd59 and no `main` or release ref does, the same module gave
1 failed and 16 passed at exit 1. The one refusal line was
`tests/behaviour/test_chain_hooks_hardening.py:443 cites 3538fd59` (executed,
one `cites` line in the log). At 9591cb4e in the same clone it gave 17
passed at exit 0. So the case reads the merged tree, the merge brought
exactly one token it refuses, and the fix removed it.

What matched, M1 and M2 on HEAD's tree: `git grep -I -ohP
'\b[0-9a-f]{7,40}\b' -- . ':(exclude)seal/'` gave 6,454 distinct tokens.
Through one `git cat-file --batch-check`, 18 resolve as commits, the same 18
`trail/phases/phase-1.md` S1 lists. The 7-to-12-hex mixed tokens that
resolve to no commit are 33 (executed). That matches the addendum.

What matched, the merge's added lines: the `+` lines of `git diff -U0
a9d9f64a^1 a9d9f64a -- . ':(exclude)seal/'` hold two hex tokens, 3538fd59
and 1790644505, and the second resolves to no commit (executed). The `+`
lines of `git diff -U0 a9d9f64a 9591cb4e -- . ':(exclude)seal/'` hold none
(executed).

What matched, the merge brought no conflict and no stale sentence into this
item's files: `git merge-tree --write-tree 881fad6d 703ab88c` gives tree
29031fa5, which is a9d9f64a's own tree, so nothing was resolved by hand
(executed). The merge changes no file under this work item's directory
(`git diff --stat a9d9f64a^1 a9d9f64a -- <item dir>`, empty, executed), and
`git grep` for conflict markers in that directory and in `tests/` finds none
(exit 1, executed). The merge changed three files this work rewrote,
`tests/hooks/test_routing.py`, `tests/github/test_roll_flow_measurement_issue.py`
and `tests/text/test_a_moved_rule_leaves_its_definition.py`. The diff of each
was read, and none touches a line D1 names (read). `git grep -nw` over the 45
tokens of D1 rows 1 to 40 and 47 at HEAD finds one line,
`evals/behaviour/proofer/seeded-7a8899d5/prompt.md:5`, which holds
`15a5ce66` as D1 row 41's data (executed). The moved-rule docstring at
`tests/text/test_a_moved_rule_leaves_its_definition.py:8-19` is still the
text round 2 confirmed (read).

What matched, the records agree on row 47 and on the counts they state:
D1 row 47 (`frame/design.md:86`) and the addendum's row 116
(`trail/phases/phase-1.md:166`) name the same token, the same line at
703ab88c, disposition P and the same removed sentence (read). The changelog
gives 86 lines in 29 files, 35 unreached, 73 P, 4 G and 9 N, and 73, 4 and
9 sum to 86 (read). The addendum gives 86 lines, 73 P and the same 29 files,
`gaps.md:9` names rows 1 to 85 and row 116, and D1's total paragraph gives
86 (read). The 35 is 34 plus 3538fd59, which only the local feature branch
contains (executed). The frame's other statements of D1's totals are
finding 1.

The fix range adds no test, so no new case is read against its group.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at 9591cb4e. The last broad run, at 9de1ab25, predates the merge of 703ab88c and caab8bc0's change to a test module | `trail/gate.md` | the orchestrator, at the broad run at HEAD |
| The sealer's re-run of its withheld claim at the new HEAD | `guarantee.md` | the sealer |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/text/test_a_cited_commit_outlives_the_squash.py tests/behaviour/test_chain_hooks_hardening.py`, in the worktree at 9591cb4e | 45 passed, exit 0 |
| `bin/test -q tests/text/test_a_cited_commit_outlives_the_squash.py`, scratch clone at a9d9f64a | 1 failed, 16 passed, exit 1; one refusal, `tests/behaviour/test_chain_hooks_hardening.py:443 cites 3538fd59` |
| the same, scratch clone at 9591cb4e | 17 passed, exit 0 |
| `git for-each-ref --contains 3538fd59`, worktree and scratch clone | `refs/heads/docs/1382-the-readme-names-two-of-four-network-places` in the worktree; its `refs/remotes/origin/` copy in the clone; no `main` or release ref |
| M1 at HEAD: `git grep -I -ohP '\b[0-9a-f]{7,40}\b' -- . ':(exclude)seal/'`, then one `git cat-file --batch-check` | 6,454 tokens, 18 commits, the S1 list |
| M2 at HEAD: 7-to-12-hex tokens holding a digit and a letter, less those that resolve | 33 |
| `git diff -U0 a9d9f64a^1 a9d9f64a -- . ':(exclude)seal/'`, `+` lines grepped for 7-to-40-hex tokens | 3538fd59 and 1790644505 |
| `git diff -U0 a9d9f64a 9591cb4e -- . ':(exclude)seal/'`, the same grep | none |
| `git merge-tree --write-tree 881fad6d 703ab88c` against `git rev-parse a9d9f64a^{tree}` | both 29031fa5 |
| `git grep -nwE` over the 45 tokens of D1 rows 1 to 40 and 47 at HEAD, outside `seal/` | one line, row 41's data |
