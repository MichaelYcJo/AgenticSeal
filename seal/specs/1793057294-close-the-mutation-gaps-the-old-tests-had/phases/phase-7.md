# 1793057294-close-the-mutation-gaps-the-old-tests-had — phase 7

| Field | Value |
|---|---|
| Phase | 7 |
| Commit | cfdf2e7b |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

Phase 7, the last phase: the rows of #1017 for
`.github/scripts/close_issues_on_release.py`, with `gh_json` removed because
it has no caller and `spec.md` *Removes* names it, which closes c13, then
`.github/scripts/label_merged_on_release_branch.py` and
`.github/scripts/tracker_labels.py`. Follow the method and table shape of
phases 1 to 6, one commit per module that needs one. Then close the work
item: this record, the `changelog.md` fragment, the closing memo
`overview.md`, and phase 7's Status in `plan.md`. The memo gathers every
divergence phases 1 to 6 handed to phase 7, lists for the repository owner
the names no input reaches, and totals the seven phases per outcome. Build on
`questions.md`'s defaults Q1 to Q5.

## The outcomes

17 rows, rebuilt as 16 mutants. 14 rows are killed by a new case, 1 was
already closed, 1 is equivalent, and 1 left the tree. None is a finding.

| Module | Commit | Rows | Mutants | Killed by a new case | Already closed | Equivalent | Left the tree |
|---|---|---|---|---|---|---|---|
| `.github/scripts/close_issues_on_release.py` | 6e7d552b | 12 | 11 | 10 | 1 | 0 | 1 |
| `.github/scripts/label_merged_on_release_branch.py` | d431f2e7 | 3 | 3 | 2 | 0 | 1 | 0 |
| `.github/scripts/tracker_labels.py` | cfdf2e7b | 2 | 2 | 2 | 0 | 0 | 0 |

## How the tables read

The tables read as phase 1's do. Each pair is written as the zsh command line
passed it to `bin/mutation-check --replace`. A `$'...'` string is ANSI-C
quoted, so `\n` in it is a newline and `\'` is a single quote.

The before column is the module's batch with `-x -p no:xdist` in `--tests`,
first against the module's own test file at 619014bd, then, for each
survivor, against every other test file that loads the module. Those files
were found with `git grep -l` over `tests/` for the module's stem, and with
the same search for the scripts that load the module. They are listed above
each table. The label module's batch over other files ran at 6e7d552b, whose
only change to those files is the closer's new cases, and none of them loads
the label module. The after column is the same batch against the module's
own file at the module's commit. Every batch passed its baseline.

A new case was seen red alone on its mutant with
`bin/mutation-check <module> --replace OLD NEW --tests "bin/test tests/test_<stem>.py -q -x -p no:xdist -k <case>"`.
Each of those runs printed `red: the cases failed against the mutation (exit 1)`
and exited 0, so its baseline passed against the code. Each failure was the
case's own assertion, except two. c32's mutant makes `run` exit inside the
case on git's `Invalid revision range`, and c35's raises `TypeError` where
`keywords_in` is handed None.

## `.github/scripts/close_issues_on_release.py`

