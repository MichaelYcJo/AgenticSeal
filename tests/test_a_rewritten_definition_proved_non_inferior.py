"""A rewritten preload is proved not worse, and the proof is recomputed (#923).

`evals/scripts/noninferiority.py` judges a new side of the behaviour suite
against a baseline by five pass rules and writes `evals/<agent>-phase-N.md`
under the work item. The verdict is the five rules applied to the record's
own numbers, outcome first and then cost, each against the baseline and
none against an absolute (#957), so a record saying `pass` over failing
numbers is red. A run's tokens are read across every model off its trace's
`result` event `modelUsage` and judged per tool call, every `tool_use` block
its trace holds, so a run with no tokens or no calls is no result rather
than free; its total tokens, tokens per true find, spend and wall seconds
are written and judge nothing.

What it cannot see: a grader that matches the wrong thing passes, which the
phase's review reads; and nothing here makes a later edit of a definition
owe a run, by design.
"""

import importlib.util
import json
import ntpath
import os
import posixpath
import re
import subprocess
import types

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
    the rows false, every shape grader green, and a new side that read a
    tenth fewer tokens across every model over as many tool calls and spent
    the same from a preload half the size."""
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
    "rule 3: the shape and reach total falling by one shape run": (
        numbers(graders={("c1", "shape-report-exists"): ("shape", 2, 2, 1, 2)}),
        "fail",
    ),
    "rule 3: the shape and reach total falling by one reach run": (
        numbers(graders={("c1", "reach-warden"): ("reach", 2, 2, 1, 2)}),
        "fail",
    ),
    "rule 3: a new side passing more often than the baseline": (
        numbers(graders={("c1", "shape-report-exists"): ("shape", 1, 2, 2, 2)}),
        "pass",
    ),
    # Catches rule 3 still comparing each grader on its own (#966): one
    # grader's lost run fails a side whose shape and reach passes held,
    # which is #957 phase 2's run 2. No case before #966 sets a loss beside
    # a gain.
    "rule 3: one shape grader's lost run offset by another's gained run": (
        numbers(
            graders={
                ("c1", "shape-report-exists"): ("shape", 2, 2, 1, 2),
                ("c1", "shape-findings"): ("shape", 1, 2, 2, 2),
            }
        ),
        "pass",
    ),
    # Catches separate totals for shape and for reach: a lost reach run
    # offset by a gained shape run fails, which is one run deciding again.
    # The case above moves shape graders alone, so it cannot tell.
    "rule 3: a reach run lost and a shape run gained share one total": (
        numbers(
            graders={
                ("c1", "reach-warden"): ("reach", 2, 2, 1, 2),
                ("c1", "shape-findings"): ("shape", 1, 2, 2, 2),
            }
        ),
        "pass",
    ),
    # Catches a rule 3 that reads the total alone: a grader the new side
    # failed on every run, where the baseline passed it, is offset by
    # another grader's gain and the side passes. Only this case holds the
    # total equal while a grader the baseline passed falls to none.
    "rule 3: a grader failing every new run where the baseline passed it, the total held": (
        numbers(
            graders={
                ("c1", "shape-report-exists"): ("shape", 2, 2, 0, 2),
                ("c1", "shape-findings"): ("shape", 0, 2, 2, 2),
            }
        ),
        "fail",
    ),
    # Catches a naming clause that names every grader the new side failed
    # on every run, whatever the baseline did. No other case has a grader
    # both sides fail on every run.
    "rule 3: a grader the baseline never passed, failing every new run, is not named": (
        numbers(graders={("c1", "shape-report-exists"): ("shape", 0, 2, 0, 2)}),
        "pass",
    ),
    # Catches totals that count a grader the baseline lacks: its new passes
    # would offset a common grader's lost run, with nothing on the
    # baseline's side to set against them.
    "rule 3: a grader the baseline lacks does not offset a lost run": (
        numbers(
            graders={
                ("c1", "shape-report-exists"): ("shape", 2, 2, 1, 2),
                ("c1", "reach-sealer"): ("reach", 0, 0, 2, 2),
            }
        ),
        "fail",
    ),
    # Catches a rule 3 that reads the new side alone and asks every run to
    # pass, which fails a rewrite for doing exactly what the baseline did:
    # the warden baseline fails three cases' shape graders itself (#957
    # phase 1).
    "rule 3: a shape grader failing as often on the new side as on the baseline": (
        numbers(graders={("c1", "shape-report-exists"): ("shape", 1, 2, 1, 2)}),
        "pass",
    ),
    # Catches a rule 3 that leaves out of both checks every grader the
    # baseline already fails, so a rewrite failing it more often still
    # passes: here it falls from 1/2 to 0/2, which lowers the total and is
    # named. The case above passes under that reading too.
    "rule 3: a shape grader passing less often than a baseline that fails it": (
        numbers(graders={("c1", "shape-report-exists"): ("shape", 1, 2, 0, 2)}),
        "fail",
    ),
    # Catches a rule 3 that reads a grader the baseline lacks as a baseline
    # rate of nothing, so a new grader failing every run passes. The grader
    # the baseline lacks is judged on the new side alone, as before #957;
    # the case above whose grader the baseline lacks passes it on every run,
    # so only this one fails it.
    "rule 3: a reach grader the baseline lacks, short of every new run": (
        numbers(graders={("c1", "reach-sealer"): ("reach", 0, 0, 1, 2)}),
        "fail",
    ),
    # The tolerance for a grader one side lacks holds only inside a case both
    # sides ran: `c1` is run twice a side here, so the grader the new side
    # lacks is the record's shape moving, not a case left unrun.
    "rule 3: a shape grader only the baseline carried, in a case both sides ran, is not judged": (
        numbers(graders={("c1", "shape-needs-a-fix"): ("shape", 2, 2, 0, 0)}),
        "pass",
    ),
    # Catches the tolerance above reaching a whole case: a case the new side
    # never ran, carrying only shape graders, left no trace in any rule and
    # the side passed (#957 round 1, finding 2). The case above keeps the
    # grader inside a case the new side ran, so it cannot tell.
    "no result: a case the baseline ran and the new side did not, whatever its graders": (
        numbers(graders={("c2", "shape-needs-a-fix"): ("shape", 2, 2, 0, 0)}),
        "no result",
    ),
    # The measured shape of the same defect: the smith's phase-3 side cut to
    # one of its four cases, every case carrying shape and reach graders
    # alone, read `pass`.
    "no result: a side cut to one case of four": (
        numbers(
            graders={
                (case, grader): (
                    k,
                    2,
                    2,
                    2 if case == "c1" else 0,
                    2 if case == "c1" else 0,
                )
                for case in ("c1", "c2", "c3", "c4")
                for grader, k in (
                    ("shape-report-exists", "shape"),
                    ("reach-smith", "reach"),
                )
            }
        ),
        "no result",
    ),
    "rule 4: a preload no smaller than the baseline's": (
        numbers(new_bytes=100000),
        "fail",
    ),
    "rule 5: tokens per tool call 1.2 times the baseline's": (
        numbers(new_tokens=1200000),
        "fail",
    ),
    # Catches a token rule with a margin, which passes a rewrite that read
    # more per call than the baseline; before #957 it was 1.1 times. The 1.2
    # case above fails under any margin below it, so only a rise inside the
    # old margin tells the two readings apart.
    "rule 5: tokens per tool call 1.05 times the baseline's": (
        numbers(new_tokens=1050000),
        "fail",
    ),
    # Catches rule 5 still judging the total (owner, 2026-10-17, after phase
    # 2): a rewrite whose calls each carry less context, and which makes more
    # of them, reads more tokens in all and passes. No other case moves the
    # calls.
    "rule 5: tokens per tool call falling while the total rises": (
        numbers(new_tokens=1200000, new_calls=150),
        "pass",
    ),
    # Catches the same rule the other way: fewer tokens in all over fewer
    # calls, each carrying more, fails. A rule reading the total passes it.
    "rule 5: tokens per tool call rising while the total falls": (
        numbers(new_tokens=900000, new_calls=80),
        "fail",
    ),
    # Catches a per-call comparison with `>` where the rule says strictly
    # below: equal per call, over more calls and more tokens, passes. No
    # other case puts the two sides' per-call figures equal.
    "rule 5: tokens per tool call equal to the baseline's": (
        numbers(new_tokens=1200000, new_calls=120),
        "fail",
    ),
    # Catches spend still judged, with or without a margin: a dearer side
    # with fewer tokens and an equal outcome fails. Spend is written and
    # judges nothing (#957); no other case moves spend alone.
    "spend 1.2 times the baseline's is written and not judged": (
        numbers(new_spend=12.0),
        "pass",
    ),
    "wall seconds doubled are written and not judged": (
        numbers(new_seconds=1200.0),
        "pass",
    ),
    # Catches spend's absence judged in its place: a side whose spend is
    # unknown while its tokens are known is no result. The run-level case
    # below makes tokens and spend unknown together, so it cannot tell.
    "spend and wall seconds unknown, tokens known, are not judged": (
        numbers(new_spend=None, new_seconds=None),
        "pass",
    ),
    "no result: the new side cut short": (numbers(new_cut=True), "no result"),
    "no result: a side with a run whose tokens are unknown": (
        numbers(new_spend=None, new_tokens=None, new_seconds=None),
        "no result",
    ),
    # Catches a side whose tool calls could not be counted read as judged:
    # with no divisor there is no per-call figure, and a zero would be a
    # division nobody can make. The token case above leaves the calls known.
    "no result: a side whose tool calls are unknown": (
        numbers(new_calls=None),
        "no result",
    ),
    "no result: a side with no tool calls": (
        numbers(old_calls=0),
        "no result",
    ),
    "no result: a side whose preload bytes are unknown": (
        numbers(old_bytes=None),
        "no result",
    ),
    "no result: the baseline cut short": (numbers(old_cut=True), "no result"),
    "no result: the sides ran a case a different number of times": (
        numbers(graders={("c1", "truth-1"): ("truth", 2, 2, 1, 1)}),
        "no result",
    ),
}


@pytest.mark.parametrize("name", sorted(CASES))
def test_the_verdict_is_recomputed_from_the_records_numbers(name):
    """Guards each pass rule on its own: the case's name says which, and a
    comment above a case added for #957 names the defect it catches and why
    no other case does."""
    given, expected = CASES[name]
    assert ni.verdict(given)[0] == expected, ni.verdict(given)


RULE_3_REASONS = {
    "the total falls": (
        {("c1", "shape-report-exists"): ("shape", 2, 2, 1, 2)},
        [
            "shape and reach graders passed 3/4 runs on the new side, fewer than "
            "the baseline's 4/4 (rule 3): c1/shape-report-exists 1/2 against 2/2"
        ],
    ),
    "a grader fails every new run, the total held": (
        {
            ("c1", "shape-report-exists"): ("shape", 2, 2, 0, 2),
            ("c1", "shape-findings"): ("shape", 0, 2, 2, 2),
        },
        [
            "shape grader c1/shape-report-exists failed every new run (0/2) "
            "where the baseline passed it 2/2 (rule 3)"
        ],
    ),
    "the total, then the named grader, then the grader the baseline lacks": (
        {
            ("c1", "shape-report-exists"): ("shape", 2, 2, 0, 2),
            ("c1", "reach-warden"): ("reach", 2, 2, 1, 2),
            ("c1", "reach-sealer"): ("reach", 0, 0, 1, 2),
        },
        [
            "shape and reach graders passed 1/4 runs on the new side, fewer than "
            "the baseline's 4/4 (rule 3): c1/reach-warden 1/2 against 2/2, "
            "c1/shape-report-exists 0/2 against 2/2",
            "shape grader c1/shape-report-exists failed every new run (0/2) "
            "where the baseline passed it 2/2 (rule 3)",
            "reach grader c1/reach-sealer, which the baseline lacks, failed on "
            "the new side (1/2) (rule 3)",
        ],
    ),
}


@pytest.mark.parametrize("name", sorted(RULE_3_REASONS))
def test_rule_3_names_the_total_and_each_grader_failing_every_new_run(name):
    """Guards S2 and S3 of #966 (contract §14): a falling shape and reach
    total is written with both totals and every grader whose passes fell,
    sorted, and a grader the new side failed on every run, where the
    baseline passed it, is named on a line of its own. Rule 3's lines come
    total first, then the named graders, then the graders the baseline
    lacks. The cases above read the verdict alone, so only this one reads
    the reasons rule 3 writes."""
    graders, reasons = RULE_3_REASONS[name]
    assert ni.verdict(numbers(graders=graders)) == ("fail", reasons)


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
    calls=100,
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
        "calls": calls,
        "seconds": seconds,
        "bytes": size,
    }


def record(old_graders, new_graders, **new):
    new.setdefault("size", 50000)
    new.setdefault("tokens", 900000)
    return ni.render("warden", 3, side(old_graders), side(new_graders, **new))


def test_a_record_reads_back_to_the_numbers_it_was_written_from():
    """Guards S1: the record carries both sides' spend, tokens read across
    every model, tool calls, wall seconds and preload bytes, and they read
    back to the numbers the verdict was computed from, so editing one is
    judged again. The tokens row says it counts every model, because the
    case session's own `usage` was 1.9% to 11.6% of it on the baseline (#957
    phase 1); the per-call and per-find rows are derived for a reader and
    read back as nothing."""
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
        "old_calls": 100,
        "new_calls": 100,
        "old_seconds": 600.0,
        "new_seconds": 512.3,
        "old_bytes": 100000,
        "new_bytes": 50000,
    }
    assert "| New tokens per tool call | 9000.0 |" in text, text
    assert "| New tokens per true find | 450000 |" in text, text
    row = "| New tool calls | {} |"
    assert row.format(100) in text, text
    hungrier = text.replace(row.format(100), row.format(90))
    assert hungrier != text
    problems = ni.check_record(hungrier)
    assert any("says `pass` and its numbers give `fail`" in p for p in problems), (
        problems
    )
    assert any("rule 5" in p for p in problems), problems


def test_spend_and_wall_seconds_are_written_and_never_judge():
    """Guards S3 as #957 turned it: a new side that spent 1.2 times the
    baseline and took ten times its wall seconds, reading more tokens in all
    and fewer per tool call with an equal outcome, passes with every number
    written; the same side reading as many per call as the baseline fails
    naming rule 5, and neither spend, seconds, the total nor the per-find
    figure is ever a reason. The rule cases above never render a record, so
    only this one reads the reasons a record prints."""
    g = {("c1", "truth-1"): ("truth", 2, 2), ("c1", "shape-x"): ("shape", 2, 2)}
    text = record(g, g, spend=12.0, seconds=6000.0, tokens=1200000, calls=150)
    assert "Verdict: pass" in text, text
    assert "| New spend USD | 12.0000 |" in text
    assert "| New wall seconds | 6000.0 |" in text
    assert "| New tokens read, every model | 1200000 |" in text
    assert "| New tokens per true find | 600000 |" in text
    text = record(g, g, spend=12.0, seconds=6000.0, tokens=1000000)
    assert "Verdict: fail" in text, text
    reasons = text.split("Verdict: fail", 1)[1]
    assert "rule 5" in reasons and "1000000" in reasons, reasons
    assert "spend" not in reasons and "seconds" not in reasons, reasons


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


# --- T7: the sealer's model, by the graders and the spend ---------------------


def model_of(tmp_path, capsys, old_graders, new_graders, **new):
    """`model` over a record `compare` could have written with the Opus side
    as `--old` and the Sonnet side as `--new`: `(exit, printed lines)`. The
    Sonnet side spends half by default, and its preload is two bytes larger
    (`sonnet` against `opus` in `model:`), so the record's own verdict fails
    rule 4 and `check` would refuse it, which `model` must not."""
    new.setdefault("spend", 5.0)
    new.setdefault("size", 100002)
    path = tmp_path / "sealer-model.md"
    path.write_text(
        ni.render("sealer", 4, side(old_graders), side(new_graders, **new)),
        encoding="utf-8",
    )
    code = ni.main(["model", str(path)])
    return code, capsys.readouterr().out.splitlines()


def test_the_model_is_decided_by_the_truths_and_the_spend(tmp_path, capsys):
    """Guards S7: `noninferiority.py model` prints `sonnet` only where no
    grader, truth, shape or reach, passes on the Sonnet side less often than
    on the Opus side and the Sonnet side spent less; anything else, a side cut
    short included, prints `opus` and one line naming why.

    The defects: a drop decided by cost alone (#957 S10), and a cheaper model
    that commits or writes outside its file, which every truth grader passes
    and only a shape grader sees (`questions.md` Q2's default). Nothing else
    catches either: `verdict` never judges spend, forgives one lost find as
    noise, and fails every model record on rule 4 whatever the graders say,
    so `check` refuses the very record this reads."""
    g = {
        ("c1", "truth-1"): ("truth", 2, 2),
        ("c1", "shape-commits-nothing"): ("shape", 2, 2),
        ("c1", "reach-sealer"): ("reach", 2, 2),
    }
    code, out = model_of(tmp_path, capsys, g, g)
    assert (code, out[0]) == (0, "sonnet"), out
    assert "Verdict: fail" in (tmp_path / "sealer-model.md").read_text(encoding="utf-8")
    for name, kind in (
        ("truth-1", "truth"),
        ("shape-commits-nothing", "shape"),
        ("reach-sealer", "reach"),
    ):
        lost = {**g, ("c1", name): (kind, 1, 2)}
        code, out = model_of(tmp_path, capsys, g, lost)
        assert (code, out[0]) == (0, "opus"), (name, out)
        assert len(out) == 2 and name in out[1], (name, out)
    for spend in (10.0, 12.0):
        code, out = model_of(tmp_path, capsys, g, g, spend=spend)
        assert (code, out[0]) == (0, "opus"), (spend, out)
        assert len(out) == 2 and "spen" in out[1], (spend, out)
    code, out = model_of(tmp_path, capsys, g, g, spend=None)
    assert (code, out[0]) == (0, "opus"), out
    code, out = model_of(tmp_path, capsys, g, g, cut=True)
    assert (code, out[0]) == (0, "opus"), out
    assert len(out) == 2 and "cut short" in out[1], out
    path = tmp_path / "sealer-model.md"
    model_of(tmp_path, capsys, g, g)
    edited = path.read_text(encoding="utf-8").replace("Verdict: fail", "Verdict: pass")
    path.write_text(edited, encoding="utf-8")
    assert ni.main(["model", str(path)]) == 2
    other = {"rev": "3" * 40, "tree": "4" * 40}
    model_of(tmp_path, capsys, g, g, suite=other)
    assert ni.main(["model", str(path)]) == 2
    assert ni.main(["model", str(tmp_path / "absent.md")]) == 2


def test_a_record_with_no_truth_grader_decides_opus(tmp_path, capsys):
    """Round 1 of #969, finding 6. S7 decides the model by every truth
    grader, so a record that carries none measured no outcome: `sonnet` there
    is a drop decided by cost alone, the defect S7 names. No graders at all,
    and a lone shape grader, both print `opus` and a reason saying so."""
    shape = {("c1", "shape-commits-nothing"): ("shape", 2, 2)}
    reach = {**shape, ("c1", "reach-sealer"): ("reach", 2, 2)}
    for graders in ({}, shape, reach):
        code, out = model_of(tmp_path, capsys, graders, graders)
        assert (code, out[0]) == (0, "opus"), (graders, out)
        assert len(out) == 2 and "no truth grader" in out[1], (graders, out)
    # Either side alone: a truth grader the other side never ran counts zero
    # runs there, so that side ran the case a different number of times,
    # which is a no result and `opus` already.
    truth = {**shape, ("c1", "truth-1"): ("truth", 2, 2)}
    for old, new, side in ((truth, shape, "Sonnet"), (shape, truth, "Opus")):
        code, out = model_of(tmp_path, capsys, old, new)
        assert (code, out[0]) == (0, "opus"), (side, out)
        assert "different number of times" in out[1], (side, out)


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
    # The case session's own tokens, which leave out the agent it spawned.
    "usage": {
        "input_tokens": 40,
        "cache_creation_input_tokens": 60000,
        "cache_read_input_tokens": 900000,
        "output_tokens": 7000,
    },
    # Every model's tokens, the spawned agent's among them, in the shape a
    # 2.1.296 trace carries (#957 phase 1).
    "modelUsage": {
        "claude-sonnet-5-5": {
            "inputTokens": 4,
            "outputTokens": 323,
            "cacheReadInputTokens": 27598,
            "cacheCreationInputTokens": 15057,
            "costUSD": 0.07,
        },
        "claude-opus-5-5": {
            "inputTokens": 28,
            "outputTokens": 8835,
            "cacheReadInputTokens": 445032,
            "cacheCreationInputTokens": 43597,
            "costUSD": 0.48,
        },
    },
}


def test_a_run_records_what_it_cost(tmp_path, monkeypatch):
    """Guards S1 and Q12: each run's spend, seconds and `modelUsage` are read
    off its trace's top-level `result` event and pooled per side, tokens
    read being input plus cache creation plus cache read summed over every
    model, so the agent the case spawned is counted and not only the case
    session's `usage`; a subagent's event is not the session's; and a trace
    with no `result` event, or one whose `result` event has no
    `modelUsage`, is a side whose tokens are unknown, which the verdict
    refuses as no result, never free (#957)."""
    sub = dict(RESULT, total_cost_usd=99.0, parent_tool_use_id="s")
    events = [{"type": "system", "subtype": "init"}, sub, RESULT]
    data, plugin = run_one_side(tmp_path, monkeypatch, events)
    cost = data["cases"][0]["arms"]["with"][0]["specseal"]["cost"]
    assert cost == {
        "total_cost_usd": 2.5,
        "duration_ms": 412000,
        "modelUsage": RESULT["modelUsage"],
    }
    size = sum(
        os.path.getsize(plugin / p) for p in ni.preload_files(str(plugin), "warden")
    )
    assert data["specseal"]["preload_bytes"] == size
    numbers_one = ni.side_numbers(data)
    every_model = 4 + 27598 + 15057 + 28 + 445032 + 43597
    assert (numbers_one["spend"], numbers_one["tokens"]) == (2.5, every_model)
    assert (numbers_one["seconds"], numbers_one["bytes"]) == (412.0, size)

    for name, last in (
        ("bare", sub),
        ("no-model-usage", {k: v for k, v in RESULT.items() if k != "modelUsage"}),
    ):
        where = tmp_path / name
        where.mkdir()
        data, _ = run_one_side(where, monkeypatch, [{"type": "system"}, last])
        unknown = ni.side_numbers(data)
        assert unknown["tokens"] is None, name
        verdict, reasons = ni.verdict(ni.merged(numbers_one, unknown))
        assert verdict == "no result", (name, verdict, reasons)
        assert any("tokens" in r for r in reasons), reasons
    # A `result` event with no `modelUsage` still writes its spend and
    # seconds, which judge nothing.
    assert (unknown["spend"], unknown["seconds"]) == (2.5, 412.0)
    assert data["cases"][0]["arms"]["with"][0]["specseal"]["cost"]["modelUsage"] is None

    # One run of two with no cost leaves the side's pooled cost unknown,
    # not the other run's cost alone.
    runs = data["cases"][0]["arms"]["with"]
    runs[0]["specseal"]["cost"] = None
    runs.append({"graders": [], "specseal": {"cost": cost, "report_rows": []}})
    assert ni.side_numbers(data)["spend"] is None
    assert ni.side_numbers(data)["tokens"] is None


def assistant(blocks, parent=None):
    """An assistant event holding BLOCKS, the agent's where PARENT is set."""
    event = {"type": "assistant", "message": {"content": blocks}}
    if parent:
        event["parent_tool_use_id"] = parent
    return event


def use(name, ident):
    return {"type": "tool_use", "id": ident, "name": name, "input": {}}


def test_a_run_counts_every_tool_call_its_trace_holds(tmp_path, monkeypatch):
    """Guards rule 5's divisor: a run's tool calls are every `tool_use` block
    in its trace, the case session's and the spawned agent's alike, a block
    an event repeats counted once by its id; a trace holding none, or one
    that cannot be read, gives no count, so the side is no result rather
    than divided by nothing (owner, 2026-10-17). The cost case above reads
    a trace with no calls at all; only this one counts them."""
    events = [
        {"type": "system", "subtype": "init"},
        assistant([{"type": "text", "text": "spawning"}, use("Agent", "t1")]),
        assistant([use("Bash", "t2"), use("Read", "t3")], parent="t1"),
        assistant([use("Read", "t3")], parent="t1"),
        {"type": "user", "message": "a string message holds no call"},
        RESULT,
    ]
    data, _plugin = run_one_side(tmp_path, monkeypatch, events)
    assert data["cases"][0]["arms"]["with"][0]["specseal"]["tool_calls"] == 3
    counted = ni.side_numbers(data)
    assert counted["calls"] == 3

    where = tmp_path / "none"
    where.mkdir()
    data, _plugin = run_one_side(where, monkeypatch, [{"type": "system"}, RESULT])
    assert data["cases"][0]["arms"]["with"][0]["specseal"]["tool_calls"] is None
    uncounted = ni.side_numbers(data)
    assert uncounted["calls"] is None
    verdict, reasons = ni.verdict(ni.merged(counted, uncounted))
    assert verdict == "no result", (verdict, reasons)
    assert any("tool calls" in r for r in reasons), reasons
    assert ni.tool_calls(str(tmp_path / "no-such-trace.jsonl")) is None


@pytest.mark.parametrize(
    ("model_usage", "want"),
    [
        (None, None),
        ({}, None),
        ({"m": "x"}, None),
        ({"m": {"inputTokens": 1, "cacheReadInputTokens": 2}}, None),
        (
            {
                "m": {
                    "inputTokens": 1,
                    "cacheReadInputTokens": 2,
                    "cacheCreationInputTokens": None,
                }
            },
            None,
        ),
        (
            {
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
            },
            66,
        ),
    ],
    ids=["absent", "empty", "not-a-model", "missing-count", "null-count", "two-models"],
)
def test_a_model_usage_missing_a_count_is_no_token_figure(model_usage, want):
    """Guards rule 5's input against a short trace: a `modelUsage` that is
    absent, empty, or has a model missing one of the three counts gives no
    token figure, never a smaller one, and two whole models sum their input,
    cache-creation and cache-read tokens and nothing else. A count read as
    zero makes a broken run look cheaper, and rule 5 then passes the rewrite
    on it. The run-level case above holds one whole `modelUsage` and one
    absent; only this one reaches a model whose counts are partial."""
    assert ni.tokens_read(model_usage) == want


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
    row = "location: `src/a.py:3`"
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
    # Round 1 of #969, finding 7: a `--tree` side's `rev` names no machine
    # path, since a committed record may not carry one (CONTRIBUTING.md
    # §House rules); the preload's hashes already name the content.
    assert side["specseal"]["rev"] == "tree", side["specseal"]["rev"]
    meta = json.loads((saved / "meta.json").read_text(encoding="utf-8"))
    assert meta["rev"] == "tree", meta["rev"]
    # A side saved before that, its `rev` an absolute path, reads back the same.
    meta["rev"] = str(tmp_path / "sonnet-tree")
    (saved / "meta.json").write_text(json.dumps(meta), encoding="utf-8")
    assert ni.main(["run", "--from-raw", str(saved), "--out", str(out)]) == 0
    side = json.loads(out.read_text(encoding="utf-8"))
    assert side["specseal"]["rev"] == "tree", side["specseal"]["rev"]


# --- the numbers a side is read to -------------------------------------------


def load_script(name):
    path = os.path.join(ROOT, "evals", "scripts", f"{name}.py")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


TRUTH = r"^location: .*(?:src\/a\.py:(?:10|11|12)(?!\d))"


def test_a_side_counts_a_finding_row_no_truth_matches_as_false():
    """Guards pass rule 2's input: a finding, read by its `location:` line,
    is false only when no truth grader's pattern matches it."""
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
                                    "location: `src/a.py:11`",
                                    "location: `src/a.py:40`",
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


# --- regrade: a committed side read again under another suite's truths (#971)

WIDE = r"^location: .*(?:src\/a\.py:(?:10|11|12|40)(?!\d))"
CASE = "evals/behaviour/warden/c1"


def suite_commits(tmp_path, monkeypatch):
    """A repository whose history holds four warden suites, with `ni` reading
    it: `own` (case c1, its truth-1 TRUTH), `wide` (truth-1 widened to line
    40), `prompt` (`wide` with c1's case.yaml changed) and `more` (`wide` with
    a case c2 added). `{name: commit}`."""
    bh = load_script("behaviour")
    d = tmp_path / "suites"
    d.mkdir()

    def git(*args):
        return subprocess.run(
            ["git", "-C", str(d), *args],
            check=True,
            capture_output=True,
            encoding="utf-8",
        ).stdout.strip()

    def write(rel, text):
        path = d / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def commit(name):
        git("add", "-A")
        git("commit", "-qm", name)
        return git("rev-parse", "HEAD")

    def truth(pattern):
        write(
            f"{CASE}/graders/truth-1.md",
            bh.report_regex("truth", "1", "r.md", pattern, "A defect.")[1],
        )

    git("init", "-q")
    git("config", "user.email", "t@example.com")
    git("config", "user.name", "t")
    write(f"{CASE}/case.yaml", "name: c1\n")
    write(
        f"{CASE}/graders/shape-x.md",
        bh.grader("shape", "x", "The report exists.", type="file_exists", path="r.md")[
            1
        ],
    )
    truth(TRUTH)
    commits = {"own": commit("own")}
    truth(WIDE)
    commits["wide"] = commit("wide")
    write(f"{CASE}/case.yaml", "name: c1, asked otherwise\n")
    commits["prompt"] = commit("prompt")
    git("reset", "-q", "--hard", commits["wide"])
    write("evals/behaviour/warden/c2/case.yaml", "name: c2\n")
    commits["more"] = commit("more")
    monkeypatch.setattr(ni, "ROOT", str(d))
    return commits


def graded_side(tmp_path, rev, rows, found):
    """A side of case c1 run on the suite at REV, its run I having printed
    ROWS[I] and recorded truth-1 as FOUND[I], its scores the ones a run of
    two graders gets. The path it is written to."""
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
    for printed, passed in zip(rows, found, strict=True):
        score = (1 + passed) / 2
        graders = [
            {"name": "shape-x", "passed": True, "weight": 1, "scored": True},
            {"name": "truth-1", "passed": passed, "weight": 1, "scored": True},
        ]
        runs.append(
            {
                "score": score,
                "passed": score >= 1,
                "graders": graders,
                "specseal": {"report_rows": printed},
            }
        )
    score = sum(r["score"] for r in runs) / len(runs)
    rate = sum(r["passed"] for r in runs) / len(runs)
    result = {
        "startedAt": "2026-10-19T00:00:00Z",
        "suite": {"threshold": 1},
        "cases": [
            {
                "name": "warden c1",
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
        "specseal": {
            "agent": "warden",
            "preload": {},
            "cut_short": False,
            "suite_rev": rev,
            "suite_tree": ni.suite_tree(rev, "warden"),
        },
    }
    path = tmp_path / "side.json"
    path.write_text(json.dumps(result), encoding="utf-8")
    return str(path)


ROWS = (
    ["location: `src/a.py:11`", "location: `src/a.py:40`"],
    ["location: `src/a.py:40`"],
)


def regrade(side, rev, out):
    return ni.main(["regrade", "--side", side, "--suite-rev", rev, "--out", str(out)])


def test_a_side_regraded_onto_its_own_suite_is_unchanged(tmp_path, monkeypatch):
    """Guards S3: under the suite it ran, a side's rows give back every
    truth result it recorded, so the rows, the false count, each grader's
    passes and the scores are the ones it was written with."""
    commits = suite_commits(tmp_path, monkeypatch)
    side = graded_side(tmp_path, commits["own"], ROWS, [True, False])
    out = tmp_path / "out.json"
    assert regrade(side, commits["own"], out) == 0
    with open(side, encoding="utf-8") as f:
        before = json.load(f)
    after = json.loads(out.read_text(encoding="utf-8"))
    old, new = ni.side_numbers(before), ni.side_numbers(after)
    assert (new["rows"], new["false"]) == (old["rows"], old["false"]) == (3, 2)
    assert new["graders"] == old["graders"]
    assert after["cases"][0]["aggregates"] == before["cases"][0]["aggregates"]
    assert after["aggregates"] == before["aggregates"]
    assert after["specseal"]["suite_rev"] == commits["own"]


def test_a_side_regraded_onto_a_wider_truth_counts_the_row_it_now_matches(
    tmp_path, monkeypatch
):
    """Guards the re-read itself: under a suite whose truth-1 also accepts
    line 40, the same rows find truth-1 on both runs and no row is false,
    the scores follow, and the side names the suite it is now graded on and
    the one it ran."""
    commits = suite_commits(tmp_path, monkeypatch)
    side = graded_side(tmp_path, commits["own"], ROWS, [True, False])
    out = tmp_path / "out.json"
    assert regrade(side, commits["wide"], out) == 0
    after = json.loads(out.read_text(encoding="utf-8"))
    numbers = ni.side_numbers(after)
    assert (numbers["rows"], numbers["false"]) == (3, 0)
    assert numbers["graders"][("warden c1", "truth-1")] == ["truth", 2, 2]
    case = after["cases"][0]
    truths = [g["config"]["pattern"] for g in case["graders"] if g["name"] == "truth-1"]
    assert truths == [WIDE]
    assert [r["passed"] for r in case["arms"]["with"]] == [True, True]
    assert case["aggregates"] == {"score": 1.0, "passRate": 1.0}
    assert after["aggregates"]["casesPassed"] == 1
    meta = after["specseal"]
    assert meta["suite_rev"] == commits["wide"]
    assert meta["suite_tree"] == ni.suite_tree(commits["wide"], "warden")
    assert meta["regraded_from"] == commits["own"]


@pytest.mark.parametrize(
    "rev, found, named",
    [
        # Its second run recorded truth-1 found, and its rows do not find it.
        ("wide", [True, True], "warden c1"),
        # The target suite asks the case otherwise, not only its truths.
        ("prompt", [True, False], "warden c1"),
        # The target suite holds a case the side never ran.
        ("more", [True, False], "c2"),
    ],
    ids=["rows-do-not-reproduce", "a-non-truth-file-differs", "another-case"],
)
def test_regrade_refuses_what_it_cannot_stand_in_for(
    tmp_path, monkeypatch, capsys, rev, found, named
):
    """Guards S4: a side whose rows do not give back its own truth results,
    or a target suite that changes a case beyond its `truth-` graders or
    holds other cases, is refused with exit 2, naming the case, and nothing
    is written."""
    commits = suite_commits(tmp_path, monkeypatch)
    side = graded_side(tmp_path, commits["own"], ROWS, found)
    out = tmp_path / "out.json"
    assert regrade(side, commits[rev], out) == 2
    assert not out.exists(), "a side was written that regrade cannot stand in for"
    assert named in capsys.readouterr().err


def test_the_report_rows_are_the_last_report_the_session_printed(tmp_path):
    """Guards where the false rows come from: the `location:` lines of the
    session's own `cat` of the report, the last one winning, and never a
    subagent's output. A record printed as `rounds/round-N.md` (0.22.0,
    #923) is read as a report is, and a confirmation's location is not a
    finding."""

    def cat(call_id, content, parent=None, path="r/round-1-report.md"):
        use = {"type": "tool_use", "id": call_id, "name": "Bash"}
        use["input"] = {"command": f"cat {path}"}
        result = {"type": "tool_result", "tool_use_id": call_id, "content": content}
        events = [{"message": {"content": [use]}}, {"message": {"content": [result]}}]
        for event in events:
            if parent:
                event["parent_tool_use_id"] = parent
        return events

    last = [
        {
            "type": "text",
            "text": "### 1. new\n\nseverity: should\nlocation: `x:1`\n"
            "verdict: open\n\n## Confirmations\n\nconfirms: none\nholds, at `x:2`.\n",
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
        *cat("a", "location: `x:9`"),
        denied,
        {"type": "assistant", "message": {"content": "plain text"}},
        *cat("c", last, path="seal/specs/i/rounds/round-1.md"),
        *cat("b", "location: `x:7`", parent="s"),
    ]
    trace = tmp_path / "trace.jsonl"
    trace.write_text(
        "\n".join(json.dumps(e) for e in events) + "\nnot json\n", encoding="utf-8"
    )
    assert ni.report_rows(str(trace)) == ["location: `x:1`"]


def test_only_a_directory_the_eval_kept_is_removed():
    """Guards the runner's cleanup: it removes a kept run's own directory and
    nothing a trace path could name elsewhere."""
    assert ni.kept_root("/tmp/e-Ab12cD/out/trace.jsonl") == "/tmp/e-Ab12cD"
    assert ni.kept_root("/tmp/claude-eval-x1/out/trace.jsonl") == "/tmp/claude-eval-x1"
    assert ni.kept_root("/Users/x/project/out/trace.jsonl") is None
    assert ni.kept_root("/tmp/e-Ab12cD/trace.jsonl") is None


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
def test_a_side_runs_the_tree_it_measures_and_no_installed_plugin(
    monkeypatch, flavour, pathsep, tree, base, want
):
    """Guards which plugin a side's sessions run: the measured tree's `bin/`
    first, and no installed plugin's `bin/` at all, in each platform's own
    PATH spelling whichever platform runs the case. A filter spelt with `/`
    alone keeps a Windows entry under `\\.claude\\plugins\\cache\\`, so a
    Windows side would run the installed plugin; the POSIX case alone, run
    on Windows, split nothing and dropped the whole PATH."""
    os_like = types.SimpleNamespace(sep=flavour.sep, pathsep=pathsep, path=flavour)
    monkeypatch.setattr(ni, "os", os_like)
    assert ni.side_path(tree, base).split(pathsep) == want


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


LABELLED_ROUND_1 = """# i — review round 1

target: 1a2b3c4 against main

## Findings

### 1. a fixed defect

severity: must
location: `src/a.py:12`, `docs/a.md`
verdict: fixed abc1234

why it matters.

answer: fixed

### 2. a finding that does not hold

severity: should
location: `src/b.py:3`
verdict: rejected

answer: it holds

## Confirmations

confirms: none
a claim of the frame that matched.
"""

LABELLED_ROUND_2 = """# i — review round 2

target: 2b3c4d5, fixes 1a2b3c4..2b3c4d5

## Findings

## Confirmations

confirms: round-1#1
holds.

confirms: round-1#2
holds.

confirms: round-3#1
another round's.
"""


def test_a_truth_of_a_labelled_record_is_a_fixed_finding_the_next_round_confirms():
    """Guards the replay set's ground truth on 0.22.0's record: a finding is
    a `### <n>. ` section read through `chain_check.py`'s own reader, with
    its `location:` value whole and whether its `verdict:` is `fixed`, and
    the next round confirms it on a `confirms: round-<N>#<n>` line. The
    table case above reads only the old rows, so without this one a reader
    that found no finding in any labelled record, which is what the
    generator did before #964, left every 0.22.0 round out unnoticed."""
    rt = load_script("replay_targets")
    rel = "seal/specs/i/rounds/round-1.md"
    assert rt.labelled(LABELLED_ROUND_1)
    assert not rt.labelled("| 🟢 | round 1's finding 2 is closed | `a:1` | confirmed |")
    read, why = rt.labelled_round(LABELLED_ROUND_1, rel, 1)
    assert why == ""
    assert read["sha"] == "1a2b3c4"
    assert read["value"] == "1a2b3c4 against main"
    assert read["findings"] == [
        (1, "a fixed defect", "`src/a.py:12`, `docs/a.md`", True),
        (2, "a finding that does not hold", "`src/b.py:3`", False),
    ]
    assert rt.confirmed(LABELLED_ROUND_2, 1) == {1, 2}
    assert rt.confirmed(LABELLED_ROUND_2, 2) == set()


def test_a_labelled_record_the_check_refuses_gives_no_truth():
    """Guards that a replay reads only what a pull request accepted: a
    record `chain_check.py` refuses is left out naming the refusal, and a
    next record it refuses confirms nothing, so a grader is never built on
    a line the check would not read. Nothing else holds the generator to
    the check's refusals, which is the class #923 found leaking three
    times."""
    rt = load_script("replay_targets")
    rel = "seal/specs/i/rounds/round-1.md"
    bad = LABELLED_ROUND_1.replace("fixed abc1234", "fixed abc1234 and more")
    read, why = rt.labelled_round(bad, rel, 1)
    assert read is None
    assert why.startswith("the check refuses the record at line 11: ")
    assert "reads `verdict: fixed abc1234 and more`" in why
    worse = LABELLED_ROUND_2.replace("round-1#1\n", "round-1#1 and more\n")
    assert rt.confirmed(worse, 1) == set()


def test_a_labelled_target_names_its_base(monkeypatch):
    """Guards where a labelled replay's clone starts: a fix range's first
    commit, an `against <sha>` commit, or the merge-base with
    `origin/<base>` for `against <base>`, and no base where none resolves,
    which leaves the round out rather than cloning the wrong range. The old
    reader found a base only in an asked paragraph, which 0.22.0's record
    does not carry."""
    rt = load_script("replay_targets")
    known = {"1a2b3c4": "1" * 40, "ce448bbe": "c" * 40, "origin/main": "d" * 40}
    monkeypatch.setattr(rt, "resolve", lambda rev: known.get(rev, ""))
    monkeypatch.setattr(
        rt,
        "git",
        lambda *a, **_k: "m" * 40 + "\n" if a[:2] == ("merge-base", "T") else "",
    )
    fixes = rt.target_base("2b3c4d5, fixes 1a2b3c4..2b3c4d5", "T")
    assert fixes == ("1" * 40, None)
    assert rt.target_base("2b3c4d5 against ce448bbe", "T") == ("c" * 40, None)
    assert rt.target_base("2b3c4d5 against main", "T") == ("m" * 40, "origin/main")
    assert rt.target_base("2b3c4d5 against gone", "T") == ("", None)


def test_records_read_only_the_named_items(monkeypatch, tmp_path):
    """Guards `--case`'s reach over every release tag: only the named work
    items' records are read, so reading all tags costs one listing a tag and
    a `git show` per named record, never one per record in the history."""
    rt = load_script("replay_targets")
    shown = []

    def git(*args, check=True):
        if args[0] == "ls-tree":
            return (
                "seal/specs/1791-a/rounds/round-1.md\n"
                "seal/specs/1792-b/rounds/round-1.md\n"
            )
        shown.append(args[1])
        return f"text of {args[1]}"

    monkeypatch.setattr(rt, "ROOT", str(tmp_path))
    monkeypatch.setattr(rt, "git", git)
    found = rt.records(["v1.0.0"], {"1791"})
    assert found == {
        ("1791-a", 1): "text of v1.0.0:seal/specs/1791-a/rounds/round-1.md"
    }
    assert shown == ["v1.0.0:seal/specs/1791-a/rounds/round-1.md"]


@pytest.mark.parametrize(
    ("script", "name", "items"),
    [
        ("replay_targets", "replay-1791382684-r2", {"1791382684"}),
        ("seed_defects", "seeded-279a580b", {"279a580b"}),
    ],
)
def test_a_named_case_is_read_at_every_release_tag(monkeypatch, script, name, items):
    """Guards that a committed case regenerates after the release that moved
    its records or commits out of the window `--list` reads: `--case` reads
    every release tag, for the named items alone. Before #964 both
    generators read the last two or three tags, and none of the eight
    committed replay and seeded cases was still on either list once 0.22.0
    was tagged, so `--case` exited 1 for each."""
    module = load_script(script)
    rt = module if script == "replay_targets" else module.rt
    calls = []
    monkeypatch.setattr(rt, "last_tags", lambda count=2: calls.append(count) or [])
    monkeypatch.setattr(
        module, "targets", lambda tags, only=None: calls.append(only) or ([], [])
    )
    monkeypatch.setattr(rt, "origin_url", lambda: "https://example.com/x/y.git")
    assert module.main(["--case", name]) == 1
    assert calls == [None, items]
    calls.clear()
    assert module.main(["--list"]) == 0
    assert calls[1] is None and calls[0] in (2, 3)


def test_a_seeded_case_is_looked_for_among_the_named_commits_alone(monkeypatch):
    """Guards what reading every release tag costs the seeded generator: a
    shipped commit `--case` does not name is skipped before any git call
    for it, so the whole history is listed and only the named commits are
    read. The wiring case above stubs `targets`, so only this one reaches
    the filter."""
    sd = load_script("seed_defects")
    monkeypatch.setattr(sd, "shipped", lambda _tags: ["aaaaaaaa1111", "bbbbbbbb2222"])
    monkeypatch.setattr(sd.rt, "git", lambda *_a, **_k: "")
    kept, left = sd.targets(["v1.0.0"], {"aaaaaaaa"})
    assert kept == []
    assert left == [("aaaaaaaa1111", "not a squashed pull request")]
    assert len(sd.targets(["v1.0.0"])[1]) == 2


def test_a_record_with_no_asked_paragraph_ends_the_spawn_at_the_report():
    """Guards the replay prompt of a labelled record, which carries no asked
    paragraph: the spawn ends at the report's path with nothing after it,
    and a table record's paragraph still follows that sentence after one
    space, as the four committed cases were written."""
    rt = load_script("replay_targets")
    t = {
        "item": "1-i",
        "n": 2,
        "branch": "b",
        "target": "t" * 40,
        "base": "a" * 40,
        "base_ref": None,
        "asked": "",
    }
    assert "and return its path.\n\nEND PROMPT" in rt.prompt(t)
    t["asked"] = "Round 2,\n  the verifying round."
    assert "and return its path. Round 2, the verifying round.\n\nEND" in rt.prompt(t)


def test_a_truth_pattern_holds_its_line_window_and_no_further():
    rt = load_script("replay_targets")
    """A truth reads a finding's `location:` line, the line within ±15 of
    the original's, and never a confirmation's or a table's coordinate."""
    pattern = re.compile(rt.truth_pattern("`docs/x.md:100`", "HEAD"), re.M)
    assert pattern.search("location: `docs/x.md:115`")
    assert pattern.search("location: `a.py:1`, `docs/x.md:85-90`")
    assert not pattern.search("location: `docs/x.md:116`")
    assert not pattern.search("location: `docs/x.md:1000`")
    assert not pattern.search("holds, at `docs/x.md:100`. read.")
    assert not pattern.search("| none | f | `docs/x.md:100` | g |")
    assert not pattern.search("Location: `docs/x.md:100`")


def test_a_truth_never_matches_a_coordinate_the_check_refuses(monkeypatch):
    """`chain_check.py` refuses a `path#unit` coordinate, so a truth that
    matched one would pass a warden for a record the pull request then
    fails. A Python truth reads its unit's lines within ±15 and never the
    unit's name after a `#`, and a truth with no lines reads the bare path
    or `path:<line>`, never `path#<anything>`."""
    rt = load_script("replay_targets")
    source = "x = 0\n\n\ndef f(a):\n    return a\n"
    monkeypatch.setattr(rt, "git", lambda *_a, **_k: source)
    for location in ("`a.py:5`", "`a.py#f`"):
        pattern = re.compile(rt.truth_pattern(location, "HEAD"), re.M)
        assert pattern.search("location: `a.py:5`"), location
        assert pattern.search("location: `b.md:1`, `a.py:4-5`"), location
        assert not pattern.search("location: `a.py:40`"), location
        assert not pattern.search("location: `a.py#f`"), location
        assert not pattern.search("location: `a.py#f:5`"), location
    bare = re.compile(rt.truth_pattern("`docs/x.md#unit`", "HEAD"), re.M)
    assert bare.search("location: `docs/x.md`")
    assert bare.search("location: `docs/x.md:7`")
    assert not bare.search("location: `docs/x.md#unit`")


def test_a_seed_lands_on_a_code_token_and_never_in_a_string():
    sd = load_script("seed_defects")
    source = 'def f(a):\n    """a == b"""\n    return a == 1\n'
    tokens = sd.code_tokens(source)
    assert (3, "==") in tokens
    assert (2, "==") not in tokens
