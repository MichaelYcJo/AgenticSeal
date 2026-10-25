# Phase 3: 1792935671-the-routing-check-moves-to-the-sessions-tools

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 516274e7 |

## What this phase was asked

Build phase 3 of `plan.md` *Phases*: the pull request. Add the trailer arm and the guarantee's `original:` arm to `skills/code-review/scripts/chain_check.py`, under markers `routing-trailer-at-the-pull-request` and `parity-in-the-guarantee`. State the trailer's convention in `skills/commit-pr-convention/SKILL.md`, the comparison duty in `agents/sealer.md`, and the line in `templates/sdd-guarantee.md`. Nothing is removed. Verify with `tests/test_chain_check.py` (S10 to S12), and show that a pull request with no `SpecSeal-Routing` trailer passes every step `templates/hygiene.yml` runs. Build `questions.md` Q1's default (a): the sealer compares and writes the line. Each new case is seen red first. The broad gate is the orchestrator's.

## What this phase found

**The frame holds for this phase, with one reading of *its own commits*.** `chain_check.py#main` returned 0 with a notice where no declaration was judged, at the `if not declarations` return, as *Technical context* says. The trailer arm now runs before that return. The frame says the arm reads the pull request's own commits with merges left out. A release pull request into `main` carries other pull requests' squash commits, and a squash body can hold the trailers of the commits it squashed. Read literally, those trailers would name work items whose declarations the check does not judge, so every release pull request would fail. The arm therefore leaves out a squash GitHub committed, by the rule `carried_by` already applies to a declaration: committer `noreply@github.com`, subject ending `(#N)`. That pull request judged its own trailers. A case pins it beside the merge case.

**How the trailer is read.** `routing_trailers` runs `git log --no-merges --reverse -z` over `<base>..HEAD` with `%(trailers:key=SpecSeal-Routing,valueonly,separator=%x1e)`, so git's parser decides what a trailer is. A value naming a work item is compared with the directory names of the declarations the check judges. `no work item` is printed as a notice. A commit with no trailer is not read. Where git cannot list the commits, the check exits 2 and says so on stderr.

**The guarantee arm reuses the round record's rule.** `originals_of` takes the work items declared `straight to the PR` beside the chained ones and reads each one's `guarantee.md` with `original_of`, the same prefix rule, under its own message, `NO_GUARANTEE_ORIGINAL`. A guarantee git does not carry is left to the guarantee arm, so it is named once. Under `--sealing` the missing line is a notice, as every other guarantee check is, because the sealer writes it after that run.

**Text that stood on the old fact, corrected in the same commit.** `templates/hygiene.yml` and `.github/workflows/hygiene.yml` said the chain step never fails a pull request that declared nothing. Both now say it fails such a pull request only for a commit whose trailer names a work item. The template's list also names the guarantee's `original:` line. `chain_check.py`'s module docstring lists the trailer arm and the guarantee's line. Found with `git grep` on the sentence's words, executed.

**The template line.** `templates/sdd-guarantee.md` gains one line under the first table: `original:` with a placeholder that says when step 5 owes it and to delete it otherwise. `agents/sealer.md` step 5 states the duty: where git carries `seal/parity.md`, the declaration answers `straight to the PR` and the diff changes a path outside `docs/` and `seal/`, the sealer compares through `skills/legacy-parity/SKILL.md` and writes the line, or withholds where it cannot compare. The step number stays 5, because the template cites `agents/sealer.md` step 5 for the verdict shapes.

**This branch's own commits carry the trailer from this phase on**, naming this work item, so the arm judges them at this pull request.

**A pull request with no trailer, read.** The only `templates/hygiene.yml` step whose code this phase changed is the chain step. `test_a_teammates_commit_is_never_judged` runs it over a pull request whose commit carries the harness's co-author trailer and no `SpecSeal-Routing`, and the check exits 0. The other steps run code this phase did not touch.

**How each new case was seen red, executed before the code.** Against the old `chain_check.py`, `test_refuses_a_commit_naming_a_work_item_no_declaration_names` exited 0 where 1 was expected, `test_refuses_to_run_where_the_commits_cannot_be_read` failed on the missing `routing_trailers`, and `test_refuses_a_direct_guarantee_with_no_original_line_and_accepts_one` failed on the missing `NO_GUARANTEE_ORIGINAL`. The cases whose expected answer is a pass also pass against the old code, so each was shown red by a mutant below. `test_a_missing_guarantee_is_named_once` was added after the mutation run found the guard it pins unpinned.

**`mutation-check`, executed after the commits.** 10 mutants of `chain_check.py` against `tests/test_chain_check.py -k 'routing_trailers or originals_of'`: the squash exclusion off, `--no-merges` dropped, every trailer value read as undeclared, the `no work item` branch off, the undeclared pull request's exit forced to 0, the unreadable-commits exit off, the guarantee read with the round record's message, `straight to the PR` items not collected, the `--sealing` notice off, and the missing-guarantee guard off. Nine went red. The guard survived. The new case was committed, and a second run showed that mutant red. `git status --short` was clean after each run.

**Tests, executed.** `tests/test_chain_check.py`: 251 passed. The 33 modules that name `templates/sdd-guarantee.md`, `agents/sealer.md`, `skills/commit-pr-convention/SKILL.md` or `hygiene.yml`: 1,903 passed, 9 skipped, and 1 failed, `test_every_spec_directory_that_reached_the_ladder_has_an_overview`, which phase 2's record explains. `test-layout --check` and `--pairs` over `tests/test_chain_check.py`: 0 refused, 0 pairs.
