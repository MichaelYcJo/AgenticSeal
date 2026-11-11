"""Every file the plugin reads or writes names its encoding (#741).

The census itself, and every entry point's answer to the streams, are the
`encoding` and `entry_point` censuses in `tests/censuses.py` since #942,
with their cases in `tests/test_censuses.py`. What stays here reads
`CONTRIBUTING.md`'s prose, which is #923's.
"""

import os

from conftest import ROOT


def test_the_rule_is_where_a_contributor_reads_it():
    """`CONTRIBUTING.md`'s House rules names the argument the rule asks for
    and the censuses that hold it, the way *No real identifiers* names its
    own."""
    with open(os.path.join(ROOT, "CONTRIBUTING.md"), encoding="utf-8") as f:
        text = f.read()
    rules = text.split("\n## House rules\n", 1)[1].split("\n## ", 1)[0]
    flat = " ".join(rules.split())
    # The argument a contributor writes into the call.
    assert '`encoding="utf-8"`' in flat, flat
    # The two censuses a contributor resolves in `tests/censuses.py`.
    for census in ("`encoding`", "`entry_point`"):
        assert census in flat, census
    # The unit that reads the one form of a loop over the pairs.
    assert "`tests/censuses.py#loop_pairs`" in flat
