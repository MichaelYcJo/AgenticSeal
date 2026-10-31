"""`hooks/lib/config.py`, the shared reader of `seal/config.md` and the pact's
tables, one class per function its cases reach.

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
seven cases `tests/skills/test_pact_check.py` left for this module, which run
`seal pact` over the pact's world in `tests/conftest.py`. Each case keeps
its body, except two that read the pact's text as `PACT_TEXT`, because
`PACT` is the world's path to it; a name its old file defined for it is
defined here, and a fixture or text two files read is `tests/conftest.py`'s.

#942's round 9 fix pass placed two more, each a case of this module alone:
the table walker's refusal of a line shown directly above the header, from
the oracle file, whose corpus it imports from there, and the case that copies
this module without `hooks/lib/blocks.py`, from
`tests/test_a_script_copied_alone_exits_2.py`, whose `routing.py` row is in
`tests/hooks/test_routing.py`.
"""

import importlib.util
import os
import subprocess
import sys

import config_shapes
import pytest
from block_shapes import SHAPES
from conftest import (
    BASELINE,
    FENCED_ABOVE,
    FENCED_BELOW_A_TABLE_THAT_NEVER_BEGAN,
    FENCED_REFUSAL,
    MOBILE_URL,
    ORDERS,
    PACT,
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
    load_hook_module,
    load_module,
    local_home,
    mark_root,
    names_path,
    old_header,
    opt_in_shared,
    pact,
    parity_file,
    shape_text,
    signer_config,
    write,
    write_config,
    write_unreadable,
)
from conftest import commit_everything_as_e as commit
from conftest import config_table as table
from test_one_table_walker_reads_what_gfm_renders import (
    HEADERS,
    INDENTS,
    KINDS,
    document,
)

TARGET = "hooks/lib/config.py"

config = load_hook_module("lib/config.py", "config_under_test")

# The mode gate, whose `undeclared` one reader case asks beside the reader.
GATE = "mode-gate.py"

# `tests/block_shapes.py`'s config shapes the comment cases read (#667).
COMMENTED_OLD_ROW = shape_text("C5")
COMMENTED_OLD_TABLE = shape_text("C6")
QUOTED_DELIMITERS = shape_text("C1")
LIVE = [("Mode", "shared"), ("Broad gate", "bin/test -q")]

# The pact readers' texts, from `tests/behaviour/test_a_signer_declares_its_pact.py`.
# The pact's text is `PACT_TEXT` here: `PACT` is the pact's path, which the
# cases that run `seal pact` over the world write to.
CONFIG_TOP = "# config\n\n| Item | Value |\n|---|---|\n| Mode | shared |\n"
CONFIG = CONFIG_TOP + f"| Pact | {URL} |\n"


def walked(text):
    """The walker's refusals of TEXT's `| Item | Value |` table, which
    `pact_declaration` appends after its own since #871. The sentences
    themselves are pinned by `Test_config_table` and by the oracle; here what
    is pinned is that they arrive, last."""
    return config.config_table(text)[1]


BARE_PIPE = (
    "has a `Item | Value` table that stops at "
    "`| Broad gate | bin/test -q | tee out |`, which is not a 2-cell row "
    "written `| … | … |` — every row below it would go unread"
)

PACT_TEXT = (
    "# Pact\n\n<!-- | Signer |\n|---|\n| git@example.com:org/quoted.git | -->\n\n"
    "| Signer |\n|---|\n"
    "| git@example.com:org/orders-web.git |\n"
    "| https://example.com/other/orders-web |\n\n"
    "## Order response shape\n\nx\n"
)

# The header 0.18.x wrote (#822), spelled out here rather than read from
# `hooks/lib/config.py#renamed_header`: a case taking the old header from the
# reader's own constant would pass with that constant changed, and the pacts
# written in 0.18.x would not.
OLD = PACT_TEXT.replace("| Signer |\n|---|\n|", "| Signatory |\n|---|\n|")

BOTH = (
    "also holds a `| Signatory |` header, the word before 0.19.0, and nothing "
    "under it is read while the `| Signer |` table stands — move its rows into "
    "that table and delete it"
)

# Every way GFM ends or breaks the `Signer` table (round 2 of #647). A table is
# a header row, a delimiter row of the same width, then body rows, and it is
# broken by a blank line or by the start of another block. Each way is either
# read as GFM reads it, or refused; none drops a signer while the table reads
# as complete. These cases pin the SENTENCES the pact prints; that the walk
# reads what GFM renders is held by
# `tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py`, over a corpus
# enumerated from the block kinds and judged by cmark-gfm itself.
WEB = "https://example.com/org/orders-web"
WEB_NORMALISED = "example.com/org/orders-web"
MOBILE = "https://example.com/org/orders-mobile"
HEAD = f"# Pact\n\n| Signer |\n|---|\n| {WEB} |\n"
CLAUSE = "\n## Order response shape\n\nx\n"
ENDS_ABOVE = (
    f"has a `Signer` table that ends above `| {MOBILE} |`, a row the walk "
    "never reaches — it and every signer below it would go unread"
)


