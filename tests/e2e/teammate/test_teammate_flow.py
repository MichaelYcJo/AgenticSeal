"""The teammate flow: a pull request that declares nothing passes every step
of `templates/setup/hygiene.yml` (#952).

A consuming repository that installed the pull-request checks runs them on
every pull request, a teammate's who never used the plugin among them. Each
case builds such a repository on one of four bases, puts a teammate's branch
on it that changes `README.md` alone, and runs every `run:` block of the
template under `bash`, its text unchanged apart from GitHub's expression for
the base branch. A second case runs the same steps on the pull request that
moves the root to local mode with the checks kept. The plugin's clone is the
one step not run: the tree under test stands where the clone puts it,
`$RUNNER_TEMP/agentic`. The oracle is each step's exit code, never what a
step printed.
"""

import json
import os
import shutil
import subprocess
import sys
import textwrap

import pytest
from conftest import (
    ROOT,
    census_case,
    commit_everything_as_e,
    git,
    mark_root,
    symlink_or_skip,
    workflow_steps,
    write,
)

TARGET = "templates/setup/hygiene.yml"

BASH = shutil.which("bash")
pytestmark = [pytest.mark.skipif(BASH is None, reason="no bash to run the steps in")]

BASE = "main"
BRANCH = "teammate"
SWITCH = "to-local"
SEAL = os.path.join(ROOT, "skills", "implement", "scripts", "seal.py")
# The one expression the template's `run:` blocks carry, and what GitHub
# puts in its place for a pull request into BASE.
BASE_REF = "${{ github.base_ref }}"
CLONE = "git clone"

WORK = "1790000000-work"
CONFIG = "# Repository config\n\n| Item | Value |\n|---|---|\n| Mode | shared |\n"
ROUTING = f"""# Routing: {WORK}

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | the session |
| Implementation | the session |
| Automation | no |
| Answer pressed | per axis |
| Branch | feat/work |

Answered 2026-01-01 by the owner, before the first edit.
"""
SPEC = "# Feature Specification: a work item\n\nA rule.\n"
OVERVIEW = """# Overview: a work item

One line of purpose.

## Not verified

| Item | Who must answer |
|---|---|
| how the gate renders in a TUI | the repository owner |
"""
# A round record in the labelled lines of the releases before #1198, as a
# work item released before it leaves one on a base. The teammate's pull
# request declares and changes no work item, so the check reads no record of
# the base, in either shape.
ROUND = f"""# Review round 1: {WORK}

target: 1a2b3c4 against main

## Findings

none
"""

ITEM = f"seal/threads/{WORK}"
OPEN_ROW_AND_ROUND = "a work item with an open row and a round record"
BASES = {
    "no root": {},
    "a root holding only its config": {"seal/config.md": CONFIG},
    "a work item with no overview": {
        "seal/config.md": CONFIG,
        f"{ITEM}/routing.md": ROUTING,
        f"{ITEM}/frame/design.md": SPEC,
    },
    OPEN_ROW_AND_ROUND: {
        "seal/config.md": CONFIG,
        f"{ITEM}/routing.md": ROUTING,
        f"{ITEM}/frame/design.md": SPEC,
        f"{ITEM}/gaps.md": OVERVIEW,
        f"{ITEM}/trail/rounds/round-1.md": ROUND,
    },
}


def run_blocks(text):
    """`(step name, script)` for every step of TEXT that has a `run: |`
    block, the script dedented as the runner hands it to the shell."""
    out = []
    for name, block in workflow_steps(text):
        lines = block.split("\n")
        at = [i for i, line in enumerate(lines) if line.strip() == "run: |"]
        if not at:
            continue
        assert len(at) == 1, f"{name!r} has {len(at)} `run: |` lines"
        floor = len(lines[at[0]]) - len(lines[at[0]].lstrip(" "))
        body = []
        for line in lines[at[0] + 1 :]:
            if line.strip() and len(line) - len(line.lstrip(" ")) <= floor:
                break
            body.append(line)
        out.append((name, textwrap.dedent("\n".join(body)).strip("\n") + "\n"))
    return out


def without_this_run(environ):
    """ENVIRON less the git and runner variables of the run this suite is
    in."""
    return {k: v for k, v in environ.items() if not k.startswith(("GIT_", "RUNNER_"))}


def seal(repo, *argv):
    """`seal <argv>` from the tree under test, run in REPO; it has to exit 0."""
    ran = subprocess.run(
        [sys.executable, SEAL, *argv],
        cwd=repo,
        env=without_this_run(os.environ),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=120,
    )
    assert ran.returncode == 0, f"seal {' '.join(argv)}: {ran.stdout}{ran.stderr}"


def base_repository(tmp_path, files, checks=False):
    """A repository whose `main` holds FILES and a README, reachable as
    `origin/main`; where CHECKS, `seal pr-checks install` wrote the plugin's
    workflow into the same commit."""
    d = tmp_path / "repo"
    d.mkdir()
    git(d, "init", "-q", "-b", BASE)
    write(d, "README.md", "# a project\n")
    for rel, text in files.items():
        write(d, rel, text)
    if (d / "seal").is_dir():
        mark_root(d / "seal")
    if checks:
        seal(d, "pr-checks", "install")
    commit_everything_as_e(d, "the base")
    git(d, "update-ref", f"refs/remotes/origin/{BASE}", BASE)
    return d


