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


def tree(tmp_path, head, base=None):
    """A repository whose agent measures `MEASURED` bytes and whose
    `seal/budgets.md` is `head`. With `base`, the file is first committed as
    `base` on a branch called `base` — or left out of it where `base` is "" —
    and `head` is committed on top, so `--baseline base` reads the two."""
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
    if base is not None:
        git(root, "init", "-q")
        if base:
            path.write_text(base, "utf-8")
        git(root, "add", "-A")
        git(root, "commit", "-qm", "base")
        git(root, "branch", "base")
    if head is not None:
        path.write_text(head, "utf-8")
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
    assert budget_check.measure(str(root), row) == MEASURED


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
