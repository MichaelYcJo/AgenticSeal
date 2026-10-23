"""A declaration that cannot be decoded is not an answer.

This file held the cases of a console the gates cannot encode to. The
dispatcher's moved to `tests/test_dispatch.py` and `hooks/console.py`'s to
`tests/test_console.py` (#942's phase 6). What stays is `hooks/routing.py`'s
case, which waits for routing's group.
"""

import os
import sys

from conftest import ROOT, opted_in_repo


def test_a_declaration_that_cannot_be_decoded_is_not_an_answer(tmp_path):
    """`hooks/routing.py` caught `OSError` only, and `UnicodeDecodeError` is a
    `ValueError`. An undecodable `routing.md` raised out of `declarations()`,
    through the commit gate, into `dispatch.py`'s `except Exception: return ""`
    — no output, which is an allow.

    The direction the module states is "no declaration", which means the gate
    goes back to asking. Not silence: silence would make a corrupt file into a
    standing waiver.
    """
    sys.path.insert(0, os.path.join(ROOT, "hooks"))
    import routing

    repo = opted_in_repo(tmp_path / "declared" / "repo")
    item = repo / "seal" / "specs" / "1780000000-work"
    item.mkdir(parents=True)
    # Valid UTF-16, which is not valid UTF-8 anywhere in it.
    (item / "routing.md").write_bytes(
        "| Review | through the review chain |\n".encode("utf-16")
    )
    assert routing.declarations(str(repo)) == []
