"""A ledger row may name the test that holds its claim, instead of a hash (#836).

A hashed row records what a unit held when somebody read it, so every edit to
the unit owes a re-read, and most rows written since 0.18.0 were that
bookkeeping. A row whose Code grounds cell names a test in pytest's own
spelling -- `tests/test_x.py::test_y`, or `tests/test_x.py::TestA::test_b`
for a method -- has no hash and never drifts: `evidence-check` reads that the
test is there, and the suite reads that it passes.

  S1   a test row resolves, and counts among `ok`
  S2   a renamed test breaks the row, naming the file and the name
  S3   a method is spelled pytest's way, and the bare spelling is named
  S4   a unit pytest does not collect is no test
  S5   a row is one form or the other; a citing row's citation is not code
  S6   a node id outside the Code grounds cell is prose
  S8   `--reverify` writes nothing on a test row, and names a broken one
  S11  a ledger with no node id reads as it always did
  S12  the copy `evidence-ci` vendors alone reads S1-S5 the same way

`docs/the-evidence-ledger.md` §*A claim held by a test* is the rule, and
`seal/specs/1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it/
spec.md` holds the decisions. No fixture here runs git.
"""

import importlib.util
import json
import os
import subprocess
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, "skills", "evidence-check", "scripts", "evidence_check.py")


def load():
    spec = importlib.util.spec_from_file_location("specseal_evidence_held", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ec = load()

SERVICE = "def handler(x):\n    return x + 1\n"
# The tests a fixture row may name, and the units that are not tests.
HELD = (
    "def test_holds():\n    assert True\n\n\n"
    "class TestA:\n    def test_b(self):\n        assert True\n\n\n"
    "class TestOuter:\n    class TestInner:\n        def test_c(self):\n"
    "            assert True\n\n\n"
    "def helper():\n    return 1\n\n\n"
    "class Holder:\n    def test_d(self):\n        assert True\n\n\n"
    "CONSTANT = 1\n"
)
FRAGMENT = "seal/ledger/2000000001-a-later-item.md"
TESTS = "tests/test_held.py"


def vendored(tmp_path):
    """The checker as `evidence-ci` vendors it: alone in `tools/`, with no
    `hooks/` and no `SKILL.md` beside it (S12)."""
    tools = tmp_path / "elsewhere" / "tools"
    tools.mkdir(parents=True)
    dst = tools / "evidence_check.py"
    dst.write_bytes(open(SCRIPT, "rb").read())
    return str(dst)


@pytest.fixture(params=["plugin", "vendored"])
def script(request, tmp_path):
    return SCRIPT if request.param == "plugin" else vendored(tmp_path)


@pytest.fixture
def repo(tmp_path):
    d = tmp_path / "proj"
    (d / "src").mkdir(parents=True)
    (d / "src" / "service.py").write_text(SERVICE, encoding="utf-8")
    (d / "tests").mkdir()
    (d / "tests" / "test_held.py").write_text(HELD, encoding="utf-8")
    return d


def fragment(repo, rows):
    path = repo / FRAGMENT
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(row + "\n" for row in rows), encoding="utf-8")
    return path


def held(grounds, claim="R1 · the claim holds"):
    return f"| {claim} | {grounds} | seen red, then green | 2026-10-08 | |"


def run(args, cwd, script=SCRIPT):
    return subprocess.run(
        [sys.executable, script, *args],
        cwd=str(cwd),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )


def findings(out):
    """`[(status, coordinate, detail)]` for every finding line printed."""
    found = []
    for line in out.splitlines():
        status, _, rest = line.strip().partition(" ")
        if status in ("DRIFTED", "BROKEN", "MALFORMED", "EXTERNAL", "OVERFLOW"):
            coord, _, detail = rest.strip().partition("  ")
            found.append((status, coord, detail))
    return found


def total(out):
    return next(line for line in out.splitlines() if line.startswith("total: "))


# --- S1 ------------------------------------------------------------------------


def test_a_test_row_resolves_and_counts_among_ok(repo, script):
    """S1. Red against the unfixed checker, which read the cell as citing
    nothing: `MALFORMED`, *cites no coordinate*."""
    fragment(repo, [held(f"`{TESTS}::test_holds`")])
    out = run(["--strict", "."], repo, script)
    assert out.returncode == 0, out.stdout + out.stderr
    assert findings(out.stdout) == [], out.stdout
    assert total(out.stdout).startswith("total: 1 ok · 0 drifted"), out.stdout


def test_several_tests_and_a_class_resolve_on_one_row(repo, script):
    fragment(repo, [held(f"`{TESTS}::test_holds`, `{TESTS}::TestA`")])
    out = run(["--strict", "."], repo, script)
    assert out.returncode == 0, out.stdout + out.stderr
    assert total(out.stdout).startswith("total: 2 ok"), out.stdout


# --- S2 ------------------------------------------------------------------------


def test_a_renamed_test_breaks_the_row(repo, script):
    """S2. BROKEN is exit 2 on the lenient run too, as a gone unit is."""
    fragment(repo, [held(f"`{TESTS}::test_holds`")])
    (repo / TESTS).write_text(
        HELD.replace("def test_holds", "def test_still_holds"), encoding="utf-8"
    )
    out = run(["."], repo, script)
    assert out.returncode == 2, out.stdout
    assert findings(out.stdout) == [
        (
            "BROKEN",
            f"{TESTS}::test_holds",
            f"no def or class named test_holds in {TESTS}",
        )
    ], out.stdout


def test_a_test_whose_file_is_gone_is_broken(repo, script):
    fragment(repo, [held("`tests/test_gone.py::test_holds`")])
    out = run(["."], repo, script)
    assert out.returncode == 2, out.stdout
    assert findings(out.stdout) == [
        ("BROKEN", "tests/test_gone.py::test_holds", "file not found")
    ], out.stdout


