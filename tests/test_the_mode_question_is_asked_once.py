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

The gate's cases are in `tests/test_mode_gate.py`, and the reader's, the
cases of `hooks/config.py`, in `tests/test_config.py`, since #942's phase 6.
What stays here is the writer's: `skills/implement/scripts/seal.py`'s
`write_row` and `with_row`, held to the reader they share a table with, and
`seal.py`'s re-export of that reader, for the group that places `seal.py`'s
light files. `tests/test_first_setup_asks_once.py` pins the half that points
at the question — the preset sentence, and the bootstrap the sentence sends a
session to.
"""

import importlib.util
import os

import config_shapes
import pytest
from conftest import (
    FENCED_ABOVE,
    FENCED_BELOW_A_TABLE_THAT_NEVER_BEGAN,
    FENCED_REFUSAL,
    PIPED_TABLE,
    UNDER_THE_COMMENT,
    crlf,
    shape_text,
    write_config,
)

# --- the reader: one parser for the Mode row -------------------------------


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
# every-config-row-below-it/spec.md`'s. `PIPED_TABLE`, in `tests/conftest.py`,
# puts a row that parses first, because the table walker stops at the first
# line it refuses (#871).


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


# --- #429: a table inside a code fence is not this repository's answer ------
#
# The scenario ids are `seal/specs/1789721571-the-gate-reads-an-example-and-
# names-rows-nobody-wrote/spec.md`'s. Three walks read this table and the
# fence rule is one rule in front of all three: `config_rows`'s walk and
# `refusal`'s walk, whose cases are in `tests/test_config.py`, and
# `seal.py#table_span`'s — the writer's — below. The fixtures are
# `tests/conftest.py`'s.


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


# --- #667: a row inside a comment that closes is not a row either ----------
#
# The shape ids are `seal/specs/1790645290-the-hooks-and-the-rider-check-read-
# fences-and-comments-by-one-rule/spec.md` *The shapes*, and the texts are
# `tests/block_shapes.py`'s, read through `tests/conftest.py#shape_text`.
# "red at base" means the case fails with `hooks/config.py` from `3911a8cf`.


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
