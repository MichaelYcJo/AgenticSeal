# 1792126889-every-agent-is-written-anew-from-its-job — review round 2

target: 155920f5, fixes 45f0d963..155920f5

## Findings

### 1. The contract's §2 now names the sealer as the one agent that runs the broad gate, and still tells it to hand the suite over unverified

severity: must
location: `skills/agent-contract/SKILL.md:42-46`, `agents/sealer.md:75`, `docs/the-broad-gate.md:38-41`, `tests/test_broad_gate_rule.py:179`
verdict: fixed 8d7e6a44
regression: round-1#1

The unit is contract §2, which 91741abf rewrote. The frame (`spec.md:153-154`,
`plan.md` row 3) had §2 say that no agent runs the broad gate; the fix made
§2 name the sealer as the one agent that runs it, as round 1 asked; the
defect comes from keeping the build's hand-over sentence, which was written
for a §2 in which no agent ran the gate, and which now reaches the agent that
does.

Read at 155920f5. §2 says: "No agent runs any of the three but the sealer,
whose definition hands it that run ... Hand over with the suite labelled
`unverified` and the orchestrator named as its answerer". The second
sentence has no exception, so it binds the sealer too. The sealer's own
step 6 (`agents/sealer.md:75`) tells it to return the gate's `SEALED` or
`NOT SEALED` lines, which is the run's result. `docs/the-broad-gate.md:38-41`
still states the rule with the exception: "Where it is yours, the same
handover carries the result instead of the label." The contract at af9c924b
carried that same clause, "Where the act is yours, the same handover carries
the result instead of the label." The build dropped it when §2 said nobody
ran the gate. The fix gave the run back to the sealer and did not restore the
clause.

So the sealer's preload once again contradicts its definition. This is the
same kind of defect round 1 rated `must`: the item's own §19 and `spec.md`
S15 do not let a contract that contradicts the sealer it is preloaded into
land. The fix is one clause. The pins below are in the case that already
holds §2's wording (`tests/test_broad_gate_rule.py:179`). No test reads the
exception today (`git grep -n -F 'instead of the label' -- skills agents docs
tests` finds only `docs/the-broad-gate.md:41`, executed).

```markdown
rounds settle, by `broad-gate --base <base> --record <item>`. No agent runs
any of the three but the sealer, whose definition hands it that run; #969
moves the run to the orchestrator, before it spawns the sealer. Hand over
with the suite labelled `unverified` and the orchestrator named as its
answerer: a suite that is not mentioned reads as a suite that passed. Where
the run is yours, the same hand-over carries its result instead of the label.
```

```python
    assert (
        "Where the run is yours, the same hand-over carries its result "
        "instead of the label"
    ) in body, (
        "§2 tells the sealer, the one agent that runs the gate, to hand its "
        "suite over unverified"
    )
```

answer: Fixed as proposed. §2 ends "Where the run is yours, the same hand-over carries its result instead of the label." and names the broad-gate case beside its `Enforced by:` target. The pin is in `test_the_prohibition_itself_has_one_home_and_it_is_the_contract`, and it was seen red (exit 1, that case failing) against §2 at 74c6a75a before the sentence was added. A grep of the contract and `agents/` finds no other sentence telling every agent to label the suite `unverified`. `agents/smith.md:232` and `agents/warden.md:140` speak of the smith's own hand-over, and `docs/the-broad-gate.md:38-41` already carries the exception.

### 2. The changelog fragment says a warden spawn preloads 27,032 bytes, and at this HEAD it preloads 27,018

severity: should
location: `seal/specs/1792126889-every-agent-is-written-anew-from-its-job/changelog.md:6`
verdict: fixed ea8b0c9d
regression: round-1#7

The unit is the fragment's first bullet, which 927f64e9 rewrote. The frame
(`spec.md` §*A number in this frame names its moment or its bound*, and
`plan.md` row 6) asks the fragment to give each before-and-after figure the
commit it was read at. The fix named the moment in one line under the table,
"Each figure is the tree at `af9c924b` → at `93c1878c`", and kept the
bullet's present tense: "a warden spawn preloads 27,032 bytes where it
preloaded 76,019". The defect comes from the fix pass's own 91741abf (§2,
46 bytes shorter) and 0067cff0 (step 7, 32 bytes longer). Both commits were
made before 927f64e9 and moved the figure that sentence states.