# --- S3 ------------------------------------------------------------------------


def test_a_method_resolves_in_pytests_spelling(repo, script):
    """S3. The names after the path join with `.`, the key `py_spans` uses."""
    fragment(
        repo,
        [
            held(f"`{TESTS}::TestA::test_b`"),
            held(f"`{TESTS}::TestOuter::TestInner::test_c`", "R2 · nested"),
        ],
    )
    out = run(["--strict", "."], repo, script)
    assert out.returncode == 0, out.stdout + out.stderr
    assert total(out.stdout).startswith("total: 2 ok"), out.stdout


def test_a_method_spelled_bare_is_named_with_its_spelling(repo, script):
    """S3's other half: `path::test_b` for a method is not a top-level
    function, and the detail says how pytest spells it."""
    fragment(repo, [held(f"`{TESTS}::test_b`")])
    out = run(["."], repo, script)
    assert out.returncode == 2, out.stdout
    assert findings(out.stdout) == [
        (
            "BROKEN",
            f"{TESTS}::test_b",
            f"no def or class named test_b in {TESTS} — it is a method of TestA, "
            f"and a method is written `{TESTS}::TestA::test_b`",
        )
    ], out.stdout


# --- S4 ------------------------------------------------------------------------


@pytest.mark.parametrize(
    "rel, text, node",
    [
        (TESTS, HELD, "helper"),
        (TESTS, HELD, "Holder"),
        (TESTS, HELD, "Holder::test_d"),
        ("tests/helpers.py", "def check():\n    assert True\n", "check"),
        ("tests/conftest.py", "def test_x():\n    assert True\n", "test_x"),
        (
            "tests/test_init.py",
            "class TestI:\n    def __init__(self):\n        pass\n\n"
            "    def test_x(self):\n        assert True\n",
            "TestI::test_x",
        ),
    ],
    ids=[
        "a def not named test",
        "a class not named Test",
        "a method of such a class",
        "a helper module",
        "conftest",
        "a class with __init__",
    ],
)
def test_a_unit_that_exists_resolves_without_a_record(repo, script, rel, text, node):
    """S4, rewritten at the reframe. With no record handed over, the static
    reader says what reading the file establishes and nothing more: a `def`
    or `class` of that name, defined once. Whether pytest collects it is the
    record's to say. Red against ec48b584, which read each as no test."""
    (repo / rel).write_text(text, encoding="utf-8")
    fragment(repo, [held(f"`{rel}::{node}`")])
    out = run(["--strict", "."], repo, script)
    assert out.returncode == 0, out.stdout + out.stderr
    assert findings(out.stdout) == [], out.stdout


def test_a_constant_names_no_def_or_class(repo, script):
    """S4's other half: a constant is no `def` or `class`, so the name the row
    cites is not there to hold anything — BROKEN, told what the name is."""
    fragment(repo, [held(f"`{TESTS}::CONSTANT`")])
    out = run(["."], repo, script)
    assert out.returncode == 2, out.stdout
    assert findings(out.stdout) == [
        (
            "BROKEN",
            f"{TESTS}::CONSTANT",
            f"no def or class named CONSTANT in {TESTS} — it is a constant",
        )
    ], out.stdout


@pytest.mark.parametrize(
    "token", [f"{TESTS}::test_holds[one]", "tests/test_held.txt::test_holds"]
)
def test_a_token_that_is_no_node_id_is_malformed(repo, script, token):
    """A parametrised id names no `def`, and a node id names a `.py` file."""
    fragment(repo, [held(f"`{token}`")])
    out = run(["."], repo, script)
    assert out.returncode == 1, out.stdout
    ((status, coord, detail),) = findings(out.stdout)
    assert (status, coord) == ("MALFORMED", token), out.stdout
    assert detail.startswith("does not parse as a test — name it"), detail


def test_a_unit_defined_twice_is_named(repo, script):
    (repo / TESTS).write_text(
        HELD + "\n\ndef test_holds():\n    assert False\n", encoding="utf-8"
    )
    fragment(repo, [held(f"`{TESTS}::test_holds`")])
    out = run(["."], repo, script)
    assert out.returncode == 2, out.stdout
    assert findings(out.stdout) == [
        (
            "BROKEN",
            f"{TESTS}::test_holds",
            f"test_holds is defined 2 times in {TESTS}; a test is defined once",
        )
    ], out.stdout


# --- S5 ------------------------------------------------------------------------


def handler_hash(repo):
    text = (repo / "src" / "service.py").read_text(encoding="utf-8")
    (place,) = ec.resolve_unit("src/service.py", "handler", text)[0]
    return ec.content_hash(ec.gfm_lines(text)[place[0] - 1 : place[1]])


def test_a_row_mixing_the_two_forms_is_malformed(repo, script):
    """S5. A row that says *held by a test* while still owing a re-read on
    every edit is the half-form that keeps the bookkeeping."""
    grounds = f"`{TESTS}::test_holds`, `src/service.py#handler@{handler_hash(repo)}`"
    fragment(repo, [held(grounds)])
    out = run(["."], repo, script)
    assert out.returncode == 1, out.stdout
    assert (
        "MALFORMED",
        grounds,
        "holds a test and a code coordinate, and a row is one form or the other — "
        "keep the test where it holds the claim and move the coordinates out, or "
        "keep the coordinates and move the test to Verified behavior",
    ) in findings(out.stdout), out.stdout


