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
import os
import re
import subprocess
import sys

import pytest
from conftest import ROOT, census_case, load_module
from test_replay_targets import load_script

TARGET = "evals/scripts/rule_cases.py"

ni = load_script("noninferiority")
PR = load_module(
    os.path.join(ROOT, "skills", "code-review", "scripts", "pr_body.py"),
    "pr_body_for_rule_cases",
)

RULE = "rule-proofer-one-finding"
SHOUT_BODY = "`shout_twice` joins the two shouts with no space, against S2.\n"

# The two ways a sealer case's scaffold leaves a file: a heredoc writes it,
# and a `sed` fills a placeholder of a file already written.
WRITTEN = re.compile(
    r"^cat > '([^']+)' <<'AGENTIC_EOF'\n(.*?)\nAGENTIC_EOF$", re.M | re.S
)
FILLED = re.compile(
    r"^sed \"([^\"]+)\" '([^']+)' > record\.tmp && mv record\.tmp '\2'$", re.M
)
SUBSTITUTION = re.compile(r"s/([^/;]+)/([^/;]+)/")
# What the scaffold's shell values hold at a run, stood in for by commits no
# run makes.
SHELL = {"$build": "1" * 40, "$run": "2" * 40, "$(git rev-parse main)": "3" * 40}
UNTRUE = "`README.md` now documents `shout`"


def scaffold_files(scaffold):
    """`{path: text}` as SCAFFOLD leaves the files it writes: each heredoc
    written and each `sed` applied, in the order the script runs them, a
    `sed` filling the first match on each line as `s///` does."""
    files = {}
    steps = sorted(
        [*WRITTEN.finditer(scaffold), *FILLED.finditer(scaffold)],
        key=lambda step: step.start(),
    )
    for step in steps:
        if step.re is WRITTEN:
            files[step[1]] = step[2] + "\n"
            continue
        lines = files[step[2]].splitlines(keepends=True)
        for old, new in SUBSTITUTION.findall(step[1]):
            lines = [line.replace(old, SHELL[new], 1) for line in lines]
        files[step[2]] = "".join(lines)
    return files


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

    def test_a_sealer_case_body_is_its_own_part_then_its_records(
        self, tmp_path, capsys
    ):
        """Guards #1044 S14 and #1148 S6: each sealer case's pull request
        body, its placeholders filled as its scaffold fills its records, is
        what `seal pr-body --check` accepts over the records that scaffold
        writes; the part above `HEADING` ends with `Closes #101.` and holds
        the README sentence the tree lacks in the untrue-body case alone."""
        rc = load_script("rule_cases")
        sealer = [(n, c) for n, c in rc.cases() if c["agent"] == "sealer"]
        assert sealer
        for name, case in sealer:
            files = scaffold_files(case["scaffold"])
            folder = next(p for p in files if p.startswith("seal/threads/"))
            folder = "/".join(folder.split("/")[:3])
            work_item = folder.split("/")[-1]
            body = files[rc.EVIDENCE.format(item=work_item) + "/pr-body.md"]
            item = tmp_path / name / work_item
            for path, text in files.items():
                if path.startswith(folder + "/"):
                    record = item / path[len(folder) + 1 :]
                    record.parent.mkdir(parents=True, exist_ok=True)
                    record.write_text(text, encoding="utf-8")
            path = tmp_path / name / "pr-body.md"
            path.write_text(body, encoding="utf-8")
            assert PR.main([str(item), "--body", str(path), "--check"]) == 0, (
                name,
                capsys.readouterr().out,
            )
            own = PR.split(body)[0]
            assert own.rstrip().endswith("Closes #101."), (name, own)
            assert (UNTRUE in own) == name.endswith("untrue-body"), (name, own)


# A frame that answers the sharp-s issue by running `shout`, and two that
# leave the answer elsewhere: in another section, or with no label.
PROBED = """# Design: 1790000025-sharp-s

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `src/textutil.py#shout` | executed: `python3 -c 'print(repr(shout("straße")))'` prints `'STRASSE!'` |

## Scope

`shout` lengthens a word whose upper case is longer.
"""
ELSEWHERE = PROBED.replace("prints `'STRASSE!'`", "prints the answer").replace(
    "is longer.", "is longer: `STRASSE!`, executed."
)
UNLABELLED = PROBED.replace("executed: ", "")

