# Closing memo: 1795860192-mutate-tests-without-a-shell

## Not verified

| Item | Who must answer |
|---|---|
| The broad gate: the full suite, the repository-wide lint and the format check | the orchestrator |
| The refusal on a Windows runner, where a backslash is no escape; the cases drive both readings from this machine, and the `windows-latest` leg runs them there | the pull request's CI |

## Not done

`$( )`, backticks and `$VAR` are not refused, as `frame/design.md` *Scope* states under *Out*.
