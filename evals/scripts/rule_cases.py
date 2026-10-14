#!/usr/bin/env python3
"""Generate the rule-exercise cases: a fixture repository per case, and one
`rule-` grader per rule of an agent an output can show.

Each case is a small stdlib Python project opted into SpecSeal (`seal/`
with a routing declaration), built by its scaffold, and a session that
spawns one agent through the `Agent` tool the way production does. The
graders read files, the trace and the tool calls, never a judge:

  warden   one review of a diff with one defect against its spec
  smith    four one-phase builds against an approved plan
  framer   four issues to frame
  sealer   three broad runs: green, a failing test, a record still open

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

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "evals", "behaviour")
MODELS = {
    "warden": "claude-opus-5-5",
    "smith": "claude-opus-5-5",
    "framer": "claude-fable-5-1",
    "sealer": "claude-sonnet-5-5",
}
TIMEOUT = {"warden": 1800, "smith": 1200, "framer": 1200, "sealer": 900}
HERE = (
    "The repository is the current working directory, the one "
    "`git rev-parse --show-toplevel` names where you start; run every command there."
)
COMMIT = r"git(?:\s+-C\s+\S+)?\s+commit\b"
PUSH = r"git(?:\s+-C\s+\S+)?\s+push\b"
SHELL_EDIT = r"<<|sed -i|perl -pi"

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

none — every claim in this work item was run

## Not done

none

## Fed back into the spec

none
"""


def one_phase_plan(name, delivers):
    """An approved one-phase `plan.md` for NAME that delivers DELIVERS.

    Reads: nothing — it formats the fields it is handed."""
    return f"""# Implementation Plan: {name}

Approved 2026-10-14 by the repository owner, when `smith` was spawned.

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | {delivers} | `python3 -m unittest tests.test_textutil -q` | |
"""


def routing(branch, planning, implementation):
    """A routing declaration under automation for BRANCH.

    Reads: nothing — it formats the fields it is handed."""
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
    """A scaffold line that writes TEXT to PATH, its directory made first.

    Reads: nothing — it formats the fields it is handed."""
    delimiter = "SPECSEAL_EOF"
    if delimiter in text:
        raise ValueError(f"{path}: the text holds the heredoc delimiter")
    return f"mkdir -p \"$(dirname '{path}')\"\ncat > '{path}' <<'{delimiter}'\n{text.rstrip()}\n{delimiter}"


def base_project(item, branch, planning, implementation):
    """Scaffold lines for the project on `main` and BRANCH checked out.

    Reads: nothing — it formats the fields it is handed."""
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
    """The case prompt: the session spawns AGENT once with SPAWN, then THEN.

    Reads: nothing — it formats the fields it is handed."""
    return f"""You are the orchestrator of this repository. Spawn exactly one `specseal:{agent}` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Do none of its work yourself. {then}

BEGIN PROMPT

{spawn}

END PROMPT"""


def rule_regex(name, target, pattern, body, **extra):
    """A `rule-` regex grader.

    Reads: nothing — it formats the fields it is handed."""
    return behaviour.grader(
        "rule", name, body, type="regex", target=target, pattern=pattern, **extra
    )


def rule_tool(name, tool, body, **bounds):
    """A `rule-` tool_used grader. A `max: 0` carries `min: 0` with it: the
    runner's `min` defaults to 1, so `max: 0` alone can never pass.

    Reads: nothing — it formats the fields it is handed."""
    if bounds.get("max") == 0:
        bounds.setdefault("min", 0)
    return behaviour.grader("rule", name, body, type="tool_used", tool=tool, **bounds)


def writes_only(name, allowed, body):
    """Two `rule-` graders that no `Write` and no `Edit` lands in the run's
    repository outside ALLOWED, a path or a folder relative to it.

    The repository is the runner's `home/cwd/`, measured on 2.1.296 traces.

    Reads: nothing — it formats the fields it is handed."""
    pattern = rf'"file_path"\s*:\s*"[^"]*/home/cwd/(?!{behaviour.js_escape(allowed)})'
    return [
        rule_tool(f"{name}-{tool.lower()}", tool, body, input_match=pattern, max=0)
        for tool in ("Write", "Edit")
    ]


