"""`evals/scripts/noninferiority.py`, one class per function.

Rebuilt by #942's phase 5 from the `noninferiority.py` half of one
behaviour module. The script runs one side of the behaviour suite, and
judges a new side's shape and reach graders against a baseline by three
pass rules.

The pure units, the pass rules, the record's writer and reader and the
trace readers run in the process on numbers, texts and files under the
case's own directory, with no git. `run` runs through `main` with the eval
replaced by a stand-in that writes the eval's JSON. The units that ask git
for a suite read one repository built once for the module, holding three
proofer suites in its history; no case writes into it, so it is never
copied, and each case writes its sides and its output under its own
directory. A few cases of `compare` read this clone's own HEAD, as a side
written before `suite_tree` was recorded does.
"""

import hashlib
import json
import ntpath
import os
import posixpath
import re
import stat
import sys
import tempfile
import types

import pytest
from conftest import ROOT, census_case, git, load_module, write
from test_no_case_tells_the_agent_it_is_evaluated import REFUSED

TARGET = "evals/scripts/noninferiority.py"

NI = load_module(os.path.join(ROOT, *TARGET.split("/")), "noninferiority_under_test")
BEHAVIOUR = load_module(
    os.path.join(ROOT, "evals", "scripts", "behaviour.py"),
    "behaviour_for_noninferiority",
)

SUITE = {"rev": "1" * 40, "tree": "2" * 40}
TRUTH = r"^location: .*(?:src\/a\.py:(?:10|11|12)(?!\d))"
CASE = "evals/behaviour/proofer/c1"
# The header rows a record written before #1487 carries, which no reader of
# a record reads any more.
REMOVED_ROWS = ("report rows", "false rows", "tokens per true find")
RESULT = {
    "type": "result",
    "subtype": "success",
    "total_cost_usd": 2.5,
    "duration_ms": 412000,
    # The case session's own tokens, which leave out the agent it spawned.
    "usage": {"input_tokens": 40, "cache_read_input_tokens": 900000},
    # Every model's tokens, the spawned agent's among them, in the shape a
    # 2.1.296 trace carries (#957 phase 1).
    "modelUsage": {
        "claude-sonnet-5-5": {
            "inputTokens": 4,
            "outputTokens": 323,
            "cacheReadInputTokens": 27598,
            "cacheCreationInputTokens": 15057,
        },
        "claude-opus-5-5": {
            "inputTokens": 28,
            "outputTokens": 8835,
            "cacheReadInputTokens": 445032,
            "cacheCreationInputTokens": 43597,
        },
    },
}
EVERY_MODEL = 4 + 27598 + 15057 + 28 + 445032 + 43597


# --- numbers, sides and records --------------------------------------------


def numbers(**over):
    """Numbers every rule passes: two truths found twice a side, every shape
    grader green, and a new side that read a tenth fewer tokens across every
    model over as many tool calls and spent the same from a preload half the
    size."""
    graders = {
        ("c1", "truth-1"): ("truth", 2, 2, 2, 2),
        ("c1", "truth-2"): ("truth", 2, 2, 2, 2),
        ("c1", "shape-report-exists"): ("shape", 2, 2, 2, 2),
        ("c1", "reach-proofer"): ("reach", 2, 2, 2, 2),
    }
    graders.update(over.pop("graders", {}))
    base = {
        "graders": graders,
        "old_cut": False,
        "new_cut": False,
        "old_spend": 10.0,
        "new_spend": 10.0,
        "old_tokens": 1000000,
        "new_tokens": 900000,
        "old_calls": 100,
        "new_calls": 100,
        "old_seconds": 600.0,
        "new_seconds": 600.0,
        "old_bytes": 100000,
        "new_bytes": 50000,
    }
    base.update(over)
    return base


def side(graders, **over):
    """A side's `side_numbers` holding GRADERS, `{key: (kind, passed, runs)}`,
    with OVER replacing any other number."""
    base = {
        "graders": {k: [v[0], v[1], v[2]] for k, v in graders.items()},
        "runs": {},
        "cut": False,
        "preload": {"agents/proofer.md": "a" * 64},
        "id": "2026-10-14T00:00:00Z 000000000000",
        "suite": SUITE,
        "spend": 10.0,
        "tokens": 1000000,
        "calls": 100,
        "seconds": 600.0,
        "bytes": 100000,
    }
    base.update(over)
    return base


GRADED = {("c1", "truth-1"): ("truth", 2, 2), ("c1", "shape-x"): ("shape", 2, 2)}
# GRADED with its shape grader passing one run fewer, which fails rule 1.
SHAPE_FELL = {**GRADED, ("c1", "shape-x"): ("shape", 1, 2)}


def written(old_graders=GRADED, new_graders=GRADED, **new):
    """The record `compare` writes for two sides, the new one cheaper per
    call and smaller unless NEW says otherwise."""
    new.setdefault("bytes", 50000)
    new.setdefault("tokens", 900000)
    return NI.render("proofer", 3, side(old_graders), side(new_graders, **new))


def eval_side(tmp_path, name, rev, tree):
    """A one-run side `run` could have written, run on the suite REV/TREE,
    its case holding a `shape-x` `file_exists` grader and its run passing
    it; the path it is written to."""
    run = {
        "graders": [{"name": "shape-x", "passed": True}],
        "agentic": {"cost": None, "tool_calls": None},
    }
    case = {
        "name": "c1",
        "graders": [{"name": "shape-x", "type": "file_exists"}],
        "arms": {"with": [run]},
    }
    meta = {
        "agent": "proofer",
        "preload": {},
        "cut_short": False,
        "suite_rev": rev,
        "suite_tree": tree,
    }
    path = tmp_path / f"{name}.json"
    path.write_text(
        json.dumps({"startedAt": name, "cases": [case], "agentic": meta}),
        encoding="utf-8",
    )
    return str(path)


def read_before_986(path):
    """Rewrite the side at PATH the way a run before #986 kept it: its rows
    and not the record its session printed."""
    with open(path, encoding="utf-8") as f:
        result = json.load(f)
    for case in result["cases"]:
        for run in NI.case_runs(case):
            run["agentic"] = {"report_rows": ["location: `src/a.py:40`"]}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f)


# --- traces -------------------------------------------------------------------


def trace_at(path, events, tail=""):
    """EVENTS written as a trace at PATH, one JSON object a line, then TAIL."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(e) + "\n" for e in events) + tail, encoding="utf-8"
    )
    return str(path)


def assistant(blocks, parent=None):
    """An assistant event holding BLOCKS, the agent's where PARENT is set."""
    event = {"type": "assistant", "message": {"content": blocks}}
    if parent:
        event["parent_tool_use_id"] = parent
    return event


def use(name, ident):
    return {"type": "tool_use", "id": ident, "name": name, "input": {}}


def plugin_tree(root, skills="  - code-review\n"):
    """A plugin tree at ROOT with one agent preloading SKILLS."""
    write(
        root, "agents/proofer.md", f"---\nname: proofer\nskills:\n{skills}---\n\n# w\n"
    )
    write(root, "skills/code-review/SKILL.md", "# code-review\n")
    return root


def run_one_side(tmp_path, monkeypatch, events, error=None):
    """`run` over a one-agent plugin tree with the eval replaced by one run
    whose trace holds EVENTS; (the side `--out` holds, the plugin tree, the
    kept run's directory)."""
    plugin = plugin_tree(tmp_path / "plugin")
    kept = tmp_path / "e-Cost01"
    trace = trace_at(kept / "out" / "trace.jsonl", events)
    raw = {
        "startedAt": "t",
        "partial": False,
        "cases": [
            {
                "name": "c1",
                "graders": [{"name": "shape-x", "type": "file_exists"}],
                "arms": {
                    "with": [
                        {
                            "graders": [{"name": "shape-x", "passed": True}],
                            "error": error,
                            "tracePath": trace,
                        }
                    ]
                },
            }
        ],
    }

    def paid_eval(command, env):
        with open(command[command.index("--json") + 1], "w", encoding="utf-8") as f:
            json.dump(raw, f)

    monkeypatch.setattr(NI, "call_eval", paid_eval)
    out = tmp_path / "side.json"
    argv = ["run", "--agent", "proofer", "--tree", str(plugin), "--out", str(out)]
    assert NI.main(argv) == 0
    return json.loads(out.read_text(encoding="utf-8")), plugin, kept


# --- the suites repository ----------------------------------------------------


