"""The release table's job runs after the suite, into `main` alone.

#923 item 3: what a release reads release to release is one table on the
release pull request, printed by `.github/scripts/release_report.py`; the
tests workflow's `release-report` job runs it after the suite, on a pull
request into `main` only. #942's phase 6 placed the script's cases in
`tests/github/test_release_report.py`; the case that reads the workflow stays here
for #923.
"""

import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WORKFLOW = os.path.join(ROOT, ".github", "workflows", "test.yml")


def job_block(text, name):
    """The lines of one job of a workflow, its header through the next job."""
    found = re.search(rf"(?ms)^  {re.escape(name)}:\n(.*?)(?=^  \S|\Z)", text)
    assert found, f"no job `{name}` in the workflow"
    return found.group(1)


def test_the_tests_workflow_prints_the_table_only_into_main_after_the_suite():
    """S9's job: after the suite whatever its verdict, on a pull request into
    `main` alone, with the whole history to find the tag in, and its output
    appended to the step summary."""
    with open(WORKFLOW, encoding="utf-8") as handle:
        text = handle.read()
    code = "\n".join(
        line for line in text.splitlines() if not line.lstrip().startswith("#")
    )
    block = job_block(code, "release-report")
    assert "needs: pytest" in block, block
    assert "if: ${{ !cancelled() && github.base_ref == 'main' }}" in block, block
    assert "fetch-depth: 0" in block, block
    assert "python .github/scripts/release_report.py" in block, block
    assert '>> "$GITHUB_STEP_SUMMARY"' in block, block
