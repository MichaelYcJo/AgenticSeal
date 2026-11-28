# Phase 1: 1795841828-settle-only-release-note

## What this phase found

**The frame holds.** Its coordinates were opened at the frame commit `c0cabec2`, whose code is the code at `3729b409` (`git diff --stat 3729b409 c0cabec2` lists the three frame files alone). The coordinates are `publish_release_note.py#main`'s refusal at lines 867 to 875, `merged_pulls` at lines 477 to 521, `chain_check.py#settled` at line 2117 with its `git` helper, which returns None where git exits non-zero, `wire` at lines 163 to 195 of the test module, and the workflow header at lines 17 to 21. Each stood where the frame says. Judged against `skills/implement/SKILL.md` *The frame is judged before it is built to*.

**The commit list is read with `git log --no-merges --reverse --format=%H %h %s`, in place of the `git rev-list --no-merges` that `frame/design.md` *Scope* item 1 names.** Both list the same commits. The log also gives the short hash and the subject that *Scope* item 3's refusal names, in one read, and `--reverse` names them oldest first. Judged against *Scope* items 1 and 3.

**A commit's deleted paths are read with the one-commit form `git diff-tree --no-commit-id -r -z --no-renames --diff-filter=D --name-only <commit>`, in place of the `<c>^ <c>` pair of G9.** For a commit other than a merge the two compare the same trees. The one-commit form prints nothing for a root commit, where `<c>^` names no commit and would stop the run. A range with no previous tag holds the root commit. That commit deletes nothing, so it is no settle and the range goes to the refusal. Judged against *Scope* items 1 and 3.

**The release pull request is read after `release_exists` and before the title, the theme and `merged_pulls`.** *Scope* item 2 asks that `release_exists` still run first. Reading the body next stops a run that cannot build its note before the other reads are spent. The `settles alone` case of `test_an_existing_release_is_left_exactly_as_it_is` holds the order. Judged against *Scope* items 2 and 4.

**The `settles` stub of `wire` answers `(False, ())` unless a case says otherwise.** So the existing A3 case is now the `no commit but merges` parameter. It still prints the existing refusal line, unchanged. Judged against *Scope* item 3 and `frame/design.md` *Data & interfaces*.

**`release_body`'s docstring says that a release pull request's body is not escaped, beside the sentence that a fragment is not.** `frame/plan.md` *Alternatives considered* row A9 found no reader that refuses an unbalanced `details` tag in that body. The docstring now says who reads it instead: the owner, before the release merges.

**Each new case was seen red against the script before the build.** The test module with the new cases was run against the script at `c0cabec2`. For that run, `wire` set the two new stubs with `raising=False`, because the attributes did not exist yet, and the line was put back before the commit. The command `uv run --no-project tests/run_tests.py -q tests/github/test_publish_release_note.py -p no:xdist` printed `12 failed, 71 passed`. Each failing line is the guard its case names:

- the S1 case failed on `assert 1 == 0`, from `main`;
- the S2 parameter failed on `assert 'abc1234 fix: a change is no settle' in ...`;
- the S4 case of `main` failed on the line `release_pull_body` gave, which the output lacked;
- the `settles alone` parameter of A2 failed on `main`'s exit 1;
- the S3 case, the six `Test_release_pull_body` cases and the git-failure assertion failed on `AttributeError`, where `settles` and `release_pull_body` did not exist.

Two assertions say that something is not asked, and the run before the build could not show them red. Each was shown red by a mutant that removes only its guard, below.

**Each unit that adds behaviour was mutated after the build commit `9b13038b`, one `bin/agentic mutate` command per unit.**