Records: the issue body's c10 to c36, `phases/phase-6.md:1482` to `:1493` at
`79f9c3fd`. Before: `tests/test_close_issues_on_release.py`, then
`tests/test_a_declared_label_reaches_the_tracker.py tests/test_gather_changelog.py tests/test_issue_claims_check.py tests/test_label_merged_on_release_branch.py tests/test_roll_flow_measurement_issue.py tests/test_the_closer_carries_on_past_a_refusal.py tests/test_tracker_labels.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| c10: `run` does not exit on a failed call | `$'    if out.returncode:\n        sys.exit(f"{\' \'.join(args)} failed'` `$'    if False:\n        sys.exit(f"{\' \'.join(args)} failed'` | SURVIVED, every file | red, `Test_run::test_refuses_a_failed_call_by_exiting_and_naming_what_it_wrote` | killed by a new case |
| c13: `gh_json` answers the text, not its JSON | no mutant | not run | not run | left the tree: 6e7d552b removed `gh_json`, which nothing in the tree called (`spec.md` *Removes*). `git grep -n gh_json -- '*.py'` prints nothing at 6e7d552b |
| c14: `_issue_api` exits on a 404 | `'        if "Not Found" in out.stderr or "404" in out.stderr:'` `'        if False:'` | SURVIVED, every file | red, `Test__issue_api::test_accepts_a_404_as_an_issue_that_does_not_exist` | killed by a new case |
| c15: `issue_state` answers `open` for every issue that exists | `'    return data.get("state") if exists else None'` `'    return "open" if exists else None'` | SURVIVED, every file | red, `Test_issue_state::test_accepts_a_closed_issue_as_closed` | killed by a new case |
| c16: `comments_on` answers 0 where the read gave no count | `'    return count if isinstance(count, int) else None'` `'    return count if isinstance(count, int) else 0'` | SURVIVED, every file | red, `Test_comments_on::test_refuses_a_read_that_gave_no_count_as_none` | killed by a new case |
| c18: `issue_labels` reads a missing issue's data | `$'    if not exists:\n        return [], False'` `$'    if False:\n        return [], False'` | SURVIVED on `tests/test_close_issues_on_release.py`; red on `tests/test_label_merged_on_release_branch.py::Test_main::test_a_claimed_number_that_names_nothing_is_skipped` | SURVIVED on `tests/test_close_issues_on_release.py`; the other file holds its case | already closed |
| c28: `close_issue` takes a count it could not read as 0 | `'    if before is not None and comments_on(repo, number) == before + 1:'` `'    if comments_on(repo, number) == (before or 0) + 1:'` | SURVIVED, every file | red, `Test_close_issue::test_refuses_a_count_it_could_not_read_as_zero_and_posts_the_comment` | killed by a new case |
| c30: `pull_request_body` answers an issue's body as a pull request's | `'    if not exists or data.get("pull_request") is None:'` `'    if not exists:'` | SURVIVED, every file | red, `Test_pull_request_body::test_refuses_an_issues_body_as_a_pull_requests` | killed by a new case |
| c32: `arrived` reads a range from an all-zero `before` | `'    if not before or set(before) == {"0"}:'` `'    if not before:'` | SURVIVED, every file | red, `Test_arrived::test_refuses_an_all_zero_before_as_a_range_and_reads_the_tip` | killed by a new case |
| c33: `arrived` reads the tip, not the range | `'    return run("git", "log", "--format=%s", f"{before}..{after}").splitlines()'` `'    return run("git", "log", "-1", "--format=%s", after).splitlines()'` | SURVIVED, every file | red, `Test_arrived::test_accepts_every_subject_in_the_range` | killed by a new case |
| c35: `main` reads keywords from a number that is no pull request | `'        if body is None:'` `'        if False:'` | SURVIVED, every file | red, `Test_main::test_refuses_a_subject_number_naming_an_issue_and_closes_what_the_pull_request_claims` | killed by a new case |
| c36: the claim lookup names the last pull request to claim an issue, not the first | `'            wanted.setdefault(int(issue), number)'` `'            wanted[int(issue)] = number'` | SURVIVED, every file | red, `Test_main::test_accepts_the_first_pull_request_to_claim_an_issue_as_its_closer` | killed by a new case |

## `.github/scripts/label_merged_on_release_branch.py`

Records: the issue body's m6, m9 and m11, `phases/phase-6.md:1500` to `:1502`
and `:1512` at `79f9c3fd`. Before: `tests/test_label_merged_on_release_branch.py`,
then
`tests/test_a_declared_label_reaches_the_tracker.py tests/test_a_merged_ticket_says_so_on_the_tracker.py tests/test_close_issues_on_release.py tests/test_publish_release_note.py tests/test_tracker_labels.py tests/test_release_completeness_check.py tests/test_a_release_cannot_ship_an_untrue_milestone.py tests/test_a_release_publishes_its_note.py tests/test_gather_changelog.py tests/test_release_seal.py`.
`tracker_labels.py`, `release_completeness_check.py` and
`publish_release_note.py` load the module, so the files that reach those
scripts are among them.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| m6: `LABEL_DESCRIPTION_LIMIT` is 1000 | `'LABEL_DESCRIPTION_LIMIT = 100'` `'LABEL_DESCRIPTION_LIMIT = 1000'` | SURVIVED, every file | SURVIVED | equivalent: no function of this module or of `tracker_labels.py` reads the constant. The description cases of `tests/test_label_merged_on_release_branch.py` and `tests/test_tracker_labels.py` read it as their ruler, so a raised cap changes nothing either script sends. Review round 1 removed the case d431f2e7 added for it, which pinned the number |
| m9: the label list is read 30 at a time | `'"--repo", repo, "--limit", "1000", "--json", "name"'` `'"--repo", repo, "--json", "name"'` | SURVIVED, every file | red, `Test_existing_labels::test_accepts_every_label_of_a_tracker_past_thirty` | killed by a new case |
| m11: the label is created in another colour | `'        "0E8A16",'` `'        "FFFFFF",'` | SURVIVED, every file | red, `Test_create_label::test_accepts_the_label_in_the_green_a_hand_made_one_carries` | killed by a new case |

## `.github/scripts/tracker_labels.py`

Records: the issue body's t4 and t6, `phases/phase-6.md:1509`, `:1510` and
`:1512` at `79f9c3fd`. Before: `tests/test_tracker_labels.py`, then
`tests/test_a_declared_label_reaches_the_tracker.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| t4: the label is created in another colour | `'        label["color"],'` `'        "FFFFFF",'` | SURVIVED, every file | red, `Test_create::test_accepts_the_declared_label_in_its_declared_colour` | killed by a new case |
| t6: `DRY_RUN` creates | `'        if args.check or dry:'` `'        if args.check:'` | SURVIVED, every file | red, `Test_main::test_refuses_to_write_under_a_dry_run_of_apply` | killed by a new case |

