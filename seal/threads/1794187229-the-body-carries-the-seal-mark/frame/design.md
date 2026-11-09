# Design: 1794187229-the-body-carries-the-seal-mark

## Grounding

The tree as read at `857a7356`.

| Policy clause | What it fixes for this work |
|---|---|
| G1. `skills/core/SKILL.md` *Judgment is not licence to skip a party*, the row *No pull request without a seal*, held by `chain_check.py`'s guarantee arm, which reads `Verdict: sealed` at HEAD (read) | The body is where the seal shows to a reader of the pull request, and no arm reads it. The reader of the body joins the check that holds this row, so the row has one holder. |
| G2. `skills/core/SKILL.md` *The rule a mechanism is kept against*: a script holds a gate only on a fact it reads exactly, and carries no list of spellings (read) | The fact is a line-for-line comparison of the body with what `seal pr-body` composes at HEAD, through `skills/code-review/scripts/pr_body.py#_check`, which the sealer already runs. The arm reads nothing else of the body and judges no wording. |
| G3. `CONTRIBUTING.md` *What a change to a gate must carry* (read) | The failure direction, the prompt budget, what the change removes and what it reads are stated in this design under *Scope*, *Removes* and *Data & interfaces*, and the pull request copies them from here. |
| G4. `skills/code-review/scripts/pr_body.py` module docstring, #1297 and #1204: the mark is written between the heading and the fold where `seal/config.md`'s `Pull request seal mark` row reads `yes` and `guarantee.md` reads `sealed` at HEAD, and `--check` composes it the same way (read) | The arm composes with the mark, so a body sent before the seal differs from the composition on the mark's line and on nothing else. |
| G5. `docs/forms/the-guarantee.md` *The guarantee*, the mark paragraph: the orchestrator runs `seal pr-body` once more after it commits a `sealed` guarantee (read) | That sentence stays as the act. This work adds the reader that holds it, and the paragraph gains the sentence naming that reader (*Rule changes*). |
| G6. `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*: run `seal pr-body` once more after the guarantee is committed, open the pull request with that file, and send a later body with `gh api -X PATCH` (read) | The acts stay. The section gains one sentence on what a red body arm asks: run `seal pr-body` again and send the file, and no sealer runs for it, since the body is not a record. |
| G7. `.github/workflows/hygiene.yml` `types:` holds `edited`, for the issue-claims step; `templates/setup/hygiene.yml` `types:` lacks it (read) | A body edit is no commit, so without `edited` the arm never reads a body sent after the pull request opened. The template gains the type; the repository's comment on it names both readers. |
| G8. `skills/code-review/scripts/chain_check.py#pull_request_state` reads `pull_request.draft` from the file `GITHUB_EVENT_PATH` names; GitHub's `pull_request` payload carries `pull_request.body` beside it (read) | The arm reads the body from the payload the check already opens. No `gh` call, no `env:` line and no new workflow step. |
| G9. `skills/implement/SKILL.md` *3. The SDD file set*, the `pr.md` row, and `skills/code-review/orchestration.md`: `pr.md` is committed before the first round, or before the broad run where no round runs; `agents/sealer.md` step 2 withholds where `seal pr-body --check` exits other than 0 (read) | Every work item sealed at HEAD has a `pr.md`, so the arm's composition has its first part. A missing `pr.md` is a refusal the sealer would already have withheld on. |
| G10. `gh api graphql` over `userContentEdits` of #1446 to #1451 (executed): each was edited between 2026-11-09T01:16:46Z and 01:17:01Z, 0.1 to 1.5 hours after opening; #1412, #1416, #1431, #1435 and #1436 carry no edit. The issue body states the first bodies carried no mark (read, the owner's finding) | The record of what the arm would have caught: every pull request of 0.36.0, and none of the five earlier ones. |
| G11. `git clone --no-local` of this worktree, `git fetch` of `refs/pull/<N>/head` for the eleven pull requests of G10, and each pull request's own `skills/code-review/scripts/pr_body.py <item> --body <its body from gh pr view --json body> --check` at its head commit (executed): exit 0 for all eleven | Every body as GitHub holds it now is what its `seal pr-body` composes at the head commit, so the arm passes every body the orchestrator repaired, and a body of GitHub's round-trips through the comparison. |
| G12. The body of #1451 with its mark line and the blank line under it removed, checked the same way (executed): exit 1, `refused: 1451.nomark.md:13: lacks ``, a fixed line` | The arm refuses a body sent before the seal. The refusal names a blank line and not the mark, because `pr_body.py#_check` names the first line of an inserted run alone and the differ aligned the blank. *Scope* item 2 fixes the naming. |
| G13. The body of #1451 with every line end turned to `\r\n`, checked the same way (executed): exit 0; `lib/blocks.py#gfm_lines` strips `\r\n` | A body GitHub returns with CRLF ends compares equal, so the arm normalises nothing. |
| G14. `time` of one `--check` over #1451's body (executed): 0.13 s wall; `gh run view --json jobs` of the four `hygiene` runs the body edits of 01:16:59Z to 01:17:08Z started (executed): 9 to 12 s each | The cost per pull request: a fraction of a second inside a job that already runs, and one `hygiene` job per body edit. |
| G15. The same four runs ended `failure`, each refusal reading `HEAD does not descend from` a commit of the branch (executed, `gh run view --log-failed`) | An `edited` event on a merged pull request re-runs the check against a tree the branch's commits are not in, and the red gates nothing. This is a limit of `edited` as it stands today in this repository, stated and not guarded. |
| G16. `templates/setup/hygiene.yml` header: in local mode nothing under `seal/` is committed, so every step examines nothing and passes; `skills/core/SKILL.md` *Judgment is not licence to skip a party*: before the pull request, and in local mode, the four rows are held by `agents/sealer.md` step 1 and by the orchestrator (read) | In local mode the body is held as the four rows are: by the sealer's `seal pr-body --check` at step 2 and by the orchestrator's run after the seal. This work builds nothing for local mode. |
| G17. `hooks/hooks.json` ships a `Stop` hook and a `SessionStart` hook and no other; #1416 is titled *the plugin directory refuses every command hook, and every hook this plugin ships is one* (read) | No hook can intercept `gh pr create`, so a wrapper command around it would hold nothing (*plan.md* Alternatives). |
| G18. `docs/running/what-a-script-gates.md` *The checks*: the `chain_check.py` row and the `seal pr-body --check` row (read) | Both rows change under *Rule changes*: the check gains a reader, and the sealer's check gains a second caller. |
| G19. The `## Rule changes` of the unsettled designs under `seal/threads/` (read): 1794178394 changes the `seal rules --check` row of the same table; the others touch no section this design changes | No order is owed between this design's rule changes and another's. |
| G20. `gh issue view 1452 --json comments` (executed): no comment. The spawn carried no line on the comments | Nothing of the issue is outside its body. |