def stops_at(line, why="which is not a one-cell row written `| … |`"):
    return (
        f"has a `Signer` table that stops at `{line}`, {why} — every "
        "signer below it would go unread"
    )


TABLE_ENDS = [
    ("a blank line, then a row", HEAD + f"\n| {MOBILE} |\n" + CLAUSE, ENDS_ABOVE),
    (
        "a line with no pipe",
        HEAD + f"{MOBILE}\n" + CLAUSE,
        f"has a `Signer` table that continues with `{MOBILE}`, a line with "
        "no pipe that GFM reads as one of its rows — write it as `| … |`",
    ),
    ("a heading", HEAD + f"## A clause\n\n| {MOBILE} |\n", None),
    ("a fence", HEAD + f"```\nx\n```\n| {MOBILE} |\n" + CLAUSE, ENDS_ABOVE),
    ("an HTML comment", HEAD + f"<!-- a note -->\n| {MOBILE} |\n" + CLAUSE, ENDS_ABOVE),
    ("a block quote", HEAD + f"> a note\n| {MOBILE} |\n" + CLAUSE, ENDS_ABOVE),
    ("a list item", HEAD + f"- a note\n| {MOBILE} |\n" + CLAUSE, ENDS_ABOVE),
    ("the end of the file", HEAD, None),
    # Round 3 of #735 (🟡 18): an autolink is a row to GFM, not an HTML
    # block, and a thematic break ends the table rather than being a row.
    (
        "an autolink row",
        HEAD + f"<{MOBILE}>\n" + CLAUSE,
        f"has a `Signer` table that continues with `<{MOBILE}>`, a line with "
        "no pipe that GFM reads as one of its rows — write it as `| … |`",
    ),
    ("an HTML block", HEAD + f"<div>\n| {MOBILE} |\n" + CLAUSE, ENDS_ABOVE),
    ("an ordered list item", HEAD + f"1. a note\n| {MOBILE} |\n" + CLAUSE, ENDS_ABOVE),
    ("a thematic break", HEAD + f"***\n| {MOBILE} |\n" + CLAUSE, ENDS_ABOVE),
    ("a thematic break, then a clause", HEAD + "---\n" + CLAUSE, None),
    # ⬜ 22: indented as GFM permits, read rather than refused.
    (
        "an indented header, delimiter and row",
        f"# Pact\n\n   | Signer |\n  |---|\n | {WEB} |\n" + CLAUSE,
        None,
    ),
    (
        "a row four columns in",
        HEAD + f"    | {MOBILE} |\n" + CLAUSE,
        f"has a `Signer` table that ends above `| {MOBILE} |`, a row the walk "
        "never reaches — it and every signer below it would go unread",
    ),
    (
        "a header GFM reads into a list item",
        f"# Pact\n\n- a note\n| Signer |\n|---|\n| {WEB} |\n" + CLAUSE,
        "has a `| Signer |` header directly under `- a note`, and GFM "
        "renders a table under a line only in some of the shapes that line "
        "can take — leave a blank line above the header",
    ),
    (
        "no delimiter row",
        f"# Pact\n\n| Signer |\n| {WEB} |\n" + CLAUSE,
        "has a `| Signer |` header with no delimiter row under it, so GFM "
        "renders no table there",
    ),
    (
        "a comment between the header and its delimiter",
        f"# Pact\n\n| Signer |\n<!-- a note -->\n|---|\n| {WEB} |\n" + CLAUSE,
        "has a `| Signer |` header with no delimiter row under it, so GFM "
        "renders no table there",
    ),
    (
        "a delimiter row of the wrong width",
        f"# Pact\n\n| Signer |\n|---|---|\n| {WEB} |\n" + CLAUSE,
        "has a `| Signer |` header over a delimiter row of 2 cells, so GFM "
        "renders no table there",
    ),
    (
        "a delimiter row out of place",
        HEAD + f"|---|\n| {MOBILE} |\n" + CLAUSE,
        stops_at("|---|", "a delimiter row out of place"),
    ),
    ("too few cells", HEAD + "|  |\n" + CLAUSE, "an empty row"),
    (
        "too many cells",
        HEAD + f"| {MOBILE} | the app |\n" + CLAUSE,
        stops_at(f"| {MOBILE} | the app |"),
    ),
    ("no closing pipe", HEAD + f"| {MOBILE}\n" + CLAUSE, stops_at(f"| {MOBILE}")),
    ("no opening pipe", HEAD + f"{MOBILE} |\n" + CLAUSE, stops_at(f"{MOBILE} |")),
]

