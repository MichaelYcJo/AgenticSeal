# 1792252400-the-sealer-reads-the-gate-the-orchestrator-ran — review round 4

target: 2ed98c29, fixes 3957339e..2ed98c29

## Findings

### 1. The sealer can now withhold because its base resolves to nothing, and the orchestration gives that verdict no repair

severity: should
location: `skills/code-review/orchestration.md:209-221`, `agents/sealer.md:48-49`
verdict: fixed e7e5574a

The unit is the orchestration's paragraph on what to do with a verdict
other than `sealed`, which phase 3 wrote (`plan.md` row 3 names
`skills/code-review/orchestration.md:178-249`); it is new work, so this
finding carries no `regression:` line. 3e6d3896 gave the sealer a second
`withheld` reason, at round 3's request: "Where none answers, write
`guarantee.md` with `Verdict: withheld — the base <name> resolves to no
commit here` and return" (`agents/sealer.md:48-49`). Round 3's grounds for
`withheld` over `undecided` were that the orchestrator's repair, naming the
worktree or fetching, is mechanical. No document tells the orchestrator
that repair.

Read. The paragraph at `skills/code-review/orchestration.md:209-221` has
two branches for `withheld`: a repair touching only the work item's records
or the pull request body (make it, commit, spawn again), and a repair
touching any other file (a verifying round, then the broad gate). This
verdict's repair touches no file and needs no commit, so neither branch
fits. The spawn at lines 187-188 names the base and the work item's
directory and no root, so nothing steers the orchestrator away from a clone
where the base does not resolve in the first place. `withheld — no broad
run at HEAD` is the one reason the paragraph's lead-in names (lines
190-192); the new one is named nowhere outside `agents/sealer.md` and its
pin (`git grep -F 'resolves to no commit'`).

Executed. In this round's clone, a `git clone --no-local` of the branch
worktree, `rev-parse --verify --quiet` exits 1 for each of
`release/v0.22.1@{upstream}`, `origin/release/v0.22.1` and
`release/v0.22.1`. A sealer spawned in such a clone reaches this verdict on
every spawn, and the orchestrator respawning it there by the first branch
gets it again.

Why it matters. This project's first goal is a run that verifies
unattended. A verdict whose repair the orchestrator has to invent is a stop
in an `automation` run, which is the cost round 3 moved the verdict away
from `undecided` to avoid.

The fix appends one sentence to the paragraph, after line 221. Executed in
the clone with it applied: the seven modules that name
`skills/code-review/orchestration.md`, with `test_one_word_one_meaning` and
`test_no_real_identifiers`, 208 passed and 6 skipped, exit 0; the file was
restored and the clone's status is clean. Rung 1 of the filing ladder: the
branch owns the paragraph.

```markdown
as `Answered <date> by <who>: <answer>`, commit, and spawn the sealer again.
`withheld — the base <name> resolves to no commit here` needs no commit: the
clone you named carries none of the base's refs, so spawn the sealer again in
the branch worktree, where `origin/<base>` resolves, or fetch the base there.
```

answer: Rung 1, the branch owns the paragraph. The orchestrator appended the sentence as written after the `undecided` line of `skills/code-review/orchestration.md` §*Commit `guarantee.md`*, in e7e5574a; the modules naming the file with `test_one_word_one_meaning`, `test_no_real_identifiers`, `test_docs_line_wrap` and `test_unverified_rows_close`: 430 passed, 6 skipped, exit 0; `rules --check` exit 0.

### 2. The overview credits e15490c5 with the base read as a commit and withheld, which 3e6d3896 wrote

severity: should
location: `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/overview.md:26`
verdict: fixed e7e5574a
regression: round-3#2

The unit is the departure cell of the row *The base the sealer's steps read
(round 2)*, which 3e6d3896 rewrote to close round 3's finding 2. The frame
gives step 1 no base (`spec.md` §*The act, as this item leaves it*, lines
181-188) and has `plan.md` row 3 build the definition, not this row; the fix
took round 3's paste-ready row as written, and the defect came from how that
text was written, a review record's paste-ready fix ending the departure
with "(e15490c5, round 3)".

