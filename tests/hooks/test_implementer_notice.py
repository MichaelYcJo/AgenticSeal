"""`hooks/implementer-notice.py`: a declaration naming an agent no mark answers
for says so, once, after a commit.

One line for both axes where both are unfulfilled. Nothing is said about an
axis whose mark stands, whose row was not answered, or in a repository that
never opted in: missing that silence, this is a fourth prompt in a plugin
whose first value is efficient development through an unattended
workflow. The notice never blocks. The cases come from `tests/test_the_implementer_is_recorded.py` and,
for the path a local-mode root prints, from
`tests/test_local_mode_resolves_under_the_git_dir.py` (#942's phase 6).
"""

import os
import shutil

import pytest
from conftest import (
    ITEM,
    bash,
    census_case,
    declare,
    declare_crafter,
    git_dir,
    load_hook_module,
    opt_in,
    run_dispatch,
    run_hook,
    spawn,
)

TARGET = "hooks/implementer-notice.py"

NOTICE = "answers `Implementation` with `crafter`"
PLANNING_NOTICE = "answers `Planning` with `framer`"
BOTH = "`Planning` with `framer` and `Implementation` with `crafter`"
# The sentence every notice ends with, whichever axes it names. Counting it is
# how S14 tells one line naming two axes from two lines naming one each.
ONCE = "Nothing was blocked, and this is said once per session."

notice = load_hook_module("implementer-notice.py", "implementer_notice_for_units")


class Test_line:
    def test_accepts_one_axis_and_says_its_agent_was_not_spawned(self):
        """The singular line, pinned whole: it is what nearly every notice
        says, and the module keeps it byte for byte (contract rule 14)."""
        assert notice.line("w.md", [("Implementation", "crafter")]) == (
            "[agentic] w.md answers `Implementation` with `crafter`, and no crafter "
            "was spawned on this branch. Either spawn it for the rest of the "
            "work, or change the row to `the session` so the declaration says "
            "what actually happened. Nothing was blocked, and this is said once "
            "per session."
        )

    def test_refuses_the_one_axis_wording_for_two_axes(self):
        said = notice.line(
            "w.md", [("Planning", "framer"), ("Implementation", "crafter")]
        )
        assert "neither was spawned on this branch" in said, said
        assert "no crafter" not in said and "no framer" not in said, said


class Test_commits:
    def test_accepts_a_git_commit(self):
        assert notice.commits("git commit -m x") is True

    def test_refuses_a_commit_that_is_only_a_heredoc_body(self):
        """The body is data the command feeds `cat`, so nothing committed."""
        assert notice.commits("cat <<'EOF'\ngit commit -m x\nEOF") is False


class Test_already_told:
    def test_accepts_a_session_once_and_records_it(self, repo):
        assert notice.already_told(str(repo), "s-once") is False
        assert notice.already_told(str(repo), "s-once") is True

    def test_refuses_a_missing_or_dot_session_id_and_records_nothing(self, repo):
        """A missing or dot id names no file of its own, so it reads as told
        and nothing is made under the git dir (#1017, the body's
        `already_told` row)."""
        for session in (None, "."):
            assert notice.already_told(str(repo), session) is True, session
            assert not os.path.exists(os.path.join(git_dir(repo), notice.NOTICE_DIR))


class Test_notify:
    def test_accepts_a_declared_crafter_and_names_the_file_from_the_root(self, repo):
        """The path a person opens is the one under the repository, not the
        absolute one, which also ends in it (#1017, round 3's n1)."""
        opt_in(repo)
        declare(repo, implementation="crafter")
        where = os.path.join("seal", "threads", ITEM, "routing.md")
        said = notice.notify(str(repo), "s-notify")
        assert said.startswith(f"[agentic] {where} answers "), said

    def test_refuses_a_branch_no_declaration_names(self, repo):
        opt_in(repo)
        assert notice.notify(str(repo), "s-notify") == ""


