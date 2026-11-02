# Design: the note opens with the owl and folds each category (#1153)

Every coordinate below was opened in the worktree at `3b343a084`, the tip of
`feat/1153-the-release-note-stacks-the-seal-and-every-category`. That branch
was cut from `release/v0.28.0` at `bf18be7d1`, which holds #1139 (#1291).
The issue had no comments when the orchestrator read it on 2026-11-02 with
`gh issue view 1153 --json body,comments`, and the framer's run of the same
command the same day showed none (executed).

The note has two writers, and this design names them by job. `publish` is
`.github/scripts/publish_release_note.py`, run by the `publish` job of
`.github/workflows/publish-release.yml`. `seal` is
`.github/scripts/release_seal.py`, run by the `seal` job after `publish`
created the release in the same run.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `docs/branch-and-release.md` *Cutting a release*: "The note opens with the release's theme", then "A summary read from the pull requests merged into `release/vX.Y.Z` follows: counts, one line per pull request under its conventional-commit type", then the seal job "replaces the glance table with the image at its display width and one line of the table's counts. … That edit is the only change it makes to a note, and only to one whose glance table is still exactly as it was generated." (read) | The four sentences this work rewrites through `## Rule changes`. The last one is the re-run rule the issue keeps: the seal edits only a block exactly as `publish` wrote it, so a second run finds nothing to edit. |
| `docs/release-checklist.md` *6. After the merge*, the box "A GitHub Release exists at `vX.Y.Z`" (read) | It restates the note's order and where the seal goes ("puts it where the glance table stood"), so it changes with them. `tests/behaviour/test_the_release_seal_is_drawn.py` pins two phrases of the box ("the same workflow's `seal` job attaches `seal.png`", "says why on a `::warning::` line"); the rule changes below leave both as they read. |
| `docs/branch-and-release.md` *Work accumulates on a release branch* and #1139's design (`seal/threads/1793582903-each-entry-links-its-pull-request/frame/design.md` *Rule changes*, read) | Untouched here. #1139 rewrites the sentences on each entry's link; no `from` below overlaps them, and the full-changelog fold that holds the entries keeps its shape. |
| `skills/core/SKILL.md` *The rule a mechanism is kept against*: "A script holds a gate only on a fact it reads exactly" | The seal keeps finding its block by the exact text the function that wrote it returns (`release_seal.py:506-513`, read). The design adds no marker, label or line grammar to find the header by. |
| #718, as `.github/workflows/publish-release.yml:24-36` and `release_seal.py`'s docstring state it (read) | Built on. The seal runs after the note is out, every step is `continue-on-error`, and a seal that cannot be drawn costs the image and never the counts. The header keeps that split: `publish` writes the counts it knows, and `seal` adds the image and the suite's results. |
| #832, merged as `149ca9ecc` (#859), as `skills/verify/scripts/seal_stamp.py:1-24` states it (read) | Built on. The stamp is "two things side by side on the terminal's own background, and nothing else": the disc at the left and the panel's text right of it, opening with a bold `SEALED`. The header is the same layout on the page: the image in the first cell, the results as text in the second, `SEALED` in bold, and no frame, colour or style attribute of its own, so the text reads in the page's own theme. The image's width stays what `draw` answers (the PNG's width over `DENSITY`), as #832 set it. |
| #857 and #1174, merged as `33c09a93c` (#1193), as `assets/seals/README.md` *The little owl — from 0.25.1* states it (read) | Built on. The image is the plugin's icon, `.claude-plugin/icon.png`, drawn from `assets/seals/owl.svg`, the round-headed owl; `release_seal.py#draw` copies it byte for byte. The icon is 512 by 512 (executed, its `IHDR` read with `python3`), so it shows at 256 CSS pixels. Nothing in the drawing or the copy changes. |
| #1053, merged as `f15b3f998` (#1140), and #572, as `publish_release_note.py:31-41` states them (read) | Built on: the theme is the milestone's first sentence, the summary is read from the merged pull requests, and the fragments stay folded under the full-changelog summary. Departed from in two places, at the issue's request: the theme no longer opens the note, the header does, and the type headings become folds. |
| #1117, merged as `6310a6e85` (#1144), as `publish-release.yml:13-23` states it (read) | Built on: the merge to `main` tags and publishes in one run, so `publish` and `seal` read one pull request list at one tag. `seal` re-reads that list through `publish`'s own `merged_pulls` and `tally` (`release_seal.py:486-489`), so the header it looks for is the one `publish` wrote. |
| The owner's rule against symbols and constants a reader trips on, as the orchestrator's spawn prompt relays it: no emoji or decorative syntax a reader must parse, and no extra config rows (the orchestrator's finding; in the tree, `tests/text/test_the_record_is_written_in_words.py` holds it for the files an agent reads as instruction, read) | Weighed both ways. The header is new text, and it carries no emoji and no `·`: the glance's emoji rows and the ` · ` that joins the sealed counts line go with them. The category summaries keep the type names as `TYPES` spells them (`publish_release_note.py:453-465`), emoji included, because the issue's own example writes the summary that way, every published note has carried them since #572, and no script reads them (`plan.md` *Alternatives considered*). No config row is added. |
| Executed 2026-11-02: `gh api repos/{owner}/{repo}/releases/tags/v0.27.3 --jq '.assets[]'` and `curl -sIL` on its `seal.png` download URL; the same for the `checksums.txt` asset of the `gh` CLI's latest release | The two assets are stored as `image/png` and `text/plain; charset=utf-8`. Both are served, after GitHub's redirect to its asset host, as `application/octet-stream` with `content-disposition: attachment`. So an SVG asset would be served the same way. A browser draws an SVG in an `<img>` only when it is served as `image/svg+xml`, and it sniffs raster formats such as PNG from their bytes (read, not opened here: the WHATWG MIME Sniffing Standard has no SVG pattern among its image patterns; the PNG drawing on every published note is consistent with it). The image stays PNG, as the issue's default says. |
| Executed 2026-11-02: `gh api -X POST markdown -f mode=gfm` over a sample of the header and two category folds, and over a fold holding a bare closing tag | GitHub's renderer keeps `<table>`, `<td>`, `<img width>`, `<br>`, `<b>`, `<details>` and `<summary>`, and the sample's header renders as one table with the image in the first cell and the eight result lines in the second. A `` `</details>` `` inside a code span in a fold's line renders as `<code>&lt;/details&gt;</code>` and stays in the fold. A bare `</details>` in a list line closes the fold there, and the lines after it fall outside. |
| Executed 2026-11-02: `gh pr list --state merged --limit 3000 --json number,title` and `gh api --paginate 'repos/{owner}/{repo}/releases?per_page=100'`, read with `close_issues_on_release.py#SPAN`'s pattern and `</?(details\|summary)` in a scratch script | 0 of the 318 merged pull request titles holds a `details` or `summary` tag, inside a code span or outside one. In the 68 published notes no line outside a code span holds one, beyond the renderer's own fold lines, and each note's `<details>` and `</details>` lines are equal in number. |
| `skills/code-review/scripts/pr_body.py:240` and `:290-296` (read), and #1218's design (`seal/threads/1793588973-pr-body-reads-a-details-tag-as-github-does/frame/design.md` *Scope* item 1, read in its worktree at `b3e74ca95`) | A work item's `changelog.md` is copied whole into its pull request body. #1218 refuses a copied line that holds a `details` tag outside a code span, so a fragment that would close a fold is refused before its pull request opens. The note's fragments reach `publish` through the same files. |

## Scope

In scope:

1. **Each category folds under its name and count.** In
   `publish_release_note.py#release_body`, each conventional-commit type
   that has pull requests is written as a `<details>` element in place of
   its `### <heading>` line. The `<summary>` is the heading as `TYPES` or
   `OTHER` spells it, a space, and the number of pull requests under it in
   parentheses. The lines under it are the pull request lines as today. The
   order of the types is unchanged. The thanks section, the update section
   and the full-changelog fold keep their shapes.
2. **`publish` writes a header of the counts it knows, first.** The note
   opens with an HTML table of one row and one cell. The cell holds the
   counts the glance table held, in words, one per line: the pull requests
   merged, the issues closed, and the outside contributors where there are
   any. The theme line follows the header, and the first category fold
   follows the theme. The `### At a glance` heading and its table go. A note
   with no pull request to read has no header, as it has no glance table
   today.
3. **`seal` replaces that header with the two-cell header.** The first cell
   holds the image, the second the results the stamp states, one per line:
   `SEALED` in bold with the version, the tagged commit and its branch; the
   pull requests merged; the issues closed; the outside contributors where
   there are any; the suite's counts; the work items and their review
   rounds; how many were capped; and the issues deferred. A count that could
   not be read says so in its line, as the alt sentence says it today. The
   image's `alt` text is `The <version> release seal`, because the second
   cell carries every number as text. The sentence `alt_text` composes
   becomes those lines.
4. **A re-run of `seal` leaves the header as it is.** `seal` edits the note
   only where `publish`'s header stands in it exactly once, as today's guard
   reads the glance table (`release_seal.py:506-513`). After the first run
   the note holds the two-cell header instead, so a second run uploads and
   edits nothing. Its refusal sentence names that case among the others.
5. **The folds stay well formed.** Each `<details>`, `<summary>` and
   `</details>` the renderer writes stands on a line of its own, with a
   blank line after the summary line and before the closing tag, as the
   full-changelog fold does today. A pull request title is written as text:
   each `<` outside a code span becomes `&lt;`, read with
   `close_issues_on_release.py#SPAN`, so no title opens or closes a fold or
   any other element, and a code span stays code. This reads no tag: it is
   the renderer writing a subject line as the text it is. A fragment is not
   escaped, since it is the records' own text and its bare tag is refused at
   `seal pr-body` by #1218. #1293's own title, merged into this release with
   three bare `details` tags, is the instance that showed a title can hold one.
6. **The code's own text states the new note.** The module docstring of
   `publish_release_note.py` (`:31-41` and `:84-91`), the docstrings of the
   functions that write and replace the header, `release_body`'s docstring,
   `release_seal.py`'s module docstring (`:27-37`), its `LABELS` comment
   (`:100-109`) and the comment at the top of `publish-release.yml`
   (`:24-36`).
7. **The policy text changes through `## Rule changes`**, which the settle
   after the release writes.

Out of scope:

- Whether a repository shows the image on its note at all: #1204's config
  rows. The header holds the image in a cell of its own, so #1204 decides
  only whether `seal` puts one there.
- `seal pr-body`'s refusal of a `details` tag: #1218.
- The emoji in the type names, the thanks heading, the update heading and
  the full-changelog summary, and the ` · closes ` on each pull request
  line. The issue asks for none of them, and every published note carries
  them.
- Folding the thanks and update sections. They are not categories.
- The image itself, its format, its width and its drawing (*Grounding*).
- The terminal stamp.
- Published notes. `publish` never republishes, and nothing edits them.
- `.claude-plugin/plugin.json`.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 each category is a fold under its count | Given the pull requests of `tests/github/test_publish_release_note.py#RELEASE`. When the note is built, then each type with pull requests is `<details>`, `<summary><heading> (<n>)</summary>`, a blank line, its pull request lines, a blank line and `</details>`, in `TYPES` order, and no `### ` line names a type. Rendered by the GFM renderer the suite pins (`.github/scripts/run_tests.py#CMARKGFM`), each fold is one `details` element whose summary reads `<heading> (<n>)`, and a title holding `` `</details>` `` in a code span stays inside its fold. | Cases in `tests/github/test_publish_release_note.py`, seen red against the current renderer |
| S2 `publish` opens the note with its header | Given the same pull requests and a theme. Then the note opens with the one-cell table holding `7 pull requests merged`, `4 issues closed` and `2 outside contributors`, one per line, then a blank line, the theme, a blank line and the first fold. A release of one pull request closing one issue reads `1 pull request merged` and `1 issue closed`, with no contributors' line. The note holds no `At a glance`. | Cases in the same module, seen red |
| S3 `seal` replaces the header with the two-cell header | Given the note `publish` writes for `tests/github/test_release_seal.py#PULLS`. When `seal` runs, then `seal.png` is uploaded before the edit, and the edited note is the published one with the header replaced by the two-cell table: the image at the release-download URL with alt `The 1.2.3 release seal` and the width `draw` answered, and the result lines in their order. Every other byte is unchanged, so the note opens with the two-cell header, the theme under it and the first fold. A value or URL holding a quote or `<` is escaped. Rows not read say so in their lines. | Cases in `tests/github/test_release_seal.py`, seen red |
| S4 a re-run of `seal` leaves the header as it is | Given the note as the first run of `seal` left it. When `seal` runs again, then nothing is uploaded and nothing is edited, and the log's `::warning::` line says the header is not in the note as `publish` writes it and names a run of the job that already replaced it. | A case in the same module, shown red with the exact-header guard alone removed: the second run then uploads and edits |
| S5 a header edited by hand is left alone | Given a note whose `publish` header was changed by one character. Then nothing is uploaded or edited. | The existing case `test_a_hand_edited_note_is_left_alone_and_nothing_is_uploaded`, rewritten to the header |
| S6 a note with no pull request to read | Given `gh pr list` fails or lists none. Then the note is the theme line and the fragments, unfolded, with no header, as today. | The existing case `test_with_nothing_to_summarise_the_note_is_the_theme_and_the_fragments`, unchanged |
| S7 the rule changes parse | `skills/settle/scripts/rule_changes.py#parse` reads this design's `## Rule changes` with no refusal and no unread line. | Executed by the framer in a scratch clone (`plan.md` *Technical context*), and by `seal chain-check` at the pull request |

## Data & interfaces

- **The header `publish` writes** (*Scope* item 2), with each line separated
  by `<br>` and no blank line inside the table, so GitHub reads the table as
  one HTML block:

  ```
  <table>
  <tr>
  <td>7 pull requests merged<br>4 issues closed<br>2 outside contributors</td>
  </tr>
  </table>
  ```

- **The header `seal` writes in its place** (*Scope* item 3): the same
  table with a first cell holding
  `<img src="<url>" alt="The <version> release seal" width="<width>">`, and
  a second cell whose lines are, in order,
  `<b>SEALED</b> v1.2.3 at aaa11111 on main`, `2 pull requests merged`,
  `2 issues closed`, `1 outside contributor`,
  `the suite at 7003 passed and 66 skipped`,
  `1 work item over 1 review round`, `1 of them capped`, `1 issue deferred`.
  The suite, items, capped and deferred phrases are the ones `alt_text`
  composes today (`release_seal.py:171-208`), and the counts' phrases are
  one function's in `publish_release_note.py`, which both headers call. URL,
  alt and every value are escaped with `html.escape`.
- **Where each shape lives**: both headers are built in
  `publish_release_note.py`, as `glance` and `sealed_glance` are now, and
  `seal` finds `publish`'s header by calling the function that wrote it. The
  crafter names the functions.
- **A category fold** (*Scope* item 1):

  ```
  <details>
  <summary><heading> (<n>)</summary>

  - <pull request line>

  </details>
  ```

  with one blank line between two folds.
- **The note's order**: the header, the theme, the folds, the thanks
  section, the update section, the full-changelog fold.
- No change to the workflow's steps, the job outputs, the asset name, the
  image URL, `draw`, `release_rows`, the counters, `section` or the entry
  link line.

## Rule changes

- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: The note opens with the release's theme, the first sentence of its
    milestone's description with a leading `Purpose:` left out; a milestone
    that cannot be read leaves the note without one and never fails the job.
  to: The note opens with a header, an HTML table whose one cell holds the
    release's counts as text, one per line: the pull requests merged, the
    issues they closed, and the outside contributors where there are any.
    The release's theme follows it, the first sentence of its milestone's
    description with a leading `Purpose:` left out; a milestone that cannot
    be read leaves the note without one and never fails the job.
- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: A summary read from the pull requests merged into
    `release/vX.Y.Z` follows: counts, one line per pull request under its
    conventional-commit type with the issues it closed,
  to: A summary read from the pull requests merged into
    `release/vX.Y.Z` follows: one fold per conventional-commit type, its
    summary the type's name and the number of pull requests under it, and
    in it one line per pull request with the issues it closed,
- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: replaces the glance table with the image at its display width and
    one line of the table's counts.
  to: replaces the note's header with a table of two cells: the image at
    its display width in the first, and in the second the results the
    stamp states, as text, one per line. They are the sealed version and
    commit, the pull requests merged, the issues closed, the outside
    contributors where there are any, the suite's counts, the work items
    and their review rounds, how many were capped, and the issues deferred.
    The image's alt text names the image alone, because the second cell
    carries every number.
- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: That edit is the only change it makes to a note, and only to one
    whose glance table is still exactly as it was generated.
  to: That edit is the only change it makes to a note, and only to one
    whose header is still exactly as it was generated, so a run of the job
    after the first finds no such header and uploads and edits nothing.
- change
  file: docs/release-checklist.md
  section: 6. After the merge
  from: The note opens with the release's theme line, then a summary of the
    release's pull requests and a
  to: The note opens with a header of the release's counts and the theme
    line under it, then the release's pull requests, one fold per
    conventional-commit type under its name and count, and a
- change
  file: docs/release-checklist.md
  section: 6. After the merge
  from: puts it where the glance table stood. Where the note still shows the
    table,
  to: puts it in the note's header, beside the results the stamp states.
    Where the header still shows no image,
- change
  file: docs/release-checklist.md
  section: 6. After the merge
  from: or the glance table was not in the note as generated: edited before
    the job reached it, published without one, or the pull requests moved
    between the two lists.
  to: or the header was not in the note as generated: edited before the job
    reached it, already replaced by an earlier run of the job, published
    without one, or the pull requests moved between the two lists.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The glance block: its heading `GLANCE_HEADING`, its table and its three emoji rows | `.github/scripts/publish_release_note.py#glance`, `#GLANCE_HEADING` (`:444`, `:595-610`) | `publish`'s one-cell header (*Scope* item 2). It is the separate table the issue removes. |
| The sealed block: the heading over the image, the image on a line of its own, and the counts joined by ` · ` | `.github/scripts/publish_release_note.py#sealed_glance` (`:613-633`) | `seal`'s two-cell header (*Scope* item 3). It is the image's standalone line the issue removes. |
| The alt sentence that carries every value, and its `[`, `]` and line-break filter, written for a Markdown image the note no longer uses | `.github/scripts/release_seal.py#alt_text` (`:171-208`) | The second cell carries the values as text, and the alt names the image. Its catch record: it was the only place the suite and chain counts reached a reader without images, and the cell is that place now. |
| The `### <heading>` line over each type's pull request lines | `.github/scripts/publish_release_note.py#release_body` (`:684-687`) | The fold's summary (*Scope* item 1). |
| The text that states the glance: the module docstring's "after the theme the note says … a count" and "The glance block is built by `glance`, and the seal's replacement for it by `sealed_glance`"; `release_seal.py`'s "unless the glance table is still in the note exactly as `glance` wrote it" and its `LABELS` comment's "they reach the note as its alt text (`alt_text`)"; the workflow comment's "meets the glance-table guard" and "replaces the note's glance table with the image and one line of the table's counts" | `publish_release_note.py:35-41`, `:89-91`; `release_seal.py:33-34`, `:108-109`; `.github/workflows/publish-release.yml:28`, `:31-32` | The same places, rewritten to the header (*Scope* item 6). |
| The refusal sentence "the glance table is not in the note exactly once as `glance` writes it for this release …" | `.github/scripts/release_seal.py#seal_release` (`:507-513`) | A sentence that names the header and a run of the job that already replaced it (*Scope* item 4), pinned by S4's and S5's cases. |
| The cases' pins of the glance, the type headings and the alt sentence | `tests/github/test_publish_release_note.py#Test_main::test_every_change_is_one_line_under_its_type`, `#Test_main::test_the_glance_counts_the_release`, `#Test_module::test_the_glance_block_is_built_by_one_function_and_its_sealed_twin_by_another`; `tests/github/test_release_seal.py#Test_main::test_accepts_a_published_note_and_replaces_its_glance_table`, `#Test_main::test_refuses_on_any_failure_and_leaves_the_note_as_published` (its two glance cases), `#Test_main::test_a_hand_edited_note_is_left_alone_and_nothing_is_uploaded`, `#Test_module::test_the_alt_text_is_one_sentence_carrying_every_value`; the two modules' docstrings where they state the glance and the theme opening the note (`tests/github/test_publish_release_note.py:23`, `tests/github/test_release_seal.py:6`) | Rewritten to the header and the folds (S1 to S5). What each case pins is otherwise unchanged. |
| The policy sentences on the glance table and the type headings | `docs/branch-and-release.md` *Cutting a release*, `docs/release-checklist.md` *6. After the merge* | `## Rule changes` above, written at the settle, never by this pull request. |

Framed 2026-11-02 by framer, before the build.
