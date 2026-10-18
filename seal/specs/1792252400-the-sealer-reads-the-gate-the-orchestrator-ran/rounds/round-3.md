# 1792252400-the-sealer-reads-the-gate-the-orchestrator-ran — review round 3

target: e4a55b7d, fixes 83baeb91..e4a55b7d

## Findings

### 1. The at-base restore still cannot find the base, because `<base>` is now a remote-tracking ref the at-base clone does not carry

severity: must
location: `agents/sealer.md:42-47`, `agents/sealer.md:113-116`, `tests/test_the_sealer_guarantees.py:348-362`
verdict: fixed 3e6d3896
reopens: round-2#1
answer: 3e6d3896 takes the paste-ready block: the resolution sentence now says every `<base>` below is the commit `git -C <root> rev-parse --verify --quiet` prints, never the ref, so step 1's range, step 2's diff and the at-base restore all read a commit; `agents/sealer.md:113-116` keeps `<base>` and inherits the definition. `test_step_1_reads_the_record_and_runs_nothing` takes the record's replacement assertions; `mutation-check` of "is the commit it prints" to "is the ref it prints" gave red. Probed read-only: in a `git clone --no-local -q` of the worktree at 3e6d3896, `git show 2fc33333bcfef5f0fa9e7d6d7bc6469366c6f2ff:agents/sealer.md` exits 0 and `git show origin/release/v0.22.1:agents/sealer.md` exits 128. The reference still measures the text at 6f76b0b0; whether it is re-run is the orchestrator's call, as the round's Not judged says.

Why round 2's close does not hold. Finding 1 named three places the plain
branch name fails: step 1's range, step 2's diff and the at-base restore
(`agents/sealer.md:111` then, 113-116 now). e15490c5's answer says the
resolved base is "every `<base>` below (step 1's range, step 2's diff, the
at-base restore)". The sentence it wrote makes `<base>` the ref that
answers, "the first of `<name>@{upstream}`, `origin/<name>` and `<name>`
that `git -C <root> rev-parse --verify --quiet` answers is every `<base>`
below". In this repository's flow that ref is `origin/release/v0.22.1`, a
remote-tracking ref of the root. The rule *A `seen red` is re-run against
the code before the change* clones the repository into `at-base/` and
restores the changed code there "from `<base>`". A clone of the root
carries the root's local branches as `origin/*` and none of its
remote-tracking refs, so the ref names nothing there. The first two places
are fixed; the third is not.

Executed, read-only. In the branch worktree,
`rev-parse --verify --quiet 'origin/release/v0.22.1^{commit}'` prints
2fc33333bcfef5f0fa9e7d6d7bc6469366c6f2ff. In this round's clone, a
`git clone --no-local` of that worktree (the shape the reference's sealers
use for `at-base/`: `git clone -q $R $S` in traces 004, 005, 008 and 009 of
`969-phase-6c-raw`), `git show origin/release/v0.22.1:agents/sealer.md`
exits 128, `git show release/v0.22.1:agents/sealer.md` exits 128, and
`git show 2fc33333bcfef5f0fa9e7d6d7bc6469366c6f2ff:agents/sealer.md` exits
0. The commit is in every clone of the branch, because the branch descends
from it; the ref is in none.

Read. `broad_gate.py#resolve_base`, which the sentence says it follows,
does not hand its consumers the ref: its docstring says "The resolution
turns the ref into its commit for them too", and it returns `Base.commit`.
Round 2's paste-ready text said the same ("Every `<base>` below is that
commit"); the committed sentence dropped the word.

Why it matters. Every `seen red` the sealer samples in this repository
meets an unknown revision at the restore. The sealer then writes the claim
`unverified` or guesses at another ref, and the claim it was spawned to
re-run is not re-run. The eval cases cannot see it: their base `main` is a
local branch, so a clone of the scaffold carries it as `origin/main` and the
sealers there restored from `main` or a hash.

```markdown
the contract. The base arrives as a plain branch name, which may be missing
here or behind its remote, so resolve it once as `broad-gate` does
(`broad_gate.py#resolve_base`): take the first of `<name>@{upstream}`,
`origin/<name>` and `<name>` that `git -C <root> rev-parse --verify --quiet`
answers, and every `<base>` below is the commit it prints, never the ref,
since the at-base clone holds the commit and not the remote-tracking ref.
Where none answers, write `guarantee.md` with
`Verdict: withheld — the base <name> resolves to no commit here` and return.
```

```python
        assert "`broad_gate.py#resolve_base`" in intro, intro
        assert (
            "take the first of `<name>@{upstream}`, `origin/<name>` and "
            "`<name>` that `git -C <root> rev-parse --verify --quiet` answers, "
            "and every `<base>` below is the commit it prints"
        ) in intro, intro
        assert (
            "`Verdict: withheld — the base <name> resolves to no commit here`"
        ) in intro, intro
