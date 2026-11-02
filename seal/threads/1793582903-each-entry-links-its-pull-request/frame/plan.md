# Implementation Plan: each entry links its pull request (#1139)

## Technical context

- **The renderer.** `.github/scripts/publish_release_note.py#fragments`
  (`:195-242`) already lists, per fragment, the range's commits that add it
  (`--diff-filter=A`) and reads the body at the newest commit that holds
  it, with `--full-history`. `#section` (`:277-296`) writes
  `<!-- specs/{item} -->` above each body at `:292`. `main` (`:690-747`)
  passes `REPO` to nothing but the `gh` calls. The publish step runs it with
  `TAG`, `REPO` and `GH_TOKEN` set (`.github/workflows/publish-release.yml:84-92`).
- **The settle.** `skills/settle/scripts/settle.py#apply` (`:1215-1260`)
  re-reads the candidates from the tree, keeps a directory whose record
  holds an open row, and removes the rest with `shutil.rmtree`.
  `#merged_pull_requests` (`:264-305`) is the existing shape for asking
  `gh` and raising `Unasked`, and `main` (`:1340-1347`) turns `Unasked`
  into the `UNASKED` sentence and exit 2. In shared mode `survey` gives
  *released* from `git ls-tree` at `--released-at` (`#released`,
  `:216-239`). The list has to be read before the loop's first `rmtree`,
  so that a failure removes nothing.
