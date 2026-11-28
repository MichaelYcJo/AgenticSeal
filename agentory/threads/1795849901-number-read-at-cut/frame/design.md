# Design: 1795849901-number-read-at-cut

## Grounding

The tree as read at `9d7a8fe2`, which is `596c79a6` and this work item's
`routing.md`. Rulesets, milestones and labels are tracker state read on
2026-11-28.

| Policy clause | What it fixes for this work |
|---|---|
| G1 `skills/core/SKILL.md` *The rule a mechanism is kept against* | Nothing is kept beside the tree to stay in step with it. A release number written into a milestone title and a branch name before the work is such a thing, so the number is read from the tree when the release is cut. What stood only on the written number (the rename procedure, the milestone reading, and the checks and tests that hold either) goes in the same change |
| G2 `skills/core/SKILL.md` *The first value: efficient development through the IADD process* | Asking a person is the costliest step. Each pull request's prefix was its writer's judgment, and a script reads the prefixes exactly, so no person approves the number. A major is the owner's word, as #1671 states |
| G3 `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | This work item's subject is the release mechanism: workflows, scripts, tests and the contributor surfaces. So the rules it changes in `docs/` go into `## Rule changes` for the settle, as the released, unsettled `1795841828-settle-only-release-note` did for the same documents. The skill, the READMEs, `CONTRIBUTING.md` and the pull request template stand outside the policy root and are edited directly |
| G4 `docs/releasing/branch-and-release.md` *Work accumulates on a release branch*, the rulesets table (read), and `gh api repos/MichaelYcJo/AgenticSeal/rulesets/<id>` (executed, 2026-11-28) | The `release` ruleset targets `refs/heads/release/**/*` with `non_fast_forward`, `pull_request` (squash only) and `required_status_checks` (`lint`, `release`, `do_not_enforce_on_create: true`), with no `deletion` rule and no bypass actor. The `main` ruleset holds `deletion`, `non_fast_forward`, `pull_request` (merge only) and the same two checks. `gh api repos/MichaelYcJo/AgenticSeal/rules/branches/release%2Fnext` (executed) lists the `release` ruleset's three rules, as for `release%2Fv0.43.0`, so the ruleset already holds an unnumbered branch under `release/`. A version move reaches a `release/` branch only through a pull request |
| G5 probes `test_tmp_merge_shapes.sh` and `test_tmp_hotfix_shape.sh` under `<scratchpad>/1795849901-number-read-at-cut/frame/`, git 2.54.0, `git merge-tree --write-tree` (executed) | Four shapes, each in a synthetic repository. (a) The integration branch heads every release pull request and its version moves through a squash into it: the second release merges clean, and its range from the merge base holds that release's two subjects alone. (b) A cut branch from the integration branch carrying a direct version commit, the integration branch never moving the version: the second release conflicts on `plugin.json`. (c) Two numbered branches cut side by side from one `main` commit: the later release conflicts on `plugin.json`. (d) Shape (a) after a hotfix merged into `main` with its own version move: the next release conflicts on `plugin.json`, and a squash into the integration branch records no parent that could resolve it |
| G6 `git log --first-parent --format=%s origin/main` (executed at `596c79a6`) | 107 first-parent subjects are merges from a `release/v` branch. The newest that is not is #523's merge of 2026-09-23, from a `test/` branch. A route into `main` beside the release pull request has gone unused since that date |
| G7 `.github/scripts/release_completeness_check.py#judge_feat` (read) | The exact reading the issue cites stands: subjects from `git log --format=%s <merge-base>..<head>`, `feat:` counted in that one spelling, a near spelling printed as `not read`, a reverted squash still counted. The reading stays and names the number; the refusal it carried for a patch, and the rename it named, go |
| G8 `.github/scripts/label_merged_on_release_branch.py` (read) | The name mapping, from the branch `release/vX.Y.Z` to the version, to the milestone `release: X.Y.Z` and to the label `merged: X.Y.Z`, lives in this file, and `release_completeness_check.py` loads it. With no number before the cut, the label names the integration branch instead |
| G9 `.github/scripts/close_issues_on_release.py#spend_label` (read) | The closer already reads each issue's labels and takes `size: now` off an issue it closes, reporting a failed removal and going on. `merged: next` comes off the same way, so the label stays true for what is in and not yet shipped |
| G10 `.github/scripts/publish_release_note.py` (read) | Three readers of the number by name: `merged_pulls` lists `--base release/v<version>`, `release_pull_body` lists `--head release/v<version>`, and `milestone_description` reads the milestone `release: <version>` for the theme. `.github/scripts/release_mark.py` line 530 calls `merged_pulls` for the same set. The fragments are already read from the tag's range, from `previous_tag`, the highest version tag merged into the tag's first parent |
| G11 The issue's list of readers, against `git grep -n -E 'release/v|release/\*|"release/|release/<'` over the tree and `git grep -n -E 'merged: |"release: |release: X|milestone'` over `.github skills lib bin hooks`, at `9d7a8fe2` (executed) | A sample by search (contract rule 12): it lists each line that spells a numbered branch, a numbered milestone or a numbered label, and a reader that builds the name from parts another way would escape it. The verdict on each reader is *Readers of the number* below |
| G12 `gh api 'repos/MichaelYcJo/AgenticSeal/milestones?state=open'` (executed, 2026-11-28) | Open: four `backlog:` milestones, `log: measurement`, `release:` milestones for 0.38.3, 0.38.4, 0.38.6 and 0.40.0 with no open issue, and `release:` milestones for 0.41.1, 0.42.0 and 0.43.0. #1671's milestone is `release: 0.43.0` |
| G13 `gh issue view 1671 --json body,comments` (executed, 2026-11-28) | No comment. The body as read is the request this frame answers |
| G14 `skills/settle/scripts/rules.py` lines 42 to 52 (read) | `agentic rules --check` excuses a refused check line inside a section that a pending `remove` with no `from` takes out, and nothing else. So the tests of `a-release-is-judged-under-its-two-names` can go in this change, and a marker that a pending `change` leaves its check line naming stays carried by a test until the settle |
| G15 `templates/setup/hygiene.yml` line 75 (read) | A connected repository clones the plugin with `--branch v<version>`, a tag. Nothing there reads a release branch |
| G16 The three searches of `frame/plan.md`'s *Verified by* cells, each run from the top level at `9d7a8fe2` as `git grep --no-color --no-line-number -P '<pattern>' -- . ':!agentory/threads/1795849901-number-read-at-cut' \| LC_ALL=C sort \| diff - <keep file>` (executed) | Phase 1's prints 29 lines opening `<` and none opening `>`, phase 2's 20 and none, phase 3's 56 and none: each line opening `<` is one a *Scope* item changes or removes, and every other line the search prints is in the keep file. So each search fails on the tree before the build, and passes only where the build has changed every line it names |
| G17 `skills/settle/scripts/rule_changes.py#parse` and `#apply_op`, run by `test_tmp_rule_changes_in_order.py` in a `git clone --no-local` at `6652be71` under the scratch directory, against this file as folded on 2026-11-28 after round 1, with `1795841828-settle-only-release-note`'s operations placed first, as the settle places them in merge order (executed) | Both sections parse with no error and no unread line, and every operation of both is placed in its document in order, each `from` found once in its section. After both, `docs/releasing/` holds none of the sentences "could not be listed", "always a hand-edit", "unless a hotfix" and "version and milestone steps", and the one "never fails the job" it holds is limited to a note of fragments |

