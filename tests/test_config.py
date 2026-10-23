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
walker held to cmark-gfm, and the reader's cases of
`tests/test_the_mode_question_is_asked_once.py`, which keeps the writer's.
Each case keeps its body; a name its old file defined for it is defined
here, and a fixture or text two files read is `tests/conftest.py`'s.
"""

import importlib.util
import os
import subprocess

import config_shapes
import pytest
from block_shapes import SHAPES
from conftest import (
    BASELINE,
    FENCED_ABOVE,
    FENCED_BELOW_A_TABLE_THAT_NEVER_BEGAN,
    FENCED_REFUSAL,
    PIPED_TABLE,
    ROOT,
    TABLE,
    UNDER_THE_COMMENT,
    census_case,
    crlf,
    load_hook_module,
    load_module,
    local_home,
    opt_in_shared,
    parity_file,
    shape_text,
    write_config,
    write_unreadable,
)
from conftest import config_table as table

TARGET = "hooks/config.py"

config = load_hook_module("config.py", "config_under_test")

# The mode gate, whose `undeclared` one reader case asks beside the reader.
GATE = "mode-gate.py"

# `tests/block_shapes.py`'s config shapes the comment cases read (#667).
COMMENTED_OLD_ROW = shape_text("C5")
COMMENTED_OLD_TABLE = shape_text("C6")
QUOTED_DELIMITERS = shape_text("C1")
LIVE = [("Mode", "shared"), ("Broad gate", "bin/test -q")]

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

    def test_an_escaped_pipe_is_one_row_and_the_rows_below_it_still_arrive(
        self, config
    ):
        """A1. `seal/config.md` is markdown and `\\|` is markdown's own answer for
        a pipe inside a cell (`questions.md` Q1, answered by the repository owner
        on 2026-09-17).

        **The count is asserted before the value, and that ordering is the
        case.** A case that checks the `Broad gate` value alone passes just as
        well when every row under it has vanished, and vanishing was the defect
        #415 was opened about: before the escape, the piped row took `Mode` and
        every later row with it, each falling back to a default with no message
        anywhere. Written bare it is now refused, naming the line (#871).
        """
        rows = config.config_rows(PIPED_TABLE)
        assert len(rows) == 4, (
            f"the table has four rows and {len(rows)} came back: {rows}. A row "
            "the reader refuses ends the table, so what is missing here is every "
            "row written BELOW the piped one"
        )
        assert [item for item, _ in rows] == [
            "Record language",
            "Broad gate",
            "Mode",
            "Commit and pull request language",
        ], rows
        assert dict(rows)["Broad gate"] == "bin/test -q | tee out.txt", (
            "the value reaches its caller with one literal pipe, because the "
            "escape is markdown's and is undone before anything else sees it"
        )
        assert dict(rows)["Mode"] == "shared", (
            "the `Mode` row sits below the piped one, which is what `seal mode` "
            "reads before deciding whether to write one"
        )

    def test_a_windows_path_survives_the_reader_exactly_as_written(self, config):
        """The constraint the repository owner attached to Q1's answer, and it
        decides the implementation rather than the choice: the reduction is
        **exactly the two characters `\\|`**, never a general backslash unescape.

        `C:\\Python\\python.exe -m pytest` is the shape a `Broad gate` row takes
        on Windows, and it reads back with its separators intact today — the
        state this repository has already synced across operating systems. A
        blanket `re.sub(r"\\\\(.)", r"\\1", value)` would hand the gate
        `C:Pythonpython.exe -m pytest`, which is a path to nothing.
        """
        text = (
            "| Item | Value |\n|---|---|\n"
            "| Broad gate | C:\\Users\\x\\Python\\python.exe -m pytest |\n"
        )
        assert config.config_rows(text) == [
            ("Broad gate", "C:\\Users\\x\\Python\\python.exe -m pytest")
        ], "a backslash that is not part of `\\|` is the value's own character"

    def test_a_backslash_against_a_pipe_is_the_one_shape_the_escape_narrows(
        self, config
    ):
        """Round 1's 🟡 2 of #415. The escape is not free in one direction only:
        a backslash immediately before a cell-ending pipe used to be a plain
        character followed by a delimiter, and it is now one escaped pipe — so
        the line has one pipe fewer than it needs and stops being a row.

        **It is kept rather than repaired, and the narrowing is named rather
        than discovered.** Once `\\|` means an escaped pipe those bytes cannot
        also mean *backslash, then the delimiter*; the old reading was only
        available while a backslash meant nothing. Nothing becomes unwritable —
        a space before the closing pipe gives the value back byte for byte,
        because `config_rows` strips the cell — and one line in the whole tree
        reads differently, in a review report quoting this shape.

        Both members of the class are here. The report named the first; the
        second is the same cause at an INTERNAL pipe, where the line stops being
        a row for the same reason.
        """
        header = "| Item | Value |\n|---|---|\n"
        tight_last = "| Broad gate | C:\\Users\\x\\tools\\|\n"
        tight_first = "| C:\\tools\\| x |\n"
        assert config.config_rows(header + tight_last) == [], (
            "a backslash against the closing pipe is markdown's escaped pipe, so "
            "the line has no closing pipe left and is not a row. If this returns "
            "a row the pattern changed and `spec.md` *What this repair cannot "
            "see* is now wrong"
        )
        assert config.config_rows(header + tight_first) == [], (
            "the same cause at the pipe BETWEEN the cells — the report named only "
            "the closing one"
        )
        assert config.config_rows(
            header + "| Broad gate | C:\\Users\\x\\tools\\ |\n"
        ) == [("Broad gate", "C:\\Users\\x\\tools\\")], (
            "written with a space before the closing pipe the value comes back "
            "exactly as the old pattern read it, so no value lost a spelling"
        )
        assert config.config_rows(header + "| C:\\tools\\ | x |\n") == [
            ("C:\\tools\\", "x")
        ], "and the same for the item cell"

    def test_a_three_column_row_is_refused_and_the_rows_above_it_arrive(self, config):
        """Shape 6 of #871. The escape widens what a cell may hold and must not
        widen what a ROW is: a greedy last cell would read `| a | b | c |` as the
        row `('a', 'b | c')`. Until #871 the line ended the table silently, and
        every row below it fell to its default; cmark-gfm shows those rows, so
        the walker refuses the line instead, naming it, and the rows above it
        are values. Seen red against the stop rule: `('c', ...)` was `(None,
        None)`, an absent row."""
        text = "| Item | Value |\n|---|---|\n| a | b |\n| x | y | z |\n| c | d |\n"
        assert config.config_rows(text) == [("a", "b")]
        value, said = config.config_value(text, "c")
        assert value is None and said is not None, (value, said)
        assert "stops at `| x | y | z |`, which is not a 2-cell row" in said, said
        assert config.config_value(text, "a") == ("b", None)

    def test_a_fenced_table_above_the_live_one_is_not_the_table(self, config, tmp_path):
        """A1. The live table is the first one outside every fence.

        `config_rows` starts at the first `| Item | Value |` header and never
        looks for another, so an example pasted above the live table WAS the
        table every gate got: the mode, the broad command, every row. The shape
        is invited rather than contrived — `config.md`'s own header comment
        points at `templates/config.md`, and `skills/config/SKILL.md` step 3
        tells a session to copy a block of that template, fenced example row
        included, naming no position for it.
        """
        assert config.config_rows(FENCED_ABOVE) == [
            ("Mode", "shared"),
            ("Broad gate", "bin/test -q"),
        ], config.config_rows(FENCED_ABOVE)
        assert "EXAMPLE" not in [
            value for _item, value in config.config_rows(FENCED_ABOVE)
        ]
        home = tmp_path / "seal"
        home.mkdir()
        write_config(home, FENCED_ABOVE)
        assert config.declared_mode(str(home)) == ("mode", "shared"), (
            "the mode the gate reads is the example's, not the repository's"
        )

    def test_a_fenced_example_below_a_table_that_never_began_is_still_not_the_table(
        self,
        config,
    ):
        """A2. Both walks step past a line they cannot parse until a row is
        found, so with nothing parsed above it a fenced example's rows became the
        live rows — the same defect one shape over, and the one a repair aimed at
        the fenced HEADER alone would have left standing."""
        rows = config.config_rows(FENCED_BELOW_A_TABLE_THAT_NEVER_BEGAN)
        assert rows == [], (
            f"the example inside the fence supplied this repository's rows:\n{rows}"
        )

    def test_what_counts_as_a_fence_is_commonmarks_rule_as_far_as_it_goes(self, config):
        """Q3 of `questions.md`, decided and pinned. `spec.md` *Data &
        interfaces* fixes the rule for the shapes that matter; the residue is
        CommonMark's own edge cases, resolved toward *not a fence* wherever the
        specification leaves room, because that is the direction that keeps a
        live table readable.

        Each assertion below is one decision:

          - four spaces of indentation is an indented code block, never a fence,
            so the table under it is still read;
          - a BACKTICK fence's info string may not hold a backtick (CommonMark
            4.5), so that line opens nothing;
          - a closing run may be longer than the one that opened the block;
          - a run of the OTHER character does not close a block, and neither
            does a run carrying an info string;
          - an unclosed fence runs to the end of the file, which lands on
            *nothing is declared* — the direction `hooks/config.py` already
            fails in.

        **A blank line stands above the live header in each fixture since
        #871**, because the walker refuses a header with a non-blank line
        directly above it whatever that line is (the migration's shape, rows 1,
        2 and 11 of the work item's measurement), and the decisions here are
        about which line opens or closes a fence, not about that one. The first
        assertion is that refusal, so the reason for the blank line is pinned
        beside it.
        """
        live = "| Item | Value |\n|---|---|\n| Mode | shared |\n"
        value, said = config.config_value("    ```\n" + live, "Mode")
        assert value is None and "leave a blank line above the header" in said, said
        assert config.config_rows("    ```\n\n" + live) == [("Mode", "shared")], (
            "four spaces is an indented code block and not a fence"
        )
        assert config.config_rows("```` `x` ````\n\n" + live) == [("Mode", "shared")], (
            "a backtick fence's info string may not hold a backtick, so this "
            "line opens no fence"
        )
        assert config.config_rows(
            "```\n| Item | Value |\n|---|---|\n| Mode | local |\n``````\n\n" + live
        ) == [("Mode", "shared")], (
            "a closing run longer than the opening one closes the block"
        )
        assert config.config_rows(
            "```\n~~~\n| Item | Value |\n|---|---|\n| Mode | local |\n```\n\n" + live
        ) == [("Mode", "shared")], "a tilde run does not close a backtick fence"
        assert config.config_rows(
            "````\n```\n| Item | Value |\n|---|---|\n| Mode | local |\n````\n\n" + live
        ) == [("Mode", "shared")], (
            "a run SHORTER than the opening one does not close the block — this "
            "repository's own records wrap a fenced example in four backticks, "
            "and a rule that knew three only would read the inner fence as the "
            "outer one's close and leave the live table inside a fence"
        )
        assert config.config_rows("```\n```markdown\n" + live) == [], (
            "a run carrying an info string does not close a block, so this file "
            "declares nothing"
        )
        assert config.config_rows("~~~\n" + live) == [], (
            "an unclosed fence runs to the end of the file"
        )
        assert config.config_rows("~~~info ~ string\n" + live + "~~~~\n") == [], (
            "a tilde fence's info string is unrestricted, which is CommonMark's "
            "rule and not an exception to this one"
        )

    def test_delimiters_quoted_in_code_spans_hide_nothing(self, config):
        """C1, named as 1790635413 named it (round 1, 🟡 3). A prose line quoting
        the opener in a code span above the table and one quoting the closer
        below it are paragraph text, so the table between them is read. Pins:
        the base read it, and the three rounds lost it by reading inline state."""
        assert config.config_rows(QUOTED_DELIMITERS) == LIVE

    @pytest.mark.parametrize("name", ["LS", "PS", "NEL", "FF", "VT", "FS", "GS", "RS"])
    def test_a_break_commonmark_does_not_honour_hides_no_config_row(self, config, name):
        """#667 round 1, 🟡 1: the routing reader's shape in `config.md`. A
        `<!--` after a character `str.splitlines` breaks at and CommonMark does
        not is mid-line to a renderer, so it hides no line, and the base read
        `Mode shared`.

        **Re-pinned by #871 to the walker's answer, which is a refusal.** The
        `-->` under the row is a row GFM shows, so the table is one the walk
        cannot read whole, and the walk reads the pieces `str.splitlines` cuts,
        where `<!--` begins one: it refuses at the header, naming an HTML block
        GFM does not see. The direction is the refusing one and no row is read
        that GFM does not show; the sentence's cause is the walker's limit on
        these eight characters, named in the work item's `overview.md`."""
        from block_shapes import BREAKS, OPEN

        text = (
            f"A note{BREAKS[name]}{OPEN}\n\n| Item | Value |\n|---|---|\n"
            "| Mode | shared |\n-->\n"
        )
        lines = text.splitlines()
        assert [i for i, _line in config.unfenced(lines, text)] == list(
            range(len(lines))
        )
        assert config.config_rows(text) == []
        value, said = config.config_value(text, "Mode")
        assert value is None and said is not None, said

    @pytest.mark.parametrize("name", ["LS", "PS", "NEL", "FF", "VT", "FS", "GS", "RS"])
    def test_a_piece_inside_an_inline_comment_is_no_config_row(self, config, name):
        """#667 round 2, 🟡 1. A table written after a break inside an inline
        comment its line opened is inside that comment to a renderer, and the
        fence run before it is fenced to the base. Read by the line it starts in,
        the piece took the line's answer, shown, and a `Mode` row neither
        reading shows was read."""
        from block_shapes import BREAKS, OPEN

        brk = BREAKS[name]
        text = (
            f"x {OPEN} a{brk}```{brk}| Item | Value |{brk}|---|---|{brk}"
            "| Mode | shared |\n-->\n"
        )
        assert config.config_rows(text) == []

    @pytest.mark.parametrize("name", ["LS", "PS", "NEL", "FF", "VT", "FS", "GS", "RS"])
    @pytest.mark.parametrize(
        "opener, closer",
        [
            ("<![CDATA[ a", "]]>"),
            ("<? a", "?>"),
            ("<!DOCTYPE a", "a>"),
            ('<span title="a', '">'),
            ("<span title='a", "'>"),
        ],
        ids=["cdata", "instruction", "declaration", "double-quoted", "single-quoted"],
    )
    def test_a_piece_inside_other_inline_html_is_no_config_row(
        self, config, name, opener, closer
    ):
        """#673, #667 round 3's 🟡 1. A comment is one kind of inline raw HTML of
        six (CommonMark 6.6); CDATA, a processing instruction, a declaration and a
        tag's quoted attribute value hide what they hold too, and the fence run
        before the table is fenced to the base. The walk looked only for a
        comment opener, so the piece was claimed shown and a `Mode` row neither
        reading shows was read. A declaration's closer is written `a>`: a `>` at
        a line's start would open a block quote instead."""
        from block_shapes import BREAKS

        brk = BREAKS[name]
        text = (
            f"x {opener}{brk}```{brk}| Item | Value |{brk}|---|---|{brk}"
            f"| Mode | shared |\n{closer}\n"
        )
        assert config.config_rows(text) == []

    @pytest.mark.parametrize("name", ["LS", "PS", "NEL", "FF", "VT", "FS", "GS", "RS"])
    def test_a_row_after_a_break_gfm_does_not_honour_is_no_row_of_its_own(
        self, config, name
    ):
        """#871 round 1, 🟡 4. A row followed on its own line by a character only
        `str.splitlines` ends a line at, then a second row, is ONE row to
        cmark-gfm, cut off at its cells: GitHub shows `Mode shared` and no
        `Broad gate`. The walk reads the first row and refuses the piece after
        the break, so no gate is handed a command GitHub does not show. Seen red
        against the walk before the guard: `Broad gate` was read as `x`."""
        from block_shapes import BREAKS

        text = TABLE.format(rows=f"| Mode | shared |{BREAKS[name]}| Broad gate | x |\n")
        assert config.config_rows(text) == [("Mode", "shared")], config.config_rows(
            text
        )
        value, said = config.config_value(text, "Broad gate")
        assert value is None and "put it on a line of its own" in (said or ""), said

    @pytest.mark.parametrize("name", ["LS", "PS", "NEL", "FF", "VT", "FS", "GS", "RS"])
    @pytest.mark.parametrize("where", ["above the header", "under the header"])
    def test_a_header_after_a_break_gfm_does_not_honour_is_no_table(
        self, config, name, where
    ):
        """#871 round 2, yellow 7. A header after a character only
        `str.splitlines` ends a line at, or a delimiter row after one on the
        header's line, is no table to cmark-gfm (measured for FF, U+2028, NEL
        and VT by the round's reviewer). The walk reads no row and refuses. Seen
        red against 4dfb3d0d: `Mode` was read as `shared`."""
        from block_shapes import BREAKS

        brk = BREAKS[name]
        text = (
            f"# c\n\n{brk}| Item | Value |\n|---|---|\n| Mode | shared |\n"
            if where == "above the header"
            else f"# c\n\n| Item | Value |{brk}|---|---|\n| Mode | shared |\n"
        )
        assert config.config_rows(text) == [], config.config_rows(text)
        value, said = config.config_value(text, "Mode")
        assert value is None and "each on a line of its own" in (said or ""), said


class Test_config_value:
    def test_accepts_one_row_as_its_value_and_no_row_as_none(self, config):
        """The two answers beside the refusal, so a reader of `config_value` can
        tell an empty row from no row: `""` is a row somebody left empty, and
        None is no row at all."""
        text = TABLE.format(rows="| Mode | shared |\n| Broad gate |  |\n")
        assert config.config_value(text, "Mode") == ("shared", None)
        assert config.config_value(text, "Broad gate") == ("", None)
        assert config.config_value(text, "Ledger frozen from") == (None, None)
        assert config.config_value(None, "Mode") == (None, None)

    def test_a_fenced_example_of_a_row_does_not_double_the_live_one(self, config):
        """The count is over the rows `config_rows` takes, so the example a
        person pastes from `templates/config.md` into a fence above the table
        (#429) is not a second row."""
        text = (
            "```markdown\n| Item | Value |\n|---|---|\n| Mode | local |\n```\n\n"
            + TABLE.format(rows="| Mode | shared |\n")
        )
        assert config.config_value(text, "Mode") == ("shared", None)

    def test_a_line_that_will_not_parse_is_named_and_the_hook_still_says_nothing(
        self, config, repo
    ):
        """A4 and A7 of #415, which are one case because they are one decision,
        re-pinned by #871.

        The reader names the line in its refusal, and the hook says nothing. The
        caller that prints the sentence is a command, which already talks to a
        person; `hooks/mode-gate.py` deliberately does not, because it is a
        `PreToolUse` hook and a wrong refusal there stops a session with nobody
        able to get past it. Until #871 a `Mode` row below an unparseable line
        read as undeclared and the gate asked the mode question again; now the
        item is a refusal, which the gate reads as an answer it cannot act on,
        so it asks nothing -- the prompt budget of a refused table is zero.
        """
        text = (
            "| Item | Value |\n|---|---|\n"
            "| Record language | English |\n"
            "| Broad gate | bin/test -q | tee out.txt |\n"
            "| Mode | shared |\n"
        )
        value, said = config.config_value(text, "Mode")
        assert value is None and "`| Broad gate | bin/test -q | tee out.txt |`" in said
        assert config.config_table(TABLE.format(rows="| Mode | shared |\n"))[1] == []
        assert config.config_table("# no table here\n\nprose.\n") == ([], [])
        assert (
            config.config_table("| Item | Value |\n|---|---|\n| a | b |\n\nprose.\n")[1]
            == []
        ), "a blank line is the table ending, not a row somebody wrote"

        gate = load_hook_module(GATE, "specseal_mode_gate_for_415")
        home = opt_in_shared(repo)
        write_config(home, text)
        answer = gate.undeclared(str(repo))
        assert answer == "", (
            'the hook\'s answer is the home or `""` and never a message; a `Mode` '
            f"row below a refused line is a refusal, which is silence: {answer!r}"
        )

    def test_a_refusal_is_per_item_and_never_an_absent_row(self, config, repo):
        """S2, one arm per assertion, over shapes 1, 5, 7 and 13. A row the walk
        read before it stopped is a value; an item it did not read is the
        walker's sentence; a doubled row is #867's sentence; and `(None, None)`
        is only an unrefused table with no such row, or no table at all. Seen
        red against the stop rule: shape 7's `Mode` read `shared`, a row GitHub
        shows truncated, and shape 13's read `shared` past a line GitHub shows
        as a row of its own."""
        shapes, stops = config_shapes.SHAPES, config_shapes.STOPS
        assert config.config_value(shapes[5], "Mode") == ("shared", None)
        assert config.config_value(shapes[7], "Record language") == ("English", None)
        for number, item in ((1, "Mode"), (5, "Broad gate"), (7, "Mode"), (13, "Mode")):
            value, said = config.config_value(shapes[number], item)
            assert value is None and said is not None, (number, item, value)
            assert stops[number] in said, (number, said)
        doubled = TABLE.format(rows="| Mode | shared |\n| Mode | local |\n")
        assert config.config_value(doubled, "Mode") == (
            None,
            "`Mode` appears 2 times — one value",
        )
        unrefused = TABLE.format(rows="| Mode | shared |\n")
        assert config.config_value(unrefused, "Broad gate") == (None, None)
        assert config.config_value("a file of prose\n", "Mode") == (None, None)
        home = opt_in_shared(repo)
        write_config(home, shapes[7])
        kind, said = config.declared_mode(str(home))
        assert kind == "refused" and stops[7] in said, (kind, said)

    def test_refuses_an_item_written_again_below_the_stopping_line(self, config):
        """#871 round 1, the reviewer's second question, answered by #867's rule:
        an item written twice has no value. A `Mode` row the walk read above a
        line it refused, and a `Mode` row written below that line, are two
        answers, so neither is the value. Seen red against the walk before the
        count reached below the stopping line: `('shared', None)`."""
        text = TABLE.format(rows="| Mode | shared |\n| a | b | c |\n| Mode | local |\n")
        assert config.config_value(text, "Mode") == (
            None,
            "`Mode` appears 2 times — one value",
        )
        assert config.config_value(text, "a")[1] is not None

    def test_an_item_named_under_the_next_heading_is_another_tables(self, config):
        """#871 round 2, yellow 10. A table under the next heading is not below
        the line the walk stopped at, so a `Mode` cell in it does not double the
        config's `Mode` row. Seen red against 4dfb3d0d: "appears 2 times"."""
        text = TABLE.format(
            rows="| Mode | shared |\n| a | b | c |\n\n## Notes\n\n"
            "| Mode | what it means |\n|---|---|\n| local | x |\n"
        )
        assert config.config_value(text, "Mode") == ("shared", None)

    @pytest.mark.parametrize("name", ["LS", "FF"])
    def test_a_line_below_the_stop_is_a_line_where_gfm_begins_one(self, config, name):
        """#871 round 2, yellow 7's class in yellow 10's count. A `| Mode | … |`
        piece after a character only `str.splitlines` ends a line at is more of
        the line above to GFM, so it names nothing and doubles nothing; and a
        heading piece after one is no heading, so the count goes on past it.
        Seen red against 4dfb3d0d on the first: "appears 2 times"."""
        from block_shapes import BREAKS

        brk = BREAKS[name]
        cut = TABLE.format(
            rows=f"| Mode | shared |\n| a | b | c |\nx{brk}| Mode | local |\n"
        )
        assert config.config_value(cut, "Mode") == ("shared", None)
        past = TABLE.format(
            rows=f"| Mode | shared |\n| a | b | c |\nx{brk}## y\n| Mode | local |\n"
        )
        assert config.config_value(past, "Mode") == (
            None,
            "`Mode` appears 2 times — one value",
        )


class Test_declared_mode:
    def test_accepts_the_row_from_the_root_the_folder_is_at(self, config, repo):
        """The reader answers for whichever root exists, so a local-mode
        repository is not read as one that declared nothing."""
        home = local_home(repo)
        write_config(home, TABLE.format(rows="| Mode | local |\n"))
        assert config.declared_mode(str(home)) == ("mode", "local")

    @pytest.mark.parametrize(
        "text, expected",
        [
            (None, ("none", "")),
            (TABLE.format(rows="| Record language | Korean |\n"), ("none", "")),
            (TABLE.format(rows="| Mode |  |\n"), ("none", "")),
            ("not a table at all\n", ("none", "")),
            (TABLE.format(rows="| Mode | SHARED |\n"), ("mode", "shared")),
            (TABLE.format(rows="| Mode | whatever |\n"), ("unknown", "whatever")),
        ],
    )
    def test_the_four_spellings_of_undeclared_are_one_answer(
        self, config, repo, text, expected
    ):
        """The same four `seal.py#declared` already had, because it is the same
        reader — moved, not rewritten. A row that names no mode is told apart from
        no row, because a claim nobody can act on is not the same as no claim."""
        home = opt_in_shared(repo)
        if text is not None:
            write_config(home, text)
        assert config.declared_mode(str(home)) == expected

    @pytest.mark.parametrize(
        "rows",
        [
            "| Mode | shared |\n| Mode | local |\n",
            "| Mode | local |\n| Mode | local |\n",
            "| Mode | shared |\n| Record language | Korean |\n| Mode |  |\n",
        ],
        ids=["two values", "the same value twice", "one value and an empty row"],
    )
    def test_refuses_a_mode_row_written_twice(self, config, repo, rows):
        """S1 of #867, the reader's half. The reader took the first row and the
        checker took the last, so a person editing the row they could see might be
        editing the one that does not answer. A row written twice has no value
        -- not its first and not its last -- and the refusal names the item and
        how many times it is written. Seen red against the first-wins reader:
        `('mode', 'shared')` for the first shape."""
        home = opt_in_shared(repo)
        write_config(home, TABLE.format(rows=rows))
        kind, said = config.declared_mode(str(home))
        assert kind == "refused", (kind, said)
        assert said == "`Mode` appears 2 times — one value"

    def test_an_absent_config_and_an_unreadable_one_are_two_states(self, config, repo):
        """S3 of #867, the reader's half. No file declares nothing; a file that is
        there and will not read is refused with a sentence naming the path. The
        reader tells the two apart once, so no caller opens the file again to
        find out -- `hooks/mode-gate.py#unreadable` did, and is gone."""
        home = opt_in_shared(repo)
        assert config.config_text(str(home)) == (None, None)
        assert config.declared_value(str(home), "Mode") == (None, None)
        for shape in ("directory", "undecodable"):
            path = write_unreadable(home, shape)
            text, said = config.config_text(str(home))
            assert text is None and said.startswith(path + " is there and cannot"), said
            assert config.declared_value(str(home), "Mode") == (None, said)
            assert config.declared_mode(str(home)) == ("refused", said)
            if shape == "directory":
                os.rmdir(path)
            else:
                os.remove(path)

    def test_rows_above_the_header_are_not_rows_of_this_table(self, config, repo):
        """A mutation survived here, and the branch it broke is the one the
        docstring's whole claim rests on: the header is this table's furniture
        ABOVE its first row. Without it a `| Mode | local |` written into some
        other table earlier in the file — an example, a comparison — is read as
        the declaration.

        Uncovered because it arrived uncovered. The parser moved here from
        `seal.py`, and the suite that looks like its home,
        `tests/test_the_pull_request_language_is_the_repositorys.py`, carries a
        second copy of the loop rather than calling this one."""
        home = opt_in_shared(repo)
        write_config(
            home,
            "# Repository config\n\n"
            "An example of what NOT to write:\n\n"
            "| Mode | local |\n\n"
            "| Item | Value |\n|---|---|\n| Mode | shared |\n",
        )
        assert config.declared_mode(str(home)) == ("mode", "shared")


class Test_config_table:
    def test_refuses_a_fenced_pipe_line_as_a_line_somebody_wrote(self, config):
        """A3. The walk that read ON past the stopping line treated any line
        beginning with a pipe as a line somebody wrote as a row — so a line
        inside an example block came back as refused, and `broad-gate` quotes a
        refused line back at the person as their own.

        Re-pinned by #871: the fence directly under the delimiter row ends the
        table, as GFM ends it, so the live `Mode` row below the fence is not one
        of the table's rows and the walk refuses it -- naming THAT line, never
        the fenced one.
        """
        rows, refusals = config.config_table(FENCED_REFUSAL)
        assert rows == [], rows
        assert len(refusals) == 1, refusals
        assert "tee out.txt" not in refusals[0], (
            f"a line inside a code fence came back as a refused row:\n{refusals}"
        )
        assert "ends above `| Mode | shared |`" in refusals[0], refusals

    @pytest.mark.parametrize(
        "name, rows, stops",
        [
            # pins: delimiters quoted in code spans either side of the table hide
            # nothing (1790635413 round 1, 🟡 3)
            ("C1", LIVE, None),
            # red at base: a closed comment above the table quoting a fence line
            # opened a fence that ran to the end and hid the live table
            ("C2", [("Mode", "shared")], None),
            # pins: a mid-line opener nobody closed switches off no fence below it
            # (1790635413 round 3, 🟡 1)
            ("C3", [("Mode", "shared"), ("Broad gate", "bin/test")], None),
            # pins: nor does one that an example's closer below seems to close
            # (1790635413 round 3, ⬜ 3)
            ("C4", LIVE, None),
            # #871: a row parked in a comment inside the table ends the table
            # there, as GFM ends it, so the live rows under the comment are
            # refused rather than read; the same in CRLF. A whole old table
            # parked above the live one still leaves the live one read.
            ("C5", [], UNDER_THE_COMMENT),
            ("C6", LIVE, None),
            ("C7", [], UNDER_THE_COMMENT),
            # red at base: a malformed pipe-line inside a comment is not the
            # person's refused row -- the walk names the live row under it
            ("C8", [], UNDER_THE_COMMENT),
            # #871: a `<!--` nobody closed still hides nothing from the fence
            # rule, but GFM renders no table under or after it, so the walk
            # refuses where the stop rule read
            ("C9a", [], "inside an HTML block opened above it and never closed"),
            ("C9b", [], UNDER_THE_COMMENT),
            # pins: #429's fenced example above the live table
            ("C12", [("Mode", "shared")], None),
            # pins: a fence nobody closed still hides everything below it, so the
            # file holds no table and declares nothing
            ("C14", [], None),
        ],
        ids=lambda value: value if isinstance(value, str) and value[:1] == "C" else "",
    )
    def test_accepts_every_config_shape_as_the_frame_expects(
        self, config, name, rows, stops
    ):
        """S5 of #667, re-pinned to the walker by #871. Every config shape the
        frame names, through `config_table`. A row inside a comment that closes
        is not an answer somebody gave, which is the direction this module fails
        in, and a fenced line is no row either. Where GFM ends the table at a
        comment or shows no table at all, the walk refuses, naming the live row
        it did not read -- never the parked one -- rather than reading on below
        it as the stop rule did; a refused item is a refusal, never absent."""
        text = shape_text(name)
        found, refusals = config.config_table(text)
        assert config.config_rows(text) == rows, config.config_rows(text)
        if stops is None:
            assert refusals == [], refusals
        else:
            assert len(refusals) == 1 and stops in refusals[0], refusals
            assert "old -q" not in refusals[0], refusals
        assert [(item, value) for _i, item, value in found] == rows

    @pytest.mark.parametrize("number", sorted(config_shapes.SHAPES))
    def test_every_config_reader_is_one_walk_over_the_sixteen_shapes(
        self, config, number
    ):
        """S1. `config_rows` is read first, because it is the name every caller
        spells and the one the stop rule answered: seen red against the stop
        rule on ten of the sixteen shapes (1-5, 9, 11-13, 16). On 6, 7, 8 and 14
        the stop rule returned the same rows above the line and dropped every
        row below it in silence, which is what the refusal assertion holds; 10
        and 15 the two readers read alike. Then the walk itself: `config_table`
        is `gfm_table` over the config header, every index names the line the
        row is written on, and the refusal names where the walk stopped."""
        text = config_shapes.SHAPES[number]
        assert config.config_rows(text) == config_shapes.READ[number]
        rows, refusals = config.config_table(text)
        walked, said = config.gfm_table(text, config.CONFIG_TABLE)
        assert rows == [(line - 1, item, value) for line, (item, value) in walked]
        assert refusals == said
        lines = text.splitlines()
        assert all(
            config.table_cells(lines[index]) == (item, value)
            for index, item, value in rows
        ), rows
        stops = config_shapes.STOPS[number]
        if stops is None:
            assert refusals == [], refusals
        else:
            assert len(refusals) == 1 and stops in refusals[0], refusals


class Test_fence_map:
    def test_refuses_to_name_a_fence_inside_a_closed_comment(self, config, tmp_path):
        """S8, C2. The comment closes, so the fence line inside it opens nothing,
        and neither `broad-gate`'s `fence_left_open` nor `seal.py`'s write guard,
        which both ask `fence_map`'s second value, names a fence nobody left
        open. Red at base: the fence ran to the end and was named."""
        lines = SHAPES["C2"]
        assert config.fence_map(lines)[1] is None
        home = tmp_path / "seal"
        home.mkdir()
        write_config(home, shape_text("C2"))
        path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "skills",
            "verify",
            "scripts",
            "broad_gate.py",
        )
        spec = importlib.util.spec_from_file_location("specseal_gate_for_667", path)
        gate = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(gate)
        assert gate.fence_left_open(str(home)) is False

    def test_accepts_a_fence_nobody_closed_as_the_one_named(self, config):
        """C14, pinned from the other side: the fence that hides the live table
        is the one `fence_map` reports, so `broad-gate` still says *close that
        fence*."""
        assert config.fence_map(SHAPES["C14"])[1] == 0

    def test_the_fence_named_is_the_one_that_hides_the_row(self, config):
        """C2 with a fence left open below the table. The old reading runs the
        fence quoted in the comment to the end, so it would name THAT line, which
        opens nothing; the walk sees the tilde fence below the table never close,
        and the line under it is hidden because of it. That is the fence
        `broad-gate` has to tell the person to close."""
        lines = [*SHAPES["C2"], "", "~~~", "| Broad gate | bin/test -q |"]
        assert config.fence_map(lines)[1] == lines.index("~~~")
        assert config.config_rows("\n".join(lines)) == [("Mode", "shared")]


