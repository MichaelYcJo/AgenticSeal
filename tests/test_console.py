"""`hooks/console.py`: a console the gates cannot encode to must not turn them
into a silent pass.

The failure this holds is not "a message came out wrong". It is that a hook
which raises while reading or printing dies with **stdout empty**, and empty
stdout is exactly how a hook says "nothing to see here" -- so the failure mode
of every gate here, under a console it cannot encode to, is an approval.

`PYTHONIOENCODING` reproduces the case on any operating system, which is
deliberate: a platform-gated test would leave the branch it exists for proven
by nothing while CI runs the other one. The dispatcher keeps a reconfigure loop
of its own, and its case is `tests/test_dispatch.py`'s. The case comes from
`tests/test_console_is_not_utf8.py` (#942's phase 6).
"""

import json
import os
import subprocess
import sys

import pytest
from conftest import HOSTILE, KOREAN, ROOT, census_case, decision_of

TARGET = "hooks/console.py"


class Test_module:
    @pytest.mark.parametrize("encoding", HOSTILE)
    def test_a_gate_run_on_its_own_still_reaches_a_verdict(self, korean_repo, encoding):
        """The seven `console.to_utf8()` calls, bound.

        `dispatch.py` is what production spawns, and its copy of the loop is held
        by `tests/test_dispatch.py`. The per-gate calls are for the other
        documented way in -- `hooks/console.py` says each gate is runnable on its
        own -- and nothing measured that: neutering `to_utf8` to a bare `return`
        left the suite at its own baseline, so all seven could be deleted and the
        tree stays green.
        """
        r = subprocess.run(
            [sys.executable, os.path.join(ROOT, "hooks", "commit-review-gate.py")],
            input=json.dumps(
                {
                    "tool_name": "Bash",
                    "session_id": f"solo-{encoding}",
                    "cwd": str(korean_repo),
                    "tool_input": {"command": f"git commit -m {KOREAN}"},
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


test_census = census_case(TARGET)
