# Feature Specification: 1793226631-every-release-ends-with-a-preparation-pull-request

Issue #1117. Every coordinate below was opened at `4134055a`, the tip of
`origin/release/v0.24.0` this work item's branch was cut from; the branch's
only later commit, `b55c2482`, adds `routing.md` and nothing else. It builds
on #1053 (merged as `f15b3f99`, #1140), whose unsettled `## Rule changes`
are part of the policy in force and are quoted below as the text in force
where they change a sentence this work changes again.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The goal a design is chosen against*: "Verification through an automated workflow is this project's first goal." Issue #1117's body: "asks the owner for nothing per release and nothing once" | No ruleset change, no secret and no command the owner runs. The owner's one act at a release is the merge of the release pull request with *Create a merge commit*. Where a step the issue does not name still asks the owner for something, it is `frame/questions.md` Q2 rather than a silent change |
| `CLAUDE.md` *The rule a mechanism is kept against*: "A fact has one source, and every other place links to it." | The version has one source, `.claude-plugin/plugin.json`, which moves once, at the release's first pull request. A process row is written once, in its work item's `changelog.md`, and the release note renders it. `seal/process/` stops being a second home and goes |
| `CLAUDE.md` *The rule a mechanism is kept against*: "A change rewrites the text it amends in place, and in the same commit removes what stood on the old fact: a check, an exception, a comment, a copy." | Every case, docstring, comment, census entry and agent or skill sentence outside the policy root that states the preparation pull request, the hand-pushed tag as the release's last act, or the process archive is rewritten or removed in the phase that changes what it states (`## Removes`) |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*: the policy root "is the baseline, and a pull request does not edit it" | `docs/release-checklist.md`, `docs/branch-and-release.md`, `docs/issues-and-milestones.md`, `docs/the-record-layout.md` and `docs/the-broad-gate.md` change through `## Rule changes` only. Cases that read those documents keep reading the baseline until the settle, so none of them is edited for a sentence this work removes |
| `docs/branch-and-release.md` *Work accumulates on a release branch*: "Both rulesets require a pull request, so neither branch takes a direct push, and there are no bypass actors" | A workflow cannot write the version into a release branch at the end. Executed on 2026-10-29 with `gh api .../rulesets`: two rulesets, `main` (`deletion`, `required_status_checks`, `non_fast_forward`, `pull_request`) and `release` (`refs/heads/release/**/*`, `non_fast_forward`, `pull_request`), both with no bypass actor, and none whose target is a tag |
| `docs/branch-and-release.md` *Cutting a release*: the note's job "never republishes a release that exists" | A re-run of the tag step on a commit the tag already names publishes nothing twice. `publish_release_note.py#main` prints and exits 0 where a release exists (read, `:671-678`) |
| #1053's `frame/design.md` *Scope*, its first out-of-scope item: "`publish_release_note.py` keeps its environment interface (`TAG`, `REPO`, `GH_TOKEN`, `DRY_RUN`, `GITHUB_OUTPUT`) and its `created` output, so #1117's workflow can run it after creating the tag in the same job; the tag only has to exist in that job's checkout" | The tag step creates the tag remotely and in the job's own checkout, then runs the script unchanged in its interface. `fragments` and `section` are the one picker and the one renderer (read, `.github/scripts/publish_release_note.py:189-242`), so the process rows are read in `section` alone |
| `tests/behaviour/test_a_release_publishes_its_note.py:115-119`: "this fires on a branch push as well; at the push to `main` the tag does not exist yet and the job would have to create it" | The case's reason is the design this work builds: the job creates the tag. The assertion and its docstring are rewritten in the phase that changes the trigger |
| `skills/verify/scripts/broad_gate.py#PARTITION` and `tests/behaviour/test_the_gate_names_every_step_ci_runs.py#test_the_skill_counts_the_steps_with_a_local_answer_and_no_arm` (read) | A new step in `hygiene.yml`'s `release` job moves the count sentence in `skills/verify/orchestration.md`, a file the parallel work item #1111 owns. So this work adds no hygiene step (`frame/questions.md` Q3) |
| `docs/release-checklist.md` *2. Gather, bump*: the process archive paragraph ends `check: none reader: the framer of the next release` | The row's reader stays a framer. `agents/framer.md` step 4 reads the rows where they now are |
| Issue #1117's body, *What the tree allows*: "A tag pushed with `GITHUB_TOKEN` starts no other workflow" | Not run here; it is GitHub's documented behaviour, read from the issue. It is why the tag, the note and the seal run in one workflow run rather than in a run the tag starts |

