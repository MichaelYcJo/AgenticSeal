"""Every census in `tests/censuses.py` holds over each tracked file that no
module file runs the censuses over itself.

A module file runs every census over its own target through
`test_census = census_case(TARGET)`. The sweep here runs them over every
other tracked file, the documents and every module no module file
declares, and lists the tracked files once. It came, unchanged, from
`tests/test_censuses.py`, which keeps each census's own cases over files they
write into a temporary root.
"""

import ast
import importlib.util
import os

import censuses
from conftest import ROOT, git_listing, on_disk

# No TARGET: its case runs every census over each tracked file no module file declares.

_LAYOUT = importlib.util.spec_from_file_location(
    "agentic_layout_for_censuses",
    os.path.join(ROOT, "skills", "verify", "scripts", "test_layout.py"),
)
layout = importlib.util.module_from_spec(_LAYOUT)
_LAYOUT.loader.exec_module(layout)


def test_every_file_no_module_file_declares_meets_every_census():
    """The censuses over every tracked file whose module file does not run
    them itself: the documents, and every module no module file declares."""
    tracked, _missing = on_disk(ROOT, git_listing(ROOT, "ls-files", check=True))
    assert tracked, "git ls-files listed no tracked file, so the sweep judged nothing"
    declared = set()
    for directory, _dirs, names in os.walk(os.path.join(ROOT, "tests")):
        for name in names:
            if name.startswith("test_") and name.endswith(".py"):
                with open(os.path.join(directory, name), encoding="utf-8") as f:
                    source = f.read()
                # Only a file that runs the censuses takes its target out
                # of the sweep: one that declares and runs none leaves it
                # here, judged.
                if layout.runs_the_censuses(ast.parse(source)):
                    declared.add(layout.declared_target(source))
    found = [p for rel in tracked if rel not in declared for p in censuses.judge(rel)]
    assert not found, "\n".join(found)
