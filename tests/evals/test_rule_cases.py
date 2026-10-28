"""`evals/scripts/rule_cases.py`, one class per function.

The rule generator writes the behaviour suite's rule cases, and a recurred
truth entry adds a `truth-` grader to the case it names, widens one it
already has, or stops the generator where the case cannot take it. A
generated truth is read back through `noninferiority.py#grader_from`, the
one reader of a grader file.

#942's phase 6 placed these cases from
`tests/behaviour/test_a_rewritten_definition_proved_non_inferior.py`, which keeps
the case that reads the committed proofer cases.
"""

import json
import re

import pytest
from conftest import census_case
from test_replay_targets import load_script

TARGET = "evals/scripts/rule_cases.py"

ni = load_script("noninferiority")

RULE = "rule-proofer-one-finding"
SHOUT_BODY = "`shout_twice` joins the two shouts with no space, against S2.\n"


def recurred_file(tmp_path, *entries):
    """The input file of added truths holding ENTRIES, and its path."""
    path = tmp_path / "recurred_truths.json"
    path.write_text(json.dumps(list(entries)), encoding="utf-8")
    return str(path)


def entry(**over):
    """One entry of the input file: a new truth of the rule case, unless
    OVER says otherwise."""
    base = {
        "case": RULE,
        "grader": "truth-no-case",
        "finding": "No case covers `shout_twice`.",
        "locations": ["tests/test_textutil.py"],
        "from": ["baseline rule-proofer-one-finding 0 1"],
    }
    base.update(over)
    return base


def rule_truths(tmp_path, monkeypatch, *entries):
    """`{file name: text}` of the truth graders `rule_cases.py` writes for
    the proofer's rule case with ENTRIES as its input file."""
    rc = load_script("rule_cases")
    monkeypatch.setattr(rc.rt, "TRUTHS", recurred_file(tmp_path, *entries))
    out = tmp_path / "out"
    assert rc.main(["--out", str(out)]) == 0
    graders = out / "proofer" / RULE / "graders"
    return {p.name: p.read_text(encoding="utf-8") for p in graders.glob("truth-*.md")}


def truth_regex(name, text):
    return re.compile(
        ni.grader_from(f"graders/{name}", text)["config"]["pattern"], re.M
    )


class Test_main:
    def test_accepts_an_entry_and_adds_the_truth_its_case_is_written_with(
        self, tmp_path, monkeypatch
    ):
        """Guards S6's added truth: an entry naming a new grader writes it beside
        the case's own truths, its body the entry's finding and its pattern
        `truth_pattern`'s for each location."""
        truths = rule_truths(tmp_path, monkeypatch, entry())
        assert sorted(truths) == ["truth-no-case.md", "truth-shout-twice.md"]
        text = truths["truth-no-case.md"]
        assert text.endswith("No case covers `shout_twice`.\n")
        found = truth_regex("truth-no-case.md", text)
        assert found.search("location: `tests/test_textutil.py`")
        assert not found.search("location: `src/textutil.py:8`")
        assert truths["truth-shout-twice.md"].endswith(SHOUT_BODY)

    def test_an_entry_widens_a_truth_and_keeps_what_it_found(
        self, tmp_path, monkeypatch
    ):
        """Guards S6's widened truth: an entry that widens a grader adds its
        locations as alternatives, the grader still finds what it found, and its
        body stays the defect it was written for."""
        widen = entry(grader="truth-shout-twice", widens=True)
        truths = rule_truths(tmp_path, monkeypatch, widen)
        assert sorted(truths) == ["truth-shout-twice.md"]
        text = truths["truth-shout-twice.md"]
        assert text.endswith(SHOUT_BODY)
        found = truth_regex("truth-shout-twice.md", text)
        assert found.search("location: `src/textutil.py:8`")
        assert found.search("location: tests/test_textutil.py")
        assert not found.search("location: `src/other.py:8`")

    @pytest.mark.parametrize(
        "over, named",
        [
            ({"case": "replay-0-r1"}, "replay-0-r1"),
            ({"grader": "truth-9", "widens": True}, "truth-9"),
            ({"grader": "truth-shout-twice"}, "truth-shout-twice"),
            ({"locations": ["src/textutil.py#shout"]}, "src/textutil.py#shout"),
            ({"locations": ["no path here"]}, "no path here"),
            ({"locations": []}, "names no location"),
            ({"window": "2"}, "is no count"),
            ({"locations": ["src/x.py:100-10"]}, "src/x.py:100-10"),
        ],
        ids=[
            "a-case-no-generator-writes",
            "a-widening-of-a-truth-the-case-lacks",
            "a-new-truth-the-case-already-has",
            "a-coordinate-the-grammar-refuses",
            "no-coordinate",
            "no-location",
            "a-window-that-is-no-count",
            "a-range-that-ends-before-it-starts",
        ],
    )
    def test_refuses_an_entry_the_case_cannot_take(
        self, tmp_path, monkeypatch, over, named
    ):
        """Guards S6's stale entry: an entry naming a case the suite does not
        hold, a truth to widen that the case lacks, a new truth whose name the
        case already has, a location outside `path`, `path:line` and
        `path:first-last`, or no location at all, which would be a truth every
        row matches, stops the generator with exit 1, naming it, so the file
        cannot go stale silently."""
        with pytest.raises(SystemExit) as stopped:
            rule_truths(tmp_path, monkeypatch, entry(**over))
        assert named in str(stopped.value.code)

    def test_an_entry_range_is_read_to_its_last_line(self, tmp_path, monkeypatch):
        """Guards #971 round 1 finding 2: a `path:first-last` location credits a
        row anywhere in the range, its last line too, and nothing past the
        window after it."""
        truths = rule_truths(
            tmp_path, monkeypatch, entry(locations=["src/x.py:10-100"])
        )
        found = truth_regex("truth-no-case.md", truths["truth-no-case.md"])
        assert found.search("location: `src/x.py:60`")
        assert found.search("location: `src/x.py:115`")
        assert not found.search("location: `src/x.py:116`")

    def test_an_entry_window_narrows_the_lines_its_truth_accepts(
        self, tmp_path, monkeypatch
    ):
        """Guards #971 round 1 finding 1's repair: an entry's `window` replaces
        the ±15 lines around each of its locations, for a line and for a range."""
        narrow = entry(locations=["src/x.py:10", "src/y.py:20-22"], window=2)
        truths = rule_truths(tmp_path, monkeypatch, narrow)
        found = truth_regex("truth-no-case.md", truths["truth-no-case.md"])
        for line in ("src/x.py:8", "src/x.py:12", "src/y.py:18", "src/y.py:24"):
            assert found.search(f"location: `{line}`"), line
        for line in ("src/x.py:7", "src/x.py:13", "src/y.py:17", "src/y.py:25"):
            assert not found.search(f"location: `{line}`"), line


test_census = census_case(TARGET)
