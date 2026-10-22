"""Every file the plugin reads or writes names its encoding (#741).

The census itself, and the hook entry points' `console.to_utf8()`, are the
`encoding` and `entry_point` censuses in `tests/censuses.py` since #942,
with their cases in `tests/test_censuses.py`. Two cases stay here until the
batch that places them: the one that reads `CONTRIBUTING.md`'s prose, which
is #923's, and the one that reads `hooks/commit-review-gate.py`, which goes
to that module's file.
"""

import os

from conftest import load_hook_module

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def test_the_rule_is_where_a_contributor_reads_it():
    """`CONTRIBUTING.md`'s House rules names the rule and the censuses that
    hold it, the way *No real identifiers* names its own."""
    with open(os.path.join(ROOT, "CONTRIBUTING.md"), encoding="utf-8") as f:
        text = f.read()
    rules = text.split("\n## House rules\n", 1)[1].split("\n## ", 1)[0]
    flat = " ".join(rules.split())
    assert "**Every file read or written names its encoding.**" in flat, flat
    assert 'The call names `encoding="utf-8"`.' in flat
    assert "The `encoding` and `entry_point` censuses in `tests/censuses.py`" in flat
    assert "opens its `__main__` with `console.to_utf8()`" in flat


def test_a_mark_that_is_not_utf8_reads_as_text_rather_than_raising(tmp_path):
    """#741's D7, at the one hook read whose handler catches `OSError` alone.

    On a cp1252 machine the unnamed read never raised, because cp1252 decodes
    almost any byte; strict UTF-8 raises `UnicodeDecodeError`. Inside a hook
    that raise reaches `dispatch.py`'s `except Exception`, which is an allow,
    so naming the encoding must not be what turns a stray byte into a pass."""
    crg = load_hook_module("commit-review-gate.py", "crg_for_the_encoding_case")
    git_dir = tmp_path / ".git"
    git_dir.mkdir()
    (git_dir / "specseal-reviewed").write_bytes(b"\xffabc\n")
    got = crg.read_mark(str(tmp_path), ".git", "specseal-reviewed")
    assert got == "\N{REPLACEMENT CHARACTER}abc", repr(got)
