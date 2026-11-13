"""`skills/settle/scripts/fold_check.py`, one class per function.

A document fits one read, and the policy root has one index (#953).
`seal fold` reports each document of the policy root or of one of its groups whose
estimate is past the `Document token ceiling` key as one to split by who
opens each section and at which step, and exits 0 on it: the estimate is a guess from bytes, so it is
a report and not a gate. Its index arm refuses a `<policy root>/README.md`
that misses a document, names one twice, or holds a row naming none. The
keys and the estimate are stated once, in `templates/setup/config.md` *The fold's
values*. Every case but two runs the command; `Test_module` holds the
estimate, a copy of the command run without its siblings, and the line
splitter this module no longer keeps.

#942's phase 6 placed these cases from
`tests/text/test_a_document_has_room_for_the_next_fold.py`, which keeps the two
cases that read the cheat sheets and the settle skill. Its round 9 fix pass
placed the copy's case from `tests/test_a_script_copied_alone_exits_2.py`
and the splitter's from `tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py`,
each a case of this module alone.

The cases that run the command beside a project's own `seal/` package
(#1059) build `tests/conftest.py`'s `package` or `shared` repository for
each case, whose root stands at `agentic-seal/`.
"""

import os
import subprocess
import sys

import pytest
from conftest import ROOT, census_case, config_json, load_module, mark_root, write
from test_seal import configured, tool

TARGET = "skills/settle/scripts/fold_check.py"

SCRIPT = os.path.join(ROOT, "skills", "settle", "scripts", "fold_check.py")

fold_check = load_module(SCRIPT, "agentic_fold_check")


def command(*args):
    """`seal fold` as a person types it, run on this interpreter."""
    done = subprocess.run(
        [sys.executable, SCRIPT, *args],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    return done.returncode, done.stdout, done.stderr


def tree(tmp_path, files, policy="docs"):
    (tmp_path / policy).mkdir()
    for name, text in files.items():
        (tmp_path / policy / name).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / policy / name).write_text(text, encoding="utf-8")
    return str(tmp_path)


INDEX = "| File | The question it answers |\n|---|---|\n"


def config_root(tmp_path, rows, policy="docs"):
    """A planted repository whose `seal/config.json` holds `rows` as its
    keys, with one short document under the policy root."""
    (tmp_path / policy).mkdir()
    (tmp_path / policy / "a.md").write_text("# A\n", encoding="utf-8")
    mark_root(tmp_path / "seal")
    (tmp_path / "seal" / "config.json").write_text(config_json(*rows), encoding="utf-8")
    return str(tmp_path)


def git_init(root):
    subprocess.run(["git", "init", "-q", root], check=True, capture_output=True)


