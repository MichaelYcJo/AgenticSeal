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


def slow(*rows, threshold=120, slack="10 %", suite=None):
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
        budgets(("suite-seconds", "seconds", ceiling, "5 %", "gate")),
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


def priced(scale, only=None):
    """`CASES` with every case, or the cases of the file `only`, multiplied."""
    return {
        case: seconds * (scale if only is None or case.startswith(only) else 1)
        for case, seconds in CASES.items()
    }


RESCALED = slow(("tests/test_a.py", 130), threshold=800, suite=(980, "5 %"))


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
    price: the level moves to 1133 and the file still reads 229 seconds in
    the ceilings' prices, over its 130."""
    root = refreshed(
        tmp_path, priced(2, only="tests/test_a.py"), RESCALED + price(1133)
    )
    assert ratchet(root, "") == 1
    out = capsys.readouterr().out
    assert (
        "budget-check: slow-file:tests/test_a.py: measured 229 seconds is over "
        "the ceiling 130" in out
    ), out
    assert "budget-check: suite-seconds:" not in out, out
    assert "budget-check: price level:" not in out, out


@pytest.mark.parametrize(
    "before, said",
    [
        ({"tests/test_z.py::t": 10.0}, "share no case id"),
        ({case: 0.0 for case in CASES}, "at 0 seconds"),
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


SUITE = budgets(("suite-seconds", "seconds", 180, "5 %", "gate"))


@pytest.mark.parametrize(
    "head, files, said",
    [
        (
            budgets(warden(MEASURED)) + table("Seconds ceiling", []),
            {},
            "and no `slow-file` row in its Budgets table",
        ),
        (
            budgets(("slow-file", "seconds", 120, "10 %", "gate")),
            {},
            "has a `slow-file` row and no `## Slow test files` table",
        ),
        (slow(("tests/test_a.py", 1), ("tests/test_a.py", 1)), {}, "is written twice"),
        (slow(("tests/test_a.py", "1,0")), {}, "is not a whole number"),
        (slow(("tests/a b.py", 1)), {}, "is no file name"),
        (
            budgets(("slow-file", "bytes", 120, "10 %", "gate"))
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
    job("ledger", 0.8),
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
        "#929 read in mid-2026, its date unverified (`questions.md` Q1)." in out
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
            "a row read off one CI run is `one-sided`",
        ),
        (
            budgets(warden(MEASURED, "one-sided")),
            None,
            None,
            "only a row read off one CI run or a `report` row is `one-sided`",
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
            "seal/specs/1-a/rounds/round-1.md": "a" * 99 + "\n",
            "seal/specs/1-a/rounds/round-2.md": "a" * 199 + "\n",
            "seal/specs/2-b/rounds/round-1.md": "b" * 49 + "\n",
            "seal/specs/3-c/spec.md": "c" * 999 + "\n",
        },
    )
    assert run(root) == 0
    out = capsys.readouterr().out
    assert (
        "| `rounds-bytes` | 300 bytes | 10 | -290 (-2900.0%) | report | over |" in out
    )
    assert "- `1-a`: 300 bytes over 2 files\n- `2-b`: 50 bytes over 1 files\n" in out, (
        out
    )


def release(version, rows):
    return {
        ".claude-plugin/plugin.json": json.dumps({"version": version}),
        f"seal/releases/{version}.md": f"## {version}\n\n### 1-a\n\n"
        + "".join(f"| {row} | grounds | read | 2026-10-14 | note |\n" for row in rows),
    }


def test_the_rereads_of_a_release_are_counted_once_each_by_their_first_marker(
    tmp_path, capsys
):
    """`ledger-rereads` counts the release file of the version the manifest
    names: a row re-reading a correction is a re-read, once, and a row whose
    cells carry an even run of backslashes before a pipe still counts by its
    opening (`questions.md` Q4)."""
    rows = [
        "Re-read · A1 · a claim",
        "Corrected · A2 · a claim",
        "Re-read · Corrected · A3 · a claim",
        "Corrected · A4 · a cell with `\\\\|` in it",
        "A5 · a new claim",
    ]
    root = tree(
        tmp_path,
        budgets(("ledger-rereads", "rows", 4, "one-sided", "report")),
        files=release("9.9.9", rows),
    )
    assert run(root) == 0
    out = capsys.readouterr().out
    assert "| `ledger-rereads` | 4 rows | 4 | 0 (0.0%) | report | holds |" in out, out
    assert (
        "`seal/releases/9.9.9.md`: 2 `Re-read ·`, 2 `Corrected ·` of 5 rows" in out
    ), out


def test_rereads_before_the_release_folds_its_file_are_unread(tmp_path, capsys):
    """Until the release folds its ledger file there is nothing to count, so
    the row is shown unread rather than read as 0, which would look like a
    release that re-read nothing."""
    root = tree(
        tmp_path,
        budgets(("ledger-rereads", "rows", 4, "one-sided", "report")),
        files={".claude-plugin/plugin.json": json.dumps({"version": "9.9.9"})},
    )
    assert run(root) == 0
    assert (
        "| `ledger-rereads` | — (read once the release folds its ledger file) | 4 |"
        in capsys.readouterr().out
    )


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


def test_a_manifest_with_no_version_is_exit_2(tmp_path, capsys):
    """The release file is named by the manifest's version; a manifest that
    states none names no file to count."""
    root = tree(
        tmp_path,
        budgets(("ledger-rereads", "rows", 4, "one-sided", "report")),
        files={".claude-plugin/plugin.json": "{}"},
    )
    assert run(root) == 2
    assert "plugin.json states no version" in capsys.readouterr().err
