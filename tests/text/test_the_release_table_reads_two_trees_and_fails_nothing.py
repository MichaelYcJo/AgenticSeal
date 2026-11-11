"""The release table's job runs after the suite, into `main` alone, over the
last release tag's whole tree.

#923 item 3: what a release reads release to release is one table on the
release pull request, printed by `.github/scripts/release_report.py`; the
tests workflow's `release-report` job runs it after the suite, on a pull
request into `main` only. #942's phase 6 placed the script's cases in
`tests/github/test_release_report.py`; the cases that read the workflow stay
here.
"""

import os

from conftest import code_lines
from workflows import load

WORKFLOW = os.path.join(".github", "workflows", "test.yml")


def release_report():
    """The tests workflow's `release-report` job, loaded."""
    return load(WORKFLOW)["jobs"]["release-report"]


def scripts(job):
    """JOB's `run:` scripts, joined, each with its shell comments off."""
    return "\n".join(
        "\n".join(code_lines(step["run"])) for step in job["steps"] if "run" in step
    )


def test_the_tests_workflow_prints_the_table_only_into_main_after_the_suite():
    """S9's job: after the suite whatever its verdict, on a pull request into
    `main` alone, with the whole history to find the tag in, and its output
    appended to the step summary."""
    job = release_report()
    assert job["needs"] == "pytest", job["needs"]
    assert job["if"] == "${{ !cancelled() && github.base_ref == 'main' }}", job["if"]
    checkouts = [
        step
        for step in job["steps"]
        if step.get("uses", "").startswith("actions/checkout")
    ]
    assert [step.get("with", {}).get("fetch-depth") for step in checkouts] == ["0"], (
        checkouts
    )
    script = scripts(job)
    assert "python .github/scripts/release_report.py" in script, script
    assert '>> "$GITHUB_STEP_SUMMARY"' in script, script


def test_the_table_reads_the_last_tag_s_whole_tree():
    """`--at` is the tag's tree checked out whole: `release_report.py` reads
    `.test_durations` and `CLAUDE.md` there, and an archive of the tag leaves
    out every path `.gitattributes` marks `export-ignore`."""
    script = scripts(release_report())
    assert 'git worktree add --detach "$RUNNER_TEMP/at" "$tag"' in script, script
    assert "git archive" not in script, script
