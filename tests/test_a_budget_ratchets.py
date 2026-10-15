"""A budget holds its ceiling from both sides, and a raise says why.

Issue #930: nothing held the repository's size and speed, so each slowdown
was found by a person and cleaned up once. `seal/budgets.md` names each
budget with its ceiling and slack, and `.github/scripts/budget_check.py`
measures it and holds the ceiling to a band: never under the measurement, and
never so far above it that a cleanup's headroom is left for the next change
to spend. A ceiling raised since the merge base needs a `Budget raised:` line
in the pull request body.

The cases build a small tree — one agent, one skill, of known sizes — and run
the checker's `main` in process. The rows of `plan.md` §*Test rows* name the
mutation each case is there to kill; `phases/phase-1.md` records each case
seen red under it. `test_the_trees_budgets_hold` is the gate's local form,
over this repository's own tree, so the sealer's run sees the budgets before
a push does.
"""

import datetime
import importlib.util
import json
import os
import re
import subprocess

import conftest
import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, ".github", "scripts", "budget_check.py")


def _load():
    spec = importlib.util.spec_from_file_location("specseal_budget_check", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


budget_check = _load()

# U+2028, which `str.splitlines` ends a line at and GitHub does not.
LS = chr(0x2028)

# The fixture agent's two files, 600 and 400 bytes: `preload:warden` measures
# 1,000 bytes in every tree `tree` builds. A second agent, `scout`, shares the
# skill and measures 500, so a case can hold a row the base did not name.
MEASURED = 1000
AGENT_HEAD = "---\nname: warden\nskills:\n  - review\n---\n"
SCOUT_HEAD = "---\nname: scout\nskills:\n  - review\n---\n"
SKILL_HEAD = "# review\n"


def _sized(head, size):
    return head + "x" * (size - len(head) - 1) + "\n"


def budgets(*rows):
    """A `seal/budgets.md` holding `rows`, each `(name, unit, ceiling, slack,
    kind)`."""
    lines = [
        "# Budgets",
        "",
        "## Budgets",
        "",
        "| Budget | Unit | Ceiling | Slack | Kind |",
        "|---|---|---|---|---|",
    ]
    lines += ["| " + " | ".join(str(cell) for cell in row) + " |" for row in rows]
    return "\n".join(lines) + "\n"


def warden(ceiling, slack="2 %", kind="gate"):
    return ("preload:warden", "bytes", ceiling, slack, kind)


def git(root, *args):
    subprocess.run(
        ["git", "-C", str(root), "-c", "user.email=t@t", "-c", "user.name=t", *args],
        check=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )


def write(root, files):
    for rel, text in (files or {}).items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, "utf-8", newline="\n")


def tree(tmp_path, head, base=None, files=None, base_files=None):
    """A repository whose agent measures `MEASURED` bytes and whose
    `seal/budgets.md` is `head`. With `base`, the file is first committed as
    `base` on a branch called `base` — or left out of it where `base` is "" —
    and `head` is committed on top, so `--baseline base` reads the two.
    `base_files` are written before the base commit and `files` after it,
    each `{path: text}`. Every file is written with LF line ends, whatever
    the platform's text mode would write."""
    root = tmp_path / "repo"
    (root / "agents").mkdir(parents=True)
    (root / "skills" / "review").mkdir(parents=True)
    (root / "seal").mkdir()
    write(
        root,
        {
            "agents/warden.md": _sized(AGENT_HEAD, 600),
            "agents/scout.md": _sized(SCOUT_HEAD, 100),
            "skills/review/SKILL.md": _sized(SKILL_HEAD, 400),
        },
    )
    write(root, base_files)
    if base is not None:
        git(root, "init", "-q")
        if base:
            write(root, {"seal/budgets.md": base})
        git(root, "add", "-A")
        git(root, "commit", "-qm", "base")
        git(root, "branch", "base")
    if head is not None:
        write(root, {"seal/budgets.md": head})
    write(root, files)
    if base is not None:
        git(root, "add", "-A")
        git(root, "commit", "-qm", "head", "--allow-empty")
    return root


def run(root, *args, env=None):
    return budget_check.main(
        ["--root", str(root), *args], env={} if env is None else env
    )


def ratchet(root, body, *args):
    return run(
        root,
        "--baseline",
        "base",
        "--pr-body-env",
        "PR_BODY",
        *args,
        env={"PR_BODY": body},
    )


def test_the_fixture_measures_what_the_cases_assume(tmp_path):
    """The number every case below is written against. A fixture that
    measured something else would make each case about a different band."""
    root = tree(tmp_path, budgets(warden(MEASURED)))
    row = budget_check.budgets_here(str(root))[0]
    assert budget_check.measure(str(root), row, {}) == MEASURED


def test_measured_over_ceiling_fails_naming_the_row(tmp_path, capsys):
    """T1, S1: one byte over the ceiling is exit 1, and the line names the
    row, what was measured and the ceiling it broke."""
    root = tree(tmp_path, budgets(warden(MEASURED - 1)))
    assert run(root) == 1
    out = capsys.readouterr().out
    assert (
        "budget-check: preload:warden: measured 1,000 bytes is over the ceiling 999 by 1"
        in out
    ), out
    assert "Budget raised: preload:warden 999 -> <new>: <reason>" in out, out