def test_a_citing_rows_citation_is_not_the_other_form(repo, script):
    """S5's other half: a `Corrected ·` row opens its grounds with the ledger
    line it supersedes, which is not a code coordinate."""
    section = "### 1000000001-the-first-item"
    row = f"| R1 · handler adds one | `src/service.py#handler@{handler_hash(repo)}` | read | 2026-01-01 | |"
    released = repo / "seal" / "releases" / "0.1.0.md"
    released.parent.mkdir(parents=True)
    released.write_text(
        f"## 0.1.0 — 2026-01-01\n\n{section}\n\n{row}\n", encoding="utf-8"
    )
    cite = (
        f'seal/releases/0.1.0.md#"{section}">"R1 · handler adds one"'
        f"@{ec.content_hash([row])}"
    )
    fragment(
        repo,
        [
            f"| Corrected · handler adds one | `{cite}`, `{TESTS}::test_holds` | "
            "seen red, then green | 2026-10-08 | Corrected 2026-10-08 by work item "
            "2000000001: held by its test from here on |"
        ],
    )
    out = run(["--strict", "."], repo, script)
    assert out.returncode == 0, out.stdout + out.stderr
    assert findings(out.stdout) == [], out.stdout


# --- S6 ------------------------------------------------------------------------


def test_a_node_id_outside_the_grounds_cell_is_prose(repo):
    """S6, over the shape the ledgers already hold: `path::name` in Verified
    behavior and Notes beside a hashed grounds cell. Nothing reads it, even
    where it names nothing."""
    fragment(
        repo,
        [
            f"| R1 · handler adds one | `src/service.py#handler@{handler_hash(repo)}` "
            "| `tests/test_gone.py::test_gone` is red without it | 2026-10-08 | "
            "`fold_check.py::bound` and `std::vector` are prose |"
        ],
    )
    out = run(["--strict", "."], repo)
    assert out.returncode == 0, out.stdout + out.stderr
    assert findings(out.stdout) == [], out.stdout
    assert total(out.stdout).startswith("total: 1 ok"), out.stdout


# --- S8 ------------------------------------------------------------------------


def test_reverify_writes_nothing_on_a_test_row(repo):
    """S8. No hash to re-stamp and no date to write: the bytes stand."""
    path = fragment(repo, [held(f"`{TESTS}::test_holds`")])
    before = path.read_bytes()
    out = run(["--reverify", "--checked", "2026-10-08", "."], repo)
    assert out.returncode == 0, out.stdout + out.stderr
    assert path.read_bytes() == before
    assert "LEFT" not in out.stdout, out.stdout


def test_reverify_names_a_test_that_is_gone(repo):
    """S8's other half. A re-read cannot clear a gone test, so it is left
    and named, and the run exits 1 as it does for a malformed row."""
    path = fragment(repo, [held(f"`{TESTS}::test_gone`")])
    before = path.read_bytes()
    out = run(["--reverify", "--checked", "2026-10-08", "."], repo)
    assert out.returncode == 1, out.stdout
    assert path.read_bytes() == before
    assert (
        f"  LEFT  {TESTS}::test_gone  BROKEN — no def or class named test_gone in "
        f"{TESTS}"
    ) in out.stdout.splitlines(), out.stdout


# --- S9 ------------------------------------------------------------------------

HELD_OPTION = (
    "  a claim a test holds can move onto it once instead: a `Corrected ·` row "
    "citing the released row and naming that test in Code grounds, "
    "`tests/test_x.py::test_y`, retires the row's hashes, and no later edit "
    "drifts it (docs/the-evidence-ledger.md)"
)


def drifted_release(repo):
    """A released row citing `handler`, the freeze declared, then `handler`
    edited: a run of `--into` owes the row a `Re-read ·` row."""
    (repo / "seal").mkdir(exist_ok=True)
    (repo / "seal" / "config.md").write_text(
        "# Repository config\n\n| Item | Value |\n|---|---|\n"
        "| Ledger frozen from | 1 |\n",
        encoding="utf-8",
    )
    row = f"| R1 · handler adds one | `src/service.py#handler@{handler_hash(repo)}` | read | 2026-01-01 | |"
    released = repo / "seal" / "releases" / "0.1.0.md"
    released.parent.mkdir(parents=True)
    released.write_text(
        f"## 0.1.0 — 2026-01-01\n\n### 1000000001-the-first-item\n\n{row}\n",
        encoding="utf-8",
    )
    (repo / "src" / "service.py").write_text(
        SERVICE.replace("x + 1", "x + 2"), encoding="utf-8"
    )


def test_into_names_the_test_row_once_where_it_wrote_a_re_read(repo):
    """S9. `--into` cannot tell which of a row's grounds holds its claim, so
    it names the other repair once, in its summary, and writes none of it."""
    drifted_release(repo)
    out = run(["--reverify", "--into", FRAGMENT, "--checked", "2026-10-08", "."], repo)
    assert out.returncode == 0, out.stdout + out.stderr
    lines = out.stdout.splitlines()
    assert lines.count(HELD_OPTION) == 1, out.stdout
    assert (
        lines.index(HELD_OPTION)
        == lines.index("1 citing row written · 0 released rows left") + 1
    ), out.stdout
    assert "Corrected" not in (repo / FRAGMENT).read_text(encoding="utf-8")
    again = run(
        ["--reverify", "--into", FRAGMENT, "--checked", "2026-10-08", "."], repo
    )
    assert again.returncode == 0, again.stdout
    assert HELD_OPTION not in again.stdout.splitlines(), again.stdout


def test_the_commit_advisor_names_the_test_row_as_a_repair():
    """Q4 of this work item: the post-commit advisor carries its own repair
    sentence for a broken row under the freeze, so it names the other form
    too, rather than only the coordinates a correction carries."""
    spec = importlib.util.spec_from_file_location(
        "specseal_evidence_advisor_held",
        os.path.join(ROOT, "hooks", "evidence-advisor.py"),
    )
    advisor = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(advisor)
    assert (
        "— or, where a test holds the claim, names that test instead, "
        "`tests/test_x.py::test_y`, and no later edit drifts it;"
    ) in advisor.FROZEN_REPAIR, advisor.FROZEN_REPAIR