def teammate_repository(tmp_path, files):
    """`base_repository` on FILES, with the teammate's branch on it changing
    the README."""
    d = base_repository(tmp_path, files)
    git(d, "switch", "-qc", BRANCH)
    write(d, "README.md", "# a project\n\nA sentence a teammate added.\n")
    commit_everything_as_e(d, "a teammate edits the README")
    return d


def switching_repository(tmp_path):
    """`base_repository` on the base with an open row and a round record and
    the plugin's workflow, with a branch whose one commit is what
    `seal mode local` staged. The local root is moved aside afterwards, as a
    checkout in CI holds none."""
    d = base_repository(tmp_path, BASES[OPEN_ROW_AND_ROUND], checks=True)
    git(d, "switch", "-qc", SWITCH)
    seal(d, "mode", "local")
    commit_everything_as_e(d, "the switch to local")
    common = git(d, "rev-parse", "--path-format=absolute", "--git-common-dir")
    os.rename(os.path.join(common.stdout.strip(), "seal"), tmp_path / "local-root")
    return d


def runner_env(tmp_path, branch=BRANCH):
    """The variables GitHub sets for a pull request from BRANCH into BASE
    that is not a draft, with `$RUNNER_TEMP/agentic` resolving to the tree
    under test, and none of the variables of the run this suite is in."""
    runner = tmp_path / "runner"
    runner.mkdir()
    symlink_or_skip(ROOT, runner / "agentic")
    event = tmp_path / "event.json"
    event.write_text(json.dumps({"pull_request": {"draft": False}}), encoding="utf-8")
    env = without_this_run(os.environ)
    env.update(
        RUNNER_TEMP=str(runner),
        GITHUB_ACTIONS="true",
        GITHUB_BASE_REF=BASE,
        GITHUB_HEAD_REF=branch,
        GITHUB_EVENT_NAME="pull_request",
        GITHUB_EVENT_PATH=str(event),
    )
    # The steps name `python3`, which `ubuntu-latest`, the runner the
    # template pins, always has. Asked by trying, as `symlink_or_skip` asks.
    found = subprocess.run(
        [BASH, "-c", "command -v python3"], env=env, capture_output=True
    )
    if found.returncode != 0:
        pytest.skip("bash finds no `python3` here, and every step names it")
    return env


def template():
    with open(os.path.join(ROOT, *TARGET.split("/")), encoding="utf-8") as handle:
        return handle.read()


def steps_to_run(text):
    """Every `run:` block of TEXT but the clone, which has to be the one step
    holding `git clone`: a second such step cannot run offline, and it fails
    the case rather than being skipped."""
    blocks = run_blocks(text)
    clones = [name for name, script in blocks if CLONE in script]
    assert len(clones) == 1, f"{len(clones)} steps hold {CLONE!r}: {clones}"
    return [(name, script) for name, script in blocks if CLONE not in script]


def failed_steps(repo, env):
    """Every step of the template that exited non-zero in REPO under ENV,
    with what it printed."""
    steps = steps_to_run(template())
    assert steps, "the template has no step to run"
    failed = []
    for name, script in steps:
        ran = subprocess.run(
            [BASH, "-e", "-c", script.replace(BASE_REF, BASE)],
            cwd=repo,
            env=env,
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
        )
        if ran.returncode != 0:
            failed.append(f"{name}: exit {ran.returncode}\n{ran.stdout}{ran.stderr}")
    return failed


class Test_a_pull_request_that_declares_nothing_owes_nothing:
    """S1: on each of the four bases, a pull request changing `README.md`
    alone passes every step the template runs, and so does the pull request
    that moves the root to local mode with the checks kept."""

    @pytest.mark.rule("nothing-declared-nothing-owed")
    @pytest.mark.parametrize("base", sorted(BASES))
    def test_accepts_a_teammates_pull_request_on_every_base(self, tmp_path, base):
        repo = teammate_repository(tmp_path, BASES[base])
        failed = failed_steps(repo, runner_env(tmp_path))
        assert not failed, "\n\n".join(failed)

    @pytest.mark.rule("nothing-declared-nothing-owed")
    def test_accepts_the_pull_request_that_moves_the_root_to_local_mode(self, tmp_path):
        """Round 1 of #952, finding 1: the switch deletes every `routing.md`
        with the root, and with no root at HEAD nothing is declared."""
        repo = switching_repository(tmp_path)
        assert not (repo / "seal").exists()
        failed = failed_steps(repo, runner_env(tmp_path, SWITCH))
        assert not failed, "\n\n".join(failed)

    def test_refuses_a_template_whose_second_step_needs_the_network(self):
        """A step holding `git clone` beside the plugin's own is refused by
        the count, not skipped."""
        doubled = template() + (
            "\n"
            "      - name: a second clone\n"
            "        shell: bash\n"
            "        run: |\n"
            "          git clone https://example.com/x.git x\n"
        )
        with pytest.raises(AssertionError, match="2 steps hold 'git clone'"):
            steps_to_run(doubled)


test_census = census_case(TARGET)