- `settles`, with the cases `-k 'settle_is_a_commit or git_read_that_fails'`: `6 mutants, 5 red, 1 SURVIVED`. The red mutants were these: `held` left False, the tree check of a gone directory removed, the directory pattern not bound to `agentory/threads/`, `--no-merges` removed, and `--reverse` removed. The survivor replaced `chain_check.settled(ROOT, f"{commit}^", gone)` with `gone`. It is equivalent wherever git answers. Each directory in `gone` lost a path in the commit, so the directory held that path at the parent, and `settled` keeps every such directory. The two differ only where `settled`'s own git read fails, and there `settled` reads the commit as no settle. The call stays because `frame/design.md` G2 and *Data & interfaces* name `chain_check.py#settled` as the one predicate that reads a settle.
- `release_pull_body`, with `-k Test_release_pull_body`: `7 mutants, 7 red, 0 SURVIVED`. The mutants were the merge commit compared with `!=`, the empty-body guard removed, `--base main` changed, `--head release/v<version>` changed, the exit-code guard removed, the body's strip removed, and `mergeCommit` left out of `--json`.
- `main`, with `-k Test_main`: `7 mutants, 7 red, 0 SURVIVED`. The mutants were these: `settles` asked for a range that added a fragment, the `not commits` arm removed, the `unsettled` arm removed, the naming loop emptied, the `rendered is None` guard removed, the line naming the body's source removed, and `section` taken whatever the range held.
- Two mutants of `main` were also run alone, to read each failing line. The first asked `settles` for a range that added a fragment, and it turned A1's absence assertion red: `AssertionError: [('settles', 'v1.2.2..v1.2.3')]`. The second read the release pull request before `release_exists`, and it turned the `settles alone` parameter of A2 red: `AssertionError: the release pull request was read for a release that already exists`.

**S6 of `frame/design.md`, executed.** It ran in a `git clone --no-local` of this worktree, checked out at `9b13038b`, under the crafter's scratch directory. The command was `DRY_RUN=1 TAG=v0.40.1 REPO=MichaelYcJo/AgenticSeal python3 .github/scripts/publish_release_note.py`. It exited 0 and printed:

```
DRY_RUN — nothing will be written
no commit after v0.40.0 up to v0.40.1 added a changelog fragment that v0.40.0 does not already hold, and each commit other than a merge is a settle, so the note carries the release pull request's body
a release already exists at v0.40.1 — leaving it. Nothing here overwrites a note, because one may have been edited by hand after it was published
```

At G8 the same command exited 1 with the refusal.

**A probe in the same clone asked the two readers of the real history, executed once.** `release_pull_body("MichaelYcJo/AgenticSeal", "0.40.1", "v0.40.1")` returned a body of 2719 characters and `the body of the release pull request #1664`. `settles("v0.39.3..v0.39.4")` returned `(True, [('235d41ff', 'chore: settle 0.37.1 to 0.39.3: ...')])`, which is G9's reading of the settle under the old root name. `settles("v0.39.4..v0.40.0")` returned two commits that are no settle. These agree with G9 and G12.

**Two checks of the tree shaped the text.** The `splitlines` census of `test_census` refused the commit list's `.splitlines(`. The list is git's log, one commit to a line, so the call carries the census's `# exempt from splitlines:` line above it. The first phase-boundary run also failed `tests/text/test_a_cited_commit_outlives_the_squash.py`. The new cases' docstrings had cited `3729b409`, a commit of this branch that the squash removes. The commit `07f3bb14` rewrites each to say "the script before #1655". That run failed two more cases on one fact, that the work item had no `gaps.md`: `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview` and `tests/behaviour/test_this_repository_passes_its_own_checks.py::Test_agentic_unverified::test_this_repositorys_own_overviews_are_all_readable`. This phase's records commit writes `gaps.md`.

**The phase-boundary set** is the plan row's files, each other test file that names a changed path, and the tree-wide files of `CONTRIBUTING.md` *The test layout*. The other test file is `tests/lib/test_console.py`. The tree-wide files hold `tests/behaviour/test_a_release_publishes_its_note.py` and `tests/behaviour/test_a_cited_section_stands_in_its_file.py`. The command is `uv run --no-project tests/run_tests.py -q tests/github/test_publish_release_note.py tests/github/test_release_mark.py tests/skills/test_settle.py tests/lib/test_console.py tests/text tests/behaviour`.