class Test_main:
    def test_a_document_past_the_ceiling_is_named_and_the_run_exits_0(self, tmp_path):
        """S12: the owner's answer of 2026-10-20 makes the ceiling a report. A
        document one token past it is named as one to split; one at it is not."""
        root = tree(tmp_path, {"big.md": "x" * 50001, "at.md": "x" * 50000})
        code, out, err = command("--root", root, "--ceiling", "25000")
        assert code == 0, (code, out, err)
        assert (
            "seal fold: docs/big.md is about 25001 tokens, past the ceiling of "
            "25000: split it by who opens each section and at which step\n"
        ) in out, out
        assert "docs/at.md is about" not in out, out
        assert (
            "held 2 documents under docs/ to 25000 estimated tokens, 1 past it\n" in out
        )

    def test_refuses_a_ceiling_that_is_not_a_positive_integer(self, tmp_path):
        root = tree(tmp_path, {"small.md": "x\n"})
        for value in ("0", "ten"):
            code, out, err = command("--root", root, "--ceiling", value)
            assert code == 2 and not out, (value, out, err)

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
    def test_an_index_that_misses_doubles_or_names_nothing_is_refused(
        self, tmp_path, rows, says
    ):
        """S13, each refusal at exit 1, its message pinned (contract rule 14)."""
        root = tree(
            tmp_path, {"a.md": "# A\n", "b.md": "# B\n", "README.md": INDEX + rows}
        )
        code, out, err = command("--root", root)
        assert code == 1, (code, out, err)
        assert f"{says}\n" in out, out

    def test_accepts_an_index_naming_each_document_once(self, tmp_path):
        """An edition goes on its English edition's row, and the index names
        itself nowhere."""
        rows = "| `docs/a.md` and `docs/a.ko.md` | a |\n| `docs/b.md` | b |\n"
        files = {"a.md": "# A\n", "a.ko.md": "# A\n", "b.md": "# B\n"}
        root = tree(tmp_path, {**files, "README.md": INDEX + rows})
        code, out, err = command("--root", root)
        assert code == 0, (code, out, err)
        assert "seal fold: the index docs/README.md names every document\n" in out

    def test_a_group_the_index_names_is_read_and_no_other_directory_is(self, tmp_path):
        """#1312 S6: a directory of the policy root that the index names a
        document of is a group, and each `.md` directly in it is measured
        against the ceiling and held to one index row. A directory the index
        names nothing of, such as `docs/experiments/`, a directory below a
        group, and `..` named as one are not read, however large their
        documents."""
        big = "x" * 50001
        rows = "| `docs/a.md` | a |\n| `docs/g/x.md` | x |\n| `docs/../out.md` | o |\n"
        files = {
            "a.md": "# A\n",
            "g/x.md": big,
            "g/y.md": "# Y\n",
            "g/deep/z.md": big,
            "experiments/e.md": big,
            "../out.md": big,
            "README.md": INDEX + rows,
        }
        code, out, err = command("--root", tree(tmp_path, files), "--ceiling", "25000")
        assert code == 1, (code, out, err)
        assert (
            "held 4 documents under docs/ to 25000 estimated tokens, 1 past it\n"
        ) in out, out
        assert "seal fold: docs/g/x.md is about 25001 tokens, past the ceiling" in out
        assert "docs/README.md has no row naming docs/g/y.md\n" in out, out
        assert "docs/README.md:5 names no document of docs/\n" in out, out
        assert "deep" not in out and "experiments" not in out, out
        assert "out.md" not in out, out
        _, shown, _ = command("--help")
        assert "of the policy root or of one of its groups" in " ".join(shown.split())

    def test_with_no_index_the_index_is_not_checked_and_the_run_says_so(self, tmp_path):
        root = tree(tmp_path, {"a.md": "# A\n"})
        code, out, _ = command("--root", root, "--ceiling", "10")
        assert code == 0, out
        assert "seal fold: there is no docs/README.md, so no index was checked\n" in out

    def test_a_root_that_declares_no_ceiling_and_has_no_index_checks_nothing(
        self, tmp_path
    ):
        """S4. Absent means not declared, as every optional row does; the line
        names the row and the file it was looked for in (contract rule 14)."""
        root = config_root(tmp_path, [("Mode", "shared")])
        code, out, err = command("--root", root)
        config = os.path.join(root, "seal", "config.json")
        assert code == 0, (out, err)
        assert out == (
            f"seal fold: `Document token ceiling` is not declared in {config}, and "
            "there is no docs/README.md, so nothing was checked\n"
        ), out

    @pytest.mark.parametrize("row", ["Document line ceiling", "Fold shape from"])
    def test_a_retired_row_is_no_longer_read(self, tmp_path, row):
        """S12: `Document token ceiling` replaced the line row, and the shape the
        cutoff row bound left with its markers, so a repository that still
        writes either has declared nothing."""
        root = config_root(tmp_path, [(row, "1")])
        code, out, err = command("--root", root)
        config = os.path.join(root, "seal", "config.json")
        assert code == 0, (out, err)
        assert out == (
            f"seal fold: `Document token ceiling` is not declared in {config}, and "
            "there is no docs/README.md, so nothing was checked\n"
        ), out

    def test_a_row_with_an_empty_value_is_not_declared(self, tmp_path):
        """The template writes a row it leaves open with an empty cell, as it does
        `Mode` and `Broad gate`; an empty cell is no value, not a bad one."""
        root = config_root(
            tmp_path, [("Document token ceiling", ""), ("Policy root", "")]
        )
        code, out, err = command("--root", root)
        assert code == 0, (out, err)
        assert "`Document token ceiling` is not declared in" in out, out

    def test_an_absent_ceiling_skips_its_check_and_says_so(self, tmp_path):
        """With an index to read, the run goes on and says in one line which
        check it did not run (contract rule 14)."""
        root = config_root(tmp_path, [("Mode", "shared")])
        (tmp_path / "docs" / "README.md").write_text(
            f"{INDEX}| `docs/a.md` | a |\n", encoding="utf-8"
        )
        code, out, _ = command("--root", root)
        config = os.path.join(root, "seal", "config.json")
        assert code == 0, out
        assert out == (
            f"seal fold: `Document token ceiling` is not declared in {config}, so "
            "no document's length was checked\n"
            "seal fold: the index docs/README.md names every document\n"
        ), out

    def test_the_policy_root_row_moves_every_check_there(self, tmp_path):
        """S14's reader half: the row names where the documents are, and
        nothing under `docs/` is read."""
        root = config_root(
            tmp_path,
            [("Policy root", "policy"), ("Document token ceiling", "1")],
            "policy",
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
                "the `Document token ceiling` key holds `ten`, which is not a "
                "positive whole number of tokens",
            ),
        ],
    )
    def test_a_row_that_will_not_parse_is_named_and_nothing_is_checked(
        self, tmp_path, row, value, says
    ):
        """S5, its message pinned (contract rule 14)."""
        root = config_root(tmp_path, [(row, value)])
        code, out, err = command("--root", root)
        config = os.path.join(root, "seal", "config.json")
        assert code == 2 and not out, (out, err)
        assert err == f"seal fold: in {config}, {says} — nothing was checked\n", err

    @pytest.mark.parametrize("row", ["Document token ceiling"])
    def test_a_row_written_twice_is_refused_and_nothing_is_checked(self, tmp_path, row):
        """S1 of #867, `seal fold`'s half. A key written twice has no value, by
        `lib/config.py#config_value`'s rule: the run exits 2 naming the key and
        the count, and nothing is checked."""
        root = config_root(tmp_path, [(row, "10"), (row, "20")])
        code, out, err = command("--root", root)
        config = os.path.join(root, "seal", "config.json")
        assert code == 2 and not out, (out, err)
        assert err == (
            f"seal fold: in {config}, `{row}` appears 2 times — one value — nothing "
            "was checked\n"
        ), err

    @pytest.mark.parametrize(
        "shape, said",
        [
            ("directory", "is there and cannot be read"),
            ("undecodable", "is there and cannot be read"),
            ("unparseable", "does not parse as JSON"),
        ],
    )
    def test_an_unreadable_config_is_refused_not_read_as_no_row(
        self, tmp_path, shape, said
    ):
        """S3 of #867 and S2 of #1454, `seal fold`'s half. A `config.json`
        that is there and will not read or parse is refused at exit 2 naming
        the path, never read as no key, and nothing is checked."""
        root = config_root(tmp_path, [("Document token ceiling", "10")])
        config = tmp_path / "seal" / "config.json"
        config.unlink()
        if shape == "directory":
            config.mkdir()
        elif shape == "undecodable":
            config.write_bytes(b'{"Document token ceiling": "10 \xff"}\n')
        else:
            config.write_bytes(b'{"Document token ceiling": "10",}\n')
        code, out, err = command("--root", root)
        assert code == 2 and not out, (out, err)
        assert f"{config} " in err and said in err, err
        assert err.endswith("— nothing was checked\n"), err

    def test_a_flag_overrides_its_row_for_one_run(self, tmp_path):
        root = config_root(tmp_path, [("Document token ceiling", "10")])
        (tmp_path / "docs" / "long.md").write_text("x" * 22, encoding="utf-8")
        code, out, _ = command("--root", root)
        assert code == 0 and "docs/long.md is about 11 tokens" in out, out
        code, out, _ = command("--root", root, "--ceiling", "11")
        assert code == 0 and "docs/long.md is about" not in out, out
        assert (tmp_path / "seal" / "config.json").read_text(encoding="utf-8").count(
            '"Document token ceiling": "10"'
        ) == 1

    def test_the_command_typed_in_a_subdirectory_reads_the_repository(self, tmp_path):
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

    def test_an_opted_out_repository_is_told_it_opted_out(self, tmp_path):
        """Round 1, finding 3: it has a root, so "no seal/ root" would be false.
        Both of the states `home_at` answers "" for are pinned whole (contract rule 14)."""
        root = config_root(tmp_path, [("Document token ceiling", "10")])
        git_init(root)
        (tmp_path / ".git" / "agentic-scratch").write_text("", encoding="utf-8")
        code, out, err = command("--root", root)
        assert code == 0, (out, err)
        assert out == (
            f"seal fold: `Document token ceiling` is not declared in {root}, which "
            "has opted out — `agentic-scratch` is under its git directory, so its "
            "seal/config.json is not read, and there is no docs/README.md, so nothing "
            "was checked\n"
        ), out

    def test_a_repository_with_no_root_is_told_it_has_none(self, tmp_path):
        (tmp_path / "docs").mkdir()
        git_init(str(tmp_path))
        code, out, err = command("--root", str(tmp_path))
        assert code == 0, (out, err)
        assert out == (
            f"seal fold: `Document token ceiling` is not declared in {tmp_path}, "
            "which has no seal/ root at either place, and there is no "
            "docs/README.md, so nothing was checked\n"
        ), out

    def test_s5_fold_reads_its_keys_from_agentic_seal(self, shared):
        """`seal fold` reads `Policy root` and `Document token ceiling` from
        `agentic-seal/config.json`, so the documents it holds to the ceiling are
        the ones under the root that key names."""
        configured(
            shared / "agentic-seal",
            ("Policy root", "policy"),
            ("Document token ceiling", "1"),
        )
        write(shared, "policy/a.md", "# A\n")
        code, out, err = tool(shared, "fold")
        assert code == 0, err
        assert "policy/a.md is about 2 tokens, past the ceiling of 1" in out, out


