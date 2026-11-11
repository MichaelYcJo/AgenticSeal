"""Two agents alive at once cannot share a scratch name.

Issue #544. Every agent of one session shares one scratchpad, and four work
items ran their review chains in parallel from one session in the 0.15.0 run.
`agents/proofer.md` named the clone's shape (`git clone --no-local` at the
target SHA) and no directory; `agents/sealer.md` named no capture file;
`skills/verify/SKILL.md`'s capture example redirected to `/tmp/run.txt`,
which every session on the machine shares. Measured three times in that run:
two wardens cloned to the same `r2clone`, a third's clone had its HEAD moved
by a foreign checkout for fifty-five seconds, and two sealers wrote
one gate output file over each other.

The class (contract rule 12) is *an instruction that names a scratch
location with a name any parallel agent would also pick*, and the repair is
the same in each of its five instances: the location carries the work item
id, which no two work items share, and the round or the phase where there
is one. The fourth is the framer's probe directory (#1047), and the fifth
the crafter's directories for a phase and a fix pass (#1445), where a
crafter that named none wrote into the scratchpad itself and removed it
whole.

Contract rule 17 states the rule once (#1474, #1503): an agent's scratch
directory is `<scratchpad>/<work-item-id>/<leaf>/`, the name keeps a
parallel agent's files apart because the agents of one session share one
scratchpad, an agent that finds its directory standing adds `-2` to the
leaf, and no agent removes the scratchpad, a scratch directory or a file
in one. Each definition names its own leaf and cites rule 17. A removal
written with a variable in its path is a command Claude Code holds for a
person (#1503), so no section of the contract and no agent definition
writes `rm -rf`. The one removal left is the orchestrator's, of the work
item's directory once the pull request is open, in one `rm -rf` with its
path written out (`skills/implement/orchestration.md` *Orchestrator: the
order inside a ticket*), which no agent preloads. This file pins rule 17's sentences, the directory each
definition names, and that absence, because a definition is a sentence an
agent reads and a sentence can be dropped without a case going red.

What it cannot pin is obedience: a spawn prompt that names a different
directory still wins in the moment, and nothing in the tree reads a prompt.
`plan.md` *Failure scenario* of the work item says so.
"""

import glob
import os

from conftest import ROOT, read

AGENTS = sorted(glob.glob(os.path.join(ROOT, "agents", "*.md")))
PROOFER = os.path.join(ROOT, "agents", "proofer.md")
SEALER = os.path.join(ROOT, "agents", "sealer.md")
FRAMER = os.path.join(ROOT, "agents", "framer.md")
CRAFTER = os.path.join(ROOT, "agents", "crafter.md")
CONTRACT = os.path.join(ROOT, "skills", "agent-contract", "SKILL.md")
REVIEW_ORCH = os.path.join(ROOT, "skills", "code-review", "orchestration.md")
VERIFY = os.path.join(ROOT, "skills", "verify", "SKILL.md")

CLONE = "<scratchpad>/<work-item-id>/round-<n>/clone"
ROUND_HOME = "<scratchpad>/<work-item-id>/round-<n>/"
FRAME_HOME = "<scratchpad>/<work-item-id>/frame/"
PHASE_HOME = "<scratchpad>/<work-item-id>/phase-<n>/"
FIX_HOME = "<scratchpad>/<work-item-id>/fix-<n>/"
LEAF_HOME = "<scratchpad>/<work-item-id>/<leaf>/"


def section(path, heading):
    """`## <heading>` to the next `## `, as one line so a pinned phrase
    survives re-wrapping."""
    text = read(path)
    start = text.index(f"## {heading}")
    end = text.find("\n## ", start + 1)
    body = text[start : end if end != -1 else len(text)]
    return " ".join(body.split())


def test_the_wardens_clone_is_named_for_the_work_item_and_the_round():
    """A12. The proofer's scratch directory carries the work item id the
    prompt names and the round, under the scratchpad the harness names, and
    the clone sits inside it, so two proofers alive at once, on two work
    items, cannot pick the same directory. Every probe, capture or fixture
    the round makes outside the clone sits beside the clone. Why the name
    carries the work item is contract rule 17's, which the definition
    cites."""
    where = section(PROOFER, "Rules")
    assert CLONE in where, (
        "`agents/proofer.md` *Rules* does not name the clone directory "
        f"as `{CLONE}`, so two parallel proofers can clone to one name"
    )
    # Quoted whole, so the clone's path, which begins with the same
    # spelling, does not hold the scratch directory's sentence too.
    assert f"`{ROUND_HOME}`" in where, (
        "the section does not name the round's scratch directory as "
        f"`{ROUND_HOME}`, so a round's probes and captures have no name of "
        "their own"
    )


