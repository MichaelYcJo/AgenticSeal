# Closing memo: the release pull request opens after the last work item merges (#1258)

## Not verified

| Item | Who must answer |
|---|---|
| closed Whether 0.27.3's release pull request runs `tests` once, on the tree it ships, with no `pull_request` run before the last merge into `release/v0.27.3` (`frame/design.md` S2, `frame/questions.md` Q1). No run can answer it before that pull request exists | answered: the last pull request into `release/v0.27.3`, #1278, merged at 2026-11-01T16:40:38Z, #1279 opened at 16:41:22Z, and `gh run list --branch release/v0.27.3 --workflow test.yml --event pull_request` lists one run, 41327609252 at `c3e02096`, success |

## Not done

nothing
