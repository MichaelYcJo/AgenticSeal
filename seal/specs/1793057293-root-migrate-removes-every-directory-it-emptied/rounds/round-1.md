# Review round 1: 1793057293-root-migrate-removes-every-directory-it-emptied

target: d3f6aaf7 against release/v0.22.4

Round 1 has no earlier record, so nothing is carried. Every fact below was
established this round, in a `git clone --no-local` of the branch at
`d3f6aaf7`, against the fork point `fa7d1374`. No `seal/parity.md` is
declared, so no parity comparison applies.

## Findings

### 1. The new `Test_run_moves` case for a merged item covers nothing the module's other cases do not already cover

severity: should
location: `tests/test_root_migrate.py:497-508`
evidence: executed `bin/mutation-check hooks/root-migrate.py --replace "                os.rmdir(here)" "                pass" --replace "if not os.listdir(here):" "if not os.listdir(here) and here != under(root, src):" --replace "    for old in (OLD_HOME, OLD_ITEMS):" "    for old in (OLD_HOME,):" --replace "topdown=False" "topdown=True" --replace "if not os.listdir(here):" "if True:" --tests "bin/test tests/test_root_migrate.py -q -p no:xdist -x -k 'not merged_into_one_that_exists'"`, `bin/test-layout --pairs tests/test_root_migrate.py`
verdict: open

`Test_run_moves::test_accepts_an_item_merged_into_one_that_exists_and_takes_away_specs`
(the frame's S3) asserts two things after a merge: the item's directory is
gone, and `specs/` is gone. Each is already held by another case of the
module. S1 (`Test_move::test_accepts_a_directory_whole_or_file_by_file_into_one_that_exists`,
line 413) calls `move` on the same merge shape and asserts that
`specs/<ITEM>` does not exist. The sibling
`test_accepts_every_unit_and_takes_away_the_emptied_roots` (line 491) asserts
that `run_moves` removes an emptied `specs/`. That removal is one `os.rmdir`
in `run_moves` (`hooks/root-migrate.py:433-445`), and it does not depend on
how the item left. So S3's only new reach is the composition of the two.
No code joins them beyond the order of two calls.

The mutation run shows it. Five mutants were run against the module with S3
left out. They covered the walk's removal, the test that keeps `src`, the
`specs/` cleanup in `run_moves`, the walk's direction, and the fresh
listing. All five went red. `test-layout --pairs` names no pair, so no
duplicate check flags the case either. It is a case the suite pays for on
every run and has to keep in step, and nothing fails without it.

The frame names S3, so removing it is a divergence for `overview.md`. The
other way to close this is to name a defect that S3 alone catches, in the
answer. This round found none.

```diff
--- a/tests/test_root_migrate.py
+++ b/tests/test_root_migrate.py
@@ class Test_run_moves:
-    def test_accepts_an_item_merged_into_one_that_exists_and_takes_away_specs(
-        self, hook, proj
-    ):
-        """#1018: the item is merged file by file, its directory goes with
-        the files, and `specs/` is then empty and goes too."""
-        git(proj, "rm", "-rq", "specs/notes")
-        commit(proj, "only SpecSeal's work items under specs/")
-        write(proj, f"seal/specs/{ITEM}/spec.md", "# already here\n")
-        assert hook.run_moves(str(proj), hook.moves(str(proj))) == (5, None)
-        assert (proj / "seal" / "specs" / ITEM / "rounds" / "round-1.md").is_file()
-        assert not (proj / "specs" / ITEM).exists(), "the item's directory stayed"
-        assert not (proj / "specs").exists(), "specs/ stayed"
-
```

A row goes into `overview.md` *Where spec and implementation diverged*. It
says that S3's scenario is held by S1 together with
`test_accepts_every_unit_and_takes_away_the_emptied_roots`, and that the
mutation run above found no defect only S3 catches. The case has no
`.test_durations` entry, so nothing there changes.

answer:

## Confirmations

confirms: none
The fix removes only a directory that holds nothing, and only under `src`.
At `hooks/root-migrate.py:397-402`, each directory is listed again with
`os.listdir`, and `os.rmdir` runs only on an empty listing. One `try` passes
over an `OSError` from either call. The walk starts at `src`, and
`run_moves` calls `move` once per unit. So a team's directory under `specs/`
is never walked, and `run_moves`'s single `os.rmdir` of `specs/` is
unchanged. The probe built a merge with three branches: one emptied leaf,
one emptied branch three levels deep, and one branch two levels deep that
holds an ignored `.DS_Store`. It also held a directory that was empty before
the run. Only the item's directory, the ignored file's two directories and
the file stayed. S4 holds this without the platform's refusal (contract rule
13). Under `if True:` in place of the fresh listing, the module went red,
and S4 is the only case that patches `rmdir` inside `move`. Executed.

confirms: none
Both shapes the issues name are pinned and fixed. S1 is #1018's merge, at
depth two. S2 is #1016's resumed move, on both mark rows: a directory the
stopped first run emptied is removed by the run that finishes the item. Run
40421812732 at `07638965` failed exactly S1, S3 and both S2 rows on ubuntu,
macOS and Windows, three times each. The one other failure was the
`overview.md` check that phase 2 answered. Run 40423069012 at `d3f6aaf7`
completed with success on every leg, the four Windows groups among them.
Locally, `tests/test_root_migrate.py` and
`tests/test_the_root_migrates_itself.py` gave 79 passed. #1016 asks that
an emptied `specs/` go too in the resumed shape. S2's fixture keeps
`specs/notes`, so S2 cannot show it. It is the same `run_moves` cleanup that
the sibling case pins. Executed.