class Test_main:
    def test_refuses_a_tool_other_than_bash_whose_input_commits(self, repo):
        """Only a Bash call runs a command. Another tool carrying a commit in
        its input committed nothing (#1017, the body's `main` row)."""
        opt_in(repo)
        declare(repo, implementation="crafter")
        out = run_hook("implementer-notice.py", {**bash(repo), "tool_name": "Write"})
        assert NOTICE not in out, out

    def test_accepts_a_declared_crafter_with_no_mark_and_notices_it(self, repo):
        """S6. Emitted from `post-bash`, whose output is read — a PreToolUse
        gate that allows produces no output at all."""
        opt_in(repo)
        declare(repo, implementation="crafter")
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
        declare(repo, implementation="crafter", planning="framer")
        out = run_dispatch("post-bash", bash(repo))
        assert out.count(ONCE) == 1, (
            f"two unfulfilled axes produced {out.count(ONCE)} notices:\n{out}"
        )
        assert BOTH in out, (
            f"one line was printed and it names only one of the two axes:\n{out}"
        )
        assert "neither was spawned" in out, (
            "the line names two axes and then says `no crafter was spawned`, which "
            "reads as one of them"
        )

    def test_refuses_a_crafter_whose_mark_stands(self, repo):
        """S7."""
        opt_in(repo)
        declare(repo, implementation="crafter")
        run_dispatch("pre-agent", spawn(repo))
        assert NOTICE not in run_dispatch("post-bash", bash(repo))

    def test_refuses_a_framer_whose_mark_stands(self, repo):
        """S13. Spawning the framer is the whole of what the row asked for."""
        opt_in(repo)
        declare(repo, implementation=None, planning="framer")
        run_dispatch("pre-agent", spawn(repo, agent="agentic:framer"))
        assert PLANNING_NOTICE not in run_dispatch("post-bash", bash(repo))

    def test_refuses_to_let_one_axis_mark_silence_the_other(self, repo):
        """S13. The cross-axis case at the reader rather than at `stands`.

        Both rows answered and only `crafter` spawned: the framer never ran, and the
        line has to say so. A notice that read one mark for both axes would go
        quiet here, which is the state this whole mechanism exists to report.
        """
        opt_in(repo)
        declare(repo, implementation="crafter", planning="framer")
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
        declare(repo, implementation="crafter")
        for cmd in ("ls -la", "echo 'remember to git commit'", "git status"):
            assert NOTICE not in run_dispatch("post-bash", bash(repo, cmd=cmd)), cmd

    def test_refuses_an_unrelated_repository(self, repo):
        opt_in(repo)
        declare(repo, implementation="crafter")
        shutil.rmtree(repo / "seal")
        assert NOTICE not in run_dispatch("post-bash", bash(repo))

    def test_the_notice_names_the_file_the_way_the_platform_spells_it(self, repo):
        """S14. `review-history-guard.py` was changed for this: a path joined with
        a literal `/` arrived on Windows as half of one command in each dialect.
        The file named is the one a person has to open."""
        opt_in(repo)
        declare(repo, implementation="crafter")
        out = run_dispatch("post-bash", bash(repo))
        assert os.path.join("seal", "threads", ITEM, "routing.md") in out, out

    def test_the_notice_is_said_once_per_repository_per_session(self, repo):
        """S8. The grain is stated because `once` has meant four things here."""
        opt_in(repo)
        declare(repo, implementation="crafter")
        assert NOTICE in run_dispatch("post-bash", bash(repo))
        assert NOTICE not in run_dispatch("post-bash", bash(repo))
        assert NOTICE in run_dispatch("post-bash", bash(repo, session="s2"))

    def test_the_notice_never_carries_a_permission_decision(self, repo):
        """S12. A PostToolUse hook cannot block, and a decision emitted from one
        would be merged by `dispatch.py` into a group that CAN."""
        opt_in(repo)
        declare(repo, implementation="crafter")
        out = run_hook("implementer-notice.py", bash(repo))
        assert NOTICE in out
        assert "permissionDecision" not in out

    def test_the_implementer_notice_names_the_local_path(self, local):
        repo, home = local
        declare_crafter(repo, home)
        out = run_hook("implementer-notice.py", bash(repo))
        assert "answers `Implementation` with `crafter`" in out, out
        assert os.path.join(".git", "seal", "threads", ITEM, "routing.md") in out, out


test_census = census_case(TARGET)
