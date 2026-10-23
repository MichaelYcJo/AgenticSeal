"""`hooks/implementer-notice.py`: a declaration naming an agent no mark answers
for says so, once, after a commit.

One line for both axes where both are unfulfilled. Nothing is said about an
axis whose mark stands, whose row was not answered, or in a repository that
never opted in: missing that silence, this is a fourth prompt in a plugin
whose first goal is verification that runs unattended. The notice never
blocks. The cases come from `tests/test_the_implementer_is_recorded.py`
(#942's phase 6).
"""

import os
import shutil

import pytest
from conftest import (
    ITEM,
    bash,
    census_case,
    declare,
    opt_in,
    run_dispatch,
    run_hook,
    spawn,
)

TARGET = "hooks/implementer-notice.py"

NOTICE = "answers `Implementation` with `smith`"
PLANNING_NOTICE = "answers `Planning` with `framer`"
BOTH = "`Planning` with `framer` and `Implementation` with `smith`"
# The sentence every notice ends with, whichever axes it names. Counting it is
# how S14 tells one line naming two axes from two lines naming one each.
ONCE = "Nothing was blocked, and this is said once per session."


class Test_main:
    def test_accepts_a_declared_smith_with_no_mark_and_notices_it(self, repo):
        """S6. Emitted from `post-bash`, whose output is read — a PreToolUse
        gate that allows produces no output at all."""
        opt_in(repo)
        declare(repo, implementation="smith")
        out = run_dispatch("post-bash", bash(repo))
        assert NOTICE in out, out
        assert ITEM in out, "the notice does not say which file"

    def test_accepts_a_declared_framer_with_no_mark_and_notices_it(self, repo):
        """S13. The fourth axis earns the same one line the third does."""
        opt_in(repo)
        declare(repo, implementation=None, planning="framer")
        out = run_dispatch("post-bash", bash(repo))
        assert PLANNING_NOTICE in out, out
        assert ITEM in out, "the notice does not say which file"
        assert NOTICE not in out, (
            "the notice named an axis the declaration did not answer"
        )

    def test_accepts_two_unfulfilled_axes_in_one_line(self, repo):
        """S14. The grain is once per repository per session, and two lines in one
        session is that grain broken in the commonest state of all — a declaration
        copied from the template and answered on both optional rows, by a session
        that then framed and built the work itself."""
        opt_in(repo)
        declare(repo, implementation="smith", planning="framer")
        out = run_dispatch("post-bash", bash(repo))
        assert out.count(ONCE) == 1, (
            f"two unfulfilled axes produced {out.count(ONCE)} notices:\n{out}"
        )
        assert BOTH in out, (
            f"one line was printed and it names only one of the two axes:\n{out}"
        )
        assert "neither was spawned" in out, (
            "the line names two axes and then says `no smith was spawned`, which "
            "reads as one of them"
        )

    def test_refuses_a_smith_whose_mark_stands(self, repo):
        """S7."""
        opt_in(repo)
        declare(repo, implementation="smith")
        run_dispatch("pre-agent", spawn(repo))
        assert NOTICE not in run_dispatch("post-bash", bash(repo))

    def test_refuses_a_framer_whose_mark_stands(self, repo):
        """S13. Spawning the framer is the whole of what the row asked for."""
        opt_in(repo)
        declare(repo, implementation=None, planning="framer")
        run_dispatch("pre-agent", spawn(repo, agent="specseal:framer"))
        assert PLANNING_NOTICE not in run_dispatch("post-bash", bash(repo))

    def test_refuses_to_let_one_axis_mark_silence_the_other(self, repo):
        """S13. The cross-axis case at the reader rather than at `stands`.

        Both rows answered and only `smith` spawned: the framer never ran, and the
        line has to say so. A notice that read one mark for both axes would go
        quiet here, which is the state this whole mechanism exists to report.
        """
        opt_in(repo)
        declare(repo, implementation="smith", planning="framer")
        run_dispatch("pre-agent", spawn(repo))
        out = run_dispatch("post-bash", bash(repo))
        assert PLANNING_NOTICE in out, out
        assert NOTICE not in out, "the fulfilled axis was named as unfulfilled"

    @pytest.mark.parametrize(
        "answer",
        ["the session", "whoever gets to it"],
        ids=["the other answer", "unreadable"],
    )
    def test_refuses_an_answer_that_names_no_agent(self, repo, answer):
        """S9. `the session` implemented it, which is what the declaration said;
        `parse()` reads an answer outside the vocabulary as unanswered, and
        unanswered is not a finding."""
        opt_in(repo)
        declare(repo, implementation=answer)
        assert NOTICE not in run_dispatch("post-bash", bash(repo))

    def test_refuses_a_declaration_without_the_row(self, repo):
        """S9. Every declaration written before this axis existed looks like this."""
        opt_in(repo)
        declare(repo, implementation=None)
        assert NOTICE not in run_dispatch("post-bash", bash(repo))

    def test_refuses_the_fourth_axis_other_answers_as_a_defect(self, repo):
        """S13's silences. `the session` framed it, which is what the row said; an
        absent row is every declaration written before the axis existed; and an
        unreadable one is unanswered, which is not a finding."""
        opt_in(repo)
        for answer in ("the session", None, "whoever gets to it", "`framer`"):
            declare(repo, implementation=None, planning=answer)
            out = run_dispatch("post-bash", bash(repo, session=f"s-{answer}"))
            assert PLANNING_NOTICE not in out, answer
            assert ONCE not in out, answer

    def test_refuses_a_command_that_does_not_commit(self, repo):
        """S10. Including one that merely mentions a commit in prose."""
        opt_in(repo)
        declare(repo, implementation="smith")
        for cmd in ("ls -la", "echo 'remember to git commit'", "git status"):
            assert NOTICE not in run_dispatch("post-bash", bash(repo, cmd=cmd)), cmd

    def test_refuses_an_unrelated_repository(self, repo):
        opt_in(repo)
        declare(repo, implementation="smith")
        shutil.rmtree(repo / "seal")
        assert NOTICE not in run_dispatch("post-bash", bash(repo))

    def test_the_notice_names_the_file_the_way_the_platform_spells_it(self, repo):
        """S14. `review-history-guard.py` was changed for this: a path joined with
        a literal `/` arrived on Windows as half of one command in each dialect.
        The file named is the one a person has to open."""
        opt_in(repo)
        declare(repo, implementation="smith")
        out = run_dispatch("post-bash", bash(repo))
        assert os.path.join("seal", "specs", ITEM, "routing.md") in out, out

    def test_the_notice_is_said_once_per_repository_per_session(self, repo):
        """S8. The grain is stated because `once` has meant four things here."""
        opt_in(repo)
        declare(repo, implementation="smith")
        assert NOTICE in run_dispatch("post-bash", bash(repo))
        assert NOTICE not in run_dispatch("post-bash", bash(repo))
        assert NOTICE in run_dispatch("post-bash", bash(repo, session="s2"))

    def test_the_notice_never_carries_a_permission_decision(self, repo):
        """S12. A PostToolUse hook cannot block, and a decision emitted from one
        would be merged by `dispatch.py` into a group that CAN."""
        opt_in(repo)
        declare(repo, implementation="smith")
        out = run_hook("implementer-notice.py", bash(repo))
        assert NOTICE in out
        assert "permissionDecision" not in out


test_census = census_case(TARGET)