### Readers of the number

Each reader G11 found, and what this work does with it.

| Reader | Verdict |
|---|---|
| `.github/scripts/label_merged_on_release_branch.py` | changes: *Scope* item 3 |
| `.github/scripts/release_completeness_check.py` | changes: *Scope* items 1 and 2 |
| `.github/scripts/publish_release_note.py`, and `.github/scripts/release_mark.py` through it | changes: *Scope* item 5 |
| `.github/scripts/close_issues_on_release.py` | changes: *Scope* item 4 |
| `.github/scripts/tag_release.py` | its logic stays: it tags where a push to `main` moved `plugin.json`'s version, read at the push's two commits, and the release pull request still moves it. Its docstring changes: *Scope* item 6 |
| `.github/workflows/hygiene.yml` | changes: *Scope* items 2 and 7 |
| `.github/workflows/label-merged-on-release-branch.yml` | its trigger `release/*` matches `release/next` and stays, and the script decides by name. Its comment changes: *Scope* item 6 |
| `.github/workflows/close-issues-on-release.yml` | its comment changes: *Scope* item 6 |
| `.github/workflows/test.yml` | stays: `pytest-wide`'s guard reads `startsWith(github.base_ref, 'release/')`, which `release/next` meets |
| `.github/PULL_REQUEST_TEMPLATE.md`, `CONTRIBUTING.md`, `README.md`, `README.ko.md` | change: *Scope* item 7 |
| `skills/commit-pr-convention/SKILL.md` *Branch names* | changes: *Scope* item 8 |
| `skills/implement/orchestration.md` *Orchestrator: how the work is routed* | its version-move sentences stay: they state the convention of a repository that names the version when it cuts the branch and of one that moves it at the release, and the version pull request belongs to no work item, so no routing rule there reaches it. Its sentence that takes `main` for a pull request whose entries read as one release, or for a gate or a hook firing where it should not, changes: *Scope* item 12 |
| `skills/implement/merge-order.md` | stays: it orders the work items of a release and names which carries the move where the repository names the version at the cut, and it routes no pull request into `main` |
| `skills/verify/scripts/broad_gate.py:505` | stays: a docstring giving `release/vX.Y.Z` as one legal branch name that `git check-ref-format --branch` accepts; `release/next` is legal too |
| `skills/code-review/scripts/pr_wait.py:79` | stays: it names the `release/*` trigger, which matches `release/next` |
| `skills/settle/scripts/settle.py` | stays: it reads no `merged:` label. Its `merged:` strings are messages about the `gh pr list` it asks for the branch a `routing.md` names (lines 724 to 783, read). The issue lists it as a reader of `merged:`, and the tree does not bear that out |
| `tests/behaviour/test_release_hygiene.py#test_no_loaded_file_names_a_version_at_or_above_the_running_one` | its behaviour stays: on `release/next` the running version is the last shipped one, which a tag names, so the refusal still covers every untagged version above it. Its docstrings that say a release's first pull request moves the version change: *Scope* item 9 |
| `.github/scripts/roll_flow_measurement_issue.py` | its reading stays: it reads `plugin.json` at the push to `main` that ships a release |
| the test fixtures that use a `release/v…` name as any branch (`tests/skills/test_stamp.py`, `tests/skills/test_broad_gate.py`, `tests/skills/test_chain_check.py`, `tests/text/test_a_cited_commit_outlives_the_squash.py`, `tests/lib/test_tables.py`, `tests/lib/test_routing.py`, `tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py`, and the four proofer eval scaffolds) | stay: each holds the name as an example branch or a ref of a past release, and none reads a number from it |

## Scope

1. **The release check reads the number.**
   `.github/scripts/release_completeness_check.py` reads the version
   `plugin.json` holds at the base and at the head, and the commit subjects
   from their merge base to the head, as it reads them now. A `feat:`
   among the subjects makes the number the next minor of the base's
   version, and its absence the next patch. It prints the number, the two
   versions and each `feat:` subject. Where the head moves the version to
   another than the number read, it fails, naming the number and each
   `feat:` subject. A head version that moves the major, with minor and
   patch 0, is the owner's word: it passes and is printed as not read
   against the subjects. A head that leaves the version where the base has
   it is the version step's to judge, and this check prints the number and
   refuses nothing for it. The `not read` lines for a near spelling of
   `feat` stay. The rename repair the patch refusal named goes, with the
   refusal. The rule marker `a-patch-carries-no-feat` stays on the cases of
   this reading, since a pending `change` leaves its check line naming it
   (G14).
2. **The release check reads no milestone and no head name.** The `M`
   arms of `judge` (`M \ D` failing, `D \ M` reported, the `M` line), the
   missing-milestone warning, `milestone_titles`, `open_in_milestone`, the
   head-name skip and the `HEAD_BRANCH` input go.
   `.github/workflows/hygiene.yml`'s step stops passing `HEAD_BRANCH`, and
   its name and comments say what it reads. The docstring's input table,
   and the case that holds the step to it, keep to the inputs that remain.
3. **The integration branch is `release/next`, and the label it writes is
   `merged: next`.** `.github/scripts/label_merged_on_release_branch.py`
   names the branch and the label once each, labels only a push to that
   branch, and gives the label a description of 100 characters or fewer
   saying when it comes off. `version_of`, `milestone_title` and the
   `RELEASE_BRANCH` pattern go. `release_completeness_check.py` reads `L`
   as the issues carrying `merged: next`, and keeps `L \ D` failing and
   `D \ L` reported.
