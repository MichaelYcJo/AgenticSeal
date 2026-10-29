# Review round 1: 1793226631-every-release-ends-with-a-preparation-pull-request

target: c3cd08c6 against origin/release/v0.24.0

## Findings

### 1. A shipped skill tells the orchestrator in any repository that its repository names the version when it cuts the release branch

severity: should
location: `skills/implement/orchestration.md:529-533`
evidence: read `skills/implement/orchestration.md:526-540`, `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/frame/design.md:35-40`
verdict: fixed 13b9d759

The rewritten paragraph reads "Where the repository names the version when
it cuts the release branch, as this one does with `release/vX.Y.Z`, the
orchestrator moves the version to that name in the first pull request into
the branch". `skills/implement/orchestration.md` ships with the plugin and
is read by the orchestrator in every repository that installs it. There,
"this one" is the reader's own repository. So an orchestrator in a
repository that moves its version at the release reads that its repository
names the version at the cut, and moves the version in the first pull
request into its release branch. The next sentence of the same paragraph,
"Where the repository moves the version at the release, a pull request into
the release branch leaves it alone", is the branch it should have taken.
The phrase came from the frame: *Scope* item 1 says "as this repository
does", which was true of the frame, because the frame is about this
repository. The skill is not.

The class was enumerated: `git grep -n -E "as this (one|repository) does"`
over `skills`, `agents`, `templates`, `hooks` and `bin` finds this line and
no other (executed). The same sentence also names "that work item's
changelog fragment", which assumes the fragment layout; a repository with one
changelog heading has an entry, not a fragment.

The fix names the branch shape rather than the repository:

```markdown
**Which branch the pull request lands on is decided with the routing
question.** A pull request into the release branch is not a release: its
entry accumulates unreleased. Whether it moves the version is the
repository's convention. Where the repository names the version when it
cuts the release branch, as a branch named `release/vX.Y.Z` does, the
orchestrator moves the version to that name in the first pull request into
the branch, in the commit that adds that work item's changelog entry,
and every later pull request into the branch leaves it. Where the
repository moves the version at the release, a pull request into the
release branch leaves it alone. A pull request into `main` is a release:
the accumulated entries go out under the version, which moves there only
where it has not moved already, and the tag follows the merge. The release
branch is the default. The orchestrator takes `main` when the accumulated
entries read as one release, or when the change is a gate or a hook firing
where it should not, which does not wait for other changes.
```

answer: Fixed as worded above. The sentence now reads "as a branch named `release/vX.Y.Z` does" and "that work item's changelog entry". Every line this branch added to a shipped file (`skills/`, `agents/`, `templates/`, `hooks/`, `bin/`) was swept for a phrase that names the reading repository. The other added lines name "the repository" generically, or name the plugin's own `seal/threads/` layout, so no other line changed. `git grep -n -E "as this (one|repository) does"` over those roots now finds no line, exit 1. `bin/test -q` over the 35 modules naming `orchestration.md` passed, 1059 cases, exit 0.

### 2. The rule change for checklist step 5 says the owner's one act at a release is the merge, but the section keeps the owner's sweep and a check line read "at release preparation"

severity: should
location: `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/frame/design.md:261-274`, `docs/release-checklist.md:194-202`
evidence: read `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/frame/design.md:261-274`, `docs/release-checklist.md:174-202`, `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/frame/questions.md:29`
verdict: fixed 78512510

The rule change for *5. The release pull request* replaces "Its hygiene
checks fail until step 4 is squashed in" with a bold sentence: "The
orchestrator opens the release pull request, and the owner's one act at a
release is its merge." The same section keeps, untouched by any operation in
`## Rule changes`, the paragraph *Each release clears what grew*: "The owner
reads the rows whose seconds or cases grew most since the tag and sweeps
each such module with one `bin/seal mutate` call". That paragraph ends
`check: none reader: the owner at release preparation`. Step 6 also keeps
its boxes for the owner. `frame/questions.md` Q2 leaves those acts with the
owner on its default (a), and (a) words them as "the owner's required act is
the merge, and these read reports that fail nothing". So after the settle,
step 5 would state in one section that the owner has one act and that the
owner sweeps. The settling session writes each section as its latest
decision, and these two sentences cannot both be that decision. The check
line would also name a release preparation that no longer exists; it is the
one sentence in the policy root naming the preparation that no operation of
`## Rule changes` reaches (the grep in `## Probes`).

