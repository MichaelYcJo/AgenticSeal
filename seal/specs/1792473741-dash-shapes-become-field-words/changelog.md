### Fixed

- **A comment opener quoted in a code span no longer hides the rest of a
  record (#1000).** The record readers blanked every line after a `<!--`
  that sat inside a code span on its line, though the page shows it as code.
  A `guarantee.md` quoting it lost its `Verdict:` line, so the stamp, the
  commit gate and the guarantee arm read no verdict; a round record quoting
  it was refused, and `## Not verified` rows below it went uncounted. A code
  span opened first now wins, as in CommonMark. A comment that never closes
  in a `guarantee.md` is refused at the line that opened it.

### Changed

- **`## Not verified` says nothing is left with the no-change block (#1000).**
  An `overview.md` whose `## Not verified` holds no table writes `- nothing`
  with its one field `why:`, the block `## Rule changes` already uses, in
  place of `none — <why>`. `unverified-check` refuses the old line and every
  near miss of the block at its line, naming the block, so an installed
  repository's overviews carrying `none — <why>` fail at the next pull
  request until rewritten. A base revision still reads the old line as no
  rows.
- **The sealer's verdict line is read whole (#1000).** It is exactly one of
  `Verdict: sealed`, `Verdict: withheld reason: <reason>` or
  `Verdict: undecided question: <question>`, at the start of its line and
  with no emphasis. Any other
  line that means the verdict, `Verdict: withheld — <reason>`, `Verdict:
  Sealed` and `**Verdict:** sealed` among them, is refused at its line
  naming the three shapes, and neither draws the stamp nor is judged by the
  commit gate as `sealed`. An earlier run on the `Target SHA` row carries
  its verdict's word alone, `; earlier run: <sha> <word>`, and any other
  entry is refused at that row. A `Claims re-run` result that fails reads
  `does not hold: <what came back>`.
- **The round record's old spellings are a table of their own (#1000).**
  `docs/the-review-record.md` §*The round record* keeps the grammar table
  with the twelve rows the check reads, and `Target SHA:`, `refixes:` and
  `fix of a fix:` move under it to `| Old spelling | Means |`, each cell one
  code span. A line in an old spelling is refused as the label its `Means`
  names, as before. `chain_check.py` stops at exit 2 naming the document
  where that table is missing, a cell is not one code span, a `Means` is no
  label, a spelling is a label or stands twice.
- **The release pull request's title is `release: X.Y.Z symptoms: <the
  symptoms the release answers>` (#1000).** `docs/release-checklist.md`
  §*5* gives the command, and `publish-release.yml` reads the line from the
  tagged merge commit whole, so the release that ships this is the first
  whose session types it. Any other line, the old `release: X.Y.Z —
  <symptoms>` among them, publishes the note under the tag name, exit 0, and
  the job log names the shape it expected and the first `release:` line it
  found. The published title keeps its `X.Y.Z — <symptoms>` form, and no
  published release is touched.