@pytest.mark.parametrize(
    "ceiling",
    [MEASURED, MEASURED * 102 // 100],
    ids=["the ceiling is the measurement", "the ceiling is the top of the band"],
)
def test_measured_inside_the_band_holds(tmp_path, capsys, ceiling):
    """T2: both edges of the band hold — a ceiling equal to the measurement,
    and one at `measured x 1.02` under a 2 % slack."""
    root = tree(tmp_path, budgets(warden(ceiling)))
    assert run(root) == 0, capsys.readouterr()


def test_a_ceiling_above_the_band_asks_to_lower(tmp_path, capsys):
    """T3, S4: a cleanup took the measurement to the ceiling / 1.05 under a
    2 % slack, and the ceiling stayed. Exit 1, naming the number to lower to
    and the top of the band."""
    root = tree(tmp_path, budgets(warden(1050)))
    assert run(root) == 1
    out = capsys.readouterr().out
    assert "the ceiling 1,050 sits above the band" in out, out
    assert (
        "Lower the ceiling in seal/budgets.md to 1000 — anything from 1000 to 1020 holds"
        in out
    ), out


RAISED_BASE = budgets(warden(1000, "10 %"))
RAISED_HEAD = budgets(warden(1050, "10 %"))


@pytest.mark.parametrize(
    "body",
    [
        "",
        "Budget raised: preload:warden 1000 -> 1100: a later raise",
        "Budget raised: preload:warden 900 -> 1050: an earlier one",
        "The warden budget preload:warden moves 1000 -> 1050 here.",
        "Budget raised: preload:warden 1000 -> 1050:",
        "Intro" + LS + "Budget raised: preload:warden 1000 -> 1050: one line to GitHub",
    ],
    ids=[
        "no line",
        "another new value",
        "another old value",
        "a mention",
        "no reason",
        "a line that opens no line GitHub shows",
    ],
)
def test_a_raise_without_its_line_fails(tmp_path, capsys, body):
    """T4, S2: a ceiling higher than at the merge base fails unless the body
    declares that raise, both numbers and a reason. The failure names the
    row and the line to write, and the summary marks the raise undeclared,
    since its band verdict alone reads `holds`."""
    root = tree(tmp_path, RAISED_HEAD, base=RAISED_BASE)
    assert ratchet(root, body) == 1
    out = capsys.readouterr().out
    assert "- `preload:warden` raised 1000 -> 1050: **not declared**" in out, out
    assert (
        "budget-check: preload:warden: the ceiling was raised from 1000 to 1050" in out
    ), out
    assert (
        "Write `Budget raised: preload:warden 1000 -> 1050: <reason>` in the body"
        in out
    ), out


@pytest.mark.parametrize(
    "body",
    [
        "Budget raised: preload:warden 1000 -> 1050: the review skill grew",
        "Intro.\n\n- Budget raised: `preload:warden` 1000 -> 1050: the review skill grew\n",
    ],
    ids=["a line of its own", "a list item with the name in backticks"],
)
def test_a_raise_with_its_line_passes_and_the_summary_shows_it(tmp_path, capsys, body):
    """T4, S3: the line, as a person writes it in markdown, is the
    declaration, and the summary carries the raise and its reason."""
    root = tree(tmp_path, RAISED_HEAD, base=RAISED_BASE)
    assert ratchet(root, body) == 0
    out = capsys.readouterr().out
    assert "- `preload:warden` raised 1000 -> 1050: the review skill grew" in out, out


OTHER = ("preload:scout", "bytes", 500, "2 %", "gate")


@pytest.mark.parametrize(
    "head",
    [budgets(), budgets(warden(MEASURED, kind="report"))],
    ids=["the row is gone", "the gate is a report"],
)
def test_a_removed_row_is_a_raise(tmp_path, capsys, head):
    """T5: a gate row that is gone, or is no longer a gate, has lifted its
    ceiling altogether. It fails without a `Budget removed:` line and passes
    with one."""
    root = tree(tmp_path, head, base=budgets(warden(MEASURED)))
    assert ratchet(root, "") == 1
    out = capsys.readouterr().out
    assert "Write `Budget removed: preload:warden: <reason>` in the body" in out, out
    assert "- `preload:warden` " in out and "**not declared**" in out, out
    assert ratchet(root, "Budget removed: preload:warden: the gate moved") == 0


def test_base_main_skips_the_line_and_keeps_the_ceiling(tmp_path, capsys):
    """T6, S6: a release pull request carries every work item's raises, and
    each carried its own line at its own pull request, so none is asked for
    against `main` — while a ceiling the tree is over still fails there."""
    root = tree(tmp_path, RAISED_HEAD, base=RAISED_BASE)
    assert ratchet(root, "", "--base-ref", "main") == 0
    assert (
        "- `preload:warden` raised 1000 -> 1050: at a release"
        in capsys.readouterr().out
    )
    over = tree(tmp_path / "over", budgets(warden(999, "10 %")), base=RAISED_BASE)
    assert ratchet(over, "", "--base-ref", "main") == 1
    assert "is over the ceiling 999" in capsys.readouterr().out


@pytest.mark.parametrize(
    "base",
    ["", budgets(OTHER)],
    ids=["no budgets file at the base", "the base has other rows"],
)
def test_a_new_row_needs_no_line(tmp_path, capsys, base):
    """T7: the first pull request to name a budget has no ceiling to have
    raised, so it needs no line."""
    root = tree(tmp_path, budgets(warden(MEASURED), OTHER), base=base)
    assert ratchet(root, "") == 0, capsys.readouterr()


def test_the_summary_goes_to_the_step_file_when_set_and_names_no_path(tmp_path, capsys):
    """T12, S5: where the runner names a step summary the table goes there,
    one line per budget with measured, ceiling, headroom and kind, and not
    to the log; and it names no path of the machine that ran it."""
    root = tree(tmp_path, budgets(warden(1010)))
    step = tmp_path / "summary.md"
    assert run(root, env={"GITHUB_STEP_SUMMARY": str(step)}) == 0
    summary = step.read_text("utf-8")
    assert (
        "| `preload:warden` | 1,000 bytes | 1,010 | 10 (1.0%) | gate | holds |"
        in summary
    ), summary
    assert "| Budget |" not in capsys.readouterr().out
    for path in (str(tmp_path), ROOT, os.path.expanduser("~")):
        assert path not in summary, path


def test_a_report_row_is_printed_and_never_fails(tmp_path, capsys):
    """A `report` row is measured and shown beside the gates, and a report
    over its ceiling does not fail the run (`spec.md` §*The budgets*, the
    Kind column)."""
    root = tree(tmp_path, budgets(warden(MEASURED - 1, kind="report")))
    assert run(root) == 0
    assert "| report | over |" in capsys.readouterr().out


@pytest.mark.parametrize(
    "ceiling, slack, verdict",
    [(1005, "+5", 0), (1005, "+5 bytes", 0), (1006, "+5", 1)],
    ids=["the top of the band", "the unit named", "one over the top"],
)
def test_an_absolute_slack_is_counted_in_the_rows_unit(
    tmp_path, capsys, ceiling, slack, verdict
):
    """`+N` is a slack of N in the row's unit, not a share: 1,000 bytes at
    `+5` allows a ceiling up to 1,005 and asks to lower one at 1,006."""
    root = tree(tmp_path, budgets(warden(ceiling, slack)))
    assert run(root) == verdict, capsys.readouterr()


def test_a_reader_the_checker_loads_that_is_gone_is_exit_2(
    tmp_path, capsys, monkeypatch
):
    """The table walker, the meter and the merge base are each read through
    the one module that owns it. A copy of the checker taken without them has
    read nothing, and says which one is missing rather than raising."""
    root = tree(tmp_path, budgets(warden(MEASURED)))
    monkeypatch.setattr(budget_check, "_loaded", {})
    monkeypatch.setitem(
        budget_check.SIBLINGS, "config", ("no-such-config.py", "it reads the table")
    )
    assert run(root) == 2
    assert (
        "cannot read no-such-config.py, and it reads the table"
        in capsys.readouterr().err
    )


def test_the_trees_budgets_hold():
    """T13: this repository's own `seal/budgets.md` holds against its own
    tree. The gate's local form, as the fold ceiling's pin is: a session and
    the sealer meet a broken budget before the pull request does."""
    assert budget_check.main(["--root", ROOT], env={}) == 0


def _broken_skill(root):
    (root / "skills" / "review" / "SKILL.md").unlink()


@pytest.mark.parametrize(
    "head, args, env, undo, said",
    [
        (None, (), {}, None, "seal/budgets.md is not in the tree"),
        (budgets(warden("1,000")), (), {}, None, "is not a whole number"),
        (budgets(warden(MEASURED, "two")), (), {}, None, "`two` is no slack"),
        (budgets(warden(MEASURED, "+5 lines")), (), {}, None, "`+5 lines` is no slack"),
        (budgets(("preload", "bytes", 1, "2 %", "gate")), (), {}, None, "no measurer"),
        (
            budgets(warden(MEASURED, kind="maybe")),
            (),
            {},
            None,
            "neither gate nor report",
        ),
        (budgets(warden(1), warden(1)), (), {}, None, "is written twice"),
        (budgets(("nosuch:x", "bytes", 1, "2 %", "gate")), (), {}, None, "no measurer"),
        (
            budgets(("preload:warden", "tokens", 1, "2 %", "gate")),
            (),
            {},
            None,
            "the unit is `tokens`",
        ),
        (
            budgets(("preload:nobody", "bytes", 1, "2 %", "gate")),
            (),
            {},
            None,
            "is named nobody",
        ),
        (budgets(warden(MEASURED)), (), {}, _broken_skill, "is not in the tree"),
        (
            budgets(warden(MEASURED)) + "| stray |\n",
            (),
            {},
            None,
            "stops at `| stray |`",
        ),
        (
            budgets(warden(MEASURED)),
            ("--pr-body-env", "PR_BODY"),
            {},
            None,
            "PR_BODY, which is not set",
        ),
        (
            budgets(warden(MEASURED)),
            ("--baseline", "nosuch"),
            {},
            None,
            "gives no merge base",
        ),
    ],
    ids=[
        "no file",
        "a ceiling with a comma",
        "a slack in words",
        "an absolute slack in another unit",
        "a family with no subject",
        "an unknown kind",
        "a row twice",
        "an unknown family",
        "a unit the family is not measured in",
        "an agent the tree lacks",
        "a skill file the agent names is gone",
        "a row the table walker refuses",
        "a body variable that is not set",
        "a baseline that does not resolve",
    ],
)
def test_a_malformed_row_or_a_missing_file_is_exit_2(
    tmp_path, capsys, head, args, env, undo, said
):
    """T16, S11: a file that is not there, a row that cannot be read, or an
    input the run was promised and did not get is exit 2 naming it — never 0,
    and never read as an empty file."""
    root = tree(tmp_path, head)
    if undo:
        undo(root)
    if "--baseline" in args:
        git(root, "init", "-q")
    assert run(root, *args, env=env) == 2
    err = capsys.readouterr().err
    assert said in err, err


# --- phase 2: the families measured per file, and the preload pair ----------


def table(header, rows):
    """A per-file table under its heading, `rows` as `(file, ceiling)`."""
    title = {
        "Seconds ceiling": "Slow test files",
        "Lines ceiling": "Docs history lines",
    }
    lines = ["", f"## {title[header]}", "", f"| File | {header} |", "|---|---|"]
    lines += [f"| {path} | {ceiling} |" for path, ceiling in rows]
    return "\n".join(lines) + "\n"


def slow(*rows, threshold=120, slack="one-sided", suite=None):
    """Budgets with the `slow-file` row and its table, and `suite-seconds`
    where `suite` is `(ceiling, slack)`."""
    head = [("slow-file", "seconds", threshold, slack, "gate")]
    if suite:
        head.append(("suite-seconds", "seconds", suite[0], suite[1], "gate"))
    return budgets(*head) + table("Seconds ceiling", rows)


# `test_a.py` at 130 s over two cases and `test_b.py` at 50 s, under a
# threshold of 120 s.
SMALL = {
    "tests/test_a.py::t1": 100.0,
    "tests/test_a.py::t2": 30.0,
    "tests/test_b.py::t": 50.0,
}
# The same with `test_c.py` at 800 s, a suite of 980 s whose bulk stands still
# while one file moves; the threshold goes to 800 to leave it unlisted.
CASES = {**SMALL, "tests/test_c.py::t": 800.0}


def docs_budget(*rows):
    return budgets(("docs-history", "lines", 0, "+0 lines", "gate")) + table(
        "Lines ceiling", rows
    )


def test_a_crlf_checkout_measures_the_bytes_an_lf_one_does(tmp_path):
    """A Windows checkout under `core.autocrlf` writes each line end as CRLF,
    and the same commit must measure the same there: a byte budget counts a
    CRLF as the one LF git stores, for an agent's files and for `CLAUDE.md`."""
    root = tree(
        tmp_path,
        budgets(warden(MEASURED), ("preload:claude-md", "bytes", 300, "2 %", "gate")),
    )
    for rel in ("agents/warden.md", "skills/review/SKILL.md"):
        path = root / rel
        path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
    (root / "CLAUDE.md").write_bytes(b"c" * 297 + b"\r\n\r\n\r\n")
    rows = {r.name: r for r in budget_check.budgets_here(str(root))}
    assert budget_check.measure(str(root), rows["preload:warden"], {}) == MEASURED
    assert budget_check.measure(str(root), rows["preload:claude-md"], {}) == 300
    assert run(root) == 0


def test_the_preload_measurer_sums_the_agents_files_and_not_the_pair(tmp_path):
    """T8: an agent's preload is its definition and the skills it names, and
    never the `CLAUDE.md` pair the harness adds — which the meter does see
    here, both halves of it under the tree. `preload:claude-md` is the
    repository's `CLAUDE.md` alone, by its bytes."""
    root = tree(
        tmp_path,
        budgets(warden(MEASURED), ("preload:claude-md", "bytes", 300, "2 %", "gate")),
        files={"CLAUDE.md": "c" * 300, ".claude/CLAUDE.md": "u" * 200},
    )
    rows = {r.name: r for r in budget_check.budgets_here(str(root))}
    assert budget_check.measure(str(root), rows["preload:warden"], {}) == MEASURED
    assert budget_check.measure(str(root), rows["preload:claude-md"], {}) == 300
    assert run(root) == 0


@pytest.mark.parametrize(
    "text, history",
    [
        ("Fixed in #123.\n", [1]),
        ("Found in round 2.\n", [1]),
        ("Read on 2026-10-14.\n", [1]),
        ("Measured once.\n", [1]),
        ("It was measured once.\n", [1]),
        ("A list item #5 is no issue number.\n", []),
        ("Prose.\n\n```\n#123\n```\n", []),
        ("Prose.\n\n<!-- #123\nround 2 -->\n", []),
        ("## The #123 rule\n", []),
        (
            "**The rule.** It says\nmore, #123.\nEnforced by: tests/x.py\nSee #456.\n",
            [4],
        ),
        ("**The rule.** #123 grounds it.\n\nThe story of #456.\n", [3]),
        ("One line" + LS + "of prose.\nSee #123.\n", [2]),
    ],
    ids=[
        "an issue number",
        "a round",
        "a date",
        "Measured",
        "measured",
        "one digit after a hash",
        "a fence",
        "a comment",
        "a heading",
        "a rule block to its Enforced by line",
        "a rule block to the end of its paragraph",
        "a line GitHub does not end at U+2028",
    ],
)
def test_the_docs_classifier_skips_fences_comments_headings_and_rule_blocks(
    text, history
):
    """T9, S8: a history line is a line outside a fence, a comment, a heading
    and a rule block that carries one of the four marks. Each exclusion is a
    case, each mark is a case, and a rule block with no `Enforced by:` line
    ends with its paragraph rather than swallowing the rest of the file."""
    assert budget_check.classify(text)[0] == history


def test_a_docs_file_that_gains_a_history_line_fails_naming_it_and_the_line(
    tmp_path, capsys
):
    """S8: a docs file listed at 0 that gains a line citing an issue fails,
    naming the file and the line; one the table does not list is held to the
    family's 0 the same way. The summary prints each document's history and
    rule lines."""
    text = "# Doc\n\nA rule.\nSee #812 for the story.\n"
    root = tree(
        tmp_path,
        docs_budget(("docs/listed.md", 0)),
        files={"docs/listed.md": text, "docs/unlisted.md": text},
    )
    assert run(root) == 1
    out = capsys.readouterr().out
    assert (
        "budget-check: docs-history:docs/listed.md: measured 1 lines is over the "
        "ceiling 0 by 1. Its history lines are at lines 4." in out
    ), out
    assert (
        "budget-check: docs-history: docs/unlisted.md is not listed and measures "
        "1 lines, over the 0 every file `## Docs history lines` does not list is "
        "held to. Its history lines are at lines 4." in out
    ), out
    assert "- `docs/listed.md`: 1 history · 0 rule" in out, out


@pytest.mark.parametrize(
    "rows, verdict, said",
    [
        ((), 1, "slow-file: tests/test_a.py is not listed and measures 130 seconds"),
        (
            (("tests/test_a.py", 125),),
            1,
            "measured 130 seconds is over the ceiling 125",
        ),
        ((("tests/test_a.py", 130),), 0, "every gate row holds"),
    ],
    ids=["unlisted over the threshold", "listed and grown", "listed and holding"],
)
def test_an_unlisted_file_over_the_threshold_fails_and_a_listed_one_may_not_grow(
    tmp_path, capsys, rows, verdict, said
):
    """T10, S7: a test file over the threshold that the table does not list
    fails, naming it; a listed one is held to its own ceiling."""
    root = tree(tmp_path, slow(*rows), files={".test_durations": json.dumps(SMALL)})
    assert run(root) == verdict
    assert said in capsys.readouterr().out


@pytest.mark.parametrize(
    "ceiling, verdict", [(181, 0), (180, 1)], ids=["at the sum", "one under"]
)
def test_the_suite_seconds_are_the_sum_of_every_priced_case(
    tmp_path, capsys, ceiling, verdict
):
    """`suite-seconds` sums every case `.test_durations` prices and rounds a
    half up: 100.25 and 80.25 seconds are 181."""
    cases = {"tests/test_a.py::t1": 100.25, "tests/test_b.py::t": 80.25}
    root = tree(
        tmp_path,
        budgets(("suite-seconds", "seconds", ceiling, "one-sided", "gate")),
        files={".test_durations": json.dumps(cases)},
    )
    assert run(root) == verdict, capsys.readouterr()


@pytest.mark.parametrize(
    "base, head, body, verdict",
    [
        (slow(), slow(("tests/test_a.py", 130)), "", 1),
        (
            slow(),
            slow(("tests/test_a.py", 130)),
            "Budget raised: slow-file:tests/test_a.py 120 -> 130: it grew",
            0,
        ),
        (
            slow(("tests/test_a.py", 130)),
            budgets(),
            "Budget removed: slow-file: gone",
            0,
        ),
    ],
    ids=["listed since the base, no line", "with its line", "the family removed"],
)
def test_a_file_row_is_held_at_its_familys_ceiling_at_the_base(
    tmp_path, capsys, base, head, body, verdict
):
    """A file row the base did not list was held there to its family's
    ceiling, so listing it above that is a raise from it and needs its line.
    A file row whose family row is gone needs no line of its own: the
    family's removal is the one."""
    root = tree(
        tmp_path, head, base=base, base_files={".test_durations": json.dumps(SMALL)}
    )
    assert ratchet(root, body) == verdict, capsys.readouterr()


def test_a_slow_file_is_reported_and_the_suite_seconds_are_gated(tmp_path, capsys):
    """Work item 1791876667, round 3's 🟡 2: one union of the Windows shards'
    parts moves a single test file 0.67 to 1.72 times the level from the
    next, past any band a one-sided ceiling of 1.3 holds, so this
    repository's `slow-file` rows are `report` rows and `suite-seconds` is
    its gate. Under the kind `seal/budgets.md` gives the family, a listed
    file over its ceiling is printed `over` and the run still holds."""
    rows = {row.name: row for row in budget_check.budgets_here(ROOT)}
    assert rows["suite-seconds"].kind == "gate"
    kind = rows["slow-file"].kind
    head = budgets(("slow-file", "seconds", 120, "one-sided", kind)) + table(
        "Seconds ceiling", [("tests/test_a.py", 125)]
    )
    root = tree(tmp_path, head, files={".test_durations": json.dumps(SMALL)})
    assert run(root) == 0
    out = capsys.readouterr().out
    assert (
        "| `slow-file:tests/test_a.py` | 130 seconds | 125 | -5 (-4.0%) | report | over |"
        in out
    ), out


def test_an_unlisted_slow_file_under_a_report_row_is_named(tmp_path, capsys):
    """Work item 1791876667, round 5's 🟡 3: a test file that crosses the
    threshold unlisted under a `report` family fails nothing, and the summary
    still names it, because the family's own line reads only the largest
    unlisted value and the path is in the row's problem alone. Neither that
    problem nor a listed file's asks for a `Budget raised:` line, which
    `ratchet` reads for a gate row alone."""
    head = budgets(("slow-file", "seconds", 120, "one-sided", "report")) + table(
        "Seconds ceiling", [("tests/test_b.py", 40)]
    )
    root = tree(tmp_path, head, files={".test_durations": json.dumps(SMALL)})
    assert run(root) == 0
    out = capsys.readouterr().out
    assert "Report rows past their band, failing nothing:" in out, out
    assert (
        "- `slow-file`: tests/test_a.py is not listed and measures 130 seconds" in out
    ), out
    assert "list it there; a report row's listing needs no `Budget raised:` line" in out
    assert (
        "- `slow-file:tests/test_b.py`: measured 50 seconds is over the ceiling 40 "
        "by 10. Bring it back under, or raise the ceiling in seal/budgets.md; a "
        "report row's raise needs no `Budget raised:` line" in out
    ), out
    assert "pull request body" not in out, out


def priced(scale, only=None):
    """`CASES` with every case, or the cases of the file `only`, multiplied."""
    return {
        case: seconds * (scale if only is None or case.startswith(only) else 1)
        for case, seconds in CASES.items()
    }


RESCALED = slow(("tests/test_a.py", 130), threshold=800, suite=(980, "one-sided"))


def price(per_mille):
    """The `## Price level` table stating `.test_durations` at `per_mille`."""
    return (
        "\n## Price level\n\n| Prices | Per mille |\n|---|---|\n"
        f"| .test_durations | {per_mille} |\n"
    )


def refreshed(tmp_path, cases, head):
    """A tree whose base holds `CASES` under `RESCALED` and whose HEAD holds
    `cases` under `head`."""
    return tree(
        tmp_path,
        head,
        base=RESCALED,
        base_files={".test_durations": json.dumps(CASES)},
        files={".test_durations": json.dumps(cases)},
    )


def test_a_uniform_rescale_of_the_durations_holds_every_row(tmp_path, capsys):
    """A refresh that prices the same cases 1.07 times higher moves no row
    once it restates the price level to 1070: the seconds rows are read in
    the prices their ceilings are written in, and the summary says the raw
    value, the ratio measured against the base and the level divided by."""
    root = refreshed(tmp_path, priced(1.07), RESCALED + price(1070))
    assert ratchet(root, "") == 0
    out = capsys.readouterr().out
    assert "prices the 4 cases it shares with the base x1.070 the base's" in out, out
    assert "divided by the price level x1.070" in out, out
    assert "| `suite-seconds` | 980 seconds (raw 1,049 at x1.070) |" in out, out


@pytest.mark.parametrize(
    "cases, level, said",
    [
        (priced(1.07), 1000, "1000 x 1.070 = 1070 per mille, and `## Price level`"),
        (CASES, 1070, "1000 x 1.000 = 1000 per mille, and `## Price level`"),
    ],
    ids=["a refresh that does not restate it", "a level moved with no refresh"],
)
def test_the_price_level_follows_the_durations_file_and_nothing_else(
    tmp_path, capsys, cases, level, said
):
    """The level is the one number a refresh restates, and the check names
    it. It cannot move unless the file did: a level raised over an unchanged
    file would loosen every seconds row without a `Budget raised:` line."""
    root = refreshed(tmp_path, cases, RESCALED + price(level))
    assert ratchet(root, "") == 1
    out = capsys.readouterr().out
    first = next(line for line in out.splitlines() if line.startswith("budget-check:"))
    assert first.startswith("budget-check: price level: ") and said in first, out


def test_restate_price_writes_the_level_a_refresh_implies(tmp_path, capsys):
    """Work item 1791876667, round 3's 🟡 1: committing a union used to
    fail until a person copied the level out of the run's message.
    `--restate-price` writes the number the check would have named into the
    one row of `## Price level`, changes no other line, and the run that
    wrote it holds, as the hygiene workflow's step will on that commit."""
    root = refreshed(tmp_path, priced(1.07), RESCALED + price(1000))
    assert ratchet(root, "", "--restate-price") == 0, capsys.readouterr()
    written = (root / "seal" / "budgets.md").read_text("utf-8")
    assert written == RESCALED + price(1070), written
    out = capsys.readouterr().out
    assert (
        "`--restate-price` wrote 1070 per mille into `## Price level` of "
        "`seal/budgets.md`; commit it with the file." in out
    ), out
    assert ratchet(root, "") == 0, capsys.readouterr()


@pytest.mark.parametrize(
    "head, args, said",
    [
        (
            RESCALED + price(1000),
            ("--restate-price",),
            "--restate-price was given without --baseline",
        ),
        (
            RESCALED,
            ("--baseline", "base", "--restate-price"),
            "--restate-price has no `## Price level` table",
        ),
    ],
    ids=["no baseline", "no table to write into"],
)
def test_restate_price_with_nothing_to_restate_against_or_into_is_exit_2(
    tmp_path, capsys, head, args, said
):
    """The level written is the base's times the file's move, so with no
    baseline there is nothing to write; and a tree with no `## Price level`
    table has no row to write it into. Both are exit 2 naming why, and the
    file is left as it was."""
    root = refreshed(tmp_path, priced(1.07), head)
    assert run(root, *args) == 2
    assert said in capsys.readouterr().err
    assert (root / "seal" / "budgets.md").read_text("utf-8") == head


def test_a_refreshed_file_holds_at_the_next_pull_request(tmp_path, capsys):
    """After a refresh lands with its level, the next pull request's base
    holds the refreshed file: the ratio is 1 and the rows are read at the
    level that refresh wrote, so the refresh fails nothing downstream."""
    head = RESCALED + price(1070)
    root = tree(
        tmp_path,
        head,
        base=head,
        base_files={".test_durations": json.dumps(priced(1.07))},
    )
    assert ratchet(root, "") == 0, capsys.readouterr()
    assert run(root) == 0


def test_a_file_doubling_against_the_rest_still_fails_its_row(tmp_path, capsys):
    """One file twice as slow while the rest stand still is composition, not
    price: the median over the files stays at 1, the level at 1000, and the
    file reads its 260 seconds against its 130. The suite grew by those 130
    seconds too, so its row says so; no price level is asked for."""
    root = refreshed(
        tmp_path, priced(2, only="tests/test_a.py"), RESCALED + price(1000)
    )
    assert ratchet(root, "") == 1
    out = capsys.readouterr().out
    assert (
        "budget-check: slow-file:tests/test_a.py: measured 260 seconds is over "
        "the ceiling 130" in out
    ), out
    assert "budget-check: suite-seconds: measured 1,110 seconds is over" in out, out
    assert "budget-check: price level:" not in out, out


@pytest.mark.parametrize(
    "before, said",
    [
        ({"tests/test_z.py::t": 10.0}, "share no case id"),
        ({case: 0.0 for case in CASES}, "prices no test file at 10 seconds"),
        (None, None),
    ],
    ids=["no case in common", "the base prices them at nothing", "no file at the base"],
)
def test_a_price_level_that_cannot_be_read_is_exit_2(tmp_path, capsys, before, said):
    """No case id in common, or a base pricing the common ones at 0, leaves
    no level to divide by, and the run says so rather than comparing raw
    seconds. A base with no durations file at all has nothing to price
    against, and the rows are read as they stand."""
    root = tree(
        tmp_path,
        RESCALED,
        base=RESCALED,
        base_files=None if before is None else {".test_durations": json.dumps(before)},
        files={".test_durations": json.dumps(CASES)},
    )
    if said is None:
        assert ratchet(root, "") == 0, capsys.readouterr()
        return
    assert ratchet(root, "") == 2
    assert said in capsys.readouterr().err


SUITE = budgets(("suite-seconds", "seconds", 180, "one-sided", "gate"))


@pytest.mark.parametrize(
    "head, files, said",
    [
        (
            budgets(warden(MEASURED)) + table("Seconds ceiling", []),
            {},
            "and no `slow-file` row in its Budgets table",
        ),
        (
            budgets(("slow-file", "seconds", 120, "one-sided", "gate")),
            {},
            "has a `slow-file` row and no `## Slow test files` table",
        ),
        (slow(("tests/test_a.py", 1), ("tests/test_a.py", 1)), {}, "is written twice"),
        (slow(("tests/test_a.py", "1,0")), {}, "is not a whole number"),
        (slow(("tests/a b.py", 1)), {}, "is no file name"),
        (
            budgets(("slow-file", "bytes", 120, "one-sided", "gate"))
            + table("Seconds ceiling", []),
            {".test_durations": json.dumps(SMALL)},
            "the unit is `bytes`, and slow-file is measured in seconds",
        ),
        (SUITE, {}, ".test_durations is not in the tree"),
        (SUITE, {".test_durations": "{"}, ".test_durations is not JSON"),
        (
            SUITE,
            {".test_durations": '{"tests/test_a.py::t": "slow"}'},
            "is not an object of case ids to seconds",
        ),
        (
            slow(("tests/test_z.py", 1)),
            {".test_durations": json.dumps(SMALL)},
            "tests/test_z.py is not in .test_durations",
        ),
        (docs_budget(("docs/gone.md", 0)), {}, "docs/gone.md is not in docs/"),
        (
            budgets(("preload:claude-md", "bytes", 1, "2 %", "gate")),
            {},
            "CLAUDE.md is not in the tree",
        ),
        (
            SUITE + price("1,070"),
            {".test_durations": json.dumps(SMALL)},
            "`## Price level` table is not one row",
        ),
        (
            SUITE + price(1000) + "| .test_durations | 1000 |\n",
            {".test_durations": json.dumps(SMALL)},
            "`## Price level` table is not one row",
        ),
    ],
    ids=[
        "a file table with no family row",
        "a family row with no file table",
        "a file twice",
        "a file ceiling with a comma",
        "a file name with a space",
        "a family row in another unit",
        "no durations file",
        "a durations file that is no JSON",
        "durations that are not seconds",
        "a listed test file the durations do not price",
        "a listed document the tree lacks",
        "no CLAUDE.md",
        "a price level with a comma",
        "a price level written twice",
    ],
)
def test_a_family_that_cannot_be_read_is_exit_2(tmp_path, capsys, head, files, said):
    """S11 for the per-file families and the files they read: a table and its
    family row come together, a row names a file that is there, and a
    durations file or a `CLAUDE.md` that is missing or unreadable stops the
    run naming it — never 0, never a reading of nothing."""
    root = tree(tmp_path, head, files=files)
    assert run(root) == 2
    assert said in capsys.readouterr().err


# --- phase 3: the minutes of one run --------------------------------------


def job(name, minutes, runner="GitHub Actions 1000014373"):
    """One job of a run as `gh api …/jobs --jq '.jobs[]'` prints it: the
    runner's name carries no operating system, as GitHub's does not."""
    start = datetime.datetime(2026, 10, 13, 22, 0, 0, tzinfo=datetime.UTC)
    end = start + datetime.timedelta(minutes=minutes)
    return {
        "name": name,
        "runner_name": runner,
        "status": "completed",
        "conclusion": "success",
        "started_at": start.isoformat().replace("+00:00", "Z"),
        "completed_at": end.isoformat().replace("+00:00", "Z"),
    }


# ubuntu 6.5, windows 20.2 + 21.3, macOS 7.0 + 7.4 + 8.1 minutes, and two
# jobs that run no suite.
RUN = [
    job("lint", 0.3),
    job("pytest (ubuntu-latest, 3.12, 15)", 6.5),
    job("pytest (windows-latest, 3.12, --splits 4 --group 1, 20)", 20.2),
    job("pytest (windows-latest, 3.12, --splits 4 --group 2, 20)", 21.3),
    job("pytest (macos-latest, 3.12, --splits 3 --group 1, 15)", 7.0),
    job("pytest (macos-latest, 3.12, --splits 3 --group 2, 15)", 7.4),
    job("pytest (macos-latest, 3.12, --splits 3 --group 3, 15)", 8.1),
    job("budgets", 0.8),
]


def minutes(ubuntu=15, windows=59, macos=32, extra=()):
    rows = [
        ("ci-minutes:ubuntu", "minutes", ubuntu, "one-sided", "gate"),
        ("ci-minutes:windows", "minutes", windows, "one-sided", "gate"),
        ("ci-minutes:macos", "minutes", macos, "one-sided", "gate"),
    ]
    return budgets(*rows, *extra)


def jobs_file(tmp_path, jobs, raw=None):
    path = tmp_path / "jobs.jsonl"
    path.write_text(
        raw if raw is not None else "".join(json.dumps(j) + "\n" for j in jobs),
        "utf-8",
    )
    return str(path)


@pytest.mark.parametrize(
    "ceilings, verdict, said",
    [
        (
            {},
            0,
            "| `ci-minutes:windows` | 41.5 minutes | 59 | 17.5 (29.7%) | gate | holds |",
        ),
        (
            {"windows": 40},
            1,
            "budget-check: ci-minutes:windows: measured 41.5 minutes is over the "
            "ceiling 40 by 1.5",
        ),
        ({"macos": 100}, 0, "| `ci-minutes:macos` | 22.5 minutes | 100 |"),
    ],
    ids=["under every ceiling", "one leg over", "far under, and no lower band"],
)
def test_ci_minutes_sum_each_leg_off_the_job_name_and_price_the_run(
    tmp_path, capsys, ceilings, verdict, said
):
    """T11, S9: each leg is the sum of its pytest jobs' minutes, the leg read
    off the job's name; a leg over its ceiling fails and one far under it
    holds, because a run's row has no lower band. The billable line rounds
    each job up to its minute and prices Windows at 2 and macOS at 10 Linux
    minutes, labelled with its price's date as unverified."""
    root = tree(tmp_path, minutes(**ceilings))
    assert run(root, "--ci-jobs", jobs_file(tmp_path, RUN)) == verdict
    out = capsys.readouterr().out
    assert said in out, out
    assert (
        "Billable: macos 24 x 10 + ubuntu 7 x 1 + windows 43 x 2 = 333 "
        "Linux-equivalent minutes, US$2.66 at $0.008 a Linux minute — the price "
        "#929 read in mid-2026, its date unverified: check it against GitHub's "
        "Actions price list before quoting the dollars." in out
    ), out


def test_a_leg_no_multiple_is_known_for_gets_no_billable_total(tmp_path, capsys):
    """A leg the billing table has no multiple for is named rather than
    priced at a guess."""
    root = tree(tmp_path, minutes())
    jobs = [*RUN, job("pytest (freebsd-latest, 3.12, 15)", 3.0)]
    assert run(root, "--ci-jobs", jobs_file(tmp_path, jobs)) == 0
    assert (
        "Billable: no multiple is known for the freebsd leg" in capsys.readouterr().out
    )


def test_a_run_row_is_shown_unread_on_the_tree_and_held_off_its_run(tmp_path, capsys):
    """The tree's run cannot read a run's minutes, so it shows those rows
    unread and holds the rest; the `budgets` job reads the run and holds
    those rows alone, so a tree row it did not measure fails nothing there."""
    root = tree(tmp_path, minutes(windows=1, extra=[warden(MEASURED - 1)]))
    assert run(root) == 1
    out = capsys.readouterr().out
    assert (
        "| `ci-minutes:windows` | — (read off each run by the tests workflow's" in out
    )
    assert "| not this run |" in out and "ci-minutes:windows: measured" not in out
    assert run(root, "--ci-jobs", jobs_file(tmp_path, RUN)) == 1
    out = capsys.readouterr().out
    assert "budget-check: ci-minutes:windows: measured 41.5" in out, out
    assert "preload:warden" not in out, out


NO_TIMES = {**job("pytest (macos-latest, 3.12, 15)", 1), "completed_at": None}


@pytest.mark.parametrize(
    "head, jobs, raw, said",
    [
        (
            budgets(("ci-minutes:ubuntu", "minutes", 15, "10 %", "gate")),
            None,
            None,
            "a row read off one run — a CI run's minutes, or `.test_durations`",
        ),
        (
            budgets(warden(MEASURED, "one-sided")),
            None,
            None,
            "only a row read off one run or a `report` row is `one-sided`",
        ),
        (
            budgets(("ci-minutes:freebsd", "minutes", 15, "one-sided", "gate")),
            None,
            None,
            "no leg of the tests workflow is called `freebsd`",
        ),
        (
            budgets(("ci-minutes", "minutes", 15, "one-sided", "gate")),
            None,
            None,
            "no leg of the tests workflow is called ``",
        ),
        (
            budgets(("ci-minutes:ubuntu", "seconds", 15, "one-sided", "gate")),
            None,
            None,
            "the unit is `seconds`, and ci-minutes is measured in minutes",
        ),
        (minutes(), "missing", None, "the job list jobs.jsonl is not there"),
        (minutes(), RUN, "{\n", "line 1 of the job list is not JSON"),
        (minutes(), RUN, "[1]\n", "line 1 of the job list is no job with a name"),
        (minutes(), [*RUN, NO_TIMES], None, "has no start and end time"),
        (minutes(), RUN[:4], None, "no pytest job of this run ran on macos"),
        (budgets(warden(MEASURED)), RUN, None, "has no row read off a run"),
    ],
    ids=[
        "a run row with a lower band",
        "a tree row with none",
        "an unknown leg",
        "a run row with no leg",
        "a run row in another unit",
        "no job list",
        "a job list that is no JSON",
        "a line that is no job",
        "a pytest job with no end",
        "a leg the run did not run",
        "a job list with no run row to hold",
    ],
)
def test_a_run_that_cannot_be_read_is_exit_2(tmp_path, capsys, head, jobs, raw, said):
    """S11 for the run's rows: a lower band on a row one run measures, or
    none on a row the tree measures, an unknown leg, a job list that is not
    there or not read, a pytest job not yet ended, a leg the run lacks, and a
    job list read for no row are each exit 2 naming it."""
    root = tree(tmp_path, head)
    args = ()
    if jobs == "missing":
        args = ("--ci-jobs", str(tmp_path / "jobs.jsonl"))
    elif jobs is not None:
        args = ("--ci-jobs", jobs_file(tmp_path, jobs, raw))
    assert run(root, *args) == 2
    assert said in capsys.readouterr().err


def workflow_code(name):
    with open(os.path.join(ROOT, ".github", "workflows", name), encoding="utf-8") as f:
        return "\n".join(conftest.code_lines(f.read()))


def job_block(text, name):
    """The code lines of one job under `jobs:`, to the next job's key."""
    match = re.search(rf"^  {name}:\n((?:(?!  [A-Za-z0-9_-]+:\n).*\n?)*)", text, re.M)
    assert match, f"no `{name}` job"
    return match.group(1)


def test_the_workflows_run_the_checker_where_the_plan_says():
    """T14, S5, S9: the hygiene step reads the merge base, the base branch
    and the body; the `budgets` job runs after every pytest leg whatever its
    verdict, with a token that reads the run's jobs, and hands their list to
    the checker."""
    step = conftest.workflow_step(
        workflow_code("hygiene.yml"),
        "every budget holds its ceiling, and a raised ceiling says why",
    )
    for part in (
        ".github/scripts/budget_check.py",
        '--baseline "origin/${{ github.base_ref }}"',
        '--base-ref "${{ github.base_ref }}"',
        "--pr-body-env PR_BODY",
        "PR_BODY: ${{ github.event.pull_request.body }}",
        '--trend "$(git describe --tags --abbrev=0 "origin/${{ github.base_ref }}")"',
    ):
        assert part in step, part
    budgets_job = job_block(workflow_code("test.yml"), "budgets")
    for part in (
        "    needs: pytest\n",
        "    if: ${{ !cancelled() }}\n",
        "      actions: read\n",
        "GH_TOKEN: ${{ github.token }}",
        "/actions/runs/${{ github.run_id }}/jobs",
        "--paginate --jq '.jobs[]'",
        "budget_check.py --ci-jobs",
    ):
        assert part in budgets_job, part


# --- phase 4: the two reports and the trend ---------------------------------


def rounds_budget(ceiling=10):
    return budgets(("rounds-bytes", "bytes", ceiling, "one-sided", "report"))


def test_the_largest_round_record_is_reported_and_never_fails(tmp_path, capsys):
    """`rounds-bytes` is the largest work item's `rounds/` in the tree, each
    work item's listed largest first, and a report: over its ceiling it says
    so and fails nothing, because no pull request has a fix for a record the
    review chain wrote."""
    root = tree(
        tmp_path,
        rounds_budget(),
        files={
            "seal/specs/1-small/rounds/round-1.md": "b" * 49 + "\n",
            "seal/specs/2-large/rounds/round-1.md": "a" * 99 + "\n",
            "seal/specs/2-large/rounds/round-2.md": "a" * 199 + "\n",
            "seal/specs/3-none/spec.md": "c" * 999 + "\n",
        },
    )
    assert run(root) == 0
    out = capsys.readouterr().out
    assert (
        "| `rounds-bytes` | 300 bytes | 10 | -290 (-2900.0%) | report | over |" in out
    )
    assert (
        "- `2-large`: 300 bytes over 2 files\n- `1-small`: 50 bytes over 1 files\n"
        in out
    ), out
    assert "`3-none`" not in out, out


def test_a_trend_sets_each_budget_beside_its_ceiling_at_the_tag(tmp_path, capsys):
    """`--trend <tag>` prints one line per budget against the tag's file: a
    ceiling then and now with today's reading, a row new since then, and a
    row gone since then."""
    then = budgets(warden(MEASURED), ("preload:scout", "bytes", 500, "2 %", "gate"))
    now = budgets(warden(1010), ("rounds-bytes", "bytes", 500, "one-sided", "report"))
    root = tree(tmp_path, now, base=then)
    git(root, "tag", "v1", "base")
    assert run(root, "--trend", "v1") == 0
    out = capsys.readouterr().out
    assert "Against v1, one line per budget:" in out, out
    assert (
        "- `preload:warden`: ceiling 1,000; ceiling 1,010, measured 1,000 bytes" in out
    ), out
    assert "- `rounds-bytes`: new since then; ceiling 500, measured 0 bytes" in out, out
    assert "- `preload:scout`: gone since then" in out, out


@pytest.mark.parametrize(
    "tag, said",
    [("", "--trend names no tag"), ("v9", "git could not list seal/budgets.md at v9")],
    ids=["an empty tag", "a tag that names nothing"],
)
def test_a_trend_that_names_no_release_is_exit_2(tmp_path, capsys, tag, said):
    """The hygiene step hands `git describe`'s answer over; a base with no
    tag hands an empty one, and the run refuses it rather than printing no
    trend."""
    root = tree(tmp_path, budgets(warden(MEASURED)), base=budgets(warden(MEASURED)))
    assert run(root, "--trend", tag) == 2
    assert said in capsys.readouterr().err


# --- round 1's fixes ---------------------------------------------------------


def test_an_unread_row_of_a_family_without_an_unread_reason_renders(
    tmp_path, capsys, monkeypatch
):
    """A family another work item adds may read nothing on a run; the
    summary shows it unread with a reason of its own rather than raising."""
    monkeypatch.setitem(
        budget_check.MEASURERS, "later", (lambda _root, _s, _cache: None, "rows", False)
    )
    root = tree(tmp_path, budgets(("later", "rows", 4, "one-sided", "report")))
    assert run(root) == 0
    assert "| `later` | — (not read on this run) | 4 |" in capsys.readouterr().out


@pytest.mark.parametrize(
    "aside",
    ["```\n## an example heading\n```\n", "<!--\n## not a heading either\n-->\n"],
    ids=["a fenced line", "a commented line"],
)
def test_a_fenced_heading_inside_a_file_section_does_not_end_it(
    tmp_path, capsys, aside
):
    """A `##` line inside a fence or a comment is no heading GitHub shows,
    so it does not end the section its family's table stands in."""
    head = (
        budgets(("docs-history", "lines", 0, "+0 lines", "gate"))
        + "\n## Docs history lines\n\n"
        + aside
        + "\n| File | Lines ceiling |\n|---|---|\n| docs/a.md | 0 |\n"
    )
    root = tree(tmp_path, head, files={"docs/a.md": "# A\n\nProse.\n"})
    assert run(root) == 0, capsys.readouterr()
    assert "| `docs-history:docs/a.md` | 0 lines | 0 |" in capsys.readouterr().out


def test_a_file_section_written_twice_is_refused(tmp_path, capsys):
    """Two `## Slow test files` sections are two tables nobody can say is
    the one, so the run refuses rather than reading the first."""
    head = slow(("tests/test_a.py", 200)) + table(
        "Seconds ceiling", [("tests/test_b.py", 60)]
    )
    root = tree(tmp_path, head, files={".test_durations": json.dumps(SMALL)})
    assert run(root) == 2
    assert "`## Slow test files` stands 2 times" in capsys.readouterr().err


def test_a_per_file_family_reads_its_own_table_with_its_own_reader(
    tmp_path, capsys, monkeypatch
):
    """A per-file family another work item adds is one `FILE_TABLES` entry,
    carrying the reader that measures it, and its table is the one under its
    own heading — even where it shares the docs table's header."""
    monkeypatch.setitem(
        budget_check.FILE_TABLES,
        "test-lines",
        budget_check.FileFamily(
            "Test lines",
            ("File", "Lines ceiling"),
            "lines",
            lambda _root, _cache: {"tests/test_a.py": 7},
        ),
    )
    head = (
        budgets(
            ("docs-history", "lines", 0, "+0 lines", "gate"),
            ("test-lines", "lines", 0, "+0 lines", "gate"),
        )
        + table("Lines ceiling", [("docs/a.md", 0)])
        + "\n## Test lines\n\n| File | Lines ceiling |\n|---|---|\n"
        + "| tests/test_a.py | 7 |\n"
    )
    root = tree(tmp_path, head, files={"docs/a.md": "# A\n\nProse.\n"})
    assert run(root) == 0, capsys.readouterr()
    out = capsys.readouterr().out
    assert "| `test-lines:tests/test_a.py` | 7 lines | 7 |" in out, out
    assert "| `docs-history:docs/a.md` | 0 lines | 0 |" in out, out


@pytest.mark.parametrize(
    "base, head, body, verdict, said",
    [
        (
            budgets(warden(MEASURED)),
            budgets(warden(MEASURED, "50 %")),
            "",
            1,
            "the slack was widened from 2 % to 50 %",
        ),
        (
            budgets(warden(MEASURED)),
            budgets(warden(MEASURED, "50 %")),
            "Budget raised: preload:warden 1000 -> 1000: a wider band",
            0,
            "- `preload:warden` raised 1000 -> 1000, slack 2 % -> 50 %: a wider band",
        ),
        (
            budgets(warden(MEASURED, "50 %")),
            budgets(warden(MEASURED)),
            "",
            0,
            "every gate row holds",
        ),
        (
            docs_budget(("docs/a.md", 0)),
            budgets(("docs-history", "lines", 0, "+5 lines", "gate"))
            + table("Lines ceiling", [("docs/a.md", 0)]),
            "",
            1,
            "budget-check: docs-history: the slack was widened from +0 lines to +5 lines",
        ),
    ],
    ids=["widened, no line", "widened, with its line", "narrowed", "a family's slack"],
)
def test_a_widened_slack_on_a_gate_row_needs_its_line(
    tmp_path, capsys, base, head, body, verdict, said
):
    """A wider slack lets a ceiling sit further over its reading, which is
    the headroom the lower band exists to take back; so it is a raise and
    needs its line, as a higher ceiling does. A narrower one needs none, and
    a family's slack is one raise, not one per file it gives it to."""
    root = tree(tmp_path, head, base=base, files={"docs/a.md": "# A\n\nProse.\n"})
    assert ratchet(root, body) == verdict
    out = capsys.readouterr().out
    assert said in out, out
    assert "docs-history:docs/a.md: the slack" not in out, out


THREE = {
    "tests/test_a.py::a1": 600.0,
    "tests/test_a.py::a2": 400.0,
    "tests/test_b.py::b": 500.0,
    "tests/test_c.py::c": 200.0,
}
THREE_BUDGETS = slow(
    ("tests/test_a.py", 1300),
    ("tests/test_b.py", 650),
    ("tests/test_c.py", 260),
    suite=(2210, "one-sided"),
)


def test_files_too_small_to_say_how_the_runners_moved_leave_the_level_alone(
    tmp_path, capsys
):
    """A test file the base prices under 10 seconds is out of the level's
    median: three one-second files tripling on a refresh say nothing about
    the runners, and the 1,000 seconds that did not move keep the level at
    1000."""
    before = {**THREE, **{f"tests/test_tiny{n}.py::t": 1.0 for n in range(5)}}
    after = {**THREE, **{f"tests/test_tiny{n}.py::t": 3.0 for n in range(5)}}
    root = tree(
        tmp_path,
        THREE_BUDGETS,
        base=THREE_BUDGETS,
        base_files={".test_durations": json.dumps(before)},
        files={".test_durations": json.dumps(after)},
    )
    assert ratchet(root, "") == 0, capsys.readouterr()


@pytest.mark.parametrize(
    "old, new, wider",
    [
        ("2 %", "one-sided", True),
        ("2 %", "5 %", True),
        ("5 %", "2 %", False),
        ("+0", "+1", True),
        ("one-sided", "2 %", False),
    ],
)
def test_one_sided_is_the_widest_slack(old, new, wider):
    """A move to `one-sided` lifts the lower band altogether, the widest a
    slack can go, and a move away from it narrows."""
    slack = lambda cell: budget_check.parse_slack(cell, "bytes")
    assert budget_check.widened(slack(old), slack(new), 1000) is wider


def test_a_cleanup_of_one_file_under_shared_ids_holds_the_untouched_rows(
    tmp_path, capsys
):
    """A pull request that halves the heaviest of three files under the same
    case ids is a cleanup, not a change of runners: the level stays at 1000,
    the untouched files read what they read, and the one that got faster
    reads faster. Under a seconds-weighted level the same refresh moved to
    0.706 and read both untouched files over their ceilings."""
    faster = {**THREE, "tests/test_a.py::a1": 300.0, "tests/test_a.py::a2": 200.0}
    root = tree(
        tmp_path,
        THREE_BUDGETS,
        base=THREE_BUDGETS,
        base_files={".test_durations": json.dumps(THREE)},
        files={".test_durations": json.dumps(faster)},
    )
    assert ratchet(root, "") == 0, capsys.readouterr()
    out = capsys.readouterr().out
    assert "| `slow-file:tests/test_b.py` | 500 seconds | 650 |" in out, out
    assert "| `slow-file:tests/test_a.py` | 500 seconds | 1,300 |" in out, out


@pytest.mark.parametrize(
    "head",
    [
        budgets(("suite-seconds", "seconds", 100, "5 %", "gate")),
        budgets(("slow-file", "seconds", 120, "10 %", "gate"))
        + table("Seconds ceiling", []),
    ],
    ids=["the suite's row", "the slow files' row"],
)
def test_a_seconds_row_with_a_lower_band_is_refused(tmp_path, capsys, head):
    """A seconds row is read off one run's union, as a minutes row is off one
    run, so it is one-sided: a lower band on it would fail every refresh
    that moves a file against the rest."""
    root = tree(tmp_path, head, files={".test_durations": json.dumps(SMALL)})
    assert run(root) == 2
    assert "a row read off one run — a CI run's minutes, or `.test_durations`" in (
        capsys.readouterr().err
    )


def test_the_unknown_family_refusal_names_every_family(tmp_path, capsys):
    """A misspelt family is told every family the checker reads, the list
    derived from the families themselves, so a family added later is in it."""
    root = tree(tmp_path, budgets(("rounds-byte", "bytes", 1, "one-sided", "report")))
    assert run(root) == 2
    err = capsys.readouterr().err
    for family in [
        *budget_check.MEASURERS,
        *budget_check.FILE_TABLES,
        *budget_check.PER_RUN,
    ]:
        assert f"`{family}" in err, (family, err)


# --- #944: a rule names what holds it, and the count of those that do not ---
#
# `seal/specs/1791940762-the-record-of-truth-is-tests-not-coordinates/spec.md`
# §*The replacement*: every `Enforced by:` target in a rule file resolves
# (`enforced-unresolved`, ceiling 0), and each rule file's rule paragraphs with
# no enforcer, or `nothing — <why>`, are a two-sided `+0` row
# (`unenforced:<file>`). The fixture's own agent and skill hold no rule
# paragraph, so every count below is the docs file's.

HELD = "tests/test_x.py"
HELD_CASE = f"{HELD}::test_held"
TESTS = {HELD: "def test_held():\n    pass\n\n\nCONSTANT = 1\n"}


def rules_budget(*rows):
    """Budgets with the two rows of #944 and an `## Unenforced rules` table
    listing `rows`, each `(file, ceiling)`."""
    head = budgets(
        ("enforced-unresolved", "targets", 0, "+0", "gate"),
        ("unenforced", "rules", 0, "+0 rules", "gate"),
    )
    lines = ["", "## Unenforced rules", "", "| File | Rules ceiling |", "|---|---|"]
    lines += [f"| {path} | {ceiling} |" for path, ceiling in rows]
    return head + "\n".join(lines) + "\n"


def rule(enforced=None, opener="**"):
    """One rule paragraph, closed by `Enforced by: <enforced>` where given."""
    text = f"{opener}A rule.** Its one why.\n"
    return text if enforced is None else text + f"Enforced by: {enforced}\n"


def doc(*paragraphs):
    """A docs file whose paragraphs stand under `## The heading`, from line 5."""
    return "# D\n\n## The heading\n\n" + "\n".join(paragraphs)


@pytest.mark.parametrize(
    "target, verdict, said",
    [
        (
            "tests/test_x.py::test_gone",
            1,
            "docs/a.md:6 §*The heading*: tests/test_x.py::test_gone: no def or "
            "class named test_gone in tests/test_x.py",
        ),
        ("tests/test_gone.py", 1, "tests/test_gone.py does not exist"),
        (
            "tests/test_x.py::CONSTANT",
            1,
            "no def or class named CONSTANT in tests/test_x.py",
        ),
        (f"{HELD}, tests/test_gone.py", 1, "tests/test_gone.py does not exist"),
        (HELD_CASE, 0, "every gate row holds"),
        (f"{HELD_CASE}, {HELD}", 0, "every gate row holds"),
        ("nothing", 1, "nothing does not exist"),
    ],
    ids=[
        "a case gone",
        "a file gone",
        "a constant",
        "one of two",
        "a case",
        "two",
        "nothing with no why",
    ],
)
def test_an_enforced_by_target_that_does_not_resolve_fails_naming_where(
    tmp_path, capsys, target, verdict, said
):
    """S1: a target that is gone, or names a constant, is exit 1 naming the
    file, the `Enforced by:` line, the heading it stands under and why; a
    target that resolves holds. Every target of the line is read, not the
    first, and a `nothing` with no `— <why>` is read as a target."""
    files = {"docs/a.md": doc(rule(target)), **TESTS}
    root = tree(tmp_path, rules_budget(), files=files)
    assert run(root) == verdict
    out = capsys.readouterr().out
    assert said in out, out
    if verdict:
        assert "enforced-unresolved: measured 1 targets is over the ceiling 0" in out


def test_an_enforced_by_line_outside_a_rule_or_inside_a_fence_is_read_or_skipped(
    tmp_path, capsys
):
    """S1's reach: every `Enforced by:` line a renderer shows is resolved,
    inside a rule paragraph or not, in every rule file; one in a fence is an
    example and is not."""
    text = doc(
        "A sentence that states no rule.\nEnforced by: tests/test_gone_a.py\n",
        "```\nEnforced by: tests/test_gone_b.py\n```\n",
    )
    files = {"agents/warden.md": AGENT_HEAD + text, **TESTS}
    root = tree(tmp_path, rules_budget(), files=files)
    assert run(root) == 1
    out = capsys.readouterr().out
    assert (
        "agents/warden.md:11 §*The heading*: tests/test_gone_a.py does not exist" in out
    )
    assert "test_gone_b" not in out, out


@pytest.mark.parametrize(
    "files, verdict, said",
    [
        ({"case.yaml": "name: a\n"}, 0, "every gate row holds"),
        ({"prompt.md": "Review.\n"}, 1, "holds no case.yaml"),
    ],
    ids=["with its case.yaml", "without"],
)
def test_an_eval_case_directory_resolves_where_its_case_yaml_is(
    tmp_path, capsys, files, verdict, said
):
    """S2: an agent's rule can be held by an eval case alone, so
    `evals/behaviour/<agent>/<case>/` is a target, resolving where the
    directory holds `case.yaml`."""
    case = "evals/behaviour/warden/a-case/"
    written = {"docs/a.md": doc(rule(case))}
    written.update({case + name: text for name, text in files.items()})
    root = tree(tmp_path, rules_budget(), files=written)
    assert run(root) == verdict
    assert said in capsys.readouterr().out


def test_an_eval_target_that_names_no_case_is_refused(tmp_path, capsys):
    """S2's grammar: the directory is `<agent>/<case>/`, so an agent's
    directory alone names no case and does not resolve."""
    written = {
        "docs/a.md": doc(rule("evals/behaviour/warden/")),
        "evals/behaviour/warden/case.yaml": "name: a\n",
    }
    root = tree(tmp_path, rules_budget(), files=written)
    assert run(root) == 1
    assert "is no eval case: write `evals/behaviour/<agent>/<case>/`" in (
        capsys.readouterr().out
    )


def test_a_new_rule_without_a_test_raises_its_files_row(tmp_path, capsys):
    """S3: a bold-led paragraph with no `Enforced by:` appended to a file at
    its ceiling is exit 1 naming `unenforced:<file>` and where its unenforced
    rules open; raising the ceiling needs its `Budget raised:` line."""
    one = doc(rule())
    two = doc(rule(), rule())
    root = tree(tmp_path, rules_budget(("docs/a.md", 1)), files={"docs/a.md": two})
    assert run(root) == 1
    out = capsys.readouterr().out
    assert (
        "budget-check: unenforced:docs/a.md: measured 2 rules is over the ceiling 1 "
        "by 1. Its unenforced rules are at lines 5, 7."
    ) in out, out

    base, head = rules_budget(("docs/a.md", 1)), rules_budget(("docs/a.md", 2))
    root = tree(
        tmp_path / "raised",
        head,
        base=base,
        base_files={"docs/a.md": one},
        files={"docs/a.md": two},
    )
    assert ratchet(root, "") == 1
    assert "Budget raised: unenforced:docs/a.md 1 -> 2: <reason>" in (
        capsys.readouterr().out
    )
    line = "Budget raised: unenforced:docs/a.md 1 -> 2: its test comes with #1"
    assert ratchet(root, line) == 0, capsys.readouterr()


def test_a_rule_file_not_listed_is_held_at_zero(tmp_path, capsys):
    """S3 for a file the table does not list: the family's ceiling is 0, so
    a new rule file with a rule and no enforcer is named."""
    root = tree(tmp_path, rules_budget(), files={"docs/b.md": doc(rule())})
    assert run(root) == 1
    assert (
        "docs/b.md is not listed and measures 1 rules, over the 0 every file "
        "`## Unenforced rules` does not list is held to. Its unenforced rules "
        "are at lines 5"
    ) in capsys.readouterr().out


@pytest.mark.parametrize(
    "paragraphs, counted",
    [
        ([rule()], 1),
        ([rule("nothing — no case can read it")], 1),
        ([rule(HELD_CASE)], 0),
        ([rule(), rule("nothing — no case can read it"), rule(HELD_CASE)], 2),
    ],
    ids=["no line", "nothing with a why", "a target", "all three"],
)
def test_nothing_is_counted_as_no_enforcer_is(tmp_path, paragraphs, counted):
    """S4: `nothing — <why>` is allowed and counted, as a paragraph with no
    `Enforced by:` line is, so the escape moves the number a reviewer sees."""
    root = tree(tmp_path, None, files={"docs/a.md": doc(*paragraphs), **TESTS})
    assert budget_check.unenforced_values(str(root), {})["docs/a.md"] == counted


@pytest.mark.parametrize(
    "ceiling, verdict, said",
    [
        (1, 1, "the ceiling 1 sits above the band: measured 0 rules"),
        (0, 0, "every gate row holds"),
    ],
    ids=["the row not lowered", "lowered"],
)
def test_a_rule_that_gains_its_test_lowers_its_row(
    tmp_path, capsys, ceiling, verdict, said
):
    """S5: a rule that gains a resolving target leaves its row above the band
    until the same pull request lowers it."""
    files = {"docs/a.md": doc(rule(HELD_CASE)), **TESTS}
    root = tree(tmp_path, rules_budget(("docs/a.md", ceiling)), files=files)
    assert run(root) == verdict
    assert said in capsys.readouterr().out


@pytest.mark.parametrize(
    "text, rules",
    [
        ("**A rule.** Why.\n", ["**A rule.** Why."]),
        ("- **A rule.** Why.\n* **Another.** Why.\n", ["- **A rule.**", "* **Another"]),
        ("1. **A rule.** Why.\n2. Not one.\n", ["1. **A rule.**"]),
        ("A sentence that wraps\n**a bold word** to the front.\n", []),
        ("```\n**A fenced line.**\n```\n", []),
        ("<!--\n**A comment.**\n-->\n", []),
        ("| **A cell** | x |\n|---|---|\n", []),
        ("**A rule.** Why.\n\nEnforced by: tests/x.py\n", ["**A rule.** Why."]),
        ("- Item.\n\n  **A rule.** Why.\n", ["**A rule.** Why."]),
        ("Text.\n\n    **An indented code line.**\n", []),
    ],
    ids=[
        "bold",
        "two list items",
        "a numbered item",
        "a wrapped bold word",
        "a fence",
        "a comment",
        "a table",
        "a line after the blank",
        "an indented paragraph",
        "four spaces in",
    ],
)
def test_a_rule_paragraph_opens_a_block_with_a_bold_lead(text, rules):
    """The grammar #923 states: a rule paragraph opens on `**`, `- **`,
    `* **` or `N. **`, up to three spaces in, so a list item's continuation
    paragraph is one, outside fences, comments and tables, and closes at its
    `Enforced by:` line or its blank line — so a line after the blank is not
    its enforcer."""
    found = budget_check.rule_paragraphs(doc(text))
    assert len(found) == len(rules), found
    assert [p.first[: len(r)] for p, r in zip(found, rules, strict=True)] == rules
    assert all(p.enforced is None for p in found), found


def test_a_list_items_enforcer_closes_it_and_the_next_item_opens_another():
    """A list item's `Enforced by:` continuation line is its enforcer, and the
    next item is a paragraph of its own rather than the first one's tail."""
    text = doc("- **One.** Why.\n  Enforced by: tests/x.py\n- **Two.** Why.\n")
    found = budget_check.rule_paragraphs(text)
    assert [(p.line, p.heading, p.enforced) for p in found] == [
        (5, "The heading", "tests/x.py"),
        (7, "The heading", None),
    ], found


def test_the_slice_document_names_what_holds_each_rule():
    """S6: `docs/the-record-layout.md`, the document phase 1 proves the shape
    on, has every rule paragraph closed by a target that resolves, so its
    `unenforced` count is 0 and the budgets file does not list it."""
    path = "docs/the-record-layout.md"
    with open(os.path.join(ROOT, path), encoding="utf-8") as handle:
        found = budget_check.rule_paragraphs(handle.read())
    assert len(found) >= 7, found
    assert budget_check.unenforced_values(ROOT, {})[path] == 0, found
    names = {row.name for row in budget_check.budgets_here(ROOT)}
    assert f"unenforced:{path}" not in names
