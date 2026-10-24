"""`hooks/answer-write.py`: before a Bash call runs, the old consent tokens it
carries are kept for that call (#692, P3). The cases come from
`tests/test_the_old_spellings_reach_the_hook.py` (#942's phase 6).
"""

from conftest import A, census_case, load_hook_module, run, shell

TARGET = "hooks/answer-write.py"

answers = load_hook_module("answers.py", "answers_under_test")

writer = load_hook_module("answer-write.py", "answer_write_under_test")


class Test_main:
    def test_accepts_two_calls_carrying_tokens_at_once_and_keeps_each_its_own(
        self, monkeypatch, tmp_path
    ):
        monkeypatch.setenv(answers.OVERRIDE, str(tmp_path))
        c = ": '[no-parity]'; git commit -m c"
        for call, command in (("toolu_a", A), ("toolu_c", c)):
            run(
                writer,
                monkeypatch,
                {
                    "tool_name": "Bash",
                    "session_id": "s1",
                    "tool_use_id": call,
                    "tool_input": {"command": command},
                },
            )
        assert answers.given("s1", "[no-review]", [shell(A)])
        assert not answers.given("s1", "[no-review]", [shell(c)])
        assert answers.given("s1", "[no-parity]", [shell(c)])

    def test_refuses_another_tool(self, monkeypatch, tmp_path):
        monkeypatch.setenv(answers.OVERRIDE, str(tmp_path))
        run(
            writer,
            monkeypatch,
            {
                "tool_name": "Write",
                "session_id": "s1",
                "tool_input": {"command": "[no-review]"},
            },
        )
        assert not answers.given("s1", "[no-review]", ["[no-review]"])


test_census = census_case(TARGET)
