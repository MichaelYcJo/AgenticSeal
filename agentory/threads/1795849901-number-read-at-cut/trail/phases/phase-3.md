# Phase 3: 1795849901-number-read-at-cut

## What this phase found

**The frame holds for this phase, with the three departures below.** Its
coordinates were opened at `cab8981c`, the HEAD the phase began at.
`CONTRIBUTING.md` *Opening a pull request* and its table,
`.github/PULL_REQUEST_TEMPLATE.md`'s opening comment, `README.md` line 474,
`README.ko.md` line 470, `skills/commit-pr-convention/SKILL.md` *Branch
names* and the version step of `.github/workflows/hygiene.yml` each stood
where `frame/plan.md` *Technical context* says. The comment of the version
step stood at lines 74 to 77 and its `::error::` line at 112, the lines
phase 2's record names. The phase 3 search of the *Verified by* cell printed
21 lines opening `<` and none opening `>` at `cab8981c`. Each of the 21 is
in a file that *Scope* items 7 and 8 name, or in a case of those files. Judged
against `skills/implement/SKILL.md` *The frame is judged before it is built
to*.

**Departure 1: the release half of the version step's refusal changed as
well.** *Scope* item 7 names the half that says where a contribution goes.
The other half told a release pull request to "move the version", and a
release pull request's head is `release/next`, which the `release` ruleset
holds to squashes (`frame/design.md` G4). So the line now says to move the
version in a pull request into `release/next`. No case pins those words;
`test_the_refusal_names_the_file_a_release_moves` still holds
`plugin.json` in the line. Judged against contract rule 19 and the
`## Rule changes` operation on *Cutting a release*.

**Departure 2: `CONTRIBUTING.md` *What a contribution is not asked for*
named "the version and milestone steps".** Since phase 1 the second step
reads no milestone. The sentence now names the version step and the release
check, and each still exits early on any base but `main` (`hygiene.yml`,
read). *Scope* item 7 names only *Opening a pull request*. Judged against
contract rule 19.

**Departure 3: two lines went into `frame/keep-3.txt`, in the commit that
wrote them, `74932873`.** The first is the line of *Scope* item 8's
convention sentence that holds `release/vX.Y.Z`,
`skills/commit-pr-convention/SKILL.md:  with no number, such as
`release/next`, or `release/vX.Y.Z` where the`. It is of the kind
`frame/design.md` *Kept lines of the searches* keeps as "the convention
line *Scope* item 8 writes". The second is the entry of
`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#BRANCH_SHAPES`
that pins that sentence whole. The row of that kind does not name a pin.
The entry is the same sentence, and it names `release/vX.Y.Z` as one shape
a repository may use, which is the reason the row gives. So it is kept
under that row, and the framer may name the pin in it. No kept line was
changed or removed.

**The two refusals of a numbered branch on the contributor surfaces read
the module's own pattern.** `test_the_section_names_the_integration_branch_and_no_numbered_one`
and `test_no_contributor_facing_surface_names_a_concrete_release_branch`
each wrote `re.findall(r"release/v\d+\.\d+\.\d+", …)`, the pattern the same
module names `RELEASE_BRANCH`. `frame/keep-3.txt` as the framer drew it
holds neither line, so the frame has them change. Each now calls
`RELEASE_BRANCH.findall`, so the module states the pattern once. What each
refuses is unchanged, and each was shown red below. Judged against
`frame/keep-3.txt` and `skills/core/SKILL.md` *The rule a mechanism is kept
against*, where a fact has one source.

**One case was renamed.** `test_the_section_names_the_branch_by_convention_not_by_number`
is now `test_the_section_names_the_integration_branch_and_no_numbered_one`,
since the section names one branch and no convention. `git grep` of the
old name printed nothing outside this record at `98bf50d8` (executed).

**The test file whose name no longer fits keeps it.** The weighing is in
`gaps.md` *Not done*, rewritten in this phase. `frame/plan.md` A10's ground
does not reach `tests/text/test_a_release_cannot_ship_an_untrue_milestone.py`,
since no `check:` line and no line of `docs/` names it. No *Scope* item names
the move, so this phase leaves it to the framer.

**The fragment carries no `### Process changes` table.**
`docs/layout/the-record-layout.md` *A change writes fragments, never a
shared file* asks for one where the work item's diff changes a file it
lists. `git diff --name-only origin/release/v0.43.0..HEAD` at `98bf50d8`
(executed) names none of them. The branch convention this phase changes is
`skills/commit-pr-convention/SKILL.md`, which the list does not hold, and
the release rules change through `## Rule changes` at the settle.

