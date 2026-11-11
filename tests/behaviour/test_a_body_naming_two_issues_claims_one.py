"""What is left of the claims check's old file: the cases that read the
hygiene workflow.

The cases of `.github/scripts/issue_claims_check.py`'s functions stand in
`tests/github/test_issue_claims_check.py`, and its `Test_read` holds the case
that runs the reader over `docs/releasing/issues-and-milestones.md`. That
document names this file on a `check:` line beside the module's file.
"""

import os

from conftest import ROOT, code_lines
from workflows import load


def test_the_workflow_runs_the_check_on_every_pull_request():
    """A check nothing calls is the standing waiver this repository refuses to
    build. It goes in the job that already runs on every pull request, so it
    needs no trigger and no token of its own."""
    with open(
        os.path.join(ROOT, ".github", "workflows", "hygiene.yml"), encoding="utf-8"
    ) as f:
        workflow = f.read()
    # The script `issue_claims_check.py`, which a step of the workflow runs
    # on every pull request.
    assert "issue_claims_check.py" in workflow
    assert os.path.isfile(
        os.path.join(ROOT, ".github", "scripts", "issue_claims_check.py")
    )


BODY = "${{ github.event.pull_request.body }}"


def test_the_body_reaches_the_script_through_the_environment():
    """A pull request body is attacker-controlled text and `${{ }}` inside a
    `run:` block is textual substitution into a shell script. Interpolating a
    body there hands whoever opens the pull request the runner, so no step's
    script holds the expression."""
    workflow = load(os.path.join(".github", "workflows", "hygiene.yml"))
    steps = [step for job in workflow["jobs"].values() for step in job["steps"]]
    running = [
        step
        for step in steps
        if "issue_claims_check.py" in "\n".join(code_lines(step.get("run", "")))
    ]
    assert len(running) == 1, f"{len(running)} steps run issue_claims_check.py"
    assert running[0].get("env", {}).get("PR_BODY") == BODY, running[0]
    interpolated = [step.get("name") for step in steps if BODY in step.get("run", "")]
    assert not interpolated, (
        f"the body is interpolated into a shell line: {interpolated}"
    )
