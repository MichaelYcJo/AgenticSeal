# Phase 2: 1795849901-number-read-at-cut

## What this phase found

**The frame holds for this phase, with the three departures below.** Its
coordinates were opened at `1a6e790d`, the HEAD the phase began at.
`publish_release_note.py`'s `release_pull_body`, `milestone_description`,
`theme_of`, `merged_pulls` and `main`, `previous_tag`, and
`release_mark.py`'s call of `merged_pulls` at line 530 each stood where
`frame/plan.md` *Technical context* says, the first five a line above the
number it gives. That line is the one phase 1's rewrap of the comment above
`TAG_RE` took out, so it is no contradiction of a coordinate dated to
`9d7a8fe2`. The phase 2 search of the *Verified by* cell printed 20 lines
opening `<` and none opening `>` at `1a6e790d`, as `frame/design.md` G16
says. Judged against `skills/implement/SKILL.md` *The frame is judged
before it is built to*.

**Q1 is decided: `merged_pulls` asks `gh pr view` once for each pull
request the range names.** The set is the numbers `lib/closing.py#MERGED_PR`
reads at the end of each subject of `git log --format=%s <range>`, each
once, in number order. Each number is asked with
`gh pr view <N> --repo <repo> --json number,title,author,body,labels,headRefName`.
The grounds are four. `gh pr view --json` gives the fields
`gh pr list --json` gives, in the same shape: both printed
`author.{id,is_bot,login,name}`, `labels` and `headRefName` for #1667 and
#1668 on 2026-11-28 (executed, with a person's token). So the mark's
`chain_counts`, which reads `labels` and `headRefName`, reads the set as
before. A call per number has no limit, where one list call has a limit a
long release can pass. Each call is the same GraphQL read of a pull request
that the publish workflow's token already makes with `gh pr list`. And a
release carries a handful of pull requests, so the cost is a handful of
calls in a job that runs once a release. Any call that fails, gives no
answer or prints no JSON makes the whole set None, as Q1's default asks:
the note then goes out with no summary, and the log names the number. A set
short of one pull request would be worse, since the header and the mark
would count it wrong. Judged against `frame/questions.md` Q1 and
`skills/core/SKILL.md` *The first value: efficient development through the
IADD process*, where a script answers what it reads exactly.

