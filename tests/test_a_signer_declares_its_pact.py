"""A signer declares its pact (#647, step A).

Some work items commit in more than one repository, and those repositories
keep one contract together. The one copy of it is the PACT, `seal/pact.md` in
the repository that holds it, and every repository of such a work item is a
SIGNER. A signer other than the pact's repository names the pact in its
own `seal/config.md`:

    | Pact | git@example.com:org/orders-api.git |

The row has one reader, `hooks/config.py#pact_declaration`, which both
`chain_check.py` (prints) and `pact_check.py` (refuses) ask. The cases below
are that reader's (S1-S3 of the work item's `spec.md`), and the routing
step's pinned sentences (S4).
"""

import os

import pytest
from conftest import load_hook_module

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

config = load_hook_module("config.py", "config_for_the_pact")

URL = "git@example.com:org/orders-api.git"
ORDERS = [(URL, "example.com/org/orders-api", "orders-api")]
CONFIG_TOP = "# config\n\n| Item | Value |\n|---|---|\n| Mode | shared |\n"
CONFIG = CONFIG_TOP + f"| Pact | {URL} |\n"


def table(*rows):
    return "# config\n\n| Item | Value |\n|---|---|\n" + "".join(
        f"| {item} | {value} |\n" for item, value in rows
    )


def flat(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as handle:
        return " ".join(handle.read().split())


def walked(text):
    """The walker's refusals of TEXT's `| Item | Value |` table, which
    `pact_declaration` appends after its own since #871. The sentences
    themselves are pinned by `tests/test_the_mode_question_is_asked_once.py`'s
    S1 and by the oracle; here what is pinned is that they arrive, last."""
    return config.config_table(text)[1]


# --- S1-S3: the row and its reader ------------------------------------------


def test_one_pact_reads_normalised():
    """S1. One URL: the URL normalised, and its name."""
    pacts, refusals = config.pact_declaration(
        table(("Mode", "shared"), ("Pact", "git@example.com:org/Orders-API.git"))
    )
    assert refusals == []
    assert pacts == [
        (
            "git@example.com:org/Orders-API.git",
            "example.com/org/orders-api",
            "orders-api",
        )
    ]


def test_two_pacts_come_back_in_order():
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
    assert [name for _, _, name in pacts] == ["orders-api", "billing"]


def test_no_row_and_an_empty_row_hold_no_pact():
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
def test_a_pact_notify_row_an_earlier_release_read_is_ignored(rows):
    """`templates/config.md` *Pact*: a `Pact notify` row left in the table
    is read by nobody, with a `Pact` row or without one, so neither a value
    outside the vocabulary the row once had nor the row written twice is
    refused. Seen red by `mutation-check` against a reader that refused the
    row (phase 8 of 1791940762)."""
    assert config.pact_declaration(table(("Pact", URL), *rows)) == (ORDERS, [])
    assert config.pact_declaration(table(*rows)) == ([], [])


def test_a_row_that_will_not_parse_is_refused_and_never_read_as_absent():
    """Each way an entry fails is a sentence naming it, so a signer that
    wrote a row is never read as one that wrote none."""
    cases = {
        "orders-api": "is not a remote URL",
        "git@example.com:org/a.git;;git@example.com:org/b.git": "holds an empty entry",
        "git@example.com:org/a.git git@example.com:org/b.git": "holds a space",
        "https://example.com/org/a+b": "which a pact anchor cannot name",
        "git@example.com:org/api.git;https://example.com/other/api": "both end in `api`",
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
            ("Pact", "git@example.com:org/a.git"), ("Pact", "git@example.com:org/b.git")
        )
    )
    assert pacts == []
    assert refusals == ["`Pact` appears 2 times — one value"]