4. **The close takes `merged: next` off.**
   `.github/scripts/close_issues_on_release.py` spends `merged: next` on an
   issue it closes, and on one already closed, as it spends `size: now`:
   after the close, only where a read says the issue carries it, with a
   failed removal reported and the run going on.
5. **The note reads the release by its range and its pull request.**
   `.github/scripts/publish_release_note.py#merged_pulls` takes the pull
   requests whose `(#N)` ends a subject of the tag's range, the range the
   fragments are read from, with the same fields, and the same fallback
   where `gh` cannot answer. `release_pull_body` finds the release pull
   request by the merge commit the tag names, with no head name. The theme
   line is the first sentence of that pull request's body. For a note of
   fragments, a body that cannot be read leaves the note without one and
   fails nothing. A note of settles alone carries none, since that body
   stands whole beneath it, and still fails where that body cannot be
   read. `milestone_description`, `MILESTONE_TITLE` and `PURPOSE_LABEL`
   go. `.github/scripts/release_mark.py` reads the same set through the
   changed call.
6. **The release automation's prose names the integration branch.** The
   docstrings of `tag_release.py`, `close_issues_on_release.py` and
   `publish_release_note.py`, and the comments of
   `label-merged-on-release-branch.yml` and `close-issues-on-release.yml`,
   say `release/next` and state the version move as this design does.
7. **A contributor bases on `release/next`.** `CONTRIBUTING.md` *Opening a
   pull request* names the branch, drops the sentence that one numbered
   branch is open at a time and the listing that finds it, and its table
   row for `plugin.json` holds as it is. `.github/PULL_REQUEST_TEMPLATE.md`,
   `README.md` *Contributing* and its twin in `README.ko.md` say the same.
   The version step's `::error::` line in `hygiene.yml` names `release/next`
   as where a contribution goes.
8. **The branch convention names both shapes.**
   `skills/commit-pr-convention/SKILL.md` *Branch names* says a release
   branch takes the repository's own name: an integration branch with no
   number, such as `release/next`, or `release/vX.Y.Z` where the repository
   names the version when it cuts the branch.
9. **The cases follow.** Each test that pins a sentence, a name, an input
   or an output that items 1 to 8 and 12 change is changed in the phase that
   changes it, and a case the change leaves standing on nothing goes
   (`## Removes`).
10. **This release's own move.** This work item carries the version move of
    its release under the rule its branch was cut with, as `routing.md`
    states: the last phase moves `.claude-plugin/plugin.json` in the commit
    that adds `changelog.md`.
11. **The step's test file is named for what it holds.**
    `tests/text/test_a_release_cannot_ship_an_untrue_milestone.py` moves to
    `tests/text/test_the_release_check_runs_from_its_step.py`. Its cases
    read the release check's step in `hygiene.yml`: that it runs only for a
    pull request into `main`, that the step hands the script every input it
    reads, and that the job's token can read issues. Since phase 1 no case
    of it reads a milestone, so the name states a fact this work removed,
    and `skills/core/SKILL.md` *The rule a mechanism is kept against* has a
    change remove what stood on the old fact in the same change. The move
    rewrites the citations of the old path that `git grep` finds, in
    `.github/scripts/release_completeness_check.py`'s docstring,
    `tests/github/test_release_completeness_check.py` and
    `tests/behaviour/test_the_release_check_watches_what_ships.py`, and
    keeps every case as it stands, so no case is rebuilt. No `check:` line
    and no line of `docs/` names the file, so no rule change follows it,
    which is why `frame/plan.md` A10's ground for keeping the script's name
    does not reach it. Phase 3 builds it.
12. **The routing rule offers `main` only where the repository's convention
    does.** `skills/implement/orchestration.md` *Orchestrator: how the work
    is routed* takes `main` "when the accumulated entries read as one
    release, or when the change is a gate or a hook firing where it should
    not". In this repository a gate firing where it should not is the
    urgent fix the hotfix route carried, which `frame/questions.md` Q2's
    answer (a) removed, and after the settle `docs/releasing/` says nothing
    reaches `main` but the release pull request. The sentence is the
    plugin's and serves repositories whose convention allows a pull request
    other than the release into `main`, so it is limited, not removed: the
    orchestrator takes `main` in those two cases only where the
    repository's convention lets a pull request other than the release
    reach `main`. Every phase had closed when this item was framed, so the
    fix pass of round 1 builds it.

**Out of scope.**

- The text of `docs/releasing/` and `docs/running/what-a-script-gates.md`.
  The rules it states change through `## Rule changes`, and the settle
  writes them (G3).
- Cutting `release/next`, closing and renaming milestones, and every other
  tracker act. Each is the orchestrator's after the release that carries
  this work merges, as `frame/plan.md` *Operational impact* states, and none
  is a file.
- The rulesets. G4 shows the `release` ruleset already holds `release/next`.
- A merge queue, or a freeze while the release pull request is open, which
  owlery#279 weighs. A squash into `release/next` while the release pull
  request is open joins it, as a squash into a release branch does today,
  and the check reads the number again at that push.
- `skills/implement/merge-order.md`, and the version-move sentences of
  `skills/implement/orchestration.md`, shown not to change in *Readers of
  the number*.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 a release with a `feat:` | Given `plugin.json` at `0.8.1` on the base and a range holding one `feat:` subject, when the head moves it to `0.9.0`, then the check exits 0 and prints the number `0.9.0` | a case in `tests/github/test_release_completeness_check.py` marked `a-patch-carries-no-feat`, seen red against a reading that returns the patch |
