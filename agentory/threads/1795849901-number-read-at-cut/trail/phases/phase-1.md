# Phase 1: 1795849901-number-read-at-cut

## What this phase found

**The frame holds, with the three departures below.** Its coordinates were
opened at the frame commit `ae7aca71`, whose code is the code at `9d7a8fe2`
(`git diff --stat 9d7a8fe2 ae7aca71` lists the three frame files and the
three keep files alone). `release_completeness_check.py`'s `merge_base`,
`subjects_since`, the milestone reads, `judge`, `judge_feat` and `main`,
`label_merged_on_release_branch.py`'s name mapping and label description,
`close_issues_on_release.py#spend_label` with its three call sites, and the
two steps of `hygiene.yml`'s `release` job each stood where
`frame/plan.md` *Technical context* says. The phase 1 search of the
*Verified by* cell printed 29 lines opening `<` and none opening `>` at
`ae7aca71`, as `frame/design.md` G16 says. Judged against
`skills/implement/SKILL.md` *The frame is judged before it is built to*.

**Departure 1: the closer loads the label's name when it runs, not when it
is imported.** `frame/design.md` *Data & interfaces* has
`close_issues_on_release.py` read `merged: next` from
`label_merged_on_release_branch.py`, and the label script loads the closer
at its own top level. A load at the closer's top level would make the two
load each other. `lib/sibling.py#load` registers a module before it runs
it, so that cycle would still finish, but each entry point would then run
one of the two files twice. The new `close_issues_on_release.py#spent_labels`
loads the label script when `main` asks for the names. The label script
still holds the name once, as `MERGED_LABEL`, beside `INTEGRATION_BRANCH`.
Judged against `frame/design.md` *Data & interfaces*.

**Departure 2: three citations of the removed names were corrected, which
`frame/design.md` *Readers of the number* does not list.** Its search, G11,
looked for spellings of a numbered name, and a citation of a function by
`path#name` spells none. `.github/scripts/publish_release_note.py`'s
comment above `TAG_RE` cited `label_merged_on_release_branch.py#version_of`,
and `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`'s
comment above `BRANCH_SHAPES` cited `#RELEASE_BRANCH`. Both names are gone,
and `tests/behaviour/test_a_cited_section_stands_in_its_file.py` reads such
a citation. The docstring of
`tests/github/test_publish_release_note.py`'s case for a `vnext` tag
compared its refusal with the label script's refusal of a branch name it
cannot read a version from, which the label script no longer makes. Each
lost its clause and kept the rest. The two `release/vX.Y.Z` spellings
these lines hold are left for phase 3. Judged against contract rule 19.

**Departure 3: a comment in `lib/closing.py` stated the removed refusal.**
Its paragraph on the limits of `HIDDEN` said that a body masked more than
GitHub masks it makes "the completeness check refuse the release, which is
loud". That was the `M \ D` arm. The signal and the check read D with the
same readers, so the issue now stays open on the tracker after its release
ships, and the comment says that. It is a comment in a shipped file, so
the module still imports: `tests/lib/test_closing.py` ran green at the phase
boundary. Judged against contract rule 19.

**Two removals of the label script that *Scope* item 3 does not name went
with the mapping.** `label_name(version)` and `label_description(version)`
built the label's name and description from a version. They are the
constants `MERGED_LABEL` and `LABEL_DESCRIPTION` now, as `frame/design.md`
*Data & interfaces* asks for one constant for the label, and
`create_label` and `add_label` take no version. The case
`test_a_minor_with_no_feat_ships_as_the_minor_it_was_named` went with
`judge_feat`: it held the line that a minor named at its cut ships as that
minor, and no release is named at its cut now.

**The number's two edges were decided in the build.** *Scope* item 1 says a
head "that moves the major, with minor and patch 0" is the owner's word.
`judge_number` reads that as a major above the base's, so a lower major,
`1.2.3` to `0.0.0`, fails as every other move does. A version is read as
three integers by `parts`. A `plugin.json` whose version is not `X.Y.Z`
raises in the conversion and ends the run loudly. The frame names no
answer for that shape, and no case holds it. Judged against *Scope* item 1
and `skills/core/SKILL.md` *The rule a mechanism is kept against*, which
keeps a guessed reading from blocking.

