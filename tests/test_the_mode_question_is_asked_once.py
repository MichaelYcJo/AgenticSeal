"""A root nobody chose a mode for is a state something names.

Issue #151, reported from a monorepo on its first work item under SpecSeal:
the session created `seal/` and started working. Nothing asked about shared or
local mode, and nothing asked the migration question.

Three files each said something correct and the three together left no route
to the question. `hooks/optin.py` says the root's existence IS the
declaration; `skills/implement/orchestration.md` *Orchestrator: Bootstrap* says the mode
question is asked there and nowhere else; and the preset block — `templates/claude-md-block.md`,
which `install.sh` copies into `~/.claude/CLAUDE.md`, so it loads in every project
on the machine — tells a session to write `seal/specs/<id>/routing.md` before the
first edit. That write creates `seal/`. Creating `seal/` opts the repository
in. The question lived in a skill the session had no reason to load.

This file pins the half that OBSERVES it. `tests/test_first_setup_asks_once.py`
pins the half that points at it — the preset sentence, and the bootstrap the
sentence sends a session to.

The scenario ids are `seal/specs/1788817289-local-mode-from-first-setup-to-
the-gate/spec.md`'s. Every case was written before `hooks/mode-gate.py` and
`hooks/config.py` existed and seen red — as a collection error, which is a
red this file's own first case makes explicit rather than leaving to a reader
to trust.
"""

import importlib.util
import os

import config_shapes
import pytest
from block_shapes import SHAPES
from conftest import (
    TABLE,
    load_hook_module,
    local_home,
    opt_in_shared,
    write_config,
    write_unreadable,
)

GATE = "mode-gate.py"


@pytest.fixture
def config():
    return load_hook_module("config.py", "specseal_config_for_tests")


# --- the reader: one parser for the Mode row -------------------------------


def test_the_row_is_read_from_the_root_the_folder_is_at(config, repo):
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
def test_the_four_spellings_of_undeclared_are_one_answer(config, repo, text, expected):
    """The same four `seal.py#declared` already had, because it is the same
    reader — moved, not rewritten. A row that names no mode is told apart from
    no row, because a claim nobody can act on is not the same as no claim."""
    home = opt_in_shared(repo)
    if text is not None:
        write_config(home, text)
    assert config.declared_mode(str(home)) == expected


# --- #867: a row written twice, and a file that will not read --------------


@pytest.mark.parametrize(
    "rows",
    [
        "| Mode | shared |\n| Mode | local |\n",
        "| Mode | local |\n| Mode | local |\n",
        "| Mode | shared |\n| Record language | Korean |\n| Mode |  |\n",
    ],
    ids=["two values", "the same value twice", "one value and an empty row"],
)
def test_a_mode_row_written_twice_has_no_value(config, repo, rows):
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


def test_an_absent_config_and_an_unreadable_one_are_two_states(config, repo):
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


def test_one_row_is_its_value_and_no_row_is_none(config):
    """The two answers beside the refusal, so a reader of `config_value` can
    tell an empty row from no row: `""` is a row somebody left empty, and
    None is no row at all."""
    text = TABLE.format(rows="| Mode | shared |\n| Broad gate |  |\n")
    assert config.config_value(text, "Mode") == ("shared", None)
    assert config.config_value(text, "Broad gate") == ("", None)
    assert config.config_value(text, "Ledger frozen from") == (None, None)
    assert config.config_value(None, "Mode") == (None, None)


def test_a_fenced_example_of_a_row_does_not_double_the_live_one(config):
    """The count is over the rows `config_rows` takes, so the example a
    person pastes from `templates/config.md` into a fence above the table
    (#429) is not a second row."""
    text = (
        "```markdown\n| Item | Value |\n|---|---|\n| Mode | local |\n```\n\n"
        + TABLE.format(rows="| Mode | shared |\n")
    )
    assert config.config_value(text, "Mode") == ("shared", None)


def test_rows_above_the_header_are_not_rows_of_this_table(config, repo):
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


