"""`hooks/lib/implementer.py`: the mark a declared agent's spawn leaves in the
repository's git dir, and the reading of it after a commit.

The module fails toward "no mark": a git dir that cannot be resolved or a
branch that cannot be named writes nothing, so the notice fires rather than
falling silent. The cases of `write` and `stands` through the two hooks stay
with `tests/hooks/test_implementer_mark.py` and `tests/hooks/test_implementer_notice.py`;
the cases here ask the module itself, for the two survivors #942 recorded
(#1017).
"""

import os
import subprocess

from conftest import census_case, git_dir, load_hook_module

TARGET = "hooks/lib/implementer.py"

implementer = load_hook_module("lib/implementer.py", "implementer_for_its_own_file")


class Test_git_dir:
    def test_accepts_a_repository_and_answers_its_absolute_git_dir(self, repo):
        assert implementer.git_dir(str(repo)) == git_dir(repo)

    def test_refuses_a_failed_git_whatever_it_printed(self, repo, monkeypatch):
        """A git that exits non-zero answers nothing, even where it wrote a
        path, so no mark goes under a directory a failed call named. The real
        git prints nothing on a failure, so the failure is faked to remove
        that guarantee (contract rule 13)."""

        def failed(cmd, **kwargs):
            return subprocess.CompletedProcess(cmd, 128, stdout="/x/.git\n", stderr="")

        monkeypatch.setattr(implementer.subprocess, "run", failed)
        assert implementer.git_dir(str(repo)) == ""


class Test_write:
    def test_accepts_a_branch_and_writes_it_as_the_axis_mark(self, repo):
        mark = implementer.IMPLEMENTATION_MARK
        assert implementer.write(str(repo), "feature/x", mark) is True
        with open(os.path.join(git_dir(repo), mark), encoding="utf-8") as handle:
            assert handle.read() == "feature/x\n"

    def test_refuses_an_empty_branch_and_writes_no_mark(self, repo):
        """A detached HEAD names no branch, and a mark holding an empty line
        would stand for no declaration while claiming a spawn happened."""
        mark = implementer.IMPLEMENTATION_MARK
        assert implementer.write(str(repo), "", mark) is False
        assert not os.path.exists(os.path.join(git_dir(repo), mark))


test_census = census_case(TARGET)
