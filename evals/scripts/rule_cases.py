#!/usr/bin/env python3
"""Generate the fixture cases: a fixture repository per case, graded on
outcome only.

Each case is a small stdlib Python project opted into AgenticSeal (`seal/`
with its marker and a routing declaration), built by its scaffold, and a session that
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
  framer   five issues to frame: the three documents with the mark and a
           Phases table carrying `Verified by`, nothing written outside
           the work item, and for the fifth, whose answer only running
           `shout` gives, that answer in `## Grounding` labelled
           `executed`
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
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "..", "hooks", "lib"
    ),
)
import behaviour
import optin
import replay_targets as rt

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "evals", "behaviour")
PR_BODY_MODULE = os.path.join(ROOT, "skills", "code-review", "scripts", "pr_body.py")


def load(path, name):
    """The Python file at PATH, imported as NAME."""
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# `seal pr-body`'s module: its `compose` writes the part of a sealer case's
# pull request body that the case's records hold.
pr_body = load(PR_BODY_MODULE, "agentic_pr_body_for_rule_cases")

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
# The author and committer of every commit a scaffold makes: the project
# every case builds, so no commit in the repository names the run as a
# measurement (`tests/text/test_no_case_tells_the_agent_it_is_evaluated.py`).
AUTHOR = "textutil"
BY = f"git -c user.name={AUTHOR} -c user.email={AUTHOR}@example.com commit -q -m"
# The directory a sealer case keeps the issue body and the pull request body
# in, by its work item, outside the work tree the sealer guarantees.
EVIDENCE = ".git/{item}"

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

Approved 2026-10-14 by the repository owner, when `crafter` was spawned.

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
    delimiter = "AGENTIC_EOF"
    if delimiter in text:
        raise ValueError(f"{path}: the text holds the heredoc delimiter")
    return f"mkdir -p \"$(dirname '{path}')\"\ncat > '{path}' <<'{delimiter}'\n{text.rstrip()}\n{delimiter}"


def fill(path, values):
    """A scaffold line that fills, in the file at PATH, each placeholder of
    VALUES, `[(placeholder, shell value)]`, with its value, the first on each
    line, through one `sed`."""
    script = "; ".join(f"s/{old}/{new}/" for old, new in values)
    return f"sed \"{script}\" '{path}' > record.tmp && mv record.tmp '{path}'"


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
        # The marker is what makes `seal/` the plugin's root to every gate.
        "seal/README.md": optin.MARKER + "\n",
        "seal/config.md": CONFIG,
        f"seal/threads/{item}/routing.md": routing(branch, planning, implementation),
    }
    lines = ["git init -q -b main ."]
    lines += [write(p, t) for p, t in files.items()]
    lines += [
        "git add -A",
        f"{BY} 'base: textutil'",
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


# --- proofer -------------------------------------------------------------------

PROOFER_ITEM = "1790000001-shout-ends-with-one-exclamation-mark"
PROOFER_CASE = "rule-proofer-one-finding"


def proofer_case():
    """One review of a diff that drops the spec's exclamation mark."""
    item, branch = PROOFER_ITEM, "feat/shout-exclaims"
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
        write(f"seal/threads/{item}/frame/design.md", spec + MARK),
        write(
            f"seal/threads/{item}/frame/plan.md",
            one_phase_plan("shout_twice", "`shout_twice(text)` in `src/textutil.py`"),
        ),
        "git add -A",
        f"{BY} 'frame: shout_twice'",
        write(
            "src/textutil.py",
            TEXTUTIL
            + '\n\ndef shout_twice(text):\n    """Return shout(TEXT) twice."""\n'
            "    return shout(text) + shout(text)\n",
        ),
        "git add -A",
        f"{BY} 'feat: shout_twice'",
    ]
    report = f"seal/threads/{item}/trail/rounds/round-1.md"
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
    for name, pattern, body in rt.truths_with(PROOFER_CASE, [shout], None):
        graders.append(behaviour.report_regex("truth", name, report, pattern, body))
    return PROOFER_CASE, {
        "agent": "proofer",
        "prompt": orchestrate(
            "proofer",
            spawn,
            f"When it returns, run `cat {report}` once and reply with the report's path.",
        ),
        "scaffold": "\n".join(lines),
        "graders": graders,
    }


# --- crafter -------------------------------------------------------------------

