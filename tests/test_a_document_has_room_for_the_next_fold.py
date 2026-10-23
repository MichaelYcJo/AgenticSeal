"""A document fits one read, and the policy root has one index (#953).

`fold-check` (`skills/settle/scripts/fold_check.py`) reports each top-level
document of the policy root whose estimate is past the `Document token
ceiling` row as one to split along its own headings, and exits 0 on it: the
estimate is a guess from bytes, so it is a report and not a gate. Its index
arm refuses a `<policy root>/README.md` that misses a document, names one
twice, or holds a row naming none. The rows and the estimate are stated once,
in `templates/config.md` *The fold's values*.
"""

import os
import subprocess
import sys

import pytest
from conftest import load_module

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, "skills", "settle", "scripts", "fold_check.py")


fold_check = load_module(SCRIPT, "specseal_fold_check")


def declared():
    """`(ceiling, policy root)` as this repository's `seal/config.md` states
    them, read by the shipped command's own reader."""
    return fold_check.declared(fold_check.seal_home(ROOT))


def command(*args):
    """`fold-check` as a person types it, run on this interpreter."""
    done = subprocess.run(
        [sys.executable, SCRIPT, *args],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    return done.returncode, done.stdout, done.stderr


def test_this_repository_passes_the_command_with_no_flags():
    """S1 and S13: the values come from `seal/config.md`, every check runs,
    and a document past the ceiling is named and does not fail the run."""
    code, out, err = command("--root", ROOT)
    assert code == 0, (out, err)
    ceiling, policy = declared()
    assert f" under {policy}/ to {ceiling} estimated tokens" in out, out
    for rel, tokens in fold_check.past_ceiling(ROOT, policy, ceiling):
        assert f"{rel} is about {tokens} tokens, past the ceiling" in out, out
    assert f"fold-check: the index {policy}/README.md names every document" in out


# --- the estimate and the ceiling ----------------------------------------------


def tree(tmp_path, files, policy="docs"):
    (tmp_path / policy).mkdir()
    for name, text in files.items():
        (tmp_path / policy / name).write_text(text, encoding="utf-8")
    return str(tmp_path)


def test_the_estimate_is_utf8_bytes_halved_rounded_up():
    assert [fold_check.tokens(t) for t in ("", "ab", "abc", "한")] == [0, 1, 2, 2]


def test_a_document_past_the_ceiling_is_named_and_the_run_exits_0(tmp_path):
    """S12: the owner's answer of 2026-10-20 makes the ceiling a report. A
    document one token past it is named as one to split; one at it is not."""
    root = tree(tmp_path, {"big.md": "x" * 50001, "at.md": "x" * 50000})
    code, out, err = command("--root", root, "--ceiling", "25000")
    assert code == 0, (code, out, err)
    assert (
        "fold-check: docs/big.md is about 25001 tokens, past the ceiling of "
        "25000: split it along its own headings\n"
    ) in out, out
    assert "docs/at.md is about" not in out, out
    assert "held 2 documents under docs/ to 25000 estimated tokens, 1 past it\n" in out


def test_the_command_refuses_a_ceiling_that_is_not_a_positive_integer(tmp_path):
    root = tree(tmp_path, {"small.md": "x\n"})
    for value in ("0", "ten"):
        code, out, err = command("--root", root, "--ceiling", value)
        assert code == 2 and not out, (value, out, err)


# --- the index -------------------------------------------------------------------


INDEX = "| File | The question it answers |\n|---|---|\n"


@pytest.mark.parametrize(
    "rows, says",
    [
        (
            "| `docs/a.md` | a |\n",
            "docs/README.md has no row naming docs/b.md",
        ),
        (
            "| `docs/a.md` | a |\n| `docs/b.md` | b |\n| `docs/a.md` again | a |\n",
            "docs/README.md names docs/a.md on 2 rows",
        ),
        (
            "| `docs/a.md` | a |\n| `docs/b.md` | b |\n| a topic | with no file |\n",
            "docs/README.md:5 names no document of docs/",
        ),
    ],
    ids=["missing", "twice", "no file"],
)
def test_an_index_that_misses_doubles_or_names_nothing_is_refused(tmp_path, rows, says):
    """S13, each refusal at exit 1, its message pinned (contract rule 14)."""
    root = tree(tmp_path, {"a.md": "# A\n", "b.md": "# B\n", "README.md": INDEX + rows})
    code, out, err = command("--root", root)
    assert code == 1, (code, out, err)
    assert f"{says}\n" in out, out


def test_an_index_naming_each_document_once_passes(tmp_path):
    """An edition goes on its English edition's row, and the index names
    itself nowhere."""
    rows = "| `docs/a.md` and `docs/a.ko.md` | a |\n| `docs/b.md` | b |\n"
    files = {"a.md": "# A\n", "a.ko.md": "# A\n", "b.md": "# B\n"}
    root = tree(tmp_path, {**files, "README.md": INDEX + rows})
    code, out, err = command("--root", root)
    assert code == 0, (code, out, err)
    assert "fold-check: the index docs/README.md names every document\n" in out


def test_with_no_index_the_index_is_not_checked_and_the_run_says_so(tmp_path):
    root = tree(tmp_path, {"a.md": "# A\n"})
    code, out, _ = command("--root", root, "--ceiling", "10")
    assert code == 0, out
    assert "fold-check: there is no docs/README.md, so no index was checked\n" in out


# --- the rows --------------------------------------------------------------------


def config_root(tmp_path, rows, policy="docs"):
    """A planted repository whose `seal/config.md` carries `rows` under the
    table header, with one short document under the policy root."""
    (tmp_path / policy).mkdir()
    (tmp_path / policy / "a.md").write_text("# A\n", encoding="utf-8")
    (tmp_path / "seal").mkdir()
    table = "".join(f"| {item} | {value} |\n" for item, value in rows)
    (tmp_path / "seal" / "config.md").write_text(
        f"# Repository config\n\n| Item | Value |\n|---|---|\n{table}",
        encoding="utf-8",
    )
    return str(tmp_path)


def test_a_root_that_declares_no_ceiling_and_has_no_index_checks_nothing(tmp_path):
    """S4. Absent means not declared, as every optional row does; the line
    names the row and the file it was looked for in (contract rule 14)."""
    root = config_root(tmp_path, [("Mode", "shared")])
    code, out, err = command("--root", root)
    config = os.path.join(root, "seal", "config.md")
    assert code == 0, (out, err)
    assert out == (
        f"fold-check: `Document token ceiling` is not declared in {config}, and "
        "there is no docs/README.md, so nothing was checked\n"
    ), out


@pytest.mark.parametrize("row", ["Document line ceiling", "Fold shape from"])
def test_a_retired_row_is_no_longer_read(tmp_path, row):
    """S12: `Document token ceiling` replaced the line row, and the shape the
    cutoff row bound left with its markers, so a repository that still
    writes either has declared nothing."""
    root = config_root(tmp_path, [(row, "1")])
    code, out, err = command("--root", root)
    config = os.path.join(root, "seal", "config.md")
    assert code == 0, (out, err)
    assert out == (
        f"fold-check: `Document token ceiling` is not declared in {config}, and "
        "there is no docs/README.md, so nothing was checked\n"
    ), out


def test_a_row_with_an_empty_value_is_not_declared(tmp_path):
    """The template writes a row it leaves open with an empty cell, as it does
    `Mode` and `Broad gate`; an empty cell is no value, not a bad one."""
    root = config_root(tmp_path, [("Document token ceiling", ""), ("Policy root", "")])
    code, out, err = command("--root", root)
    assert code == 0, (out, err)
    assert "`Document token ceiling` is not declared in" in out, out


def test_an_absent_ceiling_skips_its_check_and_says_so(tmp_path):
    """With an index to read, the run goes on and says in one line which
    check it did not run (contract rule 14)."""
    root = config_root(tmp_path, [("Mode", "shared")])
    (tmp_path / "docs" / "README.md").write_text(
        f"{INDEX}| `docs/a.md` | a |\n", encoding="utf-8"
    )
    code, out, _ = command("--root", root)
    config = os.path.join(root, "seal", "config.md")
    assert code == 0, out
    assert out == (
        f"fold-check: `Document token ceiling` is not declared in {config}, so "
        "no document's length was checked\n"
        "fold-check: the index docs/README.md names every document\n"
    ), out


def test_the_policy_root_row_moves_every_check_there(tmp_path):
    """S14's reader half: the row names where the documents are, and
    nothing under `docs/` is read."""
    root = config_root(
        tmp_path, [("Policy root", "policy"), ("Document token ceiling", "1")], "policy"
    )
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "ignored.md").write_text("x" * 99, encoding="utf-8")
    code, out, _ = command("--root", root)
    assert code == 0, out
    assert "policy/a.md is about 2 tokens, past the ceiling of 1" in out, out
    assert "docs/" not in out, out


