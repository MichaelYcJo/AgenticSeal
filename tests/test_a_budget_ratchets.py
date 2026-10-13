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

import importlib.util
import json
import os
import subprocess

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, ".github", "scripts", "budget_check.py")


def _load():
    spec = importlib.util.spec_from_file_location("specseal_budget_check", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


budget_check = _load()

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
        path.write_text(text, "utf-8")


def tree(tmp_path, head, base=None, files=None, base_files=None):
    """A repository whose agent measures `MEASURED` bytes and whose
    `seal/budgets.md` is `head`. With `base`, the file is first committed as
    `base` on a branch called `base` — or left out of it where `base` is "" —
    and `head` is committed on top, so `--baseline base` reads the two.
    `base_files` are written before the base commit and `files` after it,
    each `{path: text}`."""
    root = tmp_path / "repo"
    (root / "agents").mkdir(parents=True)
    (root / "skills" / "review").mkdir(parents=True)
    (root / "seal").mkdir()
    (root / "agents" / "warden.md").write_text(_sized(AGENT_HEAD, 600), "utf-8")
    (root / "agents" / "scout.md").write_text(_sized(SCOUT_HEAD, 100), "utf-8")
    (root / "skills" / "review" / "SKILL.md").write_text(
        _sized(SKILL_HEAD, 400), "utf-8"
    )
    path = root / "seal" / "budgets.md"
    write(root, base_files)
    if base is not None:
        git(root, "init", "-q")
        if base:
            path.write_text(base, "utf-8")
        git(root, "add", "-A")
        git(root, "commit", "-qm", "base")
        git(root, "branch", "base")
    if head is not None:
        path.write_text(head, "utf-8")
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
    ],
    ids=["no line", "another new value", "another old value", "a mention", "no reason"],
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


def test_a_uniform_rescale_of_the_durations_holds_every_row(tmp_path, capsys):
    """A refresh that prices the same cases 1.07 times higher moves no row:
    the seconds rows are read in the base's prices, and the summary says the
    raw value and the level it was divided by."""
    root = tree(
        tmp_path,
        RESCALED,
        base=RESCALED,
        base_files={".test_durations": json.dumps(CASES)},
        files={".test_durations": json.dumps(priced(1.07))},
    )
    assert ratchet(root, "") == 0
    out = capsys.readouterr().out
    assert "prices the 4 cases it shares with the base x1.070 the base's" in out, out
    assert "| `suite-seconds` | 980 seconds (raw 1,049 at x1.070) |" in out, out


def test_a_file_doubling_against_the_rest_still_fails_its_row(tmp_path, capsys):
    """One file twice as slow while the rest stand still is composition, not
    price: the level moves to 1.133 and the file still reads 230 seconds in
    the base's prices, over its 130."""
    root = tree(
        tmp_path,
        RESCALED,
        base=RESCALED,
        base_files={".test_durations": json.dumps(CASES)},
        files={".test_durations": json.dumps(priced(2, only="tests/test_a.py"))},
    )
    assert ratchet(root, "") == 1
    out = capsys.readouterr().out
    assert (
        "budget-check: slow-file:tests/test_a.py: measured 230 seconds is over "
        "the ceiling 130" in out
    ), out
    assert "budget-check: suite-seconds:" not in out, out


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
