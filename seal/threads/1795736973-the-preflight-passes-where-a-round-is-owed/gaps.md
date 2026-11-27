# Closing memo: 1795736973-the-preflight-passes-where-a-round-is-owed

## Not verified

| Item | Who must answer |
|---|---|
| The broad gate at the branch's HEAD: the full suite, `uvx ruff check .` and `uvx ruff format --check .` over the whole repository, which no agent runs (contract rule 2) | the orchestrator, by `seal gate --base <base> --record <item>` after the rounds settle |

## Not done

`docs/checks/the-pull-request-check.md` *What the check reads at the pull request* still says that a run that observed no pull request prints and exits 0, with no clause for `--sealing`. The work item's subject is the code, so `frame/design.md` `## Rule changes` holds the new text and the settle after the release writes it (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*).