@pytest.mark.parametrize(
    "row, value, says",
    [
        (
            "Document token ceiling",
            "ten",
            "the `Document token ceiling` row holds `ten`, which is not a "
            "positive whole number of tokens",
        ),
    ],
)
def test_a_row_that_will_not_parse_is_named_and_nothing_is_checked(
    tmp_path, row, value, says
):
    """S5, its message pinned (contract rule 14)."""
    root = config_root(tmp_path, [(row, value)])
    code, out, err = command("--root", root)
    config = os.path.join(root, "seal", "config.md")
    assert code == 2 and not out, (out, err)
    assert err == f"fold-check: in {config}, {says} — nothing was checked\n", err


@pytest.mark.parametrize("row", ["Document token ceiling"])
def test_a_row_written_twice_is_refused_and_nothing_is_checked(tmp_path, row):
    """S1 of #867, `fold-check`'s half. A row written twice has no value, by
    `hooks/config.py#value_of`'s rule: the run exits 2 naming the row and the
    count, and nothing is checked."""
    root = config_root(tmp_path, [(row, "10"), (row, "20")])
    code, out, err = command("--root", root)
    config = os.path.join(root, "seal", "config.md")
    assert code == 2 and not out, (out, err)
    assert err == (
        f"fold-check: in {config}, `{row}` appears 2 times — one value — nothing "
        "was checked\n"
    ), err


