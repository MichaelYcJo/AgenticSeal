# Closing memo: 1794383425-a-committed-durations-file-turns-ci-red

## Not verified

| Item | Who must answer |
|---|---|
| `test.yml`'s `pytest` job installing `PyYAML==6.0.3` from a wheel on the ubuntu, macOS and Windows legs. The wheels were read on PyPI by the framer, and no runner was used here | this work item's pull request run on GitHub's runners, read by the orchestrator |
| `publish-release.yml`'s `seal` job installing `PyYAML==6.0.3`. That job runs only when a release tag is published | the `publish-release.yml` run at the 0.37.4 tag, read by the repository owner who publishes it |
| The full suite, lint and format over the tree | the orchestrator, at the broad gate |
| The four modules phase 2 rewrote, on the Windows and macOS legs. They open repository paths written with `/` through `tests/workflows.py#load` and `tests/conftest.py#read`, and ran here on macOS alone | this work item's pull request run on GitHub's runners, read by the orchestrator |
| The eleven modules phase 3 rewrote, on the Windows and ubuntu legs. Each reads a workflow through `tests/workflows.py#load`, and they ran here on macOS alone | this work item's pull request run on GitHub's runners, read by the orchestrator |

## Not done

A key written twice in one matrix entry is no longer refused. The removed walker refused it, and `yaml.BaseLoader` keeps the last value without a word (phase 2's record). A loader that refuses duplicate keys was within reach. It was not built because `frame/design.md` *Data & interfaces* fixes `load` as the mapping `yaml.BaseLoader` returns, and a second parsing rule there would go beyond the frame. Whether GitHub's own workflow parser refuses a duplicated key, which would turn such a run red on its own, was not read here. The orchestrator or the proofer decides whether this needs a row in `frame/questions.md`.

Six readers that phase 3 rewrote take a script's shell comments off through `tests/conftest.py#code_lines`, and no case in their modules watches that. Two of them were run as a coverage probe and stayed green with the stripping removed: `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py#scripts` and `tests/behaviour/test_the_release_check_watches_what_ships.py#release_step` (phase 3's record). The other four are `tests/text/test_a_release_cannot_ship_an_untrue_milestone.py#guarded_script`, `tests/behaviour/test_the_release_seal_is_drawn.py`'s install reader, `tests/behaviour/test_the_gate_names_every_step_ci_runs.py#release_scripts` and the claims-check filter in `tests/behaviour/test_a_body_naming_two_issues_claims_one.py`. None of the scripts they read holds a shell comment that their strings match (read). The stripping keeps what the old readers did, which was to drop comment lines, and its rule has cases where it is the subject: `tests/test_conftest.py`'s `code_line` cases, the gate's B1 fixture and phase 2's fixture job. A fixture in each module was within reach. It was not built, because each would plant a comment in a copy of a workflow only to show a reading that `code_line`'s own cases already hold.
