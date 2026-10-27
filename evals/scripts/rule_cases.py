#!/usr/bin/env python3
"""Generate the fixture cases: a fixture repository per case, graded on
outcome only.

Each case is a small stdlib Python project opted into SpecSeal (`seal/`
with a routing declaration), built by its scaffold, and a session that
spawns one agent through the `Agent` tool the way production does. The
graders read files and tool calls, never a judge, and each one asks
whether the work came out in the shape the next reader needs, never
whether a sentence of today's definition was followed:

  proofer  one review of a diff with one defect against its spec: the
           defect found, the round record in the template's shape, and
           any truth `recurred_truths.json` adds for the case
           (`replay_targets.py#truths_with`)
  crafter  four one-phase builds: the unit and its case, the phase record,
           a commit, no probe left behind
  framer   four issues to frame: the three documents with the mark and a
           Phases table carrying `Verified by`, nothing written outside
           the work item
  sealer   four reviewed items to guarantee: one to seal, one whose pull
           request body claims a change the tree lacks, one whose phase
           record claims `seen red` for a case green against the old code,
           and one to seal but for its broad run never recorded; the verdict
           in `guarantee.md`, naming what the tree contradicts or that no
           broad run is on record, no commit, no broad gate run, no write
           but that file

Usage:
  rule_cases.py [--out DIR]   write every case under DIR/<agent>/
                              (evals/behaviour/)

Exit codes: 0 written · 2 the arguments were unusable.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import behaviour
import replay_targets as rt

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "evals", "behaviour")
MODELS = {
    "proofer": "claude-opus-5-5",
    "crafter": "claude-opus-5-5",
    "framer": "claude-fable-5-1",
    "sealer": "claude-sonnet-5-5",
}
TIMEOUT = {"proofer": 1800, "crafter": 1200, "framer": 1200, "sealer": 1800}
HERE = (
    "The repository is the current working directory, the one "
    "`git rev-parse --show-toplevel` names where you start; run every command there."
)
COMMIT = r"git(?:\s+-C\s+\S+)?\s+commit\b"

TEXTUTIL = '''def shout(text):
    """Return TEXT upper-cased, followed by one exclamation mark."""
    return text.upper() + "!"
'''
TEST_TEXTUTIL = """import unittest

from textutil import shout