# --- S11 -----------------------------------------------------------------------


def test_a_ledger_with_no_test_row_reads_as_it_always_did(repo):
    """S11. Hashed rows, a row citing nothing, prose holding `::` in and out
    of the grounds cell, and a fenced example holding a node id: the output
    is the one 0.20.0's checker printed for this ledger, line for line."""
    good = handler_hash(repo)
    ledger = repo / "seal" / "ledger.md"
    ledger.parent.mkdir(parents=True)
    ledger.write_text(
        "# Ledger\n\n"
        "| Clause | Code grounds | Verified behavior | Checked | Notes |\n"
        "|---|---|---|---|---|\n"
        f"| P1 | `src/service.py#handler@{good}` std::vector | read | 2026-01-01 | `a::b` |\n"
        "| P2 | `src/service.py#handler@00000000` | read | 2026-01-01 | |\n"
        "| P3 | handler, read by hand | read | 2026-01-01 | |\n"
        "\n```\n"
        f"| P4 | `{TESTS}::test_gone` | an example | 2026-01-01 | |\n"
        "```\n",
        encoding="utf-8",
    )
    out = run(["--strict", "."], repo)
    assert out.returncode == 2, out.stdout
    assert [line.replace(os.sep, "/") for line in out.stdout.splitlines()[:5]] == [
        "",
        "seal/ledger.md",
        "  DRIFTED  src/service.py#handler  content changed at 1-2 — re-verify",
        "  MALFORMED handler, read by hand  cites no coordinate, so nothing checks "
        "the claim — write `path#anchor@hash` in the Code grounds cell, the hash as "
        "`@00000000`, then run `evidence-check --reverify .`; or, where a test "
        "holds the claim, name it in Code grounds as pytest spells it, "
        "`tests/test_x.py::test_y`, or `tests/test_x.py::TestA::test_b` for a "
        "method",
        "  1 ok · 1 drifted · 0 broken · 0 external · 0 old-format · 1 malformed "
        "· 0 overflow",
    ], out.stdout


def test_the_resolver_hands_each_caller_its_own_answer():
    """`unit_kinds` is memoised on the text; a caller that changes the dict
    it was handed changes nothing for the next one."""
    first = ec.unit_kinds(HELD)
    first["test_holds"] = ("class",)
    assert ec.unit_kinds(HELD)["test_holds"] == ("def",)
    assert ec.named_unit(HELD, ["TestA", "test_b"]) == ("def",)
    assert ec.named_unit(HELD, ["test_b"]) == ()
    assert ec.named_unit("def (:\n", ["x"]) is None
    # Round 1, ⬜ 4: a name is one identifier; `A.b` is not `A::b`.
    assert ec.named_unit(HELD, ["TestA.test_b"]) == ()


# --- round 1 -------------------------------------------------------------------


def released_test_row(repo, freeze):
    """A released row naming `test_holds`, then the test renamed, then one
    `Corrected ·` row in a fragment re-pointing the claim at the new name."""
    if freeze:
        (repo / "seal").mkdir(exist_ok=True)
        (repo / "seal" / "config.md").write_text(
            "# Repository config\n\n| Item | Value |\n|---|---|\n"
            "| Ledger frozen from | 1 |\n",
            encoding="utf-8",
        )
    section = "### 1000000001-the-first-item"
    row = f"| R1 · held | `{TESTS}::test_holds` | seen red | 2026-01-01 | |"
    released = repo / "seal" / "releases" / "0.1.0.md"
    released.parent.mkdir(parents=True)
    released.write_text(
        f"## 0.1.0 — 2026-01-01\n\n{section}\n\n{row}\n", encoding="utf-8"
    )
    (repo / TESTS).write_text(
        HELD.replace("def test_holds", "def test_renamed"), encoding="utf-8"
    )
    cite = f'seal/releases/0.1.0.md#"{section}">"R1 · held"@{ec.content_hash([row])}'
    fragment(
        repo,
        [
            f"| Corrected · held | `{cite}`, `{TESTS}::test_renamed` | seen red, "
            "then green | 2026-02-01 | Corrected 2026-02-01 by work item "
            "2000000001: re-pointed |"
        ],
    )


def test_a_released_test_row_re_pointed_by_a_correction_reads_clean(repo, script):
    """Round 1, 🔴 1. A released row naming a test that was renamed is
    repaired by one `Corrected ·` row naming the new test: the released row
    is superseded, so its gone test is not read again, as a superseded row's
    hashes are not. Red before the fix: BROKEN, exit 2."""
    released_test_row(repo, freeze=True)
    out = run(["--strict", "."], repo, script)
    assert out.returncode == 0, out.stdout + out.stderr
    assert findings(out.stdout) == [], out.stdout
    assert total(out.stdout).startswith("total: 2 ok"), out.stdout


def test_reverify_leaves_a_superseded_test_row_unnamed(repo):
    """Round 1, 🔴 1, the in-place writer: without the freeze `--reverify`
    reads the released file too, and a superseded row's gone test is no
    longer named on a `LEFT` line. Red before the fix: `LEFT`, exit 1."""
    released_test_row(repo, freeze=False)
    out = run(["--reverify", "--checked", "2026-10-08", "."], repo)
    assert out.returncode == 0, out.stdout + out.stderr
    assert "test_holds" not in out.stdout, out.stdout