Read. The cell now says "every `<base>` after it is that ref's commit; none
resolving is `withheld` (e15490c5, round 3)". At e15490c5 the definition
said the opposite on both points: `<base>` was the ref, and none resolving
was `undecided` (round 3, finding 1's quoted sentence and finding 2's
unit). The commit that wrote both is 3e6d3896, which the row does not name.
The row two above it shows the convention the row breaks: "(8313e330,
worded as a condition in e15490c5)" names the commit that changed the
wording beside the one that departed.

Why it matters. The sealer's step 4 reads the records against each other
and the tree. A sealer that opens e15490c5 from this row finds the word the
row says it does not hold, and has to decide whether the record or the
definition is wrong. The information is recoverable from `rounds/round-3.md`
(`verdict: fixed 3e6d3896`), so the cost is a reader's detour or a
misplaced `withheld`, not a lost fact. Rung 1 of the filing ladder: the
branch owns the record.

```markdown
none resolving is `withheld` (e15490c5; the commit and `withheld` in 3e6d3896, round 3)
```

The line replaces the text from "none resolving is `withheld`" to the
closing parenthesis of the departure cell; the rest of the row stands.

answer: Rung 1, the branch owns the record. The orchestrator replaced the cell's tail with the line as written, in e7e5574a.

## Confirmations

confirms: round-3#1
Every `<base>` in the definition is now the resolved commit, and the commit
is readable where the at-base restore reads it (`agents/sealer.md:42-47`).
Executed in the branch worktree: `rev-parse --verify --quiet` exits 1, 0, 1
for `release/v0.22.1@{upstream}`, `origin/release/v0.22.1` and
`release/v0.22.1`, so the sentence's order picks the second, which prints
2fc33333bcfef5f0fa9e7d6d7bc6469366c6f2ff; `merge-base --is-ancestor` of it
and HEAD exits 0; step 1's
`git log --no-merges --name-only 3957339e..HEAD ^2fc33333bcfef5f0fa9e7d6d7bc6469366c6f2ff`
exits 0. Executed in this round's clone, a `git clone --no-local -q` of the
worktree at 2ed98c29: `git show 2fc33333bcfef5f0fa9e7d6d7bc6469366c6f2ff:agents/sealer.md`
exits 0 and `git show origin/release/v0.22.1:agents/sealer.md` exits 128.
The rule *A `seen red` is re-run against the code before the change*
(`agents/sealer.md:115-119`) keeps `<base>` and inherits the commit.
`test_step_1_reads_the_record_and_runs_nothing` passes, and
`mutation-check` of "is the commit it prints" to "is the ref it prints"
fails it. Read: `chain_check.py#target_of` takes the first SHA-shaped
word of the `Target SHA` row (`chain_check.py:1356-1360`), so a base
written as a commit in `<sha> against <base>` does not displace the audited
commit.

confirms: round-3#2
A base resolving to nothing is `withheld`, written to `guarantee.md` before
the sealer returns, like step 1's unresolved commit
(`agents/sealer.md:48-49`). Executed: `mutation-check` of
"`Verdict: withheld — the base" to "`Verdict: undecided — the base" fails
`test_step_1_reads_the_record_and_runs_nothing`; the unmutated module
passes. `git grep -F 'resolves to no commit'` outside the round records
finds only `agents/sealer.md:49` and its pin at
`tests/test_the_sealer_guarantees.py:366`, so no document still sends it to
the owner. The overview row's citation is finding 2.

