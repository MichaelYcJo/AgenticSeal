# Review round 3: 1793599989-a-release-is-sized-with-no-ceiling

```seal
target: 63c04805, fixes 9a67c0a4..63c04805
```

This is a verifying round over one merge resolution. Its target is `9a67c0a4..63c04805`, on the branch whose base is now `release/v0.29.0` at `d57e9ee7`, which holds #898. It was reviewed in a `git clone --no-local` of the branch worktree at `63c04805`, under `<scratchpad>/1289-round-3/clone`. Every command that names the base names `origin/release/v0.29.0`, which `git rev-parse` gives as `d57e9ee7` (executed). No `seal/parity.md` is declared at the target, so the round block holds no `original:` line (executed, `ls`).

The range holds three commits. `72e42440` adds `seal/threads/1793599989-a-release-is-sized-with-no-ceiling/handoff.md` and nothing else, and `7839017e` removes that file and nothing else, so `git diff 9a67c0a4 7839017e` is empty (executed). The third is `63c04805`, the merge of `d57e9ee7` into `7839017e`. `chain_check.py` lists commits with `--no-merges` and reads no merge, so this round is the reader of the resolution. Round 2 closed no finding, so no earlier finding is owed a `confirms:` or `reopens:` line. The round stayed inside the range and did not re-review #898's own change.

Facts carried from earlier rounds: none. The seven removed case names and the module's one remaining case were re-derived at this target and not taken from round 1's `## Confirmations`.

The implementer's account, claim by claim. The account is the orchestrator's spawn prompt.

- Claimed: the one conflict was `.test_durations`. `git show --remerge-diff 63c04805` names `.test_durations` as the only file whose content differs from git's own merge, with a content conflict there (executed). Every other file merged without a hand edit.
- Claimed: the release's file holds 6354 keys and the resolved file 6347. `json.load` of each gives 6354 and 6347 (executed).
- Claimed: `git diff --no-index` against the release's version shows 7 deletions and nothing else. `git diff d57e9ee7 63c04805 -- .test_durations` is one hunk of seven `-` lines and no `+` line (executed). Each of the 6347 kept keys has the release's value (executed).
- Claimed: `bin/test tests -q -k "test_the_durations_file_prices_the_suite or test_the_durations_file_parses"` gave 2 passed. This round ran the same command in the clone and it exited 0 with 2 passed (executed). That case passes while the share of unpriced or dead entries stays under `STALE_SHARE`, so a pass does not show an exact match. The second confirmation below shows it.

## Findings

No finding. The range adds no code and no test, so no test is read against a group.

## Confirmations

```seal
confirms: none
```
What matched: the resolved `.test_durations` is the release's file minus the seven rows of the cases this branch removed. The seven keys missing from the resolved file are `test_one_document_states_a_releases_size`, `test_the_count_survives_as_a_ceiling`, `test_the_pattern_catches_the_noun_forms_and_not_only_the_verb`, `test_the_scanned_set_reaches_the_file_a_rule_gets_restated_in`, `test_the_sweep_can_fail`, `test_the_sweep_reads_a_statement_whose_wrap_falls_inside_it` and `test_the_sweep_survives_a_tracked_file_the_tree_deleted`, each under `tests/behaviour/test_a_release_is_sized_by_a_criterion.py::`. These are the same seven names `git diff 40e6c23e 7839017e -- .test_durations` deletes on the branch side, where `40e6c23e` is the merge base. The resolved file adds no key and changes no value, and it keeps the release file's key order and layout, because the diff holds deletions only (executed).

```seal
confirms: none
```
What matched: at `63c04805` the resolved file prices every case the suite collects and holds no key for a case that is gone. `bin/test tests --collect-only -q -p no:xdist` collected 6347 node ids, all distinct, and exited 0. Read against those ids, the resolved file leaves 0 unpriced and holds 0 dead keys. The release's own file, read against the same collection, leaves 0 unpriced and holds 7 dead keys, and those 7 are exactly the keys the resolution removed. None of the seven removed names is collected at the target, and the module's one collected case is `test_the_rule_says_what_it_does_not_change`, whose key the resolved file keeps (executed, `## Probes`). The branch's other test change, the registry row it removes from `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:72`, is an entry of the dict `APPLIES_THE_SHARED_GUARD` and no case id, so it owes the file no row. The collection count settles this, since 6347 ids match 6347 keys with none unmatched (executed).

