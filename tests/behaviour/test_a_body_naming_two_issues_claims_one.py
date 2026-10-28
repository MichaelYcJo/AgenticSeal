"""What is left of the claims check's old file: the cases that read
`docs/issues-and-milestones.md`, the hygiene workflow and its template, which
wait for #923.

#942's phase 6 placed the cases of `.github/scripts/issue_claims_check.py`'s
functions in `tests/github/test_issue_claims_check.py`. The document's case reads it
through that file's `read`. `docs/issues-and-milestones.md` names this file
on a `check:` line beside the new one.
"""

import os

import pytest
from conftest import ROOT, step_running
from test_issue_claims_check import read


def test_the_document_that_teaches_the_rule_carries_no_instance_of_it():
    """`docs/issues-and-milestones.md` says a body quoting the failing shape
    inside a fence or a code span is not an instance of it. This repository's
    bodies quote its documents routinely, so the section has to hold to that
    everywhere -- a narrative past-tense keyword is still a keyword, and
    `KEYWORDS` carries the past tense of all three verbs."""
    with open(
        os.path.join(ROOT, "docs", "issues-and-milestones.md"), encoding="utf-8"
    ) as f:
        _, _, warnings = read(f.read())
    assert warnings == [], warnings[0][2] if warnings else ""


def test_the_workflow_runs_the_check_on_every_pull_request():
    """A check nothing calls is the standing waiver this repository refuses to
    build. It goes in the job that already runs on every pull request, so it
    needs no trigger and no token of its own."""
    with open(
        os.path.join(ROOT, ".github", "workflows", "hygiene.yml"), encoding="utf-8"
    ) as f:
        workflow = f.read()
    assert "issue_claims_check.py" in workflow
    assert os.path.isfile(
        os.path.join(ROOT, ".github", "scripts", "issue_claims_check.py")
    )


def test_the_body_reaches_the_script_through_the_environment():
    """A pull request body is attacker-controlled text and `${{ }}` inside a
    `run:` block is textual substitution into a shell script. Interpolating a
    body there hands whoever opens the pull request the runner."""
    with open(
        os.path.join(ROOT, ".github", "workflows", "hygiene.yml"), encoding="utf-8"
    ) as f:
        workflow = f.read()
    step = step_running(workflow, "issue_claims_check.py")
    assert "PR_BODY: ${{ github.event.pull_request.body }}" in step
    assert "${{ github.event.pull_request.body }}" not in workflow.split("run:")[-1], (
        "the body is interpolated into a shell line"
    )


@pytest.mark.parametrize("stays_home", ["issue_claims_check"])
def test_the_check_does_not_travel_to_user_repositories(stays_home):
    """`.github/scripts/` is this repository's own automation, the way
    `gather_changelog` and `fold_ledger` are — `test_first_setup_asks_once.py`
    pins those two the same way. Shipping this one means first deciding it
    belongs under `skills/`, which is a wider change than this issue asks
    for."""
    with open(
        os.path.join(ROOT, "templates", "setup", "hygiene.yml"), encoding="utf-8"
    ) as f:
        assert stays_home not in f.read()