**The step's name is quoted in `hygiene.yml`.** It reads `the version a
release moves to is the number its subjects read, and every issue labelled
merged: next is one it carries`. YAML reads a colon followed by a space in
a plain scalar as a mapping, so the name is a quoted string.
`tests/text/test_a_release_cannot_ship_an_untrue_milestone.py#STEP` holds
its opening words.

**What `frame/questions.md` asked of this phase.** Q2 is built on its
default (a): `release_completeness_check.py` judges `L \ D` for a head of
any name. Q1 is about `publish_release_note.py#merged_pulls`, *Scope* item
5, which is phase 2's, so this phase did not meet it and decided nothing on
it.

**Every new case was seen red against the scripts at `ae7aca71`.** The
changed test files were run against the old scripts with
`bin/test tests/github/test_release_completeness_check.py
tests/github/test_label_merged_on_release_branch.py
tests/github/test_close_issues_on_release.py
tests/text/test_a_release_cannot_ship_an_untrue_milestone.py -q -p no:xdist`,
which printed `58 failed, 58 passed`. The cases of `number_read`,
`judge_number` and `version_at` failed on `AttributeError`, since the
functions did not exist. The cases of `judge` failed on `TypeError` for its
old signature, and `create_label` on its old one. `Test_main` of the check
failed on `'' is not a release/vX.Y.Z branch — nothing to judge`. The label
script's push to `release/next` failed on `assert [] == ['merged: next']`,
and its refusal of `release/v1.2.3` on `a push to 'release/v1.2.3' still
reached the tracker`. The closer's `merged: next` cases failed on `merged:
next survived the close` and on `assert "would remove 'merged: next' from
#7" in ...`. The hygiene step's cases failed on `0 steps of hygiene.yml open
with ...`.

The case that the check asks the tracker for no milestone,
`Test_main::test_accepts_a_run_that_reads_no_milestone_and_no_head_name`,
named `test_reads_no_milestone_and_needs_no_head_name` until `f3393b15`,
was red at `ae7aca71` for its other half only, the skip. Run alone against
the old script with `HEAD_BRANCH=release/v1.2.3` in the environment, it
failed on `AssertionError: unexpected command: ('gh', 'api', '--paginate',
'repos/example/repo/milestones?state=all&per_page=100')`, the milestone
read it names.

Two `test_refuses_` cases were added after the first phase-boundary run,
below. Each was shown red by `agentic mutate` with only its guard broken,
in one call: `test_refuses_a_ref_git_cannot_show_by_ending_the_run` with
the `git show` read replaced by a constant version, and
`test_refuses_any_spelling_but_feat_as_a_minor` with the `startswith(FEAT)`
test replaced by a search for the word. The call printed `2 mutants, 2 red,
0 SURVIVED`.

**Each unit that adds behaviour was mutated after its commit, one
`agentic mutate` call per file.**

- `release_completeness_check.py`, after `03debfac`, with
  `bin/test tests/github/test_release_completeness_check.py -q -x -p no:xdist`:
  `22 mutants, 21 red, 1 SURVIVED`. The mutants broke `version_at`'s ref
  and path, `number_read`'s two arms and its `feat:` test, `parts`'s order,
  the major test twice, the refusal's condition twice, `failed`, the named
  subjects, the kind, the `feat: subject` and `not read` lines, the major
  and unmoved lines, `main`'s exit code, its head read and its label name,
  and `judge`'s `L \ D` arm and its repair sentence. The survivor compared
  the majors with `!=` in place of `>`. The commit `a83dd987` adds the
  parameter `1.2.3` to `0.0.0` to
  `test_refuses_a_major_that_is_not_its_first_release`, and the mutant run
  again alone printed `red`.
- `label_merged_on_release_branch.py`, with the three changed test files of
  `tests/github/`: `12 mutants, 12 red, 0 SURVIVED`. The mutants broke the
  branch and the label constants, the branch test twice, the skip line, the
  description's length, branch and wording, and the name, the description
  and the label each script call sends.
- `close_issues_on_release.py`, with its own test file: `9 mutants, 8 red,
  1 SURVIVED`. The mutants broke `spent_labels` twice, the loop of
  `spend_labels`, its dry arm twice, its guard on the write, the read of
  what the issue carries twice, and the removal after the close. The
  survivor ended the dry arm's loop at the first label. The commit
  `26c15d5b` turns the dry-run case into one over an issue that carries
  both labels, and the mutant run again alone printed `red`.

The hygiene step is YAML that only the text cases read. Its name and its
inputs were shown red with the rest at `ae7aca71`, and no mutant was run on
it.

**A probe read the number against this clone's git, executed once.**
`test_tmp_version_at.py`, under this phase's scratch directory, ran the
changed `subjects_since`, `merge_base`, `version_at` and `judge_number` at
`26c15d5b` against `origin/main`, with no `gh` call. It printed `number
read: 0.42.0, the next minor of 0.41.0, from 1 feat: subject(s)`, the
branch's own `feat:` subject, and that `plugin.json` is not moved. The
version at `origin/main` is the one this clone fetched, and phase 3
confirms the release's number against the base it merges.

**The first phase-boundary run, at `26c15d5b`, failed three cases.**
`tests/text/test_a_cited_commit_outlives_the_squash.py` refused `abc1234`,
a ref of a `version_at` case that reads as a commit; the case now names
`upstream/main`. `tests/behaviour/test_this_repository_passes_its_own_checks.py::Test_agentic_layout`
refused four classes that held no `test_refuses_` case: `Test_create_label`,
`Test_number_read`, `Test_version_at` and the check's `Test_main`. The
commit `f3393b15` gives each one. The third,
`tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
failed at `ae7aca71` too, for the `gaps.md` this phase writes.