```seal
confirms: none
```
What matched: the merge changed nothing outside what #898's squash brought, apart from the resolved file. Excluding `.test_durations`, `git diff 7839017e 63c04805` and `git diff 40e6c23e d57e9ee7` have the same `git patch-id --stable`, `6e8ce79b`. That diff is the release side as it reaches the branch: `.claude-plugin/plugin.json`, `skills/verify/SKILL.md`, `skills/verify/scripts/mutation_check.py`, `tests/skills/test_mutation_check.py` and #898's work item under `seal/threads/1793599985-a-mutant-that-does-not-compile-reads-as-caught/`. Excluding the same file, `git diff d57e9ee7 63c04805` and `git diff 40e6c23e 7839017e` have the same patch-id, `0ace044a`, so the branch's own change reaches the merge unaltered (all executed). `git show --remerge-diff 63c04805` differs from git's automatic merge in `.test_durations` alone (executed).

```seal
confirms: none
```
What matched: `chain_check.py --baseline origin/release/v0.29.0 --root <branch worktree> --worktree` exited 0 before this record was written. This holds for the plugin's installed copy (0.28.0) and for the tree's copy at the target. Each printed lines only for the not-yet-written `trail/gate.md` and `guarantee.md`. It printed no pin notice and no line at `frame/design.md`, so this round takes no finding from a notice (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck. The suite is `unverified` on this branch, and this round collected it without running it | the tree at `63c04805` | the orchestrator's `seal gate --base release/v0.29.0 --record 1793599989-a-release-is-sized-with-no-ceiling`, then the sealer's spawn |
| Whether the Windows and ubuntu collections match the resolved file as the darwin collection does. The file is measured on the Windows shards, and a case whose id or presence depends on the platform is read only there | `.test_durations` against each leg's collection | the pull request's `tests` run, whose `test_the_durations_file_prices_the_suite` reads each leg's collection |
| S3's mutation results, carried from round 1 as read and not re-run | `trail/phases/phase-1.md:15-23` | the sealer, which samples the crafter's claims |

This round leaves nothing open. What comes due is the orchestrator's broad run, and the sealer's spawn after it.

## Probes

| Command | Result |
|---|---|
| `git show --remerge-diff --stat 63c04805` | one file, `.test_durations`, with a content conflict; no other file differs from git's automatic merge |
| `git diff 9a67c0a4 7839017e`; `git diff --name-only 9a67c0a4 72e42440` | empty; `seal/threads/1793599989-a-release-is-sized-with-no-ceiling/handoff.md` only |
| `git diff <a> <b> -- . ':(exclude).test_durations' \| git patch-id --stable` for `7839017e 63c04805` and `40e6c23e d57e9ee7`, then for `d57e9ee7 63c04805` and `40e6c23e 7839017e` | `6e8ce79b` for both of the first pair; `0ace044a` for both of the second |
| `git diff d57e9ee7 63c04805 -- .test_durations` and `git diff 40e6c23e 7839017e -- .test_durations` | each one hunk deleting the same seven keys of `tests/behaviour/test_a_release_is_sized_by_a_criterion.py`, no added line |
| `bin/test tests --collect-only -q -p no:xdist -p no:cacheprovider`, its node ids read with `python3 -I` against `json.load` of the resolved file and of `git show d57e9ee7:.test_durations` | exit 0, 6347 ids collected; resolved file 6347 keys, 0 unpriced, 0 dead, every kept value equal to the release's; release file 6354 keys, 0 unpriced, 7 dead, the seven removed keys |
| `bin/test tests -q -p no:cacheprovider -k "test_the_durations_file_prices_the_suite or test_the_durations_file_parses"` | exit 0, 2 passed |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.29.0 --root <branch worktree> --worktree`, the plugin's copy and the tree's, before the record | exit 0 for each; lines for `trail/gate.md` and `guarantee.md` only; no pin notice |