Executed: `git show <rev>:<file> | wc -c` gives `agents/warden.md` 10,495 plus
the contract 16,537, so 27,032, at 93c1878c. At 155920f5 it gives 10,527 plus
16,491, so 27,018. The sum is the figure the record carries:
`evals/warden-phase-3.md` "New preload bytes | 27032". The table is right
and states its moment. The bullet states the same number as a fact about the
plugin a user installs, and a sentence placed after the table does not reach
back to it. The prompt asked this round to judge keeping the figures as
measured. Keeping them is right, because 93c1878c is what the evaluation
ran, and rule 4 still holds by arithmetic (27,018 < 76,019). Only the bullet
has to say when its figure was read.

```markdown
  about half their former size, and a warden spawn preloaded 27,032 bytes at
  its evaluation (`93c1878c`) where it preloaded 76,019 at `af9c924b`. Before
```

answer: Fixed as proposed: the bullet keeps the measured figure and names its moment, 93c1878c. The harness's `preload_bytes` at 8d7e6a44 gives 27,198, because finding 1's sentence is 180 bytes; a figure stated for HEAD would move again with the next edit. Rule 4 still holds by arithmetic, 27,198 < 76,019. The table under the bullet already names its commits.

## Confirmations

confirms: round-1#1
The ownership half is closed. §2 names the sealer as the one agent that runs
the gate by `broad-gate --base <base> --record <item>`, and names #969 as
where the run moves (`skills/agent-contract/SKILL.md:37-46`, read).
`agents/sealer.md:106-109` recites that §2. The sites round 1 named agree
with it, and I re-read each at 155920f5 rather than carrying round 1's
reading: `skills/code-review/orchestration.md:178-188`,
`CONTRIBUTING.md:107-110`, `bin/test:22-25`,
`skills/code-review/scripts/chain_check.py:1570`, `agents/smith.md:299`,
`docs/the-broad-gate.md:11` (read). `git grep` finds no sentence outside
`seal/specs/` that still says no agent runs the gate (executed). Executed:
with the contract and `agents/sealer.md` put back to 45f0d963 in the clone,
`test_the_prohibition_itself_has_one_home_and_it_is_the_contract`,
`test_each_section_holds_its_rule[2]` and
`test_deleting_a_pinned_phrase_is_caught[2]` fail, and they pass at
155920f5. The hand-over clause is finding 1.

confirms: round-1#2
`verdict` now gives `no result` for a case the baseline ran and the new side
did not, whatever graders it carries, before the tolerance for a missing
shape or reach grader is applied (`evals/scripts/noninferiority.py:588-602`,
read). The tolerance is now confined to a case both sides ran. A case only
the new side ran still goes to rule 3 alone for shape and reach graders, and
to the run-count check for truth graders, which agrees with
`evals/README.md:32-33`. Executed: with `noninferiority.py` put back to
45f0d963, the two new cases fail, `a side cut to one case of four` and `a
case the baseline ran and the new side did not, whatever its graders`, while
the other 62 pass. `check` on the six records gives the verdicts they record:
warden-phase-3 and smith-phase-3 exit 0; framer-phase-3, sealer-phase-3,
warden-phase-2 and warden-phase-2-run-1 exit 1, each with its recorded rule
3 or rule 5 reason.

confirms: round-1#3
`test_every_definition_preloads_the_contract`
(`tests/test_every_agent_reads_the_contract.py:138-146`) holds
`agent-contract` in the `skills:` list of every file under `agents/` and skips
none. The shape case's skips now name #967 to #970. Read against its group:
the shape case skips the four not yet rewritten, so the new case covers what
its group does not. Executed: with `agent-contract` removed from
`agents/smith.md` in the clone, `[agents/smith.md]` fails and nothing else in
the module does.

confirms: round-1#4
Rule 1 is stated with its one-find allowance in `evals/README.md:29-30`, in
the module docstring (`evals/scripts/noninferiority.py:23-25`) and in
`verdict`'s docstring (`:571-573`). It matches the `noise` branch it
describes (read).

confirms: round-1#5
`docs/the-agent-set.md:26-33` and `questions.md:15-19` say what the build
did. Executed: comparing the contract's headings at 155920f5 and at
af9c924b shows §1 to §10 and §12 to §15 at their numbers, the old §16 (where
`seal/` resolves) inside §11's heading, the old §17 (the commit rule) at §16,
and §17 to §20 new. `test_every_cited_section_exists`'s docstring says the
same.

confirms: round-1#6
`awk -F'|'` over `plan.md`'s Phases table gives four cells for rows 1, 1b and
2 to 6 (executed). Each Status cell holds its text.

