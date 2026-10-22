"""Local mode reaches the review chain: the pull-request check says which
root it searched (#225).

A local-mode declaration sits at `<git-common-dir>/seal/specs/<item>/
routing.md`, and nothing there is committed. The check reads what git
carries, so it examines nothing either way; what it says is which root it
searched, so a repository in local mode is not told to write a file it
already has.
"""

import os
import subprocess
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CHECK = os.path.join(ROOT, "skills", "code-review", "scripts", "chain_check.py")
ITEM_ID = "1799000000-a-local-work-item"


def git(where, *args, check=True):
    return subprocess.run(
        ["git", "-C", str(where), *args],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        check=check,
    )


def _build(d):
    d.mkdir(parents=True)
    git(d, "init", "-q", "-b", "base")
    (d / "f.py").write_text("x = 1\n", encoding="utf-8")
    git(d, "add", "-A")
    git(d, "-c", "user.email=e@example.com", "-c", "user.name=e", "commit", "-qm", "b")
    git(d, "switch", "-qc", "feature")


@pytest.fixture(scope="session")
def _repo_template(tmp_path_factory):
    """The module's fixture repository, built once; `tests/conftest.py#repo`
    copies it for each case."""
    d = tmp_path_factory.mktemp("local-mode-template") / "repo"
    _build(d)
    return d


def common_dir(where):
    """The clone's common git directory, absolute — asked of git, never
    spelled `.git`, which is a FILE in a linked worktree."""
    out = git(where, "rev-parse", "--git-common-dir").stdout.strip()
    return os.path.normpath(os.path.join(str(where), out))


def local_item(repo, item=ITEM_ID, branch="feature"):
    """A work item under the LOCAL root, with a declaration naming `branch`."""
    d = os.path.join(common_dir(repo), "seal", "specs", item)
    os.makedirs(os.path.join(d, "rounds"), exist_ok=True)
    with open(os.path.join(d, "routing.md"), "w", encoding="utf-8") as f:
        f.write(
            f"# {item} — routing\n\n"
            "| Axis | Answer |\n|---|---|\n"
            "| Review | through the review chain |\n"
            "| Destination | open the pull request |\n"
            f"| Branch | {branch} |\n"
        )
    return d


def run_check(repo, *extra):
    env = dict(os.environ)
    env.pop("GITHUB_EVENT_PATH", None)
    env.pop("GITHUB_HEAD_REF", None)
    r = subprocess.run(
        [
            sys.executable,
            CHECK,
            "--worktree",
            "--baseline",
            "HEAD",
            "--root",
            str(repo),
            *extra,
        ],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=120,
        cwd=str(repo),
        env=env,
    )
    return r.returncode, r.stdout + r.stderr


ADD_THE_FILE = "Add seal/specs/<work-item>/routing.md to declare"


def test_local_mode_is_told_it_is_local_mode(repo):
    """A local-mode repository is told the root it searched, not to write a
    file it already has."""
    local_item(repo)
    code, out = run_check(repo)
    assert code == 0, out
    assert ADD_THE_FILE not in out, out
    assert "local mode" in out, out
    assert os.path.normpath(os.path.join(common_dir(repo), "seal")) in out, out
    assert "seal mode shared" in out, out


def test_local_mode_still_examines_nothing(repo):
    """Naming the root does not turn an untracked declaration into a checked
    one: CI reads what git carries, and local mode commits nothing."""
    local_item(repo)
    _code, out = run_check(repo)
    assert "examined nothing" in out, out
    assert "through the review chain" not in out, out


def test_shared_mode_is_still_told_to_add_the_file(repo):
    """A shared-mode repository with no declaration is told to write one."""
    (repo / "seal" / "specs").mkdir(parents=True)
    code, out = run_check(repo)
    assert code == 0, out
    assert ADD_THE_FILE in out, out
    assert "local mode" not in out, out


def test_the_shared_sentence_says_what_it_searched_and_for_what(repo):
    """The prefix and the branch are what make the sentence checkable."""
    (repo / "seal" / "specs").mkdir(parents=True)
    _code, out = run_check(repo)
    assert "under `seal/specs/`" in out, out
    assert "declares `feature`" in out, out


def test_a_repository_with_no_root_is_told_to_add_the_file(repo):
    """With no root to name, the file to write is the answer."""
    code, out = run_check(repo)
    assert code == 0, out
    assert ADD_THE_FILE in out, out
    assert "local mode" not in out, out