ENTRY = "has a `Signer` entry that will not read: "

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
    """This file's `hooks/lib/config.py`; the old file loaded a copy per call."""
    return config


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
        # plugin's own. Never a `config.md` found relative to wherever the
        # process happens to stand, either.
        stray = tmp_path / "elsewhere"
        write_config(str(stray), table(("Reference specs", "docs/adr")))
        monkeypatch.chdir(stray)
        assert config.reference_roots("") == ()
        assert not config.under_reference_root("specs/x/design.md", ())

    def test_refuses_a_row_written_twice_or_a_file_that_will_not_read(self, tmp_path):
        """#867. A `Reference specs` row written twice has no value, by
        `hooks/lib/config.py#config_value`'s rule; the reader used to take the
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
        assert not config.under_reference_root("specs/x/design.md", roots)

    def test_a_row_inside_a_fence_is_not_a_row(self, tmp_path):
        """`hooks/lib/config.py#unfenced` filters in front of the table walk, so a
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
        optin = load_hook_module("lib/optin.py", "optin_for_the_root_name")
        assert config.HOME == optin.HOME, "the reader spells the root another way"

    def test_local_mode_reads_the_row_under_the_git_directory(self, tmp_path):
        """In local mode the root sits under the common git directory and nothing
        of it is in the tree, so with no row every tree `specs` is a reference
        root — and a row there is read like any other."""
        repo = tmp_path / "repo"
        repo.mkdir()
        subprocess.run(["git", "-C", str(repo), "init", "-q"], check=True)
        optin = load_hook_module("lib/optin.py", "optin_for_reference_roots")
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
            "a row the pattern changed and `frame/design.md` *What this repair cannot "
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
        points at `templates/setup/config.md`, and `skills/config/SKILL.md` step 3
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
          - an unclosed fence runs to the end of the file, which lands on
            *nothing is declared* — the direction `hooks/lib/config.py` already
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


class Test_config_text:
    def test_accepts_the_file_as_utf8_text(self, config, tmp_path):
        text = "| Item | Value |\n|---|---|\n| Mode | shared |\n"
        write_config(tmp_path, text)
        assert config.config_text(str(tmp_path)) == (text, None)

    def test_refuses_an_empty_home_whatever_the_working_directory_holds(
        self, config, monkeypatch, tmp_path
    ):
        """An empty home is no root, so no file is read, not even the
        `config.md` the working directory holds."""
        write_config(tmp_path, "| Item | Value |\n|---|---|\n| Mode | shared |\n")
        monkeypatch.chdir(tmp_path)
        assert config.config_text("") == (None, None)