## What this phase found

**c13 left the tree in this phase's own commit.** 6e7d552b removes `gh_json`
and adds the module's cases, so the module still lands in one commit.
`_issue_api` makes the module's `gh api` reads, and the module's `json`
import stays for it. This is the one change to shipped code in the work
item: of the commits on the branch's first parent since 134d7203, only
6e7d552b touches a file outside `tests/` and `seal/` (`executed`,
`git log --first-parent --no-merges`).

**c18 was red already, on the sibling's file.** The label script's case for a
claimed number that names nothing reads that issue through the closer's
`issue_labels`, and under the mutant `None.get` raises. No case was added for
it. The closer's own file still lets it survive, which is why its after batch
prints one `SURVIVED` and exits 1.

**c35 is one reading of a row with no pair (Q1).** The record's sentence says
`main` reads keywords from a number that is no pull request. The real
`pull_request_body` answers None for such a number, so `main` can read no
issue's body. The pair drops the test that steps over the None, and
`keywords_in(None)` then raises. The case asserts the behaviour the caller
needs: the issue number is skipped, and the pull request's claim still
closes. Any other reading of the row that lets the None through meets the
same case.

**c16's case reads `comments_on` directly, and c28's reads `close_issue`.**
The record names the two rows in one breath: a count unreadable before the
first route and readable after it. c28's case fakes `comments_on` to answer
None and then 1, so it cannot see c16, whose mutant sits inside
`comments_on`. Each mutant has the case of the function it changes
(`spec.md` *In* item 2).

**`arrived`'s cases run real git.** `Test_arrived` builds a scratch
repository of three commits with `conftest.git_repo` and
`commit_everything`, and moves the working directory into it, since `run`
calls git there. Under c32's mutant git refuses the range from the zero SHA,
and `run` exits.

**m9's case fakes `gh label list` as gh answers it.** `PagedTracker` returns at
most `--limit` names, and 30 where the call names no limit, which is the
default `gh label list --help` prints (`executed`, the help text of the gh
installed here). The case does not remove a guarantee to see a defence
refuse (contract rule 13). It reproduces the platform's own default, which
is the condition the `--limit 1000` is written against.

**m6 is equivalent, because no shipped code reads the cap.**
`LABEL_DESCRIPTION_LIMIT` is read by no function of its module or of
`tracker_labels.py`, whose comment names it. The two description cases, one
here and one in `tests/test_tracker_labels.py`, read it as their ruler. So
the decision the mutant changes is made only inside the suite, and no input
to a shipped function tells 100 from 1000 (`executed`,
`git grep -n LABEL_DESCRIPTION_LIMIT`). d431f2e7 added a case pinning the
value at 100. Review round 1 removed it: it wrote GitHub's cap a second time,
beside the one source `tests/test_tracker_labels.py` reads, and pinned code
no caller reaches. The name is listed in `overview.md` *Names no input
reaches*.

**m11's and t4's cases pin a colour value.** The comment above
`create_label`'s colour says why it is `0E8A16`, and `tracker_labels.py`'s
declaration says why `size: now`'s colour is its own. Each case reads the
colour the module states as its decision, not an incidental string.

**Each new function class holds both kinds of case.** `Test_run`,
`Test__issue_api`, `Test_issue_state`, `Test_comments_on`,
`Test_close_issue`, `Test_pull_request_body`, `Test_arrived`,
`Test_existing_labels`, `Test_create_label` and `Test_create` are new, and
`bin/test-layout --check` asks each for an accepts case and a refuses case.
In some classes the killing case is the accepts one: c14, c15, c33, c36, m9,
m11 and t4.