**`release_pull_body` lists the pull requests merged into `main`, with no
head name, and keeps the one whose merge commit is the tag.** The call is
`gh pr list --base main --state merged --limit 100 --json number,body,mergeCommit`.
The limit is `RELEASE_PULLS_LISTED`. `gh` lists them newest first: the
same list with `--limit 3` printed #1669, #1664 and #1661, in that order
(executed, 2026-11-28). The tag is pushed at its release's merge, so its
release pull request is the newest. A tag pushed by hand for a release more than that many release pull
requests back finds none, and says so. A second shape was measured and not
taken: `gh api repos/<repo>/commits/<sha>/pulls` returned #1664 for
`v0.40.1^{commit}`, #1669 for `v0.41.0`, #1653 for `v0.39.4` and #1544 for
`v0.38.0` (executed, 2026-11-28, a person's token). It needs no bound, but
under the publish workflow's `permissions: contents: write` alone it is a
REST read of pull requests that no step of that workflow makes today, and
no run here can measure it. The list keeps the read the token is known to
answer. Judged against *Scope* item 5 and `frame/design.md` G10.

**The theme comes from that same read, and only after `release_exists`.**
`main` calls `release_pull_body` once, after the guard that leaves an
existing release alone, so A2's case still reads no pull request for a
release already there. For a note of fragments, the body's first sentence
is the theme, and a body that cannot be read leaves no theme line, with the
log naming why. For a range of settles alone, a body that cannot be read
fails the run as before, and a body that is read stands whole in the fold
with no theme line above it. The log says why. `theme_of` keeps its
sentence rule and drops the `Purpose:` label, so a body opening with that
word keeps it. The release pull requests #1669, #1664, #1653 and #1544
each open with a sentence (executed, the read above), so the first
sentence is a theme there. Judged against *Scope* item 5.

**A `(#N)` written by hand that names an issue now drops the summary.**
Before, the base filter of `gh pr list` passed over such a number. Now
`gh pr view` finds no pull request at it, and that is a failed call. The
`release` ruleset takes squashes alone into `release/**` (`frame/design.md`
G4), and GitHub ends each squash subject with the pull request's `(#N)`, so
such a number reaches the range only where a person edits the subject at
the merge. The closer still reads such a number as a skip, by its own
`/issues/N` read. The note does not copy that read: telling a missing pull
request apart from a failed call would mean reading `gh`'s words. Judged
against `skills/core/SKILL.md` *The rule a mechanism is kept against*,
where a script decides on an exit code and not on words.

**A probe read the changed functions against this repository, executed
once.** `test_tmp_note_reads.py`, under this phase's scratch directory, ran
`previous_tag`, `merged_pulls`, `release_pull_body` and `theme_of` at
`92d9b602` against the tags `v0.41.0` and `v0.40.1`, with a person's `gh`
and no write. `merged_pulls` returned #1666, #1667 and #1668 for
`v0.40.1..v0.41.0`, and #1663 for `v0.40.0..v0.40.1`. The old reading,
`gh pr list --base release/v0.41.0` and `--base release/v0.40.1`, lists
the same two sets (executed). `release_pull_body` found #1669 and #1664,
and `theme_of` gave each body's first sentence.

**Departure 1: `.github/workflows/publish-release.yml`'s comment on the
permissions block named `gh pr list` as the read of labels and head
branches.** *Scope* item 6 does not list the file. The read is
`gh pr view` now, so the comment names both reads. Judged against contract
rule 19.

**Departure 2: `.github/scripts/roll_flow_measurement_issue.py`'s
docstring stated the old version move.** It said the release's first pull
request moves the version, and that the next version is named when the
next release branch is cut. *Scope* item 6 names the release automation's
prose, and this script runs as the second step of
`close-issues-on-release.yml`, but the item's list does not name it. The two
sentences now say the last pull request into `release/next` moves it, and
that the next number is read when the next release is cut. The script's
logic is unchanged, as `frame/design.md` *Readers of the number* says.
Judged against contract rule 19.

**Departure 3: `tests/text/test_a_merged_ticket_says_so_on_the_tracker.py`'s
docstring said the label workflow runs on a squash into a numbered branch.**
Phase 1 made the script label `release/next` alone, and this phase changes
the workflow's comment to say so. The docstring now names `release/next`.
Judged against *Scope* item 9.

**The mark reads the tag's range, and its refusal names the read.**
`release_mark.py#mark_release` passes `commit_range(previous_tag(tag), tag)`
to `merged_pulls`. Its refusal where the set is None read `gh pr list could
not list the release's pull requests`, and now reads `the release's pull
requests could not be read`. The case
`test_refuses_on_any_failure_and_leaves_the_note_as_published` names it
`the pull requests cannot be read` and pins the new words (contract rule
14). The mark job checks out the tag with `fetch-depth: 0`, so
`previous_tag` has the tags it reads.

**Every changed case was seen red against the scripts at `1a6e790d`.** The
two changed test files were run against the old scripts with
`bin/test tests/github/test_publish_release_note.py tests/github/test_release_mark.py -q -p no:xdist`,
which printed `41 failed, 103 passed`. Twenty-eight cases failed on
`unexpected command: ('gh', 'api', '--paginate', 'repos/example/repo/milestones?state=all&per_page=100')`,
the milestone read. Six of `Test_release_pull_body` failed on its old
signature, and the two settles-alone cases on the stub's. The A1 case of
`main` failed on the range it lists, `[('example/repo', '1.2.3')]`. The
label case of `theme_of` failed on `'The notes come.' == 'Purpose: the
notes come.'`. The mark's range assertion failed on `('example/repo',
'1.2.3') != ('example/repo', 'v1.2.2..v1.2.3')`, and its refusal case on
the old words. `test_the_list_is_the_pull_requests_the_range_names` failed
on `ValueError` in the stub, since the old call was `gh pr list`.
`test_a_gh_that_gave_no_answer_is_read_as_each_read_reads_a_failure`
failed on its line, and under the old script its stub let the real
`gh pr list --repo example/repo` run, which answered `HTTP 401: Bad
credentials`. Under the new script that case's `gh pr view` is the stubbed
call, and the new script makes no other `gh` call there.

**Each unit that adds behaviour was mutated after `92d9b602`, one
`agentic mutate` call per file.**

- `publish_release_note.py`, with
  `bin/test tests/github/test_publish_release_note.py -q -x -p no:xdist`:
  `18 mutants, 18 red, 0 SURVIVED`. The mutants read only the newest
  subject, read the first `(#N)` in place of the last, asked one number
  twice, asked the wrong number, asked `gh pr list` in place of
  `gh pr view`, dropped `labels` from the fields, ignored a failed call,
  went on past a failed call and past an answer that is not JSON, listed
  `release/next` in place of `main`, dropped the `--limit`, flipped the
  merge commit's comparison, put the `Purpose:` strip back, dropped the
  theme of a note of fragments, gave a note of settles alone a theme, passed
  the tag in place of the range, read the release pull request before the
  existing-release guard, and changed the settles-alone log line. The two
  that went red fastest, the range and the guard, were run again alone:
  each failed on its own assertion, `('example/repo', 'v1.2.3') !=
  ('example/repo', 'v1.2.2..v1.2.3')` and `the release pull request was read
  for a release that already exists`.
- `release_mark.py`, with `bin/test tests/github/test_release_mark.py -q -x -p no:xdist`:
  `2 mutants, 2 red, 0 SURVIVED`, the tag passed in place of the range and
  the old refusal words.

The docstrings of `tag_release.py`, `close_issues_on_release.py` and
`roll_flow_measurement_issue.py`, and the comments of the three workflows,
are prose. The phase-boundary set imports each script and loads each
workflow, and no mutant was run on them.

**The phase-boundary set** is the files of the plan row's *Verified by*
cell, the tree-wide files under `tests/text` and `tests/behaviour`, and
three more test files that load a path this phase changed:
`tests/github/test_label_merged_on_release_branch.py` and
`tests/github/test_release_completeness_check.py`, whose scripts load
`close_issues_on_release.py` through the label script, and
`tests/github/test_roll_flow_measurement_issue.py`, which loads
`roll_flow_measurement_issue.py`. The cell does not name the three. They
belong to the cell's one suite, and they ran under it as
`bin/test tests/github/test_label_merged_on_release_branch.py tests/github/test_release_completeness_check.py tests/github/test_roll_flow_measurement_issue.py -q`.

**The keep files.** This phase added, changed and removed no line of
`frame/keep-2.txt` or `frame/keep-3.txt`. Phase 1's search now prints one
line opening `>`, the `milestone_titles` line of the removed
`milestone_description`'s docstring, which `frame/design.md` *Kept lines of
the searches* names as removed by *Scope* item 5 in this phase.
`frame/keep-1.txt` is phase 1's, and `skills/verify/SKILL.md` *An absence
claim is only as good as the search behind it* has a phase keep its own
and later phases' keep files, so it stays as phase 1 closed it.

**What phase 3 meets.** Phase 3's search, run at `92d9b602`, prints
leftovers only in the files *Scope* items 7 and 8 name and their cases.
Two statements of the old version move stand outside this phase's files.
The comment at the head of `.github/workflows/hygiene.yml`'s version step
says the version moves in the release's first pull request into the
branch, beside the `::error::` line *Scope* item 7 rewrites. The docstrings
of `tests/behaviour/test_release_hygiene.py` at lines 225, 249 and 621, and
the message at line 483, say the same; `frame/design.md` *Readers of the
number* gives them to *Scope* item 9.