class Test_unreadable_config:
    def test_accepts_a_decode_error_in_its_own_words(self, config):
        exc = UnicodeDecodeError("utf-8", b"\xff", 0, 1, "invalid start byte")
        said = config.unreadable_config(os.path.join("seal", "config.md"), exc)
        assert f"({exc})" in said, said

    def test_refuses_the_error_numbers_wording_and_names_the_reason_alone(self, config):
        """An `OSError` is named by its reason, `Permission denied`, and not by
        the `[Errno 13] …: path` its own text wraps the reason in."""
        path = os.path.join("seal", "config.md")
        said = config.unreadable_config(path, OSError(13, "Permission denied", path))
        assert "(Permission denied)" in said, said
        assert "Errno" not in said, said


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

    def test_an_item_spelt_otherwise_names_no_item(self, config):
        """An item is its row's first cell spelt as `templates/setup/config.md`
        spells it, case included, so a `Policy Root` row names no item and
        `Policy root` reads as absent, which is what that file's paragraph on
        absent rows says."""
        text = TABLE.format(rows="| Policy Root | elsewhere |\n")
        assert config.config_value(text, "Policy root") == (None, None)

    def test_a_fenced_example_of_a_row_does_not_double_the_live_one(self, config):
        """The count is over the rows `config_rows` takes, so the example a
        person pastes from `templates/setup/config.md` into a fence above the table
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

        gate = load_hook_module(GATE, "agentic_mode_gate_for_415")
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
        `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`, carries a
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
        inside an example block came back as refused, and `seal gate` quotes a
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
        and neither `seal gate`'s `fence_left_open` nor `seal.py`'s write guard,
        which both ask `fence_map`'s second value, names a fence nobody left
        open. Red at base: the fence ran to the end and was named."""
        lines = SHAPES["C2"]
        assert config.fence_map(lines)[1] is None
        home = tmp_path / "seal"
        home.mkdir()
        write_config(home, shape_text("C2"))
        path = os.path.join(ROOT, "skills", "verify", "scripts", "broad_gate.py")
        spec = importlib.util.spec_from_file_location("agentic_gate_for_667", path)
        gate = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(gate)
        assert gate.fence_left_open(str(home)) is False

    def test_accepts_a_fence_nobody_closed_as_the_one_named(self, config):
        """C14, pinned from the other side: the fence that hides the live table
        is the one `fence_map` reports, so `seal gate` still says *close that
        fence*."""
        assert config.fence_map(SHAPES["C14"])[1] == 0

    def test_the_fence_named_is_the_one_that_hides_the_row(self, config):
        """C2 with a fence left open below the table. The old reading runs the
        fence quoted in the comment to the end, so it would name THAT line, which
        opens nothing; the walk sees the tilde fence below the table never close,
        and the line under it is hidden because of it. That is the fence
        `seal gate` has to tell the person to close."""
        lines = [*SHAPES["C2"], "", "~~~", "| Broad gate | bin/test -q |"]
        assert config.fence_map(lines)[1] == lines.index("~~~")
        assert config.config_rows("\n".join(lines)) == [("Mode", "shared")]


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
            table(("Mode", "shared"), ("Pact", "git@example.com:org/Orders-API.git"))
        )
        assert refusals == []
        assert pacts == [
            ("git@example.com:org/Orders-API.git", "example.com/org/orders-api")
        ]

    def test_two_pacts_come_back_in_order(self):
        """S2. `;` separates the pacts a signer signs, and the order is the
        row's."""
        pacts, refusals = config.pact_declaration(
            table(
                (
                    "Pact",
                    "https://example.com/org/orders-api ; git@example.com:org/billing.git",
                ),
            )
        )
        assert refusals == []
        assert [n for _, n in pacts] == [
            "example.com/org/orders-api",
            "example.com/org/billing",
        ]

    def test_accepts_two_pacts_whose_urls_end_in_one_segment(self):
        """S10 of #913: an anchor names the pact by its URL, so two pacts
        ending in one segment are two pacts and nothing is refused. Seen red
        against `977b6613`, which refused them as ambiguous to a name."""
        value = "git@example.com:org/api.git;https://example.com/other/api"
        assert config.pact_declaration(table(("Pact", value))) == (
            [
                ("git@example.com:org/api.git", "example.com/org/api"),
                ("https://example.com/other/api", "example.com/other/api"),
            ],
            [],
        )

    def test_no_row_and_an_empty_row_hold_no_pact(self):
        """Absent means no pact is held elsewhere, and so do an empty value and
        a file with no table."""
        for text in (
            table(("Mode", "shared")),
            table(("Pact", "")),
            "no table here\n",
        ):
            assert config.pact_declaration(text) == ([], []), text

    @pytest.mark.parametrize(
        "rows",
        [
            [("Pact notify", "sometimes")],
            [("Pact notify", "never"), ("Pact notify", "always")],
        ],
        ids=["a value outside the old vocabulary", "written twice"],
    )
    def test_a_pact_notify_row_an_earlier_release_read_is_ignored(self, rows):
        """`templates/setup/config.md` *Pact*: a `Pact notify` row left in the table
        is read by nobody, with a `Pact` row or without one, so neither a value
        outside the vocabulary the row once had nor the row written twice is
        refused. Seen red by `seal mutate` against a reader that refused the
        row (phase 8 of 1791940762)."""
        assert config.pact_declaration(table(("Pact", URL), *rows)) == (ORDERS, [])
        assert config.pact_declaration(table(*rows)) == ([], [])

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
            _, refusals = config.pact_declaration(table(("Pact", value)))
            assert len(refusals) == 1 and said in refusals[0], (value, refusals)
        # A `Pact` row written twice has no value, in the one sentence every
        # config row is refused in (#867): its first row is not the answer, so it
        # lists no pact. Seen red against the first-wins reader, which listed `a`.
        pacts, refusals = config.pact_declaration(
            table(
                ("Pact", "git@example.com:org/a.git"),
                ("Pact", "git@example.com:org/b.git"),
            )
        )
        assert pacts == []
        assert refusals == ["`Pact` appears 2 times — one value"]

    @pytest.mark.parametrize(
        "text",
        [
            f"| Item | Value |\n|---|---|\n | Pact | {URL} |\n| Mode | shared |\n",
            CONFIG_TOP + f"  | Pact | {URL} |\n",
        ],
        ids=["between the header and the first row", "indented"],
    )
    def test_an_indented_pact_row_is_read_as_cmark_gfm_renders_it(self, text):
        """#871. A row indented one to three spaces is one of the table's rows
        to cmark-gfm, and the walker reads it: the row is read, and nothing is
        refused. Seen red against the stop rule, whose row pattern began at the
        margin."""
        assert config.pact_declaration(text) == (ORDERS, [])

    def test_a_signer_config_the_walker_refuses_is_refused_after_the_pact(self):
        """#871. A signer's table is read by the walker cmark-gfm holds, so a
        line it refuses is refused here as well, after every other refusal. A
        `Pact` row above the line is read; one below it is a row the walk never
        read, so no pact comes back. Seen red against the stop rule: the line
        ended the table in silence and nothing was refused."""
        bad = "| Broad gate | bin/test -q | tee out |\n"
        assert config.pact_declaration(CONFIG + bad) == (ORDERS, [BARE_PIPE])
        assert walked(CONFIG + bad) == [BARE_PIPE]
        assert config.pact_declaration(CONFIG_TOP + bad + f"| Pact | {URL} |\n") == (
            [],
            [BARE_PIPE],
        )
        # The arm a doubled `Pact` returns from early keeps the walker's sentence
        # last too: seen red by `seal mutate` dropping it on that arm alone.
        doubled = CONFIG + "| Pact | git@example.com:org/b.git |\n" + bad
        assert config.pact_declaration(doubled) == (
            [],
            ["`Pact` appears 2 times — one value", BARE_PIPE],
        )


