# Phase 1: 1793226631-every-release-ends-with-a-preparation-pull-request

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 538e9b13 |

## What this phase was asked

Build phase 1 of `frame/plan.md` against the frame at `7bead7e7`, under the
owner's automation answer, with `frame/questions.md` Q1, Q2 and Q3 on their
defaults. The merge to `main` tags and publishes. The phase adds
`.github/scripts/tag_release.py` and `tests/github/test_tag_release.py`
(S1 to S7). It changes `publish-release.yml`'s trigger, adds the tag step
and wires the `seal` job to the tag step's output (S8). It rewrites the
workflow's, the script's and three test modules' accounts of the tag push,
as `## Removes` lists them. Each new case and the rewritten S8 case are seen
red against no script and against the workflow at `4134055a`.

## What this phase found

**The frame holds against the tree (read, at `7bead7e7`).** Every phase 1
coordinate in `frame/design.md` *Removes* and `frame/plan.md` *Technical
context* resolves to the text it names: `publish-release.yml:3-19` and
`:35-37`, `publish_release_note.py:12-14`, the three module docstrings, and
`tests/behaviour/test_a_release_publishes_its_note.py:115-119`.

**The defaults this phase built on.** Q1 (a), Q2 (a) and Q3 (a) do not reach
phase 1. Q3 (a) is why no hygiene step was added. Q4 is not answerable
before 0.24.0's merge.

**How the cases were seen red (executed).** The 13 cases of
`tests/github/test_tag_release.py` as first written, `test_census` included,
failed against no script: `bin/test tests/github/test_tag_release.py -q -p
no:xdist` exited 1 with 13 failed. The rewritten S8 case,
`test_the_workflow_fires_on_the_tag_and_writes_one_release_one_asset_one_edit`,
failed against the workflow at `4134055a` on its first assertion, `the
workflow does not fire on main`, exit 1. With the script and the workflow in
place, both modules passed.

**`decide` takes one argument the design does not name.** The design gives
it the ref, the two versions, and the tag's commit. S6 asks the log to say
whether `BEFORE` was all zeros or absent from the checkout, and a bare None
cannot say which. So `decide` also takes the pushed commit, which S3 and S4
compare the tag's commit against, and `missing`, the reason the earlier
version is None. `version_before` returns that reason. One arm is added
beyond S1 to S6: a pushed commit whose `plugin.json` names no version passes
on no tag, rather than a `vNone` tag.

**`write_output` has one source.** `tag_release.py` imports it from
`publish_release_note.py` rather than copying it. That module's imports
(`console`, `blocks`, `close_issues_on_release`) all sit in the checkout the
step runs in.

**`gh` is found through `shutil.which`.** S1's fake `gh` is a `gh.cmd` on
Windows, and `subprocess.run(["gh", ...])` does not find a `.cmd` by its bare
name. The fake follows the shape of `tests/conftest.py#_write_gh_stub`.

**A dry run passes the decision's tag on where it creates nothing.** S7
specifies only the dry run of a creation, which passes on no tag. A first
draft also blanked the tag for every other dry run. No case could reach that
conditional, so it was removed. `DRY_RUN` is never set in the workflow.

**Mutants (executed, `bin/seal mutate`, one command per unit).** Each arm of
`decide`, both reasons in `version_before`, `version_at`'s type check,
`tag_commit_of`, the three refusals in `create`, the dry run's early return,
the refused creation's output, and the output line in `main` were broken one
at a time. Each mutant turned at least one case red. Two first survived:
`version_before`'s reason for an earlier commit with no version, and
`create`'s refusal from the checkout's `git tag`. Each now has a case, at
`9a5d05c1`. One unit still has no case: `console.to_utf8()`. No census reads
`.github/scripts/`, and the `seal/follow-up.md` row on `console.to_utf8()`
already names that gap and its answerer.

**`seal layout --check` read the new module only once its script was
tracked.** Before the first commit it refused the file for a TARGET git did
not track, and that was read as the only refusal. After the commit it
refused every class of `tests/github/test_tag_release.py` for lacking a
`test_accepts_` or a `test_refuses_` case. `538e9b13` renames the cases and
adds the accepting half to `Test_version_at` and `Test_create`, and
`seal layout --check` then exited 0 (executed). The phase closes at that
commit, not at `9a5d05c1`.

**Two sentences in the publishing files changed beyond `## Removes`.**
`publish_release_note.py`'s *Environment* line said `TAG` came from
`github.ref_name`. On the push to `main` that name is `main`, so the line now
names the tag step's output. The workflow's permissions comment counted three
writes. It now counts four, the tag among them.
