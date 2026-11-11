"""What is left of `unverified_check.py`'s old file.

#942's phase 5 rebuilt `skills/verify/scripts/unverified_check.py`'s cases
into `tests/skills/test_unverified_check.py`, one class per function. Two kinds of
case stay here, byte for byte. The cases whose assertion reads a shipped
document's prose wait for #923. `test_the_fence_walks_agree_shape_by_shape`
holds `lib/blocks.py` and `lib/tables.py#fence_map` to
`lib/lines.py#fence_spans`, a check across files, which stays where it is.
The readers these cases call moved from `unverified_check.py` to
`lib/gaps.py` and `lib/lines.py` (#1482), and the cases call them there. The case that read
`skills/code-review/scripts/chain_check.py` and
`skills/settle/scripts/settle.py` for a call of this module's `settled` judged
one file per row, so each row is now a case of its module's file,
`tests/skills/test_chain_check.py` and `tests/skills/test_settle.py`.
"""

import importlib.util
import os

import pytest
from conftest import ROOT, load_lib_module

gaps = load_lib_module("gaps.py", "gaps_for_the_rows_that_close")
lines_reader = load_lib_module("lines.py", "lines_for_the_rows_that_close")


def test_the_skill_shows_the_word(tmp_path):
    """`skills/implement/SKILL.md` *4. The closing memo — only what the diff
    cannot show* is what the memo's writer reads for how a row closes, so its
    example row is one the check accepts as closed."""
    with open(
        os.path.join(ROOT, "skills", "implement", "SKILL.md"), encoding="utf-8"
    ) as f:
        text = f.read()
    example = next(ln for ln in text.splitlines() if ln.startswith("| closed "))
    p = tmp_path / "gaps.md"
    p.write_text(
        f"# memo\n\n## Not verified\n\n| Item | Who must answer |\n|---|---|\n{example}\n",
        encoding="utf-8",
    )
    op, closed, err = gaps.check_file(str(p))
    assert not err and not op and len(closed) == 1, (op, closed, err)


def test_the_template_is_the_shape_the_checker_reads(tmp_path):
    """Template and checker drift apart silently otherwise: every new work
    item would copy a section the release check then refuses."""
    with open(
        os.path.join(ROOT, "templates", "records", "sdd-gaps.md"), encoding="utf-8"
    ) as f:
        template = f.read()

    d = tmp_path / "specs" / "1780000000-work"
    d.mkdir(parents=True)
    p = d / "gaps.md"

    p.write_text(template, encoding="utf-8")
    _, _, err = gaps.check_file(str(p))
    assert err and "placeholder" in err[0][1], (
        "a template copied and never filled in has to fail, or an empty record "
        "passes as a complete one"
    )

    filled = template.replace("<what was not verified>", "the TUI rendering").replace(
        "<who or what can answer it>", "user, on the next session"
    )
    p.write_text(filled, encoding="utf-8")
    op, _, err = gaps.check_file(str(p))
    assert not err and len(op) == 1


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