def test_a_row_the_walker_did_not_read_is_refused_and_nothing_is_checked(tmp_path):
    """S4 of #871, `fold-check`'s case. A `Document token ceiling` row under
    a line the table walker refuses is one it never read, so the run exits 2
    in the walker's sentence, naming the line, and nothing is checked. A
    refusal below every row this command reads touches none of them, so
    that table is read and checked."""
    (tmp_path / "under").mkdir()
    (tmp_path / "below").mkdir()
    root = config_root(
        tmp_path / "under",
        [
            ("Mode", "shared"),
            ("Broad gate", "bin/test -q | tee out"),
            ("Document token ceiling", "10"),
        ],
    )
    code, out, err = command("--root", root)
    assert code == 2 and not out, (out, err)
    assert "stops at `| Broad gate | bin/test -q | tee out |`" in err, err
    assert err.endswith("— nothing was checked\n"), err

    root = config_root(
        tmp_path / "below",
        [
            ("Document token ceiling", "10"),
            ("Policy root", "docs"),
            ("Broad gate", "bin/test -q | tee out"),
        ],
    )
    code, out, err = command("--root", root)
    assert code == 0, (out, err)
    assert "held 1 document under docs/ to 10 estimated tokens" in out, out


@pytest.mark.parametrize("shape", ["directory", "undecodable"])
def test_an_unreadable_config_is_refused_not_read_as_no_row(tmp_path, shape):
    """S3 of #867, `fold-check`'s half. A `config.md` that is there and will
    not read is refused at exit 2 naming the path, never read as no row."""
    root = config_root(tmp_path, [("Document token ceiling", "10")])
    config = tmp_path / "seal" / "config.md"
    config.unlink()
    if shape == "directory":
        config.mkdir()
    else:
        config.write_bytes(
            b"| Item | Value |\n|---|---|\n| Document token ceiling | 10 \xff |\n"
        )
    code, out, err = command("--root", root)
    assert code == 2 and not out, (out, err)
    assert f"{config} is there and cannot be read" in err, err
    assert err.endswith("— nothing was checked\n"), err


