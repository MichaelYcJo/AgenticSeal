"""`lib/config.py`, the shared reader of `seal/config.json` and the walker
of the records' tables, one class per function its cases reach.

#1454 moved the settings out of a markdown table, so the cases that pinned
the walker's refusals of the `| Item | Value |` table as a settings reader
left with that reader; the walker's own cases over that table stay, read as
an earlier release's `config.md` that `seal mode` converts. The cases of the
pact's `| Signer |` table and of the header 0.18.x wrote left with their
reader too, and the pact's signers are read from a `Pact signers` key.

#942's phase 6 placed here the reference-root reader's cases from
`tests/behaviour/test_a_reference_root_is_read_and_never_taken.py`, the policy root's
from `tests/text/test_a_document_has_room_for_the_next_fold.py`, the remote
normaliser's from `tests/text/test_the_records_can_be_carried_out_and_in.py`, the
`Baseline commit` reader's from `tests/skills/test_chain_check.py`, the row reader's
from `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` and three
of the table walker's from
`tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py`, which keeps the
walker held to cmark-gfm, the reader's cases of
`tests/test_the_mode_question_is_asked_once.py`, whose writer's cases are in
`tests/skills/test_seal.py`, the pact readers' of `tests/behaviour/test_a_signer_declares_its_pact.py`, and the
cases `tests/skills/test_pact_check.py` left for this module that run `seal
pact` over the pact's world in `tests/conftest.py`; one of them stands, and
the rest left with the `| Signer |` table's reader. Each case keeps
its body; a name its old file defined for it is defined here, and a fixture
or text two files read is `tests/conftest.py`'s.

#942's round 9 fix pass placed two more, each a case of this module alone:
the table walker's refusal of a line shown directly above the header, from
the oracle file, whose corpus it imports from there, and the case that copies
this module without `lib/blocks.py`, from
`tests/test_a_script_copied_alone_exits_2.py`, whose `routing.py` row is in
`tests/lib/test_routing.py`.
"""

import importlib.util
import json
import os
import subprocess
import sys

import pytest
from block_shapes import SHAPES
from conftest import (
    BASELINE,
    FENCED_ABOVE,
    FENCED_BELOW_A_TABLE_THAT_NEVER_BEGAN,
    FENCED_REFUSAL,
    MOBILE_URL,
    ORDERS,
    PACT_URL,
    PIPED_TABLE,
    ROOT,
    SIGNER_URL,
    TABLE,
    UNDER_THE_COMMENT,
    URL,
    V2,
    census_case,
    clause,
    crlf,
    load_lib_module,
    load_module,
    local_home,
    mark_root,
    names_path,
    opt_in_shared,
    parity_file,
    shape_text,
    signer_config,
    write,
    write_config,
    write_old_config,
    write_unreadable,
)
from conftest import config_json as table
from test_one_table_walker_reads_what_gfm_renders import (
    HEADERS,
    INDENTS,
    KINDS,
    document,
)

TARGET = "lib/config.py"

config = load_lib_module("config.py", "config_under_test")

# `tests/block_shapes.py`'s config shapes the comment cases read (#667).
COMMENTED_OLD_ROW = shape_text("C5")
COMMENTED_OLD_TABLE = shape_text("C6")
QUOTED_DELIMITERS = shape_text("C1")
LIVE = [("Mode", "shared"), ("Broad gate", "bin/test -q")]


def walk(text):
    """(rows, refusals) for TEXT's `| Item | Value |` table as
    `lib/config.py#gfm_table` reads it: the table an earlier release's
    `config.md` holds, which `seal mode` converts. ROWS are `(item, value)`
    pairs in order, and REFUSALS the walker's sentences joined into one, its
    `holds no` sentence left out: a text with no such table converts to no
    key (`seal.py#converted`)."""
    rows, refusals = config.gfm_table(text, config.OLD_TABLE)
    said = [line for line in refusals if not line.startswith("holds no ")]
    return [tuple(cells) for _line, cells in rows], " ".join(said)


def items(text):
    """The rows `walk` reads in TEXT, the name the row reader's cases spelt."""
    return walk(text)[0]


# The sentence a pact no `Pact signers` key signs is refused in, pinned whole
# (contract rule 14).
NO_SIGNER = (
    "no `Pact signers` key names a signer, and a pact nobody signs is not a "
    "pact — write the origin remote URL of every other signer into that key, "
    "separated by `;`"
)

# `seal.py`, which re-exports `normalise_remote`: the normaliser's cases ask
# it by that name, through the `seal` fixture below.
SCRIPT = os.path.join(ROOT, "skills", "implement", "scripts", "seal.py")

# The `Baseline commit` case asks the reader `chain_check.py` loads for the
# parity arm, as the command reaches it.
chain = load_module(
    os.path.join(ROOT, "skills", "code-review", "scripts", "chain_check.py"),
    "chain_check_for_config",
)

LANGUAGE_ROW = "Commit and pull request language"


