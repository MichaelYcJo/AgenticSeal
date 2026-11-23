# Phase 1: 1795406406-code-stands-on-facts-that-no-longer-hold

## What this phase found

**The frame holds for this phase, with one statement the tree does not bear out.** `frame/design.md` *Scope* item 1 says the docstrings of `tests/github/test_close_issues_on_release.py` and `tests/github/test_label_merged_on_release_branch.py` name the removed files and are rewritten. Neither names `tracker_labels.py` or `test_tracker_labels.py`. G13's search matched them on `test_a_declared_label`, the behaviour file, which stays (`frame/plan.md` A7). The first says that file and `tests/behaviour/test_release_hygiene.py` keep the cases that read the workflow and the documents, and the behaviour file still holds A12 and A14. The second says the reader case was placed from that file, which is history. Both stand unchanged. Judged against `skills/core/SKILL.md` *The rule a mechanism is kept against*: what a change removes is what stood on the old fact, and neither sentence does.

**Four removals stood on the script and are not in `frame/design.md` `## Removes`.** Each goes in this phase on the same ground, the core's rule that a change removes in the same commit what stood on the old fact:

- `tests/github/test_close_issues_on_release.py#Tracker` lost its `labels` parameter, the `gh label list` and `gh label create` arms of `run`, and `writes`, with the `json` import only the `list` arm used. Only `tests/github/test_tracker_labels.py` passed `labels=` to it or called its `writes` (executed: `git grep -n -e 'Tracker(labels' -e 'writes()' 68b2f8136 -- tests`; the other matches, in `tests/github/test_label_merged_on_release_branch.py`, reach that file's own `Tracker` at `:59`). The closer's own `run` reaches only `arrived`, which every case replaces (read: `close_issues_on_release.py:343-345`), so `run` keeps its one arm that refuses any call.
- The case docstring at `tests/github/test_label_merged_on_release_branch.py:381` said the description goes to `gh label create` "too", beside the script's. The word goes.
- The comment over `label_merged_on_release_branch.py#LABEL_DESCRIPTION_LIMIT` said every description the directory sends is held by a case, and named both test files. It now says the one description this script sends is held, by the one case that reads the cap. Its account of a 119-character description failing the close-issues workflow is now in the past tense with #515, because no close-issues step sends a description (commit `7403ea0bc`).
- The comment over the roll step keeps why the roll carries `if: ${{ !cancelled() }}`, for the roll alone. #515's failed step is named as the step before the roll.

**The comment over `close_issues_on_release.py#SPENT_ON_CLOSE` says the label stands on the tracker and no script here creates it.** It no longer says where the label's description lives. The description is the tracker's, and `docs/releasing/issues-and-milestones.md` holds what the label means.

**A14 keeps its `parametrize` with one entry**, the roll step, as `frame/design.md` S6 states it, so the case's id keeps its step.

**This phase adds no behaviour, so it wrote no case and owed no `seal mutate` run** (`skills/verify/SKILL.md` *The narrow command still has to be able to fail*). To show that A14 can still fail against the trimmed workflow, one `seal mutate` run replaced the roll's `if: ${{ !cancelled() }}` with `if: ${{ success() }}`. A14 went red at its `found[0].get("if")` assertion, and `seal mutate` restored the file (executed).

**S5 and S6 hold** (executed at `7403ea0bc`). `git grep -n -e tracker_labels -e test_tracker_labels -- ':!seal/threads' ':!docs'` prints nothing, and over `docs/` it prints `docs/releasing/branch-and-release.md:130` alone, which `frame/design.md` `## Rule changes` rewrites at the settle. A14 passes, parametrized by the roll step alone.

**One line no edit touched now reads true.** `tests/github/test_roll_flow_measurement_issue.py:5` says the roll runs as a second step of `close-issues-on-release.yml`. While the label step stood, the roll was the third step after checkout. It is the second now.

**`tests/behaviour/test_every_tracked_file_meets_every_census.py` fails on `frame/design.md:30`**, G22, whose two `git -C` paths are absolute paths under a real home directory, which the census `real_identifiers` refuses. The line was committed with the frame at `68b2f8136`, and this phase wrote no line of it. The frame is not this phase's to write, so the hand-back names it for the orchestrator to fold.

**The next phase needs nothing from this one.** `frame/plan.md` *Overlap with the release* asks that the base be merged once #1573 lands, before phase 2, which is the orchestrator's to schedule.