confirms: none
The reference re-run at 1483d8ba reproduces from its raw side, measures the
definition that ships, and every figure quoted from it holds. Executed:
`noninferiority.py run --from-raw` of `SpecSeal-worktrees/969-phase-6d-raw`
into scratch, then `cmp` against the clone's and the worktree's
`evals/reference-sealer.json`: 0, 0, 0. `side_numbers` on it: 10 runs (2 for
each of the five cases), not cut short, 34 graders passing 68 of 68, spend
3.3898, 2,855,195 tokens over 77 calls (37,080.5 per call), 191.7 seconds,
preload 24,702 bytes. Its preload hash for `agents/sealer.md`,
071c14d8e9eefdeb833f7655a29ed9fb04998b0c452cb57a1a42c410131320c0, is the
sha256 of the file at both 1483d8ba and HEAD (2ed98c29 touches only the
item's records), and 8,099 plus the contract's 16,603 bytes is 24,702. Its
`suite_tree` 5c3e8119 is `evals/behaviour/sealer` at 1483d8ba and at HEAD.
The seven sides sum to 20.2197 and the three of phases 2 and 4 to 7.4013.
Those are the figures of `phases/phase-6.md:55-80`, `changelog.md:21`,
`overview.md:22` and `overview.md:33`, and `questions.md:44` (Q5); none of
them still quotes 6f76b0b0 as the reference.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The paid run's own exit codes in phase 6's round-3 row (`run`, `cp -R`, `diff -r`): this round re-ran only `run --from-raw` and `cmp` | `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/phases/phase-6.md:97` | the orchestrator |
| `rule-sealer-stale-gate` has not been seen failing on a sealer that skips step 1's range (contract §15); carried from round 3 | `evals/behaviour/sealer/rule-sealer-stale-gate/` | the orchestrator |
| The full suite, the repository-wide lint and the typecheck at 2ed98c29: `unverified` here | the branch | the orchestrator, by `broad-gate --record` once the rounds settle |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local -q` of the branch worktree into `<scratch>/round-4/clone`, checkout 2ed98c29 | 0, 0 |
| `noninferiority.py run --from-raw SpecSeal-worktrees/969-phase-6d-raw --out <scratch>/round-4/re/reference-sealer.json`; `cmp` against the clone's and the worktree's copy | 0; 0, 0 |
| `side_numbers` on the re-derived side; sha256 and bytes of `agents/sealer.md` at 2ed98c29, 1483d8ba and 3957339e and of the contract at 2ed98c29; `rev-parse <rev>:evals/behaviour/sealer` at 1483d8ba and 2ed98c29 | the figures of the third confirmation; 071c14d8 at 1483d8ba and 2ed98c29, 1ee24557 at 3957339e; 5c3e8119 twice |
| `rev-parse --verify --quiet` of the three spellings in the worktree and in the clone | worktree 1, 0, 1; clone 1, 1, 1 |
| `git show <rev>:agents/sealer.md` in the clone, for 2fc33333bcfef5f0fa9e7d6d7bc6469366c6f2ff and `origin/release/v0.22.1` | 0, 128 |
| step 1's `git log --no-merges --name-only 3957339e..HEAD ^2fc33333…` and `merge-base --is-ancestor 2fc33333… HEAD` in the worktree | 0, 0 |
| `bin/test` over `test_the_sealer_guarantees`, `test_docs_line_wrap`, `test_one_word_one_meaning`, `test_broad_gate_rule`, `test_the_seal_is_taken_once_by_the_sealer`, `test_evals_layout` `-q -n auto` in the clone | 0, 484 passed |
| `bin/mutation-check agents/sealer.md` twice: "is the commit it prints" to "is the ref it prints", and the base verdict's `withheld` to `undecided`, each against `test_the_sealer_guarantees.py` | 1 failed each, `test_step_1_reads_the_record_and_runs_nothing`; file restored by the tool |
| finding 1's sentence applied to the clone's `skills/code-review/orchestration.md`, then `bin/test` over the seven modules naming it with `test_one_word_one_meaning` and `test_no_real_identifiers`; `git checkout --` of the file | 0, 208 passed, 6 skipped; status clean |
| `git grep -n -F` of the fix's fragments (`resolves to no commit`, `is the commit it prints`, `remote-tracking ref`) over the tree, and of the reference's old and new figures over the work item | only the definition, its pin and the item's records, as the confirmations say |