@pytest.fixture(scope="module")
def _suites(tmp_path_factory):
    """A repository whose history holds three proofer suites, built once:
    `own` (case c1, its truth-1 TRUTH), and two from `own`: `prompt` (c1's
    case.yaml changed) and `more` (a case c2 added). `(its path, {name:
    commit})`."""
    d = tmp_path_factory.mktemp("suites")
    identity = ["-c", "user.email=t@example.com", "-c", "user.name=t"]

    def commit(name):
        git(d, "add", "-A")
        git(d, *identity, "commit", "-qm", name)
        return git(d, "rev-parse", "HEAD").stdout.strip()

    git(d, "init", "-q")
    write(d, f"{CASE}/case.yaml", "name: c1\n")
    shape = BEHAVIOUR.grader(
        "shape", "x", "The report exists.", type="file_exists", path="r.md"
    )
    write(d, f"{CASE}/graders/shape-x.md", shape[1])
    truth = BEHAVIOUR.report_regex("truth", "1", "r.md", TRUTH, "A defect.")
    write(d, f"{CASE}/graders/truth-1.md", truth[1])
    commits = {"own": commit("own")}
    write(d, f"{CASE}/case.yaml", "name: c1, asked otherwise\n")
    commits["prompt"] = commit("prompt")
    git(d, "reset", "-q", "--hard", commits["own"])
    write(d, "evals/behaviour/proofer/c2/case.yaml", "name: c2\n")
    commits["more"] = commit("more")
    return d, commits


@pytest.fixture
def suites(_suites, monkeypatch):
    """The suites' commits, with the script reading their repository."""
    d, commits = _suites
    monkeypatch.setattr(NI, "ROOT", str(d))
    return commits


# --- the cases -----------------------------------------------------------------


class Test_preload_files:
    @pytest.mark.parametrize(
        "skills, want",
        [
            ("  - code-review\n", ["agents/proofer.md", "skills/code-review/SKILL.md"]),
            (
                "  - a\n  - b\n",
                ["agents/proofer.md", "skills/a/SKILL.md", "skills/b/SKILL.md"],
            ),
            ("", ["agents/proofer.md"]),
        ],
        ids=["one skill", "two skills", "none"],
    )
    def test_accepts_a_definition_and_every_skill_it_lists(
        self, tmp_path, skills, want
    ):
        plugin_tree(tmp_path, skills)
        assert NI.preload_files(str(tmp_path), "proofer") == want

    def test_refuses_a_definition_with_no_frontmatter(self, tmp_path):
        write(tmp_path, "agents/proofer.md", "# proofer\n")
        with pytest.raises(SystemExit, match=r"agents/proofer\.md has no frontmatter"):
            NI.preload_files(str(tmp_path), "proofer")


class Test_preload_hashes:
    def test_accepts_each_file_as_its_sha256(self, tmp_path):
        plugin_tree(tmp_path)
        assert NI.preload_hashes(str(tmp_path), "proofer") == {
            rel: hashlib.sha256((tmp_path / rel).read_bytes()).hexdigest()
            for rel in ("agents/proofer.md", "skills/code-review/SKILL.md")
        }

    def test_refuses_a_skill_that_is_not_there(self, tmp_path):
        plugin_tree(tmp_path, "  - absent\n")
        with pytest.raises(FileNotFoundError):
            NI.preload_hashes(str(tmp_path), "proofer")


class Test_preload_bytes:
    def test_accepts_every_file_summed(self, tmp_path):
        plugin_tree(tmp_path)
        assert NI.preload_bytes(str(tmp_path), "proofer") == sum(
            os.path.getsize(tmp_path / rel)
            for rel in ("agents/proofer.md", "skills/code-review/SKILL.md")
        )

    def test_refuses_a_skill_that_is_not_there(self, tmp_path):
        plugin_tree(tmp_path, "  - gone\n")
        with pytest.raises(OSError):
            NI.preload_bytes(str(tmp_path), "proofer")


class Test_git_bytes:
    def test_accepts_what_git_prints_as_bytes(self, suites):
        assert (
            NI.git_bytes("rev-parse", suites["own"]).strip() == suites["own"].encode()
        )

    def test_refuses_a_git_that_exits_otherwise(self, suites):
        with pytest.raises(SystemExit, match=r"^git rev-parse --verify nowhere: "):
            NI.git_bytes("rev-parse", "--verify", "nowhere")


def marked_repo(repo):
    """A repository at REPO with one commit, whose `.gitattributes` marks
    `/evals/` `export-ignore`, holding case c1 and one skill file."""
    git(repo.parent, "init", "-q", repo.name)
    write(repo, ".gitattributes", "/evals/ export-ignore\n")
    write(repo, f"{CASE}/case.yaml", "name: c1\n")
    write(repo, "skills/a/SKILL.md", "a\n")
    git(repo, "add", "-A")
    identity = ["-c", "user.email=t@example.com", "-c", "user.name=t"]
    git(repo, *identity, "commit", "-qm", "marked")
    return repo


class Test_extract:
    def test_accepts_the_paths_named_and_the_whole_tree_for_none(
        self, suites, tmp_path
    ):
        NI.extract(
            suites["more"], ["evals/behaviour/proofer/c2"], str(tmp_path / "some")
        )
        assert [p.name for p in (tmp_path / "some").rglob("*") if p.is_file()] == [
            "case.yaml"
        ]
        NI.extract(suites["own"], [], str(tmp_path / "all"))
        assert sorted(p.name for p in (tmp_path / "all").rglob("*") if p.is_file()) == [
            "case.yaml",
            "shape-x.md",
            "truth-1.md",
        ]

    def test_accepts_what_export_ignore_marks(self, tmp_path, monkeypatch):
        """A revision whose `.gitattributes` marks `/evals/` `export-ignore`
        still gives its suite, and its whole tree, every file: `git archive`
        of a marked path exits 0 with nothing in it."""
        monkeypatch.setattr(NI, "ROOT", str(marked_repo(tmp_path / "repo")))
        NI.extract("HEAD", [NI.SUITE], str(tmp_path / "suite"))
        assert (tmp_path / "suite" / CASE / "case.yaml").read_text(
            encoding="utf-8"
        ) == "name: c1\n"
        NI.extract("HEAD", [], str(tmp_path / "all"))
        assert sorted(
            p.relative_to(tmp_path / "all").as_posix()
            for p in (tmp_path / "all").rglob("*")
            if p.is_file()
        ) == [".gitattributes", f"{CASE}/case.yaml", "skills/a/SKILL.md"]

    def test_leaves_the_repository_s_own_index_as_it_was(self, tmp_path, monkeypatch):
        """REV is read into an index of the call's own, so a change staged
        in ROOT is still staged after it."""
        repo = marked_repo(tmp_path / "repo")
        write(repo, "staged.md", "s\n")
        git(repo, "add", "staged.md")
        monkeypatch.setattr(NI, "ROOT", str(repo))
        NI.extract("HEAD", [], str(tmp_path / "all"))
        assert git(repo, "diff", "--cached", "--name-only").stdout == "staged.md\n"

    def test_accepts_an_into_relative_to_the_caller(
        self, suites, tmp_path, monkeypatch
    ):
        """git runs in ROOT, so a relative INTO is read from the caller's
        directory before git is handed it."""
        monkeypatch.chdir(tmp_path)
        NI.extract(suites["own"], [], "rel")
        assert (tmp_path / "rel" / CASE / "case.yaml").is_file()

    def test_refuses_a_rev_git_does_not_resolve(self, suites, tmp_path):
        with pytest.raises(SystemExit, match=r"^git read-tree"):
            NI.extract("nowhere", [], str(tmp_path))

    def test_refuses_a_path_the_rev_does_not_hold(self, suites, tmp_path):
        with pytest.raises(SystemExit, match=r"^git ls-files"):
            NI.extract(suites["own"], ["evals/nowhere"], str(tmp_path))


