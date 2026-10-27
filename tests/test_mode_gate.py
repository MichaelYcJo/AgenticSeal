"""`hooks/mode-gate.py`: a root nobody chose a mode for is a state the gate names.

Issue #151: a session created `seal/` and started working, and nothing asked
about shared or local mode. The gate asks on the session's first command in
a repository whose root records no `Mode`, once as a deny and once as an
ask, and then says nothing. The scenario ids are
`aa687d35:seal/specs/1788817289-local-mode-from-first-setup-to-the-gate/spec.md`'s.
The cases come from `tests/test_the_mode_question_is_asked_once.py` (#942's
phase 6).
"""

import os
import subprocess

import config_shapes
import pytest
from conftest import (
    TABLE,
    census_case,
    decision_of,
    git_dir,
    load_hook_module,
    local_home,
    mark_root,
    opt_in_shared,
    payload,
    reason_of,
    run_hook,
    write_config,
    write_unreadable,
)

TARGET = "hooks/mode-gate.py"

GATE = "mode-gate.py"


class Test_main:
    # --- S7, S10: the question, where nobody chose -------------------------

    def test_refuses_a_root_with_no_recorded_mode_and_names_it(self, repo):
        """S7. The state #151 is about: a root exists and nobody was asked."""
        opt_in_shared(repo)
        out = run_hook(GATE, payload("git commit -m x", repo))
        assert decision_of(out) == "deny"
        said = reason_of(out)
        assert "AskUserQuestion" in said
        assert "seal mode" in said
        assert "seal mode local" in said and "seal mode shared" in said

    def test_refuses_with_a_prompt_that_says_what_each_answer_costs(self, repo):
        """Every answer has to continue (`implement` *1. Read the spec before the
        code*). Both do something and
        the prompt says which — one records where the folder already is, the other
        moves it."""
        opt_in_shared(repo)
        said = reason_of(run_hook(GATE, payload("git commit -m x", repo)))
        assert "committed" in said
        assert str(repo / "seal") in said

    def test_refuses_with_a_first_paragraph_that_names_the_root(self, repo):
        """The question says where the root it asks about is before any option
        does: the first option repeats the path, and a reader who stops at
        the first paragraph still has it (#1017, the body's question-text
        row)."""
        opt_in_shared(repo)
        said = reason_of(run_hook(GATE, payload("ls", repo)))
        assert str(repo / "seal") in said.split("\n\n")[0]

    def test_refuses_with_options_that_leave_the_checks_to_their_own_command(
        self, repo
    ):
        """S7 of #952: moving the root installs and removes nothing under
        `.github/`, so neither option promises the workflow."""
        opt_in_shared(repo)
        said = " ".join(reason_of(run_hook(GATE, payload("ls", repo))).split())
        shared = said.split('2. "Shared"')[1].split('3. "Local"')[0]
        local = said.split('3. "Local"')[1]
        assert "Nothing is installed under .github/" in shared, shared
        assert "`seal pr-checks install`" in shared, shared
        assert "A workflow file already in the tree stays" in local, local
        # Round 1 of #952, finding 2: the gate fires for a root with no
        # `Mode` row, an old bootstrap, so its workflow is likely an old pin.
        assert (
            "Pinned to this release, its checks examine nothing in this mode; "
            "pinned to an older one, they fail every pull request until its "
            "`--branch` line moves or `seal pr-checks remove` takes it out."
        ) in local, local
        assert "checks are installed" not in shared and "removed" not in local

    def test_refuses_on_the_first_command_not_at_the_commit(self, repo):
        """The budget decided this, not the act #151 names. Scoping the gate to a
        commit puts the question beside the review arm's, at minute thirty, on a
        session that may have nobody at the keyboard — and `implement` *1. Read the spec before the code* says the
        cost of a question is when it arrives. The count is the same either way,
        because the budget below is per session rather than per command."""
        opt_in_shared(repo)
        assert decision_of(run_hook(GATE, payload("ls -la", repo))) == "deny"

    def test_refuses_the_second_attempt_in_a_session_with_an_ask(self, repo):
        """S10. A deny that repeats is an outage: nothing in an unattended run can
        get past it. The budget is one deny per session per repository, and `ask`
        is approvable."""
        opt_in_shared(repo)
        assert decision_of(run_hook(GATE, payload("git commit -m x", repo))) == "deny"
        out = run_hook(GATE, payload("git commit -m x", repo))
        assert decision_of(out) == "ask"
        assert "seal mode" in reason_of(out)

    def test_refuses_a_different_session_too(self, repo):
        """The budget is per session, like the answer it spends. A session that
        never saw the question has not been asked it."""
        opt_in_shared(repo)
        assert decision_of(run_hook(GATE, payload("git commit -m x", repo))) == "deny"
        assert (
            decision_of(run_hook(GATE, payload("git commit -m x", repo, session="s2")))
            == "deny"
        )

    def test_refuses_the_sessions_repository_not_the_one_git_is_sent_to(
        self, repo, tmp_path
    ):
        """`git -C <elsewhere>` moves git and does not move the session. Its
        sibling gate resolves the repository a COMMIT lands in, because a verdict
        about a change has to be about the repository that change reaches. This is
        not a verdict about a change: it is a fact about the workspace the session
        is sitting in, and that workspace is the one with the unrecorded root."""
        other = tmp_path / "other"
        other.mkdir()
        subprocess.run(["git", "-C", str(other), "init", "-q"], check=True)
        opt_in_shared(repo)
        out = run_hook(GATE, payload(f"git -C {other} commit -m x", repo))
        assert decision_of(out) == "deny", out
        assert str(repo) in reason_of(out)

    def test_refuses_a_session_in_a_subdirectory_too(self, repo):
        """A mutation survived here too, and it is the ordinary case: sessions sit
        in `src/` as often as at the top. Taking `cwd` for the repository root
        makes the gate look for `<cwd>/seal/`, find nothing, and go quiet for
        every session that is not at the top — silence that reads exactly like a
        repository with the row already written."""
        opt_in_shared(repo)
        sub = repo / "src"
        sub.mkdir()
        out = run_hook(GATE, payload("ls", sub))
        assert decision_of(out) == "deny", out
        said = reason_of(out)
        assert str(repo / "seal") in said
        assert str(sub) not in said, "the prompt names the subdirectory as the root"

    # --- S8, S9: the silences -----------------------------------------------

    @pytest.mark.parametrize(
        "root, rows",
        [
            ("shared", "| Mode | shared |\n"),
            ("local", "| Mode | local |\n"),
            ("shared", "| Mode | whatever |\n| Mode | shared |\n"),
        ],
        ids=["a-recorded-mode", "a-local-root-with-a-recorded-mode", "a-row-twice"],
    )
    def test_accepts_a_root_whose_config_answers_or_refuses_the_mode(
        self, repo, root, rows
    ):
        """S8. The row is the answer, so the question stops, read at either
        place: a gate that only looked at `<repo>/seal/` would nag every
        local-mode repository forever. And S1 of #867, the hook's half: a
        `Mode` row written twice has no value, and the gate reads that refusal
        as it reads an unreadable file, saying nothing. Asking the mode
        question would send a session to `seal mode`, which refuses to write
        into a file whose rows disagree. Seen red against the first-wins
        reader: the first row, `whatever`, names no mode, and the gate
        denied."""
        home = opt_in_shared(repo) if root == "shared" else local_home(repo)
        write_config(home, TABLE.format(rows=rows))
        assert decision_of(run_hook(GATE, payload("git commit -m x", repo))) == "silent"

    def test_accepts_a_repository_with_no_root(self, repo):
        """S9. A globally installed plugin must not nag a repository that never
        opted in — the rule `hooks/lib/optin.py` exists to hold."""
        assert decision_of(run_hook(GATE, payload("git commit -m x", repo))) == "silent"

    @pytest.mark.parametrize("shape", ["directory", "undecodable", "unreadable"])
    def test_accepts_a_config_nobody_can_open_as_silence_not_a_deny(self, repo, shape):
        """`hooks/lib/optin.py`'s rule, which this module's docstring adopts: a
        repository this cannot read is one it says nothing about.

        `hooks/lib/config.py#declared_mode` used to fold *will not open* into
        *declared nothing*; for a gate the two are different states, and treating
        them alike denied a repository whose answer might already be there. Since
        #867 the reader answers `refused` for it, and the gate reads that alone.

        Reachable, not exotic: `hooks/lib/optin.py#repo_root` already records a
        repository under a path a cp949 console cannot decode, and a row
        hand-edited in a non-UTF-8 locale puts those bytes here. The escape would
        have been `seal mode`, writing a row into the file nothing can parse.
        """
        home = opt_in_shared(repo)
        path = os.path.join(str(home), "config.md")
        if shape == "unreadable":
            write_config(home, TABLE.format(rows="| Mode | shared |\n"))
            os.chmod(path, 0o000)
        else:
            write_unreadable(home, shape)
        try:
            assert decision_of(run_hook(GATE, payload("ls", repo))) == "silent"
        finally:
            if shape == "unreadable":
                os.chmod(path, 0o600)

    @pytest.mark.parametrize("number", [1, 5, 7])
    def test_accepts_a_table_the_walker_refuses_as_silence(self, repo, number):
        """S3. The mode gate reads a refusal as an answer it cannot act on and
        says nothing, on the first call and the second, as it does for a file
        that will not read (#867); the prompt budget of a refused table is zero.
        Shape 5's `Mode` row is read, so the gate is quiet because the mode is
        declared. Seen red against the stop rule on shape 7: the row under the
        bare pipe was not read, the file read as declaring nothing, and the gate
        denied."""
        write_config(opt_in_shared(repo), config_shapes.SHAPES[number])
        seen = [decision_of(run_hook(GATE, payload("ls", repo))) for _ in range(2)]
        assert seen == ["silent", "silent"], seen

    def test_accepts_a_repository_that_is_not_this_one_without_judging_it(
        self, repo, tmp_path
    ):
        """The other half of the same rule: a session sitting OUTSIDE an opted-in
        repository hears nothing about it, whatever its commands mention."""
        other = tmp_path / "other"
        other.mkdir()
        subprocess.run(["git", "-C", str(other), "init", "-q"], check=True)
        opt_in_shared(repo)
        assert (
            decision_of(run_hook(GATE, payload(f"git -C {repo} commit -m x", other)))
            == "silent"
        )


