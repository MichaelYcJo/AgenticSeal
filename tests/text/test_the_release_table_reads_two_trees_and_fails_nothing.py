"""The release table's job runs after the suite, into `main` alone, over the
last release tag's whole tree.

#923 item 3: what a release reads release to release is one table on the
release pull request, printed by `.github/scripts/release_report.py`; the
tests workflow's `release-report` job runs it after the suite, on a pull
request into `main` only. The script's cases stand in
`tests/github/test_release_report.py`; the cases here read the workflow.
"""

import os

from conftest import census_case, code_lines
from workflows import load

TARGET = ".github/workflows/test.yml"

WORKFLOW = os.path.join(*TARGET.split("/"))


def release_report():
    """The tests workflow's `release-report` job, loaded."""
    return load(WORKFLOW)["jobs"]["release-report"]


def scripts(job):
    """JOB's `run:` scripts, joined, each with its shell comments off."""
    return "\n".join(
        "\n".join(code_lines(step["run"])) for step in job["steps"] if "run" in step
    )


def test_the_tests_workflow_prints_the_table_only_into_main_after_the_suite():
    """S9's job: after the suite and the union whatever their verdicts, on a
    pull request into `main` alone, with the whole history to find the tag
    in, and its output appended to the step summary."""
    job = release_report()
    assert job["needs"] == ["pytest", "durations"], job["needs"]
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
    # The step's command and its redirection into the step summary, which
    # the runner runs.
    assert "python .github/scripts/release_report.py" in script, script
    assert '>> "$GITHUB_STEP_SUMMARY"' in script, script


def test_the_table_reads_the_last_tag_s_whole_tree():
    """`--at` is the tag's tree checked out whole: `release_report.py` reads
    `CLAUDE.md` there, and an archive of the tag leaves out every path
    `.gitattributes` marks `export-ignore`."""
    script = scripts(release_report())
    # The step's command that checks the tag's whole tree out.
    assert 'git worktree add --detach "$RUNNER_TEMP/at" "$tag"' in script, script


def test_the_table_reads_this_run_s_union_and_the_tag_s_push_run_s():
    """S5 of #1486: the unions are run artifacts, not tree files. This run's
    comes from the `durations` job's `test-durations` artifact, and a step
    that finds none goes on, since a refused union uploads nothing. The tag's
    comes from the push run the job lists are read from, and a download that
    finds none goes on as well. The script reads each as `--durations` and
    `--durations-at`, an absent one as no reading."""
    job = release_report()
    (download,) = [
        step
        for step in job["steps"]
        if step.get("uses", "").startswith("actions/download-artifact@")
    ]
    assert download["with"].get("name") == "test-durations", download
    assert download["with"].get("path") == "${{ runner.temp }}/durations", download
    assert download.get("continue-on-error") == "true", download
    script = scripts(job)
    # The command that downloads the tag's union and goes on where there is
    # none, which the runner runs.
    assert (
        'gh run download "$run" -n test-durations -D "$RUNNER_TEMP/durations-at"'
        " || true"
    ) in script, script
    # The two flags of the script's command with the paths the unions are
    # downloaded to, which the runner hands `release_report.py`.
    assert '--durations "$RUNNER_TEMP/durations/.test_durations"' in script, script
    assert '--durations-at "$RUNNER_TEMP/durations-at/.test_durations"' in script, (
        script
    )


test_census = census_case(TARGET)