## Scope

The pull request's check reads the pull request's body against what
`seal pr-body` composes at HEAD, so a body sent before the seal, or one that
drifted from the records, fails a ready pull request. The items are five:

1. `skills/code-review/scripts/chain_check.py` gains an arm, `body`. Where
   the file `GITHUB_EVENT_PATH` names holds `pull_request.body`, the arm
   composes, for the one judged work item that is not retired, the body
   `seal pr-body` would write at HEAD: `pr.md`, the heading, the mark where
   the row and the guarantee give one, and the records' copy. It compares the
   payload's body with that composition through the function item 2 names,
   and each differing line is a refusal at the body's line. A ready pull
   request fails on it; a draft prints it. Where the payload holds no body
   field, which a run with no payload, `--worktree` and `seal gate`'s own run
   under `--sealing` share, the arm names the body as not read and decides
   nothing. Under `--sealing` a difference is a notice, since the guarantee
   the mark stands on is not written yet. Where the pull request carries more
   than one judged work item holding a `pr.md`, the arm names the body as not
   read for each, because one body is one work item's.
2. `skills/code-review/scripts/pr_body.py` exposes the composition and the
   comparison as one function that `main --check` and the arm both call, so
   the body is read by one code path at the sealer and at the pull request.
   Its refusal for a run of inserted or deleted lines names every line of the
   run, so a body lacking the mark is refused naming the mark line (G12).
