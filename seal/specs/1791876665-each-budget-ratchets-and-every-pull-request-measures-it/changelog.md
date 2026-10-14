### Added

- **This repository holds its own size and speed to written ceilings, and
  every pull request is measured against them.** `seal/budgets.md` names each
  budget — every agent's preload and `CLAUDE.md` in bytes, the suite's
  seconds, each slow test file, each `docs/` file's history lines, and each
  CI leg's minutes — and `.github/scripts/budget_check.py` measures them.

  1. A gate row fails a pull request that takes it over its ceiling. A row
     the tree alone decides also fails one that leaves the ceiling far above
     a cleanup's new reading, so the next change starts from the cleanup
     rather than from its headroom.
  2. A ceiling raised or a slack widened since the merge base needs one line
     in the pull request body, `Budget raised: <name> <old> -> <new>:
     <reason>`, read by CI so that nobody is asked; a release pull request
     asks for none.
  3. The suite's seconds and each slow file are read off one run's
     `.test_durations`, so they are held to a ceiling 1.3 times their
     reading with no lower band. A refresh restates one number, its price
     level, rather than every seconds ceiling, so a refresh on faster or
     slower runners fails nothing, and a cleanup of one file moves only that
     file.
  4. Each leg's minutes are read off the run itself by a `budgets` job
     after the suite, held to a ceiling with no lower band, and printed with
     the run's billable minutes.
  5. Two reports fail nothing: the largest round records in the tree, and
     how many rows a release re-read. A release pull request prints every
     budget against the last release tag.

  A contributor's pull request that touches none of the measured files sees
  one more green step and one more green job.
  (`1791876665-each-budget-ratchets-and-every-pull-request-measures-it`,
  #930)

### Changed

- **The broad gate's seal counts the budget step among the steps it does not
  answer.** A feature seal of SpecSeal now reads `CI also · 5 more steps`,
  five of the ten CI runs for that base, and a release seal `· 9 more steps`.
  (`1791876665-each-budget-ratchets-and-every-pull-request-measures-it`,
  #930)
