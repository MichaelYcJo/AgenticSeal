"""`evals/scripts/noninferiority.py`, one class per function.

Rebuilt by #942's phase 5 from the `noninferiority.py` half of
`tests/behaviour/test_a_rewritten_definition_proved_non_inferior.py`. The script runs
one side of the behaviour suite, judges a new side against a baseline by
five pass rules, and reads a side again under another suite's truths.

The pure units, the pass rules, the record's writer and reader, the trace
readers and the grader reader, run in the process on numbers, texts and
files under the case's own directory, with no git. `run` runs through
`main` with the eval replaced by a stand-in that writes the eval's JSON.
`regrade` and the units that ask git for a suite read one repository built
once for the module, holding seven proofer suites in its history; no case
writes into it, so it is never copied, and each case writes its sides and
its output under its own directory. A few cases of `compare` read this
clone's own HEAD, as a side written before `suite_tree` was recorded does.
"""

import hashlib
import json
import ntpath
import os
import posixpath
import re
import stat
import subprocess
import sys
import types

import pytest
from conftest import ROOT, census_case, git, load_module, write

TARGET = "evals/scripts/noninferiority.py"

NI = load_module(os.path.join(ROOT, *TARGET.split("/")), "noninferiority_under_test")
BEHAVIOUR = load_module(
    os.path.join(ROOT, "evals", "scripts", "behaviour.py"),
    "behaviour_for_noninferiority",
)

