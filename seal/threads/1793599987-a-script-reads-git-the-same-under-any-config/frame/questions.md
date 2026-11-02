# Questions for the planner: a script reads git the same under any config (#1283)

Judgments the issue left open that the tree or a probe answered. Each line
points at the row that holds its grounds.

- Where the rule's one home is: `frame/design.md` *Grounding*, the
  `docs/what-a-script-gates.md` row, and `## Rule changes`.
- A helper with `-c` over flags at each reader, and over dropping the
  person's config: `frame/plan.md` *Alternatives considered*, rows 1 to 3.
- `-z` over `core.quotePath=false` for readers of paths: `frame/plan.md`
  *Alternatives considered*, row 4.
- Only the `log` and `status` calls go through the helper, and no hook
  changes: `frame/design.md` *Scope*, items 2 and Out, and `frame/plan.md`
  *Alternatives considered*, row 5.
- No pin case, and the proofer reads the call-site rule: `frame/plan.md`
  *Alternatives considered*, rows 6 and 7.
- The per-reader key cases go: `frame/design.md` *Removes*, and
  `frame/plan.md` *Alternatives considered*, row 8.
- `i18n.logOutputEncoding` and `status.showUntrackedFiles` are in scope:
  `frame/design.md` *Grounding*, the measured table, and `frame/plan.md`
  *Alternatives considered*, row 9.
- The suite's own git calls are out: `frame/design.md` *Scope*, Out.
- The whole set of call sites: `frame/design.md` *Grounding*, the contract
  rule 12 row and the last row of the measured table.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Do the helper's key cases and the non-ASCII cases of phase 2 pass on the Windows and macOS legs of `.github/workflows/test.yml`? No probe can run here: those legs are CI runners on other platforms, and the framer ran on macOS with git 2.50.1 only. The signed-commit parameter skips where `ssh-keygen` makes no key, as the cases it replaces did | a measurement | green on both: nothing further. Red on one: the phase or fix pass that meets it reads the leg's log and fixes the case or the reader | build as framed; the orchestrator reads the legs on the pull request's test run | open |
