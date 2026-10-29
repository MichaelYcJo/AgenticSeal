"""The frozen reading never grows (#692, phase 5: S11 under the owner's answer
of 2026-10-01).

`hooks/lib/cmdline_base.py` is `86256492`'s reader, kept frozen. What keeps
that from becoming milestone 49 again is that the file cannot gain a rule:
its bytes below the rider are `86256492:hooks/cmdline.py`, and a change has
to delete a case here first.
"""

import hashlib
import subprocess
from pathlib import Path

import conftest
import pytest

ROOT = Path(conftest.ROOT)
FROZEN = ROOT / "hooks" / "lib" / "cmdline_base.py"
# The reader the bytes below the rider are, at the commit and path it stood at.
PINNED = "86256492:hooks/cmdline.py"
BASE = PINNED.split(":", 1)[0]
START = b'"""Reading a shell command line'

# sha256 of `86256492:hooks/cmdline.py` from its docstring on -- the file less
# its shebang line, which the rider sits under. Computed 2026-10-01 from
# `git show 86256492:hooks/cmdline.py`; the case below also compares against
# git itself wherever the commit is reachable (CI checks out full history).
SHA256 = "ad528c48388d3a5a84f22d073c29e2d90c7575d15a8a50afdc0cda8e4c5bd6e2"


def below_the_rider(data):
    return data[data.index(START) :]


def test_the_bytes_below_the_rider_are_86256492s():
    mine = below_the_rider(FROZEN.read_bytes())
    assert hashlib.sha256(mine).hexdigest() == SHA256, (
        "hooks/lib/cmdline_base.py changed below its rider. It is pinned to "
        f"{PINNED}: a rule added to the frozen reading is the "
        "stopped class (#692), and this case has to go before it can"
    )
    shown = subprocess.run(
        ["git", "-C", str(ROOT), "show", PINNED],
        capture_output=True,
        timeout=60,
    )
    if shown.returncode != 0:
        pytest.skip(f"{BASE} is not reachable here; the hash above still held")
    assert below_the_rider(shown.stdout) == mine
    assert shown.stdout[: shown.stdout.index(START)] == b"#!/usr/bin/env python3\n"
