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
phase 6; the checks' cases sit beside each check's own (D1, D2, D3), and this
file's last section names every shipped check and what keeps it off a
reference root.
"""

import os
import re
import subprocess
import sys

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
# fix pass moved there from this file.

PREDICATE = "asks hooks/config.py#under_reference_root"
PINNED = "reads the plugin's root by a constant under seal/"
NO_WALK = "walks no specs/ directory"
NOT_A_CHECK = "is not a check of the tree"

SHIPPED = {
    "unverified-check": (PREDICATE, "the walk and the base, by one rule"),
    "settle": (PINNED, "settle.py#SPECS; its citation scan reads as a citer"),
    "pact-check": (PINNED, "pact_check.py#anchor_files, under each signer's root"),
    "broad-gate": (NO_WALK, "hands seal/specs/ to the checks above"),
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


# A repository with a `seal/` root holding one work item, built twice: once alone, and once with a team's own `specs/` planted beside
# it — a malformed overview, a spec, and a design note, edited in the second
# commit. Every check below must say the same thing about both.
SERVICE = "def handler(x):\n    return x + 1\n"
OURS = "seal/specs/1790000000-ours"
TEAM = "specs/1788000001-team-thing"


def planted(where, team):
    def git(*args):
        subprocess.run(
            ["git", "-C", str(where), *args], check=True, capture_output=True
        )

    def put(rel, text):
        path = where / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    where.mkdir(parents=True)
    git("init", "-q", "-b", "main")
    git("config", "user.email", "t@example.com")
    git("config", "user.name", "t")
    put("src/service.py", SERVICE)
    put(f"{OURS}/routing.md", "# routing\n\n| Axis | Answer |\n|---|---|\n")
    put(
        f"{OURS}/overview.md",
        "# ours\n\n## Not verified\n\n- nothing\n  why: a probe\n",
    )
    if team:
        put(f"{TEAM}/spec.md", "# the team's spec\n\nA design they own.\n")
        put(f"{TEAM}/overview.md", "# theirs\n\n## Not verified\n\nnot a table\n")
        put(f"{TEAM}/design.md", "# design\n\n| Clause | Coordinate |\n|---|---|\n")
    git("add", "-A")
    git("commit", "-qm", "base")
    # The second commit arrives by a merge, so a check reading the range
    # meets a merge in it.
    git("switch", "-qc", "side")
    put("src/service.py", SERVICE + "\n\ndef other():\n    return 0\n")
    if team:
        put(f"{TEAM}/design.md", "# design\n\nRewritten by the team.\n")
    git("add", "-A")
    git("commit", "-qm", "second")
    git("switch", "-q", "main")
    git("merge", "-q", "--no-ff", "-m", "merge", "side")
    return where


CHECKS = {
    "chain_check.py": (
        "skills/code-review/scripts/chain_check.py",
        ["--baseline", "HEAD~1", "--root", "{r}"],
    ),
    "unverified-check": ("skills/verify/scripts/unverified_check.py", ["{r}"]),
    "settle": (
        "skills/settle/scripts/settle.py",
        ["--root", "{r}", "--released-at", "HEAD"],
    ),
}


def test_a_planted_team_specs_changes_no_checks_verdict(tmp_path):
    """D3. Each check run over the repository with and without the team's
    `specs/` exits the same and prints the same, with the repository's own
    path written out of both; and the team's directory is on disk, untouched,
    after all of them."""
    alone = planted(tmp_path / "alone", team=False)
    joined = planted(tmp_path / "joined", team=True)
    before = {
        rel: (joined / TEAM / rel).read_bytes()
        for rel in ("spec.md", "overview.md", "design.md")
    }
    for name, (script, args) in CHECKS.items():
        said = []
        for repo in (alone, joined):
            r = subprocess.run(
                [sys.executable, os.path.join(ROOT, script)]
                + [a.replace("{r}", str(repo)) for a in args],
                cwd=str(repo),
                capture_output=True,
                encoding="utf-8",
                errors="replace",
            )
            # The two repositories' paths and commits differ by construction.
            text = re.sub(
                r"\b[0-9a-f]{7,40}\b",
                "<sha>",
                (r.stdout + r.stderr).replace(str(repo), "<repo>"),
            )
            said.append((r.returncode, text))
        assert said[0] == said[1], (
            f"{name} says something else once a team's specs/ is planted:\n"
            f"alone:\n{said[0]}\njoined:\n{said[1]}"
        )
        assert "team-thing" not in said[1][1], f"{name} read the team's specs/"
    for rel, data in before.items():
        assert (joined / TEAM / rel).read_bytes() == data, rel


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