@pytest.fixture
def seal():
    spec = importlib.util.spec_from_file_location("agentic_seal", SCRIPT)
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
            "specs/x/design.md",
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
                "specs/x/design.md",
                "docs/specs/y.md",
                "a/b/specs/c/d.md",
                "specs\\x\\design.md",
            ):
                assert config.under_reference_root(rel, roots), rel
            for rel in (
                "seal/threads/1790000000-x/design.md",
                "docs/design.md",
                "specsheet/a",
            ):
                assert not config.under_reference_root(rel, roots), rel
        # No root at either place is no reference root at all: the repository has
        # not opted in, and the 0.3.x `specs/` the checks still read was the
        # plugin's own. Never a `config.json` found relative to wherever the
        # process happens to stand, either.
        stray = tmp_path / "elsewhere"
        write_config(str(stray), table(("Reference specs", "docs/adr")))
        monkeypatch.chdir(stray)
        assert config.reference_roots("") == ()
        assert not config.under_reference_root("specs/x/design.md", ())

    def test_refuses_a_row_written_twice_or_a_file_that_will_not_read(self, tmp_path):
        """#867. A `Reference specs` key written twice has no value, by
        `lib/config.py#config_value`'s rule; the reader used to take the
        first. A file that is there and will not read is the default too, as it
        was, and the reader no longer opens the file itself to find out. Seen red
        against the first-wins reader: `('docs/adr',)`."""
        home = str(tmp_path / "seal")
        write_config(
            home, table(("Reference specs", "docs/adr"), ("Reference specs", "none"))
        )
        assert config.reference_roots(home) is None
        os.remove(os.path.join(home, "config.json"))
        os.mkdir(os.path.join(home, "config.json"))
        assert config.reference_roots(home) is None

    def test_none_declares_no_reference_root(self, tmp_path):
        home = str(tmp_path / "seal")
        write_config(home, table(("Reference specs", "None")))
        roots = config.reference_roots(home)
        assert roots == (), roots
        assert not config.under_reference_root("specs/x/design.md", roots)

    def test_the_plugins_own_root_is_never_a_reference_root(self, tmp_path):
        """A reference root is outside the root by definition; a prefix naming
        `seal/` or anything under it is dropped, and the default never reaches
        `seal/threads/` either."""
        home = str(tmp_path / "seal")
        write_config(home, table(("Reference specs", "seal/threads, seal, specs")))
        roots = config.reference_roots(home)
        assert roots == ("specs",), roots
        assert not config.under_reference_root(
            "seal/threads/1790000000-x/design.md", roots
        )
        assert not config.under_reference_root(
            "seal/threads/1790000000-x/design.md", None
        )
        optin = load_lib_module("optin.py", "optin_for_the_root_name")
        assert config.HOME == optin.HOME, "the reader spells the root another way"

    def test_local_mode_reads_the_row_under_the_git_directory(self, tmp_path):
        """In local mode the root sits under the common git directory and nothing
        of it is in the tree, so with no row every tree `specs` is a reference
        root — and a row there is read like any other."""
        repo = tmp_path / "repo"
        repo.mkdir()
        subprocess.run(["git", "-C", str(repo), "init", "-q"], check=True)
        optin = load_lib_module("optin.py", "optin_for_reference_roots")
        common = optin.git_common_dir(str(repo))
        home = os.path.join(common, "seal")
        mark_root(home)
        assert optin.home_at(str(repo), common) == home, "the fixture is not local mode"
        assert config.reference_roots(home) is None
        assert config.under_reference_root("specs/x/design.md", None)
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


