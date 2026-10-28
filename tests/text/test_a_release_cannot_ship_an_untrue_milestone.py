"""What is left of the release completeness gate's old file: the cases
that read the hygiene workflow's step, and the case that holds the module
docstring and this file's input boundary to each other, which wait for #923.

#942's phase 6 placed the cases of
`.github/scripts/release_completeness_check.py`'s functions in
`tests/github/test_release_completeness_check.py`.
"""

import os
import re

from conftest import ROOT, read

SCRIPT = os.path.join(ROOT, ".github", "scripts", "release_completeness_check.py")
HYGIENE = os.path.join(ROOT, ".github", "workflows", "hygiene.yml")


def hygiene_step():
    """The gate's step, from `- name:` to the next one at the same indent."""
    text = read(HYGIENE)
    start = text.index("- name: the milestone this release claims")
    rest = text[start + 1 :]
    end = rest.find("\n      - name:")
    return rest[: end if end != -1 else len(rest)]


def test_the_gate_runs_only_for_a_release_pull_request():
    """It is the fifth release-only step in this file. A feature pull request
    carries no milestone of its own and the release branch it targets is not
    finished, so running it there is noise at best."""
    step = hygiene_step()
    assert 'github.base_ref }}" != "main" ]' in step, (
        "the step is missing the base guard the other release-only steps use"
    )
    # The whole guard, in order, not only its condition. A mutation that
    # deleted the `exit 0` and the `fi` — leaving `if …; then` with the run
    # below it — passed a check that asserted the condition alone, and that
    # step both runs on every pull request and is malformed shell.
    guard = re.search(
        r'if \[ "\$\{\{ github\.base_ref \}\}" != "main" \]; then\n'
        r"(.*?)\n\s*fi\n\s*python3 \.github/scripts/release_completeness_check\.py",
        step,
        re.S,
    )
    assert guard, (
        "the guard is not a closed `if … fi` with the script after it, so "
        f"either it does not skip or it does not run:\n{step}"
    )
    assert "exit 0" in guard.group(1), (
        "the guard's body does not exit, so a feature pull request falls "
        "through into the check"
    )


def test_the_head_shape_reaches_the_script_rather_than_the_guard():
    """A hotfix branch merging into `main` is the other shape that gets here,
    and what it does about that is a case (S7) rather than a shell condition
    nothing can test."""
    step = hygiene_step()
    assert "HEAD_BRANCH: ${{ github.head_ref }}" in step, (
        "the head branch does not reach the script, so the skip it is "
        "supposed to make is unreachable"
    )


def test_every_input_the_script_reads_is_handed_to_it_by_the_step():
    """Round 1, finding 6, and the fix for finding 2 is what earns it.

    The round judged this a note rather than a fix: deleting `REPO` from the
    step is a loud `KeyError` at the release pull request, and deleting `BASE`
    is harmless because the script's default is what a release pull request
    wants anyway. Both true.

    `HEAD_SHA` is neither. Losing it falls back to `HEAD`, which in CI is the
    merge ref — so the step goes green, the range silently collapses to the
    spelling `questions.md` Q8 rejected, and finding 2 is back with nothing
    saying so. `HEAD_BRANCH` is silent the same way: `version_of("")` takes
    the hotfix skip and borrows its log line (#362). A silent entry in the
    block is what turns the note into a case, and the case covers every entry
    rather than the silent ones, because a reader deleting a line does not
    first ask which kind it is.

    The boundary is what the step must pass — `GH_TOKEN` included, which
    reaches the script through `gh` rather than through `os.environ`.
    Measured one entry removed at a time against a fixture branch name, exit
    codes read directly: `REPO` 1 (`KeyError`), `HEAD_SHA` 0 (silent),
    `HEAD_BRANCH` 0 (the *not a release branch* line), `BASE` 0 (the
    default), `GH_TOKEN` 1 (`gh` fails). The module docstring carries the
    same table, and the case below holds the two texts to each other.
    """
    env = hygiene_step().split("shell:")[0]
    for name in ("GH_TOKEN", "HEAD_BRANCH", "HEAD_SHA", "BASE", "REPO"):
        assert f"{name}:" in env, (
            f"the gate step no longer passes {name}. Every one of these is "
            "an input of `release_completeness_check.py`, and two absences "
            "are silent"
        )
    assert "github.event.pull_request.head.sha" in env, (
        "HEAD_SHA no longer names the pull request's own head commit, so the "
        "fork point is measured against whatever the checkout left at HEAD"
    )


def test_the_script_and_this_file_draw_the_input_boundary_the_same_way():
    """#362. The module docstring said `HEAD_SHA` is *the one entry whose
    absence is silent* and named four inputs; the case above loops over five
    and repeated the superlative. Measured one input removed at a time, two
    absences are silent (`HEAD_SHA`, `HEAD_BRANCH`), so the superlative was
    false, and a count rots the next time an input is added. Both places now
    say the boundary is what the step must pass and carry the measured table
    instead of a count — this reads the two texts for the superlative and for
    the five names, so the next edit to one has to reach the other."""
    # Whitespace collapsed, because both texts wrap: the superlative sat
    # across a line break, and a substring check on the raw text missed it.
    module = " ".join(read(SCRIPT).split('"""')[1].split())
    this = read(os.path.abspath(__file__))
    here = this[
        this.index(
            "def test_every_input_the_script_reads_is_handed_to_it_by_the_step"
        ) :
    ]
    here = " ".join(here.split('"""')[1].split())
    for name, text in (
        ("the module docstring", module),
        ("the case's docstring", here),
    ):
        assert "the one entry whose absence is silent" not in text, (
            f"{name} says one absence is silent; two are, measured"
        )
        assert "the step must pass" in text, (
            f"{name} does not say which boundary it draws"
        )
        for env in ("GH_TOKEN", "HEAD_BRANCH", "HEAD_SHA", "BASE", "REPO"):
            assert f"`{env}`" in text, f"{name} does not name {env}"


def test_the_job_asks_for_a_token_that_can_read_issues():
    """`hygiene.yml` declared no `permissions:` block and used no `gh` before
    this step, so it ran on whatever an enterprise, organisation or repository
    default happened to be. The gate writes nothing, so the block is
    read-only in both scopes — narrower than any default, and stated rather
    than inherited."""
    text = "\n".join(
        line for line in read(HYGIENE).splitlines() if not line.lstrip().startswith("#")
    )
    block = re.search(r"^permissions:\n((?:  [\w-]+:.*\n)+)", text, re.M)
    assert block, "hygiene.yml states no permissions block, so it inherits a default"
    granted = dict(re.findall(r"^  ([\w-]+):\s*(\S+)\s*$", block.group(1), re.M))
    assert granted == {"contents": "read", "issues": "read"}, (
        f"the token's scopes changed: {granted}. Every step in this job reads "
        "and none of them writes"
    )
    assert "GH_TOKEN: ${{ github.token }}" in hygiene_step(), (
        "the step does not pass a token, so `gh` falls back to whatever the "
        "runner happens to have"
    )