def test_the_command_and_the_gate_read_one_parser(config):
    """`seal mode` writes the row and the gate reads it. Two readers of one
    table is how a file passes one and fails the other; `seal.py` re-exports
    this one rather than keeping a copy."""
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
    spec = importlib.util.spec_from_file_location("specseal_seal_one_parser", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # By where the code was COMPILED, not by object identity: this test loads
    # `hooks/config.py` under a name of its own, so the two module objects
    # differ while the implementation behind them must not.
    owner = os.path.join("hooks", "config.py")
    for name in ("declared", "config_rows", "config_path"):
        where = getattr(module, name).__code__.co_filename
        assert where.endswith(owner), f"seal.{name} is compiled from {where}"
    assert config.declared_mode.__code__.co_filename.endswith(owner)


# --- #415: a cell carries an escaped pipe, and the rows below it survive ----
#
# The scenario ids are `seal/specs/1789598366-a-piped-broad-gate-row-takes-
# every-config-row-below-it/spec.md`'s.
#
# **A row that parses comes FIRST in every fixture here.** The table walker
# stops at the first line it refuses, wherever it stands (#871), so a row
# read above the piped line is a value and every row below it is that
# refusal; a parseable row above it is what lets a fixture show both.

PIPED_TABLE = (
    "# Repository config\n\n"
    "| Item | Value |\n|---|---|\n"
    "| Record language | English |\n"
    "| Broad gate | bin/test -q \\| tee out.txt |\n"
    "| Mode | shared |\n"
    "| Commit and pull request language | English |\n"
)


def test_an_escaped_pipe_is_one_row_and_the_rows_below_it_still_arrive(config):
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


def test_a_windows_path_survives_the_reader_exactly_as_written(config):
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


def test_a_backslash_against_a_pipe_is_the_one_shape_the_escape_narrows(config):
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
    assert config.config_rows(header + "| Broad gate | C:\\Users\\x\\tools\\ |\n") == [
        ("Broad gate", "C:\\Users\\x\\tools\\")
    ], (
        "written with a space before the closing pipe the value comes back "
        "exactly as the old pattern read it, so no value lost a spelling"
    )
    assert config.config_rows(header + "| C:\\tools\\ | x |\n") == [
        ("C:\\tools\\", "x")
    ], "and the same for the item cell"


def test_a_three_column_row_is_refused_and_the_rows_above_it_arrive(config):
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


def test_seal_mode_writes_one_row_where_the_mode_row_sits_below_a_piped_row(
    config, tmp_path
):
    """A3, and `questions.md` M1 — **executed 2026-09-17, and it duplicated.**

    The reader and the writer read one table, so when the reader stopped
    above the `Mode` row the writer stopped there too: `declared_mode`
    answered *none*, `table_span` returned no `Mode` row, and `with_row`
    inserted a second one ABOVE the piped line while the person's own row sat
    below it. Measured on the tree before this change — two `| Mode |` rows in
    a person's file, which `table_span`'s own comment says no command can
    bring back into agreement. It is the worst outcome in this work item and
    the strongest argument for teaching the reader the escape.

    This calls `write_row`, which is the unit `seal mode` calls when the row
    reads as undeclared (`seal.py#mode`), rather than a helper beside it.

    **Nothing is asserted before the write.** What the reader answered is
    read into the failure message instead, because a guard that fires first
    takes the case's own subject — the file two rows deep — off the screen.
    """
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
    spec = importlib.util.spec_from_file_location("specseal_seal_for_415", path)
    seal = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(seal)

    home = tmp_path / "seal"
    home.mkdir()
    write_config(home, PIPED_TABLE)
    read_as = seal.declared(str(home))
    refused = seal.write_row(str(home), "shared")
    written = (home / "config.md").read_text(encoding="utf-8")
    assert written.count("| Mode |") == 1, (
        f"the person's file is {written.count('| Mode |')} `Mode` rows deep, "
        f"and no command brings it back into agreement. The reader answered "
        f"{read_as} for a file whose own row says `shared`:\n{written}"
    )
    assert refused == "", refused
    assert read_as == ("mode", "shared"), (
        "the writer stopped where the reader stopped, which is the agreement "
        "the two keep by reading one parser"
    )


BARE_TABLE = PIPED_TABLE.replace("\\|", "|")


def test_seal_mode_writes_nothing_under_a_bare_pipe_and_names_the_line(
    config, tmp_path
):
    """The inverse of round 1's 🟡 4 of #415, which #871 closes.

    Written bare, the line was no row, so the reader stopped above the
    person's `Mode` row, the writer stopped where the reader stopped, and the
    file came back two rows deep -- pinned as a limitation until now. The
    walker refuses the line instead: the `Mode` row under it is a refusal,
    never an absent row, so the writer has no row to add, and it writes
    nothing and names the line. Seen red against the stop rule's writer: the
    write returned `""` and the file held two `Mode` rows.
    """
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
    spec = importlib.util.spec_from_file_location("specseal_seal_for_415_bare", path)
    seal = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(seal)

    home = tmp_path / "seal"
    home.mkdir()
    write_config(home, BARE_TABLE)
    kind, _said = config.declared_mode(str(home))
    assert kind == "refused", kind
    said = seal.write_row(str(home), "shared")
    assert said.startswith(str(home / "config.md") + " has a `Item | Value` table"), (
        said
    )
    assert "stops at `| Broad gate | bin/test -q | tee out.txt |`" in said, said
    assert said.endswith("Nothing was written"), said
    assert (home / "config.md").read_text(encoding="utf-8") == BARE_TABLE


def test_a_line_that_will_not_parse_is_named_and_the_hook_still_says_nothing(
    config, repo
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


# --- #429: a table inside a code fence is not this repository's answer ------
#
# The scenario ids are `seal/specs/1789721571-the-gate-reads-an-example-and-
# names-rows-nobody-wrote/spec.md`'s. Three walks read this table and the
# fence rule is one rule in front of all three: `config_rows`'s walk and
# `refusal`'s walk here, and `seal.py#table_span`'s — the writer's — below.

# **Two cases build on this one, deliberately.**
# `test_the_writer_and_the_reader_agree_about_which_row_is_the_row` drives the
# writer over it, and `test_a_row_that_would_land_inside_an_unclosed_fence_is_
# refused` uses the same bytes as a canary: a refusal wide enough to swallow a
# file whose fence IS closed turns that case red. Changing these lines reaches
# both (#429, round 2's ⬜).
FENCED_ABOVE = (
    "# Repository config\n\n"
    "An example of the format, copied out of `templates/config.md`:\n\n"
    "```markdown\n"
    "| Item | Value |\n"
    "|---|---|\n"
    "| Mode | local |\n"
    "| Broad gate | EXAMPLE |\n"
    "```\n\n"
    "| Item | Value |\n"
    "|---|---|\n"
    "| Mode | shared |\n"
    "| Broad gate | bin/test -q |\n"
)

# The same shape with nothing parsed above the fence: the live table's only
# line will not parse, so both walks step past it and read on — and before
# the fence rule the example below supplied the rows.
FENCED_BELOW_A_TABLE_THAT_NEVER_BEGAN = (
    "| Item | Value |\n"
    "|---|---|\n"
    "| Broad gate | bin/test -q | tee out.txt |\n"
    "```markdown\n"
    "| Mode | local |\n"
    "| Broad gate | EXAMPLE |\n"
    "```\n"
)

# A fenced line that will not parse, standing ABOVE the first live row. Before
# the fence rule it was handed to `broad-gate` as a line to quote back at a
# person as their own malformed row; the walker refuses the live row below
# the fence instead, and never quotes the fenced one (#871).
FENCED_REFUSAL = (
    "| Item | Value |\n"
    "|---|---|\n"
    "```markdown\n"
    "| Broad gate | bin/test -q | tee out.txt |\n"
    "```\n"
    "| Mode | shared |\n"
)


def crlf(text):
    return text.replace("\n", "\r\n")


def test_a_fenced_table_above_the_live_one_is_not_the_table(config, tmp_path):
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
    assert "EXAMPLE" not in [value for _item, value in config.config_rows(FENCED_ABOVE)]
    home = tmp_path / "seal"
    home.mkdir()
    write_config(home, FENCED_ABOVE)
    assert config.declared_mode(str(home)) == ("mode", "shared"), (
        "the mode the gate reads is the example's, not the repository's"
    )


def test_a_fenced_example_below_a_table_that_never_began_is_still_not_the_table(
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


def test_a_fenced_pipe_line_is_not_a_line_somebody_wrote_as_a_row(config):
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


def test_the_writer_and_the_reader_agree_about_which_row_is_the_row(config, tmp_path):
    """A4. The WRITER locates the line `with_row` overwrites, and since #871
    it locates it by the reader's own walk, `config_table`. A writer reading
    the table any other way rewrites the `Mode` row inside somebody's pasted
    example while every gate reads the live one: a file two rows deep that
    no command can bring into agreement.

    Asserted on the BYTES, not on the reader's answer: what makes this case
    the writer's is that the fenced line comes back byte-identical and
    exactly one line of the file changed.
    """
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
    spec = importlib.util.spec_from_file_location("specseal_seal_for_429", path)
    seal = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(seal)

    before = FENCED_ABOVE.replace("| Mode | shared |", "| Mode | local |")
    home = tmp_path / "seal"
    home.mkdir()
    write_config(home, before)
    assert seal.write_row(str(home), "shared") == ""
    after = (home / "config.md").read_text(encoding="utf-8")

    assert "| Mode | local |\n| Broad gate | EXAMPLE |\n```" in after, (
        f"the writer rewrote the row inside the example block:\n{after}"
    )
    changed = [
        (i, was, now)
        # `strict=True`: a write that INSERTED a row leaves the two files
        # different lengths, and a silent truncation here would hide exactly
        # the outcome this case is about.
        for i, (was, now) in enumerate(
            zip(before.splitlines(), after.splitlines(), strict=True)
        )
        if was != now
    ]
    assert len(changed) == 1, f"the write touched {len(changed)} lines:\n{changed}"
    assert changed[0][2] == "| Mode | shared |", changed
    assert changed[0][0] > after.splitlines().index("```"), (
        "the line that changed is inside the fence, not in the live table"
    )

    # #871, S5: a table the walker refuses is one the writer refuses too,
    # in the shape a doubled `Mode` row takes -- `(None, the sentence)` --
    # and the file's bytes are left exactly as they were. Seen red against
    # the stop rule's writer, which inserted a second `Mode` row under the
    # last row above the bare pipe.
    refused_shape = config_shapes.SHAPES[7]
    assert seal.with_row(refused_shape, "local") == (
        None,
        config.config_table(refused_shape)[1][0],
    )
    shape_home = tmp_path / "shape-7" / "seal"
    shape_home.mkdir(parents=True)
    write_config(shape_home, refused_shape)
    said = seal.write_row(str(shape_home), "local")
    assert said.endswith("Nothing was written"), said
    assert (shape_home / "config.md").read_text(encoding="utf-8") == refused_shape


def test_the_writer_inserts_where_the_walk_says_the_table_ends(tmp_path):
    """#871, S5. The writer's insertion point is read off the walk's own
    line numbers: after the last row the walk read, or under the delimiter
    row where the table holds no row yet; and it overwrites the one line the
    walk read as the `Mode` row. Shape 12, whose header the stop rule's
    pattern did not match, is one of each: seen red against the stop rule's
    writer, which appended a second table to the end of the file."""
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
    spec = importlib.util.spec_from_file_location("specseal_seal_for_871", path)
    seal = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(seal)

    indented = config_shapes.SHAPES[12]
    assert seal.with_row(indented, "local") == (
        indented.replace("| Mode | shared |", "| Mode | local |"),
        "",
    )
    no_mode = indented.replace("| Mode | shared |", "| Record language | Korean |")
    assert seal.with_row(no_mode, "local") == (no_mode + "| Mode | local |\n", "")
    empty = "# c\n\n | Item | Value |\n|---|---|\n\nprose below.\n"
    assert seal.with_row(empty, "local") == (
        "# c\n\n | Item | Value |\n|---|---|\n| Mode | local |\n\nprose below.\n",
        "",
    )


def test_a_row_that_would_land_inside_an_unclosed_fence_is_refused(config, tmp_path):
    """Round 1's 🔴. The writer's claim is that the row reads back.

    A fence nobody closed runs to the end of the file, so `table_span` sees no
    table at all and `with_row` falls to its third arm and appends one at the
    END — which is inside that fence. `write_row` returned `""`, `seal mode`
    printed *one was written from where the folder is*, and `declared_mode`
    still answered `('none', '')`: the mode gate asks again next session, and
    the file grows by a table a run. Measured before the fix over both
    fixtures below, three runs each — 9 → 13 → 17 → 21 lines and 4 → 8 → 12 →
    16, `('none', '')` throughout.

    **A regression this branch introduced.** At `release/v0.12.1` the fenced
    table was visible to the writer, so the row it rewrote was read back.

    The third fixture is the shape A4 pins — a fence that IS closed above a
    live table — and it is here so that a refusal wide enough to swallow it
    turns this case red rather than passing quietly.
    """
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
    spec = importlib.util.spec_from_file_location("specseal_seal_unclosed", path)
    seal = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(seal)

    for name, before in (
        (
            "live_table_under_an_unclosed_fence",
            "# Repository config\n\nAn example of the format:\n\n```markdown\n"
            "| Item | Value |\n|---|---|\n| Mode | shared |\n",
        ),
        (
            "only_a_fenced_example_never_closed",
            "```markdown\n| Item | Value |\n|---|---|\n| Mode | shared |\n",
        ),
    ):
        home = tmp_path / name / "seal"
        home.mkdir(parents=True)
        write_config(home, before)
        failed = seal.write_row(str(home), "shared")
        assert "never closed" in failed, (
            f"{name}: the write reported success for a row no walk reads:\n{failed!r}"
        )
        assert (home / "config.md").read_text(encoding="utf-8") == before, (
            f"{name}: a refused write touched the person's file"
        )
        assert config.declared_mode(str(home)) == ("none", ""), (
            f"{name}: the reader's answer moved under a refused write"
        )

    closed = tmp_path / "closed" / "seal"
    closed.mkdir(parents=True)
    write_config(closed, FENCED_ABOVE.replace("| Mode | shared |", "| Mode | local |"))
    assert seal.write_row(str(closed), "shared") == "", (
        "the refusal reaches a file whose fence is closed and whose live "
        "table is right there"
    )
    assert config.declared_mode(str(closed)) == ("mode", "shared")


def test_a_file_whose_last_line_has_no_ending_gets_its_row_on_a_line(
    config, tmp_path, monkeypatch
):
    """Round 2's 🔴, both acts of it.

    `with_row`'s insert arm put the new row at the end of the file without
    terminating the line already there, so
    `| Record language | Korean || Mode | shared |` came back as one line of
    four cells and `config_rows` of it was `[]` — both rows gone. At
    `release/v0.12.1` that was written silently and cost the row the person
    already had; round 1's guard stopped the write and then blamed a fence the
    file does not have, which is the wrong-cause shape this work item is about
    arriving from its own repair.

    **The second half is the message, and it is pinned separately** because
    fixing the first half is what makes the guard unreachable for this shape.
    A residual cause is driven through the same unit with `with_row` replaced
    by one that changes nothing: the refusal must not name a fence in a file
    that has none.
    """
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
    spec = importlib.util.spec_from_file_location("specseal_seal_no_ending", path)
    seal = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(seal)

    no_ending = "| Item | Value |\n|---|---|\n| Record language | Korean |"
    home = tmp_path / "no_ending" / "seal"
    home.mkdir(parents=True)
    write_config(home, no_ending)
    assert seal.write_row(str(home), "shared") == "", (
        "the write is refused over a file with no fence in it at all"
    )
    written = (home / "config.md").read_text(encoding="utf-8")
    assert "Korean || Mode" not in written, (
        f"the new row was welded onto the line already there:\n{written!r}"
    )
    assert config.config_rows(written) == [
        ("Record language", "Korean"),
        ("Mode", "shared"),
    ], f"the person's own row did not survive the write:\n{written!r}"
    assert config.declared_mode(str(home)) == ("mode", "shared")

    stuck = tmp_path / "stuck" / "seal"
    stuck.mkdir(parents=True)
    write_config(stuck, no_ending)
    monkeypatch.setattr(seal, "with_row", lambda text, value: (text, ""))
    refused = seal.write_row(str(stuck), "shared")
    assert "would not read the `Mode` row back" in refused, refused
    assert "fence" not in refused, (
        f"the refusal names a fence in a file that has none:\n{refused}"
    )
    assert (stuck / "config.md").read_text(encoding="utf-8") == no_ending


def test_the_fence_rule_answers_the_same_for_a_crlf_file(config, tmp_path):
    """A7. The reader walks `splitlines()` while the writer splits with
    `splitlines(keepends=True)`, so the shared rule is the one place the two
    spellings have to meet. Round 3 of #415 measured CRLF for the existing
    walks; this is the same measurement for the answers this work item adds,
    and since #871 for the walker's refusal as well."""
    assert config.config_rows(crlf(FENCED_ABOVE)) == config.config_rows(FENCED_ABOVE)
    assert config.config_rows(crlf(FENCED_BELOW_A_TABLE_THAT_NEVER_BEGAN)) == []
    assert config.config_table(crlf(FENCED_REFUSAL)) == config.config_table(
        FENCED_REFUSAL
    )

    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
    spec = importlib.util.spec_from_file_location("specseal_seal_for_429_crlf", path)
    seal = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(seal)
    written, refused = seal.with_row(crlf(FENCED_ABOVE), "local")
    assert refused == "", refused
    assert "| Mode | local |\r\n| Broad gate | EXAMPLE |\r\n```" in written, (
        f"the writer rewrote the fenced row of a CRLF file:\n{written!r}"
    )
    assert written.count("\n") == written.count("\r\n"), (
        f"the write left a file in two endings:\n{written!r}"
    )


def test_what_counts_as_a_fence_is_commonmarks_rule_as_far_as_it_goes(config):
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


# --- #667: a row inside a comment that closes is not a row either ----------
#
# The shape ids are `seal/specs/1790645290-the-hooks-and-the-rider-check-read-
# fences-and-comments-by-one-rule/spec.md` *The shapes*, and the texts are
# `tests/block_shapes.py`'s -- most of them work item 1790635413's own strings,
# each a place an earlier reading of this file was wrong. "red at base" means
# the case fails with `hooks/config.py` from `3911a8cf`; "pins" means it passes
# there too and holds a reading that must not move.


def shape_text(name):
    return "\n".join(SHAPES[name]) + "\n"


COMMENTED_OLD_ROW = shape_text("C5")
COMMENTED_OLD_TABLE = shape_text("C6")
QUOTED_DELIMITERS = shape_text("C1")
LIVE = [("Mode", "shared"), ("Broad gate", "bin/test -q")]


# The walker's sentence for a live row written under a comment that sits
# inside the table: GFM ends the table at the comment, so the row below it is
# not one of the table's rows (#871).
UNDER_THE_COMMENT = "ends above `| Mode | shared |`, a row the walk never reaches"


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
def test_the_config_shapes_read_as_the_frame_expects(config, name, rows, stops):
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


def test_delimiters_quoted_in_code_spans_hide_nothing(config):
    """C1, named as 1790635413 named it (round 1, 🟡 3). A prose line quoting
    the opener in a code span above the table and one quoting the closer
    below it are paragraph text, so the table between them is read. Pins:
    the base read it, and the three rounds lost it by reading inline state."""
    assert config.config_rows(QUOTED_DELIMITERS) == LIVE


@pytest.mark.parametrize("name", ["LS", "PS", "NEL", "FF", "VT", "FS", "GS", "RS"])
def test_a_break_commonmark_does_not_honour_hides_no_config_row(config, name):
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
    assert [i for i, _line in config.unfenced(lines, text)] == list(range(len(lines)))
    assert config.config_rows(text) == []
    value, said = config.config_value(text, "Mode")
    assert value is None and said is not None, said


@pytest.mark.parametrize("name", ["LS", "PS", "NEL", "FF", "VT", "FS", "GS", "RS"])
def test_a_piece_inside_an_inline_comment_is_no_config_row(config, name):
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
    config, name, opener, closer
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


@pytest.mark.parametrize("name", ["LS", "FF"])
def test_the_writer_reads_where_commonmark_breaks(config, tmp_path, name):
    """#667 round 1, 🟡 1, the writer's walk: the writer never appends a
    second table under a `<!--` a renderer reads mid-line.

    Re-pinned by #871: the writer reads the table the reader reads, and the
    walker refuses this one (`test_a_break_commonmark_does_not_honour_hides_
    no_config_row` says why), so the writer refuses it too and the file's
    bytes are left exactly as they were -- no second table, and no row
    rewritten in a table the walk could not read whole."""
    from block_shapes import BREAKS, OPEN

    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
    spec = importlib.util.spec_from_file_location("specseal_seal_for_667_r1", path)
    seal = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(seal)

    before = (
        f"A note{BREAKS[name]}{OPEN}\n\n| Item | Value |\n|---|---|\n"
        "| Mode | local |\n-->\n"
    )
    home = tmp_path / "seal"
    home.mkdir()
    write_config(home, before)
    said = seal.write_row(str(home), "shared")
    assert said.endswith("Nothing was written"), said
    after = (home / "config.md").read_text(encoding="utf-8")
    assert after == before, after


def test_a_commented_row_is_not_a_row_in_either_line_ending(config):
    """S5, C5 to C7, named as 1790635413 named them. The rows parked in a
    comment are gone from every walk. Since #871 the live rows under a
    comment that sits inside the table do not arrive either: GFM ends the
    table at the comment, so the walk refuses them, naming the first, and an
    item among them is a refusal and never an absent row. Under a whole old
    table parked above the live one, the live table arrives."""
    for text in (COMMENTED_OLD_ROW, COMMENTED_OLD_TABLE, crlf(COMMENTED_OLD_ROW)):
        assert all(
            "old -q" not in line for _index, line in config.unfenced(text.splitlines())
        ), text
    assert config.config_rows(COMMENTED_OLD_TABLE) == LIVE
    for text in (COMMENTED_OLD_ROW, crlf(COMMENTED_OLD_ROW)):
        assert config.config_rows(text) == [], text
        value, said = config.config_value(text, "Broad gate")
        assert value is None and UNDER_THE_COMMENT in said, said


def test_a_fence_line_inside_a_closed_comment_names_no_unclosed_fence(config, tmp_path):
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
        os.path.dirname(__file__), "..", "skills", "verify", "scripts", "broad_gate.py"
    )
    spec = importlib.util.spec_from_file_location("specseal_gate_for_667", path)
    gate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gate)
    assert gate.fence_left_open(str(home)) is False


def test_a_fence_nobody_closed_is_still_named(config):
    """C14, pinned from the other side: the fence that hides the live table
    is the one `fence_map` reports, so `broad-gate` still says *close that
    fence*."""
    assert config.fence_map(SHAPES["C14"])[1] == 0


def test_the_fence_named_is_the_one_that_hides_the_row(config):
    """C2 with a fence left open below the table. The old reading runs the
    fence quoted in the comment to the end, so it would name THAT line, which
    opens nothing; the walk sees the tilde fence below the table never close,
    and the line under it is hidden because of it. That is the fence
    `broad-gate` has to tell the person to close."""
    lines = [*SHAPES["C2"], "", "~~~", "| Broad gate | bin/test -q |"]
    assert config.fence_map(lines)[1] == lines.index("~~~")
    assert config.config_rows("\n".join(lines)) == [("Mode", "shared")]


def test_a_mid_line_comment_hides_no_row_the_base_reads(config):
    """C13, the residual `spec.md` *Scope* names. A renderer hides the first
    pipe-line behind a lone backtick and a mid-line `<!--`, and knowing that
    needs code spans and the paragraph's extent, which is where all three of
    1790635413's rounds lost ground. The base reads it, so reading it is not
    worse; this pins that nothing here pretends to more."""
    lines = SHAPES["C13"]
    assert [index for index, _line in config.unfenced(lines)] == list(range(len(lines)))


def test_the_writer_leaves_a_commented_row_alone(config, tmp_path):
    """S6, C10. The writer's walk located the FIRST `Mode` line -- the
    commented one -- so `seal mode` rewrote a row nobody reads while the live
    row kept its old value. Asserted on the bytes. Red at base.

    Re-pinned by #871: the comment sits directly under the delimiter row, so
    GFM ends the table there and the live `Mode` row below it is a row the
    walk never reaches. The reader refuses it, and the writer refuses with
    it: neither the commented row nor the live one is rewritten."""
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
    spec = importlib.util.spec_from_file_location("specseal_seal_for_667", path)
    seal = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(seal)

    before = shape_text("C10")
    home = tmp_path / "seal"
    home.mkdir()
    write_config(home, before)
    said = seal.write_row(str(home), "shared")
    assert UNDER_THE_COMMENT.replace("shared", "local") in said, said
    after = (home / "config.md").read_text(encoding="utf-8")
    assert after == before, (
        f"the writer rewrote the commented row, or the live one:\n{after}"
    )
    assert config.declared_mode(str(home))[0] == "refused"


# --- #871: the config table is read by the walker cmark-gfm holds ----------
#
# The scenario ids are `seal/specs/1791852616-the-config-table-has-its-own-
# grammar-beside-the-gfm-walker/spec.md`'s, and the shape numbers are its
# *Data & interfaces* table's; the texts are `tests/config_shapes.py`'s.


@pytest.mark.parametrize("number", sorted(config_shapes.SHAPES))
def test_every_config_reader_is_one_walk_over_the_sixteen_shapes(config, number):
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
        config.table_cells(lines[index]) == (item, value) for index, item, value in rows
    ), rows
    stops = config_shapes.STOPS[number]
    if stops is None:
        assert refusals == [], refusals
    else:
        assert len(refusals) == 1 and stops in refusals[0], refusals