class Test_module:
    def test_the_estimate_is_utf8_bytes_halved_rounded_up(self):
        assert [fold_check.tokens(t) for t in ("", "ab", "abc", "한")] == [0, 1, 2, 2]

    @pytest.mark.parametrize(
        "args", [["--root", "{root}"], ["--help"]], ids=["a-run", "help"]
    )
    def test_a_script_copied_alone_exits_2_and_names_what_it_misses(
        self, tmp_path, args
    ):
        """#590, and S4 of #1482. A copy of this script taken without its
        siblings exits 2, with the loader's one sentence naming the absent
        `lib/sibling.py` by its path: 2 means the input or the tree was
        unusable and nothing was read, and a sibling that is not beside the
        command is that kind. The sentence names no purpose (#1482). `--help` reaches the sentence too, because the guard stands at
        import and reads no argument (#1482, A13)."""
        script = TARGET
        name = script.rsplit("/", 1)[1]
        alone = tmp_path / "alone"
        alone.mkdir()
        copy = alone / name
        with open(os.path.join(ROOT, *script.split("/")), encoding="utf-8") as f:
            copy.write_text(f.read(), encoding="utf-8")
        repo = tmp_path / "repo"
        repo.mkdir()
        done = subprocess.run(
            [sys.executable, str(copy), *(a.format(root=repo) for a in args)],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            cwd=str(repo),
        )
        assert done.returncode == 2, (done.returncode, done.stderr)
        lib = os.path.join(str(alone), "..", "..", "..", "lib", "sibling.py")
        said = fold_check.sibling.MISSING.format(path=os.path.normpath(lib))
        assert done.stderr == said + "\n", done.stderr

    def test_fold_check_keeps_no_copy_of_its_own(self):
        """The copy `fold_check.py` held while the reader was being rewritten on
        another branch is gone: a line ends where `lib/blocks.py#gfm_lines`
        ends it (#664)."""
        assert not hasattr(fold_check, "gfm_lines")
        assert not hasattr(fold_check, "GFM_LINE_RE")


test_census = census_case(TARGET)
