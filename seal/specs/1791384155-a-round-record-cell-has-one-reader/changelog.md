### Changed

- **A run with no pull-request payload is no longer told it is a draft
  (#866).** `round-record new`, `close` and `seal` used to hand the chain
  check a draft payload whenever `gh` was absent, failed or said draft, and
  the broad gate did the same for its chain arm; on a machine without `gh`
  every local run was a draft, which excused the unchecked `Pass`, the empty
  `rounds/` and `nobody` beside `Pass`. The check now reads the payload where
  GitHub wrote one, else asks `gh pr view --json isDraft` itself, else judges
  the pull request ready and prints every source it tried. Where no payload
  exists and no `gh` can answer, those three commands now exit 1 on the
  record they just wrote. The broad gate's chain arm passes `--sealing`
  instead, which excuses only the last record's `Broad gate` cell — the one
  that run is about to write — and says so on the state line.

### Fixed

- **A round-record cell is read by one reader, in `chain-check`, and every
  other script reads it through that one (#866).** Five judgments were each
  read two to four ways that disagreed:
  - the broad gate's `rounds` row drew `capped` for a bare `yes` and for
    `yesterday …` and missed `**yes — …**`; it reads `Needs a fix` as the gate
    does, and a cell the gate cannot read prints the count alone;
  - a deferral's home is what stands after `deferred` up to the first ` — `,
    as `close` writes it. The panel names that home, the release seal counts
    an issue only where the home is exactly `#N`, and `close` writes the
    rest of the cell into the grounds rather than into the verdict;
  - the depth refusal reads a finding's `Location` the way a fix of a fix
    does, so a name with no `.py` path beside it places nothing;
  - the floor's two walks, the run cut and the premature-gate test are one
    function each, shared by the check and the generator;
  - a doubled close counts only `close`'s own prefixes at the head of the
    Grounds cell, so a reviewer's sentence quoting an earlier close is not
    one, and a field row or a `Pass` box written twice fails at the pull
    request, as the generator already refused.
