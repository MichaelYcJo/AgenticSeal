"""`hooks/config.py`, the shared reader of `seal/config.md` and the pact's
tables, one class per function its cases reach.

#942's phase 6 placed here the reference-root reader's cases from
`tests/test_a_reference_root_is_read_and_never_taken.py`, the policy root's
from `tests/test_a_document_has_room_for_the_next_fold.py`, the remote
normaliser's from `tests/test_the_records_can_be_carried_out_and_in.py`, the
`Baseline commit` reader's from `tests/test_chain_check.py`, the row reader's
from `tests/test_the_pull_request_language_is_the_repositorys.py` and three
of the table walker's from
`tests/test_one_table_walker_reads_what_gfm_renders.py`, which keeps the
walker held to cmark-gfm. Each case keeps its body; a name its old file
defined for it is defined here.
"""

import importlib.util
import os
import subprocess

import pytest
from conftest import (
    BASELINE,
    ROOT,
    census_case,
    load_hook_module,
    load_module,
    parity_file,
    write_config,
)
from conftest import config_table as table

TARGET = "hooks/config.py"

config = load_hook_module("config.py", "config_under_test")

# `seal.py`, which re-exports `normalise_remote`: the normaliser's cases ask
# it by that name, through the `seal` fixture below.
SCRIPT = os.path.join(ROOT, "skills", "implement", "scripts", "seal.py")

# The `Baseline commit` case asks the reader `chain_check.py` loads for the
# parity arm, as the command reaches it.
chain = load_module(
    os.path.join(ROOT, "skills", "code-review", "scripts", "chain_check.py"),
    "chain_check_for_config",
)

# The row reader's cases call `config_rows` as `items` and the module through
# `_config_reader()`, the names their old file gave them.
LANGUAGE_ROW = "Commit and pull request language"
items = config.config_rows


def _config_reader():
    """This file's `hooks/config.py`; the old file loaded a copy per call."""
    return config


