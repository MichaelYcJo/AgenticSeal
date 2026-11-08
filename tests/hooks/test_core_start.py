"""`hooks/core-start.py`: a session whose repository holds a `seal/` root
receives the core once, and any other session receives nothing.

The hook prints `lib/core.py#output` as plain text, and `hooks/hooks.json`
registers it for `SessionStart` with the matcher `startup|clear|compact`,
because a resumed session keeps what its start printed (#1177, #1430). The
cases run the entry's command as `hooks/hooks.json` spells it, its
`python3` half with this interpreter in place of `python3` and
`${CLAUDE_PLUGIN_ROOT}` filled in. The registration itself is held by
`tests/behaviour/test_chain_hooks_hardening.py`.
"""

import json
import os
import shlex
import shutil
import subprocess
import sys

from conftest import ROOT, census_case, git_repo, load_lib_module, mark_root

TARGET = "hooks/core-start.py"

VARIABLE = "${CLAUDE_PLUGIN_ROOT}"


def command(where=ROOT):
    """The `python3` half of the `SessionStart` entry's command in
    `hooks/hooks.json`, as words: `python3` read as this interpreter, and
    `${CLAUDE_PLUGIN_ROOT}` as WHERE."""
    with open(os.path.join(ROOT, "hooks", "hooks.json"), encoding="utf-8") as f:
        (entry,) = json.load(f)["hooks"]["SessionStart"]
    (hook,) = entry["hooks"]
    first = hook["command"].split(" || ")[0]
    words = shlex.split(first)
    assert words[0] == "python3", words
    return [sys.executable] + [w.replace(VARIABLE, str(where)) for w in words[1:]]


def start(body, root=None, where=ROOT, cwd=None):
    """The command run as the harness runs it, with BODY on stdin,
    `CLAUDE_PLUGIN_ROOT` set to ROOT, or unset where ROOT is None, the script
    found under WHERE and the process started in CWD; its stdout. The hook
    writes nothing to stderr and exits 0."""
    env = {k: v for k, v in os.environ.items() if k != "CLAUDE_PLUGIN_ROOT"}
    if root is not None:
        env["CLAUDE_PLUGIN_ROOT"] = str(root)
    r = subprocess.run(
        command(where),
        input=body,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
        env=env,
        cwd=cwd,
    )
    assert (r.returncode, r.stderr) == (0, ""), (r.returncode, r.stderr)
    return r.stdout


def plugin(where, core="# scratch core\n\nA value — kept.\n"):
    """A scratch plugin root at WHERE, holding a manifest and a core."""
    os.makedirs(os.path.join(where, ".claude-plugin"))
    with open(
        os.path.join(where, ".claude-plugin", "plugin.json"), "w", encoding="utf-8"
    ) as f:
        json.dump({"name": "agentic", "version": "0.25.0"}, f)
    os.makedirs(os.path.join(where, "skills", "core"))
    with open(
        os.path.join(where, "skills", "core", "SKILL.md"),
        "w",
        encoding="utf-8",
        newline="\n",
    ) as f:
        f.write(core)
    return str(where)


def printed(cwd, root):
    """What a session receives where the hook prints `output(cwd, root)`."""
    core = load_lib_module("core.py", "core_for_the_start")
    return core.rendered(core.origin(cwd, root), root) + "\n"


def marked_repo(where):
    """A scratch repository at WHERE holding a marked `seal/` root."""
    repo = git_repo(where)
    mark_root(repo / "seal")
    return repo


class Test_main:
    def test_accepts_each_matched_source_and_prints_the_core_as_plain_text(
        self, tmp_path
    ):
        """A `startup`, `clear` and `compact` payload from a repository with
        a root each print the output whole, as plain text, ending with the
        closing line."""
        root = plugin(tmp_path / "plugin")
        repo = marked_repo(tmp_path / "repo")
        for source in ("startup", "clear", "compact"):
            body = {"hook_event_name": "SessionStart", "source": source}
            body["cwd"] = str(repo)
            out = start(json.dumps(body), root)
            assert out == printed(str(repo), root), (source, out)
            assert out.startswith("AgenticSeal core from "), out
            assert "# scratch core\n\nA value — kept.\n" in out, out
            assert "*Orchestrator: the order inside a ticket*" in out, out

    def test_accepts_a_session_in_a_clone_of_the_plugin_with_the_clones_core(
        self, tmp_path
    ):
        """A session started in this repository, a clone of the plugin that
        holds a marked root, receives this tree's core whatever plugin root
        runs."""
        root = plugin(tmp_path / "plugin")
        body = {"hook_event_name": "SessionStart", "source": "startup", "cwd": ROOT}
        first = start(json.dumps(body), root).split("\n", 1)[0]
        path = first[len("AgenticSeal core from ") :].rsplit(", plugin ", 1)[0]
        assert os.path.samefile(
            path, os.path.join(ROOT, "skills", "core", "SKILL.md")
        ), first

    def test_refuses_to_print_into_a_repository_with_no_root(self, tmp_path):
        """#1430. A session in a repository with no marked `seal/` root, or
        in a directory outside git, is doing other work and receives
        nothing."""
        root = plugin(tmp_path / "plugin")
        bare = git_repo(tmp_path / "bare")
        outside = tmp_path / "outside"
        outside.mkdir()
        for cwd in (bare, outside):
            body = {"hook_event_name": "SessionStart", "source": "startup"}
            body["cwd"] = str(cwd)
            assert start(json.dumps(body), root) == "", cwd

    def test_refuses_to_print_for_a_payload_with_no_readable_cwd(self, tmp_path):
        """A payload the hook cannot read names no repository, so it prints
        nothing and still exits 0."""
        root = plugin(tmp_path / "plugin")
        for body in (
            "not json",
            "[1]",
            json.dumps({"cwd": 7}),
            json.dumps({"cwd": ["/"]}),
            json.dumps({"cwd": ""}),
        ):
            assert start(body, root) == "", body

    def test_refuses_to_fail_where_its_library_is_gone(self, tmp_path):
        """A copy of the script with no `lib/` beside it raises at the
        import, and still exits 0 with nothing on either stream, so the
        `py -3` half never runs on a script that started."""
        alone = tmp_path / "alone"
        (alone / "hooks").mkdir(parents=True)
        shutil.copy(os.path.join(ROOT, *TARGET.split("/")), alone / "hooks")
        repo = marked_repo(tmp_path / "repo")
        body = json.dumps({"cwd": str(repo)})
        assert start(body, root=None, where=alone) == ""

    def test_accepts_a_run_with_no_plugin_root_variable_as_its_own_plugins(
        self, tmp_path
    ):
        """Without `CLAUDE_PLUGIN_ROOT` the plugin root is the one the hook's
        own file sits in, not the directory the process started in."""
        repo = marked_repo(tmp_path / "repo")
        elsewhere = tmp_path / "elsewhere"
        elsewhere.mkdir()
        out = start(json.dumps({"cwd": str(repo)}), cwd=str(elsewhere))
        assert out == printed(str(repo), ROOT), out.split("\n", 1)[0]


test_census = census_case(TARGET)