class Test_side_path:
    @pytest.mark.parametrize(
        ("flavour", "pathsep", "tree", "base", "want"),
        [
            (
                posixpath,
                ":",
                "/w/tree",
                "/usr/bin:/Users/x/.claude/plugins/cache/p/p/1/bin:/bin",
                ["/w/tree/bin", "/w/tree/.shims", "/usr/bin", "/bin"],
            ),
            (
                ntpath,
                ";",
                "C:\\w\\tree",
                "C:\\Windows;C:\\Users\\x\\.claude\\plugins\\cache\\p\\p\\1\\bin;"
                "C:/Users/x/.Claude/Plugins/Cache/p/p/2/bin;C:\\bin",
                ["C:\\w\\tree\\bin", "C:\\w\\tree\\.shims", "C:\\Windows", "C:\\bin"],
            ),
        ],
        ids=["posix", "windows"],
    )
    def test_accepts_the_tree_first_and_no_installed_plugin_in_either_spelling(
        self, monkeypatch, flavour, pathsep, tree, base, want
    ):
        """The measured tree's `bin/` first, and no installed plugin's `bin/`
        at all, in each platform's own PATH spelling whichever platform runs
        the case."""
        os_like = types.SimpleNamespace(sep=flavour.sep, pathsep=pathsep, path=flavour)
        monkeypatch.setattr(NI, "os", os_like)
        assert NI.side_path(tree, base).split(pathsep) == want

    def test_refuses_an_empty_entry(self, monkeypatch):
        os_like = types.SimpleNamespace(sep="/", pathsep=":", path=posixpath)
        monkeypatch.setattr(NI, "os", os_like)
        assert NI.side_path("/t", "::/bin:") == "/t/bin:/t/.shims:/bin"


class Test_write_git_shim:
    def test_accepts_a_mac_with_the_command_line_tools(self, tmp_path, monkeypatch):
        clt = tmp_path / "clt-git"
        clt.write_text("", encoding="utf-8")
        monkeypatch.setattr(NI, "CLT_GIT", str(clt))
        monkeypatch.setattr(NI, "sys", types.SimpleNamespace(platform="darwin"))
        NI.write_git_shim(str(tmp_path))
        shim = tmp_path / ".shims" / "git"
        assert shim.read_text(encoding="utf-8") == f'#!/bin/sh\nexec {clt} "$@"\n'
        if os.name != "nt":
            assert stat.S_IMODE(shim.stat().st_mode) == 0o755

    @pytest.mark.parametrize("platform, there", [("linux", True), ("darwin", False)])
    def test_refuses_another_platform_or_no_command_line_tools(
        self, tmp_path, monkeypatch, platform, there
    ):
        clt = tmp_path / "clt-git"
        if there:
            clt.write_text("", encoding="utf-8")
        monkeypatch.setattr(NI, "CLT_GIT", str(clt))
        monkeypatch.setattr(NI, "sys", types.SimpleNamespace(platform=platform))
        NI.write_git_shim(str(tmp_path))
        assert not (tmp_path / ".shims").exists()


class Test_run_cost:
    def test_accepts_the_sessions_last_result_event(self, tmp_path):
        first = dict(RESULT, total_cost_usd=1.0)
        path = trace_at(
            tmp_path / "t.jsonl", [first, {"type": "system"}, RESULT], "x\n"
        )
        assert NI.run_cost(path) == {
            "total_cost_usd": 2.5,
            "duration_ms": 412000,
            "modelUsage": RESULT["modelUsage"],
        }

    def test_refuses_a_subagents_event_and_a_field_it_lacks(self, tmp_path):
        sub = dict(RESULT, parent_tool_use_id="s")
        assert (
            NI.run_cost(trace_at(tmp_path / "a.jsonl", [sub, {"type": "user"}])) is None
        )
        bare = {"type": "result", "total_cost_usd": 2.5}
        assert NI.run_cost(trace_at(tmp_path / "b.jsonl", [bare])) == {
            "total_cost_usd": 2.5,
            "duration_ms": None,
            "modelUsage": None,
        }


class Test_tool_calls:
    def test_accepts_every_tool_use_block_counted_once_by_its_id(self, tmp_path):
        events = [
            {"type": "system", "subtype": "init"},
            assistant([{"type": "text", "text": "spawning"}, use("Agent", "t1")]),
            assistant([use("Bash", "t2"), use("Read", "t3")], parent="t1"),
            assistant([use("Read", "t3")], parent="t1"),
            assistant([{"type": "tool_use", "name": "Read"}]),
            {"type": "user", "message": "a string message holds no call"},
        ]
        assert NI.tool_calls(trace_at(tmp_path / "t.jsonl", events, "not json\n")) == 4

    def test_refuses_a_trace_with_no_call_or_none_at_all(self, tmp_path):
        assert NI.tool_calls(trace_at(tmp_path / "t.jsonl", [RESULT])) is None
        assert NI.tool_calls(str(tmp_path / "no-such-trace.jsonl")) is None


class Test_tokens_read:
    def test_accepts_input_cache_creation_and_cache_read_over_every_model(self):
        usage = {
            "a": {
                "inputTokens": 1,
                "cacheReadInputTokens": 2,
                "cacheCreationInputTokens": 3,
                "outputTokens": 100,
            },
            "b": {
                "inputTokens": 10,
                "cacheReadInputTokens": 20,
                "cacheCreationInputTokens": 30,
            },
        }
        assert NI.tokens_read(usage) == 66
        assert NI.tokens_read(RESULT["modelUsage"]) == EVERY_MODEL

    @pytest.mark.parametrize(
        "usage",
        [
            None,
            {},
            {"m": "x"},
            {"m": {"inputTokens": 1, "cacheReadInputTokens": 2}},
            {
                "m": {
                    "inputTokens": 1,
                    "cacheReadInputTokens": 2,
                    "cacheCreationInputTokens": None,
                }
            },
            {
                "m": {
                    "inputTokens": True,
                    "cacheReadInputTokens": 2,
                    "cacheCreationInputTokens": 3,
                }
            },
        ],
        ids=[
            "absent",
            "empty",
            "not a model",
            "a count missing",
            "a null count",
            "a count that is true",
        ],
    )
    def test_refuses_a_short_model_usage_as_no_figure(self, usage):
        """A count read as zero makes a broken run look cheaper in the record
        a person reads."""
        assert NI.tokens_read(usage) is None


class Test_kept_root:
    @pytest.mark.parametrize("root", ["/tmp/e-Ab12cD", "/tmp/claude-eval-x1"])
    def test_accepts_a_trace_under_a_directory_the_eval_kept(self, root):
        assert NI.kept_root(f"{root}/out/trace.jsonl") == root

    @pytest.mark.parametrize(
        "trace", ["/Users/x/project/out/trace.jsonl", "/tmp/e-Ab12cD/trace.jsonl"]
    )
    def test_refuses_a_trace_anywhere_else(self, trace):
        assert NI.kept_root(trace) is None


class Test_remove_kept:
    def test_accepts_a_directory_the_eval_left_read_only(self, tmp_path):
        root = tmp_path / "e-Ab12cD"
        write(root, "sealed/a/b/trace.jsonl", "x")
        for path in (
            root / "sealed" / "a" / "b",
            root / "sealed" / "a",
            root / "sealed",
            root,
        ):
            os.chmod(path, 0o500)
        NI.remove_kept(str(root))
        assert not root.exists()

    def test_refuses_to_raise_for_a_directory_already_gone(self, tmp_path):
        assert NI.remove_kept(str(tmp_path / "e-gone")) is None


class Test_runs_of:
    def test_accepts_every_run_keyed_by_its_place(self):
        result = {
            "cases": [
                {"arms": {"with": ["w0", "w1"], "base": ["b0"]}},
                {"arms": {"with": ["x0"]}},
            ]
        }
        assert NI.runs_of(result) == [
            ("0|base|0", "b0"),
            ("0|with|0", "w0"),
            ("0|with|1", "w1"),
            ("1|with|0", "x0"),
        ]

    def test_refuses_a_result_with_no_case_as_no_run(self):
        assert NI.runs_of({}) == [] and NI.runs_of({"cases": [{}]}) == []


class Test_saved_dir:
    def test_accepts_the_side_beside_its_raw_directory(self, tmp_path):
        assert NI.saved_dir(str(tmp_path / "side.json")) == str(tmp_path / "side.raw")

    def test_refuses_to_cut_a_name_at_a_directorys_dot(self, tmp_path):
        out = os.path.join(str(tmp_path), "a.b", "side")
        assert NI.saved_dir(out) == out + ".raw"


def raw_with(tmp_path, traces):
    """The eval's JSON at TMP_PATH/raw.json, one run for each of TRACES."""
    raw = {
        "startedAt": "t",
        "cases": [{"name": "c1", "arms": {"with": [{"tracePath": t} for t in traces]}}],
    }
    path = tmp_path / "raw.json"
    path.write_text(json.dumps(raw), encoding="utf-8")
    return str(path), raw