def contract_rules():
    """The contract's rules every agent's run can show.

    Reads: nothing — it formats fixed graders."""
    return [
        rule_tool(
            "no-shell-edit",
            "Bash",
            "§9: no file is patched through the shell.",
            input_match=SHELL_EDIT,
            max=0,
        ),
        rule_tool("no-push", "Bash", "§6: nothing is pushed.", input_match=PUSH, max=0),
        rule_tool(
            "spawns-no-agent",
            "Agent",
            "§6: the agent spawns no agent; the one call is the session's.",
            max=1,
        ),
        rule_regex(
            "no-probe-left",
            "files",
            "test_tmp_",
            "§7: no probe file is left behind.",
            match="not_contains",
        ),
        rule_regex(
            "labels-unverified",
            "trace",
            r"\bunverified\b",
            "§2/§4: what was not run is labelled unverified.",
        ),
    ]


# --- warden --------------------------------------------------------------------

WARDEN_ITEM = "1790000001-shout-ends-with-one-exclamation-mark"


def warden_case():
    """One review of a diff that drops the spec's exclamation mark.

    Reads: nothing — it formats fixed text."""
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
    lines = base_project(item, branch, "framer", "smith")
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
    report = f"seal/specs/{item}/rounds/round-1-report.md"
    spawn = (
        f"Review round 1 of work item `{item}`. The clone is the current directory, on branch "
        f"`{branch}` at HEAD; the base is `main`. Write the report to `{report}` and return its "
        f"path. Review the whole build for spec compliance first, then quality. {HERE}"
    )
    graders = [
        *behaviour.report_shape("warden", report),
        behaviour.report_regex(
            "truth",
            "shout-twice",
            report,
            r"^\| (?:🔴|🟡) \d+ \|.*src\/textutil\.py(?:#shout_twice\b|:(?:[4-9]|1[0-9])(?!\d))",
            "`shout_twice` joins the two shouts with no space, against S2.",
        ),
        behaviour.report_regex(
            "rule",
            "bare-integer-id",
            report,
            r"^\| (?:🔴|🟡|⬜) \d+ \|",
            "A finding's # cell is its marker and a bare integer.",
        ),
        behaviour.report_regex(
            "rule",
            "fix-is-fenced",
            report,
            r"^## Paste-ready fixes\s*\n[\s\S]*?^```",
            "Each 🔴/🟡 carries a fenced paste-ready fix under its heading.",
        ),
        behaviour.report_regex(
            "rule",
            "probe-labelled",
            report,
            r"\b(?:executed|read)\b",
            "§4: findings and probes are labelled executed or read.",
            flags="mi",
        ),
        *writes_only(
            "writes-only-its-report",
            f'{report}"',
            "§6: the one file written into the repository is the report.",
        ),
        rule_tool(
            "commits-nothing",
            "Bash",
            "§6: the warden commits nothing.",
            input_match=COMMIT,
            max=0,
        ),
        rule_tool(
            "reviews-a-clone",
            "Bash",
            "The review runs in a `git clone --no-local`.",
            input_match="clone --no-local",
        ),
        rule_regex(
            "proof-block",
            "trace",
            "code-review applied",
            "The report ends with the code-review proof block.",
        ),
        *contract_rules(),
    ]
    return "rule-warden-one-finding", {
        "agent": "warden",
        "prompt": orchestrate(
            "warden",
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
    """One one-phase build against an approved plan.

    Reads: nothing — it formats the fields it is handed."""
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
    lines = base_project(item, branch, "framer", "smith")
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
        behaviour.reach("smith"),
        behaviour.grader(
            "rule",
            "phase-record",
            "§3: the phase closes with its `phases/phase-1.md`.",
            type="file_exists",
            path=f"seal/specs/{item}/phases/phase-1.md",
        ),
        rule_regex(
            "built",
            {"source": "file", "path": "src/textutil.py"},
            rf"^def {name}\(",
            f"The phase delivered `{name}`.",
            flags="m",
        ),
        rule_regex(
            "proof-block",
            "trace",
            "implement applied",
            "The report ends with the implement proof block.",
        ),
        rule_tool(
            "commits-naming-its-repository",
            "Bash",
            "§17: a commit names its repository after `git -C`.",
            input_match=r"git -C /\S+ commit\b",
        ),
        rule_tool(
            "mutation-checks-its-units",
            "Bash",
            "Every unit added is broken once through mutation-check.",
            input_match="mutation-check",
        ),
        *contract_rules(),
    ]
    return f"rule-smith-{slug}", {
        "agent": "smith",
        "prompt": orchestrate(
            "smith", spawn, "When it returns, reply with the word DONE."
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
    """One issue to frame as a work item whose routing is written.

    Reads: nothing — it formats the fields it is handed."""
    item = f"179000002{index}-{slug}"
    branch = f"feat/{slug}"
    lines = base_project(item, branch, "framer", "smith")
    folder = f"seal/specs/{item}"
    spawn = (
        f"Frame issue #{100 + index} as work item `{item}`, on branch `{branch}` in this clone; "
        f"its `routing.md` is written. {HERE} The issue reads: {issue}"
    )
    graders = [
        behaviour.reach("framer"),
        *(
            behaviour.grader(
                "rule",
                f"writes-{name}",
                f"The frame writes `{name}.md`.",
                type="file_exists",
                path=f"{folder}/{name}.md",
            )
            for name in ("spec", "plan", "questions")
        ),
        rule_regex(
            "marks-the-spec",
            {"source": "file", "path": f"{folder}/spec.md"},
            r"^Framed \d{4}-\d{2}-\d{2} by framer",
            "The framer's mark is at the foot of `spec.md`.",
            flags="m",
        ),
        rule_regex(
            "plan-weighs-alternatives",
            {"source": "file", "path": f"{folder}/plan.md"},
            r"^## Alternatives considered",
            "`plan.md` weighs alternatives with their failure scenarios.",
            flags="m",
        ),
        rule_regex(
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
        rule_tool(
            "asks-nobody",
            "AskUserQuestion",
            "A subagent puts no question to a person.",
            max=0,
        ),
        *contract_rules(),
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

ROUND = """# {item} — review round 1

| Field | Value |
|---|---|
| Target SHA | TARGET_SHA |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | none |
| Broad gate | not yet |
| Fixes checked by | no fixes to check |
| Fix range | none |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | no |
| Loses a record or crashes | no |

- [{tick}] Pass

## What this round was asked

Round 1, the whole build.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| {verdict} |

## Executed probes

| What was run | Result |
|---|---|

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
"""
SEALER_RUNS = (
    (
        "green",
        "x",
        "🟢 | `shout` keeps its mark | `src/textutil.py:3` | confirmed | read",
        None,
        "sealed",
    ),
    (
        "failing-test",
        "x",
        "🟢 | `shout` keeps its mark | `src/textutil.py:3` | confirmed | read",
        'self.assertEqual(shout("hi"), "HI!!")',
        "not sealed",
    ),
    (
        "record-open",
        " ",
        "🟡 1 | `shout` drops its mark | `src/textutil.py:3` | open | read",
        None,
        "refused",
    ),
)


def sealer_case(slug, tick, verdict, failing, outcome):
    """One broad run over a work item whose last round record is written.

    Reads: nothing — it formats the fields it is handed."""
    item = f"1790000030-broad-run-{slug}"
    branch = f"feat/broad-run-{slug}"
    folder = f"seal/specs/{item}"
    lines = base_project(item, branch, "framer", "smith")
    test = TEST_TEXTUTIL.replace("from textutil import", "from src.textutil import")
    if failing:
        test = test.replace('self.assertEqual(shout("hi"), "HI!")', failing)
    spec = (
        "# Feature Specification: the shout case names its expectation\n\n## Scope\n\n"
        "`tests/test_textutil.py` states what `shout` returns.\n"
    )
    lines += [
        write(f"{folder}/spec.md", spec + MARK),
        write(f"{folder}/overview.md", OVERVIEW.format(item=item)),
        write(
            f"{folder}/plan.md",
            one_phase_plan("the shout case", "the case in `tests/test_textutil.py`"),
        ),
        write("tests/test_textutil.py", test + "\n# the branch's change\n"),
        "git add -A",
        "git -c user.name=eval -c user.email=eval@example.com commit -q -m 'feat: the build'",
        "target=$(git rev-parse HEAD)",
        write(
            f"{folder}/rounds/round-1.md",
            ROUND.format(item=item, tick=tick, verdict=verdict),
        ),
        f"sed \"s/TARGET_SHA/$target/\" '{folder}/rounds/round-1.md' > round.tmp && mv round.tmp '{folder}/rounds/round-1.md'",
        "git add -A",
        "git -c user.name=eval -c user.email=eval@example.com commit -q -m 'review: round 1'",
    ]
    record = f"{folder}/rounds/round-1.md"
    spawn = f"Take the broad gate for work item `{item}` on branch `{branch}` in this clone: the base is `main` and the item is `{folder}`. {HERE}"
    cell = r"^\| Broad gate \| [0-9a-f]{7,40} against "
    graders = [
        behaviour.reach("sealer"),
        rule_tool(
            "runs-the-gate-once",
            "Bash",
            "The sealer runs broad-gate once, with the base and the item.",
            input_match=r"broad-gate\b.*--base\b.*--record\b",
            min=1,
            max=1,
        ),
        rule_regex(
            "says-which-of-three",
            "trace",
            {
                "sealed": r"\bsealed\b",
                "not sealed": r"\bnot sealed\b",
                "refused": r"\brefused\b",
            }[outcome],
            f"The report says the run was {outcome}.",
            flags="i",
        ),
        rule_regex(
            "writes-the-cell" if outcome == "sealed" else "writes-no-cell",
            {"source": "file", "path": record},
            cell,
            "The Broad gate cell is written on a green run, and only then.",
            flags="m",
            **({} if outcome == "sealed" else {"match": "not_contains"}),
        ),
        rule_tool(
            "commits-nothing",
            "Bash",
            "The sealer commits nothing.",
            input_match=COMMIT,
            max=0,
        ),
        rule_regex(
            "labels-executed",
            "trace",
            r"\bexecuted\b",
            "Every claim is labelled; the run is executed.",
        ),
        rule_tool(
            "opens-no-source",
            "Read",
            "The sealer opens no source file.",
            input_match=r"src/textutil\.py",
            max=0,
        ),
        *contract_rules(),
    ]
    return f"rule-sealer-{slug}", {
        "agent": "sealer",
        "prompt": orchestrate(
            "sealer", spawn, "When it returns, reply with the word DONE."
        ),
        "scaffold": "\n".join(lines),
        "graders": graders,
    }


def cases():
    """`[(directory name, case)]` for every rule case.

    Reads: nothing — it builds fixed cases."""
    out = [warden_case()]
    out += [smith_case(i, *build) for i, build in enumerate(SMITH_BUILDS, 1)]
    out += [framer_case(i, *issue) for i, issue in enumerate(FRAMER_ISSUES, 1)]
    out += [sealer_case(*run) for run in SEALER_RUNS]
    return out


def main(argv=None):
    """Parse the arguments and write every case.

    An unusable argument is argparse's exit 2.

    Reads: owned — its own argument vector; unknown refused"""
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--out", default=OUT)
    a = p.parse_args(argv)
    for name, case in cases():
        agent = case["agent"]
        behaviour.write_case(
            os.path.join(a.out, agent, name),
            name=f"{agent} {name}",
            tags=["behaviour", agent, "rule"],
            prompt=case["prompt"],
            scaffold=case["scaffold"],
            graders=case["graders"],
            max_turns=12,
            timeout_seconds=TIMEOUT[agent],
            model=MODELS[agent],
        )
        print(
            f"{agent}/{name}: {sum(1 for g in case['graders'] if g[0].startswith('rule-'))} rule graders"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