3. `templates/setup/hygiene.yml` `types:` gains `edited`, with a comment
   stating that a body edit is no commit and that the `edited` payload
   carries the new body. `.github/workflows/hygiene.yml`'s comment on
   `edited` names the arm beside the issue-claims step.
   `tests/text/test_ci_gives_the_checks_what_they_need.py` pins `edited`
   wherever a workflow runs `chain_check.py`, as it pins the two draft events.
4. The sentences that stood on the old fact are rewritten in place:
   `chain_check.py`'s docstring counts and names the arm; `pr_body.py`'s
   docstring limit on a body edited after the pull request opens says who
   reads it now; `skills/core/SKILL.md`'s row *No pull request without a seal*
   names the body in its *Held by* cell; `skills/code-review/orchestration.md`
   *Orchestrator: the pull request opens once the sealer seals* says what a red
   body arm asks (G6). The policy root's sentences change through *Rule
   changes*.
5. Cases, each seen red before it is planted: in
   `tests/skills/test_chain_check.py`, a ready pull request whose payload body
   lacks the mark fails on the mark's line; a body equal to the composition
   passes; a body a records line drifted from fails at that line; a draft
   prints and exits 0; a payload with no body field, `--worktree` and
   `--sealing` each name the body as not read or as a notice; two judged work
   items with a `pr.md` are named as not read. In `tests/skills/test_pr_body.py`,
   the refusal for a body lacking the mark and its blank line names the mark
   line. Each case of the arm carries `@pytest.mark.rule` with the marker the
   *Rule changes* check line names.

Out of scope, each with its ground:

- A workflow step that writes the mark into the body: it needs
  `pull-requests: write` where the template declares `contents: read`, it
  writes into a body the sealer audited, and every drift but the mark stays
  unread (*plan.md* Alternatives).
- A command that composes the body and opens the pull request in one step,
  or a hook on `gh pr create`: G17.
- Local mode: G16.
- A pull request carrying more than one judged work item with a `pr.md`: the
  arm names the body as not read (item 1). One work item per pull request is
  the flow `skills/code-review/orchestration.md` describes, and a shape
  outside it gets a limit sentence and no guard.
- An `edited` event on a merged pull request: G15. The red run gates nothing
  and this work adds no condition for it.
- A re-run of an old workflow run: GitHub replays the event the run began
  with, body and all, as `.github/workflows/hygiene.yml`'s comment on `edited`
  already states. The arm reads that body.
- The sealer's `seal pr-body --check` at step 2 stays: in local mode it is the
  one reader of the body (G16), and in shared mode it catches a hand-edited
  body before the seal, where the repair costs no pull request run.
- The version: #1443 moved it to 0.36.0.