class _Old_config_table:
    """`gfm_table` over an earlier release's `config.md` table, which
    `seal mode` converts: what it reads is what the converter writes, and
    what it refuses the converter refuses to write (#1454). `Test_gfm_table`
    runs these cases."""

    def test_refuses_an_item_below_a_separator_out_of_place(self):
        """tests-todo row 9, from round 2 🟡 5, first shape — shape 8 of #871.
        cmark-gfm shows a stray separator as one of the table's rows, so the
        walker refuses it, naming it. The rows above it are read. Seen red
        against the stop rule, which ended the table there in silence."""
        text = (
            "| Item | Value |\n"
            "|---|---|\n"
            f"| {LANGUAGE_ROW} | Korean |\n"
            "|---|---|\n"
            "| Something else | x |\n"
        )
        rows, said = walk(text)
        assert rows == [(LANGUAGE_ROW, "Korean")]
        assert "stops at `|---|---|`, a delimiter row out of place" in said, said

    def test_a_repeated_header_is_read_as_a_row_and_the_doubled_item_is_refused(
        self, seal
    ):
        """tests-todo row 9, second shape — shape 9 of #871. A second
        `| Item | Value |` line under the table with no delimiter row of its own
        is one of this table's rows to cmark-gfm, so the walker reads it as one,
        and the row below it with it: the language is then written twice, which
        has no value, so the converter writes nothing. Seen red against the
        stop rule, which ended the table at the repeated header and read
        `Korean`."""
        text = (
            "| Item | Value |\n"
            "|---|---|\n"
            f"| {LANGUAGE_ROW} | Korean |\n"
            "| Item | Value |\n"
            f"| {LANGUAGE_ROW} | English |\n"
        )
        assert items(text) == [
            (LANGUAGE_ROW, "Korean"),
            ("Item", "Value"),
            (LANGUAGE_ROW, "English"),
        ]
        pairs, said = seal.converted(text)
        assert pairs is None and f"`{LANGUAGE_ROW}` row written more" in said, said

    def test_a_blank_line_above_the_first_row_ends_the_table_and_the_row_is_refused(
        self,
    ):
        """#871. A blank line under the delimiter row ends the table to
        cmark-gfm, so the row below it is not one of the table's rows: the
        walker refuses it as a row the walk never reaches. Seen red against the
        stop rule, which stepped past the blank line and read `Korean`."""
        text = f"| Item | Value |\n|---|---|\n\n| {LANGUAGE_ROW} | Korean |\n"
        rows, said = walk(text)
        assert rows == []
        assert "a row the walk never reaches" in said, said

    def test_accepts_an_item_value_table_and_no_other(self):
        """A parser that finds a row in anything is not a parser."""
        assert items("# a document with no table\n\nprose.\n") == []
        assert items("| Field | Value |\n|---|---|\n| a | b |\n") == [], (
            "an earlier release's `parity.md` header was `| Field | Value |`; "
            "matching it here would "
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
        rows = items(PIPED_TABLE)
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
        assert items(text) == [
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
        because the walker strips the cell — and one line in the whole tree
        reads differently, in a review report quoting this shape.

        Both members of the class are here. The report named the first; the
        second is the same cause at an INTERNAL pipe, where the line stops being
        a row for the same reason.
        """
        header = "| Item | Value |\n|---|---|\n"
        tight_last = "| Broad gate | C:\\Users\\x\\tools\\|\n"
        tight_first = "| C:\\tools\\| x |\n"
        assert items(header + tight_last) == [], (
            "a backslash against the closing pipe is markdown's escaped pipe, so "
            "the line has no closing pipe left and is not a row. If this returns "
            "a row the pattern changed and `frame/design.md` *What this repair cannot "
            "see* is now wrong"
        )
        assert items(header + tight_first) == [], (
            "the same cause at the pipe BETWEEN the cells — the report named only "
            "the closing one"
        )
        assert items(header + "| Broad gate | C:\\Users\\x\\tools\\ |\n") == [
            ("Broad gate", "C:\\Users\\x\\tools\\")
        ], (
            "written with a space before the closing pipe the value comes back "
            "exactly as the old pattern read it, so no value lost a spelling"
        )
        assert items(header + "| C:\\tools\\ | x |\n") == [("C:\\tools\\", "x")], (
            "and the same for the item cell"
        )

    def test_a_three_column_row_is_refused_and_the_rows_above_it_arrive(self, config):
        """Shape 6 of #871. The escape widens what a cell may hold and must not
        widen what a ROW is: a greedy last cell would read `| a | b | c |` as the
        row `('a', 'b | c')`. Until #871 the line ended the table silently, and
        every row below it fell to its default; cmark-gfm shows those rows, so
        the walker refuses the line instead, naming it, and the rows above it
        are read. Seen red against the stop rule, which ended the table there
        in silence."""
        text = "| Item | Value |\n|---|---|\n| a | b |\n| x | y | z |\n| c | d |\n"
        rows, said = walk(text)
        assert rows == [("a", "b")]
        assert "stops at `| x | y | z |`, which is not a 2-cell row" in said, said

    def test_a_fenced_table_above_the_live_one_is_not_the_table(self, config):
        """A1. The live table is the first one outside every fence.

        A reader that starts at the first `| Item | Value |` header and never
        looks for another takes an example pasted above the live table as the
        table: the mode, the broad command, every row. The shape was invited
        rather than contrived, because the setup template's fenced example
        rows were copied whole into `config.md`.
        """
        assert items(FENCED_ABOVE) == [
            ("Mode", "shared"),
            ("Broad gate", "bin/test -q"),
        ], items(FENCED_ABOVE)

    def test_a_fenced_example_below_a_table_that_never_began_is_still_not_the_table(
        self,
        config,
    ):
        """A2. Both walks step past a line they cannot parse until a row is
        found, so with nothing parsed above it a fenced example's rows became the
        live rows — the same defect one shape over, and the one a repair aimed at
        the fenced HEADER alone would have left standing."""
        rows = items(FENCED_BELOW_A_TABLE_THAT_NEVER_BEGAN)
        assert rows == [], (
            f"the example inside the fence supplied this repository's rows:\n{rows}"
        )

    def test_what_counts_as_a_fence_is_commonmarks_rule_as_far_as_it_goes(self, config):
        """Q3 of `questions.md`, decided and pinned. `frame/design.md` *Data &
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
          - an unclosed fence runs to the end of the file, so the file
            holds no table.

        **A blank line stands above the live header in each fixture since
        #871**, because the walker refuses a header with a non-blank line
        directly above it whatever that line is (the migration's shape, rows 1,
        2 and 11 of the work item's measurement), and the decisions here are
        about which line opens or closes a fence, not about that one. The first
        assertion is that refusal, so the reason for the blank line is pinned
        beside it.
        """
        live = "| Item | Value |\n|---|---|\n| Mode | shared |\n"
        rows, said = walk("    ```\n" + live)
        assert rows == [] and "leave a blank line above the header" in said, said
        assert items("    ```\n\n" + live) == [("Mode", "shared")], (
            "four spaces is an indented code block and not a fence"
        )
        assert items("```` `x` ````\n\n" + live) == [("Mode", "shared")], (
            "a backtick fence's info string may not hold a backtick, so this "
            "line opens no fence"
        )
        assert items(
            "```\n| Item | Value |\n|---|---|\n| Mode | local |\n``````\n\n" + live
        ) == [("Mode", "shared")], (
            "a closing run longer than the opening one closes the block"
        )
        assert items(
            "```\n~~~\n| Item | Value |\n|---|---|\n| Mode | local |\n```\n\n" + live
        ) == [("Mode", "shared")], "a tilde run does not close a backtick fence"
        assert items(
            "````\n```\n| Item | Value |\n|---|---|\n| Mode | local |\n````\n\n" + live
        ) == [("Mode", "shared")], (
            "a run SHORTER than the opening one does not close the block — this "
            "repository's own records wrap a fenced example in four backticks, "
            "and a rule that knew three only would read the inner fence as the "
            "outer one's close and leave the live table inside a fence"
        )
        assert items("```\n```markdown\n" + live) == [], (
            "a run carrying an info string does not close a block, so this file "
            "declares nothing"
        )
        assert items("~~~\n" + live) == [], (
            "an unclosed fence runs to the end of the file"
        )
        assert items("~~~info ~ string\n" + live + "~~~~\n") == [], (
            "a tilde fence's info string is unrestricted, which is CommonMark's "
            "rule and not an exception to this one"
        )

    def test_delimiters_quoted_in_code_spans_hide_nothing(self, config):
        """C1, named as 1790635413 named it (round 1, 🟡 3). A prose line quoting
        the opener in a code span above the table and one quoting the closer
        below it are paragraph text, so the table between them is read. Pins:
        the base read it, and the three rounds lost it by reading inline state."""
        assert items(QUOTED_DELIMITERS) == LIVE

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
        these eight characters, named in the work item's `gaps.md`."""
        from block_shapes import BREAKS, OPEN

        text = (
            f"A note{BREAKS[name]}{OPEN}\n\n| Item | Value |\n|---|---|\n"
            "| Mode | shared |\n-->\n"
        )
        lines = text.splitlines()
        assert [i for i, _line in config.unfenced(lines, text)] == list(
            range(len(lines))
        )
        rows, said = walk(text)
        assert rows == [] and said, said

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
        assert items(text) == []

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
        assert items(text) == []

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
        rows, said = walk(text)
        assert rows == [("Mode", "shared")], rows
        assert "put it on a line of its own" in said, said

    @pytest.mark.parametrize("name", ["LS", "PS", "NEL", "FF", "VT", "FS", "GS", "RS"])
    @pytest.mark.parametrize("where", ["above the header", "under the header"])
    def test_a_header_after_a_break_gfm_does_not_honour_is_no_table(
        self, config, name, where
    ):
        """#871 round 2, yellow 7. A header after a character only
        `str.splitlines` ends a line at, or a delimiter row after one on the
        header's line, is no table to cmark-gfm (measured for FF, U+2028, NEL
        and VT by the round's reviewer). The walk reads no row and refuses."""
        from block_shapes import BREAKS

        brk = BREAKS[name]
        text = (
            f"# c\n\n{brk}| Item | Value |\n|---|---|\n| Mode | shared |\n"
            if where == "above the header"
            else f"# c\n\n| Item | Value |{brk}|---|---|\n| Mode | shared |\n"
        )
        rows, said = walk(text)
        assert rows == [] and "each on a line of its own" in said, (rows, said)


class Test_config_pairs:
    def test_accepts_the_object_as_its_members_in_file_order(self, config, tmp_path):
        """S1. A value holding a pipe is a JSON string like any other, so it
        reads with the pipe plain: the escape a markdown cell needed is gone
        with the cell."""
        write_config(tmp_path, table(("Mode", "shared"), ("Broad gate", "a | b")))
        pairs, refusal = config.config_pairs(str(tmp_path))
        assert refusal is None
        assert list(pairs) == [("Mode", "shared"), ("Broad gate", "a | b")]
        assert config.declared_value(str(tmp_path), "Broad gate") == ("a | b", None)

    def test_accepts_a_byte_order_mark(self, config, tmp_path):
        """S2. An editor that writes a byte order mark has not made the file
        unreadable. Seen red against a `utf-8` decode: the parser refused the
        mark as an unexpected character."""
        path = tmp_path / "config.json"
        path.write_bytes(b"\xef\xbb\xbf" + table(("Mode", "local")).encode("utf-8"))
        assert config.declared_mode(str(tmp_path)) == ("mode", "local")

    def test_refuses_an_empty_home_whatever_the_working_directory_holds(
        self, config, monkeypatch, tmp_path
    ):
        """An empty home is no root, so no file is read, not even the
        `config.json` the working directory holds."""
        write_config(tmp_path, table(("Mode", "shared")))
        monkeypatch.chdir(tmp_path)
        assert config.config_pairs("") == (None, None)

    @pytest.mark.parametrize(
        "text, said",
        [
            ("| Item | Value |\n|---|---|\n| Mode | shared |\n", "does not parse"),
            ('{"Mode": "shared",}\n', "does not parse"),
            ("", "does not parse"),
            ('["Mode", "shared"]\n', "holds a JSON array where"),
            ('"shared"\n', "holds a JSON string where"),
            ("null\n", "holds a JSON null where"),
        ],
        ids=["a table", "a trailing comma", "empty", "an array", "a string", "null"],
    )
    def test_refuses_a_file_that_is_not_one_object_for_every_key(
        self, config, tmp_path, text, said
    ):
        """S2. A file that will not parse, or whose top level is not an object,
        holds no key anybody can read, so every key is that one refusal and
        none reads as absent. The sentence opens with the path, which the
        commands print after their own prefix."""
        write_config(tmp_path, text)
        path = str(tmp_path / "config.json")
        pairs, refusal = config.config_pairs(str(tmp_path))
        assert pairs is None and refusal.startswith(path + " "), refusal
        assert said in refusal, refusal
        assert config.declared_value(str(tmp_path), "Record language") == (
            None,
            refusal,
        )
        assert config.declared_mode(str(tmp_path)) == ("refused", refusal)

    def test_refuses_a_config_md_standing_alone_and_names_seal_mode(
        self, config, tmp_path
    ):
        """S3. A root an earlier release wrote holds `config.md` and no
        `config.json`. Its rows are answers in the table no reader reads now,
        so every key is refused naming the command that converts it, and none
        reads as absent; beside a `config.json` it is not read at all. Seen red
        against a reader that answered the root as declaring nothing."""
        write_old_config(tmp_path, TABLE.format(rows="| Mode | shared |\n"))
        path = str(tmp_path / "config.json")
        pairs, refusal = config.config_pairs(str(tmp_path))
        assert pairs is None and refusal.startswith(path + " is not there"), refusal
        assert "run `seal mode` once" in refusal, refusal
        assert config.declared_mode(str(tmp_path))[0] == "refused"
        write_config(tmp_path, table(("Mode", "local")))
        assert config.declared_mode(str(tmp_path)) == ("mode", "local")


class Test_unreadable_config:
    def test_accepts_a_decode_error_in_its_own_words(self, config):
        exc = UnicodeDecodeError("utf-8", b"\xff", 0, 1, "invalid start byte")
        said = config.unreadable_config(os.path.join("seal", "config.json"), exc)
        assert f"({exc})" in said, said

    def test_refuses_the_error_numbers_wording_and_names_the_reason_alone(self, config):
        """An `OSError` is named by its reason, `Permission denied`, and not by
        the `[Errno 13] …: path` its own text wraps the reason in."""
        path = os.path.join("seal", "config.json")
        said = config.unreadable_config(path, OSError(13, "Permission denied", path))
        assert "(Permission denied)" in said, said
        assert "Errno" not in said, said


class Test_config_value:
    def test_accepts_one_row_as_its_value_and_no_row_as_none(self, config):
        """The two answers beside the refusal, so a reader of `config_value` can
        tell an empty key from no key: `""` is a key somebody left empty, and
        None is no key at all."""
        pairs = [("Mode", "shared"), ("Broad gate", "")]
        assert config.config_value(pairs, "Mode") == ("shared", None)
        assert config.config_value(pairs, "Broad gate") == ("", None)
        assert config.config_value(pairs, "Ledger frozen from") == (None, None)
        assert config.config_value(None, "Mode") == (None, None)

    def test_an_item_spelt_otherwise_names_no_item(self, config):
        """A key is spelt as `templates/setup/config.md` spells it, case
        included, so a `Policy Root` key names nothing and `Policy root` reads
        as absent, which is what that file's paragraph on absent keys says."""
        pairs = [("Policy Root", "elsewhere")]
        assert config.config_value(pairs, "Policy root") == (None, None)

    @pytest.mark.parametrize(
        "value, kind",
        [
            (1, "number"),
            (True, "boolean"),
            (None, "null"),
            (["a"], "array"),
            ({"a": "b"}, "object"),
        ],
    )
    def test_refuses_a_value_that_is_not_a_string_for_that_key_alone(
        self, config, tmp_path, value, kind
    ):
        """S2. Every key's grammar is a string's, so a value of another JSON
        type is no value: it is refused for its key, naming the type, and
        every other key reads. Seen red against a reader that handed the
        parsed value on."""
        write_config(tmp_path, table(("Broad gate", value), ("Mode", "shared")))
        assert config.declared_value(str(tmp_path), "Broad gate") == (
            None,
            f"`Broad gate` holds a JSON {kind}, and its value is a string",
        )
        assert config.declared_mode(str(tmp_path)) == ("mode", "shared")


class Test_declared_mode:
    def test_accepts_the_row_from_the_root_the_folder_is_at(self, config, repo):
        """The reader answers for whichever root exists, so a local-mode
        repository is not read as one that declared nothing."""
        home = local_home(repo)
        write_config(home, table(("Mode", "local")))
        assert config.declared_mode(str(home)) == ("mode", "local")

    @pytest.mark.parametrize(
        "text, expected",
        [
            (None, ("none", "")),
            (table(("Record language", "Korean")), ("none", "")),
            (table(("Mode", "")), ("none", "")),
            ("{}\n", ("none", "")),
            (table(("Mode", "SHARED")), ("mode", "shared")),
            (table(("Mode", "whatever")), ("unknown", "whatever")),
        ],
    )
    def test_the_four_spellings_of_undeclared_are_one_answer(
        self, config, repo, text, expected
    ):
        """The same four `seal.py#declared` already had, because it is the same
        reader — moved, not rewritten. A key that names no mode is told apart from
        no key, because a claim nobody can act on is not the same as no claim."""
        home = opt_in_shared(repo)
        if text is not None:
            write_config(home, text)
        assert config.declared_mode(str(home)) == expected

    @pytest.mark.parametrize(
        "rows",
        [
            [("Mode", "shared"), ("Mode", "local")],
            [("Mode", "local"), ("Mode", "local")],
            [("Mode", "shared"), ("Record language", "Korean"), ("Mode", "")],
        ],
        ids=["two values", "the same value twice", "one value and an empty key"],
    )
    def test_refuses_a_mode_row_written_twice(self, config, repo, rows):
        """S1 of #867, the reader's half, and S2 of #1454. The reader took the
        first row and the checker took the last, so a person editing the one
        they could see might be editing the one that does not answer; a JSON
        parser keeps the last. A key written twice has no value -- not its
        first and not its last -- and the refusal names the key and how many
        times it is written, while every other key reads. Seen red against a
        reader over `json.loads`' dict: `('mode', 'local')` for the first
        shape."""
        home = opt_in_shared(repo)
        write_config(home, table(*rows, ("Broad gate", "bin/test")))
        kind, said = config.declared_mode(str(home))
        assert kind == "refused", (kind, said)
        assert said == "`Mode` appears 2 times — one value"
        assert config.declared_value(str(home), "Broad gate") == ("bin/test", None)

    def test_an_absent_config_and_an_unreadable_one_are_two_states(self, config, repo):
        """S3 of #867, the reader's half. No file declares nothing; a file that is
        there and will not read is refused with a sentence naming the path. The
        reader tells the two apart once, so no caller opens the file again to
        find out."""
        home = opt_in_shared(repo)
        assert config.config_pairs(str(home)) == (None, None)
        assert config.declared_value(str(home), "Mode") == (None, None)
        for shape in ("directory", "undecodable"):
            path = write_unreadable(home, shape)
            text, said = config.config_pairs(str(home))
            assert text is None and said.startswith(path + " is there and cannot"), said
            assert config.declared_value(str(home), "Mode") == (None, said)
            assert config.declared_mode(str(home)) == ("refused", said)
            if shape == "directory":
                os.rmdir(path)
            else:
                os.remove(path)


class _Old_config_shapes:
    """`gfm_table` over the config shapes of #667 and #871, each an earlier
    release's `config.md`. `Test_gfm_table` runs these cases."""

    def test_refuses_a_fenced_pipe_line_as_a_line_somebody_wrote(self, config):
        """A3. The walk that read ON past the stopping line treated any line
        beginning with a pipe as a line somebody wrote as a row — so a line
        inside an example block came back as refused, and `seal gate` quotes a
        refused line back at the person as their own.

        Re-pinned by #871: the fence directly under the delimiter row ends the
        table, as GFM ends it, so the live `Mode` row below the fence is not one
        of the table's rows and the walk refuses it -- naming THAT line, never
        the fenced one.
        """
        rows, refusals = config.gfm_table(FENCED_REFUSAL, config.OLD_TABLE)
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
        frame names, through the walker. A row inside a comment that closes
        is not an answer somebody gave, and a fenced line is no row either.
        Where GFM ends the table at a comment or shows no table at all, the
        walk refuses, naming the live row it did not read -- never the parked
        one -- rather than reading on below it as the stop rule did."""
        text = shape_text(name)
        found, refusals = walk(text)
        assert found == rows, found
        if stops is None:
            assert refusals == "", refusals
        else:
            assert stops in refusals, refusals
            assert "old -q" not in refusals, refusals


class Test_fence_map:
    def test_refuses_to_name_a_fence_inside_a_closed_comment(self, config):
        """S8, C2. The comment closes, so the fence line inside it opens
        nothing, and `fence_map`'s second value names no fence nobody left
        open. Red at base: the fence ran to the end and was named."""
        lines = SHAPES["C2"]
        assert config.fence_map(lines)[1] is None

    def test_accepts_a_fence_nobody_closed_as_the_one_named(self, config):
        """C14, pinned from the other side: the fence that hides the live table
        is the one `fence_map` reports."""
        assert config.fence_map(SHAPES["C14"])[1] == 0

    def test_the_fence_named_is_the_one_that_hides_the_row(self, config):
        """C2 with a fence left open below the table. The old reading runs the
        fence quoted in the comment to the end, so it would name THAT line, which
        opens nothing; the walk sees the tilde fence below the table never close,
        and the line under it is hidden because of it."""
        lines = [*SHAPES["C2"], "", "~~~", "| Broad gate | bin/test -q |"]
        assert config.fence_map(lines)[1] == lines.index("~~~")
        assert items("\n".join(lines)) == [("Mode", "shared")]


class Test_hidden_lines:
    def test_accepts_a_fence_that_closes_as_hidden_and_names_no_opener(self, config):
        assert config.hidden_lines(["```", "| Mode | x |", "```", "after"]) == (
            {0: "fence", 1: "fence", 2: "fence"},
            None,
        )

    def test_refuses_to_name_a_later_fence_left_open_before_the_first(self, config):
        """Two fences that never close: the first is the one that hides the
        lines under it, so it is the one named."""
        lines = ["```", "a", "~~~", "b"]
        assert config.hidden_lines(lines)[1] == 0


class Test_unfenced:
    def test_refuses_a_commented_row_in_either_line_ending(self, config):
        """S5, C5 to C7, named as 1790635413 named them. The rows parked in a
        comment are gone from every walk. Since #871 the live rows under a
        comment that sits inside the table do not arrive either: GFM ends the
        table at the comment, so the walk refuses them, naming the first. Under
        a whole old table parked above the live one, the live table arrives."""
        for text in (COMMENTED_OLD_ROW, COMMENTED_OLD_TABLE, crlf(COMMENTED_OLD_ROW)):
            assert all(
                "old -q" not in line
                for _index, line in config.unfenced(text.splitlines())
            ), text
        assert items(COMMENTED_OLD_TABLE) == LIVE
        for text in (COMMENTED_OLD_ROW, crlf(COMMENTED_OLD_ROW)):
            rows, said = walk(text)
            assert rows == [] and UNDER_THE_COMMENT in said, (text, said)

    def test_accepts_every_line_under_a_mid_line_comment(self, config):
        """C13, the residual `frame/design.md` *Scope* names. A renderer hides the first
        pipe-line behind a lone backtick and a mid-line `<!--`, and knowing that
        needs code spans and the paragraph's extent, which is where all three of
        1790635413's rounds lost ground. The base reads it, so reading it is not
        worse; this pins that nothing here pretends to more."""
        lines = SHAPES["C13"]
        assert [index for index, _line in config.unfenced(lines)] == list(
            range(len(lines))
        )


class Test_pact_declaration:
    def test_accepts_one_pact_normalised(self):
        """S1. One URL: the URL as written, and normalised."""
        pacts, refusals = config.pact_declaration(
            [("Mode", "shared"), ("Pact", "git@example.com:org/Orders-API.git")]
        )
        assert refusals == []
        assert pacts == [
            ("git@example.com:org/Orders-API.git", "example.com/org/orders-api")
        ]

    def test_two_pacts_come_back_in_order(self):
        """S2. `;` separates the pacts a signer signs, and the order is the
        key's."""
        pacts, refusals = config.pact_declaration(
            [
                (
                    "Pact",
                    "https://example.com/org/orders-api ; git@example.com:org/billing.git",
                ),
            ]
        )
        assert refusals == []
        assert [n for _, n in pacts] == [
            "example.com/org/orders-api",
            "example.com/org/billing",
        ]

    def test_accepts_two_pacts_whose_urls_end_in_one_segment(self):
        """S10 of #913: an anchor names the pact by its URL, so two pacts
        ending in one segment are two pacts and nothing is refused."""
        value = "git@example.com:org/api.git;https://example.com/other/api"
        assert config.pact_declaration([("Pact", value)]) == (
            [
                ("git@example.com:org/api.git", "example.com/org/api"),
                ("https://example.com/other/api", "example.com/other/api"),
            ],
            [],
        )

    def test_no_row_and_an_empty_row_hold_no_pact(self):
        """Absent means no pact is held elsewhere, and so do an empty value and
        no file."""
        for pairs in ([("Mode", "shared")], [("Pact", "")], [], None):
            assert config.pact_declaration(pairs) == ([], []), pairs

    @pytest.mark.parametrize(
        "rows",
        [
            [("Pact notify", "sometimes")],
            [("Pact notify", "never"), ("Pact notify", "always")],
        ],
        ids=["a value outside the old vocabulary", "written twice"],
    )
    def test_a_pact_notify_row_an_earlier_release_read_is_ignored(self, rows):
        """`templates/setup/config.md` *Pact*: a `Pact notify` key left in the
        config is read by nobody, with a `Pact` key or without one, so neither
        a value outside the vocabulary it once had nor the key written twice is
        refused. Seen red by `seal mutate` against a reader that refused the
        row (phase 8 of 1791940762)."""
        assert config.pact_declaration([("Pact", URL), *rows]) == (ORDERS, [])
        assert config.pact_declaration(rows) == ([], [])

    def test_refuses_a_row_that_will_not_parse_and_never_reads_it_as_absent(self):
        """Each way an entry fails is a sentence naming it, so a signer that
        wrote a row is never read as one that wrote none."""
        cases = {
            "orders-api": "is not a remote URL",
            "git@example.com:org/a.git;;git@example.com:org/b.git": "holds an empty entry",
            "git@example.com:org/a.git git@example.com:org/b.git": "holds a space",
            "git@example.com:org/api.git;https://example.com/org/api": "are one repository",
        }
        for value, said in cases.items():
            _, refusals = config.pact_declaration([("Pact", value)])
            assert len(refusals) == 1 and said in refusals[0], (value, refusals)
        # A `Pact` key written twice has no value, in the one sentence every
        # config key is refused in (#867): its first is not the answer, so it
        # lists no pact. Seen red against the first-wins reader, which listed `a`.
        pacts, refusals = config.pact_declaration(
            [
                ("Pact", "git@example.com:org/a.git"),
                ("Pact", "git@example.com:org/b.git"),
            ]
        )
        assert pacts == []
        assert refusals == ["`Pact` appears 2 times — one value"]


class Test_declared_pacts:
    def test_an_unreadable_config_is_no_declaration(self, tmp_path):
        """`declared_pacts` is what `seal pact` reads a signer's key
        through. No file is no key; a file that is there and will not read is
        None, which the caller refuses, because a written key read as absent is
        the silence the reader exists to end."""
        assert config.declared_pacts(str(tmp_path / "missing")) == ([], [])
        home = tmp_path / "seal"
        (home / "config.json").mkdir(parents=True)
        assert config.declared_pacts(str(home)) is None
        (home / "config.json").rmdir()
        (home / "config.json").write_text(table(("Pact", URL)), encoding="utf-8")
        pacts, refusals = config.declared_pacts(str(home))
        assert pacts == ORDERS and refusals == []

    def test_refuses_a_signer_config_that_will_not_parse_with_exit_2(self, world):
        """S2 at `seal pact`: a signer's config that will not parse is refused
        as `UNREADABLE`, in the reader's sentence after the path the command
        shows, and the run exits 2. Seen red against the sentence the command
        printed before #1454, `could not be read`, which named no cause."""
        write(world.web, "seal/config.json", '{"Pact": "x",}\n')
        world.cite(clause(V2))
        code, out = world.run()
        assert code == 2, out
        assert f"UNREADABLE {SIGNER_URL} " in out, out
        assert "seal/config.json — does not parse as JSON" in out, out

    @pytest.mark.parametrize(
        "rows",
        [
            [("Pact notify", "sometimes")],
            [("Pact notify", "never"), ("Pact notify", "always")],
        ],
        ids=["a value outside the old vocabulary", "written twice"],
    )
    def test_accepts_a_pact_notify_row_an_earlier_release_read_as_nothing(
        self, world, rows
    ):
        """`templates/setup/config.md` *Pact*: a `Pact notify` key left in a
        signer's config is read by nobody."""
        write(world.web, "seal/config.json", signer_config(("Pact", PACT_URL), *rows))
        world.cite(clause(V2))
        code, out = world.run()
        assert code == 0, out
        assert "REFUSED" not in out and "`Pact notify`" not in out, out


class Test_signer_declaration:
    def test_accepts_every_signer_the_key_lists_in_its_order(self):
        """S7. The pact's repository lists every other signer in its `Pact
        signers` key, separated by `;` as `Pact` separates pacts. Two
        signers ending in one segment are two repositories, because nobody
        cites a signer by name. Seen red against a reader of the `| Signer |`
        table, which had no such name."""
        signers, refusals = config.signer_declaration(
            [
                ("Mode", "shared"),
                (
                    "Pact signers",
                    "git@example.com:org/orders-web.git; https://example.com/other/orders-web",
                ),
            ]
        )
        assert refusals == []
        assert signers == [
            ("git@example.com:org/orders-web.git", "example.com/org/orders-web"),
            ("https://example.com/other/orders-web", "example.com/other/orders-web"),
        ]

    @pytest.mark.parametrize(
        "pairs",
        [None, [], [("Mode", "shared")], [("Pact signers", "")], [("Pact", URL)]],
        ids=["no file", "no key", "no such key", "an empty key", "a Pact key alone"],
    )
    def test_refuses_a_pact_no_key_signs_naming_the_key(self, pairs):
        """A pact nobody signs is not a pact, so an absent or empty key is a
        refusal naming it, not the no-pact answer `pact_declaration` gives
        an absent `Pact` key, and a `Pact` key is no answer about signers."""
        assert config.signer_declaration(pairs) == ([], [NO_SIGNER])

    @pytest.mark.parametrize(
        "value, read, said",
        [
            (
                f"{SIGNER_URL}; orders-mobile",
                [SIGNER_URL],
                "`orders-mobile` is not a remote URL — it reduces to no host and "
                "path, so no repository can be found by it",
            ),
            (
                f"{SIGNER_URL};;{MOBILE_URL}",
                [SIGNER_URL, MOBILE_URL],
                f"the `Pact signers` value `{SIGNER_URL};;{MOBILE_URL}` holds an "
                "empty entry — one remote URL between each `;`",
            ),
            (
                f"{SIGNER_URL} {MOBILE_URL}",
                [],
                f"`{SIGNER_URL} {MOBILE_URL}` holds a space — one remote URL per entry",
            ),
            (
                f"{SIGNER_URL}; git@example.com:org/orders-web.git",
                [SIGNER_URL],
                f"`git@example.com:org/orders-web.git` and `{SIGNER_URL}` are one "
                "repository",
            ),
        ],
        ids=["not a url", "an empty entry", "a space", "one repository twice"],
    )
    def test_refuses_each_entry_that_will_not_read_and_reads_the_rest(
        self, value, read, said
    ):
        """Each entry is read by `remote_entries`, in the sentences the
        `Pact` key prints, and an entry that will not read is refused rather
        than dropped."""
        signers, refusals = config.signer_declaration([("Pact signers", value)])
        assert refusals == [said], refusals
        assert [written for written, _n in signers] == read, signers

    def test_refuses_a_key_written_twice_or_holding_no_string(self):
        """By `config_value`'s rule and in its sentences (#867): neither key
        lists a signer."""
        assert config.signer_declaration(
            [("Pact signers", SIGNER_URL), ("Pact signers", MOBILE_URL)]
        ) == ([], ["`Pact signers` appears 2 times — one value"])
        assert config.signer_declaration([("Pact signers", [SIGNER_URL])]) == (
            [],
            ["`Pact signers` holds a JSON array, and its value is a string"],
        )


class Test_gfm_table(_Old_config_table, _Old_config_shapes):
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
        # The refusal the walker returns, whose remedy the person editing the
        # file follows.
        assert refusals and "blank line above the header" in refusals[0], refusals

    @pytest.mark.parametrize("name", ["LS", "FF"])
    def test_accepts_the_rows_above_a_heading_piece_and_refuses_the_row_below(
        self, name
    ):
        """#871 round 2, yellow 7's class after the table's end. A heading piece
        after a character only `str.splitlines` ends a line at is more of the
        line above to GFM, not a heading, so a line written `| … |` under it is
        still a row nobody reads, and is refused."""
        from block_shapes import BREAKS

        text = (
            "| Item | Value |\n|---|---|\n| Mode | shared |\n\n"
            f"x{BREAKS[name]}## Notes\n| Broad gate | y |\n"
        )
        rows, refusals = config.gfm_table(text, ("Item", "Value"))
        assert [c for _l, c in rows] == [("Mode", "shared")], rows
        assert refusals and "ends above `| Broad gate | y |`" in refusals[0], refusals

    @pytest.mark.parametrize("which", sorted(HEADERS))
    def test_a_line_directly_above_the_header_is_refused(self, which):
        """Whether cmark-gfm renders a table under a line depends on the block
        state above it, which the walker does not track, so a non-blank line the
        walk is shown directly above a header is refused with the blank-line
        remedy (round 1, yellow 5). This reverses the build's first choice,
        which mirrored cmark-gfm's interruption rules line by line and was found
        reading tables cmark-gfm does not render in shapes the corpus did not
        reach. A kind whose last line `unfenced` hides, or a blank line, leaves
        a gap or a blank above the header and is not this rule's."""
        header = HEADERS[which]
        for kind, lines in KINDS.items():
            for indent in INDENTS:
                text = document(header, lines, "before the header", indent)
                split = text.splitlines()
                head = split.index("| " + " | ".join(header) + " |")
                shown = dict(config.unfenced(split, text))
                above = shown.get(head - 1)
                if above is None or not above.strip():
                    continue
                _rows, refusals = config.gfm_table(text, header)
                # The refusal the walker returns, whose remedy the person
                # editing the file follows.
                assert refusals and "blank line above the header" in refusals[0], (
                    kind,
                    indent,
                    refusals,
                )


def parity_members(text):
    """The `(key, value)` members of the migration config TEXT, in order."""
    return json.loads(text, object_pairs_hook=list)


class Test_baseline_commit:
    @pytest.mark.parametrize("sha", [BASELINE, BASELINE[:7]])
    def test_accepts_the_sha_its_one_key_holds_alone(self, sha):
        """S6: the `Baseline commit` reader the parity arm loads through
        `chain_check.py#parity_readers` gives the SHA of `parity.json`'s
        one `Baseline commit` key, whole or abbreviated."""
        reads = chain.parity_readers()[0]
        assert reads.baseline_commit(parity_file(sha)) == (sha, None)

    @pytest.mark.parametrize(
        "text, why",
        [
            (parity_file(None), "`<SHA>`"),
            (parity_file(BASELINE.upper()), BASELINE.upper()),
            (parity_file(BASELINE[:6]), BASELINE[:6]),
            (parity_file(f"`{BASELINE}`"), f"`{BASELINE}`"),
            (parity_file(f"{BASELINE}, read 2026-11-09"), "read 2026-11-09"),
            (
                table(
                    *[
                        (k, v)
                        for k, v in parity_members(parity_file(BASELINE))
                        if k != "Baseline commit"
                    ]
                ),
                "holds no `Baseline commit` key",
            ),
            (
                table(
                    ("Baseline commit", BASELINE),
                    *parity_members(parity_file(BASELINE)),
                ),
                "`Baseline commit` appears 2 times",
            ),
            (table(("Baseline commit", 123)), "holds a JSON number"),
            (
                "| Field | Value |\n|---|---|\n| Baseline commit | `0123456` |\n",
                "does not parse as JSON",
            ),
            ("[]\n", "holds a JSON array"),
        ],
        ids=[
            "the placeholder",
            "upper case",
            "six digits",
            "a code span",
            "a SHA and a date",
            "no such key",
            "the key twice",
            "a number",
            "an earlier release's table",
            "an array",
        ],
    )
    def test_refuses_a_config_that_names_no_sha_and_says_why(self, text, why):
        """S6: a `Baseline commit` that is not 7 to 40 lowercase hex digits
        and nothing else, an absent key, a key written twice, a value that
        is not a string, and a file that is not one JSON object each give
        no SHA and a why naming it, which reads after the file's name."""
        sha, said = config.baseline_commit(text)
        assert sha is None and why in said, (said, text)
        assert not said.startswith(("seal/", "parity")), said


class Test_module:
    def test_an_old_parity_md_is_named_with_every_key_the_template_holds(self):
        """S6 and design *Scope* item 4: `unconverted_parity`, the sentence
        the parity arm refuses an earlier release's `parity.md` in and `seal
        mode` names one in, names the file to write, the template it is
        written from and each of the template's keys, so a person converts
        it without opening another page. The sentence builds from
        `PARITY_KEYS`, held here to the template's keys in order. Its
        readers' cases are in `tests/skills/test_chain_check.py` and
        `tests/skills/test_seal.py`."""
        with open(
            os.path.join(ROOT, "templates", "setup", "parity.json"), encoding="utf-8"
        ) as handle:
            template = handle.read()
        keys = tuple(k for k, _v in parity_members(template))
        assert keys == config.PARITY_KEYS
        said = config.unconverted_parity("seal/parity.json")
        assert "write seal/parity.json" in said, said
        assert "`templates/setup/parity.json`" in said, said
        for key in keys:
            assert f"`{key}`" in said, (key, said)

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
        """`lib/config.py#policy_root`, the one reader every reader asks: an
        empty value and one that leaves the repository read as `docs`."""
        config = load_lib_module("config.py", "agentic_config_for_policy_root")
        (tmp_path / "config.json").write_text(
            table(("Policy root", value)), encoding="utf-8"
        )
        assert config.policy_root(str(tmp_path)) == root
        assert config.policy_root("") == "docs"

    def test_a_reader_copied_without_the_walk_names_it(self, tmp_path):
        """#667. This module imports `lib/blocks.py`, the walk the readers under
        `lib/` share. It is a module, not a script: scripts import it, and a
        script catches the error or names the file first. So a copy without the walk raises one `ImportError` whose
        sentence names the path and what the file is for.
        `tests/lib/test_routing.py` holds `lib/routing.py` to the same."""
        name, siblings = TARGET.rsplit("/", 1)[1], []
        alone = tmp_path / "lib"
        alone.mkdir()
        for file in (name, *siblings):
            with open(os.path.join(ROOT, "lib", file), encoding="utf-8") as f:
                (alone / file).write_text(f.read(), encoding="utf-8")
        done = subprocess.run(
            [
                sys.executable,
                "-c",
                f"import sys; sys.path.insert(0, {str(alone)!r}); import {name[:-3]}",
            ],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )
        assert done.returncode != 0, done.stderr
        last = done.stderr.strip().splitlines()[-1]
        assert last.startswith("ImportError: cannot read "), last
        assert names_path(os.path.join(str(alone), "blocks.py"), last), last
        assert "tells a live row from one quoted in a fence or parked in a comment" in (
            last
        ), last


test_census = census_case(TARGET)