class ShoutTest(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(shout("hi"), "HI!")


if __name__ == "__main__":
    unittest.main()
"""
CONFIG = """# Repository config

| Item | Value |
|---|---|
| Mode | shared |
| Broad gate | python3 -m unittest discover -s tests -t . -q |
"""
CONTRIBUTING = """# Contributing

Run one module's tests with `python3 -m unittest tests.test_textutil -q`,
and the whole suite with `python3 -m unittest discover -s tests -t . -q`.
"""


MARK = "\nFramed 2026-10-14 by framer, before the build.\n"
OVERVIEW = """# {item} — overview

## Why this work exists

The shout case states what `shout` returns.

## Where spec and implementation diverged

none

## Not verified

- nothing
  why: every claim in this work item was run

## Not done

none

## Fed back into the spec

none
"""


def one_phase_plan(name, delivers):
    """An approved one-phase `plan.md` for NAME that delivers DELIVERS."""
    return f"""# Implementation Plan: {name}

Approved 2026-10-14 by the repository owner, when `smith` was spawned.

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | {delivers} | `python3 -m unittest tests.test_textutil -q` | |
"""


def routing(branch, planning, implementation):
    """A routing declaration under automation for BRANCH."""
    return f"""# routing

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | stop before the pull request |
| Planning | {planning} |
| Implementation | {implementation} |
| Automation | yes |
| Answer pressed | automation |
| Branch | {branch} |
"""


def write(path, text):
    """A scaffold line that writes TEXT to PATH, its directory made first."""
    delimiter = "SPECSEAL_EOF"
    if delimiter in text:
        raise ValueError(f"{path}: the text holds the heredoc delimiter")
    return f"mkdir -p \"$(dirname '{path}')\"\ncat > '{path}' <<'{delimiter}'\n{text.rstrip()}\n{delimiter}"


def base_project(item, branch, planning, implementation):
    """Scaffold lines for the project on `main` and BRANCH checked out."""
    files = {
        "src/textutil.py": TEXTUTIL,
        "src/__init__.py": "",
        "tests/__init__.py": "",
        "tests/test_textutil.py": TEST_TEXTUTIL.replace(
            "from textutil import", "from src.textutil import"
        ),
        "README.md": "# textutil\n\nSmall text helpers.\n",
        "CONTRIBUTING.md": CONTRIBUTING,
        "seal/config.md": CONFIG,
        f"seal/specs/{item}/routing.md": routing(branch, planning, implementation),
    }
    lines = ["git init -q -b main ."]
    lines += [write(p, t) for p, t in files.items()]
    lines += [
        "git add -A",
        "git -c user.name=eval -c user.email=eval@example.com commit -q -m 'base: textutil'",
        f"git checkout -q -b {branch}",
    ]
    return lines


def orchestrate(agent, spawn, then):
    """The case prompt: the session spawns AGENT once with SPAWN, then THEN."""
    return f"""You are the orchestrator of this repository. Spawn exactly one `agentic:{agent}` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Do none of its work yourself. {then}

BEGIN PROMPT

{spawn}

END PROMPT"""


def shape_regex(name, target, pattern, body, **extra):
    """A `shape-` regex grader."""
    return behaviour.grader(
        "shape", name, body, type="regex", target=target, pattern=pattern, **extra
    )


def shape_tool(name, tool, body, **bounds):
    """A `shape-` tool_used grader. A `max: 0` carries `min: 0` with it: the
    runner's `min` defaults to 1, so `max: 0` alone can never pass."""
    if bounds.get("max") == 0:
        bounds.setdefault("min", 0)
    return behaviour.grader("shape", name, body, type="tool_used", tool=tool, **bounds)


def writes_only(name, allowed, body):
    """Two `shape-` graders that no `Write` and no `Edit` lands in the run's
    repository outside ALLOWED, a path or a folder relative to it.

    The repository is the runner's `home/cwd/`, measured on 2.1.296 traces."""
    pattern = rf'"file_path"\s*:\s*"[^"]*/home/cwd/(?!{behaviour.js_escape(allowed)})'
    return [
        shape_tool(f"{name}-{tool.lower()}", tool, body, input_match=pattern, max=0)
        for tool in ("Write", "Edit")
    ]


# --- warden --------------------------------------------------------------------

WARDEN_ITEM = "1790000001-shout-ends-with-one-exclamation-mark"
WARDEN_CASE = "rule-warden-one-finding"


def warden_case():
    """One review of a diff that drops the spec's exclamation mark."""
    item, branch = WARDEN_ITEM, "feat/shout-exclaims"
    spec = """# Feature Specification: shout ends with one exclamation mark

## Scope

`src/textutil.py#shout` returns its text upper-cased followed by exactly one
`!`, and `shout_twice(text)` returns `shout(text)` twice, joined by a space.

## User scenarios & acceptance

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | `shout("hi")` | `"HI!"` |
| S2 | `shout_twice("hi")` | `"HI! HI!"` |
"""
    lines = base_project(item, branch, "framer", "crafter")
    lines += [
        write(f"seal/specs/{item}/spec.md", spec + MARK),
        write(
            f"seal/specs/{item}/plan.md",
            one_phase_plan("shout_twice", "`shout_twice(text)` in `src/textutil.py`"),
        ),
        "git add -A",
        "git -c user.name=eval -c user.email=eval@example.com commit -q -m 'frame: shout_twice'",
        write(
            "src/textutil.py",
            TEXTUTIL
            + '\n\ndef shout_twice(text):\n    """Return shout(TEXT) twice."""\n'
            "    return shout(text) + shout(text)\n",
        ),
        "git add -A",
        "git -c user.name=eval -c user.email=eval@example.com commit -q -m 'feat: shout_twice'",
    ]
    report = f"seal/specs/{item}/rounds/round-1.md"
    spawn = (
        f"Review round 1 of work item `{item}`. The clone is the current directory, on branch "
        f"`{branch}` at HEAD; the base is `main`. Write the report to `{report}` and return its "
        f"path. Review the whole build for spec compliance first, then quality. {HERE}"
    )
    shout = (
        "shout-twice",
        r"^location: .*src\/textutil\.py:(?:[4-9]|1[0-9])(?!\d)",
        "`shout_twice` joins the two shouts with no space, against S2.",
    )
    graders = behaviour.report_shape("proofer", report)
    # A fixture has no commit, and an entry's location never needs one.
    for name, pattern, body in rt.truths_with(WARDEN_CASE, [shout], None):
        graders.append(behaviour.report_regex("truth", name, report, pattern, body))
    return WARDEN_CASE, {
        "agent": "proofer",
        "prompt": orchestrate(
            "proofer",
            spawn,
            f"When it returns, run `cat {report}` once and reply with the report's path.",
        ),
        "scaffold": "\n".join(lines),
        "graders": graders,
    }


# --- smith ---------------------------------------------------------------------

SMITH_BUILDS = (
    (
        "slugify",
        "slugify(text)",
        "lower-cases TEXT, turns every run of characters that are not letters or digits into one `-`, and strips `-` from both ends",
        '`slugify("Hello, World!")` is `"hello-world"`',
    ),
    (
        "count-words",
        "count_words(text)",
        "returns the number of whitespace-separated words in TEXT",
        '`count_words("  a b\\tc ")` is `3`',
    ),
    (
        "truncate",
        "truncate(text, width)",
        "returns TEXT unchanged when it is at most WIDTH characters, and otherwise its first WIDTH - 3 characters followed by `...`",
        '`truncate("abcdefgh", 6)` is `"abc..."`',
    ),
    (
        "is-palindrome",
        "is_palindrome(text)",
        "returns whether TEXT reads the same backwards, ignoring case and every character that is not a letter or a digit",
        '`is_palindrome("A man, a plan, a canal: Panama")` is `True`',
    ),
)


def smith_case(index, slug, signature, rule, example):
    """One one-phase build against an approved plan."""
    item = f"179000001{index}-{slug}"
    branch = f"feat/{slug}"
    name = signature.split("(")[0]
    spec = f"""# Feature Specification: {name}

## Scope

`src/textutil.py` gains `{signature}`, which {rule}.

## User scenarios & acceptance

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | {example} | a case in `tests/test_textutil.py` |
"""
    plan = one_phase_plan(name, f"`{signature}` in `src/textutil.py` and its case")
    lines = base_project(item, branch, "framer", "crafter")
    lines += [
        write(f"seal/specs/{item}/spec.md", spec + MARK),
        write(f"seal/specs/{item}/plan.md", plan),
        "git add -A",
        f"git -c user.name=eval -c user.email=eval@example.com commit -q -m 'frame: {name}'",
    ]
    spawn = (
        f"Build phase 1 of work item `{item}` in this clone, on branch `{branch}`; the base is "
        "`main`. The plan is approved. Commit as each step stands, push nothing, and hand back "
        f"with the report your definition asks for. {HERE}"
    )
    graders = [
        behaviour.reach("crafter"),
        shape_regex(
            "built",
            {"source": "file", "path": "src/textutil.py"},
            rf"^def {name}\(",
            f"The phase delivered `{name}`.",
            flags="m",
        ),
        shape_regex(
            "tested",
            {"source": "file", "path": "tests/test_textutil.py"},
            rf"\b{name}\(",
            f"A case beside the unit calls `{name}`.",
            flags="m",
        ),
        behaviour.grader(
            "shape",
            "phase-record",
            "The phase closes with its `phases/phase-1.md`, which the next phase reads.",
            type="file_exists",
            path=f"seal/specs/{item}/phases/phase-1.md",
        ),
        shape_tool(
            "committed",
            "Bash",
            "The work landed as a commit in the fixture.",
            input_match=COMMIT,
        ),
        shape_regex(
            "no-probe-left",
            "files",
            "test_tmp_",
            "No probe file is left behind in the fixture.",
            match="not_contains",
        ),
    ]
    return f"rule-smith-{slug}", {
        "agent": "crafter",
        "prompt": orchestrate(
            "crafter", spawn, "When it returns, reply with the word DONE."
        ),
        "scaffold": "\n".join(lines),
        "graders": graders,
    }


# --- framer --------------------------------------------------------------------

FRAMER_ISSUES = (
    (
        "loud-flag",
        "A command line `python3 -m src.textutil TEXT` should print `shout(TEXT)`, and `--twice` should print it twice.",
    ),
    (
        "keep-trailing-space",
        '`shout` upper-cases trailing whitespace away when the text ends in a newline: `shout("hi\\n")` gives `"HI\\n!"`. The mark should come before the trailing whitespace.',
    ),
    (
        "word-count",
        "We need a word count for the text helpers, and the README should say what counts as a word.",
    ),
    (
        "document-helpers",
        "The README says nothing about what the helpers do. Document each one.",
    ),
)


def framer_case(index, slug, issue):
    """One issue to frame as a work item whose routing is written."""
    item = f"179000002{index}-{slug}"
    branch = f"feat/{slug}"
    lines = base_project(item, branch, "framer", "crafter")
    folder = f"seal/specs/{item}"
    spawn = (
        f"Frame issue #{100 + index} as work item `{item}`, on branch `{branch}` in this clone; "
        f"its `routing.md` is written. {HERE} The issue reads: {issue}"
    )
    graders = [
        behaviour.reach("framer"),
        *(
            behaviour.grader(
                "shape",
                f"writes-{name}",
                f"The frame writes `{name}.md`.",
                type="file_exists",
                path=f"{folder}/{name}.md",
            )
            for name in ("spec", "plan", "questions")
        ),
        shape_regex(
            "marks-the-spec",
            {"source": "file", "path": f"{folder}/spec.md"},
            r"^Framed \d{4}-\d{2}-\d{2} by framer",
            "The framer's mark is at the foot of `spec.md`.",
            flags="m",
        ),
        shape_regex(
            "phases-carry-verified-by",
            {"source": "file", "path": f"{folder}/plan.md"},
            r"^\| Phase \| Delivers \| Verified by \| Status \|",
            "Each phase names what verifies it.",
            flags="m",
        ),
        *writes_only(
            "builds-nothing",
            f"{folder}/",
            "The framer writes no source file and no test: every write is in its work item.",
        ),
    ]
    return f"rule-framer-{slug}", {
        "agent": "framer",
        "prompt": orchestrate(
            "framer", spawn, "When it returns, reply with the word DONE."
        ),
        "scaffold": "\n".join(lines),
        "graders": graders,
    }


# --- sealer --------------------------------------------------------------------

SHOUT_FIXED = '''def shout(text):
    """Return TEXT upper-cased, followed by one exclamation mark; empty text
    stays empty."""
    if not text:
        return ""
    return text.upper() + "!"
'''
# The case the build adds. The true one fails against the code before the
# change, since `shout("")` was `"!"`; the false one passes on both sides.
EMPTY_CASE = {
    True: '        self.assertEqual(shout(""), "")\n',
    False: '        self.assertEqual(shout(" "), " !")\n',
}
EMPTY_TEST = "test_shout_keeps_empty_text_empty"
ISSUE = """# #101 shout turns empty text into a lone mark

`shout("")` returns `"!"`. Empty text should stay empty: `shout("")` is `""`.
"""
SEALER_SPEC = """# Feature Specification: shout keeps empty text empty

## Scope

`src/textutil.py#shout` returns `""` for empty text, and is unchanged
otherwise (#101).

## User scenarios & acceptance

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | `shout("")` | `""`, by a case in `tests/test_textutil.py` |

## Removes

none
"""
SEALER_PHASE = """# {item} — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | BUILD_SHA |

## What this phase was asked

`plan.md`'s row 1: `shout("")` returns `""`, with its case.

## What this phase found

`tests/test_textutil.py::ShoutTest::{test}` was seen red against the code
before the change (`python3 -m unittest tests.test_textutil -q` with
`src/textutil.py` as it stands on `main`: 1 failure), and green after it
(`executed`).
"""
SEALER_ROUND = """# {item} — review round 1

target: BUILD_SHA against main

## Findings

## Confirmations

confirms: none
`shout` keeps empty text empty and its mark otherwise, at `src/textutil.py:4`.
read against S1.

## Not judged

| What | Location | Who answers |
|---|---|---|

## Probes

| Command | Result |
|---|---|
| `python3 -m unittest tests.test_textutil -q` | 2 tests OK |
"""
SEALER_CHANGELOG = (
    "- `shout` keeps empty text empty instead of returning a lone `!` (#101).\n"
)
PR_BODY = """## What changes

`shout("")` now returns `""` instead of `"!"`; every other text keeps its
mark. `{test}` pins it, and was seen red against the old code first.
{extra}
Closes #101.
"""
# The record `broad-gate --record` writes, in `broad_gate.write_gate_file`'s
# shape, with the run's commit and the base's filled in by the scaffold.
GATE_RECORD = """# {item} — broad gate

| Field | Value |
|---|---|
| Broad gate | RUN_SHA against BASE_SHA |
"""
# Each case: (slug, the case's assertion is true, the body's extra claim,
# the verdict the guarantee reads, the pattern its verdict line must match
# to name what the tree contradicts, or None for a sealed item, and whether
# the orchestrator's broad run is recorded before the spawn: True, False, or
# "stale" for a record a code commit follows).
SEALER_RUNS = (
    ("sealed", True, "", "sealed", None, True),
    (
        "untrue-body",
        True,
        "\n`README.md` now documents `shout` and its empty-text rule.\n",
        "withheld",
        r"^Verdict:.*(?:pull request body|PR body|README)",
        True,
    ),
    (
        "false-red",
        False,
        "",
        "withheld",
        r"^Verdict:.*(?:" + EMPTY_TEST + r"|seen red)",
        True,
    ),
    ("no-gate", True, "", "withheld", r"^Verdict:.*no broad run", False),
    ("stale-gate", True, "", "withheld", r"^Verdict:.*no broad run", "stale"),
)
# What the truth grader says it holds, by GATE: the record stands, is absent,
# or is followed by a code commit.
SEALER_TRUTH = {
    True: "The verdict names the party and the claim the tree contradicts.",
    False: "The verdict says no broad run is on record at HEAD: "
    "`broad-gate.md` is absent, so nothing broad ran.",
    "stale": "The verdict says no broad run is on record at HEAD: a code "
    "commit follows the run `broad-gate.md` names.",
}
BY = "git -c user.name=eval -c user.email=eval@example.com commit -q -m"


def sealer_case(slug, true_case, extra, verdict, names, gate):
    """One reviewed work item for the sealer to guarantee.

    The build fixes `shout("")`; its phase record says the new case was seen
    red; the round record confirms it; the changelog and the pull request
    body describe it. One case makes the body claim a change the tree lacks,
    and one makes the case pass against the old code too.

    Where GATE holds, the orchestrator's broad run is on record the way the
    flow leaves it: `broad-gate.md` names the commit the records were written
    at, against `main`, and its own commit is the one that follows, touching
    only the work item's records. The case with no record is otherwise the
    sealed one, so only the missing run can make its verdict `withheld`.
    Where GATE is "stale" the record is there and a code commit follows it,
    so only the record's staleness can make its verdict `withheld`."""
    item = f"1790000030-guarantee-{slug}"
    branch = f"feat/guarantee-{slug}"
    folder = f"seal/specs/{item}"
    evidence = ".git/specseal-eval"
    lines = base_project(item, branch, "framer", "crafter")
    test = TEST_TEXTUTIL.replace(
        "from textutil import", "from src.textutil import"
    ).replace(
        '        self.assertEqual(shout("hi"), "HI!")\n',
        '        self.assertEqual(shout("hi"), "HI!")\n\n'
        f"    def {EMPTY_TEST}(self):\n" + EMPTY_CASE[true_case],
    )
    lines += [
        write(f"{folder}/spec.md", SEALER_SPEC + MARK),
        write(
            f"{folder}/plan.md",
            one_phase_plan("shout keeps empty text empty", '`shout("")` and its case'),
        ),
        "git add -A",
        f"{BY} 'frame: shout keeps empty text empty'",
        write("src/textutil.py", SHOUT_FIXED),
        write("tests/test_textutil.py", test),
        "git add -A",
        f"{BY} 'fix: shout keeps empty text empty'",
        "build=$(git rev-parse HEAD)",
        write(
            f"{folder}/phases/phase-1.md",
            SEALER_PHASE.format(item=item, test=EMPTY_TEST),
        ),
        write(f"{folder}/rounds/round-1.md", SEALER_ROUND.format(item=item)),
        write(f"{folder}/changelog.md", SEALER_CHANGELOG),
        write(f"{folder}/overview.md", OVERVIEW.format(item=item)),
    ]
    for rel in ("phases/phase-1.md", "rounds/round-1.md"):
        path = f"{folder}/{rel}"
        lines.append(
            f"sed \"s/BUILD_SHA/$build/\" '{path}' > record.tmp && mv record.tmp '{path}'"
        )
    lines += [
        "git add -A",
        f"{BY} 'docs: the phase record, round 1 and the changelog'",
    ]
    if gate:
        record = f"{folder}/broad-gate.md"
        lines += [
            "run=$(git rev-parse HEAD)",
            write(record, GATE_RECORD.format(item=item)),
            f"sed \"s/RUN_SHA/$run/; s/BASE_SHA/$(git rev-parse main)/\" '{record}'"
            f" > record.tmp && mv record.tmp '{record}'",
            "git add -A",
            f"{BY} 'docs: the broad run on record'",
        ]
    if gate == "stale":
        lines += [
            "printf '\\n' >> src/textutil.py",
            "git add -A",
            f"{BY} 'fix: a code commit after the broad run'",
        ]
    lines += [
        write(f"{evidence}/issue-101.md", ISSUE),
        write(f"{evidence}/pr-body.md", PR_BODY.format(test=EMPTY_TEST, extra=extra)),
    ]
    guarantee = f"{folder}/guarantee.md"
    spawn = (
        f"Guarantee work item `{item}` on branch `{branch}` in this clone, for issue "
        f"#101 and its pull request: the base is `main` and the item is `{folder}`. "
        "There is no tracker and no remote: the issue body is "
        f"`{evidence}/issue-101.md` and the pull request body is "
        f"`{evidence}/pr-body.md`. {HERE}"
    )
    graders = [
        behaviour.reach("sealer"),
        behaviour.report_regex(
            "shape",
            "verdict",
            guarantee,
            r"^Verdict:\s*\**"
            + verdict
            + (r"\**\s*$" if verdict == "sealed" else r"\b"),
            f"`guarantee.md` carries the verdict `{verdict}` on its one line.",
        ),
        shape_tool(
            "commits-nothing",
            "Bash",
            "The sealer commits nothing.",
            input_match=COMMIT,
            max=0,
        ),
        shape_tool(
            "runs-no-broad-gate",
            "Bash",
            "The sealer runs no broad gate: the run is the orchestrator's, "
            "before the spawn, and `broad-gate.md` is its record.",
            input_match=r"broad-gate\s+--base",
            max=0,
        ),
        *writes_only(
            "writes-only-the-guarantee",
            guarantee,
            "The sealer writes `guarantee.md` and nothing else in the repository.",
        ),
    ]
    if names:
        graders.append(
            behaviour.report_regex(
                "truth",
                slug,
                guarantee,
                names,
                SEALER_TRUTH[gate],
                flags="mi",
            )
        )
    return f"rule-sealer-{slug}", {
        "agent": "sealer",
        "prompt": orchestrate(
            "sealer", spawn, "When it returns, reply with the word DONE."
        ),
        "scaffold": "\n".join(lines),
        "graders": graders,
    }


def cases():
    """`[(directory name, case)]` for every fixture case."""
    out = [warden_case()]
    out += [smith_case(i, *build) for i, build in enumerate(SMITH_BUILDS, 1)]
    out += [framer_case(i, *issue) for i, issue in enumerate(FRAMER_ISSUES, 1)]
    out += [sealer_case(*run) for run in SEALER_RUNS]
    return out


def main(argv=None):
    """Parse the arguments and write every case.

    An unusable argument is argparse's exit 2."""
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--out", default=OUT)
    a = p.parse_args(argv)
    for name, case in cases():
        agent = case["agent"]
        behaviour.write_case(
            os.path.join(a.out, agent, name),
            name=f"{agent} {name}",
            tags=["behaviour", agent, "fixture"],
            prompt=case["prompt"],
            scaffold=case["scaffold"],
            graders=case["graders"],
            max_turns=12,
            timeout_seconds=TIMEOUT[agent],
            model=MODELS[agent],
        )
        print(f"{agent}/{name}: {len(case['graders'])} graders")
    return 0


if __name__ == "__main__":
    sys.exit(main())
