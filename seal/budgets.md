# Budgets

<!-- What this repository holds its own size and speed to, one row per
budget. `.github/scripts/budget_check.py` measures each row on every pull
request and holds it to its ceiling from both sides; its docstring states the
band, the ratchet and the `Budget raised:` line a raise needs in the pull
request body. A ceiling moves in the same pull request as the change that
moves the measurement. -->

## Budgets

| Budget | Unit | Ceiling | Slack | Kind |
|---|---|---|---|---|
| preload:warden | bytes | 102229 | 2 % | gate |
