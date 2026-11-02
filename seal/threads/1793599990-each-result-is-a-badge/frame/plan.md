# Implementation Plan: #1299, each result in the release note's sealed header is a badge in the seal's reds

## Technical context

The code this builds on, opened at `64d09e81`:

- `.github/scripts/publish_release_note.py:611-669`. `plural` (`:611`),
  `counts` (`:615-625`, the counts in words, shared by both headers),
  `table` (`:628-634`, one row of cells, each cell's lines joined by
  `<br>`), `header` (`:637-642`, the text `seal` finds and replaces) and
  `sealed_header` (`:645-669`, today `<b>SEALED</b>` and the prose lines,
  with or without the image's cell). The module imports `html` already
  (`:111`); the encoder needs `urllib.parse`, one import line in the block
  at `:111-117`. The `git log`
  calls #1283 may edit sit at `:188-266`, away from these lines. Place the
  import at the end of the import block; where #1283 adds an import beside
  it, whichever branch lands second resolves the adjacent lines when it
  merges the release branch in.
- `.github/scripts/release_seal.py:144-222`. `release_rows` (`:144-182`)
  is unchanged: it stays the source of every value and the rows the dry
  run prints. `results` (`:185-219`) is rewritten to return badge lines;
  its reading of the rows (the continuation rows, the suite split on a
  comma, `NOT_READ`) stays, and only what it builds from them changes.
  `seal_release` (`:518-598`) passes `results`' two parts to
  `sealed_header` unchanged (`:570-580`); the guard (`:562-568`) reads
  `header`'s text, which this work does not touch.
- `tests/censuses.py:885-891`, `ALLOWED_DOMAINS`, gains the badge host
  with its reason as a comment.
- `.github/workflows/publish-release.yml:30-31`, one comment phrase.

Constraints: `release_seal.py` and the code it loads are standard library
only (its docstring, `:24-28`), and `urllib.parse` is standard library.
GitHub's renderer drops a `data:` URI and a `style` attribute (*Grounding*,
executed), so an image at an outside address is the only coloured thing the
note can show.

Executed 2026-11-02, the rule changes: in a `git clone --no-local` of the
worktree under the probe directory, `skills/settle/scripts/rule_changes.py`
`parse` read #1153's design (7 operations), #1204's (3) and this frame's
(3) with no error and nothing unread, and `apply_op` placed every one of
them in that merge order on the clone's `docs/branch-and-release.md` and
`docs/release-checklist.md`. The resulting *Cutting a release* paragraph
reads as one passage, with "They are the sealed version …" still following
the sentence that names the results.

