# Implementation Plan: #1204, two config rows show the seal mark on the pull request body and the release note

## Technical context

Every coordinate is at `09d7e5c8f` in this worktree (read unless labelled).

- **`pr-body`'s composition.** `skills/code-review/scripts/pr_body.py#read_item`
  (`:248-267`) reads the changelog, the plan, the gate record, `gaps.md`,
  `questions.md`, the phase records and the round records, and no
  `guarantee.md`. `#_composed` (`:436-483`) builds the part below the
  heading: `below` opens at `:454` with a blank line, the fold and its
  summary, and every line that has no source is a fixed one. The mark is a
  fixed line placed before `FOLD` in that list, so `--check` (`#_check`,
  `:537-563`) compares it as it compares every other line. The module
  already loads `chain_check.py` as `CHAIN` (`:102-104`), which carries
  `FIELDS`, `follows` and `CLOSING_RECORDS`, and `routing.py`'s `optin` as
  `OPTIN` (`:120`), which resolves the `seal/` root.
- **How the stamp reads the guarantee.** `seal_stamp.py#_guarantee_read`
  (`:1145-1155`) reads it with `chain.FIELDS.read(text, chain.FIELDS.GUARANTEE)`,
  takes the last block, and `#_sealed_by` (`:1158-1160`) compares
  `FIELDS.verdict_word(block)` with `FIELDS.SEALED`. `pr-body` reads it the
  same way. The block's `target:` field carries the commit and the base,
  as the groups `commit` and `base` of `hooks/lib/fields.py:207`.
- **The condition the pull request's check asks.** `chain_check.py#guarantee`
  (`:1646-1692`) calls `follows(root, sha, base, item, only=CLOSING_RECORDS)`
  (`:955-986`), which answers None where the commit is HEAD or every later
  commit of the branch touches only `trail/gate.md` and `guarantee.md`
  under the work item. In local mode no commit touches the work item, so
  the answer is None only at HEAD. `pr-body` asks `follows` with the root
  of the repository it runs in, and the work item as `seal/threads/<name>`.
- **The config reader.** `hooks/lib/config.py#config_text` and
  `#config_value` (`:390-470`) give `(value, refusal)` for one row.
  `release_seal.py#module` (`:73-75`) loads a tree module by path at first
  use, and every failure ends in the published note and an exit of 0
  (`#main`, `:534-552`).
- **The release seal.** `release_seal.py#seal_release` (`:467-531`) refuses
  before any write, uploads, then edits. `publish_release_note.py#table`
  and `#sealed_header` (`:627-663`) build the header. The row's read goes
  after the header guard (`:507-513`) and before the upload, so a run that
  will not edit uploads nothing under either answer.
