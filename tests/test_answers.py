"""`hooks/answers.py`: the old consent spellings, kept for one Bash call only
(#692, `questions.md` P3 answer (a), W6).

`hooks/tokens.py` reads the bare words, this module keeps them for the call
that carried them, and `hooks/answer-write.py` and `hooks/answer-clear.py`
write and clear around the call. What a hook does with an answer is
`tests/e2e/commit/test_commit_flow.py`'s. The cases come from
`tests/test_the_old_spellings_reach_the_hook.py` (#942's phase 6).
"""

import os
import time

import pytest
from conftest import A, B, census_case, load_hook_module, shell

TARGET = "hooks/answers.py"

answers = load_hook_module("answers.py", "answers_under_test")


class Test_given:
    @pytest.mark.rule("how-a-stop-is-put")
    def test_accepts_an_answer_for_the_call_that_carried_it_and_no_other(
        self, tmp_path
    ):
        """Round 1's 🟡 9: the parent and every subagent share one session id, so
        a token keyed by the session alone waived another agent's commit while
        the call that carried it ran."""
        root = str(tmp_path)
        answers.write("s1", "call-a", A, ("[no-review]",), root=root)
        assert answers.given("s1", "[no-review]", [shell(A)], root=root)
        assert not answers.given("s1", "[no-review]", [shell(B)], root=root)
        assert not answers.given("s1", "[no-parity]", [shell(A)], root=root)
        assert not answers.given("s2", "[no-review]", [shell(A)], root=root)
        assert not answers.given("s1", "[no-review]", [], root=root)

    @pytest.mark.parametrize(
        "command",
        [
            ": '[no-review]'; echo \"it's\" && git commit -m x",
            ": '[no-review]'\ngit commit -m x",
            ": '[no-review]'; git commit -m 'é 한글'",
        ],
        ids=["a quote", "a newline", "non-ascii"],
    )
    def test_accepts_the_shells_own_spelling_of_the_command(self, tmp_path, command):
        root = str(tmp_path)
        answers.write("s1", "call-a", command, ("[no-review]",), root=root)
        printed = shell(command).replace("é", "\\303\\251")
        assert answers.given("s1", "[no-review]", [printed], root=root)

    def test_accepts_an_answer_stamped_a_clock_tick_ahead_and_not_one_far_ahead(
        self,
        tmp_path,
    ):
        """#692's Windows pass: on `windows-latest` an answer's file read its
        stamp ahead of a `time.time()` taken right after the write, by under a
        microsecond, in 401 of 3,000 writes, so a different case of
        `Test_given::test_accepts_the_shells_own_spelling_of_the_command`
        failed in each run. One tick of the coarse clock is allowed here, more
        than was measured; a stamp set well into the future is still no
        answer."""
        root = str(tmp_path)
        answers.write("s1", "call-a", A, ("[no-review]",), root=root)
        stamped = os.stat(tmp_path / "s1" / "call-a" / "no-review").st_mtime
        tick = 0.016
        assert answers.given(
            "s1", "[no-review]", [shell(A)], root=root, now=stamped - tick
        )
        assert not answers.given(
            "s1", "[no-review]", [shell(A)], root=root, now=stamped - 3600
        )

    def test_refuses_to_read_the_argv_where_no_answer_is_there(self, tmp_path):
        def unread():
            raise AssertionError("the process table was walked for nothing")

        assert not answers.given("s1", "[no-review]", unread, root=str(tmp_path))

    def test_refuses_an_answer_older_than_a_bash_call_can_run(self, tmp_path):
        root = str(tmp_path)
        answers.write("s1", "call-a", A, ("[no-review]",), root=root)
        path = tmp_path / "s1" / "call-a" / "no-review"
        old = time.time() - answers.FRESH - 5
        os.utime(path, (old, old))
        assert not answers.given("s1", "[no-review]", [shell(A)], root=root)


class Test_write:
    def test_accepts_a_new_call_and_prunes_the_one_left_behind(self, tmp_path):
        """A call another gate denied never reaches `post-bash`."""
        root = str(tmp_path)
        answers.write("s1", "call-a", A, ("[no-review]",), root=root)
        old = time.time() - answers.FRESH - 5
        os.utime(tmp_path / "s1" / "call-a", (old, old))
        answers.write("s1", "call-b", B, (), root=root)
        assert not (tmp_path / "s1" / "call-a").exists()

    @pytest.mark.rule("how-a-stop-is-put")
    def test_refuses_to_replace_or_clear_another_calls_answer(self, tmp_path):
        """The other half of 🟡 9: the writer cleared the session's answers for
        every new call, so a second agent's Bash call took the first's away."""
        root = str(tmp_path)
        answers.write("s1", "call-a", A, ("[no-review]",), root=root)
        answers.write("s1", "call-b", B, (), root=root)
        answers.clear("s1", "call-b", root=root)
        assert answers.given("s1", "[no-review]", [shell(A)], root=root)
        answers.clear("s1", "call-a", root=root)
        assert not answers.given("s1", "[no-review]", [shell(A)], root=root)

    def test_refuses_a_session_or_call_id_that_names_a_directory_outside(
        self, tmp_path
    ):
        answers.write(
            "../../escaped", "c", A, ("[no-review]",), root=str(tmp_path / "a")
        )
        answers.write(
            "s1", "../../escaped", A, ("[no-review]",), root=str(tmp_path / "a")
        )
        assert not (tmp_path / "escaped").exists()
        assert answers.directory("..") == ""

    @pytest.mark.parametrize("token", ["[shared-tree-ok]", "[worktree-ok]"])
    def test_refuses_to_carry_the_tree_answers(self, tmp_path, token):
        """The switch and creation arms decide before git runs and read their own
        tokens from the command (option 1, P6), so nothing is written for them."""
        assert answers.write("s1", "c", A, (token,), root=str(tmp_path)) == []


class Test_module:
    def test_two_calls_are_kept_apart_by_id_and_by_command(self):
        assert answers.call_id("toolu_a", A) != answers.call_id("toolu_b", A)
        assert answers.call_id(None, A) != answers.call_id(None, B)
        assert answers.call_id(None, A) == answers.call_id("", A)

    def test_the_store_lives_under_the_plugins_own_directory(self, monkeypatch):
        monkeypatch.delenv(answers.OVERRIDE, raising=False)
        assert answers.root_dir() == os.path.join(
            os.path.expanduser("~"), ".claude", "specseal", "answers"
        )

    def test_the_override_names_the_store_where_it_is_set(self, monkeypatch, tmp_path):
        """Red where `root_dir` does not read `SPECSEAL_ANSWERS`. The old file's
        case of a payload with no `tool_use_id` killed that mutant at 714f2df2,
        through the answers the store under the home directory kept, and no
        case at the head did (#942's round 3 fix pass, a17)."""
        monkeypatch.setenv(answers.OVERRIDE, str(tmp_path))
        assert answers.root_dir() == str(tmp_path)


test_census = census_case(TARGET)