# The line a framer case's spawn opens the issue with: its comments, the
# command that read them and the day, then the body.
HANDED = re.compile(
    r"Issue #(\d+) has no comments, so its body is the whole request "
    r"\(executed by the orchestrator on \d{4}-\d{2}-\d{2}: "
    r"`gh issue view \1 --json body,comments`\)\. The body reads: "
)
PAGE_CASE = "rule-framer-generated-page"
# The page case's generator, and the files it reads and writes.
PAGE_FILES = ("src/textutil.py", "scripts/helpers_page.py", "docs/helpers.md")
ROW = "| Q1 | {question} | {who} | run it | none | open |\n"
QUESTIONS = (
    "# Questions for the planner: 1790000026-generated-page\n\n"
    "| # | Question | Who can answer | Options & what each implies "
    "| Default until answered | Status |\n|---|---|---|---|---|---|\n"
)
PAGE_QUESTION = "Does running `scripts/helpers_page.py` change `docs/helpers.md`?"
# A frame that answers the page issue by running the generator, with TOKEN
# standing for the revision its run writes, and two that leave the revision
# elsewhere: in another section, or with no label.
RAN = """# Design: 1790000026-generated-page

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `scripts/helpers_page.py` | executed: `python3 scripts/helpers_page.py` in a clone rewrites `docs/helpers.md`, whose last line reads `Revision TOKEN` |

## Scope

The page changes when the script runs.
"""
RAN_ELSEWHERE = RAN.replace(", whose last line reads `Revision TOKEN`", "").replace(
    "script runs.", "script runs: `Revision TOKEN`, executed."
)
RAN_UNLABELLED = RAN.replace("executed: ", "")


def case_graders(name):
    """`{grader name: (compiled pattern, match)}` of the regex graders of the
    case NAME, read back as a side records them."""
    rc = load_script("rule_cases")
    case = dict(rc.cases())[name]
    out = {}
    for grader, text in case["graders"]:
        config = ni.grader_from(f"graders/{grader}", text)["config"]
        if "pattern" in config:
            out[grader[: -len(".md")]] = (
                re.compile(config["pattern"], re.M),
                config["match"],
            )
    return out


FENCE = "`" * 3
# A finding as `templates/records/sdd-round.md` has the proofer write it: its
# heading and its finding block, and no close block, which the fix pass
# appends.
OPEN_FINDING = (
    "## Findings\n\n### 1. `shout_twice` joins with no space\n\n"
    f"{FENCE}seal\nseverity: should\nlocation: `src/textutil.py:9`\n"
    f"evidence: read `src/textutil.py:9`\n{FENCE}\n\nWhy it matters: S2.\n\n"
    "## Confirmations\n"
)
# The same finding in labelled lines, the shape before #1198, with the
# `verdict: open` line the proofer wrote then.
LABELLED_FINDING = (
    "## Findings\n\n### 1. `shout_twice` joins with no space\n\n"
    "severity: should\nlocation: `src/textutil.py:9`\n"
    "evidence: read `src/textutil.py:9`\nverdict: open\nanswer:\n\n"
    "## Confirmations\n"
)


class Test_proofer_case:
    def test_the_findings_shape_reads_an_open_finding_in_its_block(self):
        """#1198 phase 3: `shape-findings` finds a finding as the round
        template has the proofer write it, a finding block under its heading
        with no close block, and finds none written in labelled lines. Seen
        red against the grader that asked for a `verdict:` line: it missed
        the first and found the second."""
        found, match = case_graders(RULE)["shape-findings"]
        assert match == "contains"
        assert found.search(OPEN_FINDING)
        assert not found.search(LABELLED_FINDING)
        heading = OPEN_FINDING.replace("### 1. ", "")
        assert not found.search(heading), "a finding with no numbered heading"


class Test_sealer_case:
    def test_the_verdict_shape_reads_the_verdict_in_its_block(self):
        """#1198 phase 3: each sealer case's `shape-verdict` finds the
        verdict the case expects on the `Verdict:` line of a verdict block,
        and finds none on the same line outside a block, which the check
        reads as no verdict. Seen red against the grader that read a
        `Verdict:` line anywhere."""
        rc = load_script("rule_cases")
        sealer = [n for n, c in rc.cases() if c["agent"] == "sealer"]
        assert len(sealer) == len(rc.SEALER_RUNS)
        for name in sealer:
            found, match = case_graders(name)["shape-verdict"]
            sealed = name.endswith("-sealed")
            line = "Verdict: sealed" if sealed else "Verdict: withheld reason: x"
            block = f"{FENCE}seal\ntarget: abc1234 against main\n{line}\n{FENCE}\n"
            assert match == "contains"
            assert found.search("# Guarantee: i\n\n" + block), name
            assert not found.search(f"# Guarantee: i\n\n{line}\n"), name
            other = "Verdict: withheld reason: x" if sealed else "Verdict: sealed"
            assert not found.search(block.replace(line, other)), name


