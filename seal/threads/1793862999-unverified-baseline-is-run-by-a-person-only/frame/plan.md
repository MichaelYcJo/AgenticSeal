# Implementation Plan: `seal unverified --baseline` leaves (#1240)

## Technical context

`skills/verify/scripts/unverified_check.py` (1981 lines at `a0303ee9`) does two jobs. The first is the plain run: it walks the given paths for `gaps.md`, reads each `## Not verified` section, reports the open rows, and fails on a section it cannot read (`overviews`, `check_file`, `check_text`, and `main` lines 1697-1714, 1786-1800 and 1908-1966). The second is the `--baseline` arm (`main` lines 1681-1694, 1716-1784, 1802-1906), together with the units that serve only that arm (design *Scope* item 2). Other scripts also load the module as a shared reader. `chain_check.py` takes `resolves`, `merge_base`, `settled` (and through it `tree_at`), `rule_changes` and others from it. `settle.py` takes `open_record_rows` and `show`. Each kept unit is listed in design *Grounding*, the importers row. The plain run is left as it is, except that `overviews` reads each argument at its real path again.

`tests/skills/test_unverified_check.py` has 3252 lines. 45 of its lines pass `"--baseline"`, and nine of its unit classes test units that leave. The rule markers that only `--baseline` cases carry are listed in design *Grounding*, the markers row.

Failure scenario of the chosen approach, six months from now:

- A reader sees that `resolves`, `merge_base`, `commit_of`, `settled` and `tree_at` are unused by the module's own `main` and deletes them. `chain_check.py` then breaks. `tests/skills/test_chain_check.py` drives those functions through `chain_check.py`, and after this change each docstring names `chain_check.py` as its caller.
- A memo or row deleted outside any reviewed diff is read by nobody. That gap is what the owner accepted: the proofer reads the closing memo's diff, and a deletion with no pull request has no proofer.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. Remove `--baseline` and every unit that only it used. Keep the units other scripts load where they are, and rewrite their text to name today's callers. | See *Technical context*. | Chosen. It carries out the owner's decision of 2026-11-05 (issue #1240) and changes nothing that `chain_check.py` or `settle.py` reads. |
| 2. Rebuild the comparison on `os.path.samefile`. This was #1240's earlier body, answering #1238 and #1264. | Each new shape of path (another volume, a named link loop, a case-insensitive volume) reopens a check that only a person runs. #1225's three rounds and its two fixes found one such shape after another (issue #1240, *Symptom*). | Rejected by the owner's decision, which this frame does not reopen. |
| 3. Move `settled`, `tree_at`, `resolves`, `merge_base` and `commit_of` into `chain_check.py`, the only caller left. This replaces the shared-reader structure for them. | The module of the required pull-request gate, and its tests, change for a removal made somewhere else. The citations of `unverified_check.py#settled` in `docs/checks/the-fold.md`, `docs/running/the-review-and-parity-arms.md` and `chain_check.py`'s docstrings would all be re-pointed, and `Test_settled`, `Test_merge_base` and their fixtures would move between modules. No reader gains anything. | Rejected. The premise that keeps the structure was checked: the module already holds `rule_changes` for `chain_check.py` alone, and its own `main` never calls it (design *Grounding*). One more predicate in that position is the module's existing shape. |
| 4. Also remove the exit-0 states `settled_root`, `absent_root` and `unwritten_root`. They were built for the CI step (#952) and for runs of `--baseline origin/<base> seal/threads/` (G7 of #517). | A person who runs `seal unverified seal/threads/` after a complete settle, or in a repository with no root, gets exit 2 where today they get exit 0 with the state named. The rules `nothing-declared-nothing-owed` and `an-empty-root-is-settled` would each change, although `tests/skills/test_settle.py` and `tests/skills/test_chain_check.py` carry them too. | Rejected for this item. The owner kept the plain run, and these states belong to it. Only their sentences about the base go (design *Scope* item 4). |
| 5. Keep `overviews` reading through `as_named`. | It keeps `as_named`, `repository_of`, `_absolute`, `nearest_existing` and `real`, which is the spelling machinery #1240 removes. #1225 made that reading so that the base would see a named link at its own path. With no base, the output is the same either way, because `unique_by_target` already reduces each memo to its real path. | Rejected. `overviews` goes back to `os.path.realpath`, as at `bf9efcba^` (design *Grounding*). |
| 6. Remove `evals/behaviour/proofer/seeded-55b66958/` along with the code it seeds a defect in. | The proofer suite's tree changes, and `compare` refuses a pair of sides taken across that change (`evals/README.md` *A proofer comparison compares two sides taken from the same point*). Every side measured before this change could no longer be compared with any side measured after it. | Rejected. The case fetches its own commits and reads nothing of the current tree, so the removal leaves its measurement valid. |
| 7. Edit `docs/` in place in this pull request, treating the subject as the policy root. | Work items running beside this one each rewrite the same sections. The layout reserves direct edits for work whose subject is the policy root's own structure or text. | Rejected. The subject is a command, so `docs/` waits for the settle through `## Rule changes` (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*). |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Design *Scope* items 1-8 | A1 seen red against `a0303ee9` and then green. The narrow run of `tests/skills/test_unverified_check.py`, `tests/skills/test_chain_check.py`, `tests/skills/test_settle.py`, `tests/behaviour/test_unverified_rows_close.py`, `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py` and `tests/github/test_rules.py`, which shows the `one-merge-base` check line as excused and nothing refused. `git grep -n 'a-settle-is-no-deletion' -- tests` names the chain_check case. `ruff check` and `ruff format --check` on the changed files. | |
| 2 | Design *Scope* items 9-11 | A5's command names nothing. The narrow run of the cases that read the four changed files, which `git grep -l -e SKILL.md -e README -- tests/behaviour tests/text` lists for the phase to choose from. A6 is read by review. | |

## Operational impact

- `seal unverified --baseline <ref>` now exits 2, because argparse does not know the argument. A user script that still passes it fails loudly rather than silently. No workflow that this plugin ships passes it: the hygiene template has run no `seal unverified` step since `5daa931f`, and a user's workflow clones the plugin at the tag it was written against.
- There are no new dependencies, environment variables or migrations.
- Stale ids in `.test_durations` drop no case (`CONTRIBUTING.md`, lines 166-167). This work does not touch the file.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
