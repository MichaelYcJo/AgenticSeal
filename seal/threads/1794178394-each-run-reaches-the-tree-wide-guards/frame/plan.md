# Implementation Plan: each run reaches the tree-wide guards (#1441)

## Technical context

The tree as read at `94d04d30`.

The set a crafter runs is prose, and no script computes it. `skills/verify/SKILL.md:144` gives the `Phase boundary` row and `skills/verify/SKILL.md:146` gives the `Review rounds 1..n` row. `agents/crafter.md:52` (step 7) cites the first row, and `agents/crafter.md` step 9, the fix pass, cites neither. `bin/test` passes its arguments to pytest under `-n auto` (`.github/scripts/run_tests.py#main`), so a set is one command whatever its size.

This repository's layout already separates the two kinds of test file. The first paragraph of `CONTRIBUTING.md` *The test layout* gives each shipped module one file that declares `TARGET = "<path>"`. `CONTRIBUTING.md:267-269` puts every file that declares no `TARGET` in `tests/behaviour/` or `tests/text/`. A parse at `94d04d30` holds that placement without exception (`frame/design.md` *Grounding*, the `CONTRIBUTING.md` *The test layout* row). `seal layout --check` reports a file that declares no `TARGET` and does not check where it stands (`skills/verify/scripts/test_layout.py:44`, `:345-372`).

The cases that read the whole tree are mostly in those two directories already. A few stand in files that declare a `TARGET`, beside unit cases of the same module (`frame/design.md` *Grounding*, the row on tree-wide cases). These run only where their file is named, which is why #1176's round 4 met `seal layout` first at the broad gate.

The #1421 set shows where the width comes from. The glob clause, read as a text search, matched every file that writes `seal/threads`, `plan.md` or `gaps.md` into a fixture of its own. Every phase writes its own records, so every phase paid for those files (`frame/design.md` *Grounding*, the `.test_durations` row).

The chosen approach makes the guard set a place rather than a search. In this repository the place is the two directories that hold every file declaring no `TARGET`, and the tree-wide cases still elsewhere move into them. The verify table names that set as the repository's own declaration, and keeps the glob clause for a repository that declares none. A fix pass runs the same set over its own paths.