- **The tests.** `tests/github/test_publish_release_note.py` builds real
  git histories for the fragment cases (`:250-300`, S1 of #1053).
  `tests/skills/test_settle.py` puts a `gh` stub first on PATH for the
  local cases (`:279-360`), and points `settle.GH` at a missing name for the
  not-on-PATH case (`:1592`).
- **Checks named in the spawn.** Two checks cost earlier work items of this
  release a broad run or a round. `tests/hooks/test_launch.py` requires a
  module that a hook-run script newly loads to stand in `ruff.toml`
  `[per-file-target-version]` at py39. Neither the renderer nor `settle.py`
  is hook-run, so the check applies only if the shared reader is put in
  a module that one loads. `bin/seal layout --check tests` checks where
  each test file stands. Both are on every phase's *Verified by*.
- **The design's rule changes parse** (executed 2026-11-02). In a
  `git clone --no-local` of the worktree under the framer's scratch
  directory, `rule_changes.py#parse` read `## Rule changes` as four
  operations with no error and no unread line. Each `from` occurs exactly
  once in its document, with whitespace collapsed. The clone is gone.
- **The failure scenario of the chosen approach, six months on.** A pull
  request title that ends `(#N)` for some other reason is still followed
  by GitHub's own `(#PR)`, and the last number is read. So a wrong number
  needs a commit that adds a fragment and is not a squash merge: a direct
  push, or a release branch merged with a merge commit. The probe found
  none in 54 fragments. Where it happens, the entry links whatever that
  subject's last `(#N)` names, and the settle checks the same number, so
  the two agree on a wrong link and neither catches it. The second risk is
  #1153, which re-renders the note. Were it to drop the link line, every
  settle after it would keep every directory, and S4 to S7 in
  `tests/skills/test_settle.py` would not see it, because they stub the
  note. The link's one source is `section`, and a case in
  `tests/github/test_publish_release_note.py` pins it. #1153's framer reads
  this design.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Read the number from the adding commit's subject, the trailing `(#N)` (chosen) | A commit that adds a fragment and is not a squash merge links a wrong number or none (*Technical context*). Executed: 54 of 54 fragments since #1053 carry a merged pull request's number this way. | Chosen. It is git output, read exactly, at the tag, with no API call, and it is what the issue names. |
| Match the adding commit against `mergeCommit.oid` from the `gh pr list` the renderer already makes | That list can fail. `merged_pulls` then publishes the note without a summary rather than failing, and every entry would lose its link exactly when the summary is lost too. It also needs `mergeCommit` added to the shared field list that `release_seal.py#chain_counts` reads. | Rejected. It adds a dependency on the one call that the note is designed to survive without. |
| Keep the hidden marker beside the new link (keeping the structure) | The marker has had no reader in a script since #1053 (executed `git grep`). Kept, it would become the settle's key, which only this repository's notes carry: a user repository whose notes are GitHub-generated links its pull requests and never carries the marker, so the check would keep every directory there. The premise for keeping it, that something reads it, does not hold. | Rejected. The marker goes from the writer (the issue's Done when), and is read only in notes published before this change. |
| Drop the marker and read only the link in the settle | The seven released work items in the tree at `v0.27.3` would be kept by the first settle that runs under this change, because their note carries the marker and no link (executed). The owner would have to edit a published note by hand to settle work the note already carries. | Rejected. The settle also accepts `<!-- specs/<id> -->`. That reader has nothing left to read once no released directory predates this change, and it goes then (*Operational impact*). |
| Recognise the entry by the fragment's text as a substring of the body | A note edited by hand, GitHub's line-ending normalisation, or #1153's re-render would each make a carried entry read as missing. A user's note never holds fragment text. | Rejected. The URL is one exact string, and a renderer change is unlikely to touch it. |
| Put the check in this repository's own release tooling, a `.github/scripts/` step at checklist 2b, and leave the shipped `seal settle` alone | The removal is `--apply`'s, so a check beside it only advises. A session that skips the step removes the directory anyway. It also departs from the issue's Done when. | Rejected. The check is in `--apply`, scoped so that a repository with no `vX.Y.Z` tag on a candidate never runs `gh` (Q1, Q2). |
| Read the note in the dry run too | The dry run would need `gh` in shared mode, which today never asks it, and a dry run is what a person runs first in a repository with no `gh`. | Rejected. The dry run stays `gh`-free. A directory kept for its note is named by `--apply` with what to do next. |
| Ask `releases/tags/<tag>` once per version, as `publish_release_note.py#release_exists` does | Telling "no release" from "cannot read" means reading the words `Not Found` or `404` in stderr, which is a reading from words. | Rejected. One `--paginate` list answers with JSON, and an absent `tag_name` means no release at that tag. |
| Keep a directory where no note can be read: no version tag, no release at the tag, or no number | A user repository that tags without publishing GitHub Releases, or does not tag, would never settle. In this repository the missing-release shape is already the box at checklist step 6. | Rejected as the default. Q1 puts the choice to the owner. |
| A settle-side copy of the subject reading | Two copies of one fact drift, and the note and the settle would then name different pull requests. | Rejected. One function, imported by both (Q3 is where it lives). |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope items 1, 2 and 3 | `tests/github/test_publish_release_note.py`: S1, S2 and S3, each seen red against the current renderer, and the marker pins rewritten. Also `tests/behaviour/test_a_release_publishes_its_note.py`, `tests/behaviour/test_no_document_names_the_old_roots.py`, `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` (it reads `templates/setup/config.md`'s no-row list), and every test module that reads a changed path. `tests/hooks/test_launch.py` applies where the shared reader lands in a module that a hook-run script loads. `bin/seal layout --check tests`. | |
| 2 | Scope items 4 and 5 | `tests/skills/test_settle.py`: S4, S5, S6, S7 and S8, with S4, S6 and S7's `gh`-not-asked case each seen red. Also `tests/text/test_settle_reads_before_it_removes.py` (the README rows), `tests/behaviour/test_settle_applies_rule_changes_in_place.py`, every test module that reads `skills/settle/` or `templates/setup/seal-README.md`, `tests/hooks/test_launch.py`, `bin/seal layout --check tests`, and `bin/seal rules --check` for any check line the phase writes. | |

## Operational impact

- **`seal settle --apply` in shared mode asks `gh`** wherever a directory
  it would remove has a `vX.Y.Z` tag on its fragment's adding commit. A
  repository with such tags and no working `gh` stops at exit 2, as local
  mode already does (Q2). The token needs only read access to releases.
  The list leaves drafts out, as the note check does.
- **The first settle under this change** reads the notes of `v0.27.3` and
  earlier through `<!-- specs/<id> -->`, and those of `v0.28.0` and later
  through the link. Once a settle leaves no released directory older than
  `v0.28.0`, the marker reader has nothing to read. Removing it is then
  a one-line change that a later work item names. No guard schedules it.
- **The renderer runs from the tagged tree.** `v0.28.0`'s note is the first
  with links, because the publish workflow runs the script at that commit.
- **No new dependency, environment variable or config row.** `REPO`
  already reaches the publish step.
- **Process changes.** None. The diff touches no file that
  `docs/the-record-layout.md` *A change writes fragments, never a shared
  file* names for a process row.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
