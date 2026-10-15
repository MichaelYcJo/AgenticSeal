"""A rewritten preload is proved not worse, and the proof is recomputed (#923).

`evals/scripts/noninferiority.py` judges a new side of the behaviour suite
against a baseline by five pass rules and writes `evals/<agent>-phase-N.md`
under the work item. The verdict is the five rules applied to the record's
own numbers, outcome first and then cost, so a record saying `pass` over
failing numbers is red; and a run's cost is read off its trace's `result`
event, so a run with none is no result rather than free.

What it cannot see: a grader that matches the wrong thing passes, which the
phase's review reads; and nothing here makes a later edit of a definition
owe a run, by design.
"""

import importlib.util
import json
import os
import re

import pytest

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, "evals", "scripts", "noninferiority.py")


def load():
    spec = importlib.util.spec_from_file_location("noninferiority", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ni = load()


# --- T11: the five rules, one case per rule --------------------------------


def numbers(**over):
    """Numbers every rule passes: two truths found twice a side, a tenth of
    the rows false, every shape grader green, and a new side that read the
    same tokens and spent the same from a preload half the size."""
    graders = {
        ("c1", "truth-1"): ("truth", 2, 2, 2, 2),
        ("c1", "truth-2"): ("truth", 2, 2, 2, 2),
        ("c1", "shape-report-exists"): ("shape", 2, 2, 2, 2),
        ("c1", "reach-warden"): ("reach", 2, 2, 2, 2),
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
        "new_tokens": 1000000,
        "old_seconds": 600.0,
        "new_seconds": 600.0,
        "old_bytes": 100000,
        "new_bytes": 50000,
    }
    base.update(over)
    return base


CASES = {
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
    "rule 3: a shape grader short of every new run": (
        numbers(graders={("c1", "shape-report-exists"): ("shape", 2, 2, 1, 2)}),
        "fail",
    ),
    "rule 3: a reach grader short of every new run": (
        numbers(graders={("c1", "reach-warden"): ("reach", 2, 2, 1, 2)}),
        "fail",
    ),
    "rule 3: a shape grader short on the baseline": (
        numbers(graders={("c1", "shape-report-exists"): ("shape", 1, 2, 2, 2)}),
        "fail",
    ),
    "rule 4: spend 1.2 times the baseline's, outcome equal": (
        numbers(new_spend=12.0),
        "fail",
    ),
    "rule 4: spend at exactly 1.1 times the baseline's": (
        numbers(new_spend=11.0),
        "pass",
    ),
    "rule 4: tokens read 1.2 times the baseline's, outcome equal": (
        numbers(new_tokens=1200000),
        "fail",
    ),
    "rule 4: tokens read at exactly 1.1 times the baseline's": (
        numbers(new_tokens=1100000),
        "pass",
    ),
    "rule 4: a preload no smaller than the baseline's": (
        numbers(new_bytes=100000),
        "fail",
    ),
    "rule 4: wall seconds doubled are written and not judged": (
        numbers(new_seconds=1200.0),
        "pass",
    ),
    "rule 5: the new side cut short": (numbers(new_cut=True), "no result"),
    "rule 5: a side with a run whose cost is unknown": (
        numbers(new_spend=None, new_tokens=None, new_seconds=None),
        "no result",
    ),
    "rule 5: a side whose preload bytes are unknown": (
        numbers(old_bytes=None),
        "no result",
    ),
    "rule 5: the baseline cut short": (numbers(old_cut=True), "no result"),
    "rule 5: the sides ran a case a different number of times": (
        numbers(graders={("c1", "truth-1"): ("truth", 2, 2, 1, 1)}),
        "no result",
    ),
}


@pytest.mark.parametrize("name", sorted(CASES))
def test_the_verdict_is_recomputed_from_the_records_numbers(name):
    given, expected = CASES[name]
    assert ni.verdict(given)[0] == expected, ni.verdict(given)


SUITE = {"rev": "1" * 40, "tree": "2" * 40}


def side(
    graders,
    rows=20,
    false=2,
    cut=False,
    preload=None,
    suite=None,
    spend=10.0,
    tokens=1000000,
    seconds=600.0,
    size=100000,
):
    return {
        "graders": {k: [v[0], v[1], v[2]] for k, v in graders.items()},
        "rows": rows,
        "false": false,
        "runs": {},
        "cut": cut,
        "preload": preload or {"agents/warden.md": "a" * 64},
        "id": "2026-10-14T00:00:00Z 000000000000",
        "suite": suite or SUITE,
        "spend": spend,
        "tokens": tokens,
        "seconds": seconds,
        "bytes": size,
    }


def record(old_graders, new_graders, **new):
    new.setdefault("size", 50000)
    return ni.render("warden", 3, side(old_graders), side(new_graders, **new))


def test_a_record_reads_back_to_the_numbers_it_was_written_from():
    """Guards S1: the record carries both sides' spend, tokens read, wall
    seconds and preload bytes, and they read back to the numbers the
    verdict was computed from, so editing one is judged again."""
    g = {("c1", "truth-1"): ("truth", 2, 2), ("c1", "shape-x"): ("shape", 2, 2)}
    text = record(g, g, spend=10.123456, tokens=900000, seconds=512.34)
    numbers_back, stated, preload = ni.parse_record(text)
    assert stated == "pass"
    assert ni.verdict(numbers_back)[0] == "pass"
    assert preload == {"agents/warden.md": "a" * 64}
    assert ni.check_record(text) == []
    assert {k: numbers_back[k] for k in ni.COST_FIELDS} == {
        "old_spend": 10.0,
        "new_spend": 10.1235,
        "old_tokens": 1000000,
        "new_tokens": 900000,
        "old_seconds": 600.0,
        "new_seconds": 512.3,
        "old_bytes": 100000,
        "new_bytes": 50000,
    }
    dearer = text.replace("| New spend USD | 10.1235 |", "| New spend USD | 12.0000 |")
    assert dearer != text
    problems = ni.check_record(dearer)
    assert any("says `pass` and its numbers give `fail`" in p for p in problems), (
        problems
    )
    assert any("spend rose" in p and "rule 4" in p for p in problems), problems


def test_a_costlier_side_fails_naming_rule_4_and_wall_seconds_never_judge():
    """Guards S3: a new side whose pooled spend is 1.2 times the baseline's,
    outcome equal, fails and says which rule; wall seconds are written and
    never a reason."""
    g = {("c1", "truth-1"): ("truth", 2, 2), ("c1", "shape-x"): ("shape", 2, 2)}
    text = record(g, g, spend=12.0, seconds=6000.0)
    assert "Verdict: fail" in text
    assert "| New wall seconds | 6000.0 |" in text
    reasons = text.split("Verdict: fail", 1)[1]
    assert "rule 4" in reasons and "spend rose from $10.0000 to $12.0000" in reasons
    assert "seconds" not in reasons, reasons


def test_a_record_saying_pass_over_failing_numbers_is_red():
    old = {("c1", "truth-1"): ("truth", 2, 2), ("c1", "truth-2"): ("truth", 2, 2)}
    new = {("c1", "truth-1"): ("truth", 0, 2), ("c1", "truth-2"): ("truth", 0, 2)}
    text = record(old, new)
    assert "Verdict: fail" in text
    edited = text.replace("Verdict: fail", "Verdict: pass")
    problems = ni.check_record(edited)
    assert any("says `pass` and its numbers give `fail`" in p for p in problems), (
        problems
    )


def test_a_cut_short_side_is_no_result_and_never_a_pass():
    g = {("c1", "truth-1"): ("truth", 2, 2)}
    text = record(g, g, cut=True)
    assert "Verdict: no result" in text
    assert ni.check_record(text), "a cut-short record was read as a result"


def eval_side(tmp_path, name, rev, tree):
    """A one-run side `run` could have written, run on the suite REV/TREE."""
    run = {
        "graders": [{"name": "shape-x", "passed": True}],
        "specseal": {"report_rows": []},
    }
    case = {
        "name": "c1",
        "graders": [{"name": "shape-x", "type": "file_exists"}],
        "arms": {"with": [run]},
    }
    meta = {
        "agent": "warden",
        "preload": {},
        "cut_short": False,
        "suite_rev": rev,
        "suite_tree": tree,
    }
    path = tmp_path / f"{name}.json"
    path.write_text(
        json.dumps({"startedAt": name, "cases": [case], "specseal": meta}),
        encoding="utf-8",
    )
    return str(path)


def test_compare_refuses_two_sides_that_ran_different_suites(tmp_path, capsys):
    """Guards the proof's premise: both sides ran the same cases. A baseline
    taken before a case's prompt or graders changed is compared to nothing,
    and the sentence names both suites."""
    old = eval_side(tmp_path, "old", "a" * 40, "b" * 40)
    out = tmp_path / "warden-phase-3.md"
    other = eval_side(tmp_path, "new", "c" * 40, "d" * 40)
    argv = [
        "compare",
        "--agent",
        "warden",
        "--phase",
        "3",
        "--old",
        old,
        "--out",
        str(out),
    ]
    assert ni.main([*argv, "--new", other]) == 2
    assert not out.exists(), "a record was written over two suites"
    said = capsys.readouterr().err
    assert "a" * 12 in said and "c" * 12 in said, said
    same = eval_side(tmp_path, "same", "c" * 40, "b" * 40)
    assert ni.main([*argv, "--new", same]) == 0, "one suite at two commits was refused"
    assert "| Baseline suite | " + "a" * 40 + " " + "b" * 40 + " |" in out.read_text(
        encoding="utf-8"
    )
    # A side written before `suite_tree` was recorded names its commit alone,
    # and its suite is read as that commit's tree of the agent's cases.
    head = ni.git_bytes("rev-parse", "HEAD").decode("utf-8").strip()
    commit_only = eval_side(tmp_path, "commit-only", head, None)
    by_tree = eval_side(tmp_path, "by-tree", "e" * 40, ni.suite_tree("HEAD", "warden"))
    base = ["compare", "--agent", "warden", "--phase", "3", "--out", str(out)]
    assert ni.main([*base, "--old", commit_only, "--new", by_tree]) == 0
    assert ni.main([*base, "--old", commit_only, "--new", other]) == 2


def test_check_refuses_a_record_whose_sides_ran_different_suites(tmp_path):
    g = {("c1", "shape-x"): ("shape", 2, 2)}
    text = ni.render(
        "warden", 3, side(g), side(g, suite={"rev": "3" * 40, "tree": "4" * 40})
    )
    path = tmp_path / "warden-phase-3.md"
    path.write_text(text, encoding="utf-8")
    assert ni.main(["check", str(path)]) == 2
    assert any("ran different suites" in p for p in ni.check_record(text))
    unnamed = "\n".join(line for line in text.split("\n") if "suite |" not in line)
    assert any("names no suite" in p for p in ni.check_record(unnamed))


# --- what a side's run saves and records -------------------------------------


def tree(tmp_path, skill_text="# code-review\n"):
    """A plugin tree with one agent preloading one skill."""
    (tmp_path / "agents").mkdir()
    (tmp_path / "agents" / "warden.md").write_text(
        "---\nname: warden\nskills:\n  - code-review\n---\n\n# warden\n",
        encoding="utf-8",
    )
    (tmp_path / "skills" / "code-review").mkdir(parents=True)
    (tmp_path / "skills" / "code-review" / "SKILL.md").write_text(
        skill_text, encoding="utf-8"
    )
    return tmp_path


def run_one_side(tmp_path, monkeypatch, events):
    """`run` over a one-agent plugin tree with the eval replaced by one run
    whose trace holds EVENTS; the side `--out` holds, read back."""
    plugin = tmp_path / "plugin"
    plugin.mkdir()
    tree(plugin)
    kept = tmp_path / "e-Cost01"
    (kept / "out").mkdir(parents=True)
    (kept / "out" / "trace.jsonl").write_text(
        "".join(json.dumps(e) + "\n" for e in events), encoding="utf-8"
    )
    run = {
        "graders": [{"name": "shape-x", "passed": True}],
        "error": None,
        "tracePath": str(kept / "out" / "trace.jsonl"),
    }
    raw = {
        "startedAt": "t",
        "partial": False,
        "cases": [
            {
                "name": "c1",
                "graders": [{"name": "shape-x", "type": "file_exists"}],
                "arms": {"with": [run]},
            }
        ],
    }

    def paid_eval(command, env):
        with open(command[command.index("--json") + 1], "w", encoding="utf-8") as f:
            json.dump(raw, f)

    monkeypatch.setattr(ni, "call_eval", paid_eval)
    out = tmp_path / "side.json"
    argv = ["run", "--agent", "warden", "--tree", str(plugin), "--out", str(out)]
    assert ni.main(argv) == 0
    return json.loads(out.read_text(encoding="utf-8")), plugin


RESULT = {
    "type": "result",
    "subtype": "success",
    "total_cost_usd": 2.5,
    "duration_ms": 412000,
    "usage": {
        "input_tokens": 40,
        "cache_creation_input_tokens": 60000,
        "cache_read_input_tokens": 900000,
        "output_tokens": 7000,
    },
}


def test_a_run_records_what_it_cost(tmp_path, monkeypatch):
    """Guards S1 and Q12: each run's spend, seconds and usage are read off
    its trace's top-level `result` event and pooled per side, tokens read
    being input plus cache creation plus cache read; a subagent's event is
    not the session's; and a trace with no `result` event is a side whose
    cost is unknown, which the verdict refuses as no result, never free."""
    sub = dict(RESULT, total_cost_usd=99.0, parent_tool_use_id="s")
    events = [{"type": "system", "subtype": "init"}, sub, RESULT]
    data, plugin = run_one_side(tmp_path, monkeypatch, events)
    cost = data["cases"][0]["arms"]["with"][0]["specseal"]["cost"]
    assert cost == {
        "total_cost_usd": 2.5,
        "duration_ms": 412000,
        "usage": RESULT["usage"],
    }
    size = sum(
        os.path.getsize(plugin / p) for p in ni.preload_files(str(plugin), "warden")
    )
    assert data["specseal"]["preload_bytes"] == size
    numbers_one = ni.side_numbers(data)
    assert (numbers_one["spend"], numbers_one["tokens"]) == (2.5, 960040)
    assert (numbers_one["seconds"], numbers_one["bytes"]) == (412.0, size)

    bare = tmp_path / "bare"
    bare.mkdir()
    data, _ = run_one_side(bare, monkeypatch, [{"type": "system"}, sub])
    assert data["cases"][0]["arms"]["with"][0]["specseal"]["cost"] is None
    unknown = ni.side_numbers(data)
    assert unknown["spend"] is None and unknown["tokens"] is None
    merged = ni.merged(numbers_one, unknown)
    verdict, reasons = ni.verdict(merged)
    assert verdict == "no result", (verdict, reasons)
    assert any("cost" in r for r in reasons), reasons


def test_a_paid_run_survives_a_later_crash_and_is_read_again_from_what_was_saved(
    tmp_path, monkeypatch
):
    """Guards the runs a side paid for: the eval's JSON and every trace are
    saved beside `--out` before anything reads them, so a crash after the
    runs loses nothing, and `run --from-raw` reads the saved side again
    without running the eval."""
    plugin = tmp_path / "plugin"
    plugin.mkdir()
    tree(plugin)
    kept = tmp_path / "e-Fake01"
    (kept / "out").mkdir(parents=True)
    row = "| 🟡 1 | found | `src/a.py:3` | open | read |"
    use = {
        "type": "tool_use",
        "id": "a",
        "name": "Bash",
        "input": {"command": "cat r/round-1-report.md"},
    }
    result = {"type": "tool_result", "tool_use_id": "a", "content": row}
    (kept / "out" / "trace.jsonl").write_text(
        json.dumps({"message": {"content": [use]}})
        + "\n"
        + json.dumps({"message": {"content": [result]}})
        + "\n",
        encoding="utf-8",
    )
    run = {"graders": [], "error": None, "tracePath": str(kept / "out" / "trace.jsonl")}
    raw = {
        "startedAt": "t",
        "partial": False,
        "cases": [{"name": "c1", "graders": [], "arms": {"with": [run]}}],
    }

    def paid_eval(command, env):
        with open(command[command.index("--json") + 1], "w", encoding="utf-8") as f:
            json.dump(raw, f)

    def crash(*_args, **_kwargs):
        raise RuntimeError("a crash after the runs")

    real_annotate = ni.annotate
    monkeypatch.setattr(ni, "call_eval", paid_eval)
    monkeypatch.setattr(ni, "annotate", crash)
    out = tmp_path / "baseline-warden.json"
    with pytest.raises(RuntimeError):
        ni.main(["run", "--agent", "warden", "--tree", str(plugin), "--out", str(out)])
    saved = tmp_path / "baseline-warden.raw"
    assert json.loads((saved / "raw.json").read_text(encoding="utf-8")) == raw
    assert not kept.exists(), "the kept run was left behind"

    def no_eval(command, env):
        raise AssertionError("--from-raw ran the eval again")

    monkeypatch.setattr(ni, "call_eval", no_eval)
    monkeypatch.setattr(ni, "annotate", real_annotate)
    assert ni.main(["run", "--from-raw", str(saved), "--out", str(out)]) == 0
    side = json.loads(out.read_text(encoding="utf-8"))
    assert side["cases"][0]["arms"]["with"][0]["specseal"]["report_rows"] == [row]
    assert side["specseal"]["agent"] == "warden"
    assert side["specseal"]["preload"] == ni.preload_hashes(str(plugin), "warden")
    assert side["specseal"]["cut_short"] is False


# --- the numbers a side is read to -------------------------------------------


def load_script(name):
    path = os.path.join(ROOT, "evals", "scripts", f"{name}.py")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


TRUTH = r"^\| (?:🔴|🟡) \d+ \|.*(?:src\/a\.py:(?:10|11|12)(?!\d))"


def test_a_side_counts_a_finding_row_no_truth_matches_as_false():
    """Guards pass rule 2's input: a row is false only when no truth grader's
    pattern matches it."""
    result = {
        "cases": [
            {
                "name": "c1",
                "graders": [
                    {"name": "truth-1", "type": "regex", "config": {"pattern": TRUTH}},
                    {"name": "shape-x", "type": "file_exists", "config": {}},
                ],
                "arms": {
                    "with": [
                        {
                            "graders": [
                                {"name": "truth-1", "passed": True},
                                {"name": "shape-x", "passed": True},
                            ],
                            "specseal": {
                                "report_rows": [
                                    "| 🟡 1 | the bug | `src/a.py:11` | open | read |",
                                    "| 🟡 2 | elsewhere | `src/a.py:40` | open | read |",
                                ]
                            },
                        }
                    ]
                },
            }
        ]
    }
    numbers = ni.side_numbers(result)
    assert (numbers["rows"], numbers["false"]) == (2, 1)
    assert numbers["graders"][("c1", "truth-1")] == ["truth", 1, 1]
    assert numbers["graders"][("c1", "shape-x")] == ["shape", 1, 1]


def test_the_report_rows_are_the_last_report_the_session_printed(tmp_path):
    """Guards where the false rows come from: the session's own `cat` of the
    report, the last one winning, and never a subagent's output."""

    def cat(call_id, content, parent=None):
        use = {"type": "tool_use", "id": call_id, "name": "Bash"}
        use["input"] = {"command": "cat r/round-1-report.md"}
        result = {"type": "tool_result", "tool_use_id": call_id, "content": content}
        events = [{"message": {"content": [use]}}, {"message": {"content": [result]}}]
        for event in events:
            if parent:
                event["parent_tool_use_id"] = parent
        return events

    last = [
        {
            "type": "text",
            "text": "| 🟡 1 | new | `x:1` | open | read |\n| ⬜ 2 | n | `x:2` | open | r |",
        }
    ]
    # The shapes a 2.1.296 trace carries beside a tool call, read off the
    # baseline's kept traces: a `permission_denied` event whose `message` is
    # a string, and events with no `message` at all.
    denied = {
        "type": "system",
        "subtype": "permission_denied",
        "tool_name": "Read",
        "message": "Permission to use Read has been denied",
    }
    events = [
        {"type": "system", "subtype": "init", "cwd": "/w"},
        *cat("a", "| 🟡 1 | old | `x:1` | open | read |"),
        denied,
        {"type": "assistant", "message": {"content": "plain text"}},
        *cat("c", last),
        *cat("b", "| 🔴 9 | sub | `x:1` | open | read |", parent="s"),
    ]
    trace = tmp_path / "trace.jsonl"
    trace.write_text(
        "\n".join(json.dumps(e) for e in events) + "\nnot json\n", encoding="utf-8"
    )
    assert ni.report_rows(str(trace)) == ["| 🟡 1 | new | `x:1` | open | read |"]


def test_only_a_directory_the_eval_kept_is_removed():
    """Guards the runner's cleanup: it removes a kept run's own directory and
    nothing a trace path could name elsewhere."""
    assert ni.kept_root("/tmp/e-Ab12cD/out/trace.jsonl") == "/tmp/e-Ab12cD"
    assert ni.kept_root("/tmp/claude-eval-x1/out/trace.jsonl") == "/tmp/claude-eval-x1"
    assert ni.kept_root("/Users/x/project/out/trace.jsonl") is None
    assert ni.kept_root("/tmp/e-Ab12cD/trace.jsonl") is None


def test_a_side_runs_the_tree_it_measures_and_no_installed_plugin():
    """Guards which plugin a side's sessions run: the measured tree's `bin/`
    first, and no installed plugin's `bin/` at all."""
    path = ni.side_path(
        "/w/tree", "/usr/bin:/Users/x/.claude/plugins/cache/p/p/1/bin:/bin"
    )
    assert path.split(os.pathsep) == [
        "/w/tree/bin",
        "/w/tree/.shims",
        "/usr/bin",
        "/bin",
    ]


def test_a_truth_is_a_fixed_finding_the_next_round_confirmed():
    """Guards the replay set's ground truth: a 🟡 closed fixed and named
    closed by the next round's 🟢 row, and no other."""
    rt = load_script("replay_targets")
    nxt = (
        "| 🟢 | round 1's finding 2 is closed — x | `a.md:3` | confirmed | read |\n"
        "| 🟢 | round 1's 🟡 4 is closed — y | `a.md:9` | confirmed | read |\n"
        "| 🟢 | round 2's finding 3 is closed — z | `a.md:9` | confirmed | read |\n"
        "| 🟡 5 | round 1's finding 5 is closed | `a.md:9` | open | read |\n"
    )
    assert rt.confirmed(nxt, 1) == {2, 4}


def test_a_truth_pattern_holds_its_line_window_and_no_further():
    rt = load_script("replay_targets")
    pattern = re.compile(rt.truth_pattern("`docs/x.md:100`", "HEAD"), re.M)
    assert pattern.search("| 🟡 1 | f | `docs/x.md:115` | open | g |")
    assert pattern.search("| 🔴 3 | f | `docs/x.md:85-90` | open | g |")
    assert not pattern.search("| 🟡 1 | f | `docs/x.md:116` | open | g |")
    assert not pattern.search("| 🟡 1 | f | `docs/x.md:1000` | open | g |")
    assert not pattern.search("| ⬜ 1 | f | `docs/x.md:100` | open | g |")


def test_a_seed_lands_on_a_code_token_and_never_in_a_string():
    sd = load_script("seed_defects")
    source = 'def f(a):\n    """a == b"""\n    return a == 1\n'
    tokens = sd.code_tokens(source)
    assert (3, "==") in tokens
    assert (2, "==") not in tokens