| S2 a patch moved where a minor is read | Given the same range, when the head moves it to `0.8.2`, then the check exits 1 and its `::error::` line names `0.9.0` and the `feat:` subject | the same file, marked `a-patch-carries-no-feat` |
| S3 a release with no `feat:` | Given subjects `fix:` and `docs:` alone, when the head moves `0.8.1` to `0.9.0`, then it exits 1 naming `0.8.2`; moved to `0.8.2`, it exits 0 | the same file |
| S4 the owner's major | Given any subjects, when the head moves `0.8.1` to `1.0.0`, then it exits 0 and prints that a major is not read against the subjects | the same file |
| S5 the version not moved | Given a head whose `plugin.json` equals the base's, then the check prints the number and exits 0, and the version step refuses where something that ships changed | the same file, and `tests/behaviour/test_the_release_check_watches_what_ships.py` as it stands |
| S6 no milestone is asked | Given a run with `gh` answering every call, then no `gh api …/milestones` and no `gh issue list --milestone` call is made, and no `HEAD_BRANCH` is read | the same file, each `gh` call recorded |
| S7 a squash into `release/next` | Given a push to `release/next` whose pull request claims #N, then #N gains `merged: next`; given a push to any other `release/` branch, then nothing is labelled and the line says why | `tests/github/test_label_merged_on_release_branch.py` |
| S8 the close spends the label | Given an issue the release closes that carries `merged: next`, then it is closed and the label comes off after the close; a failed removal is reported and the run goes on | `tests/github/test_close_issues_on_release.py` |
| S9 the note's pull requests | Given a tag whose range holds squash subjects ending `(#11)` and `(#12)`, then the summary lists #11 and #12 and no pull request outside the range | `tests/github/test_publish_release_note.py` |
| S10 the note's theme | Given a release pull request whose merge commit the tag names and whose body opens with a sentence, then the theme line is that sentence; given a note of settles alone, then no theme line stands above its body | the same file |
| S11 a contributor's base | Given a contributor reading the pull request template, `CONTRIBUTING.md` or the version step's refusal, then each names `release/next` | `tests/behaviour/test_the_contributor_has_a_procedure.py`, `tests/behaviour/test_the_release_check_watches_what_ships.py` |
| S12 nothing names a numbered release branch outside what the design keeps | the search of phase 3 prints only the lines `frame/keep-3.txt` holds | phase 3's *Verified by* cell |

## Data & interfaces

- `release_completeness_check.py` inputs: `REPO`, `HEAD_SHA`, `BASE`
  (default `origin/main`), and `GH_TOKEN` through `gh`. `HEAD_BRANCH` goes.
  The versions are read with `git show <ref>:.claude-plugin/plugin.json` at
  the base and at `HEAD_SHA`, or at `HEAD` by hand. Exit 0 or 1, as now.
- `label_merged_on_release_branch.py`: one constant for the branch,
  `release/next`, and one for the label, `merged: next`, which
  `release_completeness_check.py` and `close_issues_on_release.py` read
  from it. Inputs unchanged: `BRANCH`, `BEFORE`, `AFTER`, `REPO`.
- `publish_release_note.py#merged_pulls` takes what names the range in
  place of `version`, and returns the list in the shape
  `gh pr list --json number,title,author,body,labels,headRefName` gives
  today, or None.
- The number: a base `A.B.C` with a `feat:` in the range gives `A.(B+1).0`,
  and without one `A.B.(C+1)`.

### Kept lines of the searches

Each phase's search keeps the kinds below. Phase 1's keeps one line a
later phase changes: the `milestone_titles` line of
`publish_release_note.py#milestone_description`'s docstring, which
*Scope* item 5 removes in phase 2. No keep file copies a reason.

| Kind | Why it stays |
|---|---|
| a line of `docs/releasing/` | `## Rule changes` carries its change, and the settle writes it (G3) |
| a test's pin on a `docs/releasing/` line a rule change changes, such as the table row `tests/text/test_the_rules_claude_md_names_have_one_home.py` quotes | the settle changes the pin with the line it pins, as step 8 of `skills/settle/SKILL.md` *The settling session's procedure* states, and `chain_check.py` names it at the pull request |
| a line of another work item's directory under `agentory/threads/` | a record of that work item, which states its own moment and leaves with its directory at the settle |
| a `merged:` in `skills/settle/scripts/settle.py`'s messages and the case that pins one | it says which pull requests merged, and is no label (*Readers of the number*) |
| a fixture or an eval scaffold naming a `release/v…` branch | the name is an example branch or a past release's ref, and nothing reads a number from it (*Readers of the number*) |
| a history sentence naming a past release branch, such as *the branch `release/v0.3.0` shipped as 0.2.0* | it states a past release, which `tests/behaviour/test_release_hygiene.py` and `tests/behaviour/test_the_contributor_has_a_procedure.py` keep as history |
| a line of a test that reads a numbered name to refuse it, such as `RELEASE_BRANCH = re.compile(r"release/v\d+\.\d+\.\d+")` in `tests/behaviour/test_the_contributor_has_a_procedure.py` | the refusal of a concrete numbered branch in a loaded file stands |
| `skills/verify/scripts/broad_gate.py:505`, `skills/implement/orchestration.md:410`, the convention line *Scope* item 8 writes, and the `BRANCH_SHAPES` entry of `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` that pins that sentence whole | each names `release/vX.Y.Z` as one shape a repository may use, and the pin changes only with the sentence it pins |

## Rule changes

- change
  file: docs/releasing/branch-and-release.md
  section: Cutting a release
  from: **The version moves at the start of a release, in the first pull request into `release/vX.Y.Z`.** The branch is cut with its version already named, the version of its milestone `release: X.Y.Z`, and nobody installs from a release branch, because the marketplace clone tracks `main`. Moved at the end, the version would need a pull request of its own, because the `release` ruleset takes no direct push and has no bypass actor, and that pull request would be one more wait at the end of every release. The party that writes the changelog fragment of the release's first work item moves it in the commit that adds the fragment: the last phase's crafter where a crafter builds the work item, and the orchestrator where the session does. Which work item carries the move is the orchestrator's choice (`skills/implement/orchestration.md` *Orchestrator: how the work is routed*), and every later pull request into the branch leaves it. What holds a release whose first pull request did not move it is
  to: **The version moves at the end of a release, in the last pull
    request into `release/next` before the release pull request opens, to
    the number the release's commit subjects read.** A number written
    before the work is a prediction kept beside the tree, so the number is
    read when the release is cut (*Work accumulates on a release branch*
    below). The `release` ruleset takes no direct push and has no bypass
    actor, so the move is a pull request: the settle's, where the release
    settles, and otherwise one the orchestrator opens that moves the
    version alone, titled `chore:`, whose commit carries
    `IADD-Routing: no work item`. A work item's pull request leaves the
    version alone. Nobody installs from `release/next`, because the
    marketplace clone tracks `main`. What holds a release whose last pull
    request did not move it is
- change
  file: docs/releasing/branch-and-release.md
  section: Cutting a release
  from: The release's theme follows it, the first sentence of its milestone's description with a leading `Purpose:` left out; a milestone that cannot be read leaves the note without one and never fails the job. A summary read from the pull requests merged into `release/vX.Y.Z` follows:
  to: The release's theme follows it, the first sentence of the body of
    the release pull request whose merge commit the tag names. For a note
    of fragments, a body that cannot be read leaves the note without one
    and never fails the job; a note of settles alone, whose changes are
    that body, carries none. A summary read from the pull requests whose squash commits the
    tag's range holds, each named by the `(#N)` its subject ends with,
    follows:
