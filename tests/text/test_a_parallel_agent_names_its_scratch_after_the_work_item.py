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
whole. Contract rule 21's removal names the work item's directory and never
the scratchpad, which is the same repair at the moment of cleanup. This
file pins the five sentences and that clause, because a definition is a
sentence an agent reads and a sentence can be dropped without a case going
red.

What it cannot pin is obedience: a spawn prompt that names a different
directory still wins in the moment, and nothing in the tree reads a prompt.
`plan.md` *Failure scenario* of the work item says so.
"""

import os

from conftest import ROOT, read

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
WORK_ITEM_HOME = "<scratchpad>/<work-item-id>/"


def section(path, heading):
    """`## <heading>` to the next `## `, as one line so a pinned phrase
    survives re-wrapping."""
    text = read(path)
    start = text.index(f"## {heading}")
    end = text.find("\n## ", start + 1)
    body = text[start : end if end != -1 else len(text)]
    return " ".join(body.split())


def test_the_wardens_clone_is_named_for_the_work_item_and_the_round():
    """A12. The clone directory carries the work item id the prompt names
    and the round, under the scratchpad the harness names — so two wardens
    alive at once, on two work items, cannot pick the same directory. Every
    probe, capture or fixture the round makes outside the clone sits beside
    it, which is also what makes *every one of them is gone* (contract rule 7) answerable
    by the agent that made them."""
    where = section(PROOFER, "Rules")
    assert CLONE in where, (
        "`agents/proofer.md` *Rules* does not name the clone directory "
        f"as `{CLONE}`, so two parallel wardens can clone to one name"
    )
    assert ROUND_HOME in where, (
        "the section does not put the round's probes and captures under "
        f"`{ROUND_HOME}`, so a round's leavings have no one home to remove"
    )
    assert "share" in where and "scratchpad" in where, (
        "the sentence names the directory and not why: agents of one session "
        "share the scratchpad"
    )


def test_the_framers_probe_is_named_for_the_work_item():
    """#1047 S4. A framer's probe writes its script, its captures and its
    clone under one directory that carries the work item id, so a framer and
    a proofer alive at once in one session cannot pick the same name, and
    the framer removes what it made by that one path."""
    where = section(FRAMER, "Rules")
    assert FRAME_HOME in where, (
        "`agents/framer.md` *Rules* does not name the probe's directory as "
        f"`{FRAME_HOME}`, so a framer's writes have no name of their own"
    )
    assert "share" in where and "scratchpad" in where, (
        "the sentence names the directory and not why: agents of one session "
        "share the scratchpad"
    )


def test_the_crafters_scratch_is_named_for_the_work_item_and_the_phase():
    """#1445 S6. A crafter that names no directory of its own writes
    straight into the scratchpad, and in the 0.37.0 run one removed the
    whole scratchpad with the files of every other agent of the session in
    it. A phase's writes sit under a directory named for the work item and
    the phase, and a fix pass's under one named for the round it fixes, so
    two crafters alive at once cannot pick one name, and each removes its
    own directory."""
    where = section(CRAFTER, "Rules")
    assert PHASE_HOME in where, (
        "`agents/crafter.md` *Rules* does not name a phase's directory as "
        f"`{PHASE_HOME}`, so a crafter's writes have no name of their own"
    )
    assert FIX_HOME in where, (
        "the section does not name a fix pass's directory as "
        f"`{FIX_HOME}`, so a fix pass writes into the shared scratchpad"
    )
    assert "share" in where and "scratchpad" in where, (
        "the sentence names the directory and not why: agents of one session "
        "share the scratchpad"
    )


def test_rule_21_removes_the_agents_directory_and_never_the_scratchpad():
    """#1445 S6. Contract rule 21 asks that a directory an agent made be
    removed in one `rm -rf`. Without a location, the scratchpad itself reads
    as such a directory, and every agent of the session loses its files with
    it. The rule names the work item's directory under the scratchpad, and
    says the removal never names the scratchpad itself."""
    where = section(CONTRACT, "21 ")
    assert WORK_ITEM_HOME in where, (
        "contract rule 21 does not name the directory a removal takes as one "
        f"under `{WORK_ITEM_HOME}`, so the scratchpad reads as the directory "
        "an agent made"
    )
    assert "never names the scratchpad itself" in where, (
        "contract rule 21 does not say a removal never names the scratchpad "
        "itself, which every agent of the session shares"
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