def test_a_refusal_is_per_item_and_never_an_absent_row(config, repo):
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


@pytest.mark.parametrize("name", ["LS", "PS", "NEL", "FF", "VT", "FS", "GS", "RS"])
def test_a_row_after_a_break_gfm_does_not_honour_is_no_row_of_its_own(config, name):
    """#871 round 1, 🟡 4. A row followed on its own line by a character only
    `str.splitlines` ends a line at, then a second row, is ONE row to
    cmark-gfm, cut off at its cells: GitHub shows `Mode shared` and no
    `Broad gate`. The walk reads the first row and refuses the piece after
    the break, so no gate is handed a command GitHub does not show. Seen red
    against the walk before the guard: `Broad gate` was read as `x`."""
    from block_shapes import BREAKS

    text = TABLE.format(rows=f"| Mode | shared |{BREAKS[name]}| Broad gate | x |\n")
    assert config.config_rows(text) == [("Mode", "shared")], config.config_rows(text)
    value, said = config.config_value(text, "Broad gate")
    assert value is None and "put it on a line of its own" in (said or ""), said


def test_an_item_written_again_below_the_stopping_line_has_no_value(config):
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


@pytest.mark.parametrize("name", ["LS", "PS", "NEL", "FF", "VT", "FS", "GS", "RS"])
@pytest.mark.parametrize("where", ["above the header", "under the header"])
def test_a_header_after_a_break_gfm_does_not_honour_is_no_table(config, name, where):
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


