"""The rules `CLAUDE.md` once named have one home each, and the files that
carry one of them name its home (#730).

#715 gave the ledger and fragment rules one home each and left the rest of
`CLAUDE.md` alone. Three more of its rows restated a rule another file held,
and one of those copies had already gone false: the merge table there said a
`# RIDER:` stamp names a commit, where its home had said the reverse since
work item `1788826000`, and it had lost two of the home's six rows. Nothing
pinned that copy, so nothing went red. A fourth restatement sat at the foot of
the goal section, beside the link to the rule it restated.

So each rule was given one home, which states it:

  the merge method per direction   docs/releasing/branch-and-release.md
  no real identifiers              CONTRIBUTING.md
  the question batch               skills/implement/orchestration.md,
                                   *Orchestrator: what needs a person is
                                   asked in one batch, before the first
                                   edit*, since #1312

`CLAUDE.md` kept a row for each that linked the home, until #940, #1169 and
#1177 took the rows out, as the comment above `LINKED` says.

#1177 retired the preset block, and the core now reaches a session from
the plugin's `SessionStart` hook. Two of the block's bullets moved to the file
that applies each:

  the project's package manager    skills/implement/SKILL.md, step 2
  a worktree only when concurrent  skills/implement/orchestration.md,
                                   *Orchestrator: the order inside a ticket*

The cases hold two things. Each home states, under its section, the facts
`RULES` gives it: a table row a reader matches, and the commands a reader
runs. Each file in `LINKED` names the home's path and its section for each
rule it carries. Whether a carrier restates a home in other words, or in the
home's own, is the proofer's to read, and
`tests/text/test_no_passage_is_pasted_into_a_second_file.py` reads a pasted
passage.
"""

import os
import re

from conftest import ROOT

# No TARGET: its cases hold each rule's home across the documents that state it and the files that link it.

BRANCHES = "docs/releasing/branch-and-release.md"
CONTRIBUTING = "CONTRIBUTING.md"
IMPLEMENT = "skills/implement/SKILL.md"
ORCH = "skills/implement/orchestration.md"

# rule: (home, section heading, the facts the home states under it)
RULES = {
    "merge": (
        BRANCHES,
        "Work accumulates on a release branch",
        (
            # The table row a person matches against the direction of a
            # merge, and the merge method it gives.
            "| a feature branch | `release/vX.Y.Z` | **squash** | *Squash and merge* |",
        ),
    ),
    # The home and the section `LINKED` resolves; the rule's words are the
    # proofer's to read.
    "identifiers": (CONTRIBUTING, "House rules", ()),
    "batch": (
        ORCH,
        "Orchestrator: what needs a person is asked in one batch, before the first edit",
        (),
    ),
    # The preset block's tooling and worktree bullets, each moved to the step
    # that applies it when the block retired (#1177).
    "tooling": (
        IMPLEMENT,
        "2. Implement test-first, and let each rule name its test",
        (
            # The two runners a session uses where the project names none.
            "`uv`",
            "`pnpm`",
        ),
    ),
    "worktree": (
        ORCH,
        "Orchestrator: the order inside a ticket",
        (
            # The command the orchestrator makes the branch with.
            "`git switch`",
        ),
    ),
}

# The files that must name a home's path and section, and for which rules.
# `CLAUDE.md` is loaded into every session; the code comments below cited it
# for the identifiers rule until this work pointed them at the home.
LINKED = {
    # The core holds the values and links only the rule its first value
    # names; it left `CLAUDE.md` for `skills/core/SKILL.md` with #1177. The
    # cadence row left `CLAUDE.md` with #940, and the merge and identifiers
    # rows with #1169: no agent merges. `agents/proofer.md` linked the
    # identifiers rule until #1148, which took the link out: a shipped
    # definition names no file of this repository's own, and its bullet
    # stands on its own words.
    "skills/core/SKILL.md": ("batch",),
    ".github/scripts/plugin_directory_check.py": ("identifiers",),
    "tests/github/test_plugin_directory_check.py": ("identifiers",),
    "tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py": ("identifiers",),
}


def flat(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return " ".join(f.read().split())


def section(rel, heading):
    """The text under the heading in REL, at any level, flattened.

    It runs to the next heading of the same level or above, so a `###`
    section keeps its own `####` children and stops at its sibling."""
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        text = f.read()
    heads = list(re.finditer(r"(?m)^(#{2,6}) (.+?)\s*$", text))
    found = [h for h in heads if h.group(2) == heading]
    assert len(found) == 1, f"{rel} has no single heading `{heading}`"
    start, level = found[0], len(found[0].group(1))
    end = len(text)
    for h in heads:
        if h.start() > start.start() and len(h.group(1)) <= level:
            end = h.start()
            break
    return " ".join(text[start.end() : end].split())


def unlinked(texts):
    """(file, rule) for every rule a linked file does not name the home of."""
    missing = []
    for rel, rules in LINKED.items():
        text = texts[rel]
        for rule in rules:
            home, heading, _ = RULES[rule]
            if home not in text or heading not in text:
                missing.append((rel, rule))
    return missing


def tree():
    return {rel: flat(rel) for rel in sorted(LINKED)}


def test_each_home_states_its_rule_under_its_section():
    for rule, (home, heading, facts) in RULES.items():
        body = section(home, heading)
        missing = [n for n in facts if " ".join(n.split()) not in body]
        assert not missing, f"{home} *{heading}* does not state {rule}: {missing}"


def test_every_linked_file_names_each_home_and_section():
    """A link is the home's path and its section's name, in the file."""
    missing = unlinked(tree())
    # The home's path and its section's heading, which a reader of the
    # linking file resolves.
    assert not missing, (
        f"these files do not name the home of a rule they carry: {missing}"
    )


def test_a_removed_link_is_named():
    """The check can fail: a row that drops its home's path is named, and so
    is one that keeps the path and drops the section."""
    linked = ".github/scripts/plugin_directory_check.py"
    texts = tree()
    texts[linked] = texts[linked].replace(CONTRIBUTING, "the guide")
    assert (linked, "identifiers") in unlinked(texts)
    texts = tree()
    texts[linked] = texts[linked].replace("House rules", "")
    assert (linked, "identifiers") in unlinked(texts)