def test_an_unreadable_config_is_no_declaration(tmp_path):
    """`declared_pacts` is what `pact-check` reads a signer's row
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
    assert [n for _, _, n in pacts] == ["orders-api"] and refusals == []


def test_seal_keeps_one_normaliser():
    """`seal.py` re-exports the reader's normaliser rather than keeping a
    second copy that could drift from the one the `Pact` row goes through."""
    seal = load_hook_module(
        os.path.join("..", "skills", "implement", "scripts", "seal.py"),
        "seal_for_the_pact",
    )
    assert seal.normalise_remote is seal.repo_config.normalise_remote


# --- the table the row is read from (#871) ----------------------------------


@pytest.mark.parametrize(
    "text",
    [
        f"| Item | Value |\n|---|---|\n | Pact | {URL} |\n| Mode | shared |\n",
        CONFIG_TOP + f"  | Pact | {URL} |\n",
    ],
    ids=["between the header and the first row", "indented"],
)
def test_an_indented_pact_row_is_read_as_cmark_gfm_renders_it(text):
    """#871. A row indented one to three spaces is one of the table's rows
    to cmark-gfm, and the walker reads it: the row is read, and nothing is
    refused. Seen red against the stop rule, whose row pattern began at the
    margin."""
    assert config.pact_declaration(text) == (ORDERS, [])


BARE_PIPE = (
    "has a `Item | Value` table that stops at "
    "`| Broad gate | bin/test -q | tee out |`, which is not a 2-cell row "
    "written `| … | … |` — every row below it would go unread"
)


def test_a_signer_config_the_walker_refuses_is_refused_after_the_pact():
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
    # last too: seen red by `mutation-check` dropping it on that arm alone.
    doubled = CONFIG + "| Pact | git@example.com:org/b.git |\n" + bad
    assert config.pact_declaration(doubled) == (
        [],
        ["`Pact` appears 2 times — one value", BARE_PIPE],
    )


def _broad_gate_block():
    """The prose `skills/config/SKILL.md` step 3 tells a session to copy
    below the live table: `templates/config.md` from `## Broad gate` down to
    `### What is refused, and what stays allowed`."""
    with open(os.path.join(ROOT, "templates", "config.md"), encoding="utf-8") as f:
        text = f.read()
    start = text.index("## Broad gate\n")
    return text[start : text.index("### What is refused, and what stays allowed")]


def test_s4_the_configs_this_plugin_writes_or_copies_are_silent():
    """S4. This repository's own `seal/config.md`, the stub `seal mode`
    writes, that stub with the copied `## Broad gate` block below it -- with
    and without the `Pact` row `orchestration.md` writes into the table --
    and `templates/config.md` copied whole, which
    `skills/commit-pr-convention/SKILL.md` tells a session to do, give no
    refusal to the reader `pact-check` reads strictly. Each is read from the
    tree, not retyped."""
    seal = load_hook_module(
        os.path.join("..", "skills", "implement", "scripts", "seal.py"),
        "seal_for_the_silent_set",
    )
    with open(os.path.join(ROOT, "seal", "config.md"), encoding="utf-8") as f:
        assert config.pact_declaration(f.read()) == ([], [])
    stub = seal.NEW_CONFIG.format(item="Mode", value="shared")
    block = _broad_gate_block()
    assert "Broad gate" in block
    assert config.pact_declaration(stub) == ([], [])
    assert config.pact_declaration(stub + "\n" + block) == ([], [])
    signed = stub + f"| Pact | {URL} |\n"
    assert config.pact_declaration(signed + "\n" + block) == (ORDERS, [])
    with open(os.path.join(ROOT, "templates", "config.md"), encoding="utf-8") as f:
        template = f.read()
    assert config.pact_declaration(template) == ([], [])
    filled = template.replace("| Pact |  |\n", f"| Pact | {URL} |\n", 1)
    assert filled != template
    assert config.pact_declaration(filled) == (ORDERS, [])


# --- the shipped rows -------------------------------------------------------


def test_the_template_and_the_config_skill_carry_the_pact_row_alone():
    """`templates/config.md` documents the `Pact` row and `/specseal:config`
    shows it; neither carries a `Pact notify` row, and the template says
    once what one left in a config does."""
    template = flat("templates", "config.md")
    skill = flat("skills", "config", "SKILL.md")
    assert f"**`{config.PACT_ROW}`**" in template
    assert f"| `{config.PACT_ROW}` |" in skill
    assert "| Pact notify |" not in template
    assert "| `Pact notify` |" not in skill
    assert (
        "**A `Pact notify` row is read by nobody.** No command refuses it, "
        "prints it or names it, like any item no reader asks for, and whoever "
        "next edits the file deletes it."
    ) in template
    assert template.count("Pact notify") == 1, "the template says it once"


# --- S4: the routing step across repositories -------------------------------

ORCHESTRATION = ("skills", "implement", "orchestration.md")


def test_the_routing_step_mints_one_id_and_declares_only_in_gated_repositories():
    """S4. The question is asked once, the id is minted once, and a
    repository with no root is named and left alone, because writing into it
    would opt it in."""
    text = flat(*ORCHESTRATION)
    start = text.index("### A work item that commits in more than one repository")
    section = text[start : text.index(" ## ", start)]
    for sentence in (
        "**One id, minted once, names the directory in every repository.** "
        "Take `date +%s` once, pick one slug, and use the resulting directory "
        "name in every repository.",
        "**Only a gated repository gets a declaration.**",
        "A repository with no root is not opted in by this step",
        "Name such a repository in the handback and write nothing into it.",
        "each in a command of its own, and commit each with that repository's "
        "absolute path written out after `git -C`",
        "A sentence is contract when another repository's code would be wrong "
        "if it changed.",
        "The pact's repository needs no row",
    ):
        assert sentence in section, sentence


# --- the pact's own table ---------------------------------------------------

PACT = (
    "# Pact\n\n<!-- | Signer |\n|---|\n| git@example.com:org/quoted.git | -->\n\n"
    "| Signer |\n|---|\n"
    "| git@example.com:org/orders-web.git |\n"
    "| https://example.com/other/orders-web |\n\n"
    "## Order response shape\n\nx\n"
)


def test_the_pact_lists_its_signers_and_a_comment_is_not_the_table():
    """Two signers may end in one segment, because nobody cites a
    signer by name; a table in a comment block is not the table."""
    signers, refusals, header = config.pact_signers(PACT)
    assert refusals == [] and header == ("Signer",)
    assert [n for _, n, _ in signers] == [
        "example.com/org/orders-web",
        "example.com/other/orders-web",
    ]


def test_a_pact_with_no_table_or_an_unfilled_one_is_refused():
    """A pact nobody signs is not a pact, and the template's placeholder row
    is refused rather than read as a signer. A pact holding neither header
    is refused naming the new one (S3 of #822)."""
    assert config.pact_signers("# Pact\n\n## A\n") == (
        [],
        ["holds no `| Signer |` table, so it names no signer"],
        None,
    )
    with open(os.path.join(ROOT, "templates", "pact.md"), encoding="utf-8") as h:
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


# --- the header 0.18.x wrote (#822) -------------------------------------------
#
# Spelled out here rather than read from `hooks/config.py#renamed_header`: a
# case taking the old header from the reader's own constant would pass with
# that constant changed, and the pacts written in 0.18.x would not.

OLD = PACT.replace("| Signer |\n|---|\n|", "| Signatory |\n|---|\n|")


def test_s2_a_pact_headed_as_0_18_wrote_it_is_read_the_same():
    """The old header reads to the same signers, and the reader says which
    header it read, so a caller can name the rename without reading the text
    again; the comment block's quoted table is still not the table."""
    assert "| Signatory |\n|---|\n| git@example.com:org/orders-web" in OLD
    signers, refusals, header = config.pact_signers(OLD)
    assert (signers, refusals) == config.pact_signers(PACT)[:2]
    assert header == ("Signatory",)
    assert config.renamed_header(config.SIGNER_HEADER)[0] == header


def test_s2_every_refusal_under_the_old_header_names_it():
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


BOTH = (
    "also holds a `| Signatory |` header, the word before 0.19.0, and nothing "
    "under it is read while the `| Signer |` table stands — move its rows into "
    "that table and delete it"
)


def test_s4_a_pact_holding_both_tables_reads_signer_and_refuses_the_old_one():
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
        assert [s[2] for s in signers] == ["orders-web"], (text, signers)
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
    assert len(refusals) == 1 and "ends above `|Signatory|`" in refusals[0], refusals
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
        assert [s[2] for s in signers] == ["orders-web"], signers
        assert sum("Signatory" in r for r in refusals) == 1, refusals
        quoted = under.split("\n", 1)[0].strip()
        assert glued.replace("`| Signatory |`", f"`{quoted}`") in refusals, refusals
    # Rows under a glued old header with no delimiter row are rows of the
    # `Signer` table to GFM, and they are read as signers; the refusal says
    # so rather than "nothing under it is read" (post-review check of #830).
    signers, refusals, _ = config.pact_signers(
        signer + "| Signatory |\n| https://example.com/org/billing |\n"
    )
    assert [s[2] for s in signers] == ["orders-web", "billing"], signers
    assert refusals == [glued], refusals
    # A glued old header above a second old table after a blank line: the
    # walk's stray-row refusal names the second, and the glued line is not
    # also refused as an entry (post-review check 2 of #830; #831).
    signers, refusals, _ = config.pact_signers(
        signer
        + "| Signatory |\n\n| Signatory |\n|---|\n| https://example.com/org/billing |\n"
    )
    assert [s[2] for s in signers] == ["orders-web"], signers
    assert refusals == [
        "has a `Signer` table that ends above `| Signatory |`, a row the walk "
        "never reaches — it and every signer below it would go unread"
    ], refusals


def test_s4_a_broken_signer_table_does_not_fall_back_to_the_old_one():
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
def test_a_signer_row_the_walk_cannot_read_is_refused(row):
    """A table line the walk cannot read ends it, and the signers below
    it would go unread; the line is refused rather than passed in silence."""
    text = (
        "# Pact\n\n| Signer |\n|---|\n| https://example.com/org/orders-web |\n"
        + row
        + "\n\n## A\n\nx\n"
    )
    signers, refusals, _ = config.pact_signers(text)
    assert [s[2] for s in signers] == ["orders-web"]
    assert refusals == [
        f"has a `Signer` table that stops at `{row}`, which is not a one-cell "
        "row written `| … |` — every signer below it would go unread"
    ], refusals


# --- every way GFM ends or breaks the `Signer` table (round 2 of #647) ---
#
# A table is a header row, a delimiter row of the same width, then body rows,
# and it is broken by a blank line or by the start of another block. Each way
# is either read as GFM reads it, or refused; none drops a signer while the
# table reads as complete. These cases pin the SENTENCES the pact prints. That
# the walk reads what GFM renders is not held here but by
# `tests/test_one_table_walker_reads_what_gfm_renders.py`, over a corpus
# enumerated from the block kinds and judged by cmark-gfm itself: a list like
# this one, written by the walk's own author, is what round 3 of #735 found
# short by an autolink.

WEB = "https://example.com/org/orders-web"
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


@pytest.mark.parametrize(
    "text, said", [c[1:] for c in TABLE_ENDS], ids=[c[0] for c in TABLE_ENDS]
)
def test_every_way_the_table_ends_is_read_or_refused(text, said):
    signers, refusals, _ = config.pact_signers(text)
    if said is None:
        assert refusals == [], refusals
        assert [s[1] for s in signers] == ["example.com/org/orders-web"]
    else:
        assert any(said in r for r in refusals), refusals


ENTRY = "has a `Signer` entry that will not read: "


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
def test_every_entry_refusal_reads_after_the_pact(row, sentence):
    """Both callers print a table refusal after "the pact "; each sentence
    an entry can raise is pinned whole (round 2 of #647, white 14)."""
    text = HEAD + row + "\n" + CLAUSE
    _, refusals, _ = config.pact_signers(text)
    assert refusals == [sentence], refusals
    assert ("the pact " + sentence).count("the pact the") == 0