confirms: round-1#7
The noun is fixed, "12 known defects, each run twice, ... 16 of 24 finds ...
13". Recounted from `evals/warden-phase-3.md`'s twelve truth rows: 13 finds
on the baseline and 16 on the new side (read). Every figure in the table
matches its record's rows: preload bytes, tokens per tool call, spend and
verdict for the warden, the smith and the framer (read against
`evals/<agent>-phase-3.md`). "About a fifth smaller" for the contract is
16,491 against 20,368, 19% (executed, `wc -c`). The bullet's present-tense
preload figure is finding 2.

confirms: round-1#8
`agents/warden.md:48-49` names `--root <the branch worktree>`, and
`test_the_warden_checks_its_record_in_the_branch_worktree` reads the command.
Executed: with `--root <the branch worktree>` removed from the clone's
`agents/warden.md`, that case fails, and it passes at 155920f5.

confirms: none
The prompt asked this round to judge the frame's sentences left as history.
They are acceptable as left: `spec.md:143`, `spec.md:153-158` (numbered anew,
§2 saying no agent runs the gate), `spec.md:24` and `spec.md:199`, `plan.md`
row 3's Delivers cell, and the T1 row's "until phase 5". Each is answered by
a divergence row in `overview.md`: "Round 1: what the contract's §2 says",
"Phase 3: the contract's section numbers" and "Phases 4 to 6" (read). This
is the practice the item already follows, as in phase 2's row "the frame's
sentence is the frame's to correct". One coordinate is loose. The §2 row
cites `spec.md` §*Scope*, which holds the orchestrator-run gate
(`spec.md:41-42`). The §2 sentences themselves sit at `spec.md:153-154` and
`spec.md:199`. A reader following the row still lands on a true statement of
the frame.

confirms: none
`bin/test` over `tests/test_broad_gate_rule.py`,
`tests/test_the_agent_contract_holds_the_universal_rules.py`,
`tests/test_a_rewritten_definition_proved_non_inferior.py`,
`tests/test_every_agent_reads_the_contract.py` and
`tests/test_a_moved_rule_leaves_its_definition.py` exits 0, with 384 passed
and 4 skipped. `bin/rules --check` exits 0, with 463 targets in 60 files
(executed, in the clone at 155920f5). These are the modules that `git grep
-F` over `tests evals` finds for each changed sentence, except
`tests/test_the_seal_is_taken_once_by_the_sealer.py`, whose only change is a
comment.

## Not judged

| What | Location | Who answers |
|---|---|---|
| CI run 39043767134 at 155920f5, and the full suite, lint and typecheck; not waited on, and not run, per contract §2 | the branch | the orchestrator, then the sealer's broad gate after the rounds settle |
| Whether the warden's outcome and rule 5 still hold at a preload 14 bytes smaller than the one measured; rule 4 holds by arithmetic, and no paid evaluation ran | `evals/warden-phase-3.md` | the orchestrator, at the milestone's close against af9c924b |
| `tests/test_the_seal_is_taken_once_by_the_sealer.py` was not run; its diff is one comment | `tests/test_the_seal_is_taken_once_by_the_sealer.py:8222-8225` | the broad gate |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the five modules named in the last confirmation; `bin/rules --check` | exit 0, 384 passed, 4 skipped; exit 0, 463 targets in 60 files |
| `noninferiority.py check evals/<record>.md` for the six records | warden-phase-3 0, smith-phase-3 0, framer-phase-3 1, sealer-phase-3 1, warden-phase-2 1, warden-phase-2-run-1 1, each with its recorded reason |
| `git checkout 45f0d963 -- evals/scripts/noninferiority.py` in the clone, then `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py`; restored | exit 1: the two new no-result cases fail, 62 pass |
| `git checkout 45f0d963 -- skills/agent-contract/SKILL.md agents/sealer.md` in the clone, then `bin/test` over the broad-gate and contract modules; restored | exit 1: 3 failed (the prohibition case, `test_each_section_holds_its_rule[2]`, `test_deleting_a_pinned_phrase_is_caught[2]`), 77 passed |
| `agent-contract` removed from the clone's `agents/smith.md` and `--root <the branch worktree>` from its `agents/warden.md`, then `bin/test` over the two modules; restored | exit 1: 2 failed (`test_every_definition_preloads_the_contract[agents/smith.md]`, `test_the_warden_checks_its_record_in_the_branch_worktree`), 238 passed, 4 skipped |
| `git show <rev>:<file> \| wc -c` for the five definitions and the contract at af9c924b, 93c1878c, 2dfa53a9 and 155920f5 | warden preload 27,032 at 93c1878c and 2dfa53a9, 27,018 at 155920f5; contract 20,368, 16,537, 16,537, 16,491 |
