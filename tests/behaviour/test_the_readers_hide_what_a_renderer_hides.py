"""The readers under `lib/` hide what a CommonMark renderer hides, and nothing else
(#667).

The acceptance property is below.
For every line L of a document, with `base(L)` a reader's reading at
`release/v0.16.0` and `renderer(L)` the oracle's:

  1. the reader never leaves both -- `new(L)` is `base(L)` or `renderer(L)`;
  2. where the walk claims to be exact, it is -- every line it does not call
     uncertain is classed as the oracle classes it;
  3. on every shape `tests/block_shapes.py` holds, the reader gives its
     expected answer.

The oracle comes first, and it is the first thing held: before any reader
moved, it had to give `RENDERER` on every shape, which was derived by
reading the specification and could not be executed. This module holds the
oracle, `tests/commonmark_oracle.py`, and nothing else.

Each reader is held in its own module file, over those shapes and the
seeded generated corpus `tests/lib/test_blocks.py` builds: half 1 in
`tests/lib/test_tables.py`'s `Test_unfenced` and `tests/lib/test_routing.py`'s
`Test_module`, half 2 in `tests/lib/test_blocks.py`'s `Test_walk` and
`Test_walk_text`, where #1489's phase 3 moved them from here, and half 3 in
each reader's own case table (#942's phase 6).
"""

import os

import commonmark_oracle as oracle
from conftest import ROOT, imported_roots

# --- the oracle is independent, and it says what the frame read -------------


def test_the_oracle_imports_the_parser_and_nothing_of_this_repositorys():
    """S1. The oracle shares no code with the walk it checks: its only
    import is the parser, and it reaches for no path of this repository's.
    Round 3 of 1790635413: "The oracle cannot catch this, because it is
    built the same way." The shape data it is checked on imports nothing."""
    assert imported_roots(oracle.__file__) == {"markdown_it"}
    with open(oracle.__file__, encoding="utf-8") as handle:
        source = handle.read()
    # `tests/commonmark_oracle.py` *It shares nothing with what it checks*:
    # the oracle's code reaches nothing under `lib/`, `skills/` or
    # `.github/`, by a path or through the import machinery.
    for reach in ("sys.path", "importlib", "lib/", "skills/", ".github"):
        assert reach not in source.split('"""', 2)[-1], reach
    assert imported_roots(os.path.join(ROOT, "tests", "block_shapes.py")) == set()
