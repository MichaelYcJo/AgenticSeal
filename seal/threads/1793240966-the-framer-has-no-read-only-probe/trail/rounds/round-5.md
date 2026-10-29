# Review round 5: 1793240966-the-framer-has-no-read-only-probe

target: b9820880, fixes bd7ad2db..b9820880

This round verifies the merge `b9820880`, which brought
`release/v0.24.1` at `99853d04` into the branch after #1091 (PR #1156),
#1046 (PR #1157) and `8de879bc` landed there. Its parents are `bd7ad2db`,
the branch as sealed, and `99853d04`. The chain check lists commits with
`--no-merges`, so no earlier round and no gate read this commit. Round 4
held no finding, so no close is owed an answer here. Carried from earlier
rounds without searching again: what `Test_framer_case` pins and how its
two cases were shown to catch the five mutants (round 4), and the framer
rule's coordinates in `agents/framer.md` (rounds 1 to 3). Re-derived here:
what the conflict resolution kept, which files both sides changed, whether
the generated cases still match the committed ones, and whether the
release's changes to the crafter, the contract, the verify skill and the
checks that read `agents/framer.md` break what this work item ships.

The orchestrator's prompt claims one conflict, in the docstring of
`evals/scripts/rule_cases.py`, resolved to keep #1091's crafter lines and
the branch's "five issues". This round found the same, as the first two
confirmations say.

## Findings

### 1. The fixture generator's docstring says the sealer has four cases, and it generates five

severity: should
location: `evals/scripts/rule_cases.py:25-31`
evidence: executed `ls evals/behaviour/sealer`, `git log --oneline -S'"stale-gate"' -- evals/scripts/rule_cases.py`, `git show 1e82fd0a:evals/scripts/rule_cases.py`
verdict: fixed 51859196

The module docstring is the one place that says what each agent's cases
check. Its sealer paragraph at `evals/scripts/rule_cases.py:25-31` says
"four reviewed items to guarantee" and describes four. `SEALER_RUNS` at
`:761-781` holds five runs, and `evals/behaviour/sealer/` holds five
directories. The fifth, `rule-sealer-stale-gate` at `:780`, is the one
where a broad run is on record and a code commit follows it, so the verdict
is `withheld` for a stale record. The docstring never names it. Someone
adding a sealer case reads the paragraph to learn what is covered, and it
leaves out the stale-record case.