```

The three assertions replace `tests/test_the_sealer_guarantees.py:356-362`.
The markdown block replaces `agents/sealer.md:42-47` and also carries
finding 2's verdict word; `overview.md`'s row *The base the sealer's steps
read (round 2)* then reads "every `<base>` after it is that ref's commit;
none resolving is `withheld`". Cost: `agents/sealer.md` changes again, so
`evals/reference-sealer.json` (preload hash `1ee24557…` of the text at
6f76b0b0) no longer measures the definition that ships; whether it is
re-run or its record says which text it measured is the orchestrator's
call, as round 2 said.

### 2. A base that resolves to nothing is sent to the owner as a question, while the same step's missing commit is withheld for the orchestrator

severity: should
location: `agents/sealer.md:46-47`, `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/overview.md:26`, `tests/test_the_sealer_guarantees.py:362`
verdict: fixed 3e6d3896
regression: round-2#1
answer: 3e6d3896 makes a base that resolves to no commit `Verdict: withheld — the base <name> resolves to no commit here`, written to `guarantee.md` before the sealer returns, in the same sentence as finding 1; the test line is the record's, and `overview.md`'s row *The base the sealer's steps read (round 2)* reads "that ref's commit; none resolving is `withheld`" with round 3's grounds. `mutation-check` of `withheld` back to `undecided` in that line gave red. `git grep -F` of `undecided` over `tests`, `evals` and `agents/sealer.md` finds only the verdict word's general uses; the old sentence survives only in `rounds/round-2.md`, a record of its state.

The unit is the clause e15490c5 added to the paragraph before
`## Order of work`: "where none answers the verdict is `undecided — the base
<name> resolves to no commit here`". The frame (`spec.md` §*The act, as this
item leaves it*, lines 181-188, and `plan.md` row 3) names no base for step 1
and sends every missing input of step 1 to `withheld — no broad run at
HEAD`; the fix added a base and gave its failure the third word, and the
word came from round 2's own paste-ready text, which the fix took as
written.

Read. `templates/sdd-guarantee.md:29-30` defines the words: `withheld — <the
claim, its party, its coordinate>` and `undecided — <the question, for the
owner>`. `docs/the-review-record.md:244-247` says "An undecided question is
the owner's", and `skills/code-review/orchestration.md:220-221` has the
orchestrator put it to the owner after the run and wait for an
`Answered <date> by <who>:` line. A base that resolves to no commit is not
a question the issue body and the tree cannot decide (step 4's test for
`undecided`). It is a defect in the sealer's input: the orchestrator named a
clone, or a base, in which the ref is missing, and only the orchestrator can
repair it. Step 1 already treats the same kind of failure, "a commit that
does not resolve", as `withheld`.

Executed. In this round's clone (a `git clone --no-local` of the branch
worktree), `rev-parse --verify --quiet` answers 1 for each of
`release/v0.22.1@{upstream}`, `origin/release/v0.22.1` and
`release/v0.22.1`, and `broad_gate.py#resolve_base` returns commit `None`.
So a prompt that names such a clone reaches this clause on every spawn.

Why it matters. This project's first goal is verification that runs
unattended (`CLAUDE.md`, *The goal a design is chosen against*). An
`undecided` here stops the run for a person whose answer cannot fix a
missing ref, and the sealer spawned again after that answer meets the same
clone. `withheld` sends it to the orchestrator, whose repair (name the
worktree, or fetch) is mechanical.

The fix is the markdown block of finding 1, whose last two lines carry the
verdict, with this test line in place of `tests/test_the_sealer_guarantees.py:362`:

```python
        assert (
            "`Verdict: withheld — the base <name> resolves to no commit here`"
        ) in intro, intro
```

