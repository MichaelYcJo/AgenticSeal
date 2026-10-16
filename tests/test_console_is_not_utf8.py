"""A console the gates cannot encode to must not turn them into a silent pass.

The failure this holds is not "a message came out wrong". It is that a hook
which raises while reading or printing dies with **stdout empty**, and empty
stdout is exactly how a hook says "nothing to see here" — so the failure mode
of every gate here, under a console it cannot encode to, is an approval.

Nothing in this file is Windows-only. `PYTHONIOENCODING` reproduces every case
on any operating system, which is deliberate: a platform-gated test would leave
the branch it exists for proven by nothing while CI runs the other one.

These are BEHAVIOURAL. An earlier attempt at this defect (pull request #43)
held it with a tier of source-text assertions, and its own round 3 killed them:
moving the reconfigure block from before `main()` to after it leaves the source
byte-identical and the behaviour gone, and 22 of those tests still passed. Any
source-text assertion is satisfiable by dead code, so there are none here.
"""

import atexit
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

ROOT = os.path.join(os.path.dirname(__file__), "..")
DISPATCH = os.path.join(ROOT, "hooks", "dispatch.py")

# Korean, and the em dash the gates print. cp949 encodes the first and not the
# second; ASCII encodes neither. Both are in the payload on purpose — it
# carries the user's own command text, which is where the non-ASCII in
# production actually is.
KOREAN = "한글"
EM_DASH = "—"

# Consoles that cannot carry what the gates say. `ascii` is the sharpest and is
# not hypothetical: it is what a bare `LC_ALL=C` gives a POSIX runner.
HOSTILE = ["cp949", "ascii", "latin-1"]


_CONSOLE_REPO_TEMPLATE = None


def _console_repo_template():
    """A repo with one committed file, built once per process -- `opted_in_repo`
    is called ten times across this file's parametrized cases, always onto
    this shape."""
    global _CONSOLE_REPO_TEMPLATE
    if _CONSOLE_REPO_TEMPLATE is None:
        d = Path(tempfile.mkdtemp(prefix="specseal-console-repo-template-")) / "repo"
        d.mkdir(parents=True)
        git = lambda *a: subprocess.run(
            ["git", "-C", str(d), *a], check=True, capture_output=True
        )
        git("init", "-q")
        git("config", "user.email", "t@t.example")
        git("config", "user.name", "t")
        (d / "f.txt").write_text("one\n", encoding="utf-8")
        git("add", "-A")
        git("commit", "-qm", "base")
        atexit.register(shutil.rmtree, d, True)
        _CONSOLE_REPO_TEMPLATE = d
    return _CONSOLE_REPO_TEMPLATE


def opted_in_repo(where):
    """A repository the commit gate fires in, at a path holding non-ASCII."""
    shutil.copytree(_console_repo_template(), where)
    (where / "seal").mkdir(exist_ok=True)
    return where


def dispatch(group, payload, encoding):
    """Run the entry point the way `hooks.json` does, on a hostile console.

    Bytes rather than `text=True`, and `ensure_ascii=False`, because the
    default JSON encoder escapes every non-ASCII character — an earlier suite
    piped `json.dumps` output and so could never carry the byte that breaks
    this. Its stdin defect survived three review rounds behind that.
    """
    return subprocess.run(
        [sys.executable, DISPATCH, group],
        input=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        capture_output=True,
        timeout=30,
        env={**os.environ, "PYTHONIOENCODING": encoding, "PYTHONUTF8": "0"},
    )


def decision_of(result):
    """The gate's verdict, or "silent" — which is what the harness allows on."""
    if not result.stdout.strip():
        return "silent"
    out = json.loads(result.stdout.decode("utf-8"))
    return out["hookSpecificOutput"]["permissionDecision"]


@pytest.fixture
def korean_repo(tmp_path):
    return opted_in_repo(tmp_path / KOREAN / "repo")


@pytest.mark.parametrize("encoding", HOSTILE)
def test_a_payload_the_console_cannot_decode_still_reaches_a_verdict(
    korean_repo, encoding
):
    """The stdin half, which is the half that was missed.

    `dispatch.py` holds the only stdin read production takes, so a raise there
    takes every gate in the group down at once — and `hooks.json` runs
    `python3 … || py -3 …`, so the retry meets an already-consumed stdin and
    passes silently a second time.

    Measured against a tree with the reconfigure removed: `exit 1`, stdout
    empty, `UnicodeDecodeError: 'cp949' codec can't decode byte 0xed`.
    """
    r = dispatch(
        "pre-bash",
        {
            "tool_name": "Bash",
            "session_id": f"ko-{encoding}",
            "cwd": str(korean_repo),
            "tool_input": {"command": f"git commit -m {KOREAN}"},
        },
        encoding,
    )
    assert decision_of(r) == "deny", (
        f"{encoding}: the gate went silent, which the harness reads as "
        f"approval. stderr: {r.stderr.decode('utf-8', 'replace')[-300:]}"
    )
    assert r.returncode == 0, r.stderr.decode("utf-8", "replace")[-300:]


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


@pytest.mark.parametrize("encoding", HOSTILE)
def test_a_gate_run_on_its_own_still_reaches_a_verdict(korean_repo, encoding):
    """The seven `console.to_utf8()` calls, bound.

    `dispatch.py` is what production spawns, and its copy of the loop is held
    by three cases above. The per-gate calls are for the other documented way
    in -- `hooks/console.py:41-50` says each gate is runnable on its own -- and
    nothing measured that: neutering `to_utf8` to a bare `return` left this
    suite at its own baseline, so all seven could be deleted and the tree stays
    green.
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