class Test_save_side:
    def test_accepts_a_paid_side_and_removes_the_run_the_eval_kept(self, tmp_path):
        kept = tmp_path / "e-Ab12cD"
        trace = trace_at(kept / "out" / "trace.jsonl", [RESULT])
        raw, data = raw_with(tmp_path, [trace])
        saved = tmp_path / "side.raw"
        NI.save_side(raw, str(saved), {"agent": "proofer"})
        assert json.loads((saved / "raw.json").read_text(encoding="utf-8")) == data
        assert (saved / "traces" / "000.jsonl").read_text(encoding="utf-8") == (
            json.dumps(RESULT) + "\n"
        )
        meta = json.loads((saved / "meta.json").read_text(encoding="utf-8"))
        assert meta == {"agent": "proofer", "traces": {"0|with|0": "traces/000.jsonl"}}
        assert not kept.exists()

    def test_refuses_to_map_a_missing_trace_or_remove_one_the_eval_did_not_keep(
        self, tmp_path
    ):
        elsewhere = trace_at(tmp_path / "project" / "out" / "trace.jsonl", [RESULT])
        raw, _data = raw_with(tmp_path, [str(tmp_path / "gone.jsonl"), elsewhere])
        saved = tmp_path / "side.raw"
        NI.save_side(raw, str(saved), {"agent": "proofer"})
        meta = json.loads((saved / "meta.json").read_text(encoding="utf-8"))
        assert meta["traces"] == {"0|with|1": "traces/001.jsonl"}
        assert os.path.isfile(elsewhere)


def saved_side(tmp_path, runs, rev="abc", partial=False, name="c1"):
    """A saved side at TMP_PATH/side.raw whose runs are RUNS, `(trace events
    or None, error)` each, of one case NAME; its path."""
    saved = tmp_path / "side.raw"
    traces, arms = {}, []
    for n, (events, error) in enumerate(runs):
        if events is not None:
            rel = f"traces/{n:03d}.jsonl"
            trace_at(saved / rel, events)
            traces[f"0|with|{n}"] = rel
        arms.append({"graders": [], "error": error})
    raw = {
        "startedAt": "t",
        "partial": partial,
        "cases": [{"name": name, "arms": {"with": arms}}],
    }
    write(saved, "raw.json", json.dumps(raw))
    meta = {
        "agent": "proofer",
        "preload": {"agents/proofer.md": "a" * 64},
        "preload_bytes": 10,
        "rev": rev,
        "suite_rev": "s",
        "suite_tree": "t",
        "traces": traces,
    }
    write(saved, "meta.json", json.dumps(meta))
    return str(saved)


class Test_annotate:
    def test_accepts_each_runs_cost_and_calls_and_the_sides_meta(self, tmp_path):
        """A run keeps its cost and its tool calls, and no `report_text`: the
        round record its session printed stays in its trace under
        `<out>.raw/`."""
        events = [assistant([use("Bash", "a"), use("Read", "r")]), RESULT]
        result = NI.annotate(saved_side(tmp_path, [(events, None)]))
        assert result["cases"][0]["arms"]["with"][0]["agentic"] == {
            "cost": {
                k: RESULT[k] for k in ("total_cost_usd", "duration_ms", "modelUsage")
            },
            "tool_calls": 2,
        }
        assert result["agentic"] == {
            "agent": "proofer",
            "preload": {"agents/proofer.md": "a" * 64},
            "preload_bytes": 10,
            "cut_short": False,
            "rev": "abc",
            "suite_rev": "s",
            "suite_tree": "t",
        }

    @pytest.mark.parametrize(
        "runs, partial, cut",
        [
            ([(None, None)], False, False),
            ([([RESULT], "boom")], False, True),
            ([([RESULT], None)], True, True),
        ],
        ids=["a run with no trace", "a run's error", "a partial eval"],
    )
    def test_refuses_to_call_a_side_whole_that_was_cut(
        self, tmp_path, runs, partial, cut
    ):
        result = NI.annotate(saved_side(tmp_path, runs, partial=partial))
        assert result["agentic"]["cut_short"] is cut
        if runs[0][0] is None:
            run = result["cases"][0]["arms"]["with"][0]["agentic"]
            assert run == {"cost": None, "tool_calls": None}

    def test_refuses_a_machine_path_as_the_sides_rev(self, tmp_path):
        """A `--tree` side's `rev` names no machine path, since a committed
        record may not carry one; a side saved with one reads back as `tree`."""
        result = NI.annotate(
            saved_side(tmp_path, [(None, None)], rev=str(tmp_path / "t"))
        )
        assert result["agentic"]["rev"] == "tree"


class Test_write_side:
    def test_accepts_the_annotated_side_as_json_with_its_characters(self, tmp_path):
        out = tmp_path / "side.json"
        saved = saved_side(tmp_path, [([RESULT], None)], name="c1 — é")
        assert NI.write_side(saved, str(out)) == 0
        text = out.read_text(encoding="utf-8")
        assert '"c1 — é"' in text and text.endswith("}\n")

    def test_refuses_a_directory_that_is_not_there(self, tmp_path):
        with pytest.raises(OSError):
            NI.write_side(
                saved_side(tmp_path, [(None, None)]), str(tmp_path / "no" / "x.json")
            )


class Test_call_eval:
    def stub(self, tmp_path):
        name = "claude.cmd" if os.name == "nt" else "claude"
        write(tmp_path / "bin", name, "")
        os.chmod(tmp_path / "bin" / name, 0o755)
        return str(tmp_path / "bin")

    def test_accepts_a_path_holding_claude_and_runs_the_command(self, tmp_path):
        marker = tmp_path / "ran"
        env = dict(os.environ, PATH=self.stub(tmp_path))
        NI.call_eval([sys.executable, "-c", f"open({str(marker)!r}, 'w').close()"], env)
        assert marker.exists()

    def test_refuses_a_path_without_claude_and_runs_nothing(self, tmp_path, capsys):
        marker = tmp_path / "ran"
        env = dict(os.environ, PATH=str(tmp_path / "empty"))
        with pytest.raises(SystemExit) as stopped:
            NI.call_eval(
                [sys.executable, "-c", f"open({str(marker)!r}, 'w').close()"], env
            )
        assert stopped.value.code == 2
        assert capsys.readouterr().err == "claude is not on PATH\n"
        assert not marker.exists()


