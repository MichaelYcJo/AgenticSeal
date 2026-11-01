### Fixed

- **A `--case` name that no case answers is named once, however often it is given (#1228).** `evals/scripts/replay_targets.py` and `evals/scripts/seed_defects.py` name on stderr each `--case` name they did not write, or with `--list` each name no listed line answers, since #1150. A name given twice was named twice, so a person read one name as two failures. Each generator now reads each `--case` name once, in the order first given, as each module's docstring says ("A name given twice is one name."). The exit codes and the line each name gets are unchanged.
