# Review round 3: 1795397629-git-runs-through-thirty-hand-written-helpers

```seal
target: 122ea4685558af9280320502be267dc1942ecc7f, fixes 64a28d00f..122ea4685
```

This is a verifying round. Its range is five commits after round 2's target, and each touches one record of the work item alone (executed: `git diff --name-only 64a28d00f..HEAD`, and `git show --stat` of `5fa72e29b` and `122ea4685`):

- `27925f55b`, round 2's record;
- `5fa72e29b`, one row added to `gaps.md`;
- `972c21ad6`, round 2's close block;
- `1df71771e`, `trail/gate.md`;
- `122ea4685`, `guarantee.md`.

No code and no case changed, so nothing in the range is reviewed as code. `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `changelog.md` and `pr.md` are byte for byte what round 2 read whole at `64a28d00f`, and the diff above shows it. `gaps.md` differs from that text by the one row, read here with the table it stands in. `trail/gate.md` and `guarantee.md` were read whole. No `pr.<lang>.md` stands, and `seal/parity.json` is not declared.

Round 2 asked for this round because its one finding named two test files in `location:` beside `gaps.md`. That finding's grounds and fix were in `gaps.md` alone. The two test paths only pointed to the cases the missing row describes, and that kept the fix from counting as records-only. Its close holds, and this round finds nothing new.

## Findings

None.

## Confirmations

```seal
confirms: round-2#1
```

What holds: read at the target, `gaps.md:14` stands after the phase 5 row of *Not verified* and is round 2's row word for word. It names `Test_main::test_refuses_a_listing_git_refused_in_one_line` and `Test_module::test_a_close_or_the_last_create_gh_refuses_stops_the_release`, says each ran on macOS alone, and names the pull request's Windows leg as the answerer. The close's reason for keeping the phase 5 row holds. The row speaks of the cases phase 5 added, which do time out one call, and the new row now covers the case it did not describe. Executed: `git show --stat 5fa72e29b` shows `gaps.md` alone, one line added.

What matched, read against the target: `trail/gate.md` names `972c21ad6 against c3f568c6a`, and only `1df71771e`, the gate record itself, follows it before the guarantee. `guarantee.md` states its audit at `1df71771e`, and each claim it makes about this work item's records agrees with them:

- `pr.md` quotes `frame/plan.md:71` and `:72`.
- `## Removes` holds 13 rows (`frame/design.md:159-171`).
- The diff from the base touches 68 files. Executed: `git diff --stat c3f568c6a..1df71771e`.
- The branch read it names is at `chain_check.py:1901`. Read: the line is the `routing.current_branch` call.
- Round 2's finding was fixed in `gaps.md` alone.

Its *Outside this guarantee* repeats round 1's *Not judged* rows with their answerers and no verdict on them. This round passes no judgment on the guarantee's verdict, which is the sealer's.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether `guarantee.md`, whose `target:` names `1df71771e`, still holds once this record is committed after it. This record touches the work item's records alone and changes no fact the guarantee audited | `seal/threads/1795397629-git-runs-through-thirty-hand-written-helpers/guarantee.md`, its `target:` line | the orchestrator, against `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* and the pull request's `chain-check` run |
| The suite, the lint and the typecheck. `trail/gate.md` records the broad run at `972c21ad6`, and this round ran none of the three (contract rule 2) | `seal/threads/1795397629-git-runs-through-thirty-hand-written-helpers/trail/gate.md` | the orchestrator's broad run, already recorded |
| The five rows of round 1's *Not judged* stand as round 1 wrote them | `seal/threads/1795397629-git-runs-through-thirty-hand-written-helpers/trail/rounds/round-1.md` | the answerers round 1 names |
