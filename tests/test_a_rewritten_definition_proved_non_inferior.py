"""A rewritten preload is proved not worse, and the proof is recomputed (#923).

`evals/scripts/noninferiority.py` judges a new side of the behaviour suite
against a baseline by five pass rules and writes `evals/<agent>-phase-N.md`
under the work item. This module holds three things:

- T10: an agent whose preload — its definition and the skills its
  `skills:` list names — differs from the one a work item's
  `evals/baseline-<agent>.json` measured owes a record beside it that
  measured the preload as it stands, and whose numbers give `pass`.
- T11: the verdict is the five rules applied to the record's own numbers,
  so a record saying `pass` over failing numbers is red.
- T12: a phase record's `## Rule census` names, for every rule, a grader
  that exercises it or `not exercisable — <why>`.

What it cannot see: an agent with no baseline owes nothing, so the proof
starts when the baseline is committed; and a grader that matches the wrong
thing passes, which the phase's review reads.
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
    """Numbers every rule passes: two truths found twice a side, no false
    rows, every shape grader green, a rule grader held on both sides."""
    graders = {
        ("c1", "truth-1"): ("truth", 2, 2, 2, 2),
        ("c1", "truth-2"): ("truth", 2, 2, 2, 2),
        ("c1", "shape-report-exists"): ("shape", 2, 2, 2, 2),
        ("c1", "reach-warden"): ("reach", 2, 2, 2, 2),
        ("c2", "rule-bare-integer-id"): ("rule", 1, 2, 1, 2),
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
    "rule 4: a rule every old run met and no new run met, recall up": (
        numbers(
            graders={
                ("c2", "rule-bare-integer-id"): ("rule", 2, 2, 0, 2),
                ("c1", "truth-3"): ("truth", 0, 2, 2, 2),
            }
        ),
        "fail",
    ),
    "rule 4: a rule no old run met is no loss": (
        numbers(graders={("c2", "rule-bare-integer-id"): ("rule", 0, 2, 0, 2)}),
        "pass",
    ),
    "rule 5: the new side cut short": (numbers(new_cut=True), "no result"),
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


def side(graders, rows=20, false=2, cut=False, preload=None):
    return {
        "graders": {k: [v[0], v[1], v[2]] for k, v in graders.items()},
        "rows": rows,
        "false": false,
        "runs": {},
        "cut": cut,
        "preload": preload or {"agents/warden.md": "a" * 64},
        "id": "2026-10-14T00:00:00Z 000000000000",
    }


def record(old_graders, new_graders, **new):
    return ni.render("warden", 3, side(old_graders), side(new_graders, **new))


def test_a_record_reads_back_to_the_numbers_it_was_written_from():
    g = {("c1", "truth-1"): ("truth", 2, 2), ("c1", "shape-x"): ("shape", 2, 2)}
    text = record(g, g)
    numbers_back, stated, preload = ni.parse_record(text)
    assert stated == "pass"
    assert ni.verdict(numbers_back)[0] == "pass"
    assert preload == {"agents/warden.md": "a" * 64}
    assert ni.check_record(text) == []


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


# --- T10: a changed preload owes a passing record --------------------------


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


def baseline(root):
    evals = root / "seal" / "specs" / "1-item" / "evals"
    evals.mkdir(parents=True)
    data = {
        "specseal": {
            "agent": "warden",
            "preload": ni.preload_hashes(str(root), "warden"),
        }
    }
    (evals / "baseline-warden.json").write_text(json.dumps(data), encoding="utf-8")
    return evals


def passing_record(root, cut=False):
    g = {("c1", "truth-1"): ("truth", 2, 2), ("c1", "shape-x"): ("shape", 2, 2)}
    new = side(g, cut=cut, preload=ni.preload_hashes(str(root), "warden"))
    return ni.render("warden", 3, side(g), new)


def test_a_changed_preload_with_no_passing_record_is_red(tmp_path):
    root = tree(tmp_path)
    evals = baseline(root)
    assert ni.owed_records(str(root)) == [], "an unchanged preload owes nothing"

    (root / "skills" / "code-review" / "SKILL.md").write_text(
        "# shorter\n", encoding="utf-8"
    )
    problems = ni.owed_records(str(root))
    assert problems and "skills/code-review/SKILL.md" in problems[0], problems

    (evals / "warden-phase-3.md").write_text(passing_record(root), encoding="utf-8")
    assert ni.owed_records(str(root)) == []

    (evals / "warden-phase-3.md").write_text(
        passing_record(root, cut=True), encoding="utf-8"
    )
    assert ni.owed_records(str(root)), "a cut-short record was read as a result"

    (evals / "warden-phase-3.md").write_text(passing_record(root), encoding="utf-8")
    (root / "agents" / "warden.md").write_text(
        "---\nname: warden\nskills:\n  - code-review\n---\n\n# edited after\n",
        encoding="utf-8",
    )
    assert ni.owed_records(str(root)), (
        "a record of an earlier preload was read as this one's"
    )


def test_every_baseline_in_the_tree_is_answered():
    assert ni.owed_records(ROOT) == []


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


# --- T12: the rule census ----------------------------------------------------


CENSUS = """## Rule census

| Rule | Where it went | Exercised by |
|---|---|---|
| A finding id is a bare integer | `agents/warden.md` §Report | `rule-warden/rule-bare-integer-id` |
| The report is written to its path | `agents/warden.md` §Report | replay-x/shape-report-exists |
| Nothing commits | `## Removes` row 2 | not exercisable — no output shows it |
"""


def test_the_census_refuses_a_rule_with_neither_grader_nor_reason():
    assert ni.census_problems(CENSUS) == []
    empty = CENSUS + "| A rule nobody can observe | `agents/warden.md` §Role |  |\n"
    assert ni.census_problems(empty), "an empty Exercised by cell passed"
    bare = CENSUS + "| A rule | `agents/warden.md` §Role | not exercisable |\n"
    assert ni.census_problems(bare), "a reason-less not-exercisable passed"


def test_every_census_in_the_tree_names_a_grader_or_a_reason():
    problems = []
    specs = os.path.join(ROOT, "seal", "specs")
    for item in sorted(os.listdir(specs)) if os.path.isdir(specs) else []:
        phases = os.path.join(specs, item, "phases")
        for name in sorted(os.listdir(phases)) if os.path.isdir(phases) else []:
            with open(os.path.join(phases, name), encoding="utf-8") as f:
                problems += [
                    f"{item}/phases/{name}: {p}" for p in ni.census_problems(f.read())
                ]
    assert not problems, problems