class Test_declared_pacts:
    def test_an_unreadable_config_is_no_declaration(self, tmp_path):
        """`declared_pacts` is what `seal pact` reads a signer's row
        through. No file is no row; a file that is there and will not read is
        None, which the caller refuses, because a written row read as absent is
        the silence the reader exists to end."""
        assert config.declared_pacts(str(tmp_path / "missing")) == ([], [])
        home = tmp_path / "seal"
        (home / "config.md").mkdir(parents=True)
        assert config.declared_pacts(str(home)) is None
        (home / "config.md").rmdir()
        (home / "config.md").write_text(table(("Pact", URL)), encoding="utf-8")
        pacts, refusals = config.declared_pacts(str(home))
        assert pacts == ORDERS and refusals == []

    def test_refuses_a_signer_config_the_walker_refuses_with_exit_2(self, world):
        """S4 of #871: a bare-piped line in a signer's table is refused in the
        walker's sentence, naming the line, and the run exits 2."""
        write(
            world.web,
            "seal/config.md",
            signer_config(("Pact", PACT_URL))
            + "| Broad gate | bin/test -q | tee out |\n",
        )
        world.cite(clause(V2))
        code, out = world.run()
        assert code == 2, out
        assert (
            f"REFUSED {SIGNER_URL} seal/config.md — has a `Item | Value` table that "
            "stops at `| Broad gate | bin/test -q | tee out |`, which is not a "
            "2-cell row written `| … | … |`"
        ) in out, out

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
        """`templates/setup/config.md` *Pact*: a `Pact notify` row left in a signer's
        table is read by nobody."""
        write(world.web, "seal/config.md", signer_config(("Pact", PACT_URL), *rows))
        world.cite(clause(V2))
        code, out = world.run()
        assert code == 0, out
        assert "REFUSED" not in out and "`Pact notify`" not in out, out