This finding does not answer Q2. Whether a sweep left to the owner meets the
owner's requirement that a release needs no act of his beyond the merge is a
row of `## Not judged`. The fix states Q2's default as (a) words it, and
renames the check line's reader.

```markdown
- change
  file: docs/release-checklist.md
  section: 5. The release pull request
  from: Its hygiene checks fail until step 4 is squashed in, by design. Then
    they go green without a push.
  to: **The orchestrator opens the release pull request, and the owner's one
    required act at a release is its merge.** The reads below and the boxes
    of step 6 are reports that fail nothing. The version moved in the
    release's first pull request, so no pull request comes between the last
    work item and this one. The orchestrator opens it with the first work
    item pull request into `release/vX.Y.Z` that finds none open, and leaves
    it open. Its milestone check fails while the milestone claims an issue
    the branch does not carry, by design, and goes green on the push that
    merges the last one.
    check: tests/github/test_release_completeness_check.py
- change
  file: docs/release-checklist.md
  section: 5. The release pull request
  from: check: none reader: the owner at release preparation
  to: check: none reader: the owner before the release pull request's merge
```

answer: Fixed by the orchestrator at 78512510, which changes `frame/design.md`'s `## Rule changes` as worded above. The section-5 `to:` now says the owner's one required act is the merge, and that the reads and step 6's boxes are reports that fail nothing. A second change re-points the check line's reader. The block parses, 30 operations and 0 errors, as executed by the orchestrator. This pass did not re-run that parse.

### 3. The 0.24.0 process table leaves out #913's change to how a signer cites the pact, which changes what a framer writes

severity: should
location: `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/changelog.md:14-18`
evidence: executed `git show --format= 7da1a77e -- skills/implement/orchestration.md`, `git grep -n "Pact | Clause | Hash" -- skills templates`, `gh issue view 913 --repo MichaelYcJo/AgenticSeal --json title,state`
verdict: fixed 78512510

`frame/design.md` *Scope* item 6 asks for a row for each of the six commits
that changed a way-of-working path and "changed the way of working", and
excludes "A commit that only corrected words". The orchestrator wrote rows for
#1041 (`fdfb20d5`), #1053 (`f15b3f99`) and this work item, and judged that
#1120, #1119, #1116 and #1112 did not change the way of working. I re-read
each diff on the three paths:

- `822d75bb` (#1112) changes "detracers" back to "describes". It corrects words only, so no row is right.
- `5287dd42` (#1120) removes sentences from five agent definitions that restated contract rules 2, 6, 7 and 9. The rules still bind every agent through the contract, so no act changed, and no row is right.
- `c825fd2c` (#1116) adds to `skills/code-review/orchestration.md` an account of what a `workflow_dispatch` run of `tests` can see. The orchestrator's act, pushing and running `gh workflow run tests`, is unchanged, so no row is right.
- `7da1a77e` (#1119, issue #913) rewrites `skills/implement/orchestration.md` (now `:605-608`). A signer used to cite the clauses it was built against "as pact anchors, in its spec's Grounding". Now it writes "one row each of a `| Pact | Clause | Hash |` table in its `frame/design.md`, the `Pact` cell holding the pact's origin URL". `skills/verify/scripts/pact_check.py:11` and `:212` read that table. This changes what a framer writes into a frame in a repository that signs a pact, and it is not a correction of words. Earlier archives recorded changes of this kind, such as "The record shapes stand in `templates/records/`" (`git show v0.23.1:seal/process/0.23.1.md`).

So #913's change belongs in the table, and the next framer, who reads this
table at its step 4, otherwise learns of it only by reading the skill. The
row names the columns in words, so that no pipe stands inside a cell:

```markdown
| 2026-10-28 | A signer cites each pact clause it was built against as one row of a table with the columns Pact, Clause and Hash in its `frame/design.md`, the Pact cell holding the pact's origin URL; `seal pact` reads the machine-local pact map as a table with the columns Remote and Path, and refuses every line of it that it does not read | The map and the anchor each had a grammar of their own, and the anchor used symbols as syntax | https://github.com/MichaelYcJo/AgenticSeal/issues/913 |
```

The row goes after the 2026-10-28 row for #1041, at `changelog.md:16`.

answer: Fixed by the orchestrator at 78512510, which adds #913's row to this work item's `changelog.md` process table. That commit changes the fragment by one line (read, `git show --stat 78512510`).

## Confirmations

confirms: none
`.github/scripts/tag_release.py#decide` (`:69-111`) makes a tag only where
the push moved the version. The tag-ref arm comes first. Then an unreadable
earlier version, an unreadable pushed version, and an unchanged version each
return `Decision("", False, ...)`. `create` is True only where the two
versions differ and no tag `v<after>` exists. A re-run, where the tag already
names the pushed commit, passes the tag on with `create` False. A tag on any
other commit passes nothing on. `main` (`:191-212`) calls `create` only on
`decided.create`, and writes `tag=` before it exits 1 on a refusal. The
claim in `gaps.md` that `decide` takes two arguments the frame does not name,
the pushed commit and `missing`, holds. S3 and S4 need the first and S6 needs
the second, so this divergence is sound (read).

confirms: none
The workflow does what S8 asks when GitHub evaluates it, not only in the
text the S8 case reads (read, `.github/workflows/publish-release.yml:39-157`).
The `push` block holds both `branches` and `tags`, so a push matching either
starts a run. A push to `main` that is not a release writes `tag=`. The note
step's `if: steps.tag.outputs.tag != ''` then skips it, so
`steps.note.outputs.created` is empty and the seal job's
`if: needs.publish.outputs.created == 'true'` skips that job too. A refusal
exits 1 and fails `publish`, which skips the note step under the implicit
`success()` and skips `seal` through `needs`. A re-run carries the same
`github.event.before` and `github.sha`. Its `fetch-depth: 0` checkout
fetches every tag, so `tag_commit_of` finds the tag the first run made. The
note step then finds the release and writes `created=false`
(`publish_release_note.py:718-725`), and nothing is published twice. The
seal checkout takes `ref: ${{ needs.publish.outputs.tag }}`, which the tag
step created on GitHub before the job ended. A tag `GITHUB_TOKEN` creates
starts no run of its own, so the new trigger cannot run the workflow twice
for one release. The issue states that behaviour; it is not run here.

confirms: none
The S1 to S7 cases and the arms the crafter added pass, and so do the S8 to
S10 cases, the refusal's pin and the skip line's pin. `bin/test -q` over the
51 modules in `## Probes` exited 0 with 2581 passed and 12 skipped. The 12
skip reasons, read with `-rs`, are platform skips and the documented skip
for a script no shipped document names (executed). I did not re-run the
seen-red claims in the phase records. Each one's first assertion fails on the
old text by reading: `branches: [main]` is absent from the workflow at
`4134055a`, and `section` at `4134055a` folds each table into its fragment
(read).

confirms: none
The other three divergences in `gaps.md` hold (read). First, the process
section ends at the next heading through
`unverified_check.py#heading_level`, so a wrapped line that opens `#120)`
does not end it. `split_process` asks it of lines whose fences are not
blanked, and that function's docstring leaves this to the caller. Only a
fence inside a process section could reach this, and the template's section
is one table. Second, `process_shape` reads the heading and header rows from
`templates/records/process.md`, so the template is their one source. Third,
the readers missing from `## Removes` were found and rewritten: the `#9` row
in `tests/github/test_release_seal.py#PULLS`, `test_release_hygiene.py:482`
and `:564`, the docstring of `publish_release_note.py#changes`, the sentence
above `tests/censuses.py#OLD_NAME_RECORDS`, and the docstring of
`test_the_direct_answer_owes_the_sealers_record.py`. Rule 19 asks for each
of these.

confirms: none
Outside the policy root, nothing in the tree still tells a person to push a
tag, open a preparation pull request or read `seal/process/` (executed, in
`## Probes`). The S11 grep found no line. The broader search for a tag push
finds only the hand-pushed tag the workflow still accepts, the
`test_the_release_tail_does_not_end_at_the_tag.py` cases that read
`docs/release-checklist.md` until the settle, and `tag_release.py`'s own
account. `agents/framer.md:63-69` reads the `### Process changes` table of
the latest GitHub Release and the fragments. Inside `docs/`, every sentence
naming the preparation, the archive or the tag push is reached by an
operation of this frame's or #1053's `## Rule changes`. The exception is the
check line in finding 2.

confirms: none
Three of the process rows check out against their sources (executed). The
#1041 row matches `skills/code-review/orchestration.md:78-84` and
`agents/crafter.md:156-158`: the fix pass writes the two lines and commits
neither, and the orchestrator commits the record. It also matches the owner's
choice that #1041's `frame/plan.md` row F records. The #1053 row's "26 of 58"
matches #1053's round 5, where 32 notes held their file and 26 did not. The
#1117 row states this work. `.claude-plugin/plugin.json` reads `0.24.0` at
`c3cd08c6`, the commit that also fills the table, as *Scope* items 2 and 6
assign. Finding 3 is the one candidate left out.

confirms: none
`bin/seal layout --check` exited 0 (161 files read, 0 refused), and
`bin/seal rules --check` exited 0 (all 266 check lines in 55 rule files
hold), so S12 holds at `c3cd08c6` (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether `gh api -X POST repos/<REPO>/git/refs` with the workflow's `GITHUB_TOKEN` creates `v0.24.0`. The merge commit it tags changes `.github/workflows/publish-release.yml` and `hygiene.yml`, and GitHub has refused a ref update by an app token without the `workflows` permission where workflow files change. Whether that refusal reaches a tag created through the API on a commit `main` already holds cannot be run before the merge | `frame/questions.md:31` (Q4), `.github/scripts/tag_release.py:153-179` | the orchestrator, reading `gh run list --workflow publish-release.yml --limit 1` and its log after 0.24.0's merge into `main`; the hand-pushed tag stays the fallback |
| Whether Q2's default (a) meets the owner's standing requirement that a release needs no act of his beyond the merge. Under (a), step 5's release-table read and `bin/seal mutate` sweep and step 6's boxes stay his | `frame/questions.md:29` (Q2), `docs/release-checklist.md:194-202` | the owner, through Q2 |
| Whether the crafter's hand-back labelled the full suite `unverified`. It was not given to this round, and neither `gaps.md` *Not verified* nor the phase records name the suite | `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/gaps.md:19-24` | the orchestrator, who holds the hand-back and runs `seal gate` |
| Earlier rounds: none exist, so no fact was carried and every verdict here was reached in this round | `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/trail/rounds/` | none needed |

## Probes

| Command | Result |
|---|---|
| `bin/test -q` over 51 modules: every `tests/` module that `git grep -l` finds naming `.claude-plugin/plugin.json`, a changed `.github/scripts/` or `.github/workflows/` file, `agents/framer.md`, `seal/process`, `skills/implement/orchestration.md`, `skills/settle/SKILL.md` or `templates/records/process.md`, plus the branch's changed test modules, `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` and `tests/test_censuses.py` | exit 0: 2581 passed, 12 skipped |
| the same run with `-rs` | exit 0. The 12 skips are 8 for a script no shipped document names, 3 Windows or `/proc` readings in `test_worktree_guard.py`, and 1 for a shell that is not `cmd.exe` |
| `bin/seal layout --check` | exit 0: 161 files read, 0 refused |
| `bin/seal rules --check` | exit 0: all 266 check lines in 55 rule files hold |
| the S11 grep of `frame/design.md:181`, outside `docs/` and `seal/threads/` | exit 1, no line |
| `git grep` for tag-push, `git tag`, process-archive and version-bump phrasing outside `docs/` and `seal/threads/` | only the lines `## Confirmations` names |
| `git grep` in `docs/`, `CONTRIBUTING.md` and `README.md` for preparation, process-archive and tag-push phrasing, each hit checked against the `## Rule changes` of this frame and of #1053 | every hit reached by an operation except `docs/release-checklist.md:202` (finding 2) |
| `git log origin/main..origin/release/v0.24.0 -- CLAUDE.md 'agents/*.md' 'skills/*/orchestration.md'` and `git show` of each of the six commits on those paths | six commits; #1119's diff changes what a signer writes (finding 3) |
| `git grep -n -E "as this (one\|repository) does"` over `skills`, `agents`, `templates`, `hooks` and `bin` | one line, `skills/implement/orchestration.md:530` (finding 1) |
| `gh issue view 1117`, `1041`, `1053` and `913` on `MichaelYcJo/AgenticSeal` | bodies read against the rows and *Done when*; #913 is open, and its title names the pact map's retired grammar |