def test_a_flag_overrides_its_row_for_one_run(tmp_path):
    root = config_root(tmp_path, [("Document token ceiling", "10")])
    (tmp_path / "docs" / "long.md").write_text("x" * 22, encoding="utf-8")
    code, out, _ = command("--root", root)
    assert code == 0 and "docs/long.md is about 11 tokens" in out, out
    code, out, _ = command("--root", root, "--ceiling", "11")
    assert code == 0 and "docs/long.md is about" not in out, out
    assert (tmp_path / "seal" / "config.md").read_text(encoding="utf-8").count(
        "| Document token ceiling | 10 |"
    ) == 1


# --- where it reads --------------------------------------------------------------


def git_init(root):
    subprocess.run(["git", "init", "-q", root], check=True, capture_output=True)


def test_the_command_typed_in_a_subdirectory_reads_the_repository(tmp_path):
    """Round 1, finding 1: typed in `docs/`, the rows and the documents are the
    repository's, so a run one directory too deep does not pass unchecked."""
    root = config_root(tmp_path, [("Document token ceiling", "10")])
    git_init(root)
    (tmp_path / "docs" / "long.md").write_text("x" * 22, encoding="utf-8")
    done = subprocess.run(
        [sys.executable, SCRIPT],
        cwd=str(tmp_path / "docs"),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    assert done.returncode == 0, done.stdout + done.stderr
    assert "docs/long.md is about 11 tokens, past the ceiling of 10" in done.stdout


def test_an_opted_out_repository_is_told_it_opted_out(tmp_path):
    """Round 1, finding 3: it has a root, so "no seal/ root" would be false.
    Both of the states `home_at` answers "" for are pinned whole (contract rule 14)."""
    root = config_root(tmp_path, [("Document token ceiling", "10")])
    git_init(root)
    (tmp_path / ".git" / "specseal-scratch").write_text("", encoding="utf-8")
    code, out, err = command("--root", root)
    assert code == 0, (out, err)
    assert out == (
        f"fold-check: `Document token ceiling` is not declared in {root}, which "
        "has opted out — `specseal-scratch` is under its git directory, so its "
        "seal/config.md is not read, and there is no docs/README.md, so nothing "
        "was checked\n"
    ), out


def test_a_repository_with_no_root_is_told_it_has_none(tmp_path):
    (tmp_path / "docs").mkdir()
    git_init(str(tmp_path))
    code, out, err = command("--root", str(tmp_path))
    assert code == 0, (out, err)
    assert out == (
        f"fold-check: `Document token ceiling` is not declared in {tmp_path}, "
        "which has no seal/ root at either place, and there is no "
        "docs/README.md, so nothing was checked\n"
    ), out


def test_a_fold_row_written_again_below_the_stop_has_no_value(tmp_path):
    """#871 round 2, yellow 9. A row read above a line the walk refused and
    written again below it has no value, in fold-check as in
    `config_value`."""
    (tmp_path / "config.md").write_text(
        "# c\n\n| Item | Value |\n|---|---|\n"
        "| Document token ceiling | 400 |\n| Policy root | docs |\n"
        "| a | b | c |\n| Document token ceiling | 9000 |\n",
        encoding="utf-8",
    )
    with pytest.raises(fold_check.Unusable, match="appears 2 times"):
        fold_check.declared(str(tmp_path))


# --- the prose that states the rule ----------------------------------------------


@pytest.mark.parametrize("edition", ["README.md", "README.ko.md"])
def test_both_cheat_sheets_point_to_the_checks_home(edition):
    """Round 1, finding 9: the `fold-check` row described the freeze after it
    was gone. It now points to the rows' one statement and restates none."""
    with open(os.path.join(ROOT, edition), encoding="utf-8") as f:
        row = next(line for line in f if line.startswith("| `fold-check [--ceiling"))
    assert "`templates/config.md` *The fold's values*" in row, row
    assert "frozen" not in row and "고정" not in row, row


def test_settle_owns_the_placement_rule():
    """A11. The rule is settle's, in general form, and it sets no value."""
    with open(
        os.path.join(ROOT, "skills", "settle", "SKILL.md"), encoding="utf-8"
    ) as f:
        text = f.read()
    section = text.split("\n## A document past its ceiling is split, never trimmed\n")
    section = " ".join(section[1].split("\n## ")[0].split())
    for phrase in (
        "is recommended to be split by topic along its own headings",
        "nothing is cut to fit",
        "The plugin sets no ceiling",
    ):
        assert phrase in section, f"settle no longer says: {phrase!r}"