def test_a_corrections_own_gone_test_is_still_broken(repo):
    """Round 1, 🔴 1's other half: the correcting row starts a family of its
    own, and its own test is read like any row's."""
    released_test_row(repo, freeze=True)
    (repo / TESTS).write_text(HELD, encoding="utf-8")
    out = run(["--strict", "."], repo)
    assert out.returncode == 2, out.stdout
    assert [(s, c) for s, c, _ in findings(out.stdout)] == [
        ("BROKEN", f"{TESTS}::test_renamed")
    ], out.stdout


def test_a_coordinate_quoting_a_scope_is_no_test(repo, script):
    """Round 1, 🟡 3, S11 and D3: a coordinate is unambiguous by its shape,
    so `::` inside its quoted locator is no node id. Red before the fix: two
    MALFORMED on a ledger holding no test row."""
    doc = repo / "docs" / "guide.md"
    doc.parent.mkdir()
    doc.write_text("# Guide\n\n## The Foo::bar form\n\nText.\n", encoding="utf-8")
    fragment(repo, [held('`docs/guide.md#"## The Foo::bar form"@00000000`')])
    run(["--reverify", "."], repo, script)
    out = run(["--strict", "."], repo, script)
    assert out.returncode == 0, out.stdout + out.stderr
    assert findings(out.stdout) == [], out.stdout


def test_a_pact_anchor_quoting_a_scope_is_no_test(repo):
    """Round 1, 🟡 3's other coordinate: a pact anchor's quoted heading path
    may hold `::` too, and it is a clause of a pact, not a test."""
    grounds = (
        f"`src/service.py#handler@{handler_hash(repo)}`, "
        '`pact:shared/"## The A::b clause"@abcdef12`'
    )
    fragment(repo, [held(grounds)])
    out = run(["--strict", "."], repo)
    assert out.returncode == 0, out.stdout + out.stderr
    assert findings(out.stdout) == [], out.stdout


# --- the reframe: the sealed run's record (S15 to S20, S22) --------------------
#
# Every case here reads a record the real recorder wrote: pytest runs over a
# planted suite with `-p specseal_pytest_record` and the recorder's two
# variables, as `tests/test_the_recorder_writes_what_its_process_ran.py`
# drives it. A hand-written record would hold the reader to this file's idea
# of the format rather than to the recorder's.

RECORDER_DIR = os.path.join(ROOT, "skills", "verify", "scripts", "pytest_record")
SUITE_KEY = "head-0123456789abcdef"
OBSERVED = (
    "import pytest\n"
    "\n"
    "@pytest.fixture\n"
    "def broken():\n"
    "    raise RuntimeError('setup')\n"
    "\n"
    "def test_pass():\n"
    "    assert True\n"
    "\n"
    "@pytest.mark.skip\n"
    "def test_skip():\n"
    "    pass\n"
    "\n"
    "@pytest.mark.xfail\n"
    "def test_xfail():\n"
    "    assert False\n"
    "\n"
    "@pytest.mark.xfail\n"
    "def test_xpass():\n"
    "    assert True\n"
    "\n"
    "def test_fail():\n"
    "    assert False\n"
    "\n"
    "def test_error(broken):\n"
    "    pass\n"
    "\n"
    "@pytest.mark.parametrize('v', [1, 2])\n"
    "def test_param(v):\n"
    "    assert v == 1\n"
    "\n"
    "@pytest.mark.parametrize('v', [1, 2])\n"
    "def test_cases(v):\n"
    "    assert v\n"
    "\n"
    "def helper():\n"
    "    return 1\n"
    "\n"
    "class TestA:\n"
    "    def test_b(self):\n"
    "        assert True\n"
    "\n"
    "    def test_c(self):\n"
    "        assert True\n"
    "\n"
    "class TestB:\n"
    "    def test_b(self):\n"
    "        assert True\n"
    "\n"
    "    @pytest.mark.skip\n"
    "    def test_c(self):\n"
    "        pass\n"
    "\n"
    "class TestI:\n"
    "    def __init__(self):\n"
    "        pass\n"
    "\n"
    "    def test_x(self):\n"
    "        assert True\n"
)
# Round 1's and round 2's spellings (S17): what the record says is what pytest
# did, and this module names a spelling only to plant it.
SPELLINGS = (
    "import pytest\n"
    "\n"
    "@pytest.mark.xfail(condition=False, reason='never')\n"
    "def test_conditional_xfail():\n"
    "    assert True\n"
    "\n"
    "@pytest.mark.xfail(strict=True)\n"
    "def test_strict_xfail():\n"
    "    assert True\n"
    "\n"
    "@pytest.mark.skipif(True, reason='always')\n"
    "def test_skipif_true():\n"
    "    assert True\n"
    "\n"
    "@pytest.mark.skipif(False, reason='never')\n"
    "def test_skipif_false():\n"
    "    assert True\n"
)
UNDER_IF = (
    "import pytest\n"
    "\n"
    "if True:\n"
    "    pytestmark = pytest.mark.skip\n"
    "\n"
    "def test_x():\n"
    "    assert True\n"
)
AUGMENTED = (
    "import pytest\n"
    "\n"
    "pytestmark = [pytest.mark.slow]\n"
    "pytestmark += [pytest.mark.skip]\n"
    "\n"
    "def test_x():\n"
    "    assert True\n"
)
MODULE_SKIP = (
    "import pytest\n"
    "\n"
    "pytest.skip('module', allow_module_level=True)\n"
    "\n"
    "def test_x():\n"
    "    assert True\n"
)
PLANTED = {
    "test_observed.py": OBSERVED,
    "test_spellings.py": SPELLINGS,
    "test_under_if.py": UNDER_IF,
    "test_augmented.py": AUGMENTED,
    "test_module_skip.py": MODULE_SKIP,
    "helpers.py": "def check():\n    assert True\n",
}