class Test_unfenced:
    def test_refuses_a_commented_row_in_either_line_ending(self, config):
        """S5, C5 to C7, named as 1790635413 named them. The rows parked in a
        comment are gone from every walk. Since #871 the live rows under a
        comment that sits inside the table do not arrive either: GFM ends the
        table at the comment, so the walk refuses them, naming the first, and an
        item among them is a refusal and never an absent row. Under a whole old
        table parked above the live one, the live table arrives."""
        for text in (COMMENTED_OLD_ROW, COMMENTED_OLD_TABLE, crlf(COMMENTED_OLD_ROW)):
            assert all(
                "old -q" not in line
                for _index, line in config.unfenced(text.splitlines())
            ), text
        assert config.config_rows(COMMENTED_OLD_TABLE) == LIVE
        for text in (COMMENTED_OLD_ROW, crlf(COMMENTED_OLD_ROW)):
            assert config.config_rows(text) == [], text
            value, said = config.config_value(text, "Broad gate")
            assert value is None and UNDER_THE_COMMENT in said, said

    def test_accepts_every_line_under_a_mid_line_comment(self, config):
        """C13, the residual `spec.md` *Scope* names. A renderer hides the first
        pipe-line behind a lone backtick and a mid-line `<!--`, and knowing that
        needs code spans and the paragraph's extent, which is where all three of
        1790635413's rounds lost ground. The base reads it, so reading it is not
        worse; this pins that nothing here pretends to more."""
        lines = SHAPES["C13"]
        assert [index for index, _line in config.unfenced(lines)] == list(
            range(len(lines))
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