def test_the_framers_probe_is_named_for_the_work_item():
    """#1047 S4. A framer's probe writes its script, its captures and its
    clone under one directory that carries the work item id, so a framer and
    a proofer alive at once in one session cannot pick the same name. Why
    the name carries the work item is contract rule 17's, which the
    definition cites."""
    where = section(FRAMER, "Rules")
    assert FRAME_HOME in where, (
        "`agents/framer.md` *Rules* does not name the probe's directory as "
        f"`{FRAME_HOME}`, so a framer's writes have no name of their own"
    )


def test_the_crafters_scratch_is_named_for_the_work_item_and_the_phase():
    """#1445 S6. A crafter that names no directory of its own writes
    straight into the scratchpad, and in the 0.37.0 run one removed the
    whole scratchpad with the files of every other agent of the session in
    it. A phase's writes sit under a directory named for the work item and
    the phase, and a fix pass's under one named for the round it fixes, so
    two crafters alive at once cannot pick one name. Why the name carries
    the work item is contract rule 17's, which the definition cites."""
    where = section(CRAFTER, "Rules")
    assert PHASE_HOME in where, (
        "`agents/crafter.md` *Rules* does not name a phase's directory as "
        f"`{PHASE_HOME}`, so a crafter's writes have no name of their own"
    )
    assert FIX_HOME in where, (
        "the section does not name a fix pass's directory as "
        f"`{FIX_HOME}`, so a fix pass writes into the shared scratchpad"
    )


def test_rule_17_names_the_scratch_directory_for_the_work_item():
    """#1474, #1503. Contract rule 17 is the one statement of the scratch
    rule, which every agent receives: the directory's shape, with the leaf
    each definition names, why the name carries the work item, and what an
    agent does where an earlier spawn left its directory standing. No agent
    removes a scratch directory, so a second sealer or proofer of one work
    item that cloned into the standing directory would fail, and the rule
    gives it the next free leaf."""
    where = section(CONTRACT, "17 ")
    assert LEAF_HOME in where, (
        "contract rule 17 does not name the scratch directory as "
        f"`{LEAF_HOME}`, so an agent whose definition names a leaf has no "
        "path to put it in"
    )
    assert "share one scratchpad" in where, (
        "contract rule 17 names the directory and not why: agents of one "
        "session share one scratchpad"
    )
    assert "add `-2` to the leaf" in where, (
        "contract rule 17 does not say what an agent does where its "
        "directory already stands, so a second clone into it fails"
    )


def test_no_contract_section_or_definition_writes_a_removal():
    """#1503. Contract rule 21 once asked an agent to remove its directory in
    one `rm -rf`, and a crafter closed a phase with a loop of `rm` on a
    variable path, which Claude Code held for the owner. No agent removes
    its scratch directory now (contract rule 17), so no section of the
    contract and no agent definition writes the command. The orchestrator's
    one removal stands in a skill no agent preloads."""
    for path in [CONTRACT, *AGENTS]:
        name = os.path.relpath(path, ROOT)
        assert "rm -rf" not in read(path), (
            f"{name} writes `rm -rf`, and no agent removes its scratch "
            "directory (contract rule 17)"
        )


def test_the_gates_capture_file_carries_the_work_item_id():
    """A13, moved by #969 with the run. Where the orchestrator redirects the
    gate's output to a file to read, the file is named for the work item; and
    the gate's own `outputs kept under seal-gate-<random>/` line is quoted,
    so a capture that was overwritten can still be told apart — which is how
    the 0.15.0 runs were not misread. Two work items run in parallel by one
    session would otherwise write one log over each other. The sealer keeps
    its own scratch: the clone a `seen red` is re-run in."""
    command = section(
        REVIEW_ORCH, "Orchestrator: the pull request opens once the sealer seals"
    )
    assert "<scratchpad>/<work-item-id>/gate.log" in command, (
        "the orchestration names no capture file carrying the work item id, "
        "so two work items' runs write one file over each other"
    )
    assert "outputs kept under" in command, (
        "the section does not tell the orchestrator to quote the gate's "
        "`outputs kept under` line, which is the one name per run the gate "
        "itself makes"
    )
    sealer = section(SEALER, "Rules")
    assert "<scratchpad>/<work-item-id>/at-base/" in sealer, (
        "the clone a `seen red` is re-run in is not named for the work item"
    )


def test_the_capture_example_is_not_a_name_every_session_shares():
    """A14. `/tmp/run.txt` is the same class one file over, shared across
    every session on the machine rather than across one session's agents.
    The fenced example redirects under the scratchpad with the work item id."""
    text = read(VERIFY)
    assert "/tmp/run.txt" not in text, (
        "skills/verify/SKILL.md still shows a capture file every session on "
        "the machine would also pick"
    )
    start = text.index("**Capture once, filter locally.**")
    example = text[start : text.index("The tell is a second invocation", start)]
    assert "<scratchpad>/<work-item-id>/" in example, (
        "the capture example does not carry the work item id in the file it "
        "redirects to"
    )