```markdown
| The base the sealer's steps read (round 2) | `spec.md` §*The act* gives step 1 no base and leaves steps 2 to 5 as 0.22.0 left them, where `<base>` was the name the prompt gave | the definition resolves the base once, as `broad_gate.py#resolve_base` does, to the first of `<name>@{upstream}`, `origin/<name>` and `<name>` that resolves, and every `<base>` after it is that ref's commit; none resolving is `withheld` (e15490c5, round 3) | round 2's finding 1: a work item's worktree has only `origin/<base>`, so `^<base>` as given exited 128, and a local branch behind its remote would not exclude the base's newer commits; round 3: the at-base clone holds the commit and not the ref, and a missing ref is the orchestrator's to repair (`rounds/round-2.md`, `rounds/round-3.md`) |
```

## Confirmations

confirms: round-2#2
`RETIRED_SAYS` (`skills/code-review/scripts/chain_check.py:91-98`) now
states the remedy as a condition and asserts nothing about the record:
"Where `broad-gate.md` names a run at HEAD, or one followed only by the work
item's records, spawn the sealer again at HEAD, which writes the new word;
otherwise run `broad-gate --base <base> --record <item>` and commit
`broad-gate.md` first". The condition is the one `chain_check.py#broad_gate`
applies: it calls `follows` with no `only`, so any path under the item
passes (read, `chain_check.py:1383-1414`, 1591). `changelog.md:37-42` says
the same to a plugin user. Executed: `test_the_old_words_are_refused_by_line`
passes in the clone, and with the message put back to "The committed
`broad-gate.md` still stands" it fails.

confirms: round-2#3
2076c4d6 renames the case to
`test_the_section_says_the_full_run_is_the_orchestrators`, which asserts
"The full suite is the orchestrator's" over `CONTRIBUTING.md:107`, and
rewrites the four sentences that gave the sealer the gate's arms or lines.
Executed: the case passes in the clone and fails with `CONTRIBUTING.md:107`
changed to "The full suite is the sealer's". The old name stands as one key
of `.test_durations:6803`, which prices nothing now; the durations case
tolerates a share of unpriced ids, so it is not a failure. The orchestrator's
class judgement holds: `git grep -n -i -E "sealer('s|s)? .{0,40}(broad|gate|stamp|capture|arms|suite|lint|typecheck|relay)"`
outside `seal/specs/`, `changelog/`, `.test_durations` and the three files
#967 and #968 own gives 34 lines, every one the sealer reading a record, a
grader or test saying the sealer runs no gate, past-tense history
(`docs/the-agent-set.md:111`, `docs/the-broad-gate.md:122`,
`tests/test_evals_layout.py:123, 341`, the fixture text of
`tests/test_a_process_record_drop_passes_the_readers.py:58, 62`), a
comment naming #957's and #969's moves, or #967's pin at
`tests/test_the_seal_is_taken_once_by_the_sealer.py:8323`.

confirms: round-2#4
`overview.md:23-26` carries the three departures round 2 named and a fourth
for the base. Read against the frame: `spec.md:181-188` gives step 1 as
`git log --name-only <sha>..HEAD` and says steps 2 to 5 stay as 0.22.0 left
them; `plan.md:120-127` orders `broad-gate --record` before the sealer; S3
(`spec.md:202`) names `rule-sealer-no-gate` as the fourth case. Each row
cites the commit that departed and the round that asked for it. The fourth
row's "none resolving is `undecided`" moves with finding 2.

confirms: none
The reference re-run after round 2 reproduces, and every figure quoted from
it holds. Executed: `noninferiority.py run --agent sealer --from-raw` of
`969-phase-6c-raw` into scratch, `cmp` against the committed
`evals/reference-sealer.json`: 0, identical, and the worktree's copy is
identical too. `side_numbers` on it: 10 runs, none cut short, spend
3.3431105, 2,747,167 tokens over 77 calls (35,677.5 per call), 295.402
seconds, preload 24,555 bytes, every grader 2 of 2 over 34 graders (68 of
68), suite rev 6f76b0b0 and tree 5c3e8119. The preload's `agents/sealer.md`
hash `1ee24557…` is the sha256 of the file at e4a55b7d, and 7,952 plus
16,603 bytes is 24,555; `git diff --stat 6f76b0b0 e4a55b7d` touches only the
item's records. The six sides sum to 16.8299 (3.1901, 2.8036, 1.4076,
2.9882, 3.0973, 3.3431), phases 2 and 4 to 7.4013. Those are the figures of
`phases/phase-6.md:55-79`, the changelog's reference row, `overview.md:33`
and `questions.md` Q5.

