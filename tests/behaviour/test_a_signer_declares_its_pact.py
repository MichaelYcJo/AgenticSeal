"""A signer declares its pact (#647, step A).

Some work items commit in more than one repository, and those repositories
keep one contract together. The one copy of it is the PACT, `seal/pact.md` in
the repository that holds it, and every repository of such a work item is a
SIGNER. A signer other than the pact's repository names the pact in its
own `seal/config.json`:

    "Pact": "git@example.com:org/orders-api.git"

The key has one reader, `lib/config.py#pact_declaration`, which
`pact_check.py` asks, run as `seal pact`, and refuses on. That reader's
cases (S1-S3 of the work item's `frame/design.md`) and the `Signer` table's are in
`tests/lib/test_config.py` since #942's phase 6, and `seal.py`'s re-export of
its normaliser is in `tests/skills/test_seal.py`. What stays here reads the configs
and templates this plugin ships through the reader, and the routing step's
pinned sentences (S4).
"""

import os

from conftest import ORDERS, ROOT, URL, flat, load_lib_module, load_module

config = load_lib_module("config.py", "config_for_the_pact")


def test_s4_the_configs_this_plugin_writes_are_silent():
    """S4. This repository's own `seal/config.json` and the file `seal mode`
    writes, with and without the `Pact` key `orchestration.md` writes into
    it, give no refusal to the reader `seal pact` reads strictly. Each is
    read from the tree or written by the tree's serializer, not retyped."""
    seal = load_module(
        os.path.join(ROOT, "skills", "implement", "scripts", "seal.py"),
        "seal_for_the_silent_set",
    )
    pairs, refusal = config.config_pairs(os.path.join(ROOT, "seal"))
    assert refusal is None, refusal
    assert config.pact_declaration(pairs) == ([], [])
    for written, pacts in (
        ([("Mode", "shared")], []),
        ([("Mode", "shared"), ("Pact", URL)], ORDERS),
    ):
        read, refusal = config.parse_config(seal.serialized(written), "config.json")
        assert refusal is None, refusal
        assert config.pact_declaration(read) == (pacts, [])


# --- the shipped rows -------------------------------------------------------


def test_the_template_and_the_config_skill_carry_the_pact_row_alone():
    """`templates/setup/config.md` documents the `Pact` row and `/agentic:config`
    shows it; neither carries a `Pact notify` row, and the template says
    once what one left in a config does."""
    template = flat("templates", "setup", "config.md")
    skill = flat("skills", "config", "SKILL.md")
    assert f"**`{config.PACT_KEY}`**" in template
    assert f"| `{config.PACT_KEY}` |" in skill
    assert "| Pact notify |" not in template
    assert "| `Pact notify` |" not in skill
    assert (
        "**A `Pact notify` row is read by nobody.** No command refuses it, "
        "prints it or names it, like any item no reader asks for, and whoever "
        "next edits the file deletes it."
    ) in template
    assert template.count("Pact notify") == 1, "the template says it once"


# --- S4: the routing step across repositories -------------------------------

# In a file of its own since #1148, opened only where a work item commits in
# more than one repository.
MULTI = ("skills", "implement", "multi-repository.md")


def test_the_routing_step_mints_one_id_and_declares_only_in_gated_repositories():
    """S4. The question is asked once, the id is minted once, and a
    repository with no root is named and left alone, because writing into it
    would opt it in."""
    text = flat(*MULTI)
    start = text.index(
        "## Orchestrator: a work item that commits in more than one repository"
    )
    section = text[start:]
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
