"""A signer declares its pact (#647, step A).

Some work items commit in more than one repository, and those repositories
keep one contract together. The one copy of it is the PACT, `seal/pact.md` in
the repository that holds it, and every repository of such a work item is a
SIGNER. A signer other than the pact's repository names the pact in its
own `seal/config.md`:

    | Pact | git@example.com:org/orders-api.git |

The row has one reader, `hooks/lib/config.py#pact_declaration`, which
`pact_check.py` asks, run as `seal pact`, and refuses on. That reader's
cases (S1-S3 of the work item's `frame/design.md`) and the `Signer` table's are in
`tests/hooks/test_config.py` since #942's phase 6, and `seal.py`'s re-export of
its normaliser is in `tests/skills/test_seal.py`. What stays here reads the configs
and templates this plugin ships through the reader, and the routing step's
pinned sentences (S4).
"""

import os

from conftest import ORDERS, ROOT, URL, flat, load_hook_module

config = load_hook_module("lib/config.py", "config_for_the_pact")


def _broad_gate_block():
    """The prose `skills/config/SKILL.md` step 3 tells a session to copy
    below the live table: `templates/setup/config.md` from `## Broad gate` down to
    `### What is refused, and what stays allowed`."""
    with open(
        os.path.join(ROOT, "templates", "setup", "config.md"), encoding="utf-8"
    ) as f:
        text = f.read()
    start = text.index("## Broad gate\n")
    return text[start : text.index("### What is refused, and what stays allowed")]


def test_s4_the_configs_this_plugin_writes_or_copies_are_silent():
    """S4. This repository's own `seal/config.md`, the stub `seal mode`
    writes, that stub with the copied `## Broad gate` block below it -- with
    and without the `Pact` row `orchestration.md` writes into the table --
    and `templates/setup/config.md` copied whole, which
    `skills/commit-pr-convention/SKILL.md` tells a session to do, give no
    refusal to the reader `seal pact` reads strictly. Each is read from the
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
    with open(
        os.path.join(ROOT, "templates", "setup", "config.md"), encoding="utf-8"
    ) as f:
        template = f.read()
    assert config.pact_declaration(template) == ([], [])
    filled = template.replace("| Pact |  |\n", f"| Pact | {URL} |\n", 1)
    assert filled != template
    assert config.pact_declaration(filled) == (ORDERS, [])


# --- the shipped rows -------------------------------------------------------


def test_the_template_and_the_config_skill_carry_the_pact_row_alone():
    """`templates/setup/config.md` documents the `Pact` row and `/agentic:config`
    shows it; neither carries a `Pact notify` row, and the template says
    once what one left in a config does."""
    template = flat("templates", "setup", "config.md")
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
