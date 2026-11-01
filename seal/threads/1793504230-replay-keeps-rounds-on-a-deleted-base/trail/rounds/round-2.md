# Review round 2: 1793504230-replay-keeps-rounds-on-a-deleted-base

```seal
target: 42035ea3, fixes 61ff39aa..42035ea3
```

This verifying round reads the diff from round 1's target, 61ff39aa, to 42035ea3, the branch's head. It holds four commits after round 1's record: e446f10d rewrites the docstrings of `ref_base` and `round_target` and one test comment, 898fcbcd closes a row of `gaps.md`, 17dde57b repairs a line break e446f10d dropped, and 42035ea3 appends round 1's close block. The round ran in a `git clone --no-local` of the worktree at 42035ea3, in a scratch directory named for the work item and the round, removed before the hand-back.

Carried from round 1 and not re-established: that 7a8899d5, the later commit that rewrote two round 1 records, holds no commit of either target (round 1, finding 1). The two targets are reachable only through `refs/pull/*/head`, which this clone did not fetch. Re-established this round: the history of `release/v0.25.2` on GitHub, the base its one record gets, the adding commit and the last writer of the two rewritten records, and the narrow suite.

## Findings

None.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the close `fixed e446f10d`. The finding said that "the commit the work landed on" read two ways, and that `targets` at times passes neither of them. Both docstrings now drop the phrase.

`ref_base` (`evals/scripts/replay_targets.py:528-538`, read) says what LANDED is: "the tip REF had when the work was squashed onto it, or a commit that descends from that squash". `seed_defects.py#target_at` passes the first of these, the shipped squash's first parent (`evals/scripts/seed_defects.py:249`, read). `targets` passes the second, the record's last writer. The docstring then states the one property the base rests on: LANDED holds none of TARGET's own commits. The property is stated once, here.

`round_target` (`evals/scripts/replay_targets.py:796-801`, read) says once what each caller passes. `targets` passes "the commit that last wrote the record: the squash that landed the work, or a later commit that rewrote the record". `seed_defects.py#target_at` passes "the shipped squash's first parent, the tip the squash landed on". It cites `ref_base` for the property instead of restating it. The test comment (`tests/evals/test_replay_targets.py:643-645`, read) cites both docstrings and states neither fact again.

The text matches the history it describes (executed). Round 1 of `1793438028-pre-0-23-upgrade-readings-removed` was added by 5560c742, #1209's squash. Round 1 of `1793443708-settle-keeps-a-gaps-file-anywhere` was added by ea73e94f, #1210's squash. 7a8899d5 last wrote both, and `git merge-base --is-ancestor` shows that both squashes are its ancestors. So the later commit `targets` passes is "a commit that descends from that squash", as `ref_base` says.

The claim that the base rests on one property was checked against policy. The property alone does not give the fork REF named: LANDED must also hold that fork, which fails if REF is rewritten between the review and the squash. Policy rules that out. `docs/branch-and-release.md` *Two rulesets enforce the merge methods* (read) allows only a squash into `release/*` and requires a pull request with no bypass actors, so the branch takes no direct push and no force-push. With that, a tip REF had at the squash descends from the fork the review saw, and "one property" is complete. `frame/plan.md`'s failure scenario names the force-push. It is the case this ruleset excludes, not a premise the docstring leaves out.

One omission was weighed and is no defect. The gloss in `round_target` lists two kinds of last writer. It leaves out a third that `frame/design.md` *Scope* item 2 names: the last writer of a branch still in progress, which descends from its target. `ref_base`'s second paragraph names that writer as a tip that gives no base (`evals/scripts/replay_targets.py:536-538`, read), and `round_target` sends the reader to `ref_base`. LANDED reaches `ref_base` only where the ref does not resolve (`:539`, read), and for a record of a branch in progress that happens only in a clone whose remote is not named `origin`, which `frame/design.md` *Scope* puts out of scope. The two docstrings together give that writer one reading.

The fix changes no code. In each of the two changed Python files, an `ast` comparison of 61ff39aa and 42035ea3 with every docstring removed finds no difference (executed). In `tests/evals/test_replay_targets.py` the trees are equal even with docstrings, since only a comment changed. The narrow suite passes at 42035ea3 (`## Probes`).

```seal
confirms: none
```
What matched: no place that states what LANDED is was missed. The fix pass searched for two wordings, `work landed on` and `landed`, outside `seal/threads`. Its close lists what that search found and does not call the list whole. This round built the list from the value itself: every function that takes or passes the `landed` parameter, found by `git grep -n -i landed` over `evals` and `tests` (executed). For code, that list is whole, because no function can pass LANDED on without naming the parameter. It gives six functions and one test. `ref_base` and `round_target` are rewritten. `base_of` and `target_base` (`evals/scripts/replay_targets.py:547-548`, `:568-569`, read) say only "LANDED standing for a ref that no longer resolves", which agrees with the new text. The `targets` docstring (`:875-878`, read) says it passes "the commit that last wrote the record (`written_at`)". The `seed_defects.py#target_at` docstring (`evals/scripts/seed_defects.py:236-238`, read) names "COMMIT's first parent" before its gloss "the release branch the item landed on". That gloss calls a commit a branch, but the commit is already named, so the sentence still has one reading. The test comment at `tests/evals/test_replay_targets.py:643-645` is rewritten. The prose outside code is an unbounded domain of wordings, so this part of the list is a sample. It searched `docs/` and `evals/` for `landed`, `first parent`, `last wrote`, `deleted after` and `squash`, and read `evals/README.md`, which says nothing about how a replay case finds its base. The fix pass's search left out `seal/threads`, which holds the work item's changelog fragment (`seal/threads/1793504230-replay-keeps-rounds-on-a-deleted-base/changelog.md:3`, read). The fragment says "the commit that last wrote the round's record" and states the same property, so it agrees with both docstrings.

