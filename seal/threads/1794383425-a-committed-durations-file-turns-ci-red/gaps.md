# Closing memo: 1794383425-a-committed-durations-file-turns-ci-red

## Not verified

| Item | Who must answer |
|---|---|
| `test.yml`'s `pytest` job installing `PyYAML==6.0.3` from a wheel on the ubuntu, macOS and Windows legs. The wheels were read on PyPI by the framer, and no runner was used here | this work item's pull request run on GitHub's runners, read by the orchestrator |
| `publish-release.yml`'s `seal` job installing `PyYAML==6.0.3`. That job runs only when a release tag is published | the `publish-release.yml` run at the 0.37.4 tag, read by the repository owner who publishes it |
| The full suite, lint and format over the tree | the orchestrator, at the broad gate |
| The four modules phase 2 rewrote, on the Windows and macOS legs. They open repository paths written with `/` through `tests/workflows.py#load` and `tests/conftest.py#read`, and ran here on macOS alone | this work item's pull request run on GitHub's runners, read by the orchestrator |

## Not done

A key written twice in one matrix entry is no longer refused. The removed walker refused it, and `yaml.BaseLoader` keeps the last value without a word (phase 2's record). A loader that refuses duplicate keys was within reach. It was not built because `frame/design.md` *Data & interfaces* fixes `load` as the mapping `yaml.BaseLoader` returns, and a second parsing rule there would go beyond the frame. Whether GitHub's own workflow parser refuses a duplicated key, which would turn such a run red on its own, was not read here. The orchestrator or the proofer decides whether this needs a row in `frame/questions.md`.

`tests/text/test_a_merged_ticket_says_so_on_the_tracker.py:23` still cites the measured reason of a helper in `tests/text/test_ci_gives_the_checks_what_they_need.py`, and phase 2 removed that helper. The docstring belongs to `#workflow_settings`, a reader in the class *Scope* item 4 enumerates, so phase 3 removes it together with that reader. A one-line edit now would be rewritten by phase 3.
