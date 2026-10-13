"""Whether a line is live is asked by what the line does (#872).

Seven readers decide whether a ledger or record line is live, and they give
three answers, because they read three kinds of line:
`docs/the-evidence-ledger.md` §*The fold, and what tells it from a deletion*
states the rule under the marker of work item 1791852615. This module is the
one place the seven stand side by side. Each per-reader module owns that
reader's edges; this one pins only the answer each reader's docstring, or the
statement, already gives on a small corpus of shapes, so a reader whose answer
moves on one shape is a red cell naming the reader and the shape.

A cell no docstring answers in so many words is answered by the reader's
stated bias, and `BY_BIAS` names each such cell rather than leaving it to look
like a quotation. The table pins stated directions and discovers no edges: a
shape nobody stated an answer for is not in it.
"""

import importlib.util
import os
import re
import sys

import pytest
from conftest import load_hook_module

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
STATEMENT_DOC = os.path.join(ROOT, "docs", "the-evidence-ledger.md")
MARKER = "<!-- specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules -->"


def _load(name, relative):
    """A script by path, registered under NAME first, the way the per-reader
    modules load the same files."""
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, relative))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


checker = _load(
    "specseal_checker_for_liveness", "skills/evidence-check/scripts/evidence_check.py"
)
reader = _load(
    "specseal_reader_for_liveness", "skills/verify/scripts/unverified_check.py"
)
settle = _load("specseal_settle_for_liveness", "skills/settle/scripts/settle.py")
riders = _load("specseal_riders_for_liveness", ".github/scripts/rider_check.py")
config = load_hook_module("config.py", "specseal_config_for_liveness")

WORK_ITEM = "1700000001-alpha"
# One ledger row, anchored inside a work item's directory so `anchored_rows`
# has something to name, and spelled as a table row so every other reader
# reads the same line.
ROW = (
    f'| a claim | `seal/specs/{WORK_ITEM}/spec.md#"# alpha"@abcdef12` '
    "| read | 2026-01-01 | |"
)

# --- the corpus --------------------------------------------------------------

SHAPES = {
    "a fence that closes": ["intro", "", "```", ROW, "```", "", "after"],
    "a fence nobody closed": ["intro", "", "```", ROW, "", "after"],
    "a comment that closes": ["intro", "", "<!--", ROW, "-->", "", "after"],
    "a comment nobody closed": ["intro", "", "<!--", ROW, "", "after"],
    "a mid-line comment before the row": [
        "intro",
        "",
        "text <!-- aside --> " + ROW,
        "",
        "after",
    ],
    "a plain line": ["intro", "", ROW, "", "after"],
    # The one shape markdown will not answer without a block model: the
    # backtick on the first line is literal if the paragraph ends first, and a
    # code span reaching the third line if it does not. Under the first
    # reading the row is inside a comment; under the second it is not.
    "a lone backtick leaves the comment in doubt": [
        "intro with a ` lone run",
        "<!--",
        "the partner ` here",
        ROW,
        "-->",
        "",
        "after",
    ],
}

ORDER = list(SHAPES)


def row_index(lines):
    return next(i for i, line in enumerate(lines) if ROW in line)


def as_text(lines):
    return "\n".join(lines) + "\n"


# --- one adapter per reader: is the row's line READ? ------------------------


def checker_quoted_lines(lines, tmp_path):
    """Read where the index is absent from the set the ledger walk skips."""
    return row_index(lines) not in checker.quoted_lines(lines)


def checker_claim_lines(lines, tmp_path):
    """Read where a `(number, text)` pair names the row's line."""
    number = row_index(lines) + 1
    return any(n == number for n, _ in checker.claim_lines(lines))


def settle_anchored_rows(lines, tmp_path):
    """Read where the retirement guard names the row, over a ledger holding
    the shape and a directory its anchor points into."""
    (tmp_path / "seal" / "specs" / WORK_ITEM).mkdir(parents=True)
    (tmp_path / "seal" / "ledger.md").write_text(as_text(lines), encoding="utf-8")
    number = row_index(lines) + 1
    return any(
        row.line == number for row in settle.anchored_rows(str(tmp_path), [WORK_ITEM])
    )


def rider_quoted_lines(lines, tmp_path):
    """Read where the index is absent from the rider check's quoted set."""
    return row_index(lines) not in riders.quoted_lines(lines, as_text(lines))


def unverified_live_lines(lines, tmp_path):
    """Read where the flag beside the row's line is True."""
    return list(reader.live_lines(lines))[row_index(lines)][1]


def config_hidden_lines(lines, tmp_path):
    """Read where the index is absent from the map of hidden lines."""
    hidden, _opened = config.hidden_lines(lines, as_text(lines))
    return row_index(lines) not in hidden


def unverified_readable(lines, tmp_path):
    """Read where the row's line comes back non-blank."""
    return bool(reader.readable(as_text(lines))[row_index(lines)].strip())


# --- the table ---------------------------------------------------------------