class Test_pact_signers:
    def test_accepts_the_signers_a_pact_lists_and_no_table_in_a_comment(self):
        """Two signers may end in one segment, because nobody cites a
        signer by name; a table in a comment block is not the table."""
        signers, refusals, header = config.pact_signers(PACT_TEXT)
        assert refusals == [] and header == ("Signer",)
        assert [n for _, n in signers] == [
            "example.com/org/orders-web",
            "example.com/other/orders-web",
        ]

    def test_refuses_a_pact_with_no_table_or_an_unfilled_one(self):
        """A pact nobody signs is not a pact, and the template's placeholder row
        is refused rather than read as a signer. A pact holding neither header
        is refused naming the new one (S3 of #822)."""
        assert config.pact_signers("# Pact\n\n## A\n") == (
            [],
            ["holds no `| Signer |` table, so it names no signer"],
            None,
        )
        with open(
            os.path.join(ROOT, "templates", "setup", "pact.md"), encoding="utf-8"
        ) as h:
            signers, refusals, header = config.pact_signers(h.read())
        assert signers == [] and len(refusals) == 1 and "holds a space" in refusals[0]
        assert header == ("Signer",), "the template begins a pact with the new word"
        _, refusals, _ = config.pact_signers("| Signer |\n|---|\n\n## A\n")
        assert refusals == ["has a `Signer` table that lists nobody"]
        # A header GFM renders no table under is that refusal alone: it names
        # no table, so it cannot be one that lists nobody.
        assert config.pact_signers("| Signer |\n\n## A\n") == (
            [],
            [
                "has a `| Signer |` header with no delimiter row under it, so "
                "GFM renders no table there"
            ],
            ("Signer",),
        )

    def test_s2_a_pact_headed_as_0_18_wrote_it_is_read_the_same(self):
        """The old header reads to the same signers, and the reader says which
        header it read, so a caller can name the rename without reading the text
        again; the comment block's quoted table is still not the table."""
        assert "| Signatory |\n|---|\n| git@example.com:org/orders-web" in OLD
        signers, refusals, header = config.pact_signers(OLD)
        assert (signers, refusals) == config.pact_signers(PACT_TEXT)[:2]
        assert header == ("Signatory",)
        assert config.renamed_header(config.SIGNER_HEADER)[0] == header

    def test_s2_every_refusal_under_the_old_header_names_it(self):
        """A table under the old header that lists nobody, or holds an entry
        that will not read, is refused in the old header's word."""
        _, refusals, header = config.pact_signers("| Signatory |\n|---|\n\n## A\n")
        assert refusals == ["has a `Signatory` table that lists nobody"]
        assert header == ("Signatory",)
        _, refusals, _ = config.pact_signers(
            "| Signatory |\n|---|\n| orders-mobile |\n\n## A\n"
        )
        assert refusals == [
            "has a `Signatory` entry that will not read: `orders-mobile` is not a "
            "remote URL — it reduces to no host and path, so no repository can be "
            "found by it"
        ], refusals

    def test_s4_a_pact_holding_both_tables_reads_signer_and_refuses_the_old_one(
        self,
    ):
        """S4 of #822, and round 1's yellow 1. A `| Signer |` table is read
        alone, and an old table anywhere else in the file is refused rather than
        left unread: below it under a heading, above it under a heading, or
        above it with only a blank line between. Its rows hold signers, and a
        signer nobody reads at exit 0 is what the table walker exists to end.
        Directly below after a blank line, the walk's stray-row refusal already
        names it; with no blank line GFM reads it as one of the `Signer` rows,
        and it is named as the old header rather than as an entry. It is never
        named twice."""
        signer = "# Pact\n\n| Signer |\n|---|\n| https://example.com/org/orders-web |\n"
        old = "| Signatory |\n|---|\n| https://example.com/org/billing |\n"
        for text in (
            signer + "\n## Before\n\n" + old + "\n## A\n\nx\n",
            f"# Pact\n\n{old}\n## Now\n\n" + signer.split("\n\n", 1)[1],
            f"# Pact\n\n{old}\n" + signer.split("\n\n", 1)[1],
        ):
            signers, refusals, header = config.pact_signers(text)
            assert [s[1] for s in signers] == [WEB_NORMALISED], (text, signers)
            assert refusals == [BOTH] and header == ("Signer",), (text, refusals)
        _, refusals, header = config.pact_signers(signer + "\n" + old)
        assert header == ("Signer",)
        assert refusals == [
            "has a `Signer` table that ends above `| Signatory |`, a row the walk "
            "never reaches — it and every signer below it would go unread"
        ], refusals
        # Written without its spaces, the old header is quoted as written by the
        # stray-row refusal, and is still named once (round 2 of #822, white 5).
        _, refusals, _ = config.pact_signers(
            signer + "\n|Signatory|\n|---|\n|https://example.com/org/billing|\n"
        )
        assert len(refusals) == 1 and "ends above `|Signatory|`" in refusals[0], (
            refusals
        )
        # With no blank line above it, GFM reads the old header as a row of the
        # `Signer` table; it is named once, as a line inside that table, and not
        # also as an entry that is not a remote URL (round 3 of #822, white 11;
        # #830). A second old table further down does not name it twice.
        glued = (
            "holds a `| Signatory |` line inside its `| Signer |` table, the word "
            "before 0.19.0, which GFM reads as one of that table's rows — delete "
            "the line"
        )
        for under in (
            "|Signatory|\n|---|\n|https://example.com/org/billing|\n",
            "| Signatory |\n",
            "  | Signatory |\n",
            "| Signatory |\n\n## X\n\n| Signatory |\n|---|\n| https://example.com/org/b |\n",
        ):
            # The line is quoted as it is written, its indent aside, so a person
            # searching the file for it finds it (#831).
            signers, refusals, _ = config.pact_signers(signer + under)
            assert [s[1] for s in signers] == [WEB_NORMALISED], signers
            assert sum("Signatory" in r for r in refusals) == 1, refusals
            quoted = under.split("\n", 1)[0].strip()
            assert glued.replace("`| Signatory |`", f"`{quoted}`") in refusals, refusals
        # Rows under a glued old header with no delimiter row are rows of the
        # `Signer` table to GFM, and they are read as signers; the refusal says
        # so rather than "nothing under it is read" (post-review check of #830).
        signers, refusals, _ = config.pact_signers(
            signer + "| Signatory |\n| https://example.com/org/billing |\n"
        )
        assert [s[1] for s in signers] == [
            WEB_NORMALISED,
            "example.com/org/billing",
        ], signers
        assert refusals == [glued], refusals
        # A glued old header above a second old table after a blank line: the
        # walk's stray-row refusal names the second, and the glued line is not
        # also refused as an entry (post-review check 2 of #830; #831).
        signers, refusals, _ = config.pact_signers(
            signer
            + "| Signatory |\n\n| Signatory |\n|---|\n| https://example.com/org/billing |\n"
        )
        assert [s[1] for s in signers] == [WEB_NORMALISED], signers
        assert refusals == [
            "has a `Signer` table that ends above `| Signatory |`, a row the walk "
            "never reaches — it and every signer below it would go unread"
        ], refusals

    def test_s4_a_broken_signer_table_does_not_fall_back_to_the_old_one(self):
        """A `Signer` table that will not read is refused as it stands; a
        well-formed old table below it is not read in its place, and is named."""
        text = (
            "# Pact\n\n- a note\n| Signer |\n|---|\n| https://example.com/org/a |\n\n"
            "| Signatory |\n|---|\n| https://example.com/org/b |\n\n## A\n\nx\n"
        )
        signers, refusals, header = config.pact_signers(text)
        assert signers == [] and header == ("Signer",), (signers, header)
        assert refusals and "`| Signer |` header directly under" in refusals[0]
        assert BOTH in refusals, refusals

    @pytest.mark.parametrize(
        "row",
        [
            "| https://example.com/org/orders-mobile",
            "| https://example.com/org/orders-mobile | the app |",
        ],
        ids=["no closing pipe", "two cells"],
    )
    def test_a_signer_row_the_walk_cannot_read_is_refused(self, row):
        """A table line the walk cannot read ends it, and the signers below
        it would go unread; the line is refused rather than passed in silence."""
        text = (
            "# Pact\n\n| Signer |\n|---|\n| https://example.com/org/orders-web |\n"
            + row
            + "\n\n## A\n\nx\n"
        )
        signers, refusals, _ = config.pact_signers(text)
        assert [s[1] for s in signers] == [WEB_NORMALISED]
        assert refusals == [
            f"has a `Signer` table that stops at `{row}`, which is not a one-cell "
            "row written `| … |` — every signer below it would go unread"
        ], refusals

    @pytest.mark.parametrize(
        "text, said", [c[1:] for c in TABLE_ENDS], ids=[c[0] for c in TABLE_ENDS]
    )
    def test_every_way_the_table_ends_is_read_or_refused(self, text, said):
        signers, refusals, _ = config.pact_signers(text)
        if said is None:
            assert refusals == [], refusals
            assert [s[1] for s in signers] == ["example.com/org/orders-web"]
        else:
            assert any(said in r for r in refusals), refusals

    @pytest.mark.parametrize(
        "row, sentence",
        [
            ("|  |", ENTRY + "an empty row"),
            (
                "| https://example.com/org/orders web |",
                ENTRY + "`https://example.com/org/orders web` holds a space — one "
                "remote URL per entry",
            ),
            (
                "| orders-mobile |",
                ENTRY + "`orders-mobile` is not a remote URL — it reduces to no host "
                "and path, so no repository can be found by it",
            ),
            (
                "| git@example.com:org/orders-web.git |",
                ENTRY + "`git@example.com:org/orders-web.git` and "
                "`https://example.com/org/orders-web` are one repository",
            ),
        ],
        ids=["empty", "a space", "not a url", "one repository"],
    )
    def test_every_entry_refusal_reads_after_the_pact(self, row, sentence):
        """`seal pact` prints a table refusal after "the pact "; each sentence
        an entry can raise is pinned whole (round 2 of #647, white 14)."""
        text = HEAD + row + "\n" + CLAUSE
        _, refusals, _ = config.pact_signers(text)
        assert refusals == [sentence], refusals
        assert ("the pact " + sentence).count("the pact the") == 0

    def test_s2_a_broken_table_under_the_old_header_is_refused_naming_it(self, world):
        """The refusal names the header the walk was asked for, so a table
        under the old header that will not read says `Signatory`, beside the
        rename line; the exit is the refusal's."""
        text = old_header(pact(V2)).replace(
            f"| {SIGNER_URL} |\n", f"| {SIGNER_URL} |\n| {MOBILE_URL}\n"
        )
        write(world.api, PACT, text)
        commit(world.api, "an old header over a row with no closing pipe")
        world.cite(clause(V2))
        code, out = world.run()
        assert code == 2, out
        assert "heads its table `| Signatory |`" in out, out
        assert (
            "REFUSED seal/pact.md — the pact has a `Signatory` table that stops at "
            f"`| {MOBILE_URL}`"
        ) in out, out

    def test_s4_a_pact_holding_both_tables_is_exit_2_naming_the_old_one(self, world):
        """The old table above the new one, under a heading of its own, holds a
        signer the `Signer` table does not list; it is refused, and no rename
        line is printed, because the header read is the new one."""
        text = pact(V2).replace(
            "# Pact\n\n",
            f"# Pact\n\n| Signatory |\n|---|\n| {MOBILE_URL} |\n\n## Before 0.19.0\n\n",
            1,
        )
        write(world.api, PACT, text)
        commit(world.api, "an old table above a new one")
        world.cite(clause(V2))
        code, out = world.run()
        assert code == 2, out
        assert (
            "REFUSED seal/pact.md — the pact also holds a `| Signatory |` header, the "
            "word before 0.19.0, and nothing under it is read while the `| Signer |` "
            "table stands — move its rows into that table and delete it"
        ) in out, out
        assert "heads its table" not in out, out

    @pytest.mark.parametrize(
        "line, message, said",
        [
            (
                f"\n| {MOBILE_URL} |\n",
                "a blank line inside the table",
                "the pact has a `Signer` table that ends above "
                f"`| {MOBILE_URL} |`, a row the walk never reaches — it and every "
                "signer below it would go unread",
            ),
            (
                f"<{MOBILE_URL}>\n",
                "a signer written as an autolink",
                "the pact has a `Signer` table that continues with "
                f"`<{MOBILE_URL}>`, a line with no pipe that GFM reads as one of "
                "its rows — write it as `| … |`",
            ),
        ],
        ids=["a row below a blank line", "a signer written as an autolink"],
    )
    def test_refuses_a_signer_the_walk_never_reads_and_prints_why(
        self, world, line, message, said
    ):
        """A signer written below a blank line, or as an autolink GFM reads as
        a row, is never passed over: `check` exits 2 and prints the walker's
        sentence after the pact's path."""
        text = pact(V2).replace(f"| {SIGNER_URL} |\n", f"| {SIGNER_URL} |\n" + line)
        write(world.api, PACT, text)
        commit(world.api, message)
        world.cite(clause(V2))
        code, out = world.run()
        assert code == 2, out
        assert "REFUSED seal/pact.md — " + said in out, out

    def test_an_entry_refusal_is_printed_after_the_pact(self, world):
        text = pact(V2).replace(f"| {SIGNER_URL} |\n", f"| {SIGNER_URL} |\n|  |\n")
        write(world.api, PACT, text)
        commit(world.api, "an empty row")
        world.cite(clause(V2))
        code, out = world.run()
        assert code == 2, out
        assert (
            "REFUSED seal/pact.md — the pact has a `Signer` entry that will not "
            "read: an empty row"
        ) in out, out


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
                assert refusals and "blank line above the header" in refusals[0], (
                    kind,
                    indent,
                    refusals,
                )