CRAFTER_BUILDS = (
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


def crafter_case(index, slug, signature, rule, example):
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
        write(f"seal/threads/{item}/frame/design.md", spec + MARK),
        write(f"seal/threads/{item}/frame/plan.md", plan),
        "git add -A",
        f"{BY} 'frame: {name}'",
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
            "The phase closes with its `trail/phases/phase-1.md`, which the next phase reads.",
            type="file_exists",
            path=f"seal/threads/{item}/trail/phases/phase-1.md",
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
    return f"rule-crafter-{slug}", {
        "agent": "crafter",
        "prompt": orchestrate(
            "crafter", spawn, "When it returns, reply with the word DONE."
        ),
        "scaffold": "\n".join(lines),
        "graders": graders,
    }


# --- framer --------------------------------------------------------------------

# A line of `## Grounding`, before the next `## ` heading, holding both the
# label and the word running `shout("straße")` returns.
PROBE_ANSWER = (
    r"^## Grounding[ \t]*$(?:\n(?!## ).*)*?\n(?!## )(?=.*[Ee]xecuted)(?=.*STRASSE).*"
)


def probe_graders(folder):
    """The sharp-s case's own grader for the work item at FOLDER: the
    answer running `shout` gives is in `## Grounding` labelled `executed`."""
    return [
        shape_regex(
            "answers-by-probe",
            {"source": "file", "path": f"{folder}/frame/design.md"},
            PROBE_ANSWER,
            "The answer running `shout` gives is a line of `## Grounding` "
            "labelled `executed`.",
            flags="m",
        ),
    ]


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
    (
        "sharp-s",
        "A user reports that `shout` returns some words longer than they went in, `straße` among them. The README should say which words `shout` lengthens and what it returns for them.",
        probe_graders,
    ),
)


def framer_case(index, slug, issue, extra=None):
    """One issue to frame as a work item whose routing is written. EXTRA,
    where given, returns the case's own graders for its work item's folder."""
    item = f"179000002{index}-{slug}"
    branch = f"feat/{slug}"
    lines = base_project(item, branch, "framer", "crafter")
    folder = f"seal/threads/{item}"
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
                f"The frame writes `frame/{document}`.",
                type="file_exists",
                path=f"{folder}/frame/{document}",
            )
            for name, document in (
                ("spec", "design.md"),
                ("plan", "plan.md"),
                ("questions", "questions.md"),
            )
        ),
        shape_regex(
            "marks-the-spec",
            {"source": "file", "path": f"{folder}/frame/design.md"},
            r"^Framed \d{4}-\d{2}-\d{2} by framer",
            "The framer's mark is at the foot of `frame/design.md`.",
            flags="m",
        ),
        shape_regex(
            "phases-carry-verified-by",
            {"source": "file", "path": f"{folder}/frame/plan.md"},
            r"^\| Phase \| Delivers \| Verified by \| Status \|",
            "Each phase names what verifies it.",
            flags="m",
        ),
        *writes_only(
            "builds-nothing",
            f"{folder}/",
            "The framer writes no source file and no test: every write is in its work item.",
        ),
        *(extra(folder) if extra else ()),
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
# The build commit's placeholder in the records and the pull request body,
# which the scaffold fills with the commit it makes. It is hexadecimal because
# `chain_check.py`'s grammar reads a `target:` line only where it names a
# commit, and `pr_body.compose` reads the round record through that grammar.
BUILD_SHA = "b0b0b0b"
SEALER_PHASE = """# {item} — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | {build} |

## What this phase was asked

`plan.md`'s row 1: `shout("")` returns `""`, with its case.

## What this phase found

`tests/test_textutil.py::ShoutTest::{test}` was seen red against the code
before the change (`python3 -m unittest tests.test_textutil -q` with
`src/textutil.py` as it stands on `main`: 1 failure), and green after it
(`executed`).
"""
SEALER_ROUND = """# {item} — review round 1

target: {build} against main

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
# The part of each case's pull request body under `pr_body.HEADING`, the
# orchestrator's: what no record holds. The part above it is
# `pr_body.compose` over the case's records.
OWN_PART = "{extra}Closes #101.\n"
# The record `seal gate --record` writes, in `broad_gate.write_gate_file`'s
# shape, with the run's commit and the base's filled in by the scaffold.
GATE_RECORD = """# {item} — broad gate

