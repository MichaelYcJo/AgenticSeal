### Changed

- **Every `tests` run measures `.test_durations`, and the case that says
  when to refresh it is the whole schedule (#931).** 0.21.1 skipped the
  release checklist's refresh box on its first use, because the box asked
  for a 35-minute measuring run a person had to dispatch.
  - Each Windows shard now runs with `--store-durations --clean-durations`
    and uploads the part it measured, and a new `durations` job unions the
    four parts into the `test-durations` artifact. Parts and union are kept
    seven days, and a re-run of failed jobs replaces them, so a partial
    re-run days later still has every part to union. Its summary gives each
    shard's measured seconds, their spread, and the union against the
    committed file. A part that is missing, an id in two parts, or a part
    that does not parse fails the job, and no smaller file is uploaded. The
    job took 7 s and 11 s.
  - `test_the_durations_file_prices_the_suite` now fails in two directions:
    when more than one collected case in twenty has no price, as before, or
    when more than one second in twenty of the file's belongs to cases the
    suite no longer collects. A pull request that removes a twentieth of the
    suite's time therefore brings the fresh file with it. Its message gives
    the refresh: `gh run download <run id> -n test-durations -D <dir>`, move
    the file over the committed one, write its price level with
    `budget_check.py --restate-price`, commit both. The download needs a
    directory of its own, because `gh` will not write over an existing file.
    A branch with no pull request, or whose run is too old to re-run, gets a
    run with `gh workflow run test.yml --ref <branch>`.
  - The checklist's refresh box, the measuring run and its recipe are gone
    from `docs/release-checklist.md` and `CONTRIBUTING.md`.
  - The first union, from run 38475370013, held 13,930 entries: every case
    collected at that commit priced, none left over, where the file then
    committed left 476 unpriced (3.4 %). Divided by the union, the slowest
    Windows shard ran 1.12 times the mean by pytest's own clock, inside the
    1.10 to 1.20 the unsharded file gave over six runs. The committed file
    is still the one #944 measured; the next refresh the case asks for
    commits a union.
  - The shards priced cases 1.07 times what the single job that measured
    the file before them did, a runner's price level rather than growth in
    the suite; the shards' part ratios move with the runner a group lands
    on, so no scaling is applied to the union. One union moves a single test
    file 0.67 to 1.72 times the level from the next, past the 1.3 band its
    `slow-file` row was set to, on files nobody changed. The union is what
    makes that spread, so this change makes the `slow-file` rows of
    `seal/budgets.md` `report` rows: each file's reading still prints in the
    summary and fails nothing, and `suite-seconds`, the sum, stays the gate.
    A pull request that commits
    a union restates `## Price level` in `seal/budgets.md` in the same
    commit, and nobody copies the number: the new
    `budget_check.py --baseline origin/<base> --restate-price` writes the
    level the hygiene workflow's budget step holds the refresh to, and the
    recipe and the failing case's message both give that command.