## Scope

In scope:

1. **The version moves at the start of a release.** `.claude-plugin/plugin.json`
   moves to `X.Y.Z` in the first pull request into `release/vX.Y.Z`, and
   every later pull request into the branch leaves it. The orchestrator moves
   it in the commit that adds that work item's `changelog.md` fragment, so no
   build phase and no review round carries it.
   `skills/implement/orchestration.md` *What the answer writes*, the
   paragraph opening **Which branch the pull request lands on is decided
   with the routing question.** (`:526-533`), says today that a pull request
   into the release branch leaves the version alone; it is rewritten to say
   that where the repository names the version at the release branch's cut,
   as this repository does, the first pull request into the branch moves it.
   The hygiene step *a change to what ships must move the version* is kept
   unchanged: on the release pull request it fails a release whose first pull
   request did not move the version.
2. **For 0.24.0, this work item is the pull request that moves the version.**
   `plugin.json` on `origin/release/v0.24.0` reads `0.23.1` (executed,
   `git show origin/release/v0.24.0:.claude-plugin/plugin.json`), and every
   commit `git log origin/main..origin/release/v0.24.0` lists left it there. The orchestrator moves it to `0.24.0` in the commit
   that adds this work item's fragment.
3. **A way-of-working change records its own process row.** A work item
   whose diff changes `CLAUDE.md`, an `agents/*.md` file or a
   `skills/*/orchestration.md` file ends its `changelog.md` with the line
   `### Process changes` and a table in the shape
   `templates/records/process.md` gives: `| Date | Change | Why | Source |`,
   one row per change. The orchestrator writes it with the fragment.
   `templates/records/process.md` is reshaped from a file's template
   (`# Process changes: <X.Y.Z>`) to that section's template.
4. **The release note lifts the process rows into one table.**
   `publish_release_note.py#section` renders, first, the heading
   `### Process changes`, the table's header and delimiter rows, and every
   row of every fragment's process section, in work item id order and in
   each fragment's own row order, and then the fragments with their process
   sections taken out. With no process row in any fragment it renders what it
   renders today. The heading is plain ASCII: no emoji, so the framer's read
   of the note matches one spelling.
5. **`seal/process/` goes.** Its three files, `0.22.4.md`, `0.23.0.md` and
   `0.23.1.md`, are readable at the tag `v0.23.1`
   (`git show v0.23.1:seal/process/0.23.1.md`; executed, `git ls-tree`
   lists all three there). They are not folded into their releases' notes:
   the publisher never edits a published note, and the owner declined editing
   published notes for #1053 (that work item's `frame/questions.md` Q2). The
   readers go with them: `release_report.py`'s document glob, the census
   entry, the fixtures, the comment, and `agents/framer.md` step 4, which
   reads instead the `### Process changes` table of the latest GitHub Release
   (`gh release view --json body --jq .body`) where the repository publishes
   one, and the same heading in the fragments under `seal/threads/`.