class Test_run_side:
    def test_accepts_a_tree_and_saves_what_its_runs_paid_for(
        self, tmp_path, monkeypatch
    ):
        sub = dict(RESULT, total_cost_usd=99.0, parent_tool_use_id="s")
        data, plugin, kept = run_one_side(
            tmp_path, monkeypatch, [{"type": "system"}, sub, RESULT]
        )
        run = data["cases"][0]["arms"]["with"][0]["agentic"]
        assert run["cost"]["total_cost_usd"] == 2.5
        assert data["agentic"]["preload"] == NI.preload_hashes(str(plugin), "proofer")
        assert data["agentic"]["preload_bytes"] == NI.preload_bytes(
            str(plugin), "proofer"
        )
        assert data["agentic"]["rev"] == "tree"
        assert (
            data["agentic"]["suite_rev"]
            == git(ROOT, "rev-parse", "HEAD").stdout.strip()
        )
        assert not kept.exists(), "the kept run was left behind"
        saved = tmp_path / "side.raw"
        assert (
            json.loads((saved / "meta.json").read_text(encoding="utf-8"))["rev"]
            == "tree"
        )

    def test_accepts_a_saved_side_again_with_no_eval(self, tmp_path, monkeypatch):
        """The eval's JSON and every trace are saved before anything reads
        them, so a crash after the runs loses nothing, and `--from-raw` reads
        the saved side again without running the eval."""

        def crash(*_args, **_kwargs):
            raise RuntimeError("a crash after the runs")

        real = NI.annotate
        monkeypatch.setattr(NI, "annotate", crash)
        with pytest.raises(RuntimeError):
            run_one_side(tmp_path, monkeypatch, [assistant([use("Bash", "a")])])
        saved, out = tmp_path / "side.raw", tmp_path / "again.json"

        def no_eval(command, env):
            raise AssertionError("--from-raw ran the eval again")

        monkeypatch.setattr(NI, "call_eval", no_eval)
        monkeypatch.setattr(NI, "annotate", real)
        assert NI.main(["run", "--from-raw", str(saved), "--out", str(out)]) == 0
        data = json.loads(out.read_text(encoding="utf-8"))
        assert data["cases"][0]["arms"]["with"][0]["agentic"] == {
            "cost": None,
            "tool_calls": 1,
        }
        assert not (tmp_path / "e-Cost01").exists()

    def test_refuses_a_run_with_no_agent_or_an_eval_that_wrote_nothing(
        self, tmp_path, monkeypatch
    ):
        plugin = plugin_tree(tmp_path / "plugin")
        out = tmp_path / "side.json"
        with pytest.raises(SystemExit, match="run needs --agent, or --from-raw"):
            NI.main(["run", "--tree", str(plugin), "--out", str(out)])
        monkeypatch.setattr(NI, "call_eval", lambda command, env: None)
        argv = ["run", "--agent", "proofer", "--tree", str(plugin), "--out", str(out)]
        with pytest.raises(SystemExit, match="claude plugin eval wrote no JSON"):
            NI.main(argv)
        assert not out.exists() and not (tmp_path / "side.raw").exists()

    def test_refuses_a_temporary_directory_whose_name_tells_the_agent_it_is_evaluated(
        self, tmp_path, monkeypatch
    ):
        """Guards #1042 S6: the tree the eval loads is the base directory of
        every skill the agent reads, so no component of its path below the
        system temporary directory holds a word
        `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py` refuses."""
        plugin = plugin_tree(tmp_path / "plugin")
        loaded = []
        monkeypatch.setattr(
            NI, "call_eval", lambda command, env: loaded.append(command[3])
        )
        argv = ["run", "--agent", "proofer", "--tree", str(plugin)]
        with pytest.raises(SystemExit, match="claude plugin eval wrote no JSON"):
            NI.main([*argv, "--out", str(tmp_path / "side.json")])
        below = os.path.relpath(loaded[0], tempfile.gettempdir())
        assert not below.startswith(os.pardir), below
        named = [part for part in below.split(os.sep) if REFUSED.search(part)]
        assert named == [], below


class Test_kind:
    @pytest.mark.parametrize(
        "name, k",
        [("truth-1", "truth"), ("shape-x", "shape"), ("reach-proofer", "reach")],
    )
    def test_accepts_the_three_prefixes(self, name, k):
        assert NI.kind(name) == k

    @pytest.mark.parametrize("name", ["truthy-1", "seal-x", "x"])
    def test_refuses_any_other_name(self, name):
        assert NI.kind(name) is None


def one_case_side(runs, graders=()):
    """A side of case c1 whose runs are RUNS, its graders GRADERS."""
    return {"cases": [{"name": "c1", "graders": list(graders), "arms": {"with": runs}}]}


# A `truth-` grader over a round record, as a side records it.
RECORD_TRUTH = {
    "name": "truth-1",
    "type": "regex",
    "weight": 1,
    "config": {
        "target": {"source": "file", "path": "seal/threads/i/trail/rounds/round-1.md"},
        "pattern": TRUTH,
        "flags": "m",
        "match": "contains",
    },
}


class Test_side_numbers:
    def test_accepts_a_side_as_its_graders_and_its_cost(self):
        """A run that keeps no `report_text` is read as any other, and the
        side's numbers hold no row count."""
        run = {
            "graders": [
                {"name": "truth-1", "passed": True},
                {"name": "shape-x", "passed": True},
                {"name": "note", "passed": True},
            ],
            "agentic": {
                "cost": {
                    k: RESULT[k]
                    for k in ("total_cost_usd", "duration_ms", "modelUsage")
                },
                "tool_calls": 7,
            },
        }
        shape = {"name": "shape-x", "type": "file_exists"}
        result = one_case_side([run], [RECORD_TRUTH, shape])
        result.update(
            startedAt="t0",
            agentic={
                "cut_short": False,
                "suite_rev": "s",
                "suite_tree": "t",
                "preload_bytes": 9,
            },
        )
        got = NI.side_numbers(result)
        assert "rows" not in got and "false" not in got
        assert got["graders"] == {
            ("c1", "truth-1"): ["truth", 1, 1],
            ("c1", "shape-x"): ["shape", 1, 1],
        }
        assert (
            got["spend"],
            got["tokens"],
            got["calls"],
            got["seconds"],
            got["bytes"],
        ) == (
            2.5,
            EVERY_MODEL,
            7,
            412.0,
            9,
        )
        assert got["runs"] == {"c1": 1} and got["suite"] == {"rev": "s", "tree": "t"}
        assert got["id"].startswith("t0 ") and len(got["id"]) == len("t0 ") + 12

    def test_accepts_a_truth_over_a_round_record_as_the_eval_recorded_it(self):
        """A side written before #1487 keeps the record its run printed, and
        a truth the eval recorded found is counted found: the kept text is
        not read again."""
        run = {
            "graders": [{"name": "truth-1", "passed": True}],
            "agentic": {"report_text": ""},
        }
        got = NI.side_numbers(one_case_side([run], [RECORD_TRUTH]))
        assert got["graders"] == {("c1", "truth-1"): ["truth", 1, 1]}

    def test_refuses_a_cost_one_run_lacks_and_a_cut_side(self):
        cost = {
            "total_cost_usd": 1.0,
            "duration_ms": 1000,
            "modelUsage": RESULT["modelUsage"],
        }
        result = one_case_side(
            [{"graders": [], "agentic": {"cost": cost}}, {"graders": []}]
        )
        result["partial"] = True
        got = NI.side_numbers(result)
        assert (got["spend"], got["tokens"], got["seconds"], got["calls"]) == (
            None,
        ) * 4
        assert got["cut"] is True


class Test_pooled:
    def test_accepts_values_as_their_sum(self):
        assert NI.pooled(iter([1, 2, 3])) == 6

    @pytest.mark.parametrize("values", [[], [1, None]], ids=["none", "one unknown"])
    def test_refuses_no_value_or_an_unknown_one(self, values):
        assert NI.pooled(values) is None


class Test_suite_tree:
    def test_accepts_the_tree_of_the_agents_cases(self, suites, _suites):
        d, _commits = _suites
        want = git(
            d, "rev-parse", f"{suites['own']}:evals/behaviour/proofer"
        ).stdout.strip()
        assert NI.suite_tree(suites["own"], "proofer") == want
        assert NI.suite_tree(suites["prompt"], "proofer") != want

    def test_refuses_an_agent_with_no_suite_there(self, suites):
        with pytest.raises(SystemExit, match=r"^git rev-parse"):
            NI.suite_tree(suites["own"], "crafter")


class Test_suite_name:
    def test_accepts_the_commit_and_the_tree(self):
        assert NI.suite_name(SUITE) == "1" * 40 + " " + "2" * 40

    def test_refuses_to_shorten_either(self):
        assert len(NI.suite_name({"rev": "a" * 40, "tree": "b" * 40})) == 81