**The failure scenario of the chosen approach, six months on.** The Shields
service retires or changes its `/badge/` path, rate-limits GitHub's image
proxy, or is down when a reader opens a note the proxy has not cached. The
results cell then shows each badge's `alt` text, or a broken-image mark
beside it, on every note since 0.28.1; no job fails, and every number is
still in the page. A second scenario: the seal is redrawn in another colour
under #857's rule that a new page image is a new icon, and the badges keep
the old reds, because the two colours are constants read from today's icon
(A7). The change that would follow either is one edit to `publish`'s badge
helpers, for the notes published after it.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1 The `/badge/<label>-<value>-<colour>` path form, each label and value with `-` and `_` doubled and then percent-encoded with nothing safe, `?labelColor=` for the label's colour | A value whose `-` or `_` is not doubled splits the badge at the wrong place or reads `_` as a space. The encoder doubles both before percent-encoding, the probe showed the service reads `--`, `__`, `%20`, `%2F`, `%25`, `%26`, `%23` and `%3F` back as the characters they stand for, and S4's decoder pins it | **Chosen.** It is the form the issue names and the service's primary static form, so the one least likely to be retired under notes already published. |
| A2 The `/static/v1?label=&message=&color=&labelColor=` query form, encoded by `urllib.parse.urlencode` with no doubling | The service keeps this form for old badges, and a retirement of it breaks every published note's cell at once, with no way to repair a published note but by hand. Its encoding is the standard query encoding, which is its advantage: no service-specific grammar | Rejected on that longevity: a published note cannot be rebuilt, so the form most likely to stay served wins over the simpler encoding. The probe showed both draw the same values today. |
| A3 Keep the prose lines (the structure #1153 built) | None in the code. The owner read v0.28.0's note and judged the cell a column of prose in which no number stands out, which is the issue | Rejected by the owner's decision in #1299. The premise that kept it, that the numbers live as text so a reader without images has them, is kept by A1's `alt` text. |
| A4 A 3x2 grid of numbers with small labels under them, or a two-column table of bold right-aligned numbers | Both stay text in the page's theme, so neither takes the seal's colour | Rejected by the owner, who chose badges from the three. |
| A5 Badges drawn by `seal` as image files and attached to the release beside `seal.png` | #1153's framer measured release assets served as `application/octet-stream` with `content-disposition: attachment` (its design's *Grounding*, executed 2026-11-02), so an SVG asset does not draw in an `<img>`; a PNG badge needs text rendering, which the standard library cannot do, and `release_seal.py` imports no package | Rejected: it would add an imaging dependency to the release job to remove an outside host from the reader's page. |
| A6 A badge inlined as a `data:` URI, or a cell coloured with `style` | GitHub's renderer drops both (*Grounding*, executed), so the reader sees an empty image or plain text | Rejected: nothing reaches the reader. |
| A7 The two colours read from the icon's pixels at seal time, so a recoloured seal recolours the badges | A PNG decoder in the release script, and a rule for which pixels are the label's and the value's colour, to follow a redraw that #857 makes a deliberate act | Rejected. The colours are two constants with a comment naming `assets/seals/owl.svg`'s relief fill and wax edge they come from; the redraw that would change them is a design act that edits its own surfaces. |
| A8 A value not read drawn in grey, so a gap stands out | One more branch and one more colour, outside the reds the owner asked for. A value not read already reads `not read` in words on the badge and in its `alt` | Rejected. Every badge is in the two reds. |
| A9 `publish`'s own header, before the seal, made of badges too | `header`'s text is what `seal` finds and replaces, so changing it changes the re-run guard's input for nothing the issue asks. The header stands alone only between the two jobs, or on a note whose seal failed, and there plain counts are the honest state | Rejected. `header` and `counts` are unchanged. |
| A10 An exemption comment above the one line naming the badge host, in place of an `ALLOWED_DOMAINS` entry | The test cases that pin the badge's `src` name the host too, so each needs its own exemption, and an exemption is for a line that "is not the defect the census looks for", while this is a real service named on purpose, like `w3.org` and `claude.com` | Rejected. The host joins `ALLOWED_DOMAINS` with its reason. |
| A11 The service's `flat-square` or `for-the-badge` style | `for-the-badge` writes every label and value in capitals, so `passed` and `main` change case; `flat-square` drops the default's rounded corners and gradient for no reader's gain | Rejected. The default style, so the URL carries no `style` parameter. |
| A12 Badges only in the two-cell header, prose where the image is off | Two shapes of the same results from one function, and the row #1204 added would decide the results' look as well as the image | Rejected. The results cell is one cell in both shapes, and the row decides only the image. |
| A13 The owner's sketch's seven-character commit | `release_rows`' `tag` row holds eight characters, the width the panel and v0.28.0's note show; a seven-character badge would be a second spelling of the same commit | Rejected. The commit badge shows the `tag` row's eight characters. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope items 1 to 7 | S1 to S6 by their cases in `tests/github/test_publish_release_note.py` and `tests/github/test_release_seal.py`, each new or changed assertion seen red first; S7 by its unchanged case; `tests/test_censuses.py` and the census case of each touched module for S8. The two modules and the census module are the phase's narrow run. | |

One phase, because the slice cannot be cut thinner and stay green:
`sealed_header`'s inputs change type, and `results` is its only caller
outside the tests.

## Operational impact

- No migration, no environment variable, no new package. One outside host
  is read by a reader's page, never by a job: the Shields badge service,
  through GitHub's image proxy.
- The first note with badges is v0.28.1's. Published notes are unchanged.
- The plugin ships no release workflow, so no user's repository sees this.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