HOLDS, EXCUSES, COUNTS = "holds", "excuses or declares", "counts"
R, N = "read", "not read"

# reader: (its adapter, the answer it gives, how the statement spells it,
#          and its answer on each shape in ORDER)
TABLE = {
    "evidence_check.py#quoted_lines": (
        checker_quoted_lines,
        HOLDS,
        "checker's `quoted_lines`",
        (N, R, R, R, R, R, R),
    ),
    "evidence_check.py#claim_lines": (
        checker_claim_lines,
        HOLDS,
        "`claim_lines`",
        (N, R, N, R, R, R, N),
    ),
    "settle.py#anchored_rows": (
        settle_anchored_rows,
        HOLDS,
        "`settle.py#anchored_rows`",
        (R, R, R, R, R, R, R),
    ),
    "rider_check.py#quoted_lines": (
        rider_quoted_lines,
        HOLDS,
        "rider check's `quoted_lines`",
        (N, R, R, R, R, R, R),
    ),
    "unverified_check.py#live_lines": (
        unverified_live_lines,
        EXCUSES,
        "`unverified_check.py#live_lines`",
        (N, N, N, N, R, R, N),
    ),
    "config.py#hidden_lines": (
        config_hidden_lines,
        EXCUSES,
        "`hooks/config.py#hidden_lines`",
        (N, N, N, R, R, R, N),
    ),
    "unverified_check.py#readable": (
        unverified_readable,
        COUNTS,
        "`unverified_check.py#readable`",
        (N, N, N, N, R, R, N),
    ),
}

# The cells answered by the reader's stated bias rather than by a sentence of
# its docstring naming the shape.
BY_BIAS = {
    # "a line begins live when it begins outside a fenced block, outside an
    # HTML comment" -- a region nobody closed runs to the end of the file, and
    # a line inside it begins inside it.
    ("unverified_check.py#live_lines", "a fence nobody closed"),
    ("unverified_check.py#live_lines", "a comment nobody closed"),
    # Where the walk is unsure the fence-only reading stands, and that reading
    # hides no line for a comment of any kind.
    ("config.py#hidden_lines", "a mid-line comment before the row"),
    # "no comment text": `comment_scan` stays inside a comment to the end of
    # the file, as `blank_fences` does for a fence it says so of.
    ("unverified_check.py#readable", "a comment nobody closed"),
}

CELLS = [
    pytest.param(name, shape, id=f"{name} on {shape}")
    for name in TABLE
    for shape in ORDER
]


@pytest.mark.parametrize("name, shape", CELLS)
def test_each_reader_gives_its_stated_answer_on_each_shape(name, shape, tmp_path):
    """S4. One cell per reader and shape: the reader, asked through its
    adapter whether the row's line is read, gives the answer the table states.
    The id names the reader and the shape, so a direction that moves is read
    off the failure line."""
    adapter, _answer, _spelling, answers = TABLE[name]
    want = answers[ORDER.index(shape)]
    got = R if adapter(SHAPES[shape], tmp_path) else N
    assert got == want, (
        f"{name} gives {got!r} on {shape!r}; the table states {want!r}"
        + (" (by its stated bias)" if (name, shape) in BY_BIAS else "")
    )


def test_every_row_answers_every_shape_and_names_a_stated_cell():
    """The table is square, and every `BY_BIAS` label names a cell in it."""
    for name, (_adapter, answer, _spelling, answers) in TABLE.items():
        assert len(answers) == len(ORDER), name
        assert answer in (HOLDS, EXCUSES, COUNTS), name
    for name, shape in BY_BIAS:
        assert name in TABLE and shape in SHAPES, (name, shape)


def statement():
    """The statement under this work item's marker, to the next marker or
    heading."""
    with open(STATEMENT_DOC, encoding="utf-8") as handle:
        lines = handle.read().split("\n")
    start = lines.index(MARKER) + 1
    body = []
    for line in lines[start:]:
        if line.startswith("<!-- specs/") or re.match(r"#{1,6} ", line):
            break
        body.append(line)
    return "\n".join(body)


def bullets(text):
    """{answer: the bullet that states it}, keyed by the capitalised word the
    bullet opens on."""
    keys = {"HOLDS": HOLDS, "EXCUSES": EXCUSES, "COUNTED": COUNTS}
    found = {}
    for chunk in re.split(r"\n(?=- \*\*)", text):
        for word, answer in keys.items():
            if chunk.startswith("- **") and word in chunk.split("**")[1]:
                found[answer] = " ".join(chunk.split())
    return found


def test_the_statement_names_each_reader_under_its_answer():
    """S1. The statement in `docs/` and this table say the same thing: every
    reader is named in the bullet of the answer the table gives it, and in no
    other bullet."""
    found = bullets(statement())
    assert set(found) == {HOLDS, EXCUSES, COUNTS}, sorted(found)
    for name, (_adapter, answer, spelling, _answers) in TABLE.items():
        assert spelling in found[answer], (name, answer)
        for other, text in found.items():
            if other != answer:
                assert spelling not in text, (name, other)