The failure direction, for `CONTRIBUTING.md` *What a change to a gate must
carry*: the arm blocks more. A wrong deny, a correct body refused, costs one
`seal pr-body` run and one `gh api -X PATCH`, or one push, and no person. A
wrong allow is the state the record in G10 shows. The arm puts no question in
front of a person. Platform: `hygiene` runs on `ubuntu-latest`, and the
suite's new cases run on every leg of `tests`.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. A body sent before the seal | Given a shared repository whose `Pull request seal mark` row reads `yes`, a work item whose `guarantee.md` reads `sealed` at HEAD, and a ready pull request whose body `seal pr-body` wrote before the guarantee existed / When `hygiene` runs `chain_check.py` / Then the check exits 1 with one refusal at the body's line, reading `lacks` and the mark line, and no other refusal | the case of *Scope* item 5 on the mark; the next pull request this repository opens through the chain |
| S2. The body the orchestrator sent after the seal | Given S1's repository and a body `seal pr-body` wrote after the guarantee was committed / When the check runs / Then the arm prints nothing and the check exits 0 | the case of *Scope* item 5 on the equal body; G11 |
| S3. A drifted body | Given S2's body on GitHub and a later commit that changed a line the copy holds, or an edit made in the browser / When `synchronize` or `edited` runs the check / Then the check refuses at the first differing line, naming the body's line and the record's line as `pr_body.py#_check` does | the case of *Scope* item 5 on drift |
| S4. A draft | Given S1's body on a draft pull request / When the check runs / Then the refusal prints and the check exits 0 | the case of *Scope* item 5 on a draft |
| S5. No body to read | Given a run with no payload, a run under `--worktree`, or `seal gate`'s run under `--sealing` / When the check runs / Then the arm names the body as not read, or under `--sealing` prints a difference as a notice, and the exit code is the other arms' | the cases of *Scope* item 5 on the three runs |
| S6. The row off | Given a repository whose row is absent, and a body carrying the mark / When the check runs / Then the mark's line is refused as a line the records do not give, since the composition holds no mark | `pr_body.py#seal_mark`'s row reading, already pinned in `tests/skills/test_pr_body.py`, and the arm's equal-body case run with the row absent |
| S7. Local mode | Given a repository whose `seal/` root sits under the common git directory / When the check runs / Then nothing is declared, nothing is read, and the body is held by the sealer's step 2 and the orchestrator | G16; `templates/setup/hygiene.yml` header |
| S8. Two work items | Given a pull request whose own commits declare two work items each holding a `pr.md` / When the check runs / Then the arm names the body as not read for each and refuses nothing for it | the case of *Scope* item 5 on two items |
| S9. A user's repository | Given a repository whose `hygiene.yml` was written by `seal pr-checks install` from the release carrying this work / When a body is edited / Then `edited` runs the check and the arm reads the new body | `tests/text/test_ci_gives_the_checks_what_they_need.py`'s pin on the template |

## Data & interfaces

- `skills/code-review/scripts/chain_check.py`: a reader of the payload's
  `pull_request.body`, beside `pull_request_state`, answering the text or
  that the field is absent, and where it read it. GitHub sends `null` for an
  empty body; the arm reads `null` as an empty body, which the comparison
  refuses at `pr_body.py#split` for having no heading line. The arm runs in
  `main` after the guarantee arm, over the declarations judged, and prints
  through `reader.annotate` as every arm does. A GitHub annotation names a
  file of the checkout, and the body is no file: which path the annotation
  carries is the work's (`frame/questions.md` Q1).
- `skills/code-review/scripts/pr_body.py`: one function taking the work
  item's directory, the body's text and the repository root, composing as
  `main` does with `seal_mark`, `read_item` and `read_own`, and returning the
  causes `_check` raises as `Refused`; `main --check` reads the file and calls
  it. `pr_body.py` loads `chain_check.py` by path at import, so
  `chain_check.py` loads `pr_body.py` inside the arm's function and never at
  module level.
- The composition reads the checkout, as `read_item` does. In CI the checkout
  is the pull request's merge commit, the tree the guarantee arm already
  reads HEAD as. Locally the arm runs only where a payload is present, so the
  difference between HEAD and the working tree has no reader there.
- `templates/setup/hygiene.yml`: `types:` reads
  `[opened, synchronize, reopened, edited, ready_for_review, converted_to_draft]`.
  The `permissions:` block stays `contents: read`: the payload is a file of
  the runner.
- The user's installed workflow is pinned to a release and clones the plugin
  at that tag, so a repository whose `hygiene.yml` predates this work runs
  no arm until `seal pr-checks remove` and `seal pr-checks install`, or a
  hand edit of the `types:` line and the tag. `seal pr-checks` reports the
  pinned release.

## Rule changes

- change
  file: docs/checks/the-pull-request-check.md
  section: What the check reads at the pull request
  from: the sealer's guarantee, the `Seal-Routing` trailers of the pull
    request's own commits
  to: the sealer's guarantee, the pull request's body where the run's event
    payload holds it, the `Seal-Routing` trailers of the pull
    request's own commits