def recording_env(records):
    """The environment the gate hands a run it measures, built on this
    process's own with the recorder's variables cleared first, so an outer
    gate's run of this suite does not leak into the case."""
    env = dict(os.environ)
    for name in ("SPECSEAL_RECORD_KEY", "SPECSEAL_RECORD_DIR", "PYTEST_ADDOPTS"):
        env.pop(name, None)
    env["PYTHONPATH"] = os.pathsep.join(
        p for p in (RECORDER_DIR, env.get("PYTHONPATH")) if p
    )
    env["PYTEST_ADDOPTS"] = "-p specseal_pytest_record"
    env["SPECSEAL_RECORD_KEY"] = SUITE_KEY
    env["SPECSEAL_RECORD_DIR"] = str(records)
    return env


def record_suite(project, records):
    """Run pytest over PROJECT's `tests/` with the recorder loaded, as the gate
    runs a row it measures; the record lands under RECORDS."""
    records.mkdir(exist_ok=True)
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "-p",
            "no:cacheprovider",
            "-p",
            "no:xdist",
            "tests",
        ],
        cwd=str(project),
        env=recording_env(records),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=240,
    )


@pytest.fixture(scope="module")
def suite(tmp_path_factory):
    """One planted project and the record its one pytest run wrote: every
    case below writes its own fragment into it."""
    base = tmp_path_factory.mktemp("suite")
    project = base / "proj"
    (project / "tests").mkdir(parents=True)
    for name, text in PLANTED.items():
        (project / "tests" / name).write_text(text, encoding="utf-8")
    records = base / "records"
    done = record_suite(project, records)
    assert done.returncode == 1, done.stdout + done.stderr
    return project, records


def observe(suite, script, rows):
    project, records = suite
    fragment(project, rows)
    return run(
        ["--strict", "--suite-record", str(records), "--suite-key", SUITE_KEY, "."],
        project,
        script,
    )


def test_the_recorder_writes_a_passed_setup_under_no_category(suite):
    """`questions.md` Q5, measured: a passed setup and teardown are written
    with the category `""`, and only the call `passed`, on the build this
    suite runs; the held rule (`passed` and nothing else, less `""`) rests on
    it. `phases/phase-7.md` records the same on pytest 7.4.4."""
    record = ec.suite_record(str(suite[1]), SUITE_KEY, str(suite[0]))
    assert record[("tests/test_observed.py", ("test_pass",))] == {"", "passed"}


def test_a_test_seen_passing_is_held(suite, script):
    """S15. Red against the phase-6 checker, which knows neither option."""
    out = observe(suite, script, [held("`tests/test_observed.py::test_pass`")])
    assert out.returncode == 0, out.stdout + out.stderr
    assert findings(out.stdout) == [], out.stdout
    assert "read for existence alone" not in out.stdout, out.stdout


UNHELD = (
    ", so nothing holds the claim — name it in Code grounds as pytest spells it, "
    "`tests/test_x.py::test_y`, or `tests/test_x.py::TestA::test_b` for a method; "
    "or, where no test holds it, write `path#anchor@hash`"
)


@pytest.mark.parametrize(
    "node, seen",
    [
        ("tests/test_observed.py::test_skip", "skipped"),
        ("tests/test_observed.py::test_xfail", "xfailed"),
        ("tests/test_observed.py::test_xpass", "xpassed"),
        ("tests/test_observed.py::test_fail", "failed"),
        ("tests/test_observed.py::test_error", "error"),
        ("tests/test_observed.py::helper", "not run"),
        ("tests/test_observed.py::TestI::test_x", "not run"),
        ("tests/test_module_skip.py::test_x", "not run"),
        ("tests/helpers.py::check", "not run"),
    ],
    ids=[
        "skipped",
        "xfailed",
        "xpassed",
        "failed",
        "error in setup",
        "a helper",
        "a class with __init__",
        "a module skipped at collection",
        "a module pytest does not collect",
    ],
)
def test_a_test_the_run_did_not_hold_is_refused_by_what_was_observed(
    suite, script, node, seen
):
    """S16. Each red against the phase-6 checker, which read every one OK."""
    out = observe(suite, script, [held(f"`{node}`")])
    assert out.returncode == 2, out.stdout + out.stderr
    assert findings(out.stdout) == [
        ("MALFORMED", node, f"{seen} in the recorded suite{UNHELD}")
    ], out.stdout


@pytest.mark.parametrize(
    "node, seen",
    [
        ("tests/test_spellings.py::test_conditional_xfail", None),
        ("tests/test_spellings.py::test_strict_xfail", "failed"),
        ("tests/test_spellings.py::test_skipif_true", "skipped"),
        ("tests/test_spellings.py::test_skipif_false", None),
        ("tests/test_under_if.py::test_x", "skipped"),
        ("tests/test_augmented.py::test_x", "skipped"),
    ],
    ids=[
        "xfail with condition=False",
        "xfail strict, passing",
        "skipif true",
        "skipif false",
        "a mark under a module if",
        "pytestmark +=",
    ],
)
def test_round_twos_spellings_are_what_pytest_did(suite, script, node, seen):
    """S17. The verdict is the record's: the xfail whose condition was false
    ran and passed, the strict xfail that passed failed, the skipped ones were
    skipped. Not one of them needed a line of the checker."""
    out = observe(suite, script, [held(f"`{node}`")])
    if seen is None:
        assert out.returncode == 0, out.stdout + out.stderr
        assert findings(out.stdout) == [], out.stdout
    else:
        assert findings(out.stdout) == [
            ("MALFORMED", node, f"{seen} in the recorded suite{UNHELD}")
        ], out.stdout


def test_the_checker_names_no_mark():
    """S17's other half: no mark's name is in the checker's source outside the
    words a detail prints, so no spelling is predicted from a file."""
    with open(SCRIPT, encoding="utf-8") as handle:
        source = handle.read()
    for word in ("pytestmark", "skipif", "mark.skip", "mark.xfail", "allow_module"):
        assert word not in source, word


