"""Every reader of markdown or record text ends a line where GFM does (#664).

`str.splitlines` ends a line at LF, CR and CRLF, and also at U+2028, U+2029,
NEL, a form feed, VT and `\\x1c`-`\\x1e`. GFM, `ast` and git end one at the
first three alone. So below one of those eight a reader that split with
`splitlines` read lines no renderer shows: a table row cut in two, a marker or
a heading that stands mid-line read as a line of its own, a line number one
off the one `grep -n` prints, and, where the reader wrote the text back, the
character turned into a line break.

One splitter, `hooks/blocks.py#gfm_lines`, which `unverified_check.py` hands
its callers, is what
every such reader now reads, and two readers of one text split it alike. The
scenarios are `seal/specs/1790655302-every-reader-ends-a-line-where-gfm-does/
spec.md`'s at `67694cba`, numbered as it numbers them, and each was seen red at `2e392d46`
before it was committed.

Every one of the eight is built from its code point, never typed: an escape
typed into an editing tool can come back as the character itself, and a file
holding one is exactly what these cases are about.

The splitter's own cases are `tests/test_blocks.py`'s `Test_gfm_lines`
(#942's phase 6). What stays here holds every copy of it to it, three
modules on one corpus. Each other reader's case judges that reader alone,
so #942's round 9 fix pass placed it in that reader's file:
`tests/test_fold_check.py`, `tests/test_gather_changelog.py`,
`tests/test_chain_check.py`, `tests/test_payload_meter.py`,
`tests/test_issue_claims_check.py` and `tests/test_worktree_guard.py`, whose
`Test_last_active_event_epoch` already held the second transcript reader's
case. The two separators those cases name are `tests/conftest.py`'s `LS` and
`FF`.
"""

import importlib.util
import os
import sys

from conftest import texts

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
READER = os.path.join(ROOT, "skills", "verify", "scripts", "unverified_check.py")
CHECKER = os.path.join(ROOT, "skills", "verify", "scripts", "coordinates.py")
ARM_CHECK = os.path.join(ROOT, "skills", "verify", "scripts", "arm_check.py")


def _load(name, path):
    """A script by path, registered under NAME first: `arm_check.py` defines
    dataclasses, which look their own module up in `sys.modules`."""
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


reader = _load("specseal_reader_for_gfm_lines", READER)


# --- S17: one splitter, and its copies agree ---------------------------------


def test_every_copy_of_the_splitter_is_the_readers():
    """S17. The reader's split is `hooks/blocks.py`'s, which it imports since
    #1005; `arm_check._lines` splits Python source where `ast` does, ends
    kept, and the coordinate kernel asks the reader itself. All are one rule,
    held equal here."""
    checker = _load("specseal_checker_for_gfm_lines", CHECKER)
    arm_check = _load("specseal_arm_check_for_gfm_lines", ARM_CHECK)
    for text in texts():
        want = reader.gfm_lines(text)
        assert checker.gfm_lines(text) == want, repr(text)
        kept = reader.gfm_lines(text, keepends=True)
        assert checker.gfm_lines(text, keepends=True) == kept, repr(text)
        assert arm_check._lines(text) == kept, repr(text)


# S19, that no shipped reader of a document splits with `.splitlines(`, is
# the `splitlines` census in `tests/censuses.py`; each call left carries its
# exemption on the line above it.
