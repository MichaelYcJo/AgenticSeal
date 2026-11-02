# Design: #1204, two config rows show the seal mark on the pull request body and the release note

Every coordinate below was opened in the worktree at `09d7e5c8f`, the tip of
`feat/1204-the-seal-mark-is-drawn-only-in-the-terminal`. That branch was cut
from `release/v0.28.0` at `4ab345cba`, which holds #1218 (#1293) and #1153
(#1294). The issue was read with `gh issue view 1204 --json body,comments`
on 2026-11-02 (executed). Its body carries the three comments as the
orchestrator folded them, and the three comments read the same as the body
says.

The surfaces have three writers, and this design names them by job.
`pr-body` is `skills/code-review/scripts/pr_body.py`, run as
`seal pr-body`. `publish` is `.github/scripts/publish_release_note.py`, and
`seal` is `.github/scripts/release_seal.py`. Both run in
`.github/workflows/publish-release.yml`, `seal` after `publish` in the same
run. The mark is the plugin's icon, `.claude-plugin/plugin.json`'s `icon`,
`.claude-plugin/icon.png`.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| The issue's *The direction (owner, 2026-10-31)* and *What the work decides* (executed: `gh issue view 1204`) | Built on. The terminal stamp stays fixed. Each new surface has one row and is off unless the row turns it on. `yes` turns it on, the spelling `routing.md`'s `Automation` row uses. An absent or empty row means off. Any other value is named as not read and leaves the surface off. This repository turns both on. The owner chose two rows over one row holding a list, so this frame adds those two and no third. |
| `skills/core/SKILL.md` *The rule a mechanism is kept against*, and the issue's keep test (read) | The mark catches no defect, so it is weighed by its cost alone. Each row is read by the step that already writes its surface: `pr-body` for the pull request body and `seal` for the note. The design adds no hook, check, label or file beside them. The rule's "names as not read a line … that looks like one of its form's" is how a value other than `yes` is answered. |
| `docs/the-review-record.md` *The stamp*: the stamp "means every party verified the work item, the sealer last", and it is queued "where the reader the pull request's check reads it through refuses none of its lines and its newest verdict block reads `Verdict: sealed`" (read) | The mark on a pull request body means the same thing and reads the guarantee the same way: `hooks/lib/fields.py` through `chain_check.FIELDS`, as `skills/verify/scripts/seal_stamp.py#_guarantee_read` does (`seal_stamp.py:1145-1160`, read). The stamp is drawn once, at the write. A pull request body is rewritten after it opens, by `gh api -X PATCH` after a repair (`skills/code-review/orchestration.md`, the stated limit). So the body also asks that the sealed commit is HEAD or followed only by the closing records, the condition `chain_check.py#guarantee` asks through `chain_check.py#follows` with `CLOSING_RECORDS` (`chain_check.py:163`, `:955-986`, `:1646-1692`, read). |
| `docs/the-review-record.md` *The guarantee*, the paragraph opening "The pull request body opens with the orchestrator's part", and `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* (read) | The orchestrator runs `seal pr-body` after the broad run and before the sealer's spawn. The sealer runs `seal pr-body --check` before it writes its verdict, and withholds where the part below the heading is not what the records give. So the body the sealer checks can hold no mark from that sealer's own run, and the mark arrives on a run after the `sealed` guarantee is committed. That run changes no copied line, because `read_item` reads no `guarantee.md` (`pr_body.py:248-267`, read). The sentence "open the pull request with the body the sealer read" (`orchestration.md:223-224`) changes with it. |
| #1044, as `pr_body.py:8-17` states it: "It copies lines and composes none: no count, no summary, no rewording" (read) | Built on. The mark is one fixed line, built from the plugin's manifest alone, and it carries no record text, no count and no summary. Departed from in one place: `pr-body` now reads `guarantee.md` and the manifest, neither of which it copies. |
| #1218, as `pr_body.py:128-135` and `:470-479` state it (read) | Untouched. The refusal reads copied lines. The mark is a fixed line, and it holds no `details` tag. |
| #832, as `skills/verify/scripts/seal_stamp.py:1-24` states it (read), and the owner's direction that the terminal stamp stays fixed | Built on. No file the stamp runs from changes: `seal_stamp.py`, `seal-mark.txt`, `hooks/sealer-stamp-queue.py`, `hooks/sealer-stamp.py`. |
| #857 and #1174, as `assets/seals/README.md` *The little owl — from 0.25.1* states them (read) | Built on. The page form of the mark is `.claude-plugin/icon.png`, drawn from `assets/seals/owl.svg`, and `seal` copies it byte for byte. The pull request mark shows the same file. Nothing in the drawing changes. |
| #718 and #1153, as `docs/branch-and-release.md` *Cutting a release* and #1153's `## Rule changes` state them (`seal/threads/1793589475-the-note-opens-with-the-owl-and-folds-each-category/frame/design.md`, read) | Built on. `seal` never fails the release. It edits only a note whose `publish` header stands exactly once, and it replaces that header with a table whose first cell is the image and whose second holds the results the stamp states. This work decides only whether `seal` attaches the image and draws that first cell. The policy in force on those sentences is #1153's `to` values, so this design's `from` values below quote them. |
| `docs/one-root-by-lifetime.md` *What the repository decides for itself, and how it is read*: "The rows that exist are documented in `templates/setup/config.md`", and "Every row is reachable from a command that shows the whole file" (read) | Both rows are documented in `templates/setup/config.md`, and `skills/config/SKILL.md` names both. `tests/text/test_the_settings_have_a_front_door.py#ROWS` (`:23-36`, read) lists every row the template ships, and gains the two. |
| `hooks/lib/config.py#config_value` (`:450-470`, read), and `templates/setup/config.md`'s opening, "A command a person runs (`seal fold`, `seal gate`, `seal mode`, `seal pact`) prints the refusal and exits 2" (read) | The one reader of a row. Neither row stops anything. A refused row, written twice or below a line the walk refused, is named and leaves the surface off, and the exit code is unchanged. The grounds are the stamp's "never a reason to stop an edit" (`hooks/sealer-stamp-queue.py:25-27`, read) and #718's rule that the seal never turns the release red. The four commands the template names keep their exit 2. |
| `templates/setup/` holds `claude-md-block.md`, `config.md`, `hygiene.yml`, `pact.md`, `parity.md` and `seal-README.md`, and no release workflow (executed: `ls templates/setup/`) | The release note's image exists only in this repository's own workflow. The row governs that workflow alone, and its documentation says so (`plan.md` *Alternatives considered*, A8). |
| `.claude-plugin/plugin.json` carries `version`, `repository` and `icon` (read) | The mark's address is built from these three fields of the manifest beside the running `pr_body.py`, three directories up, where `pr_body.py:105-107` already finds `.github/scripts/`. The code holds no host. `plugin.json` is read and never edited. |
| Executed 2026-11-02: `curl -sIL` on `<repository>/raw/v0.27.3/.claude-plugin/icon.png` with this repository's address, on the same path under the repository's former name, and on a tag that does not exist (`v9.9.9`) | The address under `github.com` answers 302 to GitHub's raw-file host, which answers 200, `image/png`, 192,647 bytes. The former name answers 301 to the current one and then the same. The missing tag answers 404. |
| Executed 2026-11-02: `gh api -X POST markdown -f mode=gfm -f context=<this repository>` over a heading, the mark's `<img>` line and a `<details>` fold | GitHub's renderer keeps the `<img>` with its `src`, `alt` and `width` as written, wraps it in a link to the same address, and renders the fold after it. A browser drawing it on a real pull request page is not probed here, since that needs a pull request (`questions.md` Q1). |
| `tests/censuses.py:884-891` *real_identifiers* (read) | `github.com` is allowed and GitHub's raw-file host is not. The code builds the address from the manifest and spells no host; the records name the raw-file host in words. |
| Executed 2026-11-02: `which seal` | The installed plugin's `bin/seal`, under its `0.27.3` directory. The orchestrator in this repository runs the installed `seal`, so this work item's own body is written by 0.27.3 and carries no mark. The first body with a mark is written after a session installs 0.28.0. |
| Executed 2026-11-02: `cmp assets/seals/owl.png .claude-plugin/icon.png`, and each file's `IHDR` read with `python3`; both images opened (read) | They differ: `owl.png` is 816 by 336, the terminal stamp's picture beside its panel, and `icon.png` is 512 by 512, the vector seal. The icon shows a round-headed owl with ringed eyes and a scalloped breast on an olive branch, inside a fret border pressed into red wax, which is how the README's entry describes it. Whether either is what the owner approved is a person's look (`questions.md` Q2). |

## Scope

In scope:

1. **Two rows in `seal/config.md`, `Pull request seal mark` and `Release
   note seal mark`.** Each is read through `hooks/lib/config.py#config_value`
   by the one step that writes its surface. `yes`, exactly so, turns its
   surface on. An absent or empty row leaves it off and prints nothing. Any
   other value, and a refusal `config_value` returns, leaves it off and is
   named on one line as not read. Neither row changes an exit code.
2. **`pr-body` writes the mark under the heading where its row reads
   `yes` and the work item is sealed at HEAD.** Sealed at HEAD means: the
   work item's `guarantee.md`, read from the directory `pr-body` is given as
   it reads the other records, is read by `hooks/lib/fields.py` with no
   refusal; its newest verdict block reads `sealed`; and
   `chain_check.py#follows` finds the commit that block's `target:` names to
   be HEAD or followed only by the closing records, with the base the same
   line names. Under both conditions the generated part holds one fixed
   line, the mark, between the heading line and the fold, with a blank line
   on each side. Under either condition unmet, the part is what it is today.
   A guarantee that is absent, refused, or not `sealed` at HEAD puts no mark
   and prints no line: the sealer and the pull request's check name those.
   `--check` composes the same part, so the sealer's check and the
   orchestrator's run agree at any one state of the tree.
3. **The mark's address comes from the plugin's manifest.** It is the
   manifest's `repository`, then `/raw/v`, the manifest's `version`, `/`,
   and the manifest's `icon` with its leading `./` dropped. A manifest that
   cannot be read, or lacks any of the three fields, puts no mark and is
   named on one line, with the exit code unchanged.
4. **`seal` reads `Release note seal mark` at the tag.** Under `yes` it does
   what it does today: it attaches `seal.png` and replaces `publish`'s
   header with the two-cell header. Under any other answer it attaches
   nothing, and it replaces `publish`'s header with a one-cell table of the
   results: the same lines in the same order as the two-cell header's
   second cell. `publish_release_note.py#sealed_header` builds both shapes.
   A value other than `yes`, and a refused row, are named on a `::warning::`
   line. The re-run guard, the escaping and the exit of 0 are unchanged.
5. **The orchestrator runs `seal pr-body` once more after it commits a
   `sealed` guarantee, before the body goes to the pull request.** The
   sentence in `skills/code-review/orchestration.md` *Orchestrator: the pull
   request opens once the sealer seals* that opens the pull request "with
   the body the sealer read" says so, and says why no copied line changes.
6. **The rows are documented where every row is.** `templates/setup/config.md`
   gains a section for the two rows. It says `Release note seal mark` is
   read by this plugin's own repository's release workflow alone, because
   the plugin ships no release workflow, so in any other repository nothing
   reads it. `skills/config/SKILL.md` names both rows in its table, and
   `tests/text/test_the_settings_have_a_front_door.py#ROWS` lists both.
7. **This repository turns both on**: its `seal/config.md` gains both rows
   reading `yes`.
8. **The code's own text states the new behaviour**: `pr_body.py`'s module
   docstring, whose "copies lines and composes none" gains the mark as the
   one fixed line that depends on a record's verdict;
   `release_seal.py`'s module docstring (`:1`, `:26-37`);
   `publish_release_note.py#sealed_header`'s docstring (`:644-654`) and
   the module docstring where it names `sealed_header` (`:94`); and the
   comment at the top of `publish-release.yml` (`:25-33`).
9. **The policy text changes through `## Rule changes`**, which the settle
   after the release writes.

Out of scope:

- The terminal stamp and every file it runs from (*Grounding*, #832).
- Shipping a release workflow to a user's repository, through
  `templates/setup/` or `seal pr-checks install` (`plan.md` A8).
- The image itself: its drawing, its format, its file and its manifest
  entry. `.claude-plugin/plugin.json` is read, never edited.
- A mark in the orchestrator's part of the body, in a commit message, or on
  any surface other than the two the issue names.
- Bodies and notes already published. Nothing edits them.
- A third row, or one row holding a list (the owner's decision).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 the mark on a sealed work item | Given a git repository whose `seal/config.md` reads `Pull request seal mark` `yes`, and a work item whose committed `guarantee.md`'s newest block reads `sealed` at a commit only that `guarantee.md` follows. When `seal pr-body` writes the body, then the part below the heading opens with a blank line, the mark line, a blank line and the fold, and the mark's `src` is the manifest's `repository`, `/raw/v`, `version` and `icon` path, its `alt` and `width` as *Data & interfaces* gives. `--check` on that body exits 0. | Cases in `tests/skills/test_pr_body.py`, each shown red before the build |
| S2 no mark before the seal | Given the row `yes` and no `guarantee.md`, or a newest block reading `withheld` or `undecided`. Then the part is today's, line for line, and nothing is printed about the mark. | Cases in the same module |
| S3 no mark on a stale seal | Given the row `yes` and a newest block reading `sealed` at a commit that a later commit outside the closing records follows. Then no mark. | A case in the same module, shown red with the `follows` condition alone removed: the mark then appears |
| S4 the row turns it off | Given a sealed work item, and the row absent, empty, reading `Yes`, `on` or `true`, or written twice. Then no mark. Absent and empty print nothing. The others print one line naming the row and the value, or the refusal, as not read, and the command exits 0. | Cases in the same module; the `Yes` case shown red with the exact-`yes` comparison alone loosened to a case-folded one |
| S5 a manifest the mark cannot be built from | Given a sealed work item and the row `yes`, and a manifest copy lacking `repository`, `version` or `icon`. Then no mark, one line naming the field, and exit 0. | A case in the same module |
| S6 `seal` under the row | Given the note `publish` writes for `tests/github/test_release_seal.py#PULLS` and a tree whose `seal/config.md` reads `Release note seal mark` `yes`. Then `seal.png` is uploaded and the note is edited as today. With the row absent, empty or any other value, nothing is uploaded and `publish`'s header is replaced by the one-cell table of the same result lines. A value other than `yes` prints a `::warning::` naming it. | Cases in `tests/github/test_release_seal.py`; the absent case shown red with the row's read alone removed: the upload then runs |
| S7 the one-cell header | `sealed_header` given no image returns one table cell holding the result lines exactly as the two-cell header's second cell holds them. | A case in `tests/github/test_publish_release_note.py` |
| S8 a re-run of `seal` under either answer | Given the note as the first run left it, under either answer. Then the second run uploads and edits nothing, as today. | The existing re-run case, run under both answers |
| S9 the rows have their door | `templates/setup/config.md` and `skills/config/SKILL.md` name both rows. | `tests/text/test_the_settings_have_a_front_door.py`, `ROWS` gaining both, shown red before the documentation lands |
| S10 the terminal stamp is unchanged | `git diff <base>...HEAD --stat` lists no file under `skills/verify/scripts/seal_stamp.py`, `skills/verify/scripts/seal-mark.txt`, `hooks/sealer-stamp-queue.py` or `hooks/sealer-stamp.py`. | Read by the proofer and the sealer |
| S11 the rule changes parse | `skills/settle/scripts/rule_changes.py#parse` reads this design's `## Rule changes` with no refusal, and `apply_op` places each operation after #1153's. | Executed by the framer in a scratch clone (`plan.md` *Technical context*), and by `seal chain-check` at the pull request |

## Data & interfaces

- **The rows**, in `seal/config.md`'s `| Item | Value |` table:

  ```
  | Pull request seal mark | yes |
  | Release note seal mark | yes |
  ```

- **The mark line** `pr-body` writes, the line after the heading's blank
  line:

  ```
  <img src="<repository>/raw/v<version>/<icon path>" alt="Sealed" width="128">
  ```

  For this plugin at 0.28.0 the `src` is the repository's `github.com`
  address followed by `/raw/v0.28.0/.claude-plugin/icon.png`. GitHub answers
  it with a redirect to its raw-file host, which serves the PNG (*Grounding*).
  The `src` and `alt` are escaped with `html.escape`. The width is a
  constant in `pr_body.py`; 128 is the default `questions.md` Q2 asks the
  owner to look at.
- **The generated part's opening** with the mark:

  ```
  ## From the records

  <img …>

  <details>
  <summary>Copied from the records in seal/threads/<name>/ by seal pr-body.</summary>
  ```

  Without the mark it is today's: the heading, a blank line and the fold.
- **What the mark ties a user's repository to**: the plugin's repository
  staying public at its address, where a rename is followed by GitHub's
  redirect (*Grounding*); the tag `v<version>` existing, which holds for
  every released version; and nothing of the user's repository, since a
  reader's browser fetches a public image. A body written by a copy of the
  plugin whose version has no tag, such as this repository's tree between
  releases, shows a broken image until the tag exists. Where the squash
  commit takes the body, its message carries the line as text, as it
  carries the fold's tags.
- **The lines a reader sees** when the mark is not written: one line opening
  `seal pr-body:`, printed beside `wrote:` or `matches:`, naming
  `Pull request seal mark` and its value, or the manifest's field, as not
  read. In `seal`, one `::warning::` line naming `Release note seal mark`
  and its value. The crafter writes and pins each sentence (contract
  rule 14).
- **`sealed_header`** takes the image as optional: given one, the table of
  two cells it builds today; given none, a table of one cell holding the
  same lines.
- No change to `read_item`, the copied sections, `TAG`, `split`, `_check`'s
  comparison, the note's other parts, the asset name, `draw`, the counters,
  the workflow's steps or the job outputs.

## Rule changes

- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: It runs the suite at the tag, attaches the page form of the stamp's
    mark, the PNG that `.claude-plugin/plugin.json` names as its `icon`, as
    `seal.png`, and replaces the note's header with a table of two cells:
    the image at its display width in the first, and in the second the
    results the stamp states, as text, one per line. They are the sealed
    version and commit, the pull requests merged, the issues closed, the
    outside contributors where there are any, the suite's counts, the work
    items and their review rounds, how many were capped, and the issues
    deferred. The image's alt text names the image alone, because the
    second cell carries every number.
  to: It runs the suite at the tag and replaces the note's header with a
    table whose last cell holds the results the stamp states, as text, one
    per line. They are the sealed version and commit, the pull requests
    merged, the issues closed, the outside contributors where there are
    any, the suite's counts, the work items and their review rounds, how
    many were capped, and the issues deferred. Where `seal/config.md`'s
    `Release note seal mark` row reads `yes` at the tag, the job first
    attaches the page form of the stamp's mark, the PNG that
    `.claude-plugin/plugin.json` names as its `icon`, as `seal.png`, and the
    table opens with a cell holding that image at its display width. Its
    alt text names the image alone, because the results' cell carries every
    number. Where the row is absent or empty, nothing is attached and the
    table is the results' cell alone. Any other value does the same, and
    the job names it on a `::warning::` line as not read. The plugin ships
    no release workflow, so the row is read in this repository alone.
- change
  file: docs/release-checklist.md
  section: 6. After the merge
  from: attaches `seal.png` and puts it in the note's header, beside the
    results the stamp states. Where the header still shows no image,
  to: attaches `seal.png` and puts it in the note's header, beside the
    results the stamp states, where `seal/config.md`'s
    `Release note seal mark` row reads `yes`; under any other value it
    attaches nothing, and the header holds the results alone. Where the row
    reads `yes` and the header still shows no image,
- add
  file: docs/the-review-record.md
  section: The guarantee
  to: **A pull request body carries the seal mark only where the
    repository turns it on and the work item is sealed at HEAD.**
    `seal pr-body` writes the mark, the plugin's icon at the tag of the
    plugin's version, as the first line under the line
    `skills/code-review/scripts/pr_body.py#HEADING` holds. It writes it
    where `seal/config.md`'s `Pull request seal mark` row reads `yes` and
    the newest verdict block of `guarantee.md` reads `sealed` at a commit
    that only the closing records follow, so the mark means what the stamp
    means (*The stamp*). An absent or empty row puts no mark, and any other
    value puts none and is named as not read. The sealer's
    `seal pr-body --check` runs before its own verdict exists, so the copy
    it checks carries no mark from that run. The orchestrator runs
    `seal pr-body` once more after it commits a `sealed` guarantee, and that
    run changes no copied line, because the copy reads no `guarantee.md`.
    The mark's address ties the body to the plugin's repository staying
    public and to the version's tag existing; a body written by a version
    with no tag shows no image until the tag exists.
    check: tests/skills/test_pr_body.py

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The sentences that state the release image as unconditional: the module docstring's "Draw the release's seal as a PNG, attach it, and put it in the note", and the workflow comment's "attaches the page form of the stamp's mark … as `seal.png`, and replaces the note's header with a table of two cells" | `.github/scripts/release_seal.py:1`, `:26-37`; `.github/workflows/publish-release.yml:25-33` | The same places, rewritten to say the row decides the image (*Scope* item 8). |
| `sealed_header`'s "the same table with two cells" as the only shape | `.github/scripts/publish_release_note.py#sealed_header` (`:644-654`) | The same docstring, naming the one-cell shape (*Scope* item 4). |
| The sentence that opens the pull request "with the body the sealer read" | `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* (`:223-224`) | The same sentence, rewritten to the run of `seal pr-body` after the seal (*Scope* item 5). |
| `pr_body.py`'s "It copies lines and composes none" as a statement with no exception | `skills/code-review/scripts/pr_body.py:8-17` | The same docstring, naming the mark as the one fixed line that depends on the guarantee's verdict and the row. |
| The policy sentences on the seal job's attach and its two-cell header | `docs/branch-and-release.md` *Cutting a release*, `docs/release-checklist.md` *6. After the merge* | `## Rule changes` above, written at the settle, never by this pull request. |
| No mechanism goes in return for the mark | none | The mark is a mechanism by `skills/core/SKILL.md` *The rule a mechanism is kept against*, and it catches no defect, so it is kept on its cost alone. Its cost is one row read by each of two steps that already write their surfaces, one `follows` call, and one more run of `seal pr-body` per sealed work item. Nothing it could replace exists: the terminal stamp stays by the owner's direction, and the release image stays in this repository by the same direction. The release image's unconditional path is not removed, it becomes the `yes` path. |

Framed 2026-11-02 by framer, before the build.