class Test_already_asked:
    def test_accepts_the_third_command_of_a_session_as_asked(self, repo):
        """The budget is TWO prompts, and the ask is spent like the deny.

        Round 1 measured what an ask that stands for the rest of the session
        costs on a gate that fires per command rather than per commit: one deny
        and NINE asks over ten ordinary calls, where the sibling gate was silent
        on nine of the same ten. And the way out, `seal mode`, is itself a Bash
        call — so a run with nobody at the keyboard could not reach the command
        that ends the asking, and every command it tried was stopped rather than
        one. That is the outage the module docstring says this cannot become.
        """
        opt_in_shared(repo)
        seen = [decision_of(run_hook(GATE, payload("ls", repo))) for _ in range(6)]
        assert seen == ["deny", "ask", "silent", "silent", "silent", "silent"], seen

    def test_accepts_the_two_prompts_counted_apart(self, repo):
        """One marker each, so spending the deny does not spend the ask.

        Sharing a directory would collapse the budget to a single prompt and lose
        the approvable retry the deny's own reason tells the model to make.
        """
        gate = load_hook_module(GATE, "agentic_mode_gate_markers")
        assert gate.CHOICE_DIR != gate.RETRY_DIR
        opt_in_shared(repo)
        run_hook(GATE, payload("ls", repo))
        marker = os.path.join(git_dir(repo), gate.CHOICE_DIR, "s1")
        assert os.path.isfile(marker)
        assert not os.path.exists(os.path.join(git_dir(repo), gate.RETRY_DIR, "s1"))

    def test_accepts_an_unwritable_marker_as_already_asked(self, repo):
        """The rule the chain spec states, and the direction matters: inverted,
        the deny repeats forever in exactly the environments that cannot write."""
        opt_in_shared(repo)
        with open(
            os.path.join(git_dir(repo), "agentic-mode-choice"), "w", encoding="utf-8"
        ) as f:
            f.write("not a directory")
        assert decision_of(run_hook(GATE, payload("git commit -m x", repo))) == "ask"

    def test_refuses_a_session_id_that_would_leave_the_git_dir(self, repo):
        """The id names a file. Measured on a sibling guard: `../../escaped` put
        an empty file at the repository root."""
        opt_in_shared(repo)
        run_hook(GATE, payload("git commit -m x", repo, session="../../escaped"))
        assert not (repo / "escaped").exists()

    @pytest.mark.parametrize("session", [".", ".."])
    def test_refuses_a_dot_session_id_as_asked_and_records_nothing(self, repo, session):
        """A dot names no file, so it counts as asked and nothing is made for
        it, not even the marker directory (#1017, the body's `.` and `..`
        row)."""
        gate = load_hook_module(GATE, "agentic_mode_gate_dots")
        before = sorted(os.listdir(git_dir(repo)))
        assert gate.already_asked(git_dir(repo), session) is True
        assert sorted(os.listdir(git_dir(repo))) == before