**`bin/test-layout --pairs` names six pairs over the three files, and they
stay.** Five are this phase's. `Test_comments_on`'s two cases and
`Test_existing_labels`' two call their function with the same repository
and number, and `Test_close_issue`'s two call `close_issue` with the same
arguments. In each, the two cases differ in what the faked reader answers,
which the normalisation does not see, and each holds a branch the other does
not. `Test_main` of `tests/test_tracker_labels.py` has three pairs among its
`main(["--apply"])` cases: one #942 named and kept, and two with t6's case,
which alone runs under `DRY_RUN`. `--pairs` is a report and exits 0.

**No case fakes a guarantee the platform gives.** `Test_run` calls the real
`run` on this interpreter, which each CI leg has. `Test__issue_api` replaces
`gh` with one answer and runs the real `_issue_api`. `Test_arrived` runs
real git, and its subjects come back through git's own `%s` on every leg.

**The spawn's coordinate for the memo's shape did not open.** It named
`seal/specs/1792628098-agent-lifetime-and-process-archive/` at 5daa931f, and
no such directory stands there. The directory with that slug is
`1793057292-agent-lifetime-and-process-archive`, and the memo and the
fragment are shaped on its `overview.md` and `changelog.md` (`executed`,
`git ls-tree` at 5daa931f).

**Q5 is the orchestrator's.** This phase adds 24 cases, none of them priced
in `.test_durations`. At cfdf2e7b the work item's own changes add 171 lines
holding `def test_` and remove none (`executed`,
`git diff 5daa931f...cfdf2e7b -- tests`). `git diff 134d7203 cfdf2e7b`
counts 184, because it also holds the 13 the merge of `release/v0.22.4` at
95fa9fb7 brought. Review round 1 later removed m6's case and k3's, so 169
stand at the head (`overview.md` *Not verified*).

**Run for the phase** (`executed`, at cfdf2e7b):
`bin/test tests/test_close_issues_on_release.py tests/test_label_merged_on_release_branch.py tests/test_tracker_labels.py -q`
exited 0, 82 passed. `bin/test-layout --check` over the three files reads 3
files with 0 refused, and `--pairs` prints the six pairs named above.
`uvx ruff check` and `uvx ruff format --check` over the three test files and
`.github/scripts/close_issues_on_release.py` exit 0.
`git grep -n gh_json -- '*.py'` prints nothing, and
`git diff 134d7203 HEAD -- tests` removes no line holding `def test_`.

## The pull request's CI found three cases reading the run's branch

**The failure.** The `tests` run 40446828473 is the first run of the
`pull_request` event on #1057, at 88c27ed5. Three cases phase 5 added failed
on each leg whose shard held them, ubuntu, macOS group 1 and Windows group 1:
`Test_declared_for_this_branch::test_accepts_the_one_routing_md_under_the_work_items_beside_a_decoy`,
under both parameters, and
`Test_declared_for_this_branch::test_refuses_two_committed_declarations_naming_the_branch`
(`read`, the orchestrator's `gh run view 40446828473 --log-failed`; the event
and head are `executed`, `gh run view 40446828473 --json event,headSha`).

**The cause.** The three cases call `chain.declared_for_this_branch` in
process. That function reads the branch from `GITHUB_HEAD_REF` before the
checked-out branch (`skills/code-review/scripts/chain_check.py:2005`). A
`pull_request` run sets `GITHUB_HEAD_REF` to the pull request's branch, so the
cases judged `test/1017-close-the-mutation-gaps-the-old-tests-had` rather than
the fixture's `feature`. Every earlier run had no such variable: the local
runs, and run 40444267960 at bf2096ba, whose event is `workflow_dispatch`
(`executed`, `gh run view 40444267960 --json event`). The file's other cases
already clear the variable, through `run_check`'s environment or
`monkeypatch.delenv`.

**The fix.** 516d0ff6 clears the variable in each of the three cases with
`monkeypatch.delenv("GITHUB_HEAD_REF", raising=False)`, after the fixture's
commit and before the call. With `GITHUB_HEAD_REF=some-other-branch` set,
`bin/test tests/test_chain_check.py -q -p no:xdist -k Test_declared_for_this_branch`
printed 3 failed and 6 passed at 88c27ed5, and 9 passed at 516d0ff6
(`executed`).

**The sweep over the work item's other cases.** Each of the 32 test files that
`git diff --name-only 5daa931f...HEAD -- tests` lists ran on its own, under
`GITHUB_HEAD_REF`, `GITHUB_BASE_REF`, `GITHUB_EVENT_NAME=pull_request`,
`GITHUB_REF`, `GITHUB_ACTIONS=true` and `CI=true`, each set to a value no
fixture uses. Every file exited 0 at 516d0ff6. The one skip, in
`tests/test_broad_gate.py`, is the case that needs `cmd.exe`, and it skips
without the variables too (`executed`). No other case read the run's
environment.
