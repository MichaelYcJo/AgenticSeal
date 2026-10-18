# 1792252400-the-sealer-reads-the-gate-the-orchestrator-ran — review round 5

target: 166ff329, fixes 5386f4e3..166ff329

## Findings

### 1. The repair's second branch, fetching the base, fails as git spells it in the clone the sentence describes

severity: should
location: `skills/code-review/orchestration.md:222-224`
verdict: fixed a5d4d32c
regression: round-4#1

The unit is the sentence e7e5574a appended to the paragraph on a verdict
other than `sealed`, in `skills/code-review/orchestration.md`
§*Commit `guarantee.md`*. The frame names that paragraph's file (`plan.md`
row 3) and says nothing about a base that resolves to no commit, which
round 4 found to be new work; the fix appended round 4's paste-ready
sentence as written; the defect came from how that sentence was written, a
review record's paste-ready fix offering "or fetch the base there" with no
command behind it.

Read. The sentence offers two repairs: "spawn the sealer again in the branch
worktree, where `origin/<base>` resolves, or fetch the base there". Round 4's
grounds name the second as "fetching" in the clone, and that is the reading
"or" invites, since a fetch in the branch worktree spawns nothing. In that
clone a plain `git fetch origin <base>` asks the branch worktree for a branch
named `<base>`, and the worktree has none: `for-each-ref` there lists
`refs/heads/release/v0.21.0` and `refs/remotes/origin/release/v0.22.1`, and
no `refs/heads/release/v0.22.1`. A `git clone` copies the source's branches
and not its remote-tracking refs, which is why round 4's probe found all
three spellings unresolved in its clone. The fetch that would work names a
refspec the sentence does not give
(`refs/remotes/origin/<base>:refs/remotes/origin/<base>`). An unattended
orchestrator that takes the second branch meets exit 128 and has to invent
the repair, the cost round 4's finding 1 was raised to remove.

Read, a smaller slip in the same sentence. "where `origin/<base>` resolves"
is true of this worktree and of any repository with a fetched remote. In a
repository with no remote, which `agents/sealer.md:36-39` allows for, the
worktree resolves the base as the plain `<base>`, the third spelling of
`broad_gate.py#resolve_base`, and the sentence names only the second.

Why it matters. The first branch alone is a repair the orchestrator can
carry out without a person, so the verdict is no longer a stop. The second
is an instruction that fails on its obvious spelling, kept beside one that
works, and nothing tells the reader which to take.

The fix replaces lines 222-224 and keeps the one repair that needs nothing
fetched. Not applied or run here: this round wrote no file but this record.

```markdown
`withheld — the base <name> resolves to no commit here` needs no commit: a
`git clone` of the branch worktree copies its branches and none of its
`origin/` refs, so spawn the sealer again with the branch worktree itself as
its clone, where `origin/<base>` or, with no remote, `<base>` resolves.
```

answer: The orchestrator replaced the sentence with the text above as written, in a5d4d32c. Probed first: in a `git clone --no-local` of the worktree, `rev-parse --verify --quiet` exits 1 for all three spellings of `release/v0.22.1`; in the worktree it exits 0 for `origin/release/v0.22.1`. The modules naming the file with `test_one_word_one_meaning`, `test_docs_line_wrap` and `test_no_real_identifiers`: 208 passed, 6 skipped, exit 0; `rules --check` exit 0.

## Confirmations

confirms: round-4#1
The verdict `withheld — the base <name> resolves to no commit here` now has a
repair in the orchestration, and its first branch holds. Read: the sentence
at `skills/code-review/orchestration.md:222-224` quotes the verdict as
`agents/sealer.md:48-49` writes it, says it needs no commit, and sends the
sealer back to the branch worktree. The sealer resolves its base by the
first of `<name>@{upstream}`, `origin/<name>` and `<name>` that
`rev-parse --verify --quiet` answers (`agents/sealer.md:42-47`), and in this
worktree `refs/remotes/origin/release/v0.22.1` exists, so the second
spelling answers there, as round 4's probe also found (worktree 1, 0, 1).
"carries none of the base's refs" is the verdict's own condition, all three
spellings unanswered. `git grep -F 'resolves to no commit'` outside the
round records finds the definition at `agents/sealer.md:49`, its pin at
`tests/test_the_sealer_guarantees.py:366` and this sentence, so the verdict
is named where the orchestrator reads its repairs. Executed: the eight
modules below pass at 166ff329. The second branch of the sentence is
finding 1.

confirms: round-4#2
The departure cell of the row *The base the sealer's steps read (round 2)*
now credits each commit with what it wrote. Read against the two commits'
diffs of `agents/sealer.md`: e15490c5 added the single resolution over the
three spellings, with every `<base>` the ref and none resolving `undecided`;
3e6d3896 made every `<base>` "the commit it prints, never the ref" and none
resolving `withheld`. The cell at
`seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/overview.md:26`
reads "(e15490c5; the commit and `withheld` in 3e6d3896, round 3)", which is
that split, in the shape of the row two above it ("8313e330, worded as a
condition in e15490c5"). The class, every other place the item's records
credit either commit, is `git grep -e e15490c5 -e 3e6d3896` over the work
item outside `rounds/`: `overview.md:24`, which credits e15490c5 with the
condition wording it did write, and `phases/phase-6.md:55-58`, which credits
e15490c5 with round 2's change to `agents/sealer.md` and 3e6d3896 with the
base paragraph, both true of the diffs. No record still calls the base's
verdict `undecided` (`git grep 'undecided — the base'` finds none).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Round 4's answer to finding 1 reports 430 passed and 6 skipped over a module set that includes `test_no_real_identifiers` and `test_unverified_rows_close`, and `rules --check` exit 0; this round ran a different set of eight modules and not `rules --check` | `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/rounds/round-4.md:62` | the orchestrator |
| No clone was made: the prompt scoped this round to reading in the branch worktree and narrow tests, so the failing fetch in finding 1 is read from the refs and git's clone behaviour, not executed | `skills/code-review/orchestration.md:222-224` | the orchestrator, at the fix pass |
| The full suite, the repository-wide lint and the typecheck at 166ff329: `unverified` here | the branch | the orchestrator, by `broad-gate --record` once the rounds settle |

## Probes

| Command | Result |
|---|---|
| `git log --oneline` and `git diff` of 5386f4e3..166ff329 in the worktree | two commits, e7e5574a and 166ff329; three files |
| `git show e15490c5 -- agents/sealer.md` and `git show 3e6d3896 -- agents/sealer.md seal/` | 0, 0 |
| `git for-each-ref` of `refs/heads/release/*` and `refs/remotes/origin/release/v0.22.1` in the worktree | 0; `refs/heads/release/v0.21.0`, `refs/remotes/origin/release/v0.22.1` |
| `git grep` of e15490c5 and 3e6d3896 over the work item, and of `resolves to no commit`, `at-base clone`, `clone you named` and `undecided — the base` over the tree, round records excluded | the places the confirmations name |
| `bin/test` over the seven modules `git grep -l "code-review/orchestration.md" -- tests` names with `test_one_word_one_meaning` `-q -n auto` | 0, 202 passed, 6 skipped |
