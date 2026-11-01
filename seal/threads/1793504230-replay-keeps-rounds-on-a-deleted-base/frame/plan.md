# Implementation Plan: 1793504230-replay-keeps-rounds-on-a-deleted-base

## Technical context

The code is `evals/scripts/replay_targets.py` at 48d035aa.

- `#ref_base` (lines 527–533) takes the ref as the tip where it resolves and LANDED where it does not, and returns the merge-base of the target and the tip. With no LANDED and no resolving ref it returns `""`.
- `#base_of` (lines 536–553), for a table record's asked paragraph, and `#target_base` (lines 556–572), for a `target:` value, both pass LANDED to `ref_base`.
- `#round_target` (lines 782–858) takes LANDED as a keyword. It passes it to `target_base` at line 817 and to `base_of` at line 820, and it leaves the round out as `<names> names no base that resolves` at line 823 where no base comes back.
- `#targets` (lines 861–881) calls `round_target` with no LANDED. This is the defect.
- `#written_at` (lines 282–298) gives the commit that last wrote a record: in the working tree's history where the tree holds it, else in the history of the first tag that holds it. `targets` already hands it to `round_target` as `wrote`, which picks the check that judges the record.
- `evals/scripts/seed_defects.py#target_at` (lines 230–273) passes `<commit>^1` as LANDED at line 249. It is not edited.

The cases are in `tests/evals/test_replay_targets.py`:

- `#two_layouts` (lines 207–272) builds a repository with each round pair committed on top of the commit it reviewed, and names its base as a commit (`against <sha>`), so LANDED is never read there. Scenario 2 needs a history shaped like a squash: a commit whose parent is the fork point, which holds the records and not the reviewed commit. The crafter either widens `two_layouts` with that shape or adds one builder beside it.
- `Test_module::test_a_labelled_target_names_its_base` (lines 565–590) unit-tests `target_base` and `base_of` with LANDED, with `git` stubbed to answer `merge-base` alone.
- `Test_module::test_targets_reads_the_next_round_by_the_commit_that_wrote_it` (lines 517–563) stubs `written_at` and `target_base`. It must keep passing with the new argument.

**Failure scenario of the chosen approach, in six months.** The approach rests on two premises. The first is that a pull request into a release branch is squashed, so the commit that last wrote a merged record holds none of the reviewed commits. The second is that the release branch only moves forward between a review and its release. A release branch that is force-pushed, or a pull request merged with a merge commit, breaks one of them. For a force-push, the base is still a commit on the branch's final line, and it can be later than the base the review saw. Nothing detects that, and the case then reviews a smaller diff than the round did. For a merge commit, scope item 2 leaves the round out instead of keeping an empty diff, and the reason it gives, that no base resolves, does not name the merge.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. Keep the structure: a round whose base ref was deleted stays left out | The premise that would keep it is that a deleted ref leaves no way to know the base. Checked, and it is false: for each of the 17 records whose release has a tag, the merge-base with the landed commit equals the merge-base with `v<X.Y.Z>^2`, the tip of the release branch at its release (`frame/design.md` *Grounding*, executed). Keeping it leaves 18 of 41 eligible rounds over the last two tags out of every list. | rejected |
| A2. Map `release/vX.Y.Z` to the tag `vX.Y.Z` and use the release merge's second parent as the tip | `v0.25.2` has no tag (executed), so its record stays out. The mapping parses a branch name into a tag name, a spelling rule the core asks a script not to carry (`skills/core/SKILL.md` *The rule a mechanism is kept against*). It covers release branches only, and a record can name any branch. | rejected |
| A3. Ask GitHub for each pull request's base (`gh pr view`) | The generator runs offline in a scratch clone and needs `gh` with credentials. A pull request's recorded base is its base at merge, not at the round, and nothing maps a round to its pull request number. | rejected |
| A4. Pass the tag the record was read at, or HEAD for the working tree, as LANDED | For a merged record it gives the same merge-base, because every commit after the landing descends from it and holds no reviewed commit. But LANDED would then depend on which tag was read rather than on the record, so one record read at two tags would take its base through two different commits. `written_at` gives one commit per record, the one the issue and `round_target`'s docstring name. | rejected |
| A5. Have `round_target` take LANDED from `wrote(rel)` when the caller passes none | `wrote` answers which commit's check judges a record. Folding the landed commit into it gives one parameter two meanings, and `seed_defects.py` passes a different LANDED (`<commit>^1`) while its `wrote` reads the shipped commit's history. The caller that knows the history passes LANDED, as `seed_defects.py` already does. | rejected |
| A6. Scope item 1 without scope item 2 | A working-tree record of a branch still in progress has a last writer that descends from its target. Where its ref does not resolve, as in a clone whose remote has another name, its merge-base is the target itself. The target's diff is then empty, its size is 0, and `--count` picks it before every other target. | rejected |
| A7. Scope item 2 for LANDED alone, and not for a ref that resolves | A ref that resolves and holds the target, such as a branch merged with a merge commit, gives the same empty diff. The class is a tip that holds the target, whichever way the tip was found (contract rule 12). | rejected |
| **A8. `targets` passes `written_at` of each record as LANDED (scope item 1), and `ref_base` gives no base where its tip holds the target (scope item 2)** | See *Technical context*. The probe keeps all 18 rounds, with no base equal to its target, and leaves every target kept today unchanged (`frame/design.md` *Grounding*, executed). | **chosen** |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1, 2 and 3 | `tests/evals/test_replay_targets.py` and `tests/evals/test_seed_defects.py` in one command, with Scenario 2's and Scenario 3's cases each seen red first (contract rule 15), and the `test_census` case of each module. Scenarios 1, 4 and 5 in a `git clone --no-local` of the phase's head with the origin's branches fetched and pruned and `refs/pull/*/head` fetched, each against the same command at 48d035aa. | |

## Operational impact

None for a deployer. Both generators are development scripts of this repository, and no script in the tree reads their output or exit code. `replay_targets.py --list` prints more kept lines than before. Over v0.27.0 and v0.26.0 on 2026-11-01 it would keep 41 targets instead of 23. `--count 4` over those two tags picks the same four cases as before, since the smallest of the 18 new targets is 231 lines and the four picked are 24, 33, 61 and 72 lines, one per work item (executed: the unchanged `--list` and the probe). #1229 regenerates the eight committed cases with `--case`, which writes the same bytes after this work (`frame/design.md` Scenario 4). A `--count` run at a later pair of tags can pick a case this work makes eligible.

#1228 edits `replay_targets.py#say_unanswered` and runs after this item, from a branch that holds it. The two items share no function.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