VERDICTS = {
    "every rule holds": (numbers(), "pass"),
    "rule 1: the total falling by one shape run": (
        numbers(graders={("c1", "shape-report-exists"): ("shape", 2, 2, 1, 2)}),
        "fail",
    ),
    "rule 1: the total falling by one reach run": (
        numbers(graders={("c1", "reach-proofer"): ("reach", 2, 2, 1, 2)}),
        "fail",
    ),
    "rule 1: a new side passing more often": (
        numbers(graders={("c1", "shape-report-exists"): ("shape", 1, 2, 2, 2)}),
        "pass",
    ),
    "rule 1: a reach run lost and a shape run gained share one total": (
        numbers(
            graders={
                ("c1", "reach-proofer"): ("reach", 2, 2, 1, 2),
                ("c1", "shape-findings"): ("shape", 1, 2, 2, 2),
            }
        ),
        "pass",
    ),
    "rule 2: a grader failing every new run where the baseline passed it, the total held": (
        numbers(
            graders={
                ("c1", "shape-report-exists"): ("shape", 2, 2, 0, 2),
                ("c1", "shape-findings"): ("shape", 0, 2, 2, 2),
            }
        ),
        "fail",
    ),
    "rule 2: a grader the baseline never passed, failing every new run, is not named": (
        numbers(graders={("c1", "shape-report-exists"): ("shape", 0, 2, 0, 2)}),
        "pass",
    ),
    "rule 1: a grader the baseline lacks does not offset a lost run": (
        numbers(
            graders={
                ("c1", "shape-report-exists"): ("shape", 2, 2, 1, 2),
                ("c1", "reach-sealer"): ("reach", 0, 0, 2, 2),
            }
        ),
        "fail",
    ),
    "rule 1: a shape grader failing as often as on the baseline": (
        numbers(graders={("c1", "shape-report-exists"): ("shape", 1, 2, 1, 2)}),
        "pass",
    ),
    "rule 3: a reach grader the baseline lacks, short of every new run": (
        numbers(graders={("c1", "reach-sealer"): ("reach", 0, 0, 1, 2)}),
        "fail",
    ),
    "rule 1: a shape grader only the baseline carried, in a case both sides ran": (
        numbers(graders={("c1", "shape-needs-a-fix"): ("shape", 2, 2, 0, 0)}),
        "pass",
    ),
    "a truth grader passing two runs fewer is written and not judged": (
        numbers(graders={("c1", "truth-1"): ("truth", 2, 2, 0, 2)}),
        "pass",
    ),
    "a preload no smaller than the baseline's is written and not judged": (
        numbers(new_bytes=100000),
        "pass",
    ),
    "the tokens and the tokens per tool call both up are written and not judged": (
        numbers(new_tokens=1100000),
        "pass",
    ),
    "tokens unknown are written and not judged": (numbers(new_tokens=None), "pass"),
    "tool calls unknown are written and not judged": (
        numbers(new_calls=None),
        "pass",
    ),
    "no tool calls are written and not judged": (numbers(old_calls=0), "pass"),
    "preload bytes unknown are written and not judged": (
        numbers(old_bytes=None),
        "pass",
    ),
    "spend and seconds up are written and not judged": (
        numbers(new_spend=12.0, new_seconds=1200.0),
        "pass",
    ),
    "spend and seconds unknown, tokens known, are not judged": (
        numbers(new_spend=None, new_seconds=None),
        "pass",
    ),
    "no result: a case the baseline ran and the new side did not": (
        numbers(graders={("c2", "shape-needs-a-fix"): ("shape", 2, 2, 0, 0)}),
        "no result",
    ),
    "no result: the new side cut short": (numbers(new_cut=True), "no result"),
    "no result: the baseline cut short": (numbers(old_cut=True), "no result"),
    "no result: a case run a different number of times": (
        numbers(graders={("c1", "truth-1"): ("truth", 2, 2, 1, 1)}),
        "no result",
    ),
}
PASSING = sorted(k for k, (_n, v) in VERDICTS.items() if v == "pass")
FAILING = sorted(k for k, (_n, v) in VERDICTS.items() if v != "pass")


class Test_verdict:
    @pytest.mark.parametrize("name", PASSING)
    def test_accepts_a_side_no_rule_fails(self, name):
        given, _ = VERDICTS[name]
        assert NI.verdict(given) == ("pass", [])

    @pytest.mark.parametrize("name", FAILING)
    def test_refuses_a_side_a_rule_fails_or_numbers_that_give_no_result(self, name):
        given, expected = VERDICTS[name]
        assert NI.verdict(given)[0] == expected, NI.verdict(given)

    @pytest.mark.parametrize(
        "graders, reasons",
        [
            (
                {("c1", "shape-report-exists"): ("shape", 2, 2, 1, 2)},
                [
                    "shape and reach graders passed 3/4 runs on the new side, fewer than "
                    "the baseline's 4/4 (rule 1): c1/shape-report-exists 1/2 against 2/2"
                ],
            ),
            (
                {
                    ("c1", "shape-report-exists"): ("shape", 2, 2, 0, 2),
                    ("c1", "reach-proofer"): ("reach", 2, 2, 1, 2),
                    ("c1", "reach-sealer"): ("reach", 0, 0, 1, 2),
                },
                [
                    "shape and reach graders passed 1/4 runs on the new side, fewer than "
                    "the baseline's 4/4 (rule 1): c1/reach-proofer 1/2 against 2/2, "
                    "c1/shape-report-exists 0/2 against 2/2",
                    "shape grader c1/shape-report-exists failed every new run (0/2) "
                    "where the baseline passed it 2/2 (rule 2)",
                    "reach grader c1/reach-sealer, which the baseline lacks, failed on "
                    "the new side (1/2) (rule 3)",
                ],
            ),
        ],
        ids=[
            "the total falls",
            "the total, then the named grader, then the one the baseline lacks",
        ],
    )
    def test_refuses_with_each_rules_line_in_its_order(self, graders, reasons):
        assert NI.verdict(numbers(graders=graders)) == ("fail", reasons)

    def test_accepts_a_side_worse_on_every_figure_no_rule_reads(self):
        """A truth grader, the preload's bytes and both token figures are
        written in the record and judge nothing."""
        assert NI.verdict(
            numbers(
                graders={("c1", "truth-1"): ("truth", 2, 2, 0, 2)},
                new_bytes=100000,
                new_tokens=1100000,
            )
        ) == ("pass", [])


class Test_merged:
    def test_accepts_two_sides_as_the_numbers_a_record_carries(self):
        old = side(GRADED)
        new = side(GRADED, spend=10.123456, seconds=512.34, tokens=900000.0)
        got = NI.merged(old, new)
        assert got["graders"] == {
            k: (v[0], v[1], v[2], v[1], v[2]) for k, v in GRADED.items()
        }
        assert (got["new_spend"], got["new_seconds"], got["new_tokens"]) == (
            10.1235,
            512.3,
            900000,
        )
        assert type(got["new_tokens"]) is int

    def test_refuses_a_grader_one_side_lacks_any_runs_there(self):
        got = NI.merged(
            side({("c1", "truth-1"): ("truth", 2, 2)}),
            side({("c1", "shape-y"): ("shape", 1, 2)}),
        )
        assert got["graders"] == {
            ("c1", "shape-y"): ("shape", 0, 0, 1, 2),
            ("c1", "truth-1"): ("truth", 2, 2, 0, 0),
        }


class Test_rounded:
    @pytest.mark.parametrize(
        "value, places, want", [(3.7, 0, 3), ("2.34567", 4, 2.3457), (512.34, 1, 512.3)]
    )
    def test_accepts_a_value_at_its_places(self, value, places, want):
        got = NI.rounded(value, places)
        assert got == want and type(got) is type(want)

    def test_refuses_to_round_an_unknown(self):
        assert NI.rounded(None, 4) is None


class Test_per:
    def test_accepts_a_value_over_its_divisor(self):
        assert NI.per(900000, 100, "{:.1f}") == "9000.0"

    @pytest.mark.parametrize("value, divisor", [(None, 1), (1, None), (1, 0)])
    def test_refuses_an_unknown_or_no_divisor(self, value, divisor):
        assert NI.per(value, divisor, "{:.1f}") == "unknown"


class Test_cost_rows:
    def test_accepts_both_sides_and_the_derived_row(self):
        lines = NI.cost_rows(numbers())
        assert lines[:2] == [
            "| Baseline spend USD | 10.0000 |",
            "| New spend USD | 10.0000 |",
        ]
        assert lines[-2:] == [
            "| Baseline tokens per tool call | 10000.0 |",
            "| New tokens per tool call | 9000.0 |",
        ]
        assert "| Baseline preload bytes | 100000 |" in lines

    def test_refuses_a_number_it_does_not_know_as_unknown(self):
        lines = NI.cost_rows(numbers(new_tokens=None, old_calls=0))
        assert "| New tokens read, every model | unknown |" in lines
        assert "| Baseline tokens per tool call | unknown |" in lines


class Test_render:
    def test_accepts_two_sides_as_a_record_that_reads_back(self):
        text = written(spend=10.123456, seconds=512.34)
        back, stated, preload = NI.parse_record(text)
        assert stated == "pass" and NI.verdict(back)[0] == "pass"
        assert preload == {"agents/proofer.md": "a" * 64}
        assert {k: back[k] for k in NI.COST_FIELDS} == {
            "old_spend": 10.0,
            "new_spend": 10.1235,
            "old_tokens": 1000000,
            "new_tokens": 900000,
            "old_calls": 100,
            "new_calls": 100,
            "old_seconds": 600.0,
            "new_seconds": 512.3,
            "old_bytes": 100000,
            "new_bytes": 50000,
        }
        assert text.startswith("# proofer — phase 3 smoke run\n")
        assert text.endswith("\nVerdict: pass\n\n- every pass rule holds\n")
        assert [row for row in REMOVED_ROWS if row in text] == []

    def test_refuses_a_failing_side_with_its_reasons_and_a_cut_one_as_no_result(self):
        text = written(GRADED, SHAPE_FELL)
        assert (
            "\nVerdict: fail\n\n- shape and reach graders passed 1/2 runs on the new "
            "side, fewer than the baseline's 2/2 (rule 1): c1/shape-x 1/2 against 2/2\n"
            in text
        )
        assert "| New cut short | yes |" in written(cut=True)
        assert "Verdict: no result" in written(cut=True)


