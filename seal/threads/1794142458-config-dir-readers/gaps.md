# Closing memo: 1794142458-config-dir-readers

## Not verified

| Item | Who must answer |
|---|---|
| whether Claude Code 2.1.319, started with `CLAUDE_CONFIG_DIR` set, writes a session's transcript under `<config>/projects/<slug>/`, which `session_cost.py#projects_dir` now reads; `frame/design.md` G4 reads this from the binary's strings, `frame/questions.md` Q1 asks only about `CLAUDE.md` and user skills, and no case runs a session under a set variable | the repository owner, at the first `seal cost --latest` in a session started with `CLAUDE_CONFIG_DIR` set |
| whether `Test_newest`'s cases pass on Windows, where `os.path.expanduser("~")` reads `USERPROFILE`, which `two_roots` sets beside `HOME`; phase 1 ran on macOS only | CI's Windows leg, at the pull request |
| whether `seal payload`'s rows name the files a session under a set `CLAUDE_CONFIG_DIR` loads: the user's `CLAUDE.md` and user skills in `<config>/`, which `payload_meter.py#user_dir` now places there; `frame/questions.md` Q1 stands open with its default, and phase 2 built on it | the repository owner, by Q1's measurement in a signed-in session started with the variable set |
| whether the four `#1367` cases of `tests/skills/test_payload_meter.py#Test_module` pass on Windows, where the child's `expanduser("~")` reads `USERPROFILE`, which `run` sets beside `HOME`; phase 2 ran on macOS only | CI's Windows leg, at the pull request |

## Not done

nothing
