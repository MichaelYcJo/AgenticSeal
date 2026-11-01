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

import io
import json
import os
import runpy
import subprocess
import sys

import pytest
from conftest import (
    HOSTILE,
    KOREAN,
    ROOT,
    census_case,
    decision_of,
    load_hook_module,
)

TARGET = "hooks/lib/console.py"


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
        """The seven `console.to_utf8()` calls, bound.

        `dispatch.py` is what production spawns, and its copy of the loop is held
        by `tests/hooks/test_dispatch.py`. The per-gate calls are for the other
        documented way in -- `hooks/lib/console.py` says each gate is runnable on its
        own -- and nothing measured that: neutering `to_utf8` to a bare `return`
        left the suite at its own baseline, so all seven could be deleted and the
        tree stays green. The gate run is the routing check at the edit tools,
        whose refusal names the repository's path, which holds `KOREAN`.
        """
        r = subprocess.run(
            [sys.executable, os.path.join(ROOT, "hooks", "routing-edit-gate.py")],
            input=json.dumps(
                {
                    "tool_name": "Write",
                    "session_id": f"solo-{encoding}",
                    "cwd": str(korean_repo),
                    "tool_input": {"file_path": str(korean_repo / f"{KOREAN}.txt")},
                },
                ensure_ascii=False,
            ).encode("utf-8"),
            capture_output=True,
            timeout=30,
            env={**os.environ, "PYTHONIOENCODING": encoding, "PYTHONUTF8": "0"},
        )
        assert decision_of(r) == "deny", (
            f"{encoding}: the gate went silent on its own, which the harness reads "
            f"as approval. stderr: {r.stderr.decode('utf-8', 'replace')[-300:]}"
        )

    @pytest.mark.parametrize(
        ("script", "code"),
        [("release_report.py", 2), ("release_seal.py", 0), ("rules.py", 2)],
    )
    def test_a_release_script_run_on_its_own_gives_the_answer_streams_holds(
        self, monkeypatch, script, code
    ):
        """Each of these scripts spells the loop inline, because it loads the
        tree's modules only when first asked, and this case holds its copy to
        `STREAMS` read at run time. Run with no argument and no `TAG`, each
        ends at its `main`'s own verdict: exit 2 for the two that refuse a
        missing argument, and `release_seal.py`'s `no seal:` at exit 0, which
        never fails a release."""
        console = load_hook_module("lib/console.py", "console_for_release_scripts")
        path = os.path.join(ROOT, ".github", "scripts", script)
        streams = {name: cp949_stream() for name, _ in console.STREAMS}
        for name, stream in streams.items():
            monkeypatch.setattr(sys, name, stream)
        monkeypatch.setattr(sys, "argv", [path])
        monkeypatch.delenv("TAG", raising=False)
        with pytest.raises(SystemExit) as ended:
            runpy.run_path(path, run_name="__main__")
        said = {name: (s.encoding, s.errors) for name, s in streams.items()}
        assert (ended.value.code, said) == (
            code,
            {name: ("utf-8", errors) for name, errors in console.STREAMS},
        )


test_census = census_case(TARGET)
