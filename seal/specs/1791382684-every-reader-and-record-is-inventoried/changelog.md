### Added

- **Every reader and record of 0.20.0 is inventoried (#834).** The work
  item's `inventory/` (`seal/specs/1791382684-every-reader-and-record-is-inventoried/inventory/`,
  read at the `v0.21.0` tag once `settle --retire` removes the directory) holds 1,467 reader rows across six parts — each unit,
  what it reads, what it decides, its input class (`owned`, `observed`,
  `guess`), where input it does not understand ends, and where the
  same judgment is copied — beside 35 record mechanisms with what each cost
  since 0.18.0, and the 63 issues since 0.18.0 by family. The decisions it
  led to are their own issues in this release.

- **The reader registry says where a `Reads:` line's direction is read
  (#834).** In `docs/the-reader-registry.md`, the direction word names where
  an input the unit does not understand ends, followed to the decision its
  value feeds, so a helper's direction is read at its callers and not on its
  own body. It is the meaning the inventory's `Unknown` column was settled
  on, after a reading of the helper's body alone kept giving the wrong word.