| Field | Value |
|---|---|
| Broad gate | RUN_SHA against BASE_SHA |
"""
# Each case: (slug, the case's assertion is true, the claim the body's
# `OWN_PART` adds before its `Closes` line, the verdict the guarantee reads,
# the pattern its verdict line must match to name what the tree
# contradicts, or None for a sealed item, and whether
# the orchestrator's broad run is recorded before the spawn: True, False, or
# "stale" for a record a code commit follows).
SEALER_RUNS = (
    ("sealed", True, "", "sealed", None, True),
    (
        "untrue-body",
        True,
        "`README.md` now documents `shout` and its empty-text rule.\n\n",
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
    "`trail/gate.md` is absent, so nothing broad ran.",
    "stale": "The verdict says no broad run is on record at HEAD: a code "
    "commit follows the run `trail/gate.md` names.",
}


def sealer_case(slug, true_case, extra, verdict, names, gate):
    """One reviewed work item for the sealer to guarantee.

    The build fixes `shout("")`; its phase record says the new case was seen
    red; the round record confirms it; the changelog describes it. The pull
    request body is `pr_body.compose` over the records, then the
    orchestrator's part, `OWN_PART`; its placeholders are filled as the
    records' are, so `seal pr-body --check` accepts it. One case makes the
    orchestrator's part claim a change the tree lacks, and one makes the case
    pass against the old code too.

    Where GATE holds, the orchestrator's broad run is on record the way the
    flow leaves it: `trail/gate.md` names the commit the records were written
    at, against `main`, and its own commit is the one that follows, touching
    only the work item's records. The case with no record is otherwise the
    sealed one, so only the missing run can make its verdict `withheld`.
    Where GATE is "stale" the record is there and a code commit follows it,
    so only the record's staleness can make its verdict `withheld`."""
    item = f"1790000030-guarantee-{slug}"
    branch = f"feat/guarantee-{slug}"
    folder = f"seal/threads/{item}"
    evidence = EVIDENCE.format(item=item)
    lines = base_project(item, branch, "framer", "crafter")
    test = TEST_TEXTUTIL.replace(
        "from textutil import", "from src.textutil import"
    ).replace(
        '        self.assertEqual(shout("hi"), "HI!")\n',
        '        self.assertEqual(shout("hi"), "HI!")\n\n'
        f"    def {EMPTY_TEST}(self):\n" + EMPTY_CASE[true_case],
    )
    # The records the body is composed from, by their path in the work item.
    records = {
        "frame/plan.md": one_phase_plan(
            "shout keeps empty text empty", '`shout("")` and its case'
        ),
        "trail/phases/phase-1.md": SEALER_PHASE.format(
            item=item, test=EMPTY_TEST, build=BUILD_SHA
        ),
        "trail/rounds/round-1.md": SEALER_ROUND.format(item=item, build=BUILD_SHA),
        "changelog.md": SEALER_CHANGELOG,
        "gaps.md": OVERVIEW.format(item=item),
    }
    built = [(BUILD_SHA, "$build")]
    ran = [("RUN_SHA", "$run"), ("BASE_SHA", "$(git rev-parse main)")]
    lines += [
        write(f"{folder}/frame/design.md", SEALER_SPEC + MARK),
        write(f"{folder}/frame/plan.md", records["frame/plan.md"]),
        "git add -A",
        f"{BY} 'frame: shout keeps empty text empty'",
        write("src/textutil.py", SHOUT_FIXED),
        write("tests/test_textutil.py", test),
        "git add -A",
        f"{BY} 'fix: shout keeps empty text empty'",
        "build=$(git rev-parse HEAD)",
    ]
    for rel in (
        "trail/phases/phase-1.md",
        "trail/rounds/round-1.md",
        "changelog.md",
        "gaps.md",
    ):
        lines.append(write(f"{folder}/{rel}", records[rel]))
    for rel in ("trail/phases/phase-1.md", "trail/rounds/round-1.md"):
        lines.append(fill(f"{folder}/{rel}", built))
    lines += [
        "git add -A",
        f"{BY} 'docs: the phase record, round 1 and the changelog'",
    ]
    if gate:
        record = f"{folder}/trail/gate.md"
        records["trail/gate.md"] = GATE_RECORD.format(item=item)
        lines += [
            "run=$(git rev-parse HEAD)",
            write(record, records["trail/gate.md"]),
            fill(record, ran),
            "git add -A",
            f"{BY} 'docs: the broad run on record'",
        ]
    if gate == "stale":
        lines += [
            "printf '\\n' >> src/textutil.py",
            "git add -A",
            f"{BY} 'fix: a code commit after the broad run'",
        ]
    body = f"{evidence}/pr-body.md"
    lines += [
        write(f"{evidence}/issue-101.md", ISSUE),
        write(body, pr_body.compose(item, records) + OWN_PART.format(extra=extra)),
        fill(body, built + (ran if gate else [])),
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
            "runs-no-broad-run",
            "Bash",
            "The sealer runs no broad gate: the run is the orchestrator's, "
            "before the spawn, and `trail/gate.md` is its record.",
            input_match=r"seal\s+gate\s+--base",
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
    out = [proofer_case()]
    out += [crafter_case(i, *build) for i, build in enumerate(CRAFTER_BUILDS, 1)]
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