confirms: none
The order the new sentence states matches `resolve_base`. Executed
read-only in the branch worktree: `release/v0.22.1@{upstream}` 1,
`origin/release/v0.22.1` 0, `release/v0.22.1` 1, and
`resolve_base(<worktree>, "release/v0.22.1")` returns ref
`origin/release/v0.22.1`, commit 2fc33333, the same the sentence's order
picks; `git log --no-merges --name-only 83baeb91..HEAD ^origin/release/v0.22.1`
exits 0. Read: `resolve_base` asks `<given>@{upstream}`, then
`refs/remotes/origin/<given>`, then the ref as given
(`skills/verify/scripts/broad_gate.py:647-700`). Executed:
`test_step_1_reads_the_record_and_runs_nothing` passes and fails with the
sentence's list changed. Finding 1 is about what `<base>` names after the
order picks, not the order.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The `root` and `path` lines under the platform's per-user temporary directory in the item's eval records, carried from round 2 | `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/evals/*.json` | the owner |
| `rule-sealer-stale-gate` has not been seen failing on a sealer that skips step 1's range (contract §15); a side on such a definition is a paid run, carried from round 2 | `evals/behaviour/sealer/rule-sealer-stale-gate/` | the orchestrator |
| Whether the reference is re-run after findings 1 and 2 change `agents/sealer.md`, or its record says it measured the text at 6f76b0b0 | `seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/evals/reference-sealer.json` | the orchestrator |
| `tests/test_the_seal_is_taken_once_by_the_sealer.py:8323` asserts "Then the sealer takes the broad gate once" in `agents/smith.md` | `tests/test_the_seal_is_taken_once_by_the_sealer.py:8323` | #967 |
| The warden's read set, not re-measured, by design | `agents/warden.md` | the milestone close |
| The full suite, the repository-wide lint and the typecheck at e4a55b7d: `unverified` here | the branch | the orchestrator, by `broad-gate --record` once the rounds settle |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the branch worktree into `<scratch>/round-3/clone`, checkout e4a55b7d | 0, 0 |
| `bin/test` over `test_the_sealer_guarantees`, `test_the_suite_has_a_command_that_is_cheap_twice`, `test_broad_gate_rule`, `test_the_gate_names_every_step_ci_runs`, `test_the_seal_is_taken_once_by_the_sealer`, `test_chain_check`, `test_docs_line_wrap`, `test_no_real_identifiers`, `test_one_word_one_meaning`, `test_evals_layout`, `test_a_rewritten_definition_proved_non_inferior`, `test_the_record_is_written_in_words` `-q -n auto` in the clone | 0, 767 passed |
| `bin/rules --check --root <clone>` | 0, 467 targets in 60 rule files |
| three mutations in the clone (`CONTRIBUTING.md:107` to "the sealer's", `RETIRED_SAYS` back to "still stands", the sealer's list without `@{upstream}`), the three cases that pin them, then `git checkout --` of the three files | 1, 3 failed; restored, status clean |
| `rev-parse --verify --quiet` of `release/v0.22.1@{upstream}`, `origin/release/v0.22.1`, `release/v0.22.1` in the worktree and in the clone | worktree 1, 0, 1; clone 1, 1, 1 |
| `broad_gate.resolve_base` on the worktree and on the clone with `release/v0.22.1` | `origin/release/v0.22.1` at 2fc33333; ref as given, commit `None` |
| `git log --no-merges --name-only 83baeb91..HEAD ^origin/release/v0.22.1` in the worktree | 0 |
| `git show <rev>:agents/sealer.md` in the clone for `origin/release/v0.22.1`, `release/v0.22.1` and 2fc33333bcfef5f0fa9e7d6d7bc6469366c6f2ff | 128, 128, 0 |
| `noninferiority.py run --agent sealer --from-raw` of `969-phase-6c-raw` into `<scratch>/round-3/re/`, `cmp` against the clone's and the worktree's `evals/reference-sealer.json` | 0; 0, 0 |
| `side_numbers` on the committed reference; sha256 and byte counts of the two preloaded files | the figures of the fourth confirmation |
| `Bash` commands of the ten reference traces matching clone, checkout, rev-parse or upstream | every sealer resolved `main` through the three spellings; the at-base clones were `git clone -q <root> <at-base>` restored from `main` or a hash |
| `git grep -n -F` of each changed sentence's fragment over `tests`, `evals`, `agents`, `skills`, `docs` and `CONTRIBUTING.md` | only the sites in the fix diff and their pins |
| the class grep of the second confirmation | 34 lines, none a present-tense owner of the gate outside #967's pin |