class Test_git_dir_of:
    def test_accepts_a_repository_and_answers_its_git_dir(self, repo):
        gate = load_hook_module(GATE, "agentic_mode_gate_git_dir")
        assert gate.git_dir_of(str(repo)) == os.path.normpath(git_dir(repo))

    def test_refuses_a_failed_git_whatever_it_printed(self, repo, monkeypatch):
        """A git that exits non-zero answers nothing, even where it wrote a
        path. The real git prints nothing on a failure, so the failure is
        faked to remove that guarantee (contract rule 13; #1017, the body's
        `git_dir_of` row)."""
        gate = load_hook_module(GATE, "agentic_mode_gate_failed_git")

        def failed(cmd, **kwargs):
            return subprocess.CompletedProcess(cmd, 128, stdout=".git\n", stderr="")

        monkeypatch.setattr(gate.subprocess, "run", failed)
        assert gate.git_dir_of(str(repo)) == ""


class Test_marker_dir:
    def test_accepts_one_local_root_as_one_question_for_the_whole_clone(
        self, repo, tmp_path
    ):
        """`README.md`'s gate row says once per session per repository, and in
        local mode one folder under the common git directory IS the repository —
        `undeclared()` reads that same root from every work tree.

        Keying the marker to `--absolute-git-dir` keyed it to the TREE, so one
        session was denied once per worktree about one folder. Measured 2026-09-08
        before the fix: main tree deny, linked worktree deny, the same folder both
        times.
        """
        local_home(repo)
        side = tmp_path / "side"
        subprocess.run(
            ["git", "-C", str(repo), "worktree", "add", "-q", "-b", "side", str(side)],
            check=True,
            capture_output=True,
        )
        assert decision_of(run_hook(GATE, payload("ls", repo))) == "deny"
        assert decision_of(run_hook(GATE, payload("ls", side))) == "ask"
        assert decision_of(run_hook(GATE, payload("ls", side))) == "silent"

    def test_accepts_an_absolute_directory_for_either_question(self, repo):
        """`git_dir_of` promises an absolute path and `already_asked` joins
        nothing onto it, so the promise is the whole of what places the marker.

        It is not git's promise. `--absolute-git-dir` is absolute; measured
        2026-09-08, `--git-common-dir` answers `.git` from a main work tree and an
        absolute path from a linked one. A relative answer passed through would
        put the marker under whatever directory the hook process happened to start
        in — a different file each time, which is a question asked again.
        """
        gate = load_hook_module(GATE, "agentic_mode_gate_absolute")
        for which in ("--absolute-git-dir", "--git-common-dir"):
            answer = gate.git_dir_of(str(repo), which)
            assert os.path.isabs(answer), f"{which} answered {answer!r}"
            assert os.path.isdir(answer)

    def test_refuses_to_share_a_shared_roots_question_across_work_trees(
        self, repo, tmp_path
    ):
        """The half that must NOT move with it. Each work tree carries its own
        `<repo>/seal/`, so each is a separate root nobody chose a mode for and
        each deserves its own question. A marker keyed to the clone for both modes
        would answer for a root the session has never seen."""
        opt_in_shared(repo)
        side = tmp_path / "side"
        subprocess.run(
            ["git", "-C", str(repo), "worktree", "add", "-q", "-b", "side", str(side)],
            check=True,
            capture_output=True,
        )
        mark_root(side / "seal")
        assert decision_of(run_hook(GATE, payload("ls", repo))) == "deny"
        assert decision_of(run_hook(GATE, payload("ls", side))) == "deny"


class Test_module:
    def test_the_gate_is_in_the_pre_bash_group(self):
        """A gate `hooks/hooks.json` never reaches decides nothing. The dispatch
        group is the wiring, and it is the half a passing gate cannot report on."""
        dispatch = load_hook_module("dispatch.py", "agentic_dispatch_for_mode_gate")
        assert GATE in dispatch.GROUPS["pre-bash"]


test_census = census_case(TARGET)
