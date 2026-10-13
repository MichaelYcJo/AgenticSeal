### Changed

- **`.test_durations` is measured again, and a case now says when it is
  measured next (#874).** The file had stopped pricing 1,276 of the suite's
  13,480 cases (9.5 %). `pytest-split` gives an unpriced case the file's
  mean, so the shards drifted apart and nothing reported it.
  - Every test id is now one spelling on every machine. 205 ids built from
    a path wrote it with a backslash on Windows, and 8 carried the
    interpreter's absolute path, so a file measured on Windows could not
    price them on ubuntu or macOS. A parametrized path now takes
    `ids=posix_id` from `tests/conftest.py`, and
    `test_no_collected_id_carries_the_interpreters_path` refuses an id that
    holds `sys.executable`.
  - The file was refreshed by `CONTRIBUTING.md`'s recipe, as one Windows job
    with `--store-durations --clean-durations` in run 38342987499, which took
    34 m 15 s. It prices all 13,482 collected cases on every leg, and it
    holds no entry the suite does not collect. `--clean-durations` is now
    part of the recipe, so each refresh replaces the file instead of merging
    into it.
  - After the first refresh, the slowest Windows shard ran 1.05 times the
    mean shard and the slowest macOS shard 1.03 times, by pytest's own
    seconds in run 38335775781. The slowest Windows job took 11 m 27 s.
  - `test_the_durations_file_prices_the_suite` fails when more than one
    collected case in twenty has no price (`STALE_SHARE`). Its message names
    the counts and the recipe. It reads the whole collection on every shard,
    and skips when one module is named on its own.
    `bin/test tests -q -k test_the_durations_file_prices_the_suite` runs it
    alone.
  - The release checklist refreshes the file at each release's preparation,
    then has the macOS shards' `timeout` read again by the rule beside the
    values. When the case goes red mid-cycle, the contributor runs the recipe in
    `CONTRIBUTING.md` §Running the checks, whose measuring leg now has a
    budget of 60 minutes.
  - No leg's `timeout` changed. The comment beside the values now names the
    slowest run of each leg: ubuntu 9 m 43 s, a macOS shard 8 m 29 s, and a
    Windows shard 12 m 42 s.

- **`survivor-check` no longer reads a `.test_durations` file or the reader
  census, at any depth (#874).** Both are data keyed by test id or by unit,
  and a line either one drops was read as a corrected sentence. A durations
  refresh rewrites its file whole, and once `--clean-durations` brought the
  file under the 2 MiB size cap, 753 places were reported on one branch. A
  census line leaves `undeclared_readers.txt` when its unit starts to
  declare, and it is spelled exactly as a ledger row cites that unit, so it
  matched every released row citing the unit at that hash. The rule is the
  file's name, never its size.
