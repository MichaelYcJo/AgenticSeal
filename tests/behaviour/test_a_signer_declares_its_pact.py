"""A signer declares its pact (#647, step A).

Some work items commit in more than one repository, and those repositories
keep one contract together. The one copy of it is the PACT, `seal/pact.md` in
the repository that holds it, and every repository of such a work item is a
SIGNER. A signer other than the pact's repository names the pact in its
own `seal/config.json`:

    "Pact": "git@example.com:org/orders-api.git"

The key has one reader, `lib/config.py#pact_declaration`, which
`pact_check.py` asks, run as `seal pact`, and refuses on. That reader's
cases (S1-S3 of the work item's `frame/design.md`) and those of the `Pact
signers` key's reader are in `tests/lib/test_config.py`, and `seal.py`'s re-export of
its normaliser is in `tests/skills/test_seal.py`. What stays here reads the configs
and templates this plugin ships through the reader, and the commands and the
key the routing step names (S4).
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


def test_the_template_and_the_config_skill_carry_the_pact_row():
    """`templates/setup/config.md` documents the `Pact` key and `/agentic:config`
    shows it."""
    template = flat("templates", "setup", "config.md")
    skill = flat("skills", "config", "SKILL.md")
    # The key `PACT_KEY` in the template's bold lead, which a person writing
    # `seal/config.json` copies and `lib/config.py#pact_declaration` matches.
    assert f"**`{config.PACT_KEY}`**" in template
    # The same key in the skill's table row, which `/agentic:config` shows.
    assert f"| `{config.PACT_KEY}` |" in skill


def test_the_template_and_the_config_skill_carry_the_pact_signers_key():
    """S7. `templates/setup/config.md` *Pact* documents the `Pact signers`
    key the pact's repository lists its signers in, and `/agentic:config`
    shows it."""
    template = flat("templates", "setup", "config.md")
    skill = flat("skills", "config", "SKILL.md")
    # The key `SIGNERS_KEY` in the template's bold lead, which a person
    # writing the pact's repository's `seal/config.json` copies and
    # `lib/config.py#signer_declaration` matches.
    assert f"**`{config.SIGNERS_KEY}`**" in template
    # The same key in the skill's table row, which `/agentic:config` shows.
    assert f"| `{config.SIGNERS_KEY}` |" in skill


# --- S4: the routing step across repositories -------------------------------

# In a file of its own since #1148, opened only where a work item commits in
# more than one repository.
MULTI = ("skills", "implement", "multi-repository.md")


def test_the_routing_step_mints_one_id_and_declares_the_signers():
    """S4. The id is minted once, each repository is committed in by its own
    path, and the pact's repository lists the other signers. Why a
    repository with no root is left alone is the proofer's to read."""
    text = flat(*MULTI)
    start = text.index(
        "## Orchestrator: a work item that commits in more than one repository"
    )
    section = text[start:]
    for said in (
        # The command the orchestrator runs once to mint the id.
        "`date +%s`",
        # The command form the orchestrator commits in each repository with.
        "`git -C`",
        # The key `lib/config.py#SIGNERS_KEY` names, which the orchestrator
        # writes into the pact's repository's `seal/config.json`.
        f"`{config.SIGNERS_KEY}`",
        # The separator `lib/config.py#remote_list` splits that key's value
        # at, which the orchestrator writes between the URLs.
        f"separated by `{config.PACT_SEPARATOR}`",
    ):
        assert said in section, said