confirms: none
The smith's divergence on the limit sentence holds. The frame says "git
checks out neither" a directory link nor a junction (`spec.md:58-60`,
`plan.md:58-63`, `questions.md:41-44`). That is false for a link. The probe
committed a link to a directory under the item, and `git ls-files -s` listed
it with mode `120000`. A merge then moved it with `git mv`, and its target's
empty subdirectory stayed. An ignored, untracked link to a directory under
`src` was not entered. The link stayed, its parent stayed because its fresh
listing names the link, and the target's empty subdirectory stayed. The
bottom-up branch of Python 3.12.12's `os.walk` excludes "symlinks to
directories if followlinks is False", through `entry.is_symlink()`. So the
docstring's junction-only limit at `hooks/root-migrate.py:362-364` is the
true one. The frame's three sentences still say the old thing. They are the
frame's, and `overview.md:17` records the divergence. Executed, and read in
the interpreter's `os.py`.

confirms: none
`main`'s line no longer names a moved item. S2 asserts that the second
start's line does not hold `specs/<ONE_MARK>`. Phase 1's account quotes the
line it held before the fix: "left specs/1788000002-one-mark where it is (no
routing.md or rounds/ that git tracks — not a SpecSeal work item)". The
probe confirmed `questions.md` Q2's premise: when an ignored file keeps the
item's directory, the line still names it that way. Q2 is open with default
(a), a person's question for the pull request. Executed.

confirms: none
No other text states the old behaviour. `git grep` for the old docstring
sentence, "stays on disk empty", "on disk, empty", "left on disk", "git
checks out neither" and "junction" found the new docstring and the frame.
The other hits were #942's records and unrelated test strings. #942's
records are that work item's history. `README.md`'s by-hand `rmdir` line is
about `git mv`, and it stays true. The test comment the frame's `## Removes`
names is gone. Executed.

confirms: none
Phase 2's mutation claims hold in substance. The round's own batch of five
mutants over the walk and the cleanup was red throughout, with S3 left out.
The account says S4 passed against the unfixed walk. That follows from
reading `os.walk`: the stale listing of `rounds/` already names
`.DS_Store`. Executed and read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Windows, on a directory another process holds open. With a sharing violation, `os.rmdir` raises, and the probe simulated that: the directory and every one above it stayed, nothing raised, and `main` named the moved item "not a SpecSeal work item" again. With delete-pending semantics, the child may still be listed when the parent is reached. Then the parent stays, and the docstring's "is removed" does not hold for it. Neither was run on Windows. The fail direction is to keep, never to remove | `hooks/root-migrate.py:356-364`, `hooks/root-migrate.py:397-402` | the repository owner, at the pull request: whether this edge gets a limit sentence beside the junction's |
| The junction limit itself: that `DirEntry.is_symlink()` is false for a junction, so the walk enters it. Read in the interpreter's source on macOS, never run on Windows. An ignored junction is also the only one that gets past the `dirty` check, because git reports an untracked link | `hooks/root-migrate.py:362-364`, `overview.md:24` | the repository owner, as `overview.md` *Not verified* names |
| The full suite, the repository-wide lint and the typecheck at this head. This round ran none of the three. CI's run 40423069012 is not the broad gate | `broad-gate.md` | the orchestrator, by `broad-gate` once the rounds settle |
| `questions.md` Q2, the line for a moved item's directory that an ignored file keeps | `questions.md` Q2 | a person, at the pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_root_migrate.py tests/test_the_root_migrates_itself.py -q -p no:xdist` | exit 0, 79 passed |
| `bin/test tests/test_tmp_round1_probe.py -q -p no:xdist -s`, four cases: a deep merge with one ignored branch, an ignored directory link under `src`, a tracked directory link under `src`, and `main`'s line with an ignored file and with `rmdir` raising a sharing violation on `phases/` | exit 1. The first case failed only on the probe's own path base: its printed listing was the item's directory, `e`, `e/f` and `e/f/.DS_Store`, which is the expected set. The other three passed. The ignored link stayed with its target's empty directory. The tracked link was `120000`, moved, and its target's empty directory stayed. Both `main` lines read "left specs/1788000000-a-work-item where it is (no routing.md or rounds/ that git tracks — not a SpecSeal work item)", and the held case left `phases` on disk. File deleted |
| `bin/mutation-check hooks/root-migrate.py`, five mutants as finding 1's `evidence:` line gives, against the module with S3 left out | exit 0, "5 mutants, 5 red, 0 SURVIVED, 0 with no verdict"; the clone clean afterwards |
| `bin/test-layout --pairs tests/test_root_migrate.py` | exit 0, 1 file read, 0 pairs |
| `gh run view 40421812732 --log-failed`, the failed case names counted | S1, S3 and both S2 rows, 3 each; `test_every_spec_directory_that_reached_the_ladder_has_an_overview`, 3 |
| `gh run view 40423069012 --json status,conclusion,headSha,jobs` | completed, success, head `d3f6aaf7`; every pytest leg success, the four Windows groups among them |