- **The python floor and the tests' layout.** `tests/hooks/test_launch.py`
  holds every script to the floor `hooks/lib/launch.py` states, and
  `bin/seal layout --check tests` holds where a test module sits. Earlier
  work items of this release lost a broad run or CI to each (the
  orchestrator's finding), so each phase names both.
- **The rule changes were probed** (executed 2026-11-02, in a
  `git clone --no-local` of this worktree under the scratchpad, removed
  after): `rule_changes.py#parse` read this design's section with no error
  and no unread line, and `apply_op` placed #1153's seven operations and
  then this design's three, each `placed`.

**The failure scenario of the chosen approach, six months on.** The mark's
address depends on the plugin's repository. Made private, deleted, or
renamed twice so that GitHub's redirect from the first name lapses, every
pull request body in every repository that turned the row on shows a broken
image, and nothing in those repositories can repair it: the bodies were
written once. The same follows a deleted tag. A second, smaller one: a
reader who sees no mark on a body has no line telling them why, because the
lines `pr-body` prints go to the orchestrator's terminal and not to the
body.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1 The mark where the row reads `yes` and the guarantee is sealed at HEAD or only the closing records follow; the orchestrator runs `seal pr-body` once more after it commits the seal | One more command per sealed work item. A guarantee edited on disk and not committed is read as it stands on disk, so in shared mode the mark can stand before the commit that the check reads. That is outside the flow, where the sealer writes and the orchestrator commits at once. | Chosen: it is the issue's condition, read the way the pull request's check reads it, and it drops the mark from a body rewritten after a repair until the repair is sealed |
| A2 The mark where the newest block reads `sealed`, whatever commit it names | After a post-PR repair, `orchestration.md`'s stated limit has the orchestrator rewrite the body and `PATCH` it before the sealer runs again. The body then carries the mark over a HEAD nobody sealed. | Rejected |
| A3 The mark wherever the row reads `yes`, and the meaning left to the check's guarantee arm | A pull request whose guarantee arm fails, or one patched mid-repair, shows the mark beside a red check. The issue's *Done when* asks for the mark only under a `sealed` guarantee. | Rejected |
| A4 The image addressed by the plugin's manifest, `<repository>/raw/v<version>/<icon>` | The plugin's repository leaves public view or its tag goes, and every body breaks (*Technical context*). A version with no tag shows a broken image until the tag exists. | Chosen: each body shows the icon of the version that wrote it, the address is under `github.com`, which GitHub's renderer keeps as written (executed), and the code holds no host |
| A5 The release asset `releases/download/v<version>/seal.png` | It exists only where this repository's `seal` job ran with its row on; a release whose job warned has no asset. #1153 measured release assets served as `application/octet-stream` with `content-disposition: attachment`. | Rejected |
| A6 The image committed into the user's repository and addressed there | Every user tree gains a file the plugin writes, and a pull request body resolves no relative path, so the address would still be absolute and, in a private repository, readable only by a reader who is signed in. | Rejected |
| A7 The icon at the default branch, unpinned | A redraw of the icon changes the mark on every body already written, so an old body no longer shows what sealed it. | Rejected |
| A8 Ship the release-note step to users, through `templates/setup/` or `seal pr-checks install` | `publish_release_note.py` and `release_seal.py` read this repository's release process: a milestone's `Purpose:` line, `release/vX.Y.Z` branches, `chain: capped` labels, the fragment layout and the broad gate's recorder at the tag (`docs/branch-and-release.md` *Cutting a release*). A user's repository keeps none of them, so a shipped job would warn on every run or need settings of its own, which is a second product. | Rejected. The structure kept is the release workflow as this repository's own; its premise was checked: `templates/setup/` ships no release workflow (executed `ls`) |
| A9 With the release row off, `seal` returns early and the note keeps `publish`'s header | The row names the image, and the early return would also take away the suite's counts and the review chain's results that #1153 put in the note. | Rejected for the one-cell results table |
| A10 Document `Release note seal mark` in `docs/branch-and-release.md` alone, not in the template | `docs/one-root-by-lifetime.md` says the rows that exist are documented in `templates/setup/config.md`, and this repository's `seal/config.md` says the same in its comment. A row missing there is one a reader of this repository's config cannot look up. | Rejected. The template documents it with the sentence that nothing outside this repository reads it |
| A11 A refused or unread row exits 2, as `seal gate` does | A row written twice would stop `seal pr-body`, so the body, the sealer's check and the pull request, over a picture. | Rejected for naming the row and leaving the mark off |
| A12 The mark at the top of the body, above the orchestrator's part | `pr-body` keeps the part above the heading byte for byte (`pr_body.py:19-24`); writing there makes it a second writer of the orchestrator's text. | Rejected for the line under the heading |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1, 6 and 7 for `Pull request seal mark`; items 2, 3 and 5; item 8 for `pr_body.py` | The new cases of `tests/skills/test_pr_body.py` for S1 to S5, each seen red before its code; S3's case shown red with the `follows` condition alone removed, and S4's `Yes` case with the exact `yes` comparison alone case-folded. `tests/text/test_the_settings_have_a_front_door.py` with `ROWS` gaining the row (S9). The modules that read a path the phase changed, `tests/test_censuses.py`, `tests/hooks/test_launch.py` and `tests/behaviour/test_the_sealer_guarantees.py` among them, and `bin/seal layout --check tests`, in one command. The rule changes parse (S11) at `seal chain-check`. | `a566ad6b2` |
| 2 | *Scope* items 1, 6 and 7 for `Release note seal mark`; item 4; item 8 for `release_seal.py`, `publish_release_note.py` and `publish-release.yml` | The new cases of `tests/github/test_release_seal.py` for S6 and S8, the absent-row case shown red with the row's read alone removed. The case of `tests/github/test_publish_release_note.py` for S7. `tests/behaviour/test_the_release_seal_is_drawn.py`. `tests/text/test_the_settings_have_a_front_door.py` with `ROWS` gaining the row. `tests/test_censuses.py`, `tests/hooks/test_launch.py` and `bin/seal layout --check tests`, in one command. S10 read on the diff. | |

## Operational impact

- No new dependency, environment variable or workflow step. `seal` reads
  one more file at the tag, `seal/config.md`, which the checkout holds.
- A user's repository sees nothing until it adds `Pull request seal mark`
  reading `yes`. Its first marked body is the first one written after a
  `sealed` guarantee is committed under the plugin version that ships this.
- This repository turns both rows on. Its release notes keep the image from
  0.28.0 on. Its pull request bodies carry the mark once a session runs
  `seal` from 0.28.0 or later; this work item's own body is written by the
  installed 0.27.3 and carries none (executed `which seal`).
- Where the squash commit takes the body, the mark line lands in the
  commit message as text, as the fold's tags already do.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-02 | Phase 1's departure is folded into the design's `add`: a base the guarantee names that git cannot resolve puts no mark and is named | `chain_check.py#follows` answers None for an unresolved base, which reads as HEAD, so a stale seal would have carried the mark that S3 forbids; the crafter checked the base first and named the gap, which the frame's sentence did not state | `skills/core/SKILL.md` *The rule a mechanism is kept against* |
