"""The gate's arm list was kept in step with the workflow's by whoever
remembered, and nothing held the two lists against each other (#468).

`skills/verify/scripts/broad_gate.py#gate` runs a handful of arms so the
sealer's one run says what CI will say. `.github/workflows/hygiene.yml`'s
`release` job runs ten named steps. #424 added one of them and the gate
was not extended, so from that merge onward a green run covered a
shorter list than the merge is judged by — and no case in the suite went red
for it.

The repair is a declared partition: every step of that job is either mirrored
by a named arm or excluded with a reason a person wrote. This module is what
keeps the partition total, and it is driven RED FROM BOTH SIDES. #423's
finding 4 was a narrow reader, one that saw three of four base spellings, and
it named both directions, which the two rows below hold:

  A1   a step added to the workflow and left unclassified fails here, so the
       seventh arm cannot arrive in silence
  A2   a partition entry naming a step the workflow no longer has fails here,
       so the list cannot rot into naming steps nobody runs

`frame/design.md` *User scenarios & acceptance* numbers the rows A1 to A7 and each
case below names the one it holds.

**The step names are read out of `hygiene.yml` itself.** `plan.md` retypes
them for a human reader and says in the same breath that its copy will rot; a
case driven by a list in a document is a case that grades the document. No
YAML parser either — `broad_gate.py` runs with no third-party dependency, so
the reader is text, and it is driven over shapes this repository's workflow
does not happen to have, in `tests/skills/test_broad_gate.py`'s `Test_job_steps`.
A reader nothing drives is a reader nobody can tell is partial (#424's
finding 4).

#942 moved the cases of `broad_gate.py` that read no file of this
repository into `tests/skills/test_broad_gate.py`: the reader's, the partition's
shape and arms, the reasons' wording, the command run over a fixture
repository, `coverage_line`'s and `base_is_main`'s. The cases here read
`hygiene.yml`, `skills/verify/orchestration.md` or `docs/the-broad-gate.md`,
which #923 places.
"""

import os
import re

from conftest import ROOT, load_module, read, workflow_step
from test_broad_gate import reasons

GATE = os.path.join(ROOT, "skills", "verify", "scripts", "broad_gate.py")
HYGIENE = os.path.join(ROOT, ".github", "workflows", "hygiene.yml")


def gate_module():
    return load_module(GATE, "agentic_broad_gate_for_partition_tests")


gate = gate_module()


# --- A1 and A2: the partition is total, in both directions ------------------


def workflow_steps():
    steps = gate.job_steps(read(HYGIENE), gate.RELEASE_JOB)
    assert steps, (
        f"{HYGIENE} names no step of the `{gate.RELEASE_JOB}` job. Either the "
        "job was renamed or the file's shape moved under the reader — and a "
        "reader that comes back empty grades nothing, so this is a refusal "
        "rather than a pass"
    )
    return steps


def test_every_step_the_workflow_runs_is_classified():
    """A1. Red when a step is added to the workflow and nobody classifies it.

    This is the direction the work item exists for: #424 added the thirteenth
    step, the gate was not extended, and the suite said nothing. A step with
    no row is the silence this ends — `classified` includes `excluded`, and an
    exclusion carries prose rather than a category (A4).
    """
    classified = {name for name, _, _ in gate.PARTITION}
    missing = [name for name in workflow_steps() if name not in classified]
    assert not missing, (
        f"these steps of `hygiene.yml`'s `{gate.RELEASE_JOB}` job are in no "
        f"row of `broad_gate.py#PARTITION`: {missing}. Add an arm that mirrors "
        "each, or a row excluding it with the reason no arm can — there is no "
        "third state, and a step with no row is a run that covers less than "
        "the merge is judged by"
    )


def test_every_entry_of_the_partition_names_a_step_the_workflow_has():
    """A2. The other side. Red when a step is renamed in the workflow, or
    removed, and the partition still names it.

    Without this the partition rots into a list of steps nobody runs, and a
    reader counting what the seal did not answer is counting ghosts."""
    steps = set(workflow_steps())
    stale = [name for name, _, _ in gate.PARTITION if name not in steps]
    assert not stale, (
        f"`broad_gate.py#PARTITION` names steps `hygiene.yml`'s "
        f"`{gate.RELEASE_JOB}` job does not have: {stale}. A renamed step is "
        "a row to rename here; a deleted one is a row to delete"
    )


# --- A4: a reason is prose a person wrote -----------------------------------


NUMBER_WORDS = ("no", "one", "two", "three", "four", "five", "six", "seven")


