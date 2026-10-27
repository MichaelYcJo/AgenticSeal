"""A project's own `specs/` is read as history and never taken (#688).

A person joining a project that kept its own `specs/` before the plugin
arrived used to have it read as the plugin's: moved into `seal/` at session
start, and searched as a record by the checks. The plugin writes only to its
own root. Every other directory named `specs` is a REFERENCE ROOT — read when
a change touches what it describes, cited where it was read, and never moved,
edited, absorbed or deleted.

`seal/config.md`'s `Reference specs` row names the reference roots, and with
no row every directory named `specs` outside the plugin's root is one. The row
has one reader, `hooks/config.py#reference_roots`, and one predicate,
`hooks/config.py#under_reference_root`; every check that would read a
reference root as a record asks that predicate instead of spelling its own
test. The resolver's cases (C1) are in `tests/test_config.py`, since #942's
phase 6; the checks' cases sit beside each check's own (D1, D2, D3), and
this file names every shipped check and what keeps it off a reference root.
"""

import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


# --- D3: every shipped check, and what keeps it off a reference root ---------
#
# The failure this file's plan names for six months out: a check added later
# walks the tree without asking the predicate, and the class reopens one
# script at a time. So every command `bin/` ships is named here with what
# keeps it off a team's `specs/`, and a command nobody classified turns this
# red. A check that walks no `specs/` says so; one pinned to the root names
# the constant it rests on, which its module's file holds under `seal/`:
# `settle.py#SPECS` in `tests/test_settle.py` and `hooks/routing.py#WORK_ITEMS`
# in `tests/test_routing.py`, each a case of one module, which #942's round 9
# fix pass moved there from this file. The checks that walk work items are
# held off a team's `specs/` in their modules' files:
# `tests/test_unverified_check.py`'s walk from the root over a team's
# unreadable overview, `tests/test_settle.py`'s apply beside a team directory
# of the removed work item's id, and `tests/test_chain_check.py`'s
# `Test_changed_routing`, which takes a declaration only under `seal/specs/`.

PREDICATE = "asks hooks/config.py#under_reference_root"
PINNED = "reads the plugin's root by a constant under seal/"
NO_WALK = "walks no specs/ directory"
NOT_A_CHECK = "is not a check of the tree"

SHIPPED = {
    "unverified-check": (PREDICATE, "the walk and the base, by one rule"),
    "settle": (PINNED, "settle.py#SPECS; its citation scan reads as a citer"),
    "pact-check": (PINNED, "pact_check.py#anchor_files, under each signer's root"),
    "broad-gate": (NO_WALK, "runs the row, chain_check.py and seal.py mode"),
    "fold-check": (NO_WALK, "reads the top level of docs/ and seal/config.md"),
    "rules": (NO_WALK, "reads the one document it is named and its targets"),
    "arm-check": (NO_WALK, "reads the Python files it is named"),
    "mutation-check": (NO_WALK, "breaks and restores the one file it is named"),
    "test-layout": (NO_WALK, "reads tests/ and the modules its files name"),
    "deferral-check": (NO_WALK, "reads the pull request body and round records"),
    "seal": (NOT_A_CHECK, "the mode command, writing seal/config.md"),
    "seal-stamp": (NOT_A_CHECK, "draws the sealer's stamp from a sealed guarantee"),
    "session-cost": (NOT_A_CHECK, "measures a transcript"),
    "payload-meter": (NOT_A_CHECK, "measures a spawn's payload"),
    "test": (NOT_A_CHECK, "this repository's own suite runner"),
}


def test_every_shipped_command_is_classified():
    shipped = {
        name
        for name in os.listdir(os.path.join(ROOT, "bin"))
        if not name.endswith(".cmd")
    }
    assert shipped == set(SHIPPED), (
        "a command in bin/ is not classified here, or a classified one left: "
        f"{sorted(shipped ^ set(SHIPPED))}. Say what keeps it off a team's "
        "specs/ — the predicate, a constant under seal/, or no walk at all"
    )


# --- C2: the readers read a reference root when relevant, and cite it --------
#
# Each party that reads the tree for a decision is told, in its own file, that
# a reference root is history: read where the work touches what it describes,
# cited where it was read, and never written. Each names the row by pointing
# at `templates/config.md` *Reference specs* rather than restating its
# grammar, so the grammar has one home.

POINTER = "`templates/config.md` *Reference specs*"
READERS = {
    "agents/framer.md": ("cite", "spec.md"),
    "agents/smith.md": ("cite", "spec.md"),
    "agents/warden.md": ("stage 1", "spec.md"),
    "skills/settle/SKILL.md": ("cite", "spec.md"),
    "skills/implement/SKILL.md": ("cite", "spec.md"),
}


def paragraph_naming(text, phrase):
    """The blank-line-bounded block that holds `phrase`, its breaks folded."""
    at = text.index(phrase)
    start = text.rfind("\n\n", 0, at) + 2
    end = text.find("\n\n", at)
    return " ".join(text[start : end if end >= 0 else None].split())


# A definition written in #957's shape keeps what it never does in `## Never`,
# so the reader's never-write half is that list's line rather than a clause
# of the paragraph that points at the row (#967).
NEVER_LINE = {
    "agents/framer.md": "- Write in a reference root, or move, edit or copy a file out of one.",
    "agents/smith.md": "- Write in a reference root, or move, edit or copy a file out of one.",
}


def test_each_reader_says_when_it_reads_a_reference_root_and_where_it_cites_it():
    for rel, (act, where) in READERS.items():
        text = open(os.path.join(ROOT, rel), encoding="utf-8").read()
        assert POINTER in text, f"{rel} does not point at the row's section"
        said = paragraph_naming(text, POINTER)
        assert "touches what" in said and "describes" in said, (rel, said)
        assert act in said and where in said, (rel, said)
        if rel in NEVER_LINE:
            never = text[text.index("\n## Never\n") :].split("\n## ", 2)[1]
            assert NEVER_LINE[rel] in never, (rel, never)
        else:
            assert re.search(r"\bnever writ", said), (rel, said)


def test_the_seal_readme_says_nothing_writes_the_old_names():
    """The sentence used to say nothing READS a top-level `specs/`, which a
    reference root now contradicts; what is true of it is that nothing
    writes there, and what moves is the plugin's own marked work items."""
    for rel in ("templates/seal-README.md", "seal/README.md"):
        text = open(os.path.join(ROOT, rel), encoding="utf-8").read()
        flat = " ".join(text.split())
        assert "Nothing writes `.specseal/` or a top-level `specs/`" in flat, rel
        assert "Nothing reads `.specseal/`" not in flat, rel
        assert "`routing.md` or `rounds/`" in flat, rel