@pytest.mark.parametrize(
    "node, seen",
    [
        ("tests/test_observed.py::TestA", None),
        ("tests/test_observed.py::TestB", "skipped"),
        ("tests/test_observed.py::test_cases", None),
        ("tests/test_observed.py::test_param", "failed"),
    ],
    ids=[
        "a class all passed",
        "a class one skipped",
        "cases all passed",
        "a case failed",
    ],
)
def test_a_class_and_a_parametrised_function_own_their_lines(suite, script, node, seen):
    """S18. A cited unit owns every line whose names begin with its own: a
    class its methods, a function its parametrised cases."""
    out = observe(suite, script, [held(f"`{node}`")])
    if seen is None:
        assert out.returncode == 0, out.stdout + out.stderr
        assert findings(out.stdout) == [], out.stdout
    else:
        assert findings(out.stdout) == [
            ("MALFORMED", node, f"{seen} in the recorded suite{UNHELD}")
        ], out.stdout


def test_another_files_test_of_the_same_name_is_not_this_rows(suite, script):
    """S18's last clause: `TestA::test_b` and `TestB::test_b` share a name, and
    a row naming `TestB::test_b` owns only TestB's line; a file pytest never
    collected owns no line of another file's `check`."""
    out = observe(
        suite,
        script,
        [
            held("`tests/test_observed.py::TestB::test_b`"),
            held("`tests/test_observed.py::TestB::test_c`", "R2 · the skipped one"),
        ],
    )
    assert findings(out.stdout) == [
        (
            "MALFORMED",
            "tests/test_observed.py::TestB::test_c",
            f"skipped in the recorded suite{UNHELD}",
        )
    ], out.stdout


def test_the_path_is_the_records_never_rebuilt_from_the_node_id(tmp_path, script):
    """S19. pytest's rootdir is `tests/`, so the record's node id is
    `test_x.py::test_y`; the row's `tests/test_x.py::test_y` matches through
    the line's `path`, and the gate's own reader names the same file."""
    project = tmp_path / "proj"
    (project / "tests").mkdir(parents=True)
    (project / "tests" / "pytest.ini").write_text("[pytest]\n", encoding="utf-8")
    (project / "tests" / "test_x.py").write_text(
        "def test_y():\n    assert True\n", encoding="utf-8"
    )
    records = tmp_path / "records"
    done = record_suite(project, records)
    assert done.returncode == 0, done.stdout + done.stderr
    nodeids = [
        json.loads(line).get("nodeid")
        for name in os.listdir(records)
        for line in (records / name).read_text(encoding="utf-8").splitlines()
    ]
    assert "test_x.py::test_y" in nodeids, nodeids
    fragment(project, [held("`tests/test_x.py::test_y`")])
    out = run(
        ["--strict", "--suite-record", str(records), "--suite-key", SUITE_KEY, "."],
        project,
        script,
    )
    assert out.returncode == 0, out.stdout + out.stderr
    assert findings(out.stdout) == [], out.stdout
    spec = importlib.util.spec_from_file_location(
        "specseal_broad_gate_for_held_rows",
        os.path.join(ROOT, "skills", "verify", "scripts", "broad_gate.py"),
    )
    gate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gate)
    assert set(gate.read_record(str(records), SUITE_KEY, str(project)).collected) == {
        "tests/test_x.py"
    }
    assert list(ec.suite_record(str(records), SUITE_KEY, str(project))) == [
        ("tests/test_x.py", ("test_y",))
    ]


EXISTENCE = (
    "test rows were read for existence alone: no suite record was given, so "
    "whether each cited test ran and passed was not read — `broad-gate` hands "
    "this check the sealed run's record"
)


def test_no_record_is_existence_and_says_so_once(repo, script):
    """S20. With no record the test rows are read by existence alone, and one
    line, printed once beside the totals, says so."""
    fragment(
        repo,
        [
            held(f"`{TESTS}::test_holds`"),
            held(f"`{TESTS}::TestA::test_b`", "R2 · another"),
        ],
    )
    out = run(["--strict", "."], repo, script)
    assert out.returncode == 0, out.stdout + out.stderr
    lines = out.stdout.splitlines()
    assert lines.count(EXISTENCE) == 1, out.stdout
    assert lines[lines.index(EXISTENCE) - 1].startswith("total: 2 ok"), out.stdout


def test_a_record_with_no_session_under_the_key_names_the_key(repo, script, tmp_path):
    """S20: a directory under which no session carries the key is read as no
    record, and the line names the key, not a refusal of every row."""
    empty = tmp_path / "records"
    empty.mkdir()
    (empty / "other.jsonl").write_text(
        '{"kind": "session", "key": "head-another"}\n', encoding="utf-8"
    )
    fragment(repo, [held(f"`{TESTS}::test_holds`")])
    out = run(
        ["--strict", "--suite-record", str(empty), "--suite-key", SUITE_KEY, "."],
        repo,
        script,
    )
    assert out.returncode == 0, out.stdout + out.stderr
    assert (
        f"test rows were read for existence alone: no session under {empty} "
        f"carries the key {SUITE_KEY}, so whether each cited test ran and passed "
        "was not read — `broad-gate` hands this check the sealed run's record"
    ) in out.stdout.splitlines(), out.stdout


def test_a_ledger_with_no_test_row_prints_no_existence_line(repo, script):
    """S20's last clause: the line is about test rows, so a ledger of hashed
    rows prints none."""
    fragment(
        repo,
        [
            f"| P1 | `src/service.py#handler@{handler_hash(repo)}` | read | 2026-10-12 | |"
        ],
    )
    out = run(["--strict", "."], repo, script)
    assert out.returncode == 0, out.stdout + out.stderr
    assert "read for existence alone" not in out.stdout, out.stdout


