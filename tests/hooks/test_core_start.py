"""`hooks/core-start.py`: a session receives the core once, from its own group.

The hook prints `hooks/lib/core.py#output` as plain text. It is the one gate
of the `session-core` group, because `hooks/dispatch.py#merge` drops plain
text beside a neighbour's JSON, and `hooks/hooks.json` registers that group
for `SessionStart` with the matcher `startup|clear|compact`, because a
resumed session keeps what its start printed (#1177, S2 of work item
1793273065). The cases drive `dispatch.py` as production spawns it.
"""

import json
import os
import subprocess
import sys

from conftest import ROOT, census_case, load_hook_module

TARGET = "hooks/core-start.py"

HOOKS = os.path.join(ROOT, "hooks")
GATE = "core-start.py"
GROUP = "session-core"
MATCHER = "startup|clear|compact"


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


def start(body, root=None):
    """`dispatch.py session-core` run as the harness runs it, with BODY on
    stdin and `CLAUDE_PLUGIN_ROOT` set to ROOT, or unset where ROOT is None;
    its stdout. The hook writes nothing to stderr and exits 0."""
    env = {k: v for k, v in os.environ.items() if k != "CLAUDE_PLUGIN_ROOT"}
    if root is not None:
        env["CLAUDE_PLUGIN_ROOT"] = root
    r = subprocess.run(
        [sys.executable, os.path.join(HOOKS, "dispatch.py"), GROUP],
        input=body,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
        env=env,
    )
    assert (r.returncode, r.stderr) == (0, ""), r.stderr
    return r.stdout


def printed(core, cwd, root):
    """What a session receives where the hook prints `output(cwd, root)`."""
    return core.output(cwd, root).rstrip("\n") + "\n"


class Test_main:
    def test_accepts_each_matched_source_and_prints_the_core_as_plain_text(
        self, tmp_path
    ):
        """S2: a `startup`, `clear` and `compact` payload each print the
        output whole, as plain text, through the dispatcher."""
        core = load_hook_module("lib/core.py", "core_for_the_start")
        root = plugin(tmp_path / "plugin")
        cwd = tmp_path / "outside"
        cwd.mkdir()
        for source in ("startup", "clear", "compact"):
            body = {"hook_event_name": "SessionStart", "source": source}
            body["cwd"] = str(cwd)
            out = start(json.dumps(body), root)
            assert out == printed(core, str(cwd), root), (source, out)
            assert out.startswith("AgenticSeal core from "), out
            assert core.parse(out).body.rstrip("\n") == (
                "# scratch core\n\nA value — kept."
            )

    def test_accepts_a_session_in_a_clone_of_the_plugin_with_the_clones_core(
        self, tmp_path
    ):
        """S4 through the hook: a session started in this repository, a clone
        of the plugin, receives this tree's core whatever plugin root runs."""
        core = load_hook_module("lib/core.py", "core_for_the_clone")
        root = plugin(tmp_path / "plugin")
        body = {"hook_event_name": "SessionStart", "source": "startup", "cwd": ROOT}
        out = start(json.dumps(body), root)
        assert os.path.samefile(
            core.parse(out).path, os.path.join(ROOT, "skills", "core", "SKILL.md")
        ), out.split("\n", 1)[0]

    def test_refuses_to_print_nothing_for_a_payload_with_no_readable_cwd(
        self, tmp_path
    ):
        """The core reaches every session, so a payload the hook cannot read
        prints the plugin's core rather than nothing."""
        core = load_hook_module("lib/core.py", "core_for_the_payload")
        root = plugin(tmp_path / "plugin")
        for body in ("not json", "[1]", json.dumps({"cwd": 7})):
            assert start(body, root) == printed(core, "", root), body

    def test_accepts_a_run_with_no_plugin_root_variable_as_its_own_plugins(
        self, tmp_path
    ):
        """Without `CLAUDE_PLUGIN_ROOT` the plugin root is the one the hook's
        own file sits in."""
        core = load_hook_module("lib/core.py", "core_for_no_variable")
        cwd = tmp_path / "outside"
        cwd.mkdir()
        out = start(json.dumps({"cwd": str(cwd)}))
        assert out == printed(core, str(cwd), ROOT), out.split("\n", 1)[0]


class Test_module:
    def test_the_core_has_a_group_and_a_session_start_entry_of_its_own(self):
        """S2: `core-start.py` is the one gate of `session-core` and in no
        other group, and `hooks/hooks.json` runs that group for
        `SessionStart` from one entry, matched to every source but `resume`,
        holding nothing else; the entry with no matcher does not run it."""
        d = load_hook_module("dispatch.py", "dispatch_for_the_core_group")
        assert d.GROUPS[GROUP] == (GATE,)
        others = [g for g, gates in d.GROUPS.items() if GATE in gates and g != GROUP]
        assert not others, others
        with open(os.path.join(HOOKS, "hooks.json"), encoding="utf-8") as f:
            entries = json.load(f)["hooks"]["SessionStart"]
        running = [
            e
            for e in entries
            for h in e["hooks"]
            if f'/hooks/dispatch.py" {GROUP}' in h["command"]
        ]
        assert len(running) == 1, entries
        entry = running[0]
        assert entry.get("matcher") == MATCHER, entry
        assert len(entry["hooks"]) == 1, entry
        for alternative in entry["hooks"][0]["command"].split(" || "):
            assert alternative.endswith(f'/hooks/dispatch.py" {GROUP}'), alternative


test_census = census_case(TARGET)
