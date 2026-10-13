### Changed

- **Every `tests` run measures `.test_durations`, and the case that says
  when to refresh it is the whole schedule (#931).** 0.21.1 skipped the
  release checklist's refresh box on its first use, because the box asked
  for a 35-minute measuring run a person had to dispatch.
  - Each Windows shard now runs with `--store-durations --clean-durations`
    and uploads the part it measured, and a new `durations` job unions the
    four parts into the `test-durations` artifact, kept seven days. Its
    summary gives each shard's measured seconds, their spread, and the union
    against the committed file. A part that is missing, an id in two parts,
    or a part that does not parse fails the job, and no smaller file is
    uploaded. The job took 7 s and 11 s.
  - `test_the_durations_file_prices_the_suite` now fails in two directions:
    when more than one collected case in twenty has no price, as before, or
    when more than one second in twenty of the file's belongs to cases the
    suite no longer collects. A pull request that removes a twentieth of the
    suite's time therefore brings the fresh file with it. Its message gives
    the refresh: `gh run download <run id> -n test-durations -D <dir>`, move
    the file over the committed one, commit it. The download needs a
    directory of its own, because `gh` will not write over an existing file.
  - The checklist's refresh box, the measuring run and its recipe are gone
    from `docs/release-checklist.md` and `CONTRIBUTING.md`.
  - The committed file is the first union, from run 38475370013: 13,930
    entries, every collected case priced, none left over. The old file left
    476 cases unpriced (3.4 %). Divided by the new file, the slowest Windows
    shard ran 1.12 times the mean by pytest's own clock, inside the 1.10 to
    1.20 the old file gave over six runs.
  - The shards price cases 1.07 times what the single job that measured the
    old file did, a runner's price level rather than growth in the suite;
    the shards' part ratios move with the runner a group lands on, so no
    scaling is applied to the union.