@pytest.fixture
def seal():
    spec = importlib.util.spec_from_file_location("specseal_seal", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Test_reference_roots:
    def test_accepts_a_row_naming_its_prefixes_with_or_without_a_slash(self, tmp_path):
        """Present: the prefixes it names, normalised, and nothing else."""
        home = str(tmp_path / "seal")
        write_config(
            home,
            table(
                ("Reference specs", "specs/, docs/adr ,./design/, specs, tools\\notes")
            ),
        )
        roots = config.reference_roots(home)
        assert roots == ("specs", "docs/adr", "design", "tools/notes"), roots
        for rel in (
            "specs/x/spec.md",
            "docs/adr/0001.md",
            "design/a.md",
            "specs",
            "./specs/x.md",
            "tools/notes/n.md",
        ):
            assert config.under_reference_root(rel, roots), rel
        for rel in ("docs/adrs/0001.md", "docs/specs/x.md", "src/specs.py", "spec/x"):
            assert not config.under_reference_root(rel, roots), rel

    def test_no_row_means_every_specs_directory_outside_the_root(
        self, tmp_path, monkeypatch
    ):
        """Absent, empty or unreadable: the ticket's default, at any depth."""
        home = str(tmp_path / "seal")
        for body in (None, table(("Mode", "shared")), table(("Reference specs", ""))):
            if body is not None:
                write_config(home, body)
            roots = config.reference_roots(home)
            assert roots is None, (body, roots)
            for rel in (
                "specs/x/spec.md",
                "docs/specs/y.md",
                "a/b/specs/c/d.md",
                "specs\\x\\spec.md",
            ):
                assert config.under_reference_root(rel, roots), rel
            for rel in (
                "seal/specs/1790000000-x/spec.md",
                "docs/spec.md",
                "specsheet/a",
            ):
                assert not config.under_reference_root(rel, roots), rel
        # No root at either place is no reference root at all: the repository has
        # not opted in, and the 0.3.x `specs/` the checks still read was the
        # plugin's own. Never a `config.md` found relative to wherever the
        # process happens to stand, either.
        stray = tmp_path / "elsewhere"
        write_config(str(stray), table(("Reference specs", "docs/adr")))
        monkeypatch.chdir(stray)
        assert config.reference_roots("") == ()
        assert not config.under_reference_root("specs/x/spec.md", ())

    def test_refuses_a_row_written_twice_or_a_file_that_will_not_read(self, tmp_path):
        """#867. A `Reference specs` row written twice has no value, by
        `hooks/config.py#config_value`'s rule; the reader used to take the
        first. A file that is there and will not read is the default too, as it
        was, and the reader no longer opens the file itself to find out. Seen red
        against the first-wins reader: `('docs/adr',)`."""
        home = str(tmp_path / "seal")
        write_config(
            home, table(("Reference specs", "docs/adr"), ("Reference specs", "none"))
        )
        assert config.reference_roots(home) is None
        os.remove(os.path.join(home, "config.md"))
        os.mkdir(os.path.join(home, "config.md"))
        assert config.reference_roots(home) is None

    def test_none_declares_no_reference_root(self, tmp_path):
        home = str(tmp_path / "seal")
        write_config(home, table(("Reference specs", "None")))
        roots = config.reference_roots(home)
        assert roots == (), roots
        assert not config.under_reference_root("specs/x/spec.md", roots)

    def test_a_row_inside_a_fence_is_not_a_row(self, tmp_path):
        """`hooks/config.py#unfenced` filters in front of the table walk, so a
        row quoted in a fence above the live table is an example."""
        home = str(tmp_path / "seal")
        write_config(
            home,
            "# config\n\n```markdown\n| Item | Value |\n|---|---|\n"
            "| Reference specs | none |\n```\n\n"
            + table(("Mode", "shared")).split("\n\n", 1)[1],
        )
        assert config.reference_roots(home) is None

    def test_the_plugins_own_root_is_never_a_reference_root(self, tmp_path):
        """A reference root is outside the root by definition; a prefix naming
        `seal/` or anything under it is dropped, and the default never reaches
        `seal/specs/` either."""
        home = str(tmp_path / "seal")
        write_config(home, table(("Reference specs", "seal/specs, seal, specs")))
        roots = config.reference_roots(home)
        assert roots == ("specs",), roots
        assert not config.under_reference_root("seal/specs/1790000000-x/spec.md", roots)
        assert not config.under_reference_root("seal/specs/1790000000-x/spec.md", None)
        optin = load_hook_module("optin.py", "optin_for_the_root_name")
        assert config.HOME == optin.HOME, "the reader spells the root another way"

    def test_local_mode_reads_the_row_under_the_git_directory(self, tmp_path):
        """In local mode the root sits under the common git directory and nothing
        of it is in the tree, so with no row every tree `specs` is a reference
        root — and a row there is read like any other."""
        repo = tmp_path / "repo"
        repo.mkdir()
        subprocess.run(["git", "-C", str(repo), "init", "-q"], check=True)
        optin = load_hook_module("optin.py", "optin_for_reference_roots")
        common = optin.git_common_dir(str(repo))
        home = os.path.join(common, "seal")
        os.makedirs(home)
        assert optin.home_at(str(repo), common) == home, "the fixture is not local mode"
        assert config.reference_roots(home) is None
        assert config.under_reference_root("specs/x/spec.md", None)
        write_config(home, table(("Reference specs", "docs/adr")))
        assert config.reference_roots(home) == ("docs/adr",)


class Test_normalise_remote:
    @pytest.mark.parametrize(
        "left,right",
        [
            ("git@example.com:org/repo.git", "https://example.com/org/repo"),
            ("ssh://git@example.com/org/repo.git", "https://example.com/org/repo/"),
            ("HTTPS://Example.com/Org/Repo.git", "https://example.com/org/repo"),
        ],
    )
    def test_accepts_remote_urls_that_reduce_to_one_host_and_path(
        self, seal, left, right
    ):
        assert seal.normalise_remote(left) == seal.normalise_remote(right)

    def test_a_port_is_not_read_as_an_scp_separator(self, seal):
        """The colon becomes `/` only where there was no scheme. Otherwise
        `https://example.com:8443/x` reduces to `example.com/8443/x`, and two
        ports of one host stop comparing equal to themselves."""
        assert seal.normalise_remote("https://example.com:8443/org/repo") == (
            "example.com:8443/org/repo"
        )

    def test_refuses_to_reduce_two_different_repositories_to_one(self, seal):
        """The direction the normalisation must not be wrong in."""
        assert seal.normalise_remote(
            "git@example.com:org/a.git"
        ) != seal.normalise_remote("git@example.com:org/b.git")
        assert seal.normalise_remote("git@example.com:org/a") != seal.normalise_remote(
            "git@other.example:org/a"
        )


class Test_config_rows:
    def test_refuses_an_item_below_a_separator_out_of_place(self):
        """tests-todo row 9, from round 2 🟡 5, first shape — shape 8 of #871.
        cmark-gfm shows a stray separator as one of the table's rows, so the
        walker refuses it, naming it, and an item below it is that refusal
        rather than an absent row. The rows above it are read. Seen red against
        the stop rule, which ended the table there in silence."""
        text = (
            "| Item | Value |\n"
            "|---|---|\n"
            f"| {LANGUAGE_ROW} | Korean |\n"
            "|---|---|\n"
            "| Something else | x |\n"
        )
        reader = _config_reader()
        assert items(text) == [(LANGUAGE_ROW, "Korean")]
        value, said = reader.config_value(text, "Something else")
        assert (
            value is None
            and "stops at `|---|---|`, a delimiter row out of place" in (said or "")
        ), said

    def test_a_repeated_header_is_read_as_a_row_and_the_doubled_item_is_refused(
        self,
    ):
        """tests-todo row 9, second shape — shape 9 of #871. A second
        `| Item | Value |` line under the table with no delimiter row of its own
        is one of this table's rows to cmark-gfm, so the walker reads it as one,
        and the row below it with it: the language is then written twice, which
        has no value. Seen red against the stop rule, which ended the table at
        the repeated header and read `Korean`."""
        text = (
            "| Item | Value |\n"
            "|---|---|\n"
            f"| {LANGUAGE_ROW} | Korean |\n"
            "| Item | Value |\n"
            f"| {LANGUAGE_ROW} | English |\n"
        )
        reader = _config_reader()
        assert items(text) == [
            (LANGUAGE_ROW, "Korean"),
            ("Item", "Value"),
            (LANGUAGE_ROW, "English"),
        ]
        assert reader.config_value(text, LANGUAGE_ROW) == (
            None,
            f"`{LANGUAGE_ROW}` appears 2 times — one value",
        )

    def test_a_blank_line_above_the_first_row_ends_the_table_and_the_row_is_refused(
        self,
    ):
        """#871. A blank line under the delimiter row ends the table to
        cmark-gfm, so the row below it is not one of the table's rows: the
        walker refuses it as a row the walk never reaches, and the item it names
        is that refusal rather than an absent row. Seen red against the stop
        rule, which stepped past the blank line and read `Korean`."""
        text = f"| Item | Value |\n|---|---|\n\n| {LANGUAGE_ROW} | Korean |\n"
        assert items(text) == []
        value, said = _config_reader().config_value(text, LANGUAGE_ROW)
        assert value is None and "a row the walk never reaches" in (said or ""), said

    def test_accepts_an_item_value_table_and_no_other(self):
        """A parser that finds a row in anything is not a parser."""
        assert items("# a document with no table\n\nprose.\n") == []
        assert items("| Field | Value |\n|---|---|\n| a | b |\n") == [], (
            "`parity.md`'s header is `| Field | Value |`; matching it here would "
            "make this reader agree with a file it is not reading"
        )
        assert items("| Item | Value |\n|---|---|\n| a | b |\n") == [("a", "b")], (
            "the separator is being read as a row again"
        )

    def test_a_row_of_another_table_ends_this_one(self):
        """tests-todo row 3, from round 1 🟡 6.

        A three-cell row used to be skipped as though it were not there, so
        everything after it was absorbed. The interesting half is the LAST
        assertion: the danger was never the odd row itself, it was the ordinary
        row behind it arriving as though it belonged here.
        """
        text = (
            "| Item | Value |\n"
            "|---|---|\n"
            "| Commit and pull request language | Korean |\n"
            "| a | b | c |\n"
            "| Something else | x |\n"
        )
        assert items(text) == [("Commit and pull request language", "Korean")], (
            "a row of a different table did not end this one"
        )
        assert ("Something else", "x") not in items(text), (
            "the row behind the foreign one was read as part of this table"
        )

    def test_refuses_a_second_table_further_down_as_more_rows(self):
        """The same property at document scale, which is what `config.md`
        actually looks like: a table, prose, then another table."""
        text = (
            "| Item | Value |\n"
            "|---|---|\n"
            "| Commit and pull request language | Korean |\n"
            "\n"
            "## notes\n"
            "\n"
            "| Item | Value |\n"
            "|---|---|\n"
            "| Commit and pull request language | English |\n"
        )
        assert items(text) == [("Commit and pull request language", "Korean")], (
            "the first table's answer must win; a second one further down is "
            "prose about the first, not more rows of it"
        )


class Test_gfm_table:
    @pytest.mark.parametrize(
        "above",
        ["text\n```\nx\n```\n", "text\n" + "<" + "!-- c -->\n"],
        ids=[
            "a closed fence directly above, under a paragraph",
            "a closed comment directly above, under a paragraph",
        ],
    )
    def test_refuses_a_hidden_line_directly_above_the_header(self, above):
        """**The trade** (round 2, yellow 15). cmark-gfm renders both of these
        tables, and until round 2 the walker read them, because `unfenced` hides
        the closing fence or comment and the walk saw a gap above the header.
        The walker now judges the line above as written, hidden or not, because
        the same hidden line is what hid a header cmark-gfm does not render: a
        fence inside a kind 6-7 HTML block, or a list item a fence-only reading
        hid. So these are refused with the blank-line remedy, as a paragraph
        directly above already is (round 1, yellow 5). Every template and the
        writer leave the blank line."""
        text = f"# Pact\n\n{above}| Signer |\n|---|\n| https://example.com/org/a |\n"
        _rows, refusals = config.gfm_table(text, ("Signer",))
        assert refusals and "blank line above the header" in refusals[0], refusals

    @pytest.mark.parametrize("name", ["LS", "PS", "NEL", "FF", "VT", "FS", "GS", "RS"])
    def test_a_signer_after_a_break_gfm_does_not_honour_is_no_signer(self, name):
        """#871 round 2, the deferred half of yellow 7. A signer row after a
        character only `str.splitlines` ends a line at is more of the row above
        it to cmark-gfm, which shows one signer (measured for FF and U+2028 by
        the round's reviewer). The walk reads the first and refuses the second,
        for every table it walks, so `pact_signers` names one signer and the
        refusal. Seen red against 4dfb3d0d: two signers, no refusal."""
        from block_shapes import BREAKS

        a, b = "https://example.com/org/a", "https://example.com/org/b"
        text = f"# Pact\n\n| Signer |\n|---|\n| {a} |{BREAKS[name]}| {b} |\n"
        rows, refusals = config.gfm_table(text, ("Signer",))
        assert [c for _l, c in rows] == [(a,)], rows
        assert refusals and "not a row of its own to GFM" in refusals[0], refusals
        signers, said, _header = config.pact_signers(text)
        assert [s[0] for s in signers] == [a], signers
        assert any("not a row of its own to GFM" in s for s in said), said

    @pytest.mark.parametrize("name", ["LS", "FF"])
    def test_accepts_the_rows_above_a_heading_piece_and_refuses_the_row_below(
        self, name
    ):
        """#871 round 2, yellow 7's class after the table's end. A heading piece
        after a character only `str.splitlines` ends a line at is more of the
        line above to GFM, not a heading, so a line written `| … |` under it is
        still a row nobody reads, and is refused. Seen red against 4dfb3d0d,
        where the piece ended the walk's look for such rows."""
        from block_shapes import BREAKS

        text = (
            "| Item | Value |\n|---|---|\n| Mode | shared |\n\n"
            f"x{BREAKS[name]}## Notes\n| Broad gate | y |\n"
        )
        rows, refusals = config.gfm_table(text, ("Item", "Value"))
        assert [c for _l, c in rows] == [("Mode", "shared")], rows
        assert refusals and "ends above `| Broad gate | y |`" in refusals[0], refusals


class Test_module:
    @pytest.mark.parametrize(
        "value, root",
        [
            ("policy", "policy"),
            ("./policy/", "policy"),
            ("", "docs"),
            ("/etc", "docs"),
            ("../elsewhere", "docs"),
        ],
    )
    def test_the_policy_root_row_reads_as_docs_unless_it_names_a_directory_inside(
        self, tmp_path, value, root
    ):
        """`hooks/config.py#policy_root`, the one reader every reader asks: an
        empty value and one that leaves the repository read as `docs`."""
        from conftest import load_hook_module

        config = load_hook_module("config.py", "specseal_config_for_policy_root")
        (tmp_path / "config.md").write_text(
            f"| Item | Value |\n|---|---|\n| Policy root | {value} |\n",
            encoding="utf-8",
        )
        assert config.policy_root(str(tmp_path)) == root
        assert config.policy_root("") == "docs"

    def test_the_baseline_is_the_first_code_span_of_its_one_row(self):
        """The `Baseline commit` reader in `hooks/config.py`: the SHA in the
        first code span of the one row, else no SHA and why, naming a
        placeholder, a second row, no row and no table."""
        config = chain.parity_readers()[0]
        row = (
            "| Baseline commit | `<SHA>`, the commit the original's coordinates "
            "refer to |"
        )
        text = parity_file(BASELINE)
        assert config.baseline_commit(text) == (BASELINE, None)
        assert config.baseline_commit(parity_file(BASELINE[:7])) == (
            BASELINE[:7],
            None,
        )
        for bad, why in (
            (parity_file(None), "`<SHA>`"),
            (parity_file(BASELINE.upper()), BASELINE.upper()),
            (
                text.replace(row.replace("<SHA>", BASELINE) + "\n", ""),
                "no `Baseline commit` row",
            ),
            (
                text.replace(
                    "| Policy root |",
                    row.replace("<SHA>", BASELINE) + "\n| Policy root |",
                ),
                "2 `Baseline commit` rows",
            ),
            ("# Migration config\n", "holds no `| Field | Value |` table"),
        ):
            sha, said = config.baseline_commit(bad)
            assert sha is None and why in said, (said, bad)
        _sha, said = config.baseline_commit("# Migration config\n")
        assert "Baseline commit" not in said, said


test_census = census_case(TARGET)