SUITE = {"rev": "1" * 40, "tree": "2" * 40}
TRUTH = r"^location: .*(?:src\/a\.py:(?:10|11|12)(?!\d))"
WIDE = r"^location: .*(?:src\/a\.py:(?:10|11|12|40)(?!\d))"
REPORT = "seal/threads/i/trail/rounds/round-1.md"
CASE = "evals/behaviour/proofer/c1"
# Run 0's truth is its second finding's `location:` line, which a regex
# finds only where the grader's `m` flag reaches it.
ROWS = (
    ["location: `src/a.py:40`", "location: `src/a.py:11`"],
    ["location: `src/a.py:40`"],
)
# A path and a host the identifier scan refuses, built from halves so this
# file carries neither whole.
REFUSED_PATH = "/Users/" + "someone/"
REFUSED_HOST = "fixture.example" + ".net"
# The user root alone, which the scan refuses once the side's JSON writes
# the character after it as an escape.
USER_ROOT = "/Users" + "/"
FENCED_FIX = (
    "### 1. a defect with a fenced fix\n\nseverity: must\n"
    "location: `src/a.py:11`\nverdict: open\n\n"
    "```\nlocation: `src/a.py:40`\n```\n"
)
UNCLOSED = "Why it matters.\n\n~~~\nand nothing closes this.\n\n"
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
    """Numbers every rule passes: two truths found twice a side, a tenth of
    the rows false, every shape grader green, and a new side that read a
    tenth fewer tokens across every model over as many tool calls and spent
    the same from a preload half the size."""
    graders = {
        ("c1", "truth-1"): ("truth", 2, 2, 2, 2),
        ("c1", "truth-2"): ("truth", 2, 2, 2, 2),
        ("c1", "shape-report-exists"): ("shape", 2, 2, 2, 2),
        ("c1", "reach-proofer"): ("reach", 2, 2, 2, 2),
    }
    graders.update(over.pop("graders", {}))
    base = {
        "graders": graders,
        "old_rows": 20,
        "old_false": 2,
        "new_rows": 20,
        "new_false": 2,
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
        "rows": 20,
        "false": 2,
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


def written(old_graders=GRADED, new_graders=GRADED, **new):
    """The record `compare` writes for two sides, the new one cheaper per
    call and smaller unless NEW says otherwise."""
    new.setdefault("bytes", 50000)
    new.setdefault("tokens", 900000)
    return NI.render("proofer", 3, side(old_graders), side(new_graders, **new))


def printed(findings, before="", after=""):
    """A round record a case session printed: BEFORE above its `## Findings`
    section, FINDINGS in it, and AFTER below it."""
    return (
        "# i — review round 1\n\ntarget: 1a2b3c4 against main\n"
        f"{before}\n## Findings\n\n{findings}{after}"
    )


def record_of(rows):
    """A printed round record holding one finding for each of ROWS, each
    finding's `location:` line the row."""
    return printed(
        "".join(
            f"### {n}. a finding\n\nseverity: should\n{row}\nverdict: open\n\n"
            for n, row in enumerate(rows, 1)
        ),
        after="## Confirmations\n\nconfirms: none\nheld.\n",
    )


def three_findings(tail):
    """A printed record of three findings, each with its `location:` line,
    and TAIL[n] after finding n's."""
    return printed(
        "".join(
            f"### {n}. a finding\n\nseverity: should\n"
            f"location: `src/b.py:{n}`\nverdict: open\n\n{tail.get(n, '')}"
            for n in (1, 2, 3)
        )
    )


def record_truth(name, pattern):
    """A `truth-` grader over the round record, as a side records it."""
    return {
        "name": name,
        "type": "regex",
        "weight": 1,
        "config": {
            "target": {"source": "file", "path": REPORT},
            "pattern": pattern,
            "flags": "m",
            "match": "contains",
        },
    }


def printed_side(text, truths=(), found=()):
    """A side of case c1 whose one run printed TEXT: its truth graders are
    TRUTHS, `(name, pattern)` each, and the run recorded the ones FOUND
    names as passed, as the eval's search of the whole file would."""
    run = {
        "graders": [{"name": n, "passed": n in found} for n, _ in truths],
        "agentic": {"report_text": text},
    }
    case = {
        "name": "c1",
        "graders": [record_truth(n, p) for n, p in truths],
        "arms": {"with": [run]},
    }
    return {"cases": [case]}


def eval_side(tmp_path, name, rev, tree, text=""):
    """A one-run side `run` could have written, run on the suite REV/TREE;
    the path it is written to."""
    run = {
        "graders": [{"name": "shape-x", "passed": True}],
        "agentic": {"report_text": text},
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


def cat(call_id, content, parent=None, path="r/round-1-report.md", error=False):
    """The two events of a Bash `cat PATH` whose result is CONTENT."""
    use = {"type": "tool_use", "id": call_id, "name": "Bash"}
    use["input"] = {"command": f"cat {path}"}
    result = {"type": "tool_result", "tool_use_id": call_id, "content": content}
    if error:
        result["is_error"] = True
    events = [{"message": {"content": [use]}}, {"message": {"content": [result]}}]
    for event in events:
        if parent:
            event["parent_tool_use_id"] = parent
    return events


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
    """A repository whose history holds seven proofer suites, built once:
    `own` (case c1, its truth-1 TRUTH), `wide` (truth-1 widened to line 40),
    and five from `wide`: `prompt` (c1's case.yaml changed), `more` (a case
    c2 added), `kind` (truth-1 a file test, which no report row answers),
    `flag` (truth-1 carrying a flag Python's `re` has no letter for) and
    `plain` (truth-1 with no front matter). `(its path, {name: commit})`."""
    d = tmp_path_factory.mktemp("suites")
    identity = ["-c", "user.email=t@example.com", "-c", "user.name=t"]

    def commit(name):
        git(d, "add", "-A")
        git(d, *identity, "commit", "-qm", name)
        return git(d, "rev-parse", "HEAD").stdout.strip()

    def truth(pattern, flags="m"):
        text = BEHAVIOUR.report_regex("truth", "1", "r.md", pattern, "A defect.", flags)
        write(d, f"{CASE}/graders/truth-1.md", text[1])

    git(d, "init", "-q")
    write(d, f"{CASE}/case.yaml", "name: c1\n")
    shape = BEHAVIOUR.grader(
        "shape", "x", "The report exists.", type="file_exists", path="r.md"
    )
    write(d, f"{CASE}/graders/shape-x.md", shape[1])
    truth(TRUTH)
    commits = {"own": commit("own")}
    truth(WIDE)
    commits["wide"] = commit("wide")
    write(d, f"{CASE}/case.yaml", "name: c1, asked otherwise\n")
    commits["prompt"] = commit("prompt")
    git(d, "reset", "-q", "--hard", commits["wide"])
    write(d, "evals/behaviour/proofer/c2/case.yaml", "name: c2\n")
    commits["more"] = commit("more")
    git(d, "reset", "-q", "--hard", commits["wide"])
    kind = BEHAVIOUR.grader("truth", "1", "A defect.", type="file_exists", path="r.md")
    write(d, f"{CASE}/graders/truth-1.md", kind[1])
    commits["kind"] = commit("kind")
    git(d, "reset", "-q", "--hard", commits["wide"])
    truth(WIDE, flags="mu")
    commits["flag"] = commit("flag")
    git(d, "reset", "-q", "--hard", commits["wide"])
    write(d, f"{CASE}/graders/truth-1.md", "A defect, with no front matter.\n")
    commits["plain"] = commit("plain")
    return d, commits


@pytest.fixture
def suites(_suites, monkeypatch):
    """The suites' commits, with the script reading their repository."""
    d, commits = _suites
    monkeypatch.setattr(NI, "ROOT", str(d))
    return commits


def graded_side(tmp_path, rev, rows, found, spoil=None):
    """A side of case c1 run on the suite at REV, its run I having printed a
    round record of one finding for each of ROWS[I] and recorded truth-1 as
    FOUND[I], its scores the ones a run of two graders gets, and SPOIL
    applied to it where one is given. The path it is written to."""
    truth = {
        "name": "truth-1",
        "type": "regex",
        "weight": 1,
        "config": {
            "target": {"source": "file", "path": "r.md"},
            "pattern": TRUTH,
            "flags": "m",
            "match": "contains",
        },
    }
    shape = {
        "name": "shape-x",
        "type": "file_exists",
        "weight": 1,
        "config": {"path": "r.md"},
    }
    runs = []
    for shown, passed in zip(rows, found, strict=True):
        score = (1 + passed) / 2
        runs.append(
            {
                "score": score,
                "passed": score >= 1,
                "graders": [
                    {"name": "shape-x", "passed": True, "weight": 1, "scored": True},
                    {"name": "truth-1", "passed": passed, "weight": 1, "scored": True},
                ],
                "agentic": {"report_text": record_of(shown)},
            }
        )
    score = sum(r["score"] for r in runs) / len(runs)
    rate = sum(r["passed"] for r in runs) / len(runs)
    result = {
        "startedAt": "2026-10-19T00:00:00Z",
        "suite": {"threshold": 1},
        "cases": [
            {
                "name": "proofer c1",
                "dir": CASE,
                "graders": [shape, truth],
                "arms": {"with": runs},
                "aggregates": {"score": score, "passRate": rate},
            }
        ],
        "aggregates": {
            "casesTotal": 1,
            "casesPassed": int(rate >= 1),
            "overallScore": score,
            "overallPassRate": rate,
        },
        "agentic": {
            "agent": "proofer",
            "preload": {},
            "cut_short": False,
            "suite_rev": rev,
            "suite_tree": NI.suite_tree(rev, "proofer"),
        },
    }
    if spoil:
        spoil(result)
    path = tmp_path / "side.json"
    path.write_text(json.dumps(result), encoding="utf-8")
    return str(path)


def regraded_to(side_path, rev, out):
    return NI.main(
        ["regrade", "--side", side_path, "--suite-rev", rev, "--out", str(out)]
    )


def fenced_first_run(result):
    """Run 0 printed truth-1's line only inside a finding's fenced fix."""
    run = result["cases"][0]["arms"]["with"][0]
    run["agentic"]["report_text"] = printed(
        "### 1. a defect\n\nseverity: must\nlocation: `src/a.py:40`\n"
        "verdict: open\n\n```\nlocation: `src/a.py:11`\n```\n"
    )


def run_score_off(result):
    result["cases"][0]["arms"]["with"][0]["score"] = 0.5


def case_score_off(result):
    result["cases"][0]["aggregates"]["score"] = 0.5


def side_score_off(result):
    result["aggregates"]["overallScore"] = 0.5


def truth_not_its_suites(result):
    result["cases"][0]["graders"][1]["config"]["pattern"] = WIDE


def no_suite(result):
    result["agentic"]["suite_rev"] = None


def no_agent(result):
    result["agentic"]["agent"] = "nobody"


def with_c2(result):
    case = json.loads(json.dumps(result["cases"][0]))
    case.update(name="proofer c2", dir="evals/behaviour/proofer/c2")
    result["cases"].append(case)


# --- the cases -----------------------------------------------------------------


class Test_module:
    def test_the_scan_loads_in_a_process_that_cannot_import_a_test_module(
        self, tmp_path
    ):
        """A side's run is `python3` on the script, with no `tests/` on its
        path and maybe no pytest, so the scan is loaded without the
        `conftest` import its cases need. Run in an isolated interpreter, a
        refused path is masked."""
        code = (
            "import sys\n"
            f"sys.path.insert(0, {os.path.join(ROOT, 'evals', 'scripts')!r})\n"
            "import noninferiority as ni\n"
            "print(ni.masked(sys.argv[1]))\n"
        )
        run = subprocess.run(
            [sys.executable, "-I", "-c", code, f"read {REFUSED_PATH}log"],
            cwd=tmp_path,
            capture_output=True,
            encoding="utf-8",
        )
        assert run.returncode == 0, run.stderr
        assert run.stdout == "read /Users/x/log\n", run.stdout


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
            NI.git_bytes("rev-parse", suites["plain"]).strip()
            == suites["plain"].encode()
        )

    def test_refuses_a_git_that_exits_otherwise(self, suites):
        with pytest.raises(SystemExit, match=r"^git rev-parse --verify nowhere: "):
            NI.git_bytes("rev-parse", "--verify", "nowhere")


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

    def test_refuses_a_rev_git_does_not_resolve(self, suites, tmp_path):
        with pytest.raises(SystemExit, match=r"^git archive"):
            NI.extract("nowhere", [], str(tmp_path))


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


class Test_identifier_scan:
    def test_accepts_the_census_module_by_its_path(self):
        scan = NI.identifier_scan()
        assert scan.ALLOWED_USER_PATH == "/Users/x/"
        assert NI.identifier_scan() is scan

    def test_refuses_a_census_module_that_will_not_load(self, tmp_path, monkeypatch):
        monkeypatch.setattr(NI, "SCAN", str(tmp_path / "absent.py"))
        with pytest.raises(FileNotFoundError):
            NI.identifier_scan.__wrapped__()


class Test_masked:
    def test_accepts_a_text_the_scan_refuses_nothing_of_as_it_is(self):
        text = "### 1. a defect\nlocation: `src/a.py:11`\nread /Users/x/log at example.com\n"
        assert NI.masked(text) == text

    def test_refuses_a_user_path_and_a_host_by_the_fixture_ones(self):
        scan = NI.identifier_scan()
        text = NI.masked(f"read {REFUSED_PATH}w/log at {REFUSED_HOST}\nnext\n")
        assert (
            text
            == f"read {scan.ALLOWED_USER_PATH}w/log at {scan.FIXTURE_DOMAIN}\nnext\n"
        )


class Test_apart:
    def test_accepts_a_text_whose_json_form_hides_nothing(self):
        scan = NI.identifier_scan()
        text = "github.com/x/y answered it.\n"
        assert NI.apart(text, scan) == text

    @pytest.mark.parametrize(
        "text",
        [
            "x\n" + "example.com answered it.",
            f"ends at {USER_ROOT}\nand",
            f'"{USER_ROOT}" + x',
        ],
        ids=[
            "a host after a line break",
            "the user root before a line break",
            "the user root in quotes",
        ],
    )
    def test_refuses_a_refusal_an_escape_takes_part_in(self, text):
        scan = NI.identifier_scan()
        kept = NI.apart(text, scan)
        assert kept != text and kept.replace(" ", "") == text.replace(" ", "")
        form = json.dumps(kept, ensure_ascii=False)
        assert [*scan.refused_domains(form), *scan.refused_user_paths(form)] == []


class Test_finding_rows:
    @pytest.mark.parametrize(
        "text, want",
        [
            (printed(FENCED_FIX), ["location: `src/a.py:11`"]),
            (
                printed(
                    "### 1. a finding with no location line\n\nseverity: should\n"
                    "verdict: open\n\n### 2. a finding in a broken shape\n\n"
                    "severity: should\nlocation: `src/a.py#unit`\nverdict: open\n"
                ),
                ["", "location: `src/a.py#unit`"],
            ),
            (
                printed(
                    "### 1. a defect\n\nseverity: must\nlocation: `src/b.py:1`\n"
                    "verdict: open\n",
                    before="location: `src/a.py:10`\n",
                    after="\n## Not judged\n\nlocation: `src/a.py:12`\n",
                ),
                ["location: `src/b.py:1`"],
            ),
        ],
        ids=[
            "a fenced fix",
            "a shape the check refuses",
            "lines outside every finding",
        ],
    )
    def test_accepts_each_finding_as_its_location_lines(self, text, want):
        assert NI.finding_rows(text) == want

    @pytest.mark.parametrize(
        "text, count",
        [
            (three_findings({1: UNCLOSED}), 3),
            (three_findings({1: "```\n## Not judged\n```\n\n", 3: UNCLOSED}), 3),
            (
                three_findings(
                    {1: UNCLOSED, 2: "```\n### 9. a quoted finding heading\n```\n\n"}
                ),
                4,
            ),
            (three_findings({}).replace("### 2.", "## Findings\n\n### 2.", 1), 3),
            (three_findings({}).replace("## Findings\n", "## Findings (3)\n", 1), 3),
        ],
        ids=[
            "a fence that never closes",
            "a fenced heading beside it",
            "a fenced finding heading",
            "a second findings section",
            "a misspelt findings heading",
        ],
    )
    def test_refuses_a_record_the_check_cannot_read_by_an_empty_row_per_heading(
        self, text, count
    ):
        """A record the check cannot read or split is one production reads
        as no finding; each raw finding heading is one empty, false row, so a
        proofer cannot lower its false count by breaking the record."""
        assert NI.finding_rows(text) == [""] * count


class Test_text_of:
    def test_accepts_the_record_a_run_kept(self):
        assert NI.text_of("c1", 0, {"agentic": {"report_text": "# r\n"}}) == "# r\n"

    @pytest.mark.parametrize(
        "run",
        [{}, {"agentic": {"report_rows": ["x"]}}, {"agentic": {"report_text": 5}}],
        ids=["no agentic", "rows and no text", "a text that is no string"],
    )
    def test_refuses_a_run_that_keeps_no_text(self, run):
        with pytest.raises(ValueError, match=r"^c1, run 2, keeps no report_text"):
            NI.text_of("c1", 2, run)


class Test_reads_record:
    @pytest.mark.parametrize("path", [REPORT, "r/x-report.md"])
    def test_accepts_a_truth_regex_over_a_round_record(self, path):
        grader = record_truth("truth-1", TRUTH)
        grader["config"]["target"]["path"] = path
        assert NI.reads_record(grader)

    @pytest.mark.parametrize(
        "grader",
        [
            {
                "name": "shape-x",
                "type": "regex",
                "config": {"target": {"path": REPORT}},
            },
            {
                "name": "truth-1",
                "type": "regex",
                "config": {"target": {"path": "notes.md"}},
            },
            {
                "name": "truth-1",
                "type": "file_exists",
                "config": {"target": {"path": REPORT}},
            },
            {"name": "truth-1", "type": "regex"},
        ],
        ids=["a shape grader", "another file", "not a regex", "no target"],
    )
    def test_refuses_any_other_grader(self, grader):
        assert not NI.reads_record(grader)


class Test_report_text:
    def test_accepts_the_last_record_the_session_printed(self, tmp_path):
        """The round record of the session's own `cat`, the last one
        winning, byte for byte, and never a subagent's output; a record
        printed as `trail/rounds/round-N.md` is kept as a `-report.md` one is."""
        last = [
            {
                "type": "text",
                "text": "### 1. new\n\nseverity: should\nlocation: `x:1`\n"
                "verdict: open\n\n## Confirmations\n\nconfirms: none\nholds, at `x:2`.\n",
            }
        ]
        denied = {
            "type": "system",
            "subtype": "permission_denied",
            "message": "Permission to use Read has been denied",
        }
        events = [
            {"type": "system", "subtype": "init", "cwd": "/w"},
            *cat("a", "location: `x:9`"),
            denied,
            {"type": "assistant", "message": {"content": "plain text"}},
            *cat("c", last, path="seal/threads/i/trail/rounds/round-1.md"),
            *cat("b", "location: `x:7`", parent="s"),
        ]
        text = NI.report_text(trace_at(tmp_path / "t.jsonl", events, "not json\n"))
        assert text == last[0]["text"]
        assert NI.finding_rows(printed(text)) == ["location: `x:1`"]

    @pytest.mark.parametrize(
        "events",
        [
            [],
            cat("a", "location: `x:9`", error=True),
            cat("a", "location: `x:9`", path="notes.md"),
            cat("a", "location: `x:9`", parent="s"),
        ],
        ids=["nothing printed", "a cat that failed", "another file", "a subagent's"],
    )
    def test_refuses_a_print_that_is_not_the_sessions_record(self, tmp_path, events):
        assert NI.report_text(trace_at(tmp_path / "t.jsonl", events)) == ""

    def test_refuses_to_keep_what_the_identifier_scan_refuses(self, tmp_path):
        scan = NI.identifier_scan()
        shown = printed(
            "### 1. a defect\n\nseverity: must\nlocation: `src/a.py:11`\n"
            f"evidence: read {REFUSED_PATH}w/log at {REFUSED_HOST}\nverdict: open\n",
            after=f"\n{REFUSED_HOST} answered it.\n",
        )
        text = NI.report_text(
            trace_at(tmp_path / "t.jsonl", cat("a", shown, path=REPORT))
        )
        assert REFUSED_PATH not in text and REFUSED_HOST not in text
        assert f"{scan.ALLOWED_USER_PATH}w/log at {scan.FIXTURE_DOMAIN}" in text
        assert NI.finding_rows(text) == ["location: `src/a.py:11`"]


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
        """A count read as zero makes a broken run look cheaper, and rule 5
        then passes the rewrite on it."""
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


def saved_side(tmp_path, runs, rev="abc", partial=False):
    """A saved side at TMP_PATH/side.raw whose runs are RUNS, `(trace events
    or None, error)` each; its path."""
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
        "cases": [{"name": "c1", "arms": {"with": arms}}],
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
    def test_accepts_each_runs_text_cost_and_calls_and_the_sides_meta(self, tmp_path):
        events = [
            *cat("a", "location: `x:1`", path=REPORT),
            assistant([use("Read", "r")]),
            RESULT,
        ]
        result = NI.annotate(saved_side(tmp_path, [(events, None)]))
        assert result["cases"][0]["arms"]["with"][0]["agentic"] == {
            "report_text": "location: `x:1`",
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
            assert run == {"report_text": "", "cost": None, "tool_calls": None}

    def test_refuses_a_machine_path_as_the_sides_rev(self, tmp_path):
        """A `--tree` side's `rev` names no machine path, since a committed
        record may not carry one; a side saved with one reads back as `tree`."""
        result = NI.annotate(
            saved_side(tmp_path, [(None, None)], rev=str(tmp_path / "t"))
        )
        assert result["agentic"]["rev"] == "tree"


class Test_write_side:
    def test_accepts_the_annotated_side_as_json_with_its_characters(self, tmp_path):
        events = cat("a", "location: `x:1` — é", path=REPORT)
        out = tmp_path / "side.json"
        assert NI.write_side(saved_side(tmp_path, [(events, None)]), str(out)) == 0
        text = out.read_text(encoding="utf-8")
        assert "`x:1` — é" in text and text.endswith("}\n")

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
            run_one_side(
                tmp_path, monkeypatch, cat("a", "location: `src/a.py:3`", path=REPORT)
            )
        saved, out = tmp_path / "side.raw", tmp_path / "again.json"

        def no_eval(command, env):
            raise AssertionError("--from-raw ran the eval again")

        monkeypatch.setattr(NI, "call_eval", no_eval)
        monkeypatch.setattr(NI, "annotate", real)
        assert NI.main(["run", "--from-raw", str(saved), "--out", str(out)]) == 0
        data = json.loads(out.read_text(encoding="utf-8"))
        assert data["cases"][0]["arms"]["with"][0]["agentic"]["report_text"] == (
            "location: `src/a.py:3`"
        )
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


class Test_side_numbers:
    def test_accepts_a_side_as_its_rows_its_graders_and_its_cost(self):
        text = record_of(["location: `src/a.py:11`", "location: `src/a.py:40`"])
        result = printed_side(text, [("truth-1", TRUTH)])
        case = result["cases"][0]
        case["graders"].append({"name": "shape-x", "type": "file_exists"})
        run = case["arms"]["with"][0]
        run["graders"] += [
            {"name": "shape-x", "passed": True},
            {"name": "note", "passed": True},
        ]
        run["agentic"].update(
            cost={
                k: RESULT[k] for k in ("total_cost_usd", "duration_ms", "modelUsage")
            },
            tool_calls=7,
        )
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
        assert (got["rows"], got["false"]) == (2, 1)
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

    def test_accepts_a_truth_found_only_inside_a_fence_as_found_by_no_run(self):
        fenced = r"^location: .*(?:src\/a\.py:(?:40)(?!\d))"
        got = NI.side_numbers(
            printed_side(printed(FENCED_FIX), [("truth-1", fenced)], ["truth-1"])
        )
        assert got["graders"][("c1", "truth-1")] == ["truth", 0, 1]
        assert (got["rows"], got["false"]) == (1, 1)

    def test_refuses_a_run_with_no_text_and_a_truth_it_cannot_grade(self):
        with pytest.raises(ValueError, match=r"^c1, run 0, keeps no report_text"):
            NI.side_numbers({"cases": [{"name": "c1", "arms": {"with": [{}]}}]})
        result = printed_side(record_of([]), [("truth-1", TRUTH)])
        result["cases"][0]["graders"][0]["config"]["flags"] = "q"
        with pytest.raises(ValueError, match=r"^c1: truth-1 carries the flag 'q'"):
            NI.side_numbers(result)

    def test_refuses_a_cost_one_run_lacks_and_a_cut_side(self):
        result = printed_side(record_of([]))
        runs = result["cases"][0]["arms"]["with"]
        runs[0]["agentic"]["cost"] = {
            "total_cost_usd": 1.0,
            "duration_ms": 1000,
            "modelUsage": RESULT["modelUsage"],
        }
        runs.append({"graders": [], "agentic": {"report_text": ""}})
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
    "rule 1: two finds fewer": (
        numbers(graders={("c1", "truth-1"): ("truth", 2, 2, 0, 2)}),
        "fail",
    ),
    "rule 1: one find fewer, still found by a new run, is noise": (
        numbers(graders={("c1", "truth-1"): ("truth", 2, 2, 1, 2)}),
        "pass",
    ),
    "rule 1: one find fewer, found by no new run": (
        numbers(graders={("c1", "truth-1"): ("truth", 1, 2, 0, 2)}),
        "fail",
    ),
    "rule 1: two truths one find fewer each is no longer noise": (
        numbers(
            graders={
                ("c1", "truth-1"): ("truth", 2, 2, 1, 2),
                ("c1", "truth-2"): ("truth", 2, 2, 1, 2),
            }
        ),
        "fail",
    ),
    "rule 2: false rate up by exactly the margin": (numbers(new_false=3), "pass"),
    "rule 2: false rate up past the margin": (numbers(new_false=4), "fail"),
    "rule 3: the total falling by one shape run": (
        numbers(graders={("c1", "shape-report-exists"): ("shape", 2, 2, 1, 2)}),
        "fail",
    ),
    "rule 3: the total falling by one reach run": (
        numbers(graders={("c1", "reach-proofer"): ("reach", 2, 2, 1, 2)}),
        "fail",
    ),
    "rule 3: a new side passing more often": (
        numbers(graders={("c1", "shape-report-exists"): ("shape", 1, 2, 2, 2)}),
        "pass",
    ),
    "rule 3: a reach run lost and a shape run gained share one total": (
        numbers(
            graders={
                ("c1", "reach-proofer"): ("reach", 2, 2, 1, 2),
                ("c1", "shape-findings"): ("shape", 1, 2, 2, 2),
            }
        ),
        "pass",
    ),
    "rule 3: a grader failing every new run where the baseline passed it, the total held": (
        numbers(
            graders={
                ("c1", "shape-report-exists"): ("shape", 2, 2, 0, 2),
                ("c1", "shape-findings"): ("shape", 0, 2, 2, 2),
            }
        ),
        "fail",
    ),
    "rule 3: a grader the baseline never passed, failing every new run, is not named": (
        numbers(graders={("c1", "shape-report-exists"): ("shape", 0, 2, 0, 2)}),
        "pass",
    ),
    "rule 3: a grader the baseline lacks does not offset a lost run": (
        numbers(
            graders={
                ("c1", "shape-report-exists"): ("shape", 2, 2, 1, 2),
                ("c1", "reach-sealer"): ("reach", 0, 0, 2, 2),
            }
        ),
        "fail",
    ),
    "rule 3: a shape grader failing as often as on the baseline": (
        numbers(graders={("c1", "shape-report-exists"): ("shape", 1, 2, 1, 2)}),
        "pass",
    ),
    "rule 3: a reach grader the baseline lacks, short of every new run": (
        numbers(graders={("c1", "reach-sealer"): ("reach", 0, 0, 1, 2)}),
        "fail",
    ),
    "rule 3: a shape grader only the baseline carried, in a case both sides ran": (
        numbers(graders={("c1", "shape-needs-a-fix"): ("shape", 2, 2, 0, 0)}),
        "pass",
    ),
    "rule 4: a preload no smaller than the baseline's": (
        numbers(new_bytes=100000),
        "fail",
    ),
    "rule 5: tokens per tool call 1.05 times the baseline's": (
        numbers(new_tokens=1050000),
        "fail",
    ),
    "rule 5: tokens per tool call falling while the total rises": (
        numbers(new_tokens=1200000, new_calls=150),
        "pass",
    ),
    "rule 5: tokens per tool call rising while the total falls": (
        numbers(new_tokens=900000, new_calls=80),
        "fail",
    ),
    "rule 5: tokens per tool call equal to the baseline's": (
        numbers(new_tokens=1200000, new_calls=120),
        "fail",
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
    "no result: tokens unknown": (numbers(new_tokens=None), "no result"),
    "no result: tool calls unknown": (numbers(new_calls=None), "no result"),
    "no result: no tool calls": (numbers(old_calls=0), "no result"),
    "no result: preload bytes unknown": (numbers(old_bytes=None), "no result"),
    "no result: a case run a different number of times": (
        numbers(graders={("c1", "truth-1"): ("truth", 2, 2, 1, 1)}),
        "no result",
    ),
}
PASSING = sorted(k for k, (_n, v) in VERDICTS.items() if v == "pass")
FAILING = sorted(k for k, (_n, v) in VERDICTS.items() if v != "pass")


class Test_verdict:
    @pytest.mark.parametrize("name", PASSING)
    def test_accepts_a_new_side_no_worse_than_the_baseline(self, name):
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
                    "the baseline's 4/4 (rule 3): c1/shape-report-exists 1/2 against 2/2"
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
                    "the baseline's 4/4 (rule 3): c1/reach-proofer 1/2 against 2/2, "
                    "c1/shape-report-exists 0/2 against 2/2",
                    "shape grader c1/shape-report-exists failed every new run (0/2) "
                    "where the baseline passed it 2/2 (rule 3)",
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
    def test_refuses_with_rule_3s_lines_in_their_order(self, graders, reasons):
        assert NI.verdict(numbers(graders=graders)) == ("fail", reasons)

    def test_refuses_with_a_line_for_each_other_rule(self):
        _v, reasons = NI.verdict(
            numbers(
                graders={("c1", "truth-1"): ("truth", 2, 2, 0, 2)},
                new_false=5,
                new_bytes=100000,
                new_tokens=1000000,
            )
        )
        assert reasons == [
            "recall fell from 4 to 2 finds: c1/truth-1",
            "false-finding rate rose from 0.100 to 0.250",
            "the new preload is 100000 bytes, not below the baseline's 100000 (rule 4)",
            "the new side read 10000.0 tokens across every model per tool call "
            "(1000000 over 100), not below the baseline's 10000.0 (1000000 over 100) (rule 5)",
        ]


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
    def test_accepts_both_sides_and_the_two_derived_rows(self):
        lines = NI.cost_rows(numbers())
        assert lines[:2] == [
            "| Baseline spend USD | 10.0000 |",
            "| New spend USD | 10.0000 |",
        ]
        assert "| New tokens per tool call | 9000.0 |" in lines
        assert "| New tokens per true find | 225000 |" in lines
        assert "| Baseline preload bytes | 100000 |" in lines

    def test_refuses_a_number_it_does_not_know_as_unknown(self):
        lines = NI.cost_rows(
            numbers(
                new_tokens=None,
                old_calls=0,
                graders={
                    ("c1", "truth-1"): ("truth", 0, 2, 0, 2),
                    ("c1", "truth-2"): ("truth", 0, 2, 0, 2),
                },
            )
        )
        assert "| New tokens read, every model | unknown |" in lines
        assert "| Baseline tokens per tool call | unknown |" in lines
        assert "| Baseline tokens per true find | unknown |" in lines


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
        assert text.startswith("# proofer — phase 3 non-inferiority\n")
        assert text.endswith("\nVerdict: pass\n\n- every pass rule holds\n")

    def test_refuses_a_failing_side_with_its_reasons_and_a_cut_one_as_no_result(self):
        old = {("c1", "truth-1"): ("truth", 2, 2), ("c1", "truth-2"): ("truth", 2, 2)}
        new = {("c1", "truth-1"): ("truth", 0, 2), ("c1", "truth-2"): ("truth", 0, 2)}
        text = written(old, new)
        assert (
            "\nVerdict: fail\n\n- recall fell from 4 to 0 finds: c1/truth-1, c1/truth-2\n"
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
        assert NI.read_record("| Baseline report rows | x |\n")[3][0].startswith(
            "the record does not parse: "
        )
        edited = written(tokens=1100000).replace("Verdict: fail", "Verdict: pass")
        assert "it says `pass` and its numbers give `fail`" in NI.read_record(edited)[3]


class Test_check_record:
    def test_accepts_a_sound_pass(self):
        assert NI.check_record(written()) == []

    @pytest.mark.parametrize(
        "over", [{"cut": True}, {"tokens": 1100000}], ids=["no result", "fail"]
    )
    def test_refuses_anything_but_pass(self, over):
        problems = NI.check_record(written(**over))
        assert any(p.startswith("its numbers give `") for p in problems), problems

    def test_refuses_an_edited_cell_the_verdict_does_not_follow(self):
        text = written()
        hungrier = text.replace("| New tool calls | 100 |", "| New tool calls | 90 |")
        assert hungrier != text
        problems = NI.check_record(hungrier)
        assert any("says `pass` and its numbers give `fail`" in p for p in problems)
        assert any("rule 5" in p for p in problems)


MODEL_GRADERS = {
    ("c1", "truth-1"): ("truth", 2, 2, 2, 2),
    ("c1", "shape-commits-nothing"): ("shape", 2, 2, 2, 2),
    ("c1", "reach-sealer"): ("reach", 2, 2, 2, 2),
}


def model_numbers(graders=MODEL_GRADERS, **over):
    """A model record's numbers: the Sonnet side half the spend and two
    bytes larger, so its own verdict fails rule 4, which `model` reads past."""
    over.setdefault("new_spend", 5.0)
    over.setdefault("new_bytes", 100002)
    return {**numbers(**over), "graders": dict(graders)}


class Test_cheaper_model:
    def test_accepts_sonnet_where_every_grader_holds_and_it_spent_less(self):
        assert NI.verdict(model_numbers())[0] == "fail"
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
        assert (
            capsys.readouterr().out == re.search(r"^Verdict: .*$", text, re.M)[0] + "\n"
        )

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

    def test_refuses_a_side_read_before_986_and_one_naming_no_suite(
        self, tmp_path, capsys
    ):
        old = eval_side(tmp_path, "old", "a" * 40, "b" * 40)
        new = eval_side(tmp_path, "new", "a" * 40, "b" * 40)
        out = tmp_path / "proofer-phase-3.md"
        argv = [*self.ARGV, "--old", old, "--new", new, "--out", str(out)]
        read_before_986(old)
        assert NI.main(argv) == 2 and not out.exists()
        said = capsys.readouterr().err
        assert old in said and "the reader before #986" in said
        unnamed = eval_side(tmp_path, "unnamed", None, None)
        assert (
            NI.main([*self.ARGV, "--old", unnamed, "--new", new, "--out", str(out)])
            == 2
        )
        assert "records no suite_rev" in capsys.readouterr().err


class Test_check:
    def test_accepts_a_record_whose_verdict_holds(self, tmp_path):
        path = tmp_path / "r.md"
        path.write_text(written(), encoding="utf-8")
        assert NI.main(["check", str(path)]) == 0

    def test_refuses_a_failing_record_and_one_over_two_suites(self, tmp_path, capsys):
        path = tmp_path / "r.md"
        old = {("c1", "truth-1"): ("truth", 2, 2), ("c1", "truth-2"): ("truth", 2, 2)}
        new = {("c1", "truth-1"): ("truth", 0, 2), ("c1", "truth-2"): ("truth", 0, 2)}
        path.write_text(
            written(old, new).replace("Verdict: fail", "Verdict: pass"),
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
            text = NI.render(
                "sealer", 4, side(GRADED), side(GRADED, spend=5.0, tokens=1100000)
            )
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


class Test_scalar:
    @pytest.mark.parametrize(
        "text, want",
        [
            (
                "{source: file, path: 'it''s, {a}.md'}",
                {"source": "file", "path": "it's, {a}.md"},
            ),
            ("'it''s'", "it's"),
            ("2", 2),
            ("-3", -3),
        ],
        ids=["a flow map", "a quoted string", "an integer", "a negative integer"],
    )
    def test_accepts_a_map_a_quoted_string_and_an_integer(self, text, want):
        assert NI.scalar(text) == want

    @pytest.mark.parametrize("text", ["regex", "1.5"])
    def test_refuses_anything_else_and_keeps_its_text(self, text):
        assert NI.scalar(f" {text} ") == text


class Test_grader_at:
    def test_accepts_a_truth_file_at_a_commit(self, suites):
        grader = NI.grader_at(suites["wide"], f"{CASE}/graders/truth-1.md")
        assert grader["name"] == "truth-1" and grader["config"]["pattern"] == WIDE

    def test_refuses_a_file_the_commit_does_not_hold(self, suites):
        with pytest.raises(SystemExit, match=r"^git show"):
            NI.grader_at(suites["own"], f"{CASE}/graders/truth-9.md")


class Test_grader_from:
    def test_accepts_what_behaviour_writes_field_for_field(self):
        pattern = r"^location: .*it's(?:a|b)"
        name, text = BEHAVIOUR.report_regex(
            "truth", "q", "it's, {a}.md", pattern, "A defect.", "m", weight=2
        )
        assert NI.grader_from(f"graders/{name}", text) == {
            "name": "truth-q",
            "type": "regex",
            "weight": 2,
            "config": {
                "target": {"source": "file", "path": "it's, {a}.md"},
                "pattern": pattern,
                "flags": "m",
                "match": "contains",
            },
        }

    def test_accepts_a_file_naming_no_weight_and_no_match(self):
        got = NI.grader_from(
            "graders/truth-1.md", "---\ntype: regex\npattern: 'x'\n---\nA defect.\n"
        )
        assert (got["weight"], got["config"]["match"]) == (1, "contains")

    def test_refuses_a_file_with_no_front_matter(self):
        with pytest.raises(
            ValueError, match=r"^graders/truth-1\.md has no front matter$"
        ):
            NI.grader_from("graders/truth-1.md", "A defect.\n")


class Test_suite_files:
    def test_accepts_every_file_of_every_case_by_its_blob(self, suites, _suites):
        d, _commits = _suites
        got = NI.suite_files(suites["more"], "proofer")
        assert sorted(got) == [CASE, "evals/behaviour/proofer/c2"]
        blob = git(d, "rev-parse", f"{suites['more']}:{CASE}/case.yaml").stdout.strip()
        assert got[CASE][f"{CASE}/case.yaml"] == blob

    def test_refuses_an_agent_with_no_suite_as_no_case(self, suites):
        assert NI.suite_files(suites["own"], "crafter") == {}


class Test_is_truth_file:
    def test_accepts_a_cases_truth_grader(self):
        assert NI.is_truth_file(f"{CASE}/graders/truth-1.md")

    @pytest.mark.parametrize(
        "path", [f"{CASE}/graders/shape-x.md", f"{CASE}/truth-1.md", "truth-1.md"]
    )
    def test_refuses_any_other_file(self, path):
        assert not NI.is_truth_file(path)


class Test_truths_at:
    def test_accepts_each_cases_truth_graders(self, suites):
        got = NI.truths_at(suites["own"], NI.suite_files(suites["own"], "proofer"))
        assert [g["config"]["pattern"] for g in got[CASE]] == [TRUTH]

    def test_refuses_a_case_with_no_truth_as_none(self, suites):
        got = NI.truths_at(suites["more"], NI.suite_files(suites["more"], "proofer"))
        assert got["evals/behaviour/proofer/c2"] == []


class Test_grade:
    @pytest.mark.parametrize(
        "rows, found",
        [
            (["location: `src/b.py:1`", "location: `src/a.py:11`"], True),
            (["location: `src/a.py:40`"], False),
        ],
    )
    def test_accepts_a_contains_regex_over_the_rows(self, rows, found):
        got = NI.grade(record_truth("truth-1", TRUTH), rows)
        assert got == {
            "name": "truth-1",
            "passed": found,
            "weight": 1,
            "explanation": "regraded from the kept report text: "
            + ("found" if found else "not found"),
            "withOnly": False,
            "scored": True,
        }

    @pytest.mark.parametrize(
        "change, why",
        [
            ({"type": "file_exists"}, "is not a regex the report must contain"),
            ({"match": "equals"}, "is not a regex the report must contain"),
            ({"flags": "mu"}, "carries the flag 'u'"),
        ],
        ids=["not a regex", "not contains", "an unknown flag"],
    )
    def test_refuses_a_grader_it_cannot_read(self, change, why):
        grader = record_truth("truth-1", TRUTH)
        if "type" in change:
            grader["type"] = change["type"]
        else:
            grader["config"].update(change)
        with pytest.raises(ValueError, match=f"^truth-1 {re.escape(why)}"):
            NI.grade(grader, ["location: `src/a.py:11`"])


class Test_mean:
    def test_accepts_values_as_their_mean(self):
        assert NI.mean(iter([1, 2, 6])) == 3

    def test_refuses_no_value_as_zero(self):
        assert NI.mean([]) == 0


class Test_case_runs:
    def test_accepts_every_arms_runs(self):
        assert NI.case_runs({"arms": {"a": [1, 2], "b": [3]}}) == [1, 2, 3]

    def test_refuses_a_case_with_no_arm_as_no_run(self):
        assert NI.case_runs({}) == []


class Test_regraded:
    def test_accepts_a_side_graded_on_new_truths_with_its_scores_recomputed(
        self, suites, tmp_path
    ):
        with open(
            graded_side(tmp_path, suites["own"], ROWS, [True, False]), encoding="utf-8"
        ) as f:
            result = json.load(f)
        wide = [record_truth("truth-1", WIDE)]
        got = NI.regraded(result, {CASE: wide})
        case = got["cases"][0]
        assert [r["passed"] for r in case["arms"]["with"]] == [True, True]
        assert case["aggregates"] == {"score": 1.0, "passRate": 1.0}
        assert got["aggregates"] == {
            "casesTotal": 1,
            "casesPassed": 1,
            "overallScore": 1.0,
            "overallPassRate": 1.0,
        }
        assert result["cases"][0]["aggregates"] == {"score": 0.75, "passRate": 0.5}

    def test_accepts_the_whole_text_where_whole_is_set(self, suites, tmp_path):
        side_path = graded_side(
            tmp_path, suites["own"], ROWS, [True, False], spoil=fenced_first_run
        )
        with open(side_path, encoding="utf-8") as f:
            result = json.load(f)
        truths = {CASE: [record_truth("truth-1", TRUTH)]}
        first = NI.regraded(result, truths, whole=True)["cases"][0]["arms"]["with"][0]
        assert {g["name"]: g["passed"] for g in first["graders"]}["truth-1"] is True
        rows = NI.regraded(result, truths)["cases"][0]["arms"]["with"][0]
        assert {g["name"]: g["passed"] for g in rows["graders"]}["truth-1"] is False

    def test_refuses_a_run_with_no_text_and_a_truth_it_cannot_grade(
        self, suites, tmp_path
    ):
        with open(
            graded_side(tmp_path, suites["own"], ROWS, [True, False]), encoding="utf-8"
        ) as f:
            result = json.load(f)
        flagged = record_truth("truth-1", TRUTH)
        flagged["config"]["flags"] = "x"
        with pytest.raises(
            ValueError, match=r"^proofer c1: truth-1 carries the flag 'x'"
        ):
            NI.regraded(result, {CASE: [flagged]})
        del result["cases"][0]["arms"]["with"][1]["agentic"]
        with pytest.raises(
            ValueError, match=r"^proofer c1, run 1, keeps no report_text"
        ):
            NI.regraded(result, {CASE: []})


class Test_differs:
    def test_accepts_two_sums_of_one_score_in_another_order(self):
        assert (
            NI.differs(
                {"score": 0.1 + 0.2, "passed": True},
                {"score": 0.3, "passed": True},
                ("score", "passed"),
            )
            == []
        )

    def test_refuses_a_value_the_again_does_not_give_and_skips_one_not_recorded(self):
        assert NI.differs({"score": 0.5}, {"score": 1.0, "x": 1}, ("score", "x")) == [
            "score 0.5, not 1.0"
        ]


class Test_unreproduced:
    def test_accepts_a_side_graded_again_as_it_recorded(self, suites, tmp_path):
        with open(
            graded_side(tmp_path, suites["own"], ROWS, [True, False]), encoding="utf-8"
        ) as f:
            result = json.load(f)
        files = NI.suite_files(suites["own"], "proofer")
        again = NI.regraded(result, NI.truths_at(suites["own"], files), whole=True)
        assert NI.unreproduced(result, again) == []

    def test_refuses_a_truth_result_its_text_does_not_give(self, suites, tmp_path):
        with open(
            graded_side(tmp_path, suites["own"], ROWS, [True, True]), encoding="utf-8"
        ) as f:
            result = json.load(f)
        files = NI.suite_files(suites["own"], "proofer")
        again = NI.regraded(result, NI.truths_at(suites["own"], files), whole=True)
        assert NI.unreproduced(result, again)[0] == (
            "proofer c1, run 1: it recorded {'truth-1': True} and its report text gives "
            "{'truth-1': False}"
        )


class Test_regrade:
    def test_accepts_a_side_onto_its_own_suite_unchanged(self, suites, tmp_path):
        side_path = graded_side(tmp_path, suites["own"], ROWS, [True, False])
        out = tmp_path / "out.json"
        assert regraded_to(side_path, suites["own"], out) == 0
        with open(side_path, encoding="utf-8") as f:
            before = json.load(f)
        after = json.loads(out.read_text(encoding="utf-8"))
        old, new = NI.side_numbers(before), NI.side_numbers(after)
        assert (new["rows"], new["false"]) == (old["rows"], old["false"]) == (3, 2)
        assert new["graders"] == old["graders"]
        assert after["aggregates"] == before["aggregates"]
        assert after["agentic"]["suite_rev"] == suites["own"]

    def test_accepts_a_wider_truth_and_names_the_suite_its_runs_answered(
        self, suites, tmp_path, capsys
    ):
        side_path = graded_side(tmp_path, suites["own"], ROWS, [True, False])
        out = tmp_path / "out.json"
        assert regraded_to(side_path, suites["wide"], out) == 0
        assert (
            capsys.readouterr().out
            == f"graded on {suites['wide'][:8]}: 3 rows, 0 false\n"
        )
        after = json.loads(out.read_text(encoding="utf-8"))
        numbers_after = NI.side_numbers(after)
        assert numbers_after["graders"][("proofer c1", "truth-1")] == ["truth", 2, 2]
        meta = after["agentic"]
        assert (meta["suite_rev"], meta["regraded_from"]) == (
            suites["wide"],
            suites["own"],
        )
        assert meta["suite_tree"] == NI.suite_tree(suites["wide"], "proofer")
        again = tmp_path / "again.json"
        assert regraded_to(str(out), suites["wide"], again) == 0
        assert (
            json.loads(again.read_text(encoding="utf-8"))["agentic"]["regraded_from"]
            == (suites["own"])
        )

    def test_accepts_a_side_the_eval_found_on_a_fenced_line(self, suites, tmp_path):
        """The eval searched the whole file, so the side's own suite gives
        its result back only from the whole text; graded on a suite, the run
        is read by its finding rows, where the fenced line is no row."""
        side_path = graded_side(
            tmp_path, suites["own"], ROWS, [True, False], spoil=fenced_first_run
        )
        out = tmp_path / "out.json"
        assert regraded_to(side_path, suites["own"], out) == 0
        after = json.loads(out.read_text(encoding="utf-8"))
        assert NI.side_numbers(after)["graders"][("proofer c1", "truth-1")] == [
            "truth",
            0,
            2,
        ]

    @pytest.mark.parametrize(
        "own, rev, found, spoil, named",
        [
            ("own", "wide", [True, True], None, "proofer c1, run 1: it recorded {"),
            (
                "own",
                "wide",
                [True, False],
                run_score_off,
                "proofer c1, run 0: it recorded score",
            ),
            (
                "own",
                "wide",
                [True, False],
                case_score_off,
                "proofer c1: its aggregates",
            ),
            ("own", "wide", [True, False], side_score_off, "the side's aggregates"),
            (
                "own",
                "wide",
                [True, False],
                truth_not_its_suites,
                "proofer c1: its truth",
            ),
            ("own", "wide", [True, False], no_suite, "suite is unknown"),
            (
                "own",
                "wide",
                [True, False],
                no_agent,
                "records no agent or no suite_rev",
            ),
            ("own", "more", [True, False], with_c2, "proofer c2: the suite it ran"),
            ("more", "wide", [True, False], with_c2, "proofer c2: the suite at"),
            ("own", "prompt", [True, False], None, "proofer c1: the suite at"),
            ("own", "more", [True, False], None, "proofer/c2: the suite at"),
            ("own", "kind", [True, False], None, "proofer c1: truth-1 is not"),
            ("own", "flag", [True, False], None, "proofer c1: truth-1 carries"),
            ("own", "plain", [True, False], None, "c1/graders/truth-1.md has no"),
        ],
        ids=[
            "rows-do-not-reproduce",
            "a-run-score-does-not-reproduce",
            "a-case-score-does-not-reproduce",
            "the-side-score-does-not-reproduce",
            "a-truth-not-its-suites",
            "no-suite",
            "an-agent-of-no-suite",
            "a-case-its-own-suite-lacks",
            "a-case-the-target-lacks",
            "a-non-truth-file-differs",
            "another-case",
            "a-truth-no-row-answers",
            "an-unknown-flag",
            "no-front-matter",
        ],
    )
    def test_refuses_a_side_it_cannot_stand_in_for(
        self, suites, tmp_path, capsys, own, rev, found, spoil, named
    ):
        side_path = graded_side(tmp_path, suites[own], ROWS, found, spoil)
        out = tmp_path / "out.json"
        assert regraded_to(side_path, suites[rev], out) == 2
        assert not out.exists()
        assert named in capsys.readouterr().err

    def test_refuses_a_side_read_before_986(self, suites, tmp_path, capsys):
        side_path = graded_side(tmp_path, suites["own"], ROWS, [True, False])
        read_before_986(side_path)
        out = tmp_path / "out.json"
        assert regraded_to(side_path, suites["own"], out) == 2
        assert not out.exists()
        said = capsys.readouterr().err
        assert side_path in said and "the reader before #986" in said


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
            (
                ["regrade", "--side", "s", "--suite-rev", "HEAD", "--out", "o"],
                "regrade",
            ),
        ],
    )
    def test_accepts_each_subcommand_and_hands_it_on(self, monkeypatch, argv, called):
        seen = []
        for name, fn in (
            ("run_side", "run"),
            ("compare", "compare"),
            ("check", "check"),
            ("model", "model"),
            ("regrade", "regrade"),
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
        ],
        ids=["no subcommand", "no source", "two sources", "no such agent"],
    )
    def test_refuses_arguments_it_cannot_use(self, monkeypatch, argv):
        monkeypatch.setattr(NI, "run_side", lambda a: 0)
        monkeypatch.setattr(NI, "compare", lambda a: 0)
        with pytest.raises(SystemExit) as stopped:
            NI.main(argv)
        assert stopped.value.code == 2


test_census = census_case(TARGET)
