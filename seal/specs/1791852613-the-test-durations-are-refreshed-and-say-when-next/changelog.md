### Changed

- **`.test_durations` is measured again, and a case now says when it is
  measured next (#874).** The file had stopped pricing 1,276 of the suite's
  13,480 cases (9.5 %). `pytest-split` gives an unpriced case the file's
  mean, so the shards drifted apart and nothing reported it.
  - The file was refreshed by `CONTRIBUTING.md`'s recipe, as one Windows job
    with `--store-durations` in run 38332345615, which took 37 m 21 s. It
    now prices every case as Windows collects it. 213 parametrized cases
    whose ids carry a path stay unpriced on ubuntu and macOS (1.6 %),
    because Windows writes those ids with a backslash.
  - After the refresh, the slowest Windows shard runs 1.05 times the mean
    shard and the slowest macOS shard 1.03 times, by pytest's own seconds
    in run 38335775781. The slowest Windows job took 11 m 27 s.
  - `test_the_durations_file_prices_the_suite` fails when more than one
    collected case in twenty has no price (`STALE_SHARE`). Its message names
    the counts and the recipe. It reads the whole collection on every shard,
    and skips when one module is named on its own.
    `bin/test tests -q -k test_the_durations_file_prices_the_suite` runs it
    alone.
  - The release checklist refreshes the file at each release's preparation.
    When the case goes red mid-cycle, the contributor runs the recipe in
    `CONTRIBUTING.md` §Running the checks, whose measuring leg now has a
    budget of 60 minutes.
  - No leg's `timeout` changed. The comment beside the values now names the
    slowest run of each leg: ubuntu 9 m 43 s, a macOS shard 8 m 29 s, and a
    Windows shard 12 m 42 s.
