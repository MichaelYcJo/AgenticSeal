"""`hooks/gate.py`, the commit gate's one judgment, one class per function.

The arms and the refusals run through the hooks that render them: as git runs
them in the commit flow, `tests/e2e/commit/test_commit_flow.py`, and in the
process in `tests/test_commit_review_gate.py` and `tests/test_commitgate.py`.
The one case here came from `tests/test_chain_hooks_hardening.py` (#942's phase
6): the backstop's path reader hands `touches_code` None where `git diff` fails,
and None reads as code, in the `repo` fixture with a `git` that refuses `diff`.
"""

import os
import sys

import pytest
from conftest import a_git_whose_diff_fails, census_case, git, stage

TARGET = "hooks/gate.py"


class Test_module:
    def test_the_backstop_hands_the_parity_arm_none_where_git_could_not_list(
        self, repo, tmp_path, monkeypatch
    ):
        """S10 of work item 1791384157 (#868), the backstop's path reader:
        `reference-transaction` lists what a commit past `--no-verify` carries
        with `git diff` over its base, and a failure there is None, which
        `gate.touches_code` answers True. A break reading the failure as an empty
        list survived every case until this one."""
        if os.name == "nt":
            pytest.skip("the shim is a POSIX shell script")
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "hooks"))
        import commitgate
        import gate

        head = git(repo, "rev-parse", "HEAD").stdout.strip()
        stage(repo, "service.py")
        git(
            repo,
            "-c",
            "user.email=e@example.com",
            "-c",
            "user.name=e",
            "commit",
            "-qm",
            "c",
        )
        new = git(repo, "rev-parse", "HEAD").stdout.strip()
        assert commitgate._paths_between(str(repo), head, new)() == ["service.py"]
        monkeypatch.setenv("PATH", a_git_whose_diff_fails(tmp_path))
        listed = commitgate._paths_between(str(repo), head, new)()
        assert listed is None, listed
        assert gate.touches_code(listed)


test_census = census_case(TARGET)
