"""The gaps memo's template, and the fence walks the record readers share.

`test_the_memo_holds_what_went_out_unproved_and_what_was_not_taken` reads
the headings of `templates/records/sdd-gaps.md`.
`test_the_fence_walks_agree_shape_by_shape` holds `lib/blocks.py` and
`lib/tables.py#fence_map` to `lib/lines.py#fence_spans`, a check across
modules. The cases of `lib/gaps.py` stand in `tests/lib/test_gaps.py`, those
of `skills/verify/scripts/unverified_check.py` in
`tests/skills/test_unverified_check.py`, and the cases that call `settled`
for `chain_check.py` and `settle.py` in `tests/skills/test_chain_check.py`
and `tests/skills/test_settle.py`.
"""

import importlib.util
import os

import pytest
from conftest import ROOT, load_lib_module

# No TARGET: its cases hold one fence walk across lib/blocks.py, lib/tables.py and lib/lines.py, and read the headings of templates/records/sdd-gaps.md.


lines_reader = load_lib_module("lines.py", "lines_for_the_rows_that_close")


def test_the_memo_holds_what_went_out_unproved_and_what_was_not_taken():
    """#1148. The purpose restated the changelog fragment, the divergence
    table copied the phase records, and nothing wrote the fed-back clauses,
    so the memo is the two sections it is the home of, and the scope line on
    the ladder's second rung. How the skill says so is the proofer's to
    read."""
    with open(
        os.path.join(ROOT, "templates", "records", "sdd-gaps.md"), encoding="utf-8"
    ) as f:
        headings = [line for line in f.read().splitlines() if line.startswith("## ")]
    # The template's three headings: `## Not verified` is the one
    # `lib/gaps.py` reads, and the crafter writes under all three.
    assert headings == ["## Scope confirmation", "## Not verified", "## Not done"], (
        headings
    )


FENCE_SHAPES = [
    ["```", "x", "```"],
    ["~~~", "x", "~~~"],
    ["   ```", "x", "   ```"],
    ["    ```", "x", "    ```"],
    ["```", "x", "    ```", "y", "```"],
    ["```python", "x", "```"],
    ["```", "x", "```python", "y", "```"],
    ["```", "x", "```   ", "y"],
    ["````", "```", "x", "````"],
    ["```", "x", "``````", "y"],
    ["```", "x", "~~~", "y", "```"],
    ["~~~", "```", "x", "~~~"],
    ["```x`", "y", "```"],
    ["``` `x`", "y"],
    ["~~~ `x`", "y", "~~~", "z"],
    ["``", "x", "``"],
    ["```", "x", "y"],
    ["a", "```\r", "x\r", "```\r", "b\r"],
    ["| a |", "```", "| b |", "```", "| c |"],
]


@pytest.mark.parametrize("lines", FENCE_SHAPES, ids=range(len(FENCE_SHAPES)))
def test_the_fence_walks_agree_shape_by_shape(lines):
    """The delimiter rule is written once, in `lib/blocks.py`, and three
    walks still apply it, each with its own state: `lines.py#fence_spans`,
    `blocks.fence_only`, and the walk behind `lib/tables.py#fence_map`.
    They agree on which lines are fenced and on where a block that never
    closes opened."""
    from conftest import load_lib_module

    spec = importlib.util.spec_from_file_location(
        "agentic_tables_for_fence_walks",
        os.path.join(ROOT, "lib", "tables.py"),
    )
    tables = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tables)
    blocks = load_lib_module("blocks.py", "agentic_blocks_for_fence_walks")
    fenced = set()
    for first, last in lines_reader.fence_spans(lines):
        fenced.update(range(first, len(lines) if last is None else last + 1))
    unclosed = [
        first for first, last in lines_reader.fence_spans(lines) if last is None
    ]
    shown, opened_at = tables.fence_map(lines)
    assert fenced == set(range(len(lines))) - {n for n, _ in shown}
    assert unclosed == ([] if opened_at is None else [opened_at])
    assert blocks.fence_only(lines) == (fenced, opened_at)
    walked = blocks.walk(lines)
    claimed = {n for n in range(len(lines)) if not walked.uncertain[n]}
    assert set(walked.hidden()) & claimed == fenced & claimed