```seal
confirms: none
```
What matched: the closed `gaps.md` row for `release/v0.25.2` (898fcbcd). The row now opens with `closed`, as `skills/verify/scripts/unverified_check.py` reads a closed row, and its second cell cites round 1's confirmation, which exists (read). This round re-ran round 1's evidence instead of carrying it. GitHub's activity log for `refs/heads/release/v0.25.2` still shows three events: creation at 13dc7c63 at 00:55:28Z, PR #1196's merge from 13dc7c63 to f80f48e6 at 01:44:57Z, and deletion at 07:44:17Z on 2026-10-31 (executed). In the clone, `written_at` gives f80f48e6 as the last writer of round 1 of `1793408293-less-text-means-nothing-said-twice`. `ref_base('9a803e0b', 'origin/release/v0.25.2', <that writer>)` gives 13dc7c63, the tip the branch held throughout the review. `git merge-base --is-ancestor 9a803e0b f80f48e6` exits 1, so the guard does not fire (executed).

```seal
confirms: none
```
What matched: Scenario 4 does not need to run again, and the decision rests on what was executed. The eight committed cases are generated by `replay_targets.py` and by `seed_defects.py`, which imports it. Between 61ff39aa and 42035ea3, the only change to `replay_targets.py` is in two function docstrings: the `ast` comparison with docstrings removed is equal. The module docstring did not change (`git diff` shows two hunks, in `ref_base` and `round_target`). No code reads a function's docstring. The only `__doc__` read is the module docstring's first line for `argparse` (`evals/scripts/replay_targets.py:1012`, read; `grep -rn __doc__ evals/scripts/`, executed). `seed_defects.py` is unchanged. The one record that changed is this work item's own round 1, which none of the eight cases names. Every input of a `--case` run is therefore the same at both commits, and the output cannot differ.

```seal
confirms: none
```
What matched: 17dde57b's line break. The `round_target` docstring ends its LANDED sentences with "A" and opens the next line with "target is `{...}`", the layout it had at 61ff39aa (`evals/scripts/replay_targets.py:801-802`, read). `uvx ruff check` and `uvx ruff format --check` pass on both changed Python files (executed).

```seal
confirms: none
```
What matched: the suite's label. `gaps.md` *Not verified* still names the full suite, the repository-wide lint and the format check as unverified, to be answered by the orchestrator's `seal gate`. That label is honest (contract rule 2). The narrow run agrees: `bin/test tests/evals/test_replay_targets.py tests/evals/test_seed_defects.py -q` passed 46 at 42035ea3 (executed). This round leaves nothing open, so the orchestrator's broad run is due next, and then the sealer's spawn.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at 42035ea3 (contract rule 2) | the branch | the orchestrator, by `seal gate --base origin/release/v0.27.1 --record 1793504230-replay-keeps-rounds-on-a-deleted-base` |
| Whether 7a8899d5 holds no commit of `d25aad94` or `1090b7c3`. This round carried the fact from round 1, because the clone did not fetch `refs/pull/*/head` | `trail/rounds/round-1.md` finding 1 | the sealer, where it samples the rounds' executed claims |
| Whether every target the unchanged generator keeps over every release tag comes out equal with LANDED passed, which round 1 also left to the sealer | `frame/design.md` *Grounding*, the every-tag row | the sealer, where it samples the frame's executed claims |

## Probes

| Command | Result |
|---|---|
| `python3` `ast` comparison of `evals/scripts/replay_targets.py` and `tests/evals/test_replay_targets.py` at 61ff39aa and 42035ea3, docstrings removed | both equal; `replay_targets.py` differs only in docstrings, the test file not at all |
| `grep -rn __doc__ evals/scripts/` | four module-docstring reads for `argparse`, none of a function's docstring |
| `bin/test tests/evals/test_replay_targets.py tests/evals/test_seed_defects.py -q` at 42035ea3 | 46 passed, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` on the two changed Python files | both exit 0 |
| `gh api repos/MichaelYcJo/AgenticSeal/activity?ref=refs/heads/release/v0.25.2` | creation at 13dc7c63, one merge to f80f48e6, deletion; exit 0 |
| `python3 -c` calling `written_at` and `ref_base` for round 1 of `1793408293-less-text-means-nothing-said-twice` over `last_tags()` | last writer f80f48e6; base 13dc7c63 |
| `git log --format=%h --diff-filter=A` and `git log -1 --format=%h` at v0.27.0 on round 1 of `1793438028` and `1793443708`, then `git merge-base --is-ancestor` of each adding commit and 7a8899d5 | added by 5560c742 and ea73e94f, both last written by 7a8899d5, both ancestors of it |
| `git grep -n -i` for `landed`, `first parent`, `last wrote` and `deleted after` outside `seal/threads` | six functions and one test comment state LANDED; each agrees with the rewritten docstrings |