def test_an_item_named_under_the_next_heading_is_another_tables(config):
    """#871 round 2, yellow 10. A table under the next heading is not below
    the line the walk stopped at, so a `Mode` cell in it does not double the
    config's `Mode` row. Seen red against 4dfb3d0d: "appears 2 times"."""
    text = TABLE.format(
        rows="| Mode | shared |\n| a | b | c |\n\n## Notes\n\n"
        "| Mode | what it means |\n|---|---|\n| local | x |\n"
    )
    assert config.config_value(text, "Mode") == ("shared", None)


@pytest.mark.parametrize("name", ["LS", "FF"])
def test_a_line_below_the_stop_is_a_line_where_gfm_begins_one(config, name):
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


def test_a_refused_append_names_the_walkers_cause_not_a_defect(config, tmp_path):
    """#871 round 1, 🟡 2. A file with no table and an HTML comment that
    never closes: `with_row` appends a table, the walker refuses the
    appended header as inside that block, and `write_row` says so — the
    walker's sentence — rather than calling it a defect in the command. Seen
    red against the generic read-back sentence."""
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    path = os.path.join(root, "skills", "implement", "scripts", "seal.py")
    spec = importlib.util.spec_from_file_location("specseal_seal_for_871_r1", path)
    seal = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(seal)
    from block_shapes import OPEN

    before = f"# Repository config\n\n{OPEN} a note nobody closed\n"
    home = tmp_path / "seal"
    home.mkdir()
    write_config(home, before)
    said = seal.write_row(str(home), "shared")
    assert "inside an HTML block opened above it and never closed" in said, said
    assert "defect in this command" not in said, said
    assert (home / "config.md").read_text(encoding="utf-8") == before
