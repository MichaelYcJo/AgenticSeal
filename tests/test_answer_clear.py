"""`hooks/answer-clear.py`: the call that carried a consent token is over, so
the token is too (#692, P3, W6). Each case writes through
`hooks/answer-write.py` first, because there is nothing to clear until a call
has been written. The cases come from
`tests/test_the_old_spellings_reach_the_hook.py` (#942's phase 6).
"""

from conftest import A, census_case, load_hook_module, run, shell

TARGET = "hooks/answer-clear.py"

answers = load_hook_module("answers.py", "answers_under_test")

writer = load_hook_module("answer-write.py", "answer_write_under_test")
clearer = load_hook_module("answer-clear.py", "answer_clear_under_test")


class Test_module:
    def test_the_gates_write_before_the_call_and_clear_after_it(
        self, monkeypatch, tmp_path
    ):
        monkeypatch.setenv(answers.OVERRIDE, str(tmp_path))
        payload = {
            "tool_name": "Bash",
            "session_id": "s1",
            "tool_use_id": "toolu_a",
            "tool_input": {"command": A},
        }
        run(writer, monkeypatch, payload)
        assert answers.given("s1", "[no-review]", [shell(A)])
        run(clearer, monkeypatch, payload)
        assert not answers.given("s1", "[no-review]", [shell(A)])

    def test_a_payload_with_no_tool_use_id_is_keyed_by_its_command(
        self, monkeypatch, tmp_path
    ):
        monkeypatch.setenv(answers.OVERRIDE, str(tmp_path))
        payload = {
            "tool_name": "Bash",
            "session_id": "s1",
            "tool_input": {"command": A},
        }
        run(writer, monkeypatch, payload)
        assert answers.given("s1", "[no-review]", [shell(A)])
        run(clearer, monkeypatch, payload)
        assert not answers.given("s1", "[no-review]", [shell(A)])


test_census = census_case(TARGET)
