"""A project's own `specs/` is read as history and never taken (#688).

A person joining a project that kept its own `specs/` before the plugin
arrived used to have it read as the plugin's: moved into `seal/` at session
start, and searched as a record by the checks. The plugin writes only to its
own root. Every other directory named `specs` is a REFERENCE ROOT — read when
a change touches what it describes, cited where it was read, and never moved,
edited, absorbed or deleted.

`seal/config.json`'s `Reference specs` key names the reference roots, and with
no key every directory named `specs` outside the plugin's root is one. The key
has one reader, `lib/config.py#reference_roots`, and one predicate,
`lib/config.py#under_reference_root`; every check that would read a
reference root as a record asks that predicate instead of spelling its own
test. The resolver's cases (C1) are in `tests/lib/test_config.py`, since #942's
phase 6; the checks' cases sit beside each check's own (D1, D2, D3), and
this file names every shipped check and what keeps it off a reference root.
"""

import os

from conftest import ROOT, load_module

# No TARGET: its cases list every command under bin/ and seal.py's subcommands, and hold one citation across the files that read a reference root.

SEAL = load_module(
    os.path.join(ROOT, "skills", "implement", "scripts", "seal.py"),
    "seal_for_the_reference_root",
)


# --- D3: every shipped check, and what keeps it off a reference root ---------
#
# The failure this file's plan names for six months out: a check added later
# walks the tree without asking the predicate, and the class reopens one
# script at a time. So every command `bin/` ships, and every subcommand
# `seal.py#TOOLS` hands to a script, is named here with what
# keeps it off a team's `specs/`, and a command nobody classified turns this
# red. A check that walks no `specs/` says so; one pinned to the root names
# what it rests on, which its module's file holds under the root's own
# directory: `settle.py#threads` in `tests/skills/test_settle.py`'s
# `Test_threads`, a case of one module, which #942's round 9 fix pass moved
# there from this file as a constant and #1059 made the root's own name. The checks that
# walk work items are held off a team's `specs/` in their modules' files:
# `tests/skills/test_unverified_check.py`'s walk from the root over a team's
# unreadable overview, `tests/skills/test_settle.py`'s apply beside a team directory
# of the removed work item's id, and `tests/skills/test_chain_check.py`'s
# `Test_changed_routing`, which takes a declaration only under the directory
# of the work items it is given, and `Test_declared_for_this_branch`, which
# takes the one under `seal/threads/` beside a team's `specs/`.

PREDICATE = "asks lib/config.py#under_reference_root"
PINNED = "reads the plugin's root under its own directory"
NO_WALK = "walks no specs/ directory"
NOT_A_CHECK = "is not a check of the tree"

SHIPPED = {
    "seal unverified": (PREDICATE, "the walk, by one rule"),
    "seal settle": (
        PINNED,
        "settle.py#threads; its citation scan reads as a citer, and --from reads "
        "only a directory a person names and writes nothing there",
    ),
    "seal pact": (PINNED, "pact_check.py#anchor_files, under each signer's root"),
    "seal gate": (NO_WALK, "runs the command, chain_check.py and seal.py mode"),
    "seal fold": (
        NO_WALK,
        "reads the policy root, each group its index names, and seal/config.json",
    ),
    "seal rules": (NO_WALK, "reads the one document it is named and its targets"),
    "seal mutate": (NO_WALK, "breaks and restores the one file it is named"),
    "seal layout": (NO_WALK, "reads tests/ and the modules its files name"),
    "seal deferrals": (NO_WALK, "reads the pull request body and round records"),
    "seal pr-body": (NO_WALK, "reads the one work item it is named and a body file"),
    "seal": (NOT_A_CHECK, "the mode command, writing seal/config.json"),
    "seal stamp": (NOT_A_CHECK, "draws the sealer's stamp from a sealed guarantee"),
    "seal cost": (NOT_A_CHECK, "measures a transcript"),
    "seal payload": (NOT_A_CHECK, "measures a spawn's payload"),
    "test": (NOT_A_CHECK, "this repository's own suite runner"),
}


def test_every_shipped_command_is_classified():
    shipped = {
        name
        for name in os.listdir(os.path.join(ROOT, "bin"))
        if not name.endswith(".cmd")
    } | {f"seal {name}" for name in SEAL.TOOLS}
    assert shipped == set(SHIPPED), (
        "a command in bin/ or a `seal` subcommand is not classified here, or "
        "a classified one left: "
        f"{sorted(shipped ^ set(SHIPPED))}. Say what keeps it off a team's "
        "specs/ — the predicate, the root's own directory, or no walk at all"
    )


# --- C2: the readers read a reference root when relevant, and cite it --------
#
# Each party that reads the tree for a decision is told, in a file it opens at
# that step, that a reference root is history: read where the work touches
# what it describes, cited where it was read, and never written. Each names
# the row by pointing at `templates/setup/config.md` *Reference specs* rather
# than restating its grammar, so the grammar has one home. The framer and the
# crafter are told by `skills/implement/SKILL.md` *Document layout — two
# roots, three lifetimes*, which the crafter's step 1 and the framer's *A
# design states its rule changes* open (#1313). How each paragraph says it
# is the proofer's to read; the case below reads the citation and the facts
# a reader acts on in the paragraph that holds it.

# The citation each reader resolves for the row's grammar: the path and the
# heading in italics.
POINTER = "`templates/setup/config.md` *Reference specs*"
READERS = {
    # The stage `stage 1`, which the proofer resolves to the stage of the
    # review skill it opens the citation in, and the path `frame/design.md`,
    # which holds the citation it opens.
    "agents/proofer.md": ("stage 1", "frame/design.md"),
    # The path `frame/design.md`, where the party cites a reference root it
    # read.
    "skills/settle/SKILL.md": ("frame/design.md",),
    "skills/implement/SKILL.md": ("frame/design.md",),
}


def paragraph_naming(text, phrase):
    """The blank-line-bounded block that holds `phrase`, its breaks folded."""
    at = text.index(phrase)
    start = text.rfind("\n\n", 0, at) + 2
    end = text.find("\n\n", at)
    return " ".join(text[start : end if end >= 0 else None].split())


def test_each_reader_points_at_the_row_and_names_where_it_cites_it():
    for rel, facts in READERS.items():
        text = open(os.path.join(ROOT, rel), encoding="utf-8").read()
        assert POINTER in text, f"{rel} does not point at the row's section"
        said = paragraph_naming(text, POINTER)
        for fact in facts:
            assert fact in said, (rel, said)