This defect is not the merge's. `git log -S` dates the fifth run to
`4a6e24f6` (#969), and the merge base `1e82fd0a` already reads "four
reviewed items". Neither side of the merge touched the sealer paragraph.
This round reports it because the resolution rewrote the counts of the two
paragraphs above it, and it is the one count in the docstring left wrong.
The crafter count (four builds and one rename) and the framer count (five
issues) match `evals/behaviour/crafter/` and `evals/behaviour/framer/`,
five directories each.

```python
  sealer   five reviewed items to guarantee: one to seal, one whose pull
           request body claims a change the tree lacks, one whose phase
           record claims `seen red` for a case green against the old code,
           one to seal but for its broad run never recorded, and one whose
           broad run is recorded with a code commit after it; the verdict
           in `guarantee.md`, naming what the tree contradicts or that no
           broad run is on record, no commit, no broad gate run, no write
           but that file
```

answer: The finding holds. `ls evals/behaviour/sealer` lists five directories, `rule-sealer-stale-gate` among them. I fixed it here rather than deferring it. It is one sentence in the docstring whose framer line this branch already edits, and a deferral would leave the one wrong count beside two corrected ones. Commit `51859196` applies the paste-ready text to `evals/scripts/rule_cases.py:25-32`. The paragraph is one line longer, so it ends at `:32`. The commit changes the path this `location:` names, so the line gains nothing. `git grep -n -i -e "four reviewed" -e "four sealer" -e "sealer cases"` outside `seal/threads/` found this paragraph as the only statement of the count. After the fix, these were executed: `rule_cases.py --out <scratch>` exited 0, and `diff -r` of its `framer/`, `crafter/` and `sealer/` against `evals/behaviour/` exited 0 for each. Its `proofer/` differs only where the tree holds cases from the other generators. `bin/test tests/evals/test_rule_cases.py -q` exited 0 with 16 passed. `uvx ruff check` and `uvx ruff format --check` over the file each exited 0.

## Confirmations

confirms: none
The resolution keeps both sides' lines word for word and adds nothing.
Read: `git show b9820880 --cc`. The combined diff holds one hunk, in
`evals/scripts/rule_cases.py` at `:14-27`. The three crafter lines at
`:16-19` differ from the branch parent and equal the release parent, so
they are #1091's text. The framer lines at `:20-24` differ from the
release parent and equal the branch parent, so they are this work item's
text with "five issues". No other file shows in the combined diff, so
every other file took one side's content without a hand edit.

confirms: none
Only one file outside the records was changed by both sides. Executed: the
names changed from the merge base `1e82fd0a` to each parent, intersected.
The intersection is `evals/scripts/rule_cases.py` alone. The branch's other
shipped paths are `agents/framer.md`, `evals/behaviour/framer/rule-framer-sharp-s/`,
`tests/evals/test_rule_cases.py` and
`tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py`.
The release changed none of them.

confirms: none
The merged generator writes the committed cases byte for byte. Executed in
the round's clone at `b9820880`: `python3 evals/scripts/rule_cases.py
--out` a scratch directory exited 0. `diff -r` of `crafter/`, `framer/`
and `sealer/` against `evals/behaviour/` exited 0, 0 and 0, and of
`proofer/rule-proofer-one-finding/` exited 0. `diff -r` of the whole
`proofer/` exited 1 only because the committed directory also holds the
`replay-*` and `seeded-*` cases, which another generator writes. So both
the framer case `rule-framer-sharp-s` and #1091's `rule-crafter-rename`
come out of the merged `cases()` at `evals/scripts/rule_cases.py:944-951`.
This agrees with the orchestrator's account.

confirms: none
The release's changes leave the framer rule's text and its checks intact.
Read: the release side's diff from `1e82fd0a` to `99853d04` of
`skills/agent-contract/SKILL.md`, `agents/crafter.md`, `agents/sealer.md`,
`skills/implement/SKILL.md`, `skills/verify/SKILL.md`,
`tests/text/test_the_rules_have_one_owner.py`, `tests/censuses.py`,
`hooks/lib/routing.py` and `skills/code-review/scripts/chain_check.py`.
Contract rule 2 now names the set a builder runs at a phase boundary. The
framer rule at `agents/framer.md:132-149` cites rule 2 only for running
no repository check, and rule 2 still says no agent runs the broad gate.
#1091's rename row in `skills/verify/SKILL.md` and its crafter steps
govern a builder's proof of a rename. The framer builds nothing and has no
such step. #1157 moved Bootstrap and Parity setup out of
`skills/implement/orchestration.md`. Executed: `grep` of
`agents/framer.md`, the framer case and the branch's test module for
`orchestration.md`, `bootstrap` and `Parity setup` found only the test
module's constant for `skills/code-review/orchestration.md`, a file #1157
did not move. The heading `agents/framer.md` cites in the implement
skill, *3. The SDD file set*, stands at `skills/implement/SKILL.md:287`.
The routing declaration's `crafter` answer does not depend on the
`OLD_BY_CRAFTER` reading `8de879bc` removed.

confirms: none
The modules that read the merged files pass, and every rule's `check:`
target stands. Executed in the round's clone at `b9820880`: `bin/test`
over `tests/evals/test_rule_cases.py`, `tests/behaviour/test_evals_layout.py`,
`tests/text/test_no_case_tells_the_agent_it_is_evaluated.py`,
`tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py`,
`tests/text/test_the_rules_have_one_owner.py`,
`tests/text/test_every_agent_reads_the_contract.py`,
`tests/text/test_a_moved_rule_leaves_its_definition.py` and
`tests/text/test_the_agent_contract_holds_the_universal_rules.py` exited 0
with 343 passed. `bin/seal rules --check` exited 0, with 268 check lines
in 55 rule files holding. That includes the framer rule's two targets,
`evals/behaviour/framer/rule-framer-sharp-s/` and the parallel-agent test
module.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck over the merged tree: `unverified`, not run by this round under contract rule 2. `skills/verify/SKILL.md` names the broad gate as a merge's scope | the branch at `b9820880` | the orchestrator, at `seal gate --base release/v0.24.1 --record 1793240966-the-framer-has-no-read-only-probe` |
| Whether `guarantee.md` and `trail/gate.md`, both written before `b9820880`, still hold for the merged tree | the work item's `guarantee.md` and `trail/gate.md` | the orchestrator's broad run, then the sealer's spawn after it |
| Whether the new rule made the other four framer cases worse: carried from round 1, still unmeasured | `evals/behaviour/framer/` | the owner, at #947's milestone run |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the branch worktree into the round's scratch directory, at `b9820880` | exit 0 |
| `git show b9820880 --cc` | exit 0; one hunk, in `evals/scripts/rule_cases.py` |
| `git diff --name-only` from `1e82fd0a` to each parent, intersected with `comm -12` | exit 0; `evals/scripts/rule_cases.py` alone |
| `python3 evals/scripts/rule_cases.py --out` the scratch directory | exit 0 |
| `diff -r` of `crafter/`, `framer/`, `sealer/` and `proofer/rule-proofer-one-finding/` against `evals/behaviour/` | exit 0, 0, 0 and 0 |
| `diff -rq` of the whole `proofer/` against `evals/behaviour/proofer/` | exit 1; only the committed `replay-*` and `seeded-*` cases differ |
| `bin/test` over the eight modules named in the last confirmation, `-q -p no:xdist` | exit 0, 343 passed |
| `bin/seal rules --check` | exit 0, 268 check lines in 55 rule files hold |
| `grep` of the branch's shipped framer text and test module for `orchestration.md`, `bootstrap` and `Parity setup` | one hit, the test module's `skills/code-review/orchestration.md` constant |
| `ls evals/behaviour/sealer` and `git log --oneline -S'"stale-gate"' -- evals/scripts/rule_cases.py` | five directories; the run arrived at `4a6e24f6` |
| `git show 1e82fd0a:evals/scripts/rule_cases.py` | exit 0; the sealer paragraph already read "four reviewed items" |