- change
  file: docs/releasing/branch-and-release.md
  section: Work accumulates on a release branch
  from: So `main` moves once per release, and work collects on a branch cut for that release.
  to: So `main` moves once per release, and work collects on one
    integration branch, `release/next`, which carries no number.
- change
  file: docs/releasing/branch-and-release.md
  section: Work accumulates on a release branch
  from: main ──cut──▶ release/vX.Y.Z ──cut──▶ feature branches
  to: main ──cut once──▶ release/next ──cut──▶ feature branches
- change
  file: docs/releasing/branch-and-release.md
  section: Work accumulates on a release branch
  from: | `main` | `release/vX.Y.Z` | cut a branch | — |
  to: | `main` | `release/next` | cut a branch, once | — |
- change
  file: docs/releasing/branch-and-release.md
  section: Work accumulates on a release branch
  from: | `release/vX.Y.Z` | a feature branch | cut a branch | — |
  to: | `release/next` | a feature branch | cut a branch | — |
- change
  file: docs/releasing/branch-and-release.md
  section: Work accumulates on a release branch
  from: | a feature branch | `release/vX.Y.Z` | **squash** | *Squash and merge* |
  to: | a feature branch | `release/next` | **squash** | *Squash and merge* |
- change
  file: docs/releasing/branch-and-release.md
  section: Work accumulates on a release branch
  from: | `release/vX.Y.Z` | `main` | **3-way merge** | *Create a merge commit* |
  to: | `release/next` | `main` | **3-way merge** | *Create a merge commit* |
- remove
  file: docs/releasing/branch-and-release.md
  section: Work accumulates on a release branch
  from: | a hotfix branch | `main` | **3-way merge** | *Create a merge commit* |
