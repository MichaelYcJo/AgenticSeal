# Implementation Plan: the note opens with the owl and folds each category (#1153)

## Technical context

The note is built in one place and edited in one place, and both stay.

- `.github/scripts/publish_release_note.py#release_body` (`:651-709`)
  writes the theme, the glance block (`#glance`, `:595-610`), one
  `### <heading>` and its lines per conventional-commit type (`:684-687`),
  the thanks section, the update section and the full-changelog fold
  (`:702-708`). The fold already has the shape *Scope* item 5 asks of every
  fold: its tags on lines of their own, a blank line after the summary and
  before the closing tag.
- `.github/scripts/release_seal.py#seal_release` (`:469-529`) reads the
  published note, finds `glance`'s block exactly once (`:506-513`),
  uploads `seal.png`, and replaces the block with `sealed_glance`'s
  (`:514-528`). That exact-text guard is what makes a re-run of `seal`
  harmless today, and it is the guard *Scope* item 4 keeps.
- `release_seal.py#release_rows` (`:130-168`) builds the stamp's rows, which
  the dry run prints, and `#alt_text` (`:171-208`) turns them into one
  sentence. The sentence's phrases become the second cell's lines.
- Both scripts run with the standard library alone in the `publish` and
  `seal` jobs (`publish-release.yml`; `release_seal.py:13-16`). The header
  and the folds are strings, so nothing new is imported. The GFM renderer
  the S1 case uses, `cmarkgfm`, is installed by the suite's own runs
  (`.github/scripts/run_tests.py#CMARKGFM`, and the `seal` job's install
  line), never by the scripts.

S7 was executed by the framer on 2026-11-02 in a scratch clone made with
`git clone --no-local` from this worktree: `rule_changes.py#parse` read the
seven operations of `frame/design.md` *Rule changes* with no error and no
unread line, and each `from` was found, whitespace collapsed, in the section
it names. The clone was removed afterwards.

**The failure scenario of the chosen approach.** In six months #1204 has
made the image optional. A repository that turns it off keeps `publish`'s
one-cell header, which reads as a complete header on its own, so nothing
breaks. What can break is the exact-text guard: a change to the counts'
words that lands between `publish` and `seal` of one run would make `seal`
refuse. Both read the words from one function at one tag in one run, so
that needs a change to the function inside a single workflow run, which
cannot happen. A pull request title that holds a bare `</details>` would
close its category's fold early; the limit sentence says so, and the next
person to see it fixes one note with `gh release edit`.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. `publish` writes a one-cell header of the counts it knows; `seal` replaces the whole header with the two-cell one, found by the exact text `publish`'s function returns | A header edited by hand before `seal` runs keeps its one cell and gets no image, as a hand-edited glance table does today. | Chosen. It is the issue's first option, and it keeps the one guard the re-run rule already rests on. |
| A2. `publish` writes the two-cell table with the cells it knows, and `seal` fills the rest | `seal` has to find and fill cells inside a table, which is a second shape to find beside the header. Before `seal` runs, or when it fails, the first cell is empty or points at an image not yet uploaded, and the empty result lines are visible on the page. | Rejected. It needs a placeholder shape that a failed seal leaves on the page. |
| A3. Replace the two jobs with one: `publish` runs the suite first and writes the whole header once, with no edit | The note waits for a 30-minute suite after the merge, and a red or hung suite delays or stops the note. #718 put the seal in a `continue-on-error` job after the note precisely so that a seal that cannot be drawn costs the image and never the note. Premise checked: the `seal` job is `continue-on-error: true` with `timeout-minutes: 60`, and its suite step has `timeout-minutes: 30` (`publish-release.yml`, read). | Rejected. The split is what keeps the note independent of the suite, and the issue keeps the re-run rule. |
| A4. Find the header by an HTML comment marker that `publish` writes and `seal` looks for | The marker is a new mark in the note with no reader but the seal, and a hand edit that keeps the marker and changes the counts would be overwritten. | Rejected. The issue asks for no new mark, and the exact-text guard already finds the block. |
| A5. Keep the glance table in `publish`'s note and let `seal` turn it into the two-cell header | A seal that fails leaves the old table and its heading on the note. | Rejected. The issue removes the separate table, and A1 removes it whether or not `seal` succeeds. |
| A6. The renderer escapes a `details` or `summary` tag outside a code span in each title and fragment | A second reader of the same tag, in a stdlib script, beside #1218's reader at `seal pr-body`. It guards a shape found in 0 of 318 merged titles and 0 of 68 published notes (`frame/design.md` *Grounding*). | Rejected. The fragment is held at the pull request by #1218, and the title is a limit stated in the docstring. |
| A7. An SVG asset in place of the PNG | Every release asset is served as `application/octet-stream`, and a browser draws an SVG only when it is served as `image/svg+xml` (`frame/design.md` *Grounding*). The note would show a broken image. | Rejected. PNG stays, as the issue's default says. |
| A8. Strip the emoji from the category summaries under the owner's rule against symbols a reader trips on | The note's type names change in every release from 0.28.0 on, which the issue does not ask for, and its own example writes the summary with the type's emoji. No script reads the summaries. | Rejected. The header the work adds carries none, and the glance's emoji and its ` · ` go with it. |
| A9. Fold the thanks and update sections too | The update command, which every reader needs, is hidden behind a click. | Rejected. They are not categories, and the issue names categories. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1 and 5, and the parts of item 6 that state the folds | S1's cases, each seen red against the current renderer. `bin/test tests/github/test_publish_release_note.py tests/github/test_release_seal.py tests/skills/test_settle.py tests/behaviour/test_a_release_publishes_its_note.py`, the modules that read or load the renderer. `uvx ruff check` and `uvx ruff format --check` on the changed files. | |
| 2 | *Scope* items 2, 3 and 4, and the rest of item 6 | S2, S3 and S4's cases, each seen red against phase 1's tree, and S4's case shown red with the exact-header guard in `seal_release` alone removed. S5's rewritten case and S6's unchanged case pass. `bin/test tests/github/test_publish_release_note.py tests/github/test_release_seal.py tests/behaviour/test_the_release_seal_is_drawn.py tests/behaviour/test_a_release_publishes_its_note.py tests/behaviour/test_the_gate_names_every_step_ci_runs.py tests/text/test_the_release_tail_does_not_end_at_the_tag.py tests/hooks/test_console.py tests/hooks/test_launch.py tests/skills/test_settle.py tests/test_censuses.py`, the modules that read a changed path, with the launch floor and the real-identifier census among them. `bin/seal layout --check tests`. `uvx ruff check` and `uvx ruff format --check` on the changed files. The full suite is the orchestrator's broad run (contract rule 2). | |

## Operational impact

None for a deployer. No step, output, permission, asset name or dependency
of `publish-release.yml` changes. The first note built in the new shape is
the one the merge of 0.28.0 into `main` publishes. Notes already published
are never rewritten.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