**The version moved to `0.43.0` in `e3554644`, the commit that adds
`changelog.md`.** `frame/plan.md` *Operational impact* names that value, and
it holds only once the base holds `0.42.0`. At `e3554644`,
`git show origin/main:.claude-plugin/plugin.json` reads `0.41.0` (executed),
and `origin/release/v0.41.1` and `origin/release/v0.42.0` each still read
`0.41.0`. Before the move, the changed release check, run by hand as
`HEAD_SHA=HEAD REPO=MichaelYcJo/AgenticSeal python3 .github/scripts/release_completeness_check.py`,
printed `number read: 0.42.0, the next minor of 0.41.0, from 3 feat:
subject(s)` and exited 0. After it, the check exited 1 with `the head moves
plugin.json to 0.43.0, and the subjects read 0.42.0` (both executed). So the
confirmation the plan asks for waits on the merge of `main` that brings the
release before this one. `gaps.md` *Not verified* names it, with the
orchestrator as its answerer.

**Every changed case was seen red against the surfaces at `cab8981c`.** The
four changed test files were run with the surfaces not yet edited, as
`bin/test tests/behaviour/test_the_contributor_has_a_procedure.py tests/behaviour/test_the_release_check_watches_what_ships.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/behaviour/test_release_hygiene.py -q -p no:xdist`,
which printed `7 failed, 128 passed`. The section case and the three
surface cases failed on `assert 'release/next' in …`, and the refusal case
of the version step on the same assertion over the `::error::` line. The
*Branch names* case failed on `*Branch names* does not state "A release
branch takes the repository's own name: …"`. The timer's refusal case
failed on `the timer's cost went`, the pin of the new words of
`test_release_hygiene.py#refusal` (contract rule 14).

**Two `agentic mutate` calls showed the refusals of a numbered branch red,
each with a numbered branch written into the surface it reads.** The
template, with `release/v1.2.3` added to its base sentence and
`-k concrete_release_branch`, printed `red`, failing on
`.github/PULL_REQUEST_TEMPLATE.md names ['release/v1.2.3']`. The section of
`CONTRIBUTING.md`, with the same name added and
`-k integration_branch_and_no_numbered_one`, printed `red`, failing on
`the section names ['release/v1.2.3']`. The rest of the phase is prose, a
comment, an error message and docstrings, which the cases above read, and
no unit of logic, so no other mutant was run. Judged against
`skills/verify/SKILL.md` *The narrow command still has to be able to fail*.

**The phase-boundary set** is the plan row's *Verified by* command, which
covers every changed test file and the tree-wide files under `tests/text`
and `tests/behaviour`, and the test files outside those whose scripts read
`.claude-plugin/plugin.json`, which this phase changed:
`tests/skills/test_pr_body.py`, `tests/lib/test_core.py`,
`tests/hooks/test_core_start.py`, `tests/skills/test_stamp.py`, and
`tests/github/test_plugin_directory_check.py`,
`test_release_completeness_check.py`, `test_release_mark.py`,
`test_tag_release.py` and `test_roll_flow_measurement_issue.py`. The cell
does not name them. They belong to the cell's one suite, and they ran under
it as
`bin/test tests/skills/test_pr_body.py tests/lib/test_core.py tests/hooks/test_core_start.py tests/skills/test_stamp.py tests/github/test_plugin_directory_check.py tests/github/test_release_completeness_check.py tests/github/test_release_mark.py tests/github/test_tag_release.py tests/github/test_roll_flow_measurement_issue.py -q`,
which printed `539 passed` at `8575d33b`. `tests/skills/test_broad_gate.py`
was not run: its version cases write the manifest they read (`a_plugin`).
The cell's command at `e3554644` printed `1 failed, 948 passed`: the first
line of the rewritten paragraph of `CONTRIBUTING.md` ran to 91 columns, and
`8575d33b` rewraps it. At `98bf50d8` it printed `949 passed, 10 skipped`,
the search of the cell printed nothing, and `bin/agentic rules --check`
exited 0 with the one line `frame/design.md` G14 says it excuses (all
executed).

**The read of the phase's range made one correction, in `98bf50d8`.** Two
docstrings of `test_release_hygiene.py`, those of `shipped_tags` and
`timers_in`, and that of `test_a_tagged_version_is_history_and_is_kept`, were
rewrapped where this phase's edits had left a long or a short line.

**Two sentences of `docs/releasing/release-checklist.md` *The release pull
request* state the old rule, and no `## Rule changes` operation reaches
them.** Line 150 says `main` stays "where the release branch was cut unless
a hotfix moves it", and line 156 names "the `hygiene` workflow's version
and milestone steps". `frame/questions.md` Q2's answer removes the hotfix
route, `release/next` is cut once, and phase 1 took the milestone out of
the second step. The text of `docs/releasing/` is out of this work item's
scope (`frame/design.md` *Scope*), so both are left for the framer to fold
into `## Rule changes`.
