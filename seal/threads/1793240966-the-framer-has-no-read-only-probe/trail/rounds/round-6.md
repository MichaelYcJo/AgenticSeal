# Review round 6: 1793240966-the-framer-has-no-read-only-probe

target: df5611ee, fixes cce81ac1..df5611ee

This round verifies the fix pass over round 5. The range holds two
commits. `51859196` changes `evals/scripts/rule_cases.py` alone, at the
docstring's sealer paragraph. `df5611ee` commits the round-5 record with
finding 1's `verdict:` and `answer:` lines filled in. Round 5 closed one
finding, `fixed 51859196`, and this round answers it. Carried from round 5
without searching again: where the sealer runs stand (`SEALER_RUNS` at
`evals/scripts/rule_cases.py:762-782`), the commit that added the fifth run
(`4a6e24f6`), and that the merge base already read "four reviewed items".
Re-derived here: whether the new paragraph matches the five runs, whether
any other text in the tree states the sealer's count, whether the generator
still writes the committed cases, and whether the fix pass wrote only its
two lines in the round-5 record.

The fix pass's account claims the generator reproduces the committed
`framer/`, `crafter/` and `sealer/` cases, that the module's tests pass
with 16, and that `git grep` found no other statement of the count. This
round ran each again in its own clone and found the same, as the
confirmation below says.

## Findings

None.

## Confirmations

confirms: round-5#1
The sealer paragraph now counts five items and names the stale broad run.
Read: `evals/scripts/rule_cases.py:25-32` at `df5611ee`. It says "five
reviewed items" and lists five: one to seal, one with an untrue pull
request body, one with a false `seen red`, one with no broad run recorded,
and one whose broad run is followed by a code commit. That is the
paste-ready text of round 5 word for word. Each item matches one run of
`SEALER_RUNS` at `:762-782`, in the same order, and the fifth is the
`stale-gate` run at `:781`, whose gate value is `"stale"`. The comment at
`:756-761` defines `"stale"` as a record that a code commit follows, which
is what the new line says. The paragraph's tail, "naming what the tree
contradicts or that no broad run is on record", still covers the fifth
case. Its verdict pattern at `:781` is `no broad run`, and `SEALER_TRUTH`
at `:789-790` says the verdict reports no broad run on record at HEAD.
Executed: `ls evals/behaviour/sealer` lists five directories, and
`rule-sealer-stale-gate` is one of them.

Executed, the other statements of the count: `git grep` outside
`seal/threads/` for "four reviewed", "four sealer", "five sealer" and
"sealer cases" exited 1 with no hit. `git grep -w four` over `evals/`,
`docs/` and `agents/sealer.md` found only the crafter line at
`evals/scripts/rule_cases.py:16`, and that count is right: four builds and
one rename. The files that name `rule-sealer-no-gate` are
`agents/sealer.md`, `skills/agent-contract/SKILL.md`,
`tests/behaviour/test_the_sealer_guarantees.py` and the case itself. None
of them states a count. `agents/sealer.md` also names
`rule-sealer-stale-gate`. So this paragraph was the only place the count
stood, and no other place carries the old count.

Executed in the round's clone at `df5611ee`: `python3
evals/scripts/rule_cases.py --out` a scratch directory exited 0. `diff -r`
of its `framer/`, `crafter/`, `sealer/` and
`proofer/rule-proofer-one-finding/` against `evals/behaviour/` exited 0
each. `bin/test tests/evals/test_rule_cases.py -q -p no:xdist` exited 0
with 16 passed. `uvx ruff check` and `uvx ruff format --check` over the
file exited 0 and 0. This agrees with the fix pass's account.

The fix pass touched only its two lines in the round-5 record. Executed:
`git diff cce81ac1..df5611ee` of `trail/rounds/round-5.md` changes two
lines of finding 1: its verdict from `open` to `fixed 51859196`, and its
answer from empty to the fix pass's prose. Nothing else in the file
changed. `51859196` changes
`evals/scripts/rule_cases.py`, the path that the finding's `location:`
names. The answer says the paragraph now ends at `:32`, and it does.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck over the branch: `unverified`, not run by this round under contract rule 2 | the branch at `df5611ee` | the orchestrator, at `seal gate --base release/v0.24.1 --record 1793240966-the-framer-has-no-read-only-probe` |
| Whether `guarantee.md` and `trail/gate.md`, both written before `b9820880`, still hold for the tree at `df5611ee` | the work item's `guarantee.md` and `trail/gate.md` | the orchestrator's broad run, then the sealer's spawn after it |
| Whether the new rule made the other four framer cases worse: carried from round 1, still unmeasured | `evals/behaviour/framer/` | the owner, at #947's milestone run |

This round leaves nothing open. What comes due is the orchestrator's broad
run, and the sealer's spawn after it.

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the branch worktree into the round's scratch directory | exit 0, HEAD `df5611ee` |
| `git diff cce81ac1..df5611ee` | exit 0; two files, `evals/scripts/rule_cases.py` and `trail/rounds/round-5.md` |
| `ls evals/behaviour/sealer` | exit 0, five directories |
| `git log --oneline -S'"stale-gate"' -- evals/scripts/rule_cases.py` | exit 0, `4a6e24f6` |
| `git show 1e82fd0a:evals/scripts/rule_cases.py` | exit 0; the sealer paragraph reads "four reviewed items" |
| `git grep -n -i -E` outside `seal/threads/` for the sealer count's phrasings | exit 1, no hit |
| `git grep -n -i -w four` over `evals/`, `docs/` and `agents/sealer.md` | exit 0; only the crafter line at `evals/scripts/rule_cases.py:16` |
| `git grep -l` outside `seal/threads/` for `rule-sealer-no-gate` and for `rule-sealer-stale-gate` | exit 0 and 0; four files and two files |
| `python3 evals/scripts/rule_cases.py --out` the scratch directory | exit 0 |
| `diff -r` of `framer/`, `crafter/`, `sealer/` and `proofer/rule-proofer-one-finding/` against `evals/behaviour/` | exit 0, 0, 0 and 0 |
| `bin/test tests/evals/test_rule_cases.py -q -p no:xdist` | exit 0, 16 passed |
| `uvx ruff check` and `uvx ruff format --check` over `evals/scripts/rule_cases.py` | exit 0 and 0 |
| `chain_check.py --baseline origin/release/v0.24.1 --root` the branch worktree `--worktree`, with this record in place | exit 1; nothing refused in this record; two refusals stand, `trail/gate.md` behind HEAD at `51859196` and `guarantee.md` behind HEAD at `cce81ac1` |
