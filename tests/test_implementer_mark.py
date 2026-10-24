"""`hooks/implementer-mark.py`: spawning `smith` or `framer` leaves that axis's
mark in the repository's git dir.

The routing declaration answers `Implementation` and `Planning`, and a session
can declare an agent and then do the work itself. The mark is what spawning
the agent leaves, so the notice can tell. Missing, the notice fires for work
that was done correctly. The mark decides nothing, and a broken mark gate must
leave the worktree guard's verdict alone, which is the objection #26 raised
against putting a second gate in `pre-agent`. What `hooks/implementer.py`
writes and reads is asked through this hook. The cases come from
`tests/test_the_implementer_is_recorded.py` (#942's phase 6).
"""

import os
import shutil
from pathlib import Path

from conftest import (
    HOOKS,
    branch_of,
    census_case,
    fired,
    git_dir,
    load_hook_module,
    opt_in,
    run_dispatch,
    spawn,
)

TARGET = "hooks/implementer-mark.py"

implementer = load_hook_module("implementer.py", "specseal_implementer")


def mark_path(repo, mark):
    """Where one axis's mark lives. The axis is named at every call site, so a
    case cannot assert about the implementation mark while meaning the other."""
    return os.path.join(git_dir(repo), mark)


class Test_main:
    def test_accepts_a_smith_spawn_and_leaves_a_mark(self, repo):
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

    def test_accepts_a_framer_spawn_and_leaves_the_planning_mark(self, repo):
        """S13. The second axis arrives on the first's mechanism: same gate, same
        group, same silence, a different file under the git dir."""
        opt_in(repo)
        assert (
            run_dispatch("pre-agent", spawn(repo, agent="specseal:framer")).strip()
            == ""
        )
        assert os.path.isfile(mark_path(repo, implementer.PLANNING_MARK))
        assert implementer.stands(str(repo), branch_of(repo), implementer.PLANNING_MARK)

    def test_accepts_the_project_local_spelling_of_the_agent(self, repo):
        """S3. The harness spells a plugin's agent `specseal:smith` and a
        project-local one `smith`. Reading only the first would leave the notice
        firing forever in a repository that defines its own."""
        opt_in(repo)
        run_dispatch("pre-agent", spawn(repo, agent="smith"))
        assert os.path.isfile(mark_path(repo, implementer.IMPLEMENTATION_MARK))
        run_dispatch("pre-agent", spawn(repo, agent="framer"))
        assert os.path.isfile(mark_path(repo, implementer.PLANNING_MARK))

    def test_refuses_a_mark_for_one_axis_answering_for_the_other(self, repo):
        """S13's other half, and the shape `stands`'s branch scoping already has.

        Two axes share one directory, so the axis is part of the address exactly as
        the branch is. A `smith` spawned on this branch answering for a `framer`
        that never ran is the false silence the module refuses — and it is the
        likelier direction, because `smith` is spawned on nearly every work item.
        """
        opt_in(repo)
        run_dispatch("pre-agent", spawn(repo))
        branch = branch_of(repo)
        assert implementer.stands(str(repo), branch, implementer.IMPLEMENTATION_MARK)
        assert not implementer.stands(str(repo), branch, implementer.PLANNING_MARK)
        assert not os.path.exists(mark_path(repo, implementer.PLANNING_MARK))

    def test_refuses_any_other_agent(self, repo):
        """S2. `smith-helper` and `framer-helper` are in the list because a
        substring test would read either as the agent itself."""
        opt_in(repo)
        for agent in (
            "specseal:warden",
            "specseal:scribe",
            "specseal:sealer",
            "general-purpose",
            "smith-helper",
            "framer-helper",
        ):
            run_dispatch("pre-agent", spawn(repo, agent=agent))
            for mark in (implementer.IMPLEMENTATION_MARK, implementer.PLANNING_MARK):
                assert not os.path.exists(mark_path(repo, mark)), f"{agent} -> {mark}"

    def test_refuses_a_repository_that_never_opted_in(self, repo):
        """S4. A globally installed plugin must not write into repositories that
        never asked for the workflow."""
        for agent in ("specseal:smith", "specseal:framer"):
            run_dispatch("pre-agent", spawn(repo, agent=agent))
        for mark in (implementer.IMPLEMENTATION_MARK, implementer.PLANNING_MARK):
            assert not os.path.exists(mark_path(repo, mark)), mark

    def test_refuses_to_answer_for_another_branch(self, repo):
        """S5. One `smith` spawned once would otherwise silence the notice for
        every work item in that repository, forever."""
        opt_in(repo)
        run_dispatch("pre-agent", spawn(repo))
        run_dispatch("pre-agent", spawn(repo, agent="specseal:framer"))
        for mark in (implementer.IMPLEMENTATION_MARK, implementer.PLANNING_MARK):
            assert implementer.stands(str(repo), branch_of(repo), mark), mark
            assert not implementer.stands(str(repo), "feature/somewhere-else", mark), (
                mark
            )


class Test_module:
    def test_a_broken_mark_gate_leaves_the_worktree_guards_verdict_alone(
        self, repo, tmp_path
    ):
        """S13. Issue #26's second objection to building this: a second gate in
        `pre-agent` whose import fails could take the worktree guard's answer
        with it. `dispatch.py#run_gate` catches per gate, so it does not — and
        this is the measurement, with the mark gate unparseable and then absent.

        The intact run also pins `questions.md` Q2: the mark is written even when
        the guard stops the same spawn, because the gates do not see each other.
        """
        opt_in(repo)
        hooks = tmp_path / "hooks"
        shutil.copytree(Path(HOOKS).resolve(), hooks)
        # A fresh session id per call. The guard remembers which sessions it has
        # already put the two-option question to (`already_asked`) and answers a
        # repeat from the same session with the shorter fallback, so three calls
        # under one id would differ on the guard's own state and say nothing
        # about the mark gate. Measured on CI, where ps/lsof are absent and the
        # guard reaches that site; macOS reached another and never showed it.
        isolated = spawn(repo, isolation="worktree", session="s-intact")

        intact = run_dispatch("pre-agent", isolated, hooks=str(hooks))
        assert fired(intact), "the guard did not fire, so there is nothing to protect"
        assert os.path.isfile(mark_path(repo, implementer.IMPLEMENTATION_MARK)), (
            "Q2: written before the group decides"
        )

        for n, broken in enumerate(("def broken(:\n", None)):
            if broken is None:
                (hooks / "implementer-mark.py").unlink()
            else:
                (hooks / "implementer-mark.py").write_text(broken, encoding="utf-8")
            again = spawn(repo, isolation="worktree", session=f"s-broken-{n}")
            after = run_dispatch("pre-agent", again, hooks=str(hooks))
            assert after == intact, (
                f"a broken mark gate changed the worktree guard's verdict:\n{after}"
            )


test_census = census_case(TARGET)