6. **0.24.0's own process rows.** No archive is written for 0.24.0, so its
   rows live in fragments. Six commits on the release branch since `main`
   changed a way-of-working path (executed,
   `git log origin/main..origin/release/v0.24.0 -- CLAUDE.md 'agents/*.md' 'skills/*/orchestration.md'`):
   `f15b3f99` (#1140), `fdfb20d5` (#1137), `5287dd42` (#1120), `7da1a77e`
   (#1119), `c825fd2c` (#1116) and `822d75bb` (#1112). Their work items
   merged before this rule existed, so the orchestrator writes a row for each
   of them that changed the way of working, with this work item's own row,
   in this work item's `### Process changes` table. A commit that only
   corrected words writes no row; that judgment is the orchestrator's at the
   fragment. A 0.24.0 work item merged after this one writes its own row.
7. **The merge to `main` tags and publishes.**
   `.github/workflows/publish-release.yml` fires on a push to `main` as well
   as on a `v*` tag push. A new step in the `publish` job runs
   `.github/scripts/tag_release.py`, which decides and, where it decides to,
   creates the tag; the note step then runs `publish_release_note.py` with
   that tag, and the `seal` job draws for it. The decision is the issue's:
   the push moved `plugin.json`'s version and no `vX.Y.Z` tag exists yet.
   One arm is added, for a re-run: where the tag already names the pushed
   commit, the step passes it on without creating it. Every other push to
   `main` passes on no tag, and the note step and the `seal` job are skipped.
   A tag pushed by hand passes on that tag, as today.
8. **`PREPARATION_RE` goes.** It kept the preparation pull request out of
   the note's list of changes (`publish_release_note.py:376-378`, `:446-452`).
   No such pull request is opened from 0.24.0 on, and the version's pull
   request is a work item's, which belongs in the list.
9. **Every other reader of the preparation or the hand-pushed tag outside
   the policy root** is rewritten in place: the docstrings and header
   comments in `## Removes`, the timer refusal's message in
   `tests/behaviour/test_release_hygiene.py#refusal` with its pin
   (`:470-479`) in the same commit (contract rule 14), and
   `skills/settle/SKILL.md:176`.
10. **The checklist loses its preparation steps**, through `## Rule changes`:
    steps 1, 2, 3 and 4 whole, the tag push in step 6, and every sentence
    that names the preparation commit, branch or pull request. #1053's
    operations on steps 2, 3 and 4 are superseded by the whole-section
    removals here; the settle applies the latest decision of each section.
    The headings that stay keep their numbers, because `*5. The release pull
    request*` and `*6. After the merge*` are cited across the tree, and the
    settle may renumber them with their citations. Two rules that stood in
    the removed steps are kept: the step 3 paragraph on a sweep that walks a
    git listing moves to `docs/the-broad-gate.md`, and step 2b's trailer
    sentence names the `no work item` answer itself, since step 4, which it
    cited, goes. `tests/text/test_the_direct_answer_owes_the_sealers_record.py#test_the_release_checklist_names_the_waiver_as_the_no_work_item_answer`
    reads that phrase in the checklist, and step 2b's new sentence carries it.

How the release carrying this work is cut, 0.24.0:

1. This work item's pull request into `release/v0.24.0` carries the
   workflow, the script, the renderer, the removals, `plugin.json` at
   `0.24.0` and the 0.24.0 process rows. The owner squash-merges it, as he
   does every work item's.
2. The rest of the milestone's work items merge into the branch the same way.
3. The orchestrator opens the release pull request, `release/v0.24.0` into
   `main`, titled `release: 0.24.0 symptoms: <...>`. When it opens it is
   `frame/questions.md` Q1; the default is with this work item's pull
   request, since none is open (executed, `gh pr list --state open` listed
   none on 2026-10-29). Its milestone check stays red while the milestone
   claims an issue the branch does not carry, and goes green on the push
   that merges the last one.
4. The owner merges the release pull request with *Create a merge commit*.
   That is his one act at the release.
5. The push to `main` runs `publish-release.yml` from the merged tree, which
   is the new one: it creates `v0.24.0` on the merge commit, publishes the
   note and draws the seal. `close-issues-on-release.yml` closes the issues
   on the same push, as today.

Out of scope, each with why:

- **A check that refuses a pull request into `release/vX.Y.Z` whose tree
  does not name `X.Y.Z`.** It needs a hygiene step, which edits #1111's file
  (*Grounding*); `frame/questions.md` Q3 asks for it, and the release pull
  request's version step holds the release meanwhile.
- **Deriving the version from commit prefixes**, and **whether a branch can
  be created with a commit of its own under the `release` ruleset**: both are
  out of scope in the issue, and neither is needed once the version moves at
  the start.
- **Folding the three process archives into their published notes**
  (*Scope* item 5).
- **Step 5's release-table read and mutate sweep, and step 6's boxes other
  than the tag push.** The issue names steps 1 to 4 and the tag push; the
  rest is `frame/questions.md` Q2.
- **`CONTRIBUTING.md`'s row "a new version in `.claude-plugin/plugin.json`".**
  It stays true: a contribution into the release branch inherits the moved
  version from its base, and the version step still exits 0 unless the base
  is `main`.
- **`.github/scripts/release_completeness_check.py`, `close-issues-on-release.yml`
  and `roll_flow_measurement_issue.py`'s logic.** Each reads the version or
  the milestone at the push to `main`, where the tree still names the version
  that push shipped. Only the roll's docstring changes (`## Removes`).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 the release is tagged | Given a push to `main` whose `before` commit's `plugin.json` names `1.2.2` and whose pushed commit's names `1.2.3`, and no tag `v1.2.3`; when the tag step runs; then it creates `v1.2.3` on the pushed commit, in the job's checkout and through `gh api -X POST repos/<REPO>/git/refs`, and passes on `v1.2.3` | a case in `tests/github/test_tag_release.py` driving a real `git` repository in `tmp_path` and a fake `gh` on `PATH`, seen red against no script |
| S2 a push that moves no version | Given a push to `main` whose two commits name the same version; when the tag step runs; then it creates nothing, passes on no tag, and its log says the version did not move | a case of the decision function's own |
| S3 a re-run | Given the version moved and `v1.2.3` already names the pushed commit; when the step runs; then it creates nothing and passes on `v1.2.3`, so the note step runs and leaves an existing release as it is | a case of the decision function's own |
| S4 a tag elsewhere | Given the version moved and `v1.2.3` names another commit; when the step runs; then it creates nothing, passes on no tag, and its log names the commit the tag names | a case of the decision function's own |
| S5 a tag pushed by hand | Given a push of the tag `v1.2.3`; when the step runs; then it creates nothing and passes on `v1.2.3` | a case of the decision function's own |
| S6 no earlier commit to read | Given a `before` that is all zeros or that the checkout does not hold; when the step runs; then it creates nothing, passes on no tag, and its log says which | a case of the decision function's own |
| S7 a dry run | Given `DRY_RUN=1` and S1's history; when the step runs; then it prints the tag it would create and the commit, creates none, and passes on no tag | a case in `tests/github/test_tag_release.py` |
| S8 the workflow's shape | `publish-release.yml` fires on `push: branches: [main]` and `push: tags: ['v*']`; its `publish` job runs the tag step before the note step, the note step runs only when the tag step passed on a tag and reads `TAG` from it, the job's outputs are `created` and `tag`, the `seal` job checks out that tag and reads `TAG` from it, and the only scope declared is `contents: write` | `tests/behaviour/test_a_release_publishes_its_note.py#test_the_workflow_fires_on_the_tag_and_writes_one_release_one_asset_one_edit`, rewritten and seen red against the workflow at `4134055a` |
| S9 the note lifts the process rows | Given two fragments, the first with a `### Process changes` table of two rows after its prose, the second with none, and a third whose body is the section alone; when `section` renders them; then the output opens with `### Process changes`, the header and delimiter rows and the two rows, then each fragment under its marker line with no process section, the third fragment's marker line with no body under it | a case in `tests/github/test_publish_release_note.py`, seen red against the script at `4134055a` |
| S10 no fragment carries rows | Given fragments with no process section; when `section` renders them; then the output is what `section` returns at `4134055a` | the existing cases of `section` and of the note, unchanged and green |
| S11 no living text names the removed things | `git grep -n -i -E 'seal/process\|preparation (commit\|branch\|pull request)\|release-prep\|PREPARATION_RE'` outside `docs/`, `seal/threads/` and `docs/experiments/` finds no line; `skills/commit-pr-convention/SKILL.md:124`'s "release preparation", the kind of change a `chore:` prefix names, is the one hit allowed | the grep, run by the crafter at phase 3's close, its hits read by the proofer. No case holds it, because `docs/` names them until the settle |
| S12 every check line resolves | the `check:` lines in `## Rule changes` name files that exist after the build | `bin/seal rules --check` exits 0 at the work item's head, and the rule changes block parses (`seal settle`'s reader at the pull request) |

## Data & interfaces

`.github/scripts/tag_release.py`, new:

- **Environment.** `REF` (`github.ref`), `BEFORE` (`github.event.before`),
  `AFTER` (`github.sha`), `REPO`, `GH_TOKEN`, `DRY_RUN`, and `GITHUB_OUTPUT`
  where the runner sets it. It calls `console.to_utf8()` first, as an entry
  point.
- **The decision.** One function with no I/O takes the ref, the version at
  `BEFORE` (or None), the version at `AFTER`, and the commit the tag
  `v<version at AFTER>` names (or None), and returns the tag to pass on (or
  nothing), whether to create it, and the log line. Its arms are S1 to S6.
- **The reads.** A version is `json.loads` of `git show <sha>:.claude-plugin/plugin.json`.
  A tag's commit is `git rev-parse -q --verify refs/tags/<tag>^{commit}`,
  read from the checkout, which `fetch-depth: 0` fills with every tag.
- **The creation.** `gh api -X POST repos/<REPO>/git/refs -f ref=refs/tags/<tag> -f sha=<AFTER>`,
  a lightweight tag like every tag this repository holds (executed:
  `git cat-file -t v0.23.1` and `v0.22.4` print `commit`), then
  `git tag <tag> <AFTER>` in the job's checkout, so the note step finds it
  without a fetch.
- **Output.** `tag=<tag>` or `tag=` to `$GITHUB_OUTPUT`, through the same
  write-and-ignore shape as `publish_release_note.py#write_output`.
- **Exit codes.** 0 for every decision, a dry run included. 1 where the
  creation was refused, naming the error: the release is then untagged and
  the run says so.

`.github/workflows/publish-release.yml`:

- `on: push: branches: [main]` and `tags: ['v*']`.
- `publish`: checkout with `fetch-depth: 0`; the tag step (`id: tag`); the
  note step (`id: note`, `if: steps.tag.outputs.tag != ''`, `TAG` from
  `steps.tag.outputs.tag`). Outputs `created` and `tag`. No `needs`.
- `seal`: `needs: publish`, `if: needs.publish.outputs.created == 'true'`;
  its checkout takes `ref: ${{ needs.publish.outputs.tag }}` and its drawing
  step reads `TAG` from the same output, since `github.ref_name` is `main` on
  the push this work adds.
- `permissions: contents: write`, unchanged: creating a ref through the API
  needs that scope and no other.

`publish_release_note.py#section`: input and output types unchanged. The
process section of a fragment is the line `### Process changes` and every
line after it up to the next line starting with `#` or the fragment's end;
its rows are the lines starting with `|` after the header and delimiter
rows. Nothing else in the module's interface changes.

`templates/records/process.md`: the line `### Process changes`, a blank
line, the header row, the delimiter row and one placeholder row.

## Rule changes

- remove
  file: docs/release-checklist.md
  section: 0. Before starting
  from: - [ ] No other Claude session is working in this checkout, and the
    editor is not about to pull. An editor's pull can switch the checkout
    to another branch between two commands, and the preparation commit
    lands there. `git status -sb` after every `switch` is the cheap check.
- remove
  file: docs/release-checklist.md
  section: 1. The preparation branch
- remove
  file: docs/release-checklist.md
  section: 2. Gather, bump
- change
  file: docs/release-checklist.md
  section: 2b. Settle what earlier releases left behind
  from: each of its commits carries the trailer `Seal-Routing: no work item`,
    as step 4 shows.
  to: each of its commits carries the trailer `Seal-Routing: no work item`,
    the recorded form of the routing question's `no work item` answer
    (`skills/commit-pr-convention/SKILL.md`).
- remove
  file: docs/release-checklist.md
  section: 3. Verify before committing
- remove
  file: docs/release-checklist.md
  section: 4. Commit, push, open the first pull request
- change
  file: docs/release-checklist.md
  section: 5. The release pull request
  from: Its hygiene checks fail until step 4 is squashed in, by design. Then
    they go green without a push.
  to: **The orchestrator opens the release pull request, and the owner's one
    act at a release is its merge.** The version moved in the release's
    first pull request, so no pull request comes between the last work item
    and this one. The orchestrator opens it with the first work item pull
    request into `release/vX.Y.Z` that finds none open, and leaves it open.
    Its milestone check fails while the milestone claims an issue the branch
    does not carry, by design, and goes green on the push that merges the
    last one.
    check: tests/github/test_release_completeness_check.py
- change
  file: docs/release-checklist.md
  section: What a release pull request is held to
  from: from the preparation commit until the next bump the running version
    is one that has already shipped, and a tag is what says so.
  to: from the release's merge until the next release's first pull request
    moves the version, the running version is one that has already shipped,
    and a tag is what says so.
- remove
  file: docs/release-checklist.md
  section: 6. After the merge
  from: git tag vX.Y.Z <merge commit> && git push origin vX.Y.Z
- change
  file: docs/release-checklist.md
  section: 6. After the merge
  from: The tag push fires `.github/workflows/publish-release.yml`, which
  to: The merge's push to `main` fires `.github/workflows/publish-release.yml`,
    which tags the merge commit `vX.Y.Z` and then, in the same run,
- change
  file: docs/release-checklist.md
  section: 6. After the merge
  from: - [ ] Local `release/vX.Y.Z` and `main` fast-forwarded; the
    preparation branch deleted or left, either is fine.
  to: - [ ] Local `release/vX.Y.Z` and `main` fast-forwarded.
- change
  file: docs/release-checklist.md
  section: 6. After the merge
  from: - [ ] The next release branch is cut from `main`, not from this one.
  to: - [ ] The next release branch is cut from `main`, not from this one,
    named for the version its milestone `release: X.Y.Z` carries, and its
    first pull request moves `plugin.json` to that version.
- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: 2. **A `vX.Y.Z` git tag on the release commit, pushed.**
  to: 2. **A `vX.Y.Z` git tag on the release commit**, which
    `.github/workflows/publish-release.yml` creates when the release
    reaches `main`.
- remove
  file: docs/branch-and-release.md
  section: Cutting a release
  from: git tag vX.Y.Z <release commit> && git push origin vX.Y.Z
- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: **A release pull request that changes what the plugin ships moves the
    version.** `tests/behaviour/test_chain_hooks_hardening.py` binds the
    changelog to whatever `plugin.json` says, and the `hygiene` workflow
    fails a release pull request, one whose base is `main`, that changes
    `skills/`, `agents/`, `hooks/`, `templates/`, `bin/` or
    `.claude-plugin/` without moving the version. The tag is still the
    maintainer's to push; nothing in CI can do it.
  to: **The version moves at the start of a release, in the first pull
    request into `release/vX.Y.Z`.** The branch is cut with its version
    already named, the version of its milestone `release: X.Y.Z`, and
    nobody installs from a release branch, because the marketplace clone
    tracks `main`. Moved at the end, the version needed a pull request of
    its own, because the `release` ruleset takes no direct push and has no
    bypass actor, and that pull request was one more wait at the end of
    every release. The orchestrator moves it in the commit that adds the
    changelog fragment of the release's first work item, and every later
    pull request into the branch leaves it. The `hygiene` workflow fails a
    release pull request, one whose base is `main`, that changes `skills/`,
    `agents/`, `hooks/`, `templates/`, `bin/` or `.claude-plugin/` without
    moving the version, which is what holds a release whose first pull
    request did not move it.
- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: Two different pushes fire two of the acts. The merge to `main` fires
    the close-issues workflow, so the label is created and spent before any
    tag exists. The tag push, the maintainer's last act, fires the note,
    because a note has to name a tag.
  to: The merge to `main` fires every act. It fires the close-issues
    workflow, so the label is created and spent, and it fires the publish
    workflow, which creates the tag and then publishes the note in the same
    run: a note has to name a tag, and a tag a workflow creates with its own
    token starts no workflow of its own. A tag pushed by hand fires the
    publish workflow too.
- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: fires on the `v*` tag push and publishes a note built from the
    release's changelog fragments, titled from the tagged commit's
  to: fires on the push to `main`, and on a `v*` tag pushed by hand. On the
    push to `main` it publishes only where that push moved `plugin.json`'s
    version: it creates the `vX.Y.Z` tag on the pushed commit through the
    GitHub API where no such tag exists, and takes the tag where it already
    names that commit, which is a re-run. It publishes a note built from the
    release's changelog fragments, titled from the tagged commit's
- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: check: tests/behaviour/test_a_release_publishes_its_note.py tests/github/test_publish_release_note.py tests/text/test_the_release_tail_does_not_end_at_the_tag.py tests/behaviour/test_the_release_seal_is_drawn.py tests/github/test_release_seal.py
  to: check: tests/behaviour/test_a_release_publishes_its_note.py tests/github/test_publish_release_note.py tests/github/test_tag_release.py tests/text/test_the_release_tail_does_not_end_at_the_tag.py tests/behaviour/test_the_release_seal_is_drawn.py tests/github/test_release_seal.py
- remove
  file: docs/branch-and-release.md
  section: Work accumulates on a release branch
  from: | the release-prep branch | `release/vX.Y.Z` | **squash** | *Squash and merge* |
- change
  file: docs/branch-and-release.md
  section: Work accumulates on a release branch
  from: The release-preparation commit therefore needs a branch of its own
    and a squash merge, like any other work.
  to: No workflow can therefore commit the version to a release branch,
    which is why the version moves in the release's first pull request.
- change
  file: docs/branch-and-release.md
  section: Work accumulates on a release branch
  from: carrying one commit of its own: the one that moves `plugin.json`.
    Then the tag.
  to: carrying no commit of its own, because the version moved in the
    release's first pull request. The publish workflow then tags the merge
    commit.
- change
  file: docs/branch-and-release.md
  section: Work accumulates on a release branch
  from: and leave `plugin.json` alone. The hygiene workflow asks for the bump
    only when the base is `main`, which is what makes that enforceable.
  to: and leave `plugin.json` alone, except the release's first, which moves
    it. The hygiene workflow asks for the moved version only when the base
    is `main`, where it holds a release whose first pull request did not
    move it.
- change
  file: docs/branch-and-release.md
  section: Work accumulates on a release branch
  from: **The version is provisional until the content settles.** Release
    when the accumulated changes read as one changelog entry, not on a
    commit count, so whether the number is a minor or a patch is known at
    the end, not at the cut. Rename the branch if the answer changes; while
    it is unpushed that costs nothing.
  to: **The version is named at the cut.** A release's milestone,
    `release: X.Y.Z`, names the version before its first work item starts,
    and the branch is cut as `release/vX.Y.Z` for it. A release whose
    content changes the answer, a minor become a patch or a patch become a
    minor, is cut again under the new name from the old branch, and the new
    branch's first pull request moves `plugin.json` to the new version.
- change
  file: docs/issues-and-milestones.md
  section: A label answers *what it is about*, and survives the move
  from: The tag decides, never the changelog: the preparation commit bumps
    the running version and writes its heading in the same commit, so until
    the next bump the running version is one that has already shipped, and
    only its tag says so. The version in the title is a fact rather than a
    prediction: `docs/branch-and-release.md` says whether the next number is
    a minor or a patch is known at the end and not at the cut, so at the
    moment the roll runs the next version is the one thing nobody can name.
  to: The tag decides, never `plugin.json`: a release's first pull request
    moves the running version to one that has not shipped, and from the
    release's merge until the next release's first pull request the running
    version is one that has already shipped, and only its tag says so. The
    version in the title is a fact rather than a prediction: the roll runs
    at the push to `main` that ships a release, when `plugin.json` names the
    version that push shipped.
- change
  file: docs/the-record-layout.md
  section: Every kind of record, at a glance
  from: | The process archive | `seal/process/<X.Y.Z>.md`, one file per
    release, written at its preparation | each file under target | the file
    name, by version |
  to: | The process rows | a `### Process changes` table at the end of a work
    item's `changelog.md` while its work item is open; the release note's
    table of the same name once its release is published | each fragment is
    under target | the repository's releases on GitHub, by tag |
- remove
  file: docs/the-record-layout.md
  section: seal/
  from: | `seal/process/<X.Y.Z>.md` | what one release changed in the way of
    working, and why |
- add
  file: docs/the-record-layout.md
  section: A change writes fragments, never a shared file
  to: **A change to the way of working writes its process row in its own
    fragment.** A work item whose diff changes `CLAUDE.md`, an `agents/*.md`
    file or a `skills/*/orchestration.md` file ends its `changelog.md` with
    the line `### Process changes` and a table in the shape
    `templates/records/process.md` gives: one row per change, holding the
    date, the change, one line of why, and a link to the issue comment or
    commit it came from. The orchestrator writes it with the fragment. A row
    written with its change leaves no write for the end of the release, and
    the next framer reads what the way of working became and why.
    check: none reader: the framer of the next work item
- add
  file: docs/the-record-layout.md
  section: A change writes fragments, never a shared file
  to: **The release note lifts every process row into one table.** Under the
    heading `### Process changes`, above the fragments, the note carries
    every row of every fragment's process section, in work item id order,
    and each fragment follows without its section, so a row is shown once.
    check: tests/github/test_publish_release_note.py
- add
  file: docs/the-broad-gate.md
  section: What the runner owes the person who typed it
  to: **A sweep that walks a git listing judges what remains instead of
    stopping at the first tracked file the disk lacks, and a case whose
    verdict needs the whole corpus says so.** A tree can hold tracked files
    the disk does not have, a removal nothing has staged yet. So a count
    line reading `N passed, M skipped` with reasons naming paths is that
    state rather than something to debug; one appears when the tree is
    mid-edit somewhere a check like that reads, under `docs/`, `skills/`,
    `templates/`, `tests/` or a shipped `.py`.
    check: tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py tests/test_conftest.py

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The three process archives | `seal/process/0.22.4.md`, `seal/process/0.23.0.md`, `seal/process/0.23.1.md` | The tag `v0.23.1` holds all three. New rows land in fragments and the release note (*Scope* items 3 to 5) |
| The template's file heading `# Process changes: <X.Y.Z>` | `templates/records/process.md` | The same file, reshaped to the fragment section `### Process changes` and its table |
| `"seal/process/*.md"` in `DOCUMENTS`, and the docstring lines naming each process archive file | `.github/scripts/release_report.py:24-25`, `:54`, `:180` | No such file remains to measure |
| The case that a process archive is a document row | `tests/github/test_release_report.py:250-267` | It pinned the glob above |
| `"seal/process/"` in `OLD_NAME_RECORDS` | `tests/censuses.py:1056` | No such path remains to exempt |
| The planted `seal/process/0.1.0.md` fixture paths | `tests/test_censuses.py:788`, `:806`, `:926` | They pinned the exemption above |
| The comment naming the process archive's files under `seal/process/` | `tests/text/test_a_record_carries_no_comment.py:18-19` | The comment names `templates/records/process.md` as the fragment section's template. The fixture at `:59-66` keeps planting the file, which still exists |
| Step 4's read of the process archive of the highest version | `agents/framer.md:64-67` | The `### Process changes` table of the latest GitHub Release, and the same heading in the fragments under `seal/threads/` |
| `PREPARATION_RE`, its comment, and the filter in `changes` | `.github/scripts/publish_release_note.py:376-378`, `:446-452` | No preparation pull request is opened. `changes` keeps its sort |
| The assertion that the preparation pull request is not listed, and the fixture pull request `#9` it reads | `tests/github/test_publish_release_note.py:496` and the line that plants `#9` | It pinned the filter above |
| The workflow's trigger as a tag push only, and its pin that no branch is named | `.github/workflows/publish-release.yml:35-37`; `tests/behaviour/test_a_release_publishes_its_note.py:115-119` | S8. The case's other assertions, `publish` with no `needs` among them, still hold |
| The header comment's account of the tag push as the release's last manual act, and its claim that nothing in CI creates a tag | `.github/workflows/publish-release.yml:3-19` | The comment states the push to `main` and the tag step |
| The docstring's account of the tag push as the release's last manual act | `.github/scripts/publish_release_note.py:12-14` | The docstring names both triggers |
| "The tag push fires" in module docstrings | `tests/github/test_publish_release_note.py:5`, `tests/github/test_release_seal.py:3`, `tests/behaviour/test_a_release_publishes_its_note.py:3` | Each names the push to `main` and the hand-pushed tag |
| The release-preparation commit as what moved the version, and the next number being known at the end | `.github/scripts/roll_flow_measurement_issue.py:12-22` | The release's first pull request moves it, and the tree at the push to `main` names the version that push shipped |
| The preparation commit as what bumps the version, in docstrings | `tests/behaviour/test_release_hygiene.py:222-224`, `:246-248`, `:615` | The release's first pull request bumps it |
| "on the release's own preparation commit" in the refusal, and its pin | `tests/behaviour/test_release_hygiene.py#refusal` (`:314`), `:470-479` | The message names the commit that moves the version. The pin moves with it in the same commit |
| "on the preparation branch" | `skills/settle/SKILL.md:176` | "on the settle's branch", which step 2b of the checklist and *A settle is not a work item* already give it |
| "and the version is left alone", for a pull request into the release branch | `skills/implement/orchestration.md:527-529` | The paragraph says the repository's convention decides, and that here the first pull request into the branch moves it |
| The policy root's sentences on the preparation branch, its commit, the process archive and the hand-pushed tag | `docs/` | `## Rule changes` above, written at the settle, never by this pull request |

## Open questions

<none here: each is a row of `questions.md`>

Framed 2026-10-29 by framer, before the build.