- add
  file: docs/checks/the-pull-request-check.md
  section: What the check reads at the pull request
  to: **Where the run's event payload holds the pull request's body, a ready
    pull request passes only where that body is what `seal pr-body` composes
    at HEAD for the one judged work item the pull request carries: its
    `pr.md`, the heading, the seal mark where the `Pull request seal mark`
    row reads `yes` and the work item is sealed at HEAD, and the records'
    copy.** The check reads the body from the file `GITHUB_EVENT_PATH`
    names, the file it reads the draft state from, and compares it through
    the function `seal pr-body --check` compares with, so the sealer and the
    pull request read the body by one code path. Each differing line is
    refused at the body's line, naming the record's line or the fixed line
    the composition gives there. A body written before the sealer's verdict
    differs on the mark's line alone, and the refusal names that line. Where
    the payload holds no body, as a run outside CI, `--worktree` and the run
    of `seal gate` under `--sealing` do, the body is named as not read and
    nothing is decided on it; under `--sealing` a difference is a notice.
    Where the pull request carries more than one judged work item holding a
    `pr.md`, the body is named as not read for each, since one body is one
    work item's. The workflow runs on `edited`, because a body edit is no
    commit and the `edited` payload carries the new body. It errs where the
    payload is not the body GitHub shows: a re-run of an old run replays the
    body the run began with, and an `edited` event on a merged pull request
    runs the check against a tree the branch's commits are not in, where the
    red gates nothing. In local mode nothing is declared, and the body is
    held by the sealer's `seal pr-body --check` and by the orchestrator's run
    after the seal.
    check: body-is-what-pr-body-composes
- change
  file: docs/forms/the-guarantee.md
  section: The guarantee
  from: The orchestrator runs
    `seal pr-body` once more after it commits a `sealed` guarantee, and that
    run changes no copied line, because the copy reads no `guarantee.md`.
  to: The orchestrator runs
    `seal pr-body` once more after it commits a `sealed` guarantee, and that
    run changes no copied line, because the copy reads no `guarantee.md`. The
    pull request's check reads the body against what `seal pr-body` composes
    at HEAD, so a body sent before that run fails a ready pull request on the
    mark's line (`docs/checks/the-pull-request-check.md` *What the check reads
    at the pull request*).
- change
  file: docs/running/what-a-script-gates.md
  section: The checks
  from: `seal/parity.md`'s `Baseline commit` | refuses at its line a block
    line that does not parse, and a required block that is absent; names each
    file under `trail/rounds/` it did not read,
  to: `seal/parity.md`'s `Baseline commit`; the pull request's body, from the
    run's event payload, against what `seal pr-body` composes at HEAD |
    refuses at its line a block line that does not parse, a required block
    that is absent, and a line of the body that is not what `seal pr-body`
    composes; names the body as not read where the payload holds none or the
    pull request carries more than one judged work item with a `pr.md`; names
    each file under `trail/rounds/` it did not read,
- change
  file: docs/running/what-a-script-gates.md
  section: The checks
  from: | `seal pr-body --check` | the sealer | the body file against the
    records | withholds | none |
  to: | `seal pr-body --check` | the sealer, before its verdict; the pull
    request's check, through the same function | the body against `pr.md`,
    the records and the mark the row and the guarantee at HEAD give |
    withholds at the sealer; refuses at the pull request | none |

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the limit sentence *A body edited on GitHub after the pull request opens is read by nobody.* | `skills/code-review/scripts/pr_body.py` module docstring, *Limits* | rewritten in place: the pull request's check reads it where the workflow runs on `edited`, and nobody reads it in local mode (G16) |
| the comment sentence *`edited` is here for the issue-claims step below, which reads the pull request body.* | `.github/workflows/hygiene.yml`, the comment above `types:` | rewritten in place to name the body arm beside the issue-claims step (G7) |

No mechanism goes. The arm adds a reader of a fact nothing read (G1), so
there is no earlier reader of the body to retire. The sealer's step 2 check
stays as local mode's one reader and as the catch before the seal, and the
orchestrator's run after the seal stays as the act the arm holds (G5, G6,
G16). What the arm costs is G14's: a fraction of a second in a job that
already runs, and one `hygiene` job per body edit. What it would have caught
is G10's: every pull request of 0.36.0.

Framed 2026-11-09 by framer, before the build.
