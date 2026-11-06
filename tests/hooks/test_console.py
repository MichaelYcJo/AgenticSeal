"""`hooks/lib/console.py`: a console the gates cannot encode to must not turn them
into a silent pass.

The failure this holds is not "a message came out wrong". It is that a hook
which raises while reading or printing dies with **stdout empty**, and empty
stdout is exactly how a hook says "nothing to see here" -- so the failure mode
of every gate here, under a console it cannot encode to, is an approval.

`PYTHONIOENCODING` reproduces the case on any operating system, which is
deliberate: a platform-gated test would leave the branch it exists for proven
by nothing while CI runs the other one. The dispatcher keeps a reconfigure loop
of its own, and its case is `tests/hooks/test_dispatch.py`'s. The case comes from
`tests/test_console_is_not_utf8.py` (#942's phase 6).
"""

import importlib.util
import io
import json
import os
import subprocess
import sys

import pytest
from conftest import (
    HOSTILE,
    ROOT,
    census_case,
    load_hook_module,
)

TARGET = "hooks/lib/console.py"

STAMP = os.path.join(ROOT, "skills", "verify", "scripts", "seal_stamp.py")
STAMP_VALUES = {
    "tree": "aaa1111",
    "base": "bbb2222",
    "from": "origin/base",
    "item": "/x/seal/threads/1799000000-an-item",
    "session": "s-1",
    "scale": 0.9,
    "rows": [("SEALED", ""), None, ("tree", "aaa1111")],
}


def seal_stamp(name):
    spec = importlib.util.spec_from_file_location(name, STAMP)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def cp949_stream():
    """A text stream a Korean Windows console would hand the process."""
    return io.TextIOWrapper(io.BytesIO(), encoding="cp949", errors="strict")


class Test_to_utf8:
    def test_accepts_each_of_the_three_streams_and_makes_it_utf8(self, monkeypatch):
        """The streams are stand-ins, so the verdict is the same whatever
        console the case runs under."""
        console = load_hook_module("lib/console.py", "console_for_to_utf8")
        streams = {name: cp949_stream() for name in ("stdin", "stdout", "stderr")}
        for name, stream in streams.items():
            monkeypatch.setattr(sys, name, stream)
        console.to_utf8()
        said = {name: (s.encoding, s.errors) for name, s in streams.items()}
        assert said == {
            "stdin": ("utf-8", "replace"),
            "stdout": ("utf-8", "replace"),
            "stderr": ("utf-8", "backslashreplace"),
        }

    def test_refuses_to_raise_on_a_stream_that_is_absent_or_cannot_reconfigure(
        self, monkeypatch
    ):
        console = load_hook_module("lib/console.py", "console_for_absent_streams")
        stderr = cp949_stream()
        monkeypatch.setattr(sys, "stdin", None)
        monkeypatch.setattr(sys, "stdout", io.StringIO())
        monkeypatch.setattr(sys, "stderr", stderr)
        console.to_utf8()
        assert (stderr.encoding, stderr.errors) == ("utf-8", "backslashreplace")


class Test_module:
    @pytest.mark.parametrize("encoding", HOSTILE)
    def test_a_gate_run_on_its_own_still_reaches_a_verdict(self, korean_repo, encoding):
        """The gates' own `console.to_utf8()` calls, bound.

        `dispatch.py` is what production spawns, and its copy of the loop is held
        by `tests/hooks/test_dispatch.py`. The per-gate calls are for the other
        documented way in -- `hooks/lib/console.py` says each gate is runnable on its
        own -- and nothing measured that: neutering `to_utf8` to a bare `return`
        left the suite at its own baseline, so every one of them could be deleted
        and the tree stays green. The gate run is the stamp's drawer, whose
        payload names the repository's path, which holds `KOREAN`, and which
        prints the stamp waiting for the session there.
        """
        session = f"solo-{encoding}"
        stamp = seal_stamp(f"seal_stamp_for_the_console_{encoding.replace('-', '_')}")
        stamp.write_values(str(korean_repo / ".git"), session, STAMP_VALUES)
        r = subprocess.run(
            [sys.executable, os.path.join(ROOT, "hooks", "sealer-stamp.py")],
            input=json.dumps(
                {
                    "hook_event_name": "Stop",
                    "session_id": session,
                    "cwd": str(korean_repo),
                },
                ensure_ascii=False,
            ).encode("utf-8"),
            capture_output=True,
            timeout=30,
            env={**os.environ, "PYTHONIOENCODING": encoding, "PYTHONUTF8": "0"},
        )
        out = r.stdout.decode("utf-8")
        assert out.strip(), (
            f"{encoding}: the gate went silent on its own, which the harness reads "
            f"as nothing to show. stderr: {r.stderr.decode('utf-8', 'replace')[-300:]}"
        )
        assert json.loads(out)["systemMessage"].startswith("SEALED aaa1111"), out


test_census = census_case(TARGET)
