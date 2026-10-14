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