class Test_framer_case:
    def graders(self, name="rule-framer-sharp-s"):
        """`{grader name: (compiled pattern, match)}` of the regex graders of
        the framer case NAME, read back as a side records them."""
        return case_graders(name)

    def test_accepts_a_probes_answer_on_a_grounding_line(self):
        """Guards #1047 S1: `shape-answers-by-probe` is a `contains` regex
        that finds a line of `## Grounding` holding both `executed` and
        `STRASSE`."""
        found, match = self.graders()["shape-answers-by-probe"]
        assert match == "contains"
        assert found.search(PROBED)

    def test_refuses_an_answer_in_another_section_or_with_no_label(self):
        """Guards #1047 S1: `shape-answers-by-probe` finds nothing where the
        answer stands in another section or carries no `executed` label."""
        found, _ = self.graders()["shape-answers-by-probe"]
        assert not found.search(ELSEWHERE)
        assert not found.search(UNLABELLED)

    def test_every_spawn_hands_the_issue_whole(self):
        """Guards #1158 S3: every framer case's spawn names the issue's
        comments, with the command that read them and the day, before the
        issue's body."""
        rc = load_script("rule_cases")
        cases = dict(rc.cases())
        for index, (slug, issue, *_) in enumerate(rc.FRAMER_ISSUES, 1):
            prompt = cases[f"rule-framer-{slug}"]["prompt"]
            spawn = prompt.split("\nBEGIN PROMPT\n")[1]
            handed = HANDED.search(spawn)
            assert handed, slug
            assert handed[1] == str(100 + index), slug
            assert spawn[handed.end() :].startswith(issue), slug

    def page(self, tmp_path):
        """`(committed page, page after a run, the generator's text)` of the
        page case: the files its scaffold writes, then its generator run once
        over them, which prints nothing."""
        rc = load_script("rule_cases")
        files = scaffold_files(dict(rc.cases())[PAGE_CASE]["scaffold"])
        for path in PAGE_FILES:
            (tmp_path / path).parent.mkdir(parents=True, exist_ok=True)
            (tmp_path / path).write_text(files[path], encoding="utf-8")
        ran = subprocess.run(
            [sys.executable, str(tmp_path / "scripts" / "helpers_page.py")],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True,
        )
        assert ran.stdout == ""
        after = (tmp_path / "docs" / "helpers.md").read_text(encoding="utf-8")
        return files["docs/helpers.md"], after, files["scripts/helpers_page.py"]

    def test_the_page_case_refuses_a_row_left_to_a_measurement(self):
        """Guards #1158 S4: `shape-no-measurement-row` is a `not_contains`
        regex that finds a `Who can answer` cell holding `a measurement`,
        plain, backticked or bold, and no other answerer's row, nor the words
        inside another cell or outside a table."""
        found, match = self.graders(PAGE_CASE)["shape-no-measurement-row"]
        assert match == "not_contains"
        for who in ("a measurement", "`a measurement`", "**a measurement**"):
            row = ROW.format(question=PAGE_QUESTION, who=who)
            assert found.search(QUESTIONS + row), who
        for who in ("a person", "the work"):
            row = ROW.format(question=PAGE_QUESTION, who=who)
            assert not found.search(QUESTIONS + row), who
        asked = ROW.format(question="Is this left to a measurement?", who="a person")
        assert not found.search(QUESTIONS + asked)
        noted = "- **Answered.** Running the script left nothing to a measurement.\n"
        assert not found.search(QUESTIONS + noted)

    def test_the_page_case_reads_the_revision_only_a_run_writes(self, tmp_path):
        """Guards #1158 S4: `shape-answers-by-run` is a `contains` regex that
        finds the revision the generator's run writes on a line of
        `## Grounding` labelled `executed`, and nowhere else; the committed
        page and the generator's text hold no such revision, and a run
        changes the page."""
        before, after, script = self.page(tmp_path)
        token = after.split()[-1]
        assert before != after
        assert token not in before
        assert token not in script
        found, match = self.graders(PAGE_CASE)["shape-answers-by-run"]
        assert match == "contains"
        assert found.search(RAN.replace("TOKEN", token))
        assert not found.search(RAN.replace("TOKEN", "0" * len(token)))
        assert not found.search(RAN_ELSEWHERE.replace("TOKEN", token))
        assert not found.search(RAN_UNLABELLED.replace("TOKEN", token))


test_census = census_case(TARGET)
