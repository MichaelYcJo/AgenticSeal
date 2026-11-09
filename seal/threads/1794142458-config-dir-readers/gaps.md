# Closing memo: 1794142458-config-dir-readers

## Not verified

| Item | Who must answer |
|---|---|
| closed whether Claude Code 2.1.319, started with `CLAUDE_CONFIG_DIR` set, writes a session's transcript under `<config>/projects/<slug>/`, which `session_cost.py#projects_dir` now reads; `frame/design.md` G4 reads this from the binary's strings, `frame/questions.md` Q1 asks only about `CLAUDE.md` and user skills, and no case runs a session under a set variable | a measurement no record asks for: the answer would decide whether `seal cost --latest` finds a session's transcript where the variable is set; no open issue, failed run or other work item's rule waits on it, and nothing is opened |
| closed whether `Test_newest`'s cases pass on Windows, where `os.path.expanduser("~")` reads `USERPROFILE`, which `two_roots` sets beside `HOME`; phase 1 ran on macOS only | answered by run 42564261755, the `tests` run of the 0.36.0 release pull request #1457: each of its four `windows-latest` pytest jobs passed, and none of their 34 `SKIPPED` lines names `Test_newest`, read by the settling session with `gh run view 42564261755 --log` |
| closed whether `seal payload`'s rows name the files a session under a set `CLAUDE_CONFIG_DIR` loads: the user's `CLAUDE.md` and user skills in `<config>/`, which `payload_meter.py#user_dir` now places there; `frame/questions.md` Q1 stands open with its default, and phase 2 built on it | a measurement no record asks for: the answer would decide whether `seal payload` names the user files of a session under a set variable; no open issue, failed run or other work item's rule waits on it, and nothing is opened |
| closed whether the four `#1367` cases of `tests/skills/test_payload_meter.py#Test_module` pass on Windows, where the child's `expanduser("~")` reads `USERPROFILE`, which `run` sets beside `HOME`; phase 2 ran on macOS only | answered by run 42564261755, the `tests` run of the 0.36.0 release pull request #1457: each of its four `windows-latest` pytest jobs passed, and none of their 34 `SKIPPED` lines names a `#1367` case of `Test_module`, read by the settling session with `gh run view 42564261755 --log` |

## Not done

nothing