Failure scenario in six months: a contributor writes a new tree-wide case into a file that declares a `TARGET`. It runs only where that file is named, and it fails first at the broad gate, as #1176's did. Nothing refuses the placement, because no script can tell a case that reads the real tree from one that builds a fixture with the same paths. The proofer reads the placement against `CONTRIBUTING.md` *The test layout*. A second scenario: `tests/behaviour/` keeps growing, and every phase and fix pass pays for each new file. At `94d04d30` the two directories cost 118.9 s of stored price. After the move, the longest single case in them is the census sweep at 27.38 s, which sets a floor on the parallel wall time.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **Chosen.** The tree-wide set is the files that declare no `TARGET` (`tests/text/`, `tests/behaviour/`), and tree-wide cases move there. The third part is narrowed to naming a changed path in full, importing it or loading it. The glob clause is kept only as the fallback for a repository whose guide declares nothing. A fix pass runs the same set. | A tree-wide case written into a `TARGET` file is missed until the broad gate. The proofer reads placement, and nothing refuses it. | Chosen. For #1421's change it costs 143.1 s of stored price against 1,488.5 s, plus the moved cases' 34 s or so. It reaches every guard the ticket names that stands in the tree today, including the records readers the #1421 crafter re-ran, named in the row two below, which all stand in `tests/behaviour/`. |
| Keep the glob clause and the current placement, and add `tests/text/` and `seal layout --check` to every run (the ticket's "to weigh") | The phase set stays near the #1421 width. The records terms alone pull most of it on every phase, because every phase writes records (`frame/design.md` *Grounding*, the `.test_durations` row). The records readers in `tests/behaviour/`, and the census sweep in `tests/test_censuses.py`, still reach no fix pass. | Rejected. It keeps the structure that makes the set wide. The premise for keeping the glob clause, that a text search finds the files that read a directory, fails on fixture builders: `tests/skills/test_chain_check.py` matches `seal/threads` and costs 408.1 s on its own. |
| `tests/text/`, `seal layout --check` and `seal rules --check` in every run, with the glob clause dropped | The records readers (`test_docs_line_wrap.py`, `test_a_phase_hands_the_next_one_a_record.py`, `test_the_set_a_work_item_always_has.py`, `test_chain_hooks_hardening.py`), the release hygiene module and the census sweep reach no narrow run. #831's failure, in a hygiene module, comes back. | Rejected. It saves about 102 s of stored price and gives up the files the #1421 crafter itself re-ran after its record edits. |
| Drop the glob clause and add nothing | Every tree-wide file leaves the narrow runs, and the late failures the ticket lists come back. | Rejected. The ticket says narrowing alone brings the late failures back, and the reading agrees: no file that reads records is reached by naming a new work item's path. |
| Leave the tree-wide cases in their `TARGET` files, and name those files whole in the guard set | `tests/skills/test_test_layout.py` is 89.4 s and `tests/test_conftest.py` is 16.7 s, almost all of it unit cases. The list of named files is a list kept beside the tree, which the core forbids. A new such case is missed the same way as under the chosen approach. | Rejected. It costs more on every run and adds a list. |
| A pytest marker on each tree-wide case, or a declared list of guard modules in the runner | Same as above for the list. A marker is a new mark, which the owner rejects, and it owes a `## Removes` row with nothing to remove. | Rejected. |
| Run the tree-wide files in `seal gate --preflight` | The preflight runs no suite by design (#638, #697) and comes after the last round. A failure there still costs a fix and a verifying round, and it saves only the second gate and the second sealer. | Rejected. The failure has to come before the round that reads the tree, and that is the fix pass. |
| A `bin/test` option that computes the phase set from a base (`--changed <base>`) | A new script mode that encodes what "reads a path" means. It turns a judgment into a grammar rule and owes a `## Removes` row. The chosen set is one command of two directories and a few named files. | Rejected for this work. If the hand-drawn third part keeps costing calls, a later work item can measure it. |
| Have the proofer run the tree-wide files at the start of each round | The proofer would re-run a set the fix pass ran at the same commit. The core re-checks only what the diff shows changed. | Rejected. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 and 2 | The enumeration's method and its whole list in `trail/phases/phase-1.md`, as contract rule 12 asks. The moved cases pass at their new paths in one `bin/test` command. `bin/seal layout --moved <base> --from <old files> --to <new files>` exits 0, and its command and last line go in the record. `bin/seal layout --check` exits 0. A `git grep` for each moved case's name finds it only at its new path. This is the rename-or-move row of `skills/verify/SKILL.md` *The narrow command still has to be able to fail*, so it owes no new case and no `seal mutate` run. The phase boundary runs the set *Scope* item 3 describes for this phase's paths, as the frame decides here, because the old row is the text this work replaces. | `f40ab296` |
| 2 | `frame/design.md` *Scope* items 3, 4, 5, 6 and 7 | `git grep -n -F 'what the fix touches'` returns nothing outside `seal/threads/`. The glob clause stands only as the fallback. The phase boundary runs the new row's set for this phase's paths, which includes `tests/text/`, the files that read the edited prose. *Scope* item 7's two timed runs, each with its command, file count, case count, exit code and wall-clock seconds, are in `trail/phases/phase-2.md`. | |

## Operational impact

No migration, environment variable, dependency or compatibility break.

The cases *Scope* item 1 moves get new pytest ids. Their stored prices in `.test_durations` stay under the old ids until the next refresh. That is about 34 s of 1,599.8 s, under the stale-seconds bound `test_the_durations_file_prices_the_suite` reads. The Windows and macOS shards are divided by that file, so they shift by that much and drop no case.

This pull request does not move the version. The orchestrator assigns the move to 0.36.0 to one work item of the release later.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