class Test_table:
    TEXT = "## A\n\n| H | I |\n|---|---|\n| a | 1 |\n| b | 2 |\n\n## B\n\n| H |\n|---|\n| c |\n"

    def test_accepts_the_body_rows_under_the_heading(self):
        assert NI.table(self.TEXT, "A") == [["a", "1"], ["b", "2"]]

    def test_refuses_a_heading_that_is_not_there(self):
        assert NI.table(self.TEXT, "C") == []


class Test_header_field:
    def test_accepts_a_row_of_the_header_table(self):
        assert (
            NI.header_field("# r\n| Agent | proofer |\n| Phase | 3 |\n", "Phase") == "3"
        )

    def test_refuses_a_row_that_is_not_there_or_not_whole(self):
        assert NI.header_field("| Agent | proofer |\n", "Phase") is None
        assert NI.header_field("x | Phase | 3 |\n", "Phase") is None


class Test_parse_record:
    def test_accepts_a_record_and_an_unknown_cost(self):
        text = written(spend=None)
        back, stated, _preload = NI.parse_record(text)
        assert back["new_spend"] is None and stated == "pass"
        assert back["graders"] == {
            k: (v[0], v[1], v[2], v[1], v[2]) for k, v in GRADED.items()
        }

    def test_refuses_a_count_that_is_no_integer_and_reads_a_missing_cut_as_cut(self):
        text = written()
        with pytest.raises(ValueError):
            NI.parse_record(
                text.replace(
                    "| truth | c1 | truth-1 | 2 |", "| truth | c1 | truth-1 | x |"
                )
            )
        bare = "\n".join(line for line in text.split("\n") if "cut short" not in line)
        back, _stated, _preload = NI.parse_record(bare)
        assert back["old_cut"] is True and back["new_cut"] is True


class Test_differ:
    def test_accepts_two_suites_and_names_both(self):
        said = NI.differ("a b", "c d")
        assert "the baseline at a b and the new side at c d" in said

    def test_refuses_to_reuse_the_baseline(self):
        said = NI.differ("e f", "e g")
        assert "(`<commit> <tree of evals/behaviour/<agent>>`)" in said
        assert said.endswith("; a changed suite needs a new baseline")


class Test_suite_problem:
    def test_accepts_one_tree_at_two_commits(self):
        text = "| Baseline suite | a t |\n| New suite | c t |\n"
        assert NI.suite_problem(text) is None

    @pytest.mark.parametrize(
        "text, why",
        [
            ("| Baseline suite | a t |\n", "names no suite"),
            ("| Baseline suite | a t |\n| New suite | a u |\n", "ran different suites"),
        ],
        ids=["one side names none", "two trees"],
    )
    def test_refuses_a_side_naming_none_or_two_trees(self, text, why):
        assert why in NI.suite_problem(text)


class Test_read_record:
    def test_accepts_a_record_whose_numbers_give_what_it_says(self):
        _numbers, computed, reasons, problems = NI.read_record(written())
        assert (computed, reasons, problems) == ("pass", [], [])

    def test_refuses_a_record_that_does_not_parse_or_says_otherwise(self):
        unread = written().replace(
            "| shape | c1 | shape-x | 2 |", "| shape | c1 | shape-x | x |"
        )
        assert NI.read_record(unread)[3][0].startswith("the record does not parse: ")
        edited = written(GRADED, SHAPE_FELL).replace("Verdict: fail", "Verdict: pass")
        assert "it says `pass` and its numbers give `fail`" in NI.read_record(edited)[3]


class Test_check_record:
    def test_accepts_a_sound_pass(self):
        assert NI.check_record(written()) == []

    @pytest.mark.parametrize(
        "over",
        [{"cut": True}, {"new_graders": SHAPE_FELL}],
        ids=["no result", "fail"],
    )
    def test_refuses_anything_but_pass(self, over):
        problems = NI.check_record(written(**over))
        assert any(p.startswith("its numbers give `") for p in problems), problems

    def test_refuses_an_edited_cell_the_verdict_does_not_follow(self):
        text = written()
        fewer = text.replace(
            "| shape | c1 | shape-x | 2 | 2 | 2 | 2 |",
            "| shape | c1 | shape-x | 2 | 2 | 1 | 2 |",
        )
        assert fewer != text
        problems = NI.check_record(fewer)
        assert any("says `pass` and its numbers give `fail`" in p for p in problems)
        assert any("(rule 1)" in p for p in problems)


MODEL_GRADERS = {
    ("c1", "truth-1"): ("truth", 2, 2, 2, 2),
    ("c1", "shape-commits-nothing"): ("shape", 2, 2, 2, 2),
    ("c1", "reach-sealer"): ("reach", 2, 2, 2, 2),
    ("c1", "reach-framer"): ("reach", 0, 0, 1, 2),
}


def model_numbers(graders=MODEL_GRADERS, **over):
    """A model record's numbers: the Sonnet side half the spend, and short on
    one run of a reach grader the Opus side lacks, so its own verdict fails
    rule 3, which `model` reads past."""
    over.setdefault("new_spend", 5.0)
    return {**numbers(**over), "graders": dict(graders)}


class Test_cheaper_model:
    def test_accepts_sonnet_where_every_grader_holds_and_it_spent_less(self):
        assert NI.verdict(model_numbers()) == (
            "fail",
            [
                "reach grader c1/reach-framer, which the baseline lacks, failed on "
                "the new side (1/2) (rule 3)"
            ],
        )
        assert NI.cheaper_model(model_numbers()) == (
            "sonnet",
            "every grader holds and Sonnet spent 5.0 USD, below 10.0",
        )

    @pytest.mark.parametrize(
        "over, why",
        [
            (
                {
                    "graders": {
                        **MODEL_GRADERS,
                        ("c1", "truth-1"): ("truth", 2, 2, 1, 2),
                    }
                },
                "truth grader c1/truth-1",
            ),
            (
                {
                    "graders": {
                        **MODEL_GRADERS,
                        ("c1", "shape-commits-nothing"): ("shape", 2, 2, 1, 2),
                    }
                },
                "shape grader",
            ),
            (
                {
                    "graders": {
                        **MODEL_GRADERS,
                        ("c1", "reach-sealer"): ("reach", 2, 2, 1, 2),
                    }
                },
                "reach grader",
            ),
            ({"new_spend": 10.0}, "not below Opus's 10.0"),
            ({"new_spend": None}, "Sonnet spent None USD"),
            ({"new_cut": True}, "cut short"),
            (
                {"graders": {("c1", "shape-commits-nothing"): ("shape", 2, 2, 2, 2)}},
                "no truth grader",
            ),
        ],
        ids=[
            "a truth lost",
            "a shape lost",
            "a reach lost",
            "spend equal",
            "spend unknown",
            "cut short",
            "no truth",
        ],
    )
    def test_refuses_sonnet_on_any_loss_or_no_saving(self, over, why):
        graders = over.pop("graders", MODEL_GRADERS)
        found, said = NI.cheaper_model(model_numbers(graders, **over))
        assert found == "opus" and why in said, said


