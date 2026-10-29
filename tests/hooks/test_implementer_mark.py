"""`hooks/implementer-mark.py`: spawning `crafter` or `framer` leaves that axis's
mark in the repository's git dir.

The routing declaration answers `Implementation` and `Planning`, and a session
can declare an agent and then do the work itself. The mark is what spawning
the agent leaves, so the notice can tell. Missing, the notice fires for work
that was done correctly. The mark decides nothing. What
`hooks/lib/implementer.py` writes and reads is asked through this hook. The cases come from
`tests/test_the_implementer_is_recorded.py` (#942's phase 6).
"""

import os

from conftest import (
    branch_of,
    census_case,
    git_dir,
    git_out,
    load_hook_module,
    opt_in,
    run_dispatch,
    spawn,
)

TARGET = "hooks/implementer-mark.py"

implementer = load_hook_module("lib/implementer.py", "agentic_implementer")


def mark_path(repo, mark):
    """Where one axis's mark lives. The axis is named at every call site, so a
    case cannot assert about the implementation mark while meaning the other."""
    return os.path.join(git_dir(repo), mark)


class Test_main:
    def test_accepts_a_crafter_spawn_and_leaves_a_mark(self, repo):
        """S1, through the group the harness actually runs, not the gate alone."""
        opt_in(repo)
        assert not os.path.exists(mark_path(repo, implementer.IMPLEMENTATION_MARK))
        assert run_dispatch("pre-agent", spawn(repo)).strip() == "", (
            "the mark gate must decide nothing; output here would be a fourth prompt"
        )
        assert os.path.isfile(mark_path(repo, implementer.IMPLEMENTATION_MARK))
        assert implementer.stands(
            str(repo), branch_of(repo), implementer.IMPLEMENTATION_MARK
        )

    def test_accepts_a_crafter_spawn_on_a_branch_with_no_commit_yet(self, tmp_path):
        """A new repository's `main` has no commit, and the mark stands for
        `main`, the branch the edit gate and the declaration resolve there
        (round 5 of #1027, finding 1)."""
        fresh = tmp_path / "fresh"
        fresh.mkdir()
        assert git_out(fresh, "init", "-q", "-b", "main") == ""
        opt_in(fresh)
        run_dispatch("pre-agent", spawn(fresh))
        assert implementer.stands(str(fresh), "main", implementer.IMPLEMENTATION_MARK)

    def test_accepts_a_framer_spawn_and_leaves_the_planning_mark(self, repo):
        """S13. The second axis arrives on the first's mechanism: same gate, same
        group, same silence, a different file under the git dir."""
        opt_in(repo)
        assert (
            run_dispatch("pre-agent", spawn(repo, agent="agentic:framer")).strip() == ""
        )
        assert os.path.isfile(mark_path(repo, implementer.PLANNING_MARK))
        assert implementer.stands(str(repo), branch_of(repo), implementer.PLANNING_MARK)

    def test_accepts_the_project_local_spelling_of_the_agent(self, repo):
        """S3. The harness spells a plugin's agent `agentic:crafter` and a
        project-local one `crafter`. Reading only the first would leave the notice
        firing forever in a repository that defines its own."""
        opt_in(repo)
        run_dispatch("pre-agent", spawn(repo, agent="crafter"))
        assert os.path.isfile(mark_path(repo, implementer.IMPLEMENTATION_MARK))
        run_dispatch("pre-agent", spawn(repo, agent="framer"))
        assert os.path.isfile(mark_path(repo, implementer.PLANNING_MARK))

    def test_refuses_a_mark_for_one_axis_answering_for_the_other(self, repo):
        """S13's other half, and the shape `stands`'s branch scoping already has.

        Two axes share one directory, so the axis is part of the address exactly as
        the branch is. A `crafter` spawned on this branch answering for a `framer`
        that never ran is the false silence the module refuses — and it is the
        likelier direction, because `crafter` is spawned on nearly every work item.
        """
        opt_in(repo)
        run_dispatch("pre-agent", spawn(repo))
        branch = branch_of(repo)
        assert implementer.stands(str(repo), branch, implementer.IMPLEMENTATION_MARK)
        assert not implementer.stands(str(repo), branch, implementer.PLANNING_MARK)
        assert not os.path.exists(mark_path(repo, implementer.PLANNING_MARK))

    def test_refuses_any_other_agent(self, repo):
        """S2. `crafter-helper` and `framer-helper` are in the list because a
        substring test would read either as the agent itself."""
        opt_in(repo)
        for agent in (
            "agentic:proofer",
            "agentic:tracer",
            "agentic:sealer",
            "general-purpose",
            "crafter-helper",
            "framer-helper",
        ):
            run_dispatch("pre-agent", spawn(repo, agent=agent))
            for mark in (implementer.IMPLEMENTATION_MARK, implementer.PLANNING_MARK):
                assert not os.path.exists(mark_path(repo, mark)), f"{agent} -> {mark}"

    def test_refuses_a_tool_other_than_agent_or_task_naming_crafter(self, repo):
        """Only a spawn leaves the mark. A call of another tool whose input
        happens to name `crafter` spawned nothing, so the notice must still be
        free to fire (#1017, the body's `main` row on another tool)."""
        opt_in(repo)
        run_dispatch("pre-agent", {**spawn(repo), "tool_name": "Bash"})
        assert not os.path.exists(mark_path(repo, implementer.IMPLEMENTATION_MARK))

    def test_refuses_a_repository_that_never_opted_in(self, repo):
        """S4. A globally installed plugin must not write into repositories that
        never asked for the workflow."""
        for agent in ("agentic:crafter", "agentic:framer"):
            run_dispatch("pre-agent", spawn(repo, agent=agent))
        for mark in (implementer.IMPLEMENTATION_MARK, implementer.PLANNING_MARK):
            assert not os.path.exists(mark_path(repo, mark)), mark

    def test_refuses_to_answer_for_another_branch(self, repo):
        """S5. One `crafter` spawned once would otherwise silence the notice for
        every work item in that repository, forever."""
        opt_in(repo)
        run_dispatch("pre-agent", spawn(repo))
        run_dispatch("pre-agent", spawn(repo, agent="agentic:framer"))
        for mark in (implementer.IMPLEMENTATION_MARK, implementer.PLANNING_MARK):
            assert implementer.stands(str(repo), branch_of(repo), mark), mark
            assert not implementer.stands(str(repo), "feature/somewhere-else", mark), (
                mark
            )


test_census = census_case(TARGET)