def test_a_directory_without_its_key_is_refused(repo):
    """The record is one run's: a directory alone, or a key alone, names
    none, and the run is refused before anything is read."""
    out = run(["--suite-record", str(repo), "."], repo)
    assert out.returncode == 2, out.stdout
    assert (
        "`--suite-record` and `--suite-key` name one run's record together — pass "
        "both or neither"
    ) in out.stderr, out.stderr


def test_reverify_names_what_the_record_refuses_and_writes_nothing(suite):
    """S22. `--reverify`, and `--reverify --into` under the freeze, name a test
    row the record refuses on a `LEFT` line with the observation, write
    nothing on it and exit 1."""
    project, records = suite
    node = "tests/test_observed.py::test_skip"
    path = fragment(project, [held(f"`{node}`")])
    before = path.read_bytes()
    record = ["--suite-record", str(records), "--suite-key", SUITE_KEY]
    out = run(["--reverify", "--checked", "2026-10-12", *record, "."], project)
    assert out.returncode == 1, out.stdout + out.stderr
    assert path.read_bytes() == before
    left = f"  LEFT  {node}  MALFORMED — skipped in the recorded suite{UNHELD}"
    assert left in out.stdout.splitlines(), out.stdout
    config = project / "seal" / "config.md"
    config.write_text(
        "# Repository config\n\n| Item | Value |\n|---|---|\n"
        "| Ledger frozen from | 1 |\n",
        encoding="utf-8",
    )
    try:
        out = run(
            ["--reverify", "--into", FRAGMENT, "--checked", "2026-10-12", *record, "."],
            project,
        )
    finally:
        config.unlink()
    assert out.returncode == 1, out.stdout + out.stderr
    assert path.read_bytes() == before
    assert left in out.stdout.splitlines(), out.stdout


# --- S13 -----------------------------------------------------------------------


def prose(rel):
    """REL's text with every run of whitespace one space, so a pin holds a
    sentence however the paragraph is wrapped."""
    with open(os.path.join(ROOT, rel), encoding="utf-8") as handle:
        return " ".join(handle.read().split())


@pytest.mark.parametrize(
    "rel, sentence",
    [
        (
            "docs/the-evidence-ledger.md",
            "**A row may name the test that holds its claim instead of a hash over "
            "the code.**",
        ),
        (
            "docs/the-evidence-ledger.md",
            "**The checker reads that the test is there, and the sealed run's record "
            "says whether it passed.**",
        ),
        ("docs/the-evidence-ledger.md", "**A row is one form or the other.**"),
        (
            "docs/the-evidence-ledger.md",
            "**A released row moves onto its test by one `Corrected ·` row, written "
            "when an edit reaches it, and never in bulk by a feature branch.**",
        ),
        ("docs/the-evidence-ledger.md", "**`path::name` has one resolver.**"),
        (
            "templates/ledger.md",
            "| <claim> | `tests/test_x.py::test_y`, … | how the test was seen red | "
            "<date seen red, then green> | |",
        ),
        (
            "templates/ledger.md",
            "| <claim> | `path#anchor@hash`, … | what reading the code showed | "
            "<date read> | |",
        ),
        (
            "skills/evidence-check/SKILL.md",
            "**A row held by a test takes three of these, and never `DRIFTED`** "
            "(#836).",
        ),
        (
            "skills/evidence-check/SKILL.md",
            "A row held by a test has no hash to rewrite: the run writes nothing on "
            "it and dates nothing",
        ),
        (
            "skills/evidence-ci/SKILL.md",
            "**Update the copy before the ledger holds a row held by a test.**",
        ),
        (
            "skills/evidence-ci/SKILL.md",
            "an older vendored copy reads it as `MALFORMED`, *cites no coordinate*",
        ),
        # Round 1, 🔴 1.
        (
            "docs/the-evidence-ledger.md",
            "the superseded row's tests are not read again, as its hashes are not.",
        ),
        # The reframe after round 2 (S23).
        (
            "docs/the-evidence-ledger.md",
            "Reading the row's file establishes one thing for certain, and the "
            "checker reads that alone: a `def` or `class` of the cited name is "
            "defined in the cited file once.",
        ),
        (
            "docs/the-evidence-ledger.md",
            "a test row is `OK` there only where every line the record holds for "
            "the cited test says `passed`",
        ),
        (
            "docs/the-evidence-ledger.md",
            "test rows are read for existence alone, and the run says so in one "
            "line beside its totals.",
        ),
        (
            "skills/evidence-check/SKILL.md",
            "a test is `OK` only where every line the pytest recorder wrote for it "
            "says `passed`, and `MALFORMED` otherwise",
        ),
        (
            "skills/evidence-check/SKILL.md",
            "Given no record, a test that exists is `OK`, and one line beside the "
            "totals says the test rows were read for existence alone.",
        ),
        (
            "templates/ledger.md",
            "`broad-gate` holds it only where the run it seals recorded the test "
            "passing",
        ),
        (
            "skills/evidence-ci/SKILL.md",
            "loads `specseal_pytest_record` in its own test job and hands the step "
            "that run's directory and key with `--suite-record` and `--suite-key`",
        ),
        (
            "skills/verify/scripts/broad_gate.py",
            "`--suite-record` and `--suite-key` hand it that run's pytest record, "
            "so a row held by a test is held only where the test was seen passing "
            "in it (#836).",
        ),
    ],
)
def test_the_documents_state_the_test_row(rel, sentence):
    """S13. Each sentence a person reads to write or update a test row, pinned
    where it stands (`agent-contract` §14)."""
    assert sentence in prose(rel), f"{rel} no longer says: {sentence!r}"
