"""Every file the plugin reads or writes names its encoding (#741).

The census itself, and the hook entry points' `console.to_utf8()`, are the
`encoding` and `entry_point` censuses in `tests/censuses.py` since #942,
with their cases in `tests/test_censuses.py`. The case that reads
`hooks/commit-review-gate.py#read_mark` over a mark that is not UTF-8 is in
`tests/test_commit_review_gate.py`'s `Test_module`. What stays here reads
`CONTRIBUTING.md`'s prose, which is #923's.
"""

import os

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