class Test_compare:
    ARGV = ("compare", "--agent", "proofer", "--phase", "3")

    def test_accepts_one_suite_at_two_commits_and_writes_the_record(
        self, tmp_path, capsys
    ):
        old = eval_side(tmp_path, "old", "a" * 40, "b" * 40)
        same = eval_side(tmp_path, "same", "c" * 40, "b" * 40)
        out = tmp_path / "proofer-phase-3.md"
        assert (
            NI.main([*self.ARGV, "--old", old, "--new", same, "--out", str(out)]) == 0
        )
        text = out.read_text(encoding="utf-8")
        assert "| Baseline suite | " + "a" * 40 + " " + "b" * 40 + " |" in text
        assert [row for row in REMOVED_ROWS if row in text] == []
        assert (
            capsys.readouterr().out == re.search(r"^Verdict: .*$", text, re.M)[0] + "\n"
        )

    def test_accepts_a_side_read_before_986(self, tmp_path, capsys):
        """A side whose runs keep the rows the reader before #986 matched,
        and no `report_text`, is read for the result the eval recorded."""
        old = eval_side(tmp_path, "old", "a" * 40, "b" * 40)
        new = eval_side(tmp_path, "new", "a" * 40, "b" * 40)
        read_before_986(old)
        out = tmp_path / "proofer-phase-3.md"
        assert NI.main([*self.ARGV, "--old", old, "--new", new, "--out", str(out)]) == 0
        text = out.read_text(encoding="utf-8")
        assert "| shape | c1 | shape-x | 1 | 1 | 1 | 1 |" in text
        assert capsys.readouterr().out == "Verdict: pass\n"

    def test_accepts_a_side_naming_its_commit_alone(self, tmp_path):
        """A side written before `suite_tree` was recorded names its commit,
        and its suite is read as that commit's tree of the agent's cases."""
        head = NI.git_bytes("rev-parse", "HEAD").decode("utf-8").strip()
        commit_only = eval_side(tmp_path, "commit-only", head, None)
        by_tree = eval_side(
            tmp_path, "by-tree", "e" * 40, NI.suite_tree("HEAD", "proofer")
        )
        other = eval_side(tmp_path, "other", "c" * 40, "d" * 40)
        out = ["--out", str(tmp_path / "r.md")]
        assert NI.main([*self.ARGV, "--old", commit_only, "--new", by_tree, *out]) == 0
        assert NI.main([*self.ARGV, "--old", commit_only, "--new", other, *out]) == 2

    def test_refuses_two_suites_and_names_both(self, tmp_path, capsys):
        old = eval_side(tmp_path, "old", "a" * 40, "b" * 40)
        other = eval_side(tmp_path, "new", "c" * 40, "d" * 40)
        out = tmp_path / "proofer-phase-3.md"
        assert (
            NI.main([*self.ARGV, "--old", old, "--new", other, "--out", str(out)]) == 2
        )
        assert not out.exists()
        said = capsys.readouterr().err
        assert "a" * 12 in said and "c" * 12 in said

    def test_refuses_a_side_naming_no_suite(self, tmp_path, capsys):
        new = eval_side(tmp_path, "new", "a" * 40, "b" * 40)
        unnamed = eval_side(tmp_path, "unnamed", None, None)
        out = tmp_path / "proofer-phase-3.md"
        assert (
            NI.main([*self.ARGV, "--old", unnamed, "--new", new, "--out", str(out)])
            == 2
        )
        assert not out.exists()
        assert "records no suite_rev" in capsys.readouterr().err


class Test_check:
    def test_accepts_a_record_whose_verdict_holds(self, tmp_path):
        path = tmp_path / "r.md"
        path.write_text(written(), encoding="utf-8")
        assert NI.main(["check", str(path)]) == 0

    def test_accepts_a_record_written_before_1487_as_it_was_judged(
        self, tmp_path, capsys
    ):
        """A record written before #1487 carries the four row counts and the
        two `tokens per true find` rows; `check` and `model` read past them
        and give what they give the same record without them."""
        now = NI.render("sealer", 4, side(GRADED), side(GRADED, spend=5.0))
        before = now.replace(
            "| New cut short | no |\n",
            "| New cut short | no |\n| Baseline report rows | 20 |\n"
            "| Baseline false rows | 2 |\n| New report rows | 20 |\n"
            "| New false rows | 4 |\n",
        ).replace(
            "| New tokens per tool call | 10000.0 |\n",
            "| New tokens per tool call | 10000.0 |\n"
            "| Baseline tokens per true find | 500000 |\n"
            "| New tokens per true find | 500000 |\n",
        )
        assert [row for row in REMOVED_ROWS if before.count(row) != 2] == []
        said = []
        for text in (now, before):
            path = tmp_path / "r.md"
            path.write_text(text, encoding="utf-8")
            assert NI.main(["check", str(path)]) == 0
            assert NI.main(["model", str(path)]) == 0
            said.append(capsys.readouterr().out)
        assert (
            said[0]
            == said[1]
            == ("sonnet\nevery grader holds and Sonnet spent 5.0 USD, below 10.0\n")
        )

    def test_refuses_a_failing_record_and_one_over_two_suites(self, tmp_path, capsys):
        path = tmp_path / "r.md"
        path.write_text(
            written(GRADED, SHAPE_FELL).replace("Verdict: fail", "Verdict: pass"),
            encoding="utf-8",
        )
        assert NI.main(["check", str(path)]) == 1
        assert "says `pass` and its numbers give `fail`" in capsys.readouterr().out
        two = written(suite={"rev": "3" * 40, "tree": "4" * 40})
        path.write_text(two, encoding="utf-8")
        assert NI.main(["check", str(path)]) == 2


class Test_model:
    def test_accepts_a_sound_record_and_prints_the_model_and_why(
        self, tmp_path, capsys
    ):
        path = tmp_path / "m.md"
        path.write_text(
            NI.render("sealer", 4, side(GRADED), side(GRADED, spend=5.0)),
            encoding="utf-8",
        )
        assert NI.main(["model", str(path)]) == 0
        assert capsys.readouterr().out.splitlines() == [
            "sonnet",
            "every grader holds and Sonnet spent 5.0 USD, below 10.0",
        ]

    @pytest.mark.parametrize("shape", ["edited", "two suites", "absent"])
    def test_refuses_a_record_it_cannot_read_or_trust(self, tmp_path, capsys, shape):
        path = tmp_path / "m.md"
        if shape == "edited":
            text = NI.render("sealer", 4, side(GRADED), side(SHAPE_FELL, spend=5.0))
            path.write_text(
                text.replace("Verdict: fail", "Verdict: pass"), encoding="utf-8"
            )
        elif shape == "two suites":
            other = {"rev": "3" * 40, "tree": "4" * 40}
            path.write_text(
                NI.render("sealer", 4, side(GRADED), side(GRADED, suite=other)),
                encoding="utf-8",
            )
        assert NI.main(["model", str(path)]) == 2
        assert capsys.readouterr().out == ""


class Test_case_runs:
    def test_accepts_every_arms_runs(self):
        assert NI.case_runs({"arms": {"a": [1, 2], "b": [3]}}) == [1, 2, 3]

    def test_refuses_a_case_with_no_arm_as_no_run(self):
        assert NI.case_runs({}) == []


class Test_main:
    @pytest.mark.parametrize(
        "argv, called",
        [
            (["run", "--agent", "proofer", "--rev", "HEAD", "--out", "o"], "run"),
            (
                [
                    "compare",
                    "--agent",
                    "crafter",
                    "--phase",
                    "1",
                    "--old",
                    "a",
                    "--new",
                    "b",
                    "--out",
                    "o",
                ],
                "compare",
            ),
            (["check", "r.md"], "check"),
            (["model", "r.md"], "model"),
        ],
    )
    def test_accepts_each_subcommand_and_hands_it_on(self, monkeypatch, argv, called):
        seen = []
        for name, fn in (
            ("run_side", "run"),
            ("compare", "compare"),
            ("check", "check"),
            ("model", "model"),
        ):
            monkeypatch.setattr(NI, name, lambda a, _fn=fn: seen.append(_fn) or 0)
        assert NI.main(argv) == 0
        assert seen == [called]

    @pytest.mark.parametrize(
        "argv",
        [
            [],
            ["run", "--agent", "proofer", "--out", "o"],
            ["run", "--rev", "HEAD", "--tree", "t", "--out", "o"],
            [
                "compare",
                "--agent",
                "nobody",
                "--phase",
                "1",
                "--old",
                "a",
                "--new",
                "b",
                "--out",
                "o",
            ],
            ["regrade", "--side", "s", "--suite-rev", "HEAD", "--out", "o"],
        ],
        ids=[
            "no subcommand",
            "no source",
            "two sources",
            "no such agent",
            "the removed regrade",
        ],
    )
    def test_refuses_arguments_it_cannot_use(self, monkeypatch, argv):
        monkeypatch.setattr(NI, "run_side", lambda a: 0)
        monkeypatch.setattr(NI, "compare", lambda a: 0)
        with pytest.raises(SystemExit) as stopped:
            NI.main(argv)
        assert stopped.value.code == 2


test_census = census_case(TARGET)