def test_the_skill_counts_the_steps_with_a_local_answer_and_no_arm():
    """The shipped verify skill's orchestrator half counts the `release` steps
    that have a local answer and no arm — the ones that run this repository's
    own script, and the one written inline — and the count is `PARTITION`'s,
    so a step added to either kind moves the sentence or fails here."""
    scripts = sum(".github/scripts/" in reason for _, reason in reasons())
    inline = sum("inline" in reason for _, reason in reasons())
    with open(
        os.path.join(ROOT, "skills", "verify", "orchestration.md"), encoding="utf-8"
    ) as f:
        skill = " ".join(f.read().split())
    said = (
        f"{NUMBER_WORDS[scripts + inline].capitalize()} steps of AgenticSeal's own "
        f"`release` job have a local answer and no arm: {NUMBER_WORDS[scripts]} "
        f"{'runs' if scripts == 1 else 'run'} a script under `.github/scripts/`, "
        f"which no plugin ships, and {NUMBER_WORDS[inline]} is shell written "
        "inline in the workflow"
    )
    assert said in skill, said


def test_a_step_a_row_excludes_is_still_pointed_at_its_reason():
    """The other half of `tests/skills/test_broad_gate.py`'s
    `test_a_step_no_row_classifies_is_not_said_to_carry_a_reason`, and what
    keeps that case from being answered by deleting the pointer. A step the
    partition DOES exclude carries a written reason, and naming where it is
    written is the whole of `frame/design.md` *Scope* 5."""
    said = gate.coverage_line(read(HYGIENE), "base")
    assert "no arm mirrors it in `broad_gate.py#PARTITION`" in said, said
    assert "both READMEs move together" in said.split("no arm mirrors it in", 1)[1]
    assert "no row of `broad_gate.py#PARTITION` at all" not in said, said


# --- no mirrored step skips a pull request into `main` ---------------------

# A step's shell guard that ends it on a pull request into `main`, as
# `hygiene.yml` would write it: the test, then an `exit 0` before its `fi`.
SKIPS_AT_MAIN = re.compile(
    r'if \[ "\$\{\{ github\.base_ref \}\}" = "main" \]; then\n'
    r"(?:(?!\s*fi\b).*\n)*?.*\bexit 0\b"
)


def step_text(text, name):
    """The lines of the step called `name`, from its `- name:` line to the
    next step's, as one string."""
    lines = text.splitlines(keepends=True)
    start = next(i for i, line in enumerate(lines) if line.strip() == f"- name: {name}")
    end = next(
        (
            i
            for i in range(start + 1, len(lines))
            if lines[i].lstrip().startswith("- ")
            and len(lines[i]) - len(lines[i].lstrip())
            == len(lines[start]) - len(lines[start].lstrip())
        ),
        len(lines),
    )
    return "".join(lines[start:end])


def mirrored_steps_skipping_at_main(text):
    """The mirrored `release` steps whose `run:` exits on a pull request
    into `main`."""
    return {
        name
        for name, arm, _ in gate.PARTITION
        if arm and SKIPS_AT_MAIN.search(step_text(text, name))
    }


def test_every_mirrored_step_runs_at_every_base():
    """The gate runs every arm at every base, so a mirrored step CI skips at
    `main` would be a step the release seal answers and CI does not ask. None
    does; the reader is shown able to find one by planting a guard in a copy
    of the workflow."""
    text = read(HYGIENE)
    assert mirrored_steps_skipping_at_main(text) == set()
    name = "a declared review chain has the round record it claimed"
    step = step_text(text, name)
    guard = 'if [ "${{ github.base_ref }}" = "main" ]; then\n  exit 0\nfi\n'
    planted = text.replace(step, step.replace("run: |\n", "run: |\n" + guard, 1))
    assert planted != text, "the plant did not land"
    assert mirrored_steps_skipping_at_main(planted) == {name}


# --- #666: the count is over the steps CI runs for this base ---------------

# A step's shell guard that ends it on any pull request NOT into `main`, as
# `hygiene.yml` writes it — `SKIPS_AT_MAIN`'s twin, with `!=`.
RUNS_ONLY_AT_MAIN = re.compile(
    r'if \[ "\$\{\{ github\.base_ref \}\}" != "main" \]; then\n'
    r"(?:(?!\s*fi\b).*\n)*?.*\bexit 0\b"
)