class Test_baseline_commit:
    def test_accepts_the_first_code_span_where_the_value_holds_two(self, config):
        row = "| Baseline commit | `0123456`, not `89abcde` |"
        text = f"| Field | Value |\n|---|---|\n{row}\n"
        assert config.baseline_commit(text) == ("0123456", None)

    def test_refuses_a_table_the_walk_stops_and_names_why_its_row_went_unread(
        self, config
    ):
        """The row is missing because the walk stopped above it, and the why
        says so beside the missing row: the walk's refusal is the only place
        the person learns which line to fix."""
        text = (
            "| Field | Value |\n|---|---|\n| Original | x |\n"
            "text\n| Baseline commit | `0123456` |\n"
        )
        _rows, refusals = config.gfm_table(text, config.PARITY_TABLE)
        sha, said = config.baseline_commit(text)
        assert sha is None and refusals, refusals
        assert "no `Baseline commit` row" in said, said
        assert all(r in said for r in refusals), said


class Test_renamed_header:
    def test_accepts_a_header_holding_signer_and_renames_that_cell_alone(self, config):
        old, said = config.renamed_header(("Signer", "Note"))
        assert old == ("Signatory", "Note")
        assert "`| Signatory | Note |`" in said, said

    def test_refuses_a_header_that_holds_no_signer(self, config):
        assert config.renamed_header(config.PARITY_TABLE) == (None, None)


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
        """`hooks/lib/config.py#policy_root`, the one reader every reader asks: an
        empty value and one that leaves the repository read as `docs`."""
        from conftest import load_hook_module

        config = load_hook_module("lib/config.py", "agentic_config_for_policy_root")
        (tmp_path / "config.md").write_text(
            f"| Item | Value |\n|---|---|\n| Policy root | {value} |\n",
            encoding="utf-8",
        )
        assert config.policy_root(str(tmp_path)) == root
        assert config.policy_root("") == "docs"

    def test_the_baseline_is_the_first_code_span_of_its_one_row(self):
        """The `Baseline commit` reader in `hooks/lib/config.py`: the SHA in the
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

    def test_a_hook_reader_copied_without_the_walk_names_it(self, tmp_path):
        """#667. This module imports `hooks/lib/blocks.py`, the walk the hook-path
        readers share. It is a module, not a script: gates and scripts import
        it, a gate that raises is skipped and said at the end of the turn
        (`hooks/dispatch.py`, #28), and a script catches the error or names the
        file first. So a copy without the walk raises one `ImportError` whose
        sentence names the path and what the file is for.
        `tests/hooks/test_routing.py` holds `hooks/lib/routing.py` to the same."""
        name, siblings = TARGET.rsplit("/", 1)[1], []
        alone = tmp_path / "hooks"
        alone.mkdir()
        for file in (name, *siblings):
            with open(os.path.join(ROOT, "hooks", "lib", file), encoding="utf-8") as f:
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
