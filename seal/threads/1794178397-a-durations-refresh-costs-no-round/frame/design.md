# Design: a .test_durations refresh costs no review round and no broad run (#1444)

## Grounding

The tree as read at `94d04d30`.

| Policy clause | What it fixes for this work |
|---|---|
| G1. `skills/core/SKILL.md` *Judgment is not licence to skip a party*, row *No fix that no round reads* (read) | The invariant holds every change after the last round to a round's reading, through `skills/code-review/scripts/chain_check.py`'s records arm. This work changes neither the row nor the check. After it, no work item commits `.test_durations`, so no commit of the file follows any round. |
| G2. `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* and the `withheld` paragraph of *Orchestrator: the pull request opens once the sealer seals* (read) | A commit after the last round that touches a file outside the work item's records owes a verifying round, a second broad run and a second sealer. A mid-run refresh of `.test_durations` is such a commit today. That is the cost the ticket's log records, and this work removes its cause instead of granting the file an exception. |
| G3. `docs/releasing/branch-and-release.md` *Work accumulates on a release branch* (read) | Both rulesets require a pull request, so neither `main` nor `release/vX.Y.Z` takes a direct push, and no workflow can commit to a release branch. A refresh at the release therefore lands through a pull request into `release/vX.Y.Z`. |
| G4. `docs/releasing/release-checklist.md` *2b. Settle what earlier releases left behind* and `docs/checks/the-routing-check.md` *At the pull request* (read) | A change that is no work item opens no directory under `seal/threads/`, and each of its commits carries the trailer `Seal-Routing: no work item`, as the settle's commits do. The release refresh is such a change, so it owes no round and no sealer. |
| G5. `docs/releasing/release-checklist.md` *5. The release pull request* (read) | The orchestrator opens the release pull request after the last merge, and the owner's one required act is its merge. Its sentence "no pull request comes between the last work item and this one" is changed by `## Rule changes` below. |
| G6. `CONTRIBUTING.md:162-191` and `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:37-46`, `:90`, `:336-355` (read) | `test_the_durations_file_prices_the_suite` fails when more than `STALE_SHARE` (0.05) of the collected cases have no price in the file, or more than that share of the file's seconds belongs to entries nobody collects. It runs in every run of the suite: in each CI leg that collects the whole suite, and in the broad gate, whose `Broad gate` row in `seal/config.md` ends `bin/test -q`. The contributor refreshes from the branch's own latest `tests` run. |
| G7. `.github/workflows/test.yml:186-214` and `.github/scripts/durations_union.py#report` (read) | The `durations` job unions the Windows shards' parts into the `test-durations` artifact, the file a refresh commits, and its summary already reports the same two shares the suite case computes, against the committed file. The union's keys are the Windows collection, because each shard stores its own session with `--clean-durations`. |
| G8. Probe of the committed file against `main`'s latest union (executed) | `gh run download 42530874464 -n test-durations` (the `push` run at `94d04d30`) into the scratch directory, then a key comparison with the tree's `.test_durations`: union 5,919 cases, committed 5,891 entries, 65 unpriced (1.10 %), 37 dead entries holding 2.9 s of 1,599.8 s (0.18 %). `git log -- .test_durations` (executed) names `c6ec999a` (2026-11-06, #1376) as the last refresh, four releases earlier (0.34.0 to 0.35.1). |
| G9. The crossings the ticket logs (read) | `v0.33.0:seal/threads/1793935041-the-directory-refuses-every-command-hook/trail/rounds/round-2.md:25-62` and `:167-195`: a work item that moved `tests/hooks/` left 848 stale entries, and its round 2 read the refresh byte for byte and found a `gaps.md` sentence the refresh made false. The ticket cites #1027's 1,378 stale keys. Crossings came from one work item renaming or removing many cases, not from slow growth, which G8 measures at about a quarter of the share over four releases. |
| G10. #931 and `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#test_the_recipe_names_the_artifact_and_the_checklist_has_no_box` (read) | #931 settled that the file is refreshed on the threshold and that a failing check, never a checklist box, is the schedule, because 0.21.1 skipped the box. This frame keeps both. It moves where the check fails, from every run of the suite to the release pull request. |
| G11. `.github/workflows/test.yml#release-report` (read) | A job that acts only on a pull request into `main` already exists and is gated by `github.base_ref == 'main'`. The staleness verdict takes the same condition. |
| G12. `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | A script holds a gate only on a fact it reads exactly. Which keys of the union the committed file lacks, and the seconds of the keys it holds that the union lacks, are exact readings of two parsed maps. |
| G13. Ticket #1444 (executed) | `gh issue view 1444 --json comments` returned no comments on 2026-11-09, which agrees with the orchestrator's line. |

## Scope

In:

1. The staleness verdict leaves the suite. `test_the_durations_file_prices_the_suite` leaves `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, with every helper and fixture case that serves only it (`## Removes`). `collects_the_suite`, `tests/conftest.py#COLLECTED_NODE_IDS` and `test_no_collected_id_carries_the_interpreters_path` stay, because the last still reads the whole collection, and the union stays comparable with the committed file only while every id has one spelling.
2. `.github/scripts/durations_union.py` computes the two shares once, in one function that both its summary report and its verdict read. `STALE_SHARE` moves there at its present value, 0.05.
3. On a pull request into `main`, the `durations` job is red when either share is past `STALE_SHARE`, and only after the `test-durations` artifact of that run is uploaded, because that artifact is what the refresh commits. Its sentence names the counts, the shares, the first ids of each side, and the release remedy of item 4. On every other run the job writes the union and its report and passes as it does now.
4. The release remedy: the run's `test-durations` artifact is downloaded into a directory of its own and moved over `.test_durations`, committed alone with the trailer `Seal-Routing: no work item` on a branch cut from `release/vX.Y.Z`, and merged into it by a pull request. The release pull request's next run reads the refreshed file. `CONTRIBUTING.md`'s paragraph on the file states this remedy, and states that a work item never commits `.test_durations`.
5. `test_the_recipe_names_the_artifact_and_the_checklist_has_no_box` pins the rewritten paragraph's words, and still pins that `docs/releasing/release-checklist.md` *0. Before starting* holds no refresh box.
6. The sentences that state the old schedule are rewritten in place: the test module's docstring paragraph opening "And it is held to its age", and the comment above `tests/conftest.py#COLLECTED_NODE_IDS` that names the removed case.

A limit, stated in `CONTRIBUTING.md`'s paragraph and guarded by nothing: a shard that runs past its `timeout` during the release because the file is stale is answered by the same refresh, taken from the newest run whose `durations` job wrote the union, since a shard killed at its timeout uploads no part.

Out:

- `skills/code-review/scripts/chain_check.py`, `skills/code-review/orchestration.md` and the core's invariant table. Letting a durations-only commit follow the last round is weighed in `frame/plan.md` *Alternatives considered* and rejected there.
- The value of `STALE_SHARE`. The owner rejects a loosened number as an answer, and a rename within one work item crosses any share.
- Each leg's `timeout` and the shard counts.
- `.github/scripts/release_report.py`, which reads the file and judges nothing.
- A workflow that commits the refresh itself, which G3's rulesets forbid.
- The version move to 0.36.0, which the orchestrator assigns to another work item.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. A work item adds cases past the share | Given a branch whose new or renamed cases leave more than `STALE_SHARE` of the collection unpriced, when the orchestrator takes the broad run, then no case reads `.test_durations` against the collection, so the run does not fail on it, and no round reads a refresh. | `git grep -n 'prices_the_suite' -- tests` prints nothing; `bin/test tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` passes without the case. |
| S2. A pull request into a release branch | Given a stale committed file, when the `durations` job runs on a pull request whose base is not `main`, then it writes the union, uploads it, reports both shares in its summary, and exits 0. | A case of `tests/github/test_durations_union.py` drives the script over stale fixture parts without the verdict and reads exit 0 and the report lines. |
| S3. The release pull request, file past the share | Given the same file, when the job runs on a pull request into `main`, then it is red after the artifact upload, and its sentence names the counts, the shares, the first unpriced and first dead ids, and the remedy of *Scope* item 4. | Cases of `tests/github/test_durations_union.py` at the boundary: exactly the share passes and one more fails, on each side; both sides over name both in one sentence; an empty committed file is all unpriced and nothing dead. Each is seen red against the old script. |
| S4. The workflow's shape | Given `test.yml`, when its `durations` job is read, then the verdict is asked only where `github.base_ref == 'main'`, and the upload of `test-durations` does not depend on the verdict's exit. | A case in `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` reads the job's steps, beside `test_the_durations_job_needs_pytest_and_runs_unless_cancelled`. |
| S5. A contributor reads the recipe | Given `CONTRIBUTING.md` *Running the checks*, when the paragraph on `.test_durations` is read, then it names the release pull request's `durations` job as the schedule, the remedy of *Scope* item 4, the trailer, the limit sentence, and that a work item never commits the file; and the checklist's step 0 holds no refresh box. | `test_the_recipe_names_the_artifact_and_the_checklist_has_no_box`, rewritten, seen red against the old paragraph. |

## Data & interfaces

`.github/scripts/durations_union.py`:

- One function returns, for a union and a committed map, the unpriced ids in union order, the dead ids in the file's order, and the two shares. `report` reads it for its unpriced and dead lines, and the verdict reads it. An empty union is refused, as `unpriced` refuses an empty collection today.
- The verdict is asked by the command line, for instance a `--stale-fails` switch. With it, the script exits 1 when either share is past `STALE_SHARE`, having written the union and its report, and prints the sentence to stderr and to the summary. Exit codes become: 0 wrote the union and the file is within the share or the verdict was not asked; 1 wrote the union and the file is past the share; 2 refused and wrote nothing. The module docstring states all three.
- The sentence carries the remedy as one constant, the successor of the test module's `REMEDY`.

`.github/workflows/test.yml`, job `durations`: the verdict is asked only where `github.base_ref == 'main'`, and the `test-durations` upload runs whenever the union was written, so the red run still carries the file the refresh commits. Whether the verdict is a switch on the union step with an upload condition, or a separate last step, is the phase's choice, recorded in its phase record. `test_the_durations_job_needs_pytest_and_runs_unless_cancelled` reads the union step's words in pairs, so a switch without a value changes what that case parses.

## Rule changes

- change
  file: docs/releasing/release-checklist.md
  section: 5. The release pull request
  from: The version moved in the release's first pull
    request, so no pull request comes between the last work item and this one.
  to: The version moved in the release's first pull
    request, so the one pull request that may come between the last work item
    and this one refreshes `.test_durations`. The release pull request's
    `durations` job is red when the committed file prices too little of the
    suite its run measured, and its sentence names the refresh: the run's
    `test-durations` artifact, committed alone with the trailer
    `Seal-Routing: no work item`, in a pull request into `release/vX.Y.Z`,
    as `CONTRIBUTING.md` *Running the checks* gives it. The release pull
    request's next run reads the refreshed file.

## Removes

The work takes out the eight rows below.

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the suite case that fails every run on a stale file | `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#test_the_durations_file_prices_the_suite` | the `durations` job's verdict on a pull request into `main` (*Scope* item 3) |
| the share's helpers and constants | `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#unpriced`, `#dead`, `#staleness`, `#REMEDY`, `#STALE_SHARE` | the one share function, the remedy constant and `STALE_SHARE` in `.github/scripts/durations_union.py` |
| the fixture builders and their boundary constants | `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#_collection`, `#_with_gone`, `#FIXTURE_SIZE`, `#AT_THE_SHARE` | fixtures of `tests/github/test_durations_union.py`, which already builds parts and a committed file (`#write_parts`) |
| the fixture cases of the share | `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#test_exactly_the_share_unpriced_passes`, `#test_one_more_unpriced_fails_and_names_the_counts_and_the_recipe`, `#test_an_empty_collection_is_refused`, `#test_an_entry_nobody_collects_is_not_counted`, `#test_dead_seconds_past_the_share_fail_and_at_the_share_pass`, `#test_both_sides_over_are_named_in_one_sentence`, `#test_an_empty_file_is_all_unpriced_and_nothing_gone` | each is rewritten as a case of the script's function in `tests/github/test_durations_union.py`, one class per function as that file holds them |
| the report's own count of unpriced and dead entries | `.github/scripts/durations_union.py#report` | the one share function (*Data & interfaces*), so the summary and the verdict cannot disagree |
| the per-branch refresh recipe | `CONTRIBUTING.md:175-191`, the sentences from "When to commit it is" to the dispatch for a branch with no pull request | the release remedy (*Scope* item 4); a work item no longer refreshes, so the branch-run, re-run and dispatch instructions have no reader |
| the docstring paragraph that states the schedule as the suite case | `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:37-46` | rewritten in place to say the release pull request's `durations` job holds the file's age |
| the comment that names the removed case as the collection's reader | `tests/conftest.py:852-857` | rewritten in place to name `test_no_collected_id_carries_the_interpreters_path` |

The verdict added in *Scope* item 3 is a moved check, not a new one: the suite case it replaces ran on four CI jobs of every run (ubuntu at 3.12 and 3.14, one macOS shard, one Windows shard, as the v0.33.0 guarantee's CI row records) and in every broad run, and it caught the four crossings the ticket logs at a review round each.

Framed 2026-11-09 by framer, before the build.