**The phase-boundary set** is the files of the plan row's *Verified by*
cell, the tree-wide files under `tests/text` and `tests/behaviour`, and
three more test files that load a path this phase changed:
`tests/github/test_release_mark.py`, which loads
`publish_release_note.py`, and `tests/skills/test_chain_check.py` and
`tests/skills/test_pr_body.py`, whose scripts load `lib/closing.py`. The
cell does not name the three. They belong to the cell's one suite, and
they ran under it as
`bin/test tests/github/test_release_mark.py tests/skills/test_chain_check.py tests/skills/test_pr_body.py -q`.

**The read of the phase's range made the corrections below, in
`0203c27a`.** The case that holds the hygiene step to its inputs said that
two absences are silent, and with `HEAD_BRANCH` gone one is. A sentence of
the check's input table lacked a possessive. The module docstring of
`tests/github/test_close_issues_on_release.py`, the comment above
`publish_release_note.py#TAG_RE` and the limits paragraph of
`lib/closing.py` were rewrapped where this phase's edits had left a short
or a long line.

**`agentic rules --check` excuses one line, as `frame/design.md` G14
says.** It printed `excused: docs/releasing/issues-and-milestones.md:239:
One thing reads a milestone, and it can stop a release: no test carries the
marker a-release-is-judged-under-its-two-names`. The cases of
`a-patch-carries-no-feat` now hold the number reading.

**One line went into `frame/keep-3.txt`, a commit after the line.** The
parametrize line of
`tests/github/test_label_merged_on_release_branch.py::Test_main::test_refuses_a_branch_that_is_not_release_next_and_writes_nothing`
names `release/v1.2.3` among the branches the label script refuses. It is
of the kind `frame/design.md` *Kept lines of the searches* keeps as "a line
of a test that reads a numbered name to refuse it", so phase 3's search
prints it at that phase's close. The line was written in `03debfac`, and the
keep file took it in this phase's records commit, which is a later commit
than the one `skills/verify/SKILL.md` *An absence claim is only as good as
the search behind it* asks for. This phase added, changed and removed no
line of `frame/keep-1.txt` or `frame/keep-2.txt`, and phase 2's search
prints no line opening `>` against `frame/keep-2.txt`.
