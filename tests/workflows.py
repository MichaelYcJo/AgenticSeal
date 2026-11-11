"""The suite's one reading of a workflow file (#1486).

A case that reads a job, a step or a key of `.github/workflows/*.yml` or
`templates/setup/hygiene.yml` reads what `load` returns. The file is parsed
by PyYAML, pinned in `.github/scripts/run_tests.py#PYYAML`, so no case reads
a workflow's structure by indentation or by a regular expression over lines.

**`yaml.BaseLoader`, not `yaml.safe_load`.** PyYAML reads YAML 1.1, where a
bare `on` is a boolean, so `safe_load` returns the trigger key of every
workflow as `True`, and `15` as an integer. GitHub reads `on` as a key. The
base loader resolves no scalar: every value is a string as it is written,
`''` for an empty one, so the trigger key is `"on"` and a case compares
strings.

A parser drops comments, so a case whose subject is a comment reads it from
the file's text.

This module sits beside `tests/commonmark_oracle.py` and imports PyYAML at
its top, so a missing PyYAML fails the modules that import this one and
leaves `tests/conftest.py` importable.
"""

import os

import yaml
from conftest import ROOT


def load(path):
    """The mapping the workflow file at PATH parses to, every scalar a
    string. PATH is absolute, or relative to the repository root."""
    with open(os.path.join(ROOT, path), encoding="utf-8") as handle:
        return yaml.load(handle.read(), Loader=yaml.BaseLoader)
