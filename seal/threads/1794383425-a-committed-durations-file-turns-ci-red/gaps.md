# Closing memo: 1794383425-a-committed-durations-file-turns-ci-red

## Not verified

| Item | Who must answer |
|---|---|
| `test.yml`'s `pytest` job installing `PyYAML==6.0.3` from a wheel on the ubuntu, macOS and Windows legs. The wheels were read on PyPI by the framer, and no runner was used here | this work item's pull request run on GitHub's runners, read by the orchestrator |
| `publish-release.yml`'s `seal` job installing `PyYAML==6.0.3`. That job runs only when a release tag is published | the `publish-release.yml` run at the 0.37.4 tag, read by the repository owner who publishes it |
| The full suite, lint and format over the tree | the orchestrator, at the broad gate |

## Not done

nothing
