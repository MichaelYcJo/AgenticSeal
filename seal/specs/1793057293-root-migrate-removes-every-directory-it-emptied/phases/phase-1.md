# Phase 1: 1793057293-root-migrate-removes-every-directory-it-emptied

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | db3670d2 |

## What this phase was asked

Commit the cases S1, S2 and S3 of `spec.md` *User scenarios & acceptance*
before any fix, with `hooks/root-migrate.py` unchanged, in one commit. Then
confirm locally that exactly those cases fail, with exit 1. Run only
`tests/test_root_migrate.py` and `tests/test_the_root_migrates_itself.py`,
and `uvx ruff check` and `uvx ruff format --check` over the changed Python
file. Build on `questions.md`'s defaults. Stop after this phase. The
orchestrator pushes the branch and runs the `tests` workflow on the three
systems to see the cases red there, and spawns phase 2 separately.

## What this phase found

**The frame holds** (`read`, at `d0c0a4bf`). Every coordinate in `plan.md`
*Technical context* is where it says. `move` opens at line 352 of
`hooks/root-migrate.py`, and its walk is lines 389 to 394. `run_moves` opens
at line 414. `main`'s printed line is built from `old_items` at lines 549 to
565. The four test ranges in `tests/test_root_migrate.py` are the cases the
plan names. `main` reads `old_items` after the run and names an id-shaped
directory with no tracked mark as "no routing.md or rounds/ that git tracks
— not a SpecSeal work item", as `spec.md` *Grounding* says. The
seen-red run below shows that line naming the moved item.

**The three cases, as built.**

- **S1** rewrites
  `Test_move::test_accepts_a_directory_whole_or_file_by_file_into_one_that_exists`.
  It plants and commits `specs/<ITEM>/phases/deep/p.md` in the case. It
  checks that `rounds/round-1.md`, `phases/deep/p.md` and `routing.md` are
  each at the destination. It then asserts that `specs/<ITEM>` does not
  exist. The comment and the `iterdir() == []` assertion are gone, as
  `## Removes` names them. The assertion that `specs/<ITEM>/rounds` is gone
  stays. `## Removes` does not name it, and S1's new assertion covers it.
- **S2** extends
  `Test_main::test_accepts_either_mark_alone_and_resumes_its_item_once_settled`.
  It plants `specs/<ONE_MARK>/phases/phase-1.md`. The first start moves it,
  because the non-mark files sort first and `phases/` comes before
  `spec.md`. Then the first start stops at `spec.md`. After the second
  start, the case asserts three things: `phases/phase-1.md` is at the
  destination, `specs/<ONE_MARK>` does not exist, and the printed line does
  not contain `specs/<ONE_MARK>`. The old assertion that `rounds/` is gone
  is replaced, as `## Removes` names it.
- **S3** is a new case,
  `Test_run_moves::test_accepts_an_item_merged_into_one_that_exists_and_takes_away_specs`.
  It removes and commits `specs/notes`, writes `seal/specs/<ITEM>/spec.md`,
  and runs `run_moves` over `moves()`. It asserts the return is
  `(5, None)`, that `rounds/round-1.md` is at the destination, and that
  neither `specs/<ITEM>` nor `specs/` exists. Its sibling
  `test_accepts_every_unit_and_takes_away_the_emptied_roots` moves the item
  whole, so S3 covers what that case does not: a merge into an existing
  destination.

**The cases were seen red against the unfixed hook** (`executed`).
`bin/test tests/test_root_migrate.py -q -p no:xdist -rf` exited 1, with 4
failed and 69 passed. The four failures were S1, S3 and both rows of S2, and
each failed on the same message, "the item's directory stayed". After the
commit, `bin/test tests/test_root_migrate.py
tests/test_the_root_migrates_itself.py -q -p no:xdist` exited 1, with the same 4 failed and 74 passed. Before the
edit, the same two modules exited 0 with 77 passed.

**Two assertions sit behind another one, and each was seen red on its own**
(`executed`). S2's printed-line assertion and S3's `specs/` assertion come
after an assertion that already fails against the unfixed hook. So the run
above cannot show that either of them fails. `mutation-check` cannot show it
either: it refuses a red baseline ("No baseline: the cases fail against the
file as it is"). Each preceding directory assertion was removed with `Edit`,
and the two cases were run with `-k "resumes_its_item or
merged_into_one_that_exists"`. The run exited 1 with 3 failed. S3 failed on
"specs/ stayed". Both rows of S2 failed on the printed line, which read
`left specs/1788000002-one-mark where it is (no routing.md or rounds/ that
git tracks — not a SpecSeal work item)`. Both assertions were restored with
`Edit`, and `git diff` was empty against `db3670d2` afterwards.

**Q1, measured on one system only** (`executed`, local macOS, Python
3.12.12). A one-off probe made `item/rounds/` and walked `item` bottom-up,
removing a directory where `dirs` and `files` were both empty. It printed
`item/rounds [] []` and then `item ['rounds'] []`, and `item` stayed on
disk. So Python 3.12 lists a directory before it yields its subdirectories,
as 3.15 does, on macOS. The Linux and Windows legs, and CI's macOS legs, are
still the dispatched run's to show. `.github/workflows/test.yml` splits the
macOS legs into 3 shards and the Windows legs into 4 with `pytest-split`.
The four failing cases can land in different shards of one system, so each
system's answer is the union of its shards. `.test_durations` has no entry
for S3 yet, which changes only the shard it lands in.

**No unit was added, so nothing was mutation-tested.** This phase changes
only `tests/test_root_migrate.py`.

**The narrow checks** (`executed`, exit 0 each): `uvx ruff check` and
`uvx ruff format --check` over `tests/test_root_migrate.py`. `test-layout
--check` refused nothing and `--pairs` found no pair. `--check` reported
that `git`, `say` and `under` have no class, which was already true at
`d0c0a4bf`.