- change
  file: docs/releasing/branch-and-release.md
  section: Work accumulates on a release branch
  from: The last two rows are one rule: **anything reaching `main` is a merge commit.** A hotfix squash costs nothing only while no round record names its commits, and that is a condition nobody should have to check at the merge button, so the ruleset does not offer the choice.
  to: **Nothing reaches `main` but the release pull request from
    `release/next`, as a merge commit.** An urgent fix squashes into
    `release/next`, and the release is cut then. A branch merged into
    `main` beside it puts a version move on `main` that `release/next`
    does not hold, and the next release pull request then conflicts on
    `plugin.json`: a squash records no parent, so no pull request into
    `release/next` can resolve it (#1671).
- change
  file: docs/releasing/branch-and-release.md
  section: Work accumulates on a release branch
  from: No workflow can therefore commit the version to a release branch, which is why the version moves in the release's first pull request.
  to: No workflow can therefore commit the version to `release/next`,
    which is why the version moves in a pull request into it.
- change
  file: docs/releasing/branch-and-release.md
  section: Work accumulates on a release branch
  from: **`release/vX.Y.Z` is cut from `main`.** Not from the previous release branch, and not from a long-lived branch that outlives its release. An accumulation branch that survives a release has to be brought back to `main` afterwards, and nothing enforces that.
  to: **`release/next` is cut from `main` once, and never again.** The
    release pull request merges its tip into `main`, so after the merge
    `main` holds everything `release/next` held, and the next release's
    range, read from their merge base, holds only what squashed in after.
    Nothing has to be brought back, because nothing reaches `main` but the
    release pull request.
- change
  file: docs/releasing/branch-and-release.md
  section: Work accumulates on a release branch
  from: **The release branch merges into `main` as a merge commit**, carrying no commit of its own, because the version moved in the release's first pull request.
  to: **`release/next` merges into `main` as a merge commit**, carrying no
    commit of its own, because the version moved in the last pull request
    into it.
- change
  file: docs/releasing/branch-and-release.md
  section: Work accumulates on a release branch
  from: Feature pull requests write their entry to `agentory/threads/<work-item-id>/changelog.md` and leave `plugin.json` alone, except the release's first, which moves it. The hygiene workflow asks for the moved version only when the base is `main`, where it holds a release whose first pull request did not move it.
  to: Feature pull requests write their entry to
    `agentory/threads/<work-item-id>/changelog.md` and leave `plugin.json`
    alone. The hygiene workflow asks for the moved version only when the
    base is `main`, where it holds a release whose last pull request did
    not move it, and one that moved it to a number its subjects do not
    read.
- change
  file: docs/releasing/branch-and-release.md
  section: Work accumulates on a release branch
  from: **A closing keyword does nothing when the base is `release/vX.Y.Z`.**
  to: **A closing keyword does nothing when the base is `release/next`.**
- remove
  file: docs/releasing/branch-and-release.md
  section: Work accumulates on a release branch
  from: The base is what decides this, not the kind of branch. A hotfix taken straight into `main` has its `Closes #N` fire, so a hotfix that goes to `main` writes the keyword and gets the close. What follows is about everything that goes to the release branch first, which is nearly everything.
- change
  file: docs/releasing/branch-and-release.md
  section: Work accumulates on a release branch
  from: **The version is named at the cut, a `feat:` ships in the planned minor whose goal it shares, and the prefix is never lowered to fit the number.** A release's milestone, `release: X.Y.Z`, names the version before its first work item starts, and the branch is cut as `release/vX.Y.Z` for it. A release that carries a `feat:` is a minor, and every other prefix fits a patch; `skills/commit-pr-convention/SKILL.md` *Commit messages* says which change takes which prefix. A planned minor is a category with one goal, which its milestone's description states (`docs/releasing/issues-and-milestones.md` *A milestone answers when, and takes three shapes*), and the `feat:`s that share that goal ship together in it, so one minor is not made for each `feat:`. A `feat:` lands in a milestone when an issue titled `feat:` is filed into it or moved into it, or when a pull request takes `feat:` where its issue had another prefix. When it lands in a milestone numbered as a patch, its issue moves to the planned minor whose goal it shares. Where no planned minor shares its goal, or the work that follows needs it in effect before that minor ships, that milestone and every later planned `release:` milestone are renamed one step forward in one act instead, each keeping the step it had from the milestone before it, and every description is rewritten for the new numbers. A rename made because the work that follows needs the `feat:` sooner states its grounds in the renamed milestone's description: the work item that needs it, and why the minor that shares its goal ships too late. A `feat:` already squashed onto a patch's branch stays in that release's range, because the release pull request's reading counts it after a revert as well, so its repair is the same rename. A release branch already cut is cut again under the new name from the old one, and the new branch's first pull request moves `plugin.json` to the new version. Until a branch is cut under a name, the planned milestones' names follow their goals, and a regrouping renames them in one act, back as well as forward, with every description rewritten. Once a branch is cut, its name is never pulled back: a minor that carries no `feat:` ships as the minor it was named, because the branch, the `merged:` labels and `plugin.json` already carry that name. The release pull request refuses a patch-numbered release whose own commit subjects carry a `feat:`, and names each one. The reading is exact.
  to: **A release takes its number when it is cut, from what merged, and
    the prefix is never lowered to fit the number.** A `feat:` among the
    commit subjects the release brings to `main`, read from the merge base
    of `main` and the release pull request's head, makes the release the
    next minor of the version `main` holds, and their absence makes it the
    next patch; `skills/commit-pr-convention/SKILL.md` *Commit messages*
    says which change takes which prefix. The prefix is each pull
    request's own judgment and a script reads it exactly, so no person
    approves the number: asking one at every release is the costliest step
    `skills/core/SKILL.md` *The first value: efficient development through
    the IADD process* names. A major is the owner's word alone: a release
    pull request that moves the major, to a version whose minor and patch
    are 0, is not read against the subjects and says so. The release pull
    request refuses a `plugin.json` moved to another version than the one
    read, and names the number and each `feat:` subject. The reading counts
    the one spelling `feat:`, and names a subject whose first word is
    `feat` spelt otherwise as not read. A reverted squash stays in the
    range, so a reverted `feat:` still makes a minor. No milestone and no
    branch carries a number before the cut, so nothing is renamed when a
    `feat:` lands.
- change
  file: docs/releasing/issues-and-milestones.md
  section: A milestone answers when, and takes three shapes
  from: | `release:` | the work going out in that version | closed when the version ships |
  to: | none: the goal, named by what it builds | the work planned toward one goal, which ships in whichever release it has merged into when that release is cut | closed when its last issue closes |
- change
  file: docs/releasing/issues-and-milestones.md
  section: A milestone answers when, and takes three shapes
  from: `release:` milestones carry the version's release date as their due date, and are closed when the release reaches `main`. An open milestone with a past due date reads as overdue, which is the tracker's way of saying a release shipped and nobody closed its milestone.
  to: **A planned milestone is named by its goal and never by a version
    number**, because a release takes its number only when it is cut
    (`docs/releasing/branch-and-release.md` *Work accumulates on a release
    branch*). An issue keeps its milestone whichever release ships it. A
    title holding a number is a prediction kept beside the tree, renamed
    by hand whenever a `feat:` lands. A `release: X.Y.Z` milestone on the
    tracker is a release that shipped under the rule before #1671, and
    stays as its record. A goal milestone is closed once its last issue
    closes.
- change
  file: docs/releasing/issues-and-milestones.md
  section: A milestone answers when, and takes three shapes
  from: **No number caps a release: whoever places an issue in a `release:` milestone judges whether the release has grown past what its description can make clear.**
  to: **No number caps a milestone: whoever places an issue in a goal
    milestone judges whether it has grown past what its description can
    make clear.**
- change
  file: docs/releasing/issues-and-milestones.md
  section: A milestone answers when, and takes three shapes
  from: An issue that does not have to be in effect before the next work item starts then moves to a later `release:` milestone, and a `feat:` moves only where `docs/releasing/branch-and-release.md` *Work accumulates on a release branch* sends it.
  to: An issue that does not have to be in effect before the next work
    item starts then moves to a later goal's milestone.
- change
  file: docs/releasing/issues-and-milestones.md
  section: A milestone answers when, and takes three shapes
  from: A `release:` milestone is still the pool a release is cut from rather than the release itself, `backlog:` below is still the unscheduled pool, and nothing schedules from either: the one thing that reads a milestone checks a cut release against its pool and never decides what goes into one.
  to: A goal milestone is still a pool and not a release, `backlog:` below
    is still the unscheduled pool, nothing schedules from either, and no
    script reads a milestone.
- change
  file: docs/releasing/issues-and-milestones.md
  section: A milestone answers when, and takes three shapes
  from: **A scheduled release milestone's description states the release's purpose and the grounds for the order its issues sit in**, and grounds belonging to one ticket sit on that ticket. A minor's purpose names the one goal its `feat:`s share, and a patch's purpose says it builds no `feat:`, so whether a `feat:` shares a minor's goal is judged against something written, by whoever files or moves it (`docs/releasing/branch-and-release.md` *Work accumulates on a release branch*). No label or field holds the goal, and no script reads it. So "what is in 1.2.3, and why in that order" is answered without opening a file. The number is illustrative, for the reason *A rolling log is titled after the version it rolled from* gives below.
  to: **A goal milestone's description states the goal and the grounds
    for the order its issues sit in**, and grounds belonging to one ticket
    sit on that ticket. No label or field holds the goal, and no script
    reads it. So "what is this goal, and why in that order" is answered
    without opening a file, and what a release shipped is its note.
- change
  file: docs/releasing/issues-and-milestones.md
  section: A label answers *what it is about*, and survives the move
  from: **`merged: X.Y.Z` goes on earlier inside that same release**, at the squash onto the release branch:
  to: **`merged: next` goes on earlier inside that same release**, at the
    squash onto `release/next`:
- remove
  file: docs/releasing/issues-and-milestones.md
  section: One thing reads a milestone, and it can stop a release
- change
  file: docs/releasing/issues-and-milestones.md
  section: A label says a ticket is already in, before the release ships
  from: **An issue a pull request into a release branch claimed carries `merged: X.Y.Z` before the release ships.**
  to: **An issue a pull request into `release/next` claimed carries
    `merged: next` until the release ships.**
- change
  file: docs/releasing/issues-and-milestones.md
  section: A label says a ticket is already in, before the release ships
  from: `.github/scripts/label_merged_on_release_branch.py` runs on a push to `release/*` and puts `merged: X.Y.Z` on every issue the arriving pull requests claimed, creating the label the first time. One query answers *what is already in*: `gh issue list --milestone "release: X.Y.Z"`, and the merged ones carry the label.
  to: `.github/scripts/label_merged_on_release_branch.py` runs on a push
    to `release/*` and, where the branch is `release/next`, puts
    `merged: next` on every issue the arriving pull requests claimed,
    creating the label the first time. One query answers *what is already
    in*: `gh issue list --label "merged: next"`. The label carries no
    number, because the number is read only when the release is cut.
- change
  file: docs/releasing/issues-and-milestones.md
  section: A label says a ticket is already in, before the release ships
  from: **The labels accumulate and are never removed**, one per release. Deleting one deletes it from every issue that ever carried it, which falsifies the record it was created to leave.
  to: **`merged: next` comes off an issue when the release closes it**,
    taken off by the close-issues workflow as `size: now` is, so the label
    names only what is in and not yet shipped. The `merged: X.Y.Z` labels
    of the releases before #1671 stay where they are: deleting one deletes
    it from every issue that ever carried it, which falsifies the record
    it was created to leave.
- change
  file: docs/releasing/issues-and-milestones.md
  section: A label says a ticket is already in, before the release ships
  from: The gate above recomputes what the release carries from the branch itself and never asks the labels,
  to: The release check, `.github/scripts/release_completeness_check.py`,
    recomputes what the release carries from the branch itself and never
    asks the labels,
- change
  file: docs/releasing/issues-and-milestones.md
  section: A label says a ticket is already in, before the release ships
  from: a label naming a release the issue is not in **fails**, because that is always a hand-edit or a squash subject that lost its `(#N)` and one command repairs it,
  to: a `merged: next` on an issue the release does not carry **fails**,
    because that is a hand-edit, a squash subject that lost its `(#N)`, or
    a label the last release's close did not take off, and one command
    repairs each,
- change
  file: docs/releasing/issues-and-milestones.md
  section: An issue is titled like a commit
  from: Who retitles an issue whose pull request takes another prefix is `skills/commit-pr-convention/SKILL.md` *Commit messages*, and where a `feat:` filed into a milestone numbered as a patch moves is `docs/releasing/branch-and-release.md` *Work accumulates on a release branch*.
  to: Who retitles an issue whose pull request takes another prefix is
    `skills/commit-pr-convention/SKILL.md` *Commit messages*, and no
    milestone moves for it, since a release takes its number when it is
    cut.
- change
  file: docs/releasing/issues-and-milestones.md
  section: Reconstructing a missing milestone
  from: The signal is the tag, not the branch. For a closed issue with no milestone,
  to: The signal is the tag, not the branch or the milestone. For a closed
    issue, whose goal milestone names no release,
- change
  file: docs/releasing/release-checklist.md
  section: Before starting
  from: Every work item of the release is squash-merged into `release/vX.Y.Z`
  to: Every work item of the release is squash-merged into `release/next`
- change
  file: docs/releasing/release-checklist.md
  section: Before starting
  from: **The milestone `release: X.Y.Z` holds what this release is actually carrying, and nothing else.** Every open issue in it that is not shipping moves to another milestone now, a planning act that needs no code. Left, the release pull request goes red when it opens: `release_completeness_check.py` refuses while the milestone claims an open issue the release branch does not carry, and names each one, at the worst moment to do the planning.
  to: **`plugin.json` on `release/next` moves to the number the release's
    commit subjects read, in the last pull request into it**: the
    settle's below where the release settles, and otherwise one that moves
    the version alone (`docs/releasing/branch-and-release.md` *Cutting a
    release*). After `git fetch origin`,
    `HEAD_SHA=origin/release/next REPO=<owner>/<repo> python3 .github/scripts/release_completeness_check.py`
    prints the number. A release holds what merged when it is cut, so no
    issue moves between milestones first.
- change
  file: docs/releasing/release-checklist.md
  section: The release pull request
  from: gh pr create --base main --head release/vX.Y.Z \
  to: gh pr create --base main --head release/next \
- change
  file: docs/releasing/release-checklist.md
  section: The release pull request
  from: **The orchestrator opens the release pull request once the last pull request into `release/vX.Y.Z` has merged,
  to: **The orchestrator opens the release pull request once the pull
    request that moves the version has merged into `release/next`,
- change
  file: docs/releasing/release-checklist.md
  section: The release pull request
  from: since `main` stays where the release branch was cut unless a hotfix moves it.
  to: since `main` stays where `release/next` last merged into it, and
    nothing else moves it.
- change
  file: docs/releasing/release-checklist.md
  section: The release pull request
  from: runs `tests` once, on the tree the release ships, and what no pull request into `release/vX.Y.Z` runs answers once:
  to: runs `tests` once, on the tree the release ships, and what no pull
    request into `release/next` runs answers once:
- change
  file: docs/releasing/release-checklist.md
  section: The release pull request
  from: and the `hygiene` workflow's version and milestone steps.
  to: and the `hygiene` workflow's version step and release check.
- change
  file: docs/releasing/release-checklist.md
  section: The release pull request
  from: A defect that only the ubuntu 3.14 or the macOS leg meets is fixed by a pull request into `release/vX.Y.Z`, which the release pull request's next run reads.
  to: A defect that only the ubuntu 3.14 or the macOS leg meets is fixed
    by a pull request into `release/next`, which the release pull
    request's next run reads, and whose push the number is read at again.
- change
  file: docs/releasing/release-checklist.md
  section: The release pull request
  from: `gh pr list --base release/vX.Y.Z --state open` lists no pull request; a settle's pull request closes no issue, so only this command sees it. And the release pull request's own milestone check exits 0 and prints its `M (open in 'release: X.Y.Z')` line, run as `python3 .github/scripts/release_completeness_check.py` with `HEAD_BRANCH=release/vX.Y.Z`, `HEAD_SHA=origin/release/vX.Y.Z` and `REPO` set to what `gh repo view --json nameWithOwner --jq .nameWithOwner` prints. Exit 0 alone does not read the moment: the script also exits 0 when the branch name is not a release name and when no milestone of that title exists, and then prints a line saying so in place of the `M` line. That check fails the release pull request while the milestone claims an issue the branch does not carry, and names each one. An issue it names that no branch is building is the milestone box of *Before starting*, left undone. Where it fails for another reason, a patch carrying a `feat:` or a label on an issue the branch does not carry, its `::error::` line names the repair.
  to: `gh pr list --base release/next --state open` lists no pull request;
    a settle's pull request closes no issue, so only this command sees it.
    And the release check exits 0 and prints the number its subjects read
    beside the version `plugin.json` holds, run as
    `python3 .github/scripts/release_completeness_check.py` with
    `HEAD_SHA=origin/release/next` and `REPO` set to what
    `gh repo view --json nameWithOwner --jq .nameWithOwner` prints. Where
    it fails, its `::error::` line names the repair: a `plugin.json` moved
    to a number the subjects do not read, or a `merged: next` label on an
    issue the branch does not carry. A pull request squashed into
    `release/next` while the release pull request is open ships with it.
- change
  file: docs/releasing/release-checklist.md
  section: The release pull request
  from: "$(git describe --tags --abbrev=0 origin/main)..origin/release/vX.Y.Z" \
  to: "$(git describe --tags --abbrev=0 origin/main)..origin/release/next" \
- change
  file: docs/releasing/release-checklist.md
  section: What a release pull request is held to
  from: from the release's merge until the next release's first pull request moves the version, the running version is one that has already shipped, and a tag is what says so.
  to: on `release/next`, until the release's last pull request moves the
    version, the running version is one that has already shipped, and a
    tag is what says so.
- change
  file: docs/releasing/release-checklist.md
  section: After the merge
  from: the push did not move `plugin.json`'s version, which the release's first pull request owed,
  to: the push did not move `plugin.json`'s version, which the release's
    last pull request into `release/next` owed,
- change
  file: docs/releasing/release-checklist.md
  section: After the merge
  from: Where the job log says the pull requests could not be listed, the note went out as the theme line and the fragments alone, and for a range of settles alone as the theme line and the release pull request's body alone. One `gh release edit` repairs either.
  to: Where the job log says one of the release's pull requests could not
    be read, the note went out with no summary of the pull requests: the
    theme line and the fragments, or for a range of settles alone the
    release pull request's body with no theme line. One `gh release edit`
    repairs either.
- change
  file: docs/releasing/release-checklist.md
  section: After the merge
  from: Leave the `merged: X.Y.Z` labels where they are. They accumulate, one per release, and that is deliberate: deleting a label deletes it from every issue that ever carried it, which falsifies the record the label was created to leave.
  to: The close-issues run takes `merged: next` off each issue it closes.
    Leave the `merged: X.Y.Z` labels of the releases before #1671 where
    they are: deleting a label deletes it from every issue that ever
    carried it, which falsifies the record the label was created to leave.
- change
  file: docs/releasing/release-checklist.md
  section: After the merge
  from: Local `release/vX.Y.Z` and `main` fast-forwarded.
  to: Local `release/next` and `main` fast-forwarded.
- remove
  file: docs/releasing/release-checklist.md
  section: After the merge
  from: - [ ] The next release branch is cut from `main`, not from this one, named for the version its milestone `release: X.Y.Z` carries, and its first pull request moves `plugin.json` to that version.
- change
  file: docs/releasing/release-checklist.md
  section: After the merge
  from: **The milestone `release: X.Y.Z` is closed once the close-issues run has closed its issues, by `gh api -X PATCH repos/<owner>/<repo>/milestones/<number> -f state=closed`.** Nothing else closes it: `.github/scripts/close_issues_on_release.py` closes each issue and leaves the milestone open with none in it, which reads as a release still in flight.
  to: **Each goal milestone the close-issues run left with no open issue
    is closed, by
    `gh api -X PATCH repos/<owner>/<repo>/milestones/<number> -f state=closed`.**
    Nothing else closes it: `.github/scripts/close_issues_on_release.py`
    closes each issue and leaves the milestone open with none in it,
    which reads as a goal still in progress.
- change
  file: docs/running/what-a-script-gates.md
  section: The checks
  from: the body's closing keywords by GitHub's own grammar; `plugin.json`; the milestone through `gh`; commit subjects' `(#N)` and their `feat:` prefix in that one spelling; the head branch's version; two files
  to: the body's closing keywords by GitHub's own grammar; `plugin.json`
    at the base and at the head; commit subjects' `(#N)` and their `feat:`
    prefix in that one spelling; the `merged: next` label through `gh`;
    two files

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the milestone reading, its arms `M \ D` and `D \ M`, its `M` line and its missing-milestone warning | `.github/scripts/release_completeness_check.py#milestone_titles`, `#open_in_milestone`, `#judge`, `#main` | no milestone names a release before its cut, so no milestone states what a release should carry: the release is what merged (*Scope* item 2) |
| the head-name skip and the `HEAD_BRANCH` input | `.github/scripts/release_completeness_check.py#main`, and the `.github/workflows/hygiene.yml` step that runs it | the number is read from the base's and the head's `plugin.json`, so the check needs no name, and a pull request into `main` from any head is judged by the one reading. Where `frame/questions.md` Q2 is answered with a shape that keeps a hotfix route, the `L \ D` arm alone is judged only for a head of `release/next` |
| the patch refusal and the rename repair it names | `.github/scripts/release_completeness_check.py#judge_feat` | the refusal of a `plugin.json` moved to another number than the one read (*Scope* item 1) |
| the mapping from a branch name to a version and a milestone title | `.github/scripts/label_merged_on_release_branch.py#version_of`, `#milestone_title`, `RELEASE_BRANCH` | one constant for `release/next` and one for `merged: next` (*Scope* item 3) |
| the theme read from a milestone | `.github/scripts/publish_release_note.py#milestone_description`, `MILESTONE_TITLE`, `PURPOSE_LABEL` | the first sentence of the release pull request's body (*Scope* item 5) |
| the base and head names the note lists by | `.github/scripts/publish_release_note.py#merged_pulls`, `#release_pull_body` | the tag's range and the merge commit (*Scope* item 5) |
| the cases of what goes above: the milestone arms, the head shapes and the missing milestone marked `a-release-is-judged-under-its-two-names`, the mapping, the milestone theme | `tests/github/test_release_completeness_check.py`, `tests/github/test_label_merged_on_release_branch.py#Test_version_of`, `tests/text/test_a_release_cannot_ship_an_untrue_milestone.py#test_the_head_shape_reaches_the_script_rather_than_the_guard`, `tests/github/test_publish_release_note.py` | the cases of *Scope* items 1, 3 and 5. The marker's check line stands in a section a pending `remove` with no `from` takes out, so `agentic rules --check` excuses it until the settle (G14) |
| the sentence that one numbered release branch is open at a time, and the listing that finds it | `CONTRIBUTING.md` *Opening a pull request* | the branch's one name, `release/next` (*Scope* item 7) |
| the rename procedure, the milestone check's section, the hotfix route (the default of `frame/questions.md` Q2) and the box that cuts the next release branch | `docs/releasing/branch-and-release.md` *Work accumulates on a release branch*, `docs/releasing/issues-and-milestones.md` *One thing reads a milestone, and it can stop a release*, `docs/releasing/release-checklist.md` *After the merge* | `## Rule changes` above, written at the settle |

Framed 2026-11-28 by framer, before the build.
