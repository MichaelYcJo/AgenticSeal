"""The scanned files hold the records root's second name (#1059) where it is
defined and nowhere else: once in `skills/core/SKILL.md`, and on one line of
each README's section on shared and local mode.

`tracked` lists the tracked files under `SCANNED` whose names end in one of
`SUFFIXES`, those on disk and those not.
`tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` names it among
the scopes that apply the shared guard.

That no code of the plugin opens `.specseal/` or a top-level `specs/` on its
own is behaviour, which `tests/lib/test_optin.py` reads.
"""

import os

import pytest
from conftest import (
    ROOT,
    git_listing,
    load_lib_module,
    on_disk,
    read,
)

# No TARGET: its cases walk every scanned document of the tree for the roots' old names.

SCANNED = (
    ".github/workflows",
    "templates",
    "skills",
    "agents",
    "docs",
    "CONTRIBUTING.md",
    "CLAUDE.md",
    "SECURITY.md",
    "seal/README.md",
    "README.md",
    "README.ko.md",
)
SUFFIXES = (".md", ".yml", ".sh")


def tracked(root=ROOT):
    """`(the scanned files on disk, the scanned paths that are not)`.

    `root` is an argument so a case can build a repository with a
    tracked-and-deleted file and watch the guard work; `conftest.on_disk`
    carries why the second half is returned rather than dropped.
    """
    out = git_listing(root, "ls-files", *SCANNED)
    listed = [rel for rel in out if rel.endswith(SUFFIXES)]
    return on_disk(root, listed)


# --- #1059: the second name stands where it is defined, and nowhere else ----
#
# Every shipped text calls the records root `seal/`, and the core's opening
# paragraph says once which folder that is where the project keeps a `seal/`
# of its own. A person reads a README before any core is printed, so each
# README states the name on one line of its section on shared and local mode.
# A rename then changes the core, `lib/optin.py` and those two lines, and the
# cases below name each one it left behind.

SECOND_HOME = load_lib_module("optin.py", "agentic_optin_second_name").SECOND_HOME
CORE = "skills/core/SKILL.md"
# Each README, and the heading of the section that holds its one line.
READMES = {
    "README.md": "### Shared or local",
    "README.ko.md": "### shared 인가 local 인가",
}


def lines_naming_the_second_root(text):
    """The lines of TEXT that hold `lib/optin.py#SECOND_HOME`."""
    return [line for line in text.splitlines() if SECOND_HOME in line]


def test_the_core_states_the_second_name_once():
    core = read(*CORE.split("/"))
    assert core.count(f"`{SECOND_HOME}/`") == 1, (
        f"{CORE} does not name `{SECOND_HOME}/` exactly once"
    )
    assert len(lines_naming_the_second_root(core)) == 1, CORE


@pytest.mark.parametrize("rel", sorted(READMES))
def test_each_readme_states_the_second_name_on_one_line_of_shared_or_local(rel):
    text = read(rel)
    found = lines_naming_the_second_root(text)
    assert len(found) == 1, f"{rel} names {SECOND_HOME} on {len(found)} lines"
    heading = READMES[rel]
    assert heading in text, f"{heading!r} is not a heading of {rel} any more"
    body = text.split(heading, 1)[1].split("\n#", 1)[0]
    assert found[0] in body.splitlines(), f"{rel}: {found[0]!r} is not under {heading}"


def test_no_other_scanned_file_states_the_second_name():
    files, _ = tracked()
    found = []
    for rel in files:
        if rel == CORE or rel in READMES:
            continue
        with open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace") as f:
            text = f.read()
        found += [
            f"  {rel}:{number}  {line.strip()[:100]}"
            for number, line in enumerate(text.splitlines(), 1)
            if SECOND_HOME in line
        ]
    assert not found, "\n".join(
        [f"{SECOND_HOME} is stated outside {CORE} and the READMEs:", *found]
    )
