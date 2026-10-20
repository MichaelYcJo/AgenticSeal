### Changed

- **`## Not verified` says nothing is left with the no-change block (#1000).**
  An `overview.md` whose `## Not verified` holds no table writes `- nothing`
  with its one field `why:`, the block `## Rule changes` already uses, in
  place of `none — <why>`. `unverified-check` refuses the old line and every
  near miss of the block at its line, naming the block, so an installed
  repository's overviews carrying `none — <why>` fail at the next pull
  request until rewritten. A base revision still reads the old line as no
  rows.