def steps_guarded_off_main(text):
    """The `release` steps whose `run:` exits on a base that is not `main`."""
    return {
        name
        for name in gate.job_steps(text, gate.RELEASE_JOB)
        if RUNS_ONLY_AT_MAIN.search(workflow_step(text, name))
    }


def test_the_steps_left_out_off_main_are_the_steps_guarded_off_main():
    """A13. `ONLY_AT_MAIN` is exactly the set of `release` steps whose guard
    ends them on any base but `main`, from both sides — and the comparison is
    shown able to fail on a copy of the workflow with one guard turned
    around, so a guard added to a fourth step, or dropped from one of the
    three, fails here."""
    text = read(HYGIENE)
    guarded = steps_guarded_off_main(text)
    assert guarded, "no step is guarded off main, so the reader found nothing"
    assert guarded == set(gate.ONLY_AT_MAIN), (
        f"the workflow guards these steps off `main`: {sorted(guarded)}, and "
        f"`ONLY_AT_MAIN` holds {sorted(gate.ONLY_AT_MAIN)}"
    )
    assert len(gate.ONLY_AT_MAIN) == len(set(gate.ONLY_AT_MAIN)) == 3
    flipped = text.replace('" != "main" ]', '" = "main" ]', 1)
    assert flipped != text and steps_guarded_off_main(flipped) != set(
        gate.ONLY_AT_MAIN
    ), "turning one guard around did not move the reader"


FEATURE_UNANSWERED = (
    "every issue this pull request claims, and every one it only names",
    "both READMEs move together",
)


def real_panel_workflow_row(given):
    checks = {
        name: gate.Check(name, 0, "", "") for name in (gate.SUITE, gate.CHAIN_NAME)
    }
    base = gate.Base(given, "cccccccc", given, "cccccccc")
    rows = gate.panel("ccccccc", base, checks, None, read(HYGIENE))
    return next(value for label, value in [r for r in rows if r] if label == "CI also")


def test_a_feature_seal_counts_the_steps_ci_runs_for_it():
    """A11 over this repository's own workflow. Against a base that is not
    `main` CI runs 4 of the 7 steps and the gate mirrors 2, so the panel
    reads `CI also · 2 more steps`; the line names the two unanswered steps
    CI runs and none of the three only-at-`main` ones, and says three were
    left out and why. Pinned verbatim (contract rule 14). The ninth step,
    the CLAUDE.md copy held to its template, left with the copy (#940), and
    the unverified record's step and its arm left together (#945)."""
    assert gate.steps_for(read(HYGIENE), "release/x") == [
        step
        for step in gate.job_steps(read(HYGIENE), gate.RELEASE_JOB)
        if step not in gate.ONLY_AT_MAIN
    ]
    assert real_panel_workflow_row("release/x") == "· 2 more steps"
    said = gate.coverage_line(read(HYGIENE), "release/x")
    assert said.startswith(
        f"seal gate: {gate.WORKFLOW}'s `release` job runs 4 steps for this base "
        "and this run answers 2. 3 more run only on a pull request into `main`, "
        "so this count leaves them out."
    ), said
    for step in FEATURE_UNANSWERED:
        assert step in said, step
    for step in gate.ONLY_AT_MAIN:
        assert step not in said, step


def test_a_release_seal_counts_every_step_ci_runs_for_it():
    """A12. Against `main` CI runs every one of the 7 steps and the gate
    mirrors 2, so the panel reads `CI also · 5 more steps` and the line
    leaves no step out."""
    for given in ("main", "origin/main"):
        assert real_panel_workflow_row(given) == "· 5 more steps", given
        said = gate.coverage_line(read(HYGIENE), given)
        assert said.startswith(
            f"seal gate: {gate.WORKFLOW}'s `release` job runs 7 steps for this "
            "base and this run answers 2."
        ), said
        assert "leaves" not in said.split("Not answered", 1)[0], said
        for step in gate.ONLY_AT_MAIN:
            assert step in said, step


def test_the_documents_say_the_count_is_over_the_steps_ci_runs():
    """S5's documentation (contract rule 14): the skill section that
    explains the count and the partition's policy paragraph each say a step
    CI does not run for the base is outside the count. Since #969 the sealer
    sees no output of the gate's and explains none of it, so its definition
    is not asked."""
    verify = " ".join(
        read(os.path.join(ROOT, "skills", "verify", "orchestration.md")).split()
    )
    assert "counted over the steps CI runs for the base" in verify
    broad = " ".join(read(os.path.join(ROOT, "docs", "the-broad-gate.md")).split())
    assert "A step CI does not run for the base is neither answered nor unanswered" in (
        broad
    )
