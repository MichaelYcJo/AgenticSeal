# Questions for the planner: the README names every network place (#1382)

The tree answered these judgments that the issue left open. Each line points
at where the grounds stand, so nobody reopens them:

- Whether the README names only the issue's four places or every place the
  census finds: `frame/plan.md` *Alternatives considered*, row 3.
- When `seal cost --post` runs: `frame/design.md` *Grounding*, the row for
  `docs/running/measuring-a-run.md` *Where a reading goes* and
  `skills/verify/orchestration.md`.
- Whether `seal gate` reaches the network: `frame/design.md` *Grounding*,
  census row 5.
- Whether the `.github/scripts/` network calls and `bin/test` count as the
  installed plugin's: `frame/design.md` *Grounding*, *What the census left
  out, and why*.
- The shape of the passage, a kept paragraph and one new table:
  `frame/plan.md` *Alternatives considered*, rows 1 and 2.
- Whether the policy paragraph and the hook's docstring change too:
  `frame/plan.md` *Alternatives considered*, row 7.
- Whether a check holds the list: `frame/plan.md` *Alternatives
  considered*, row 4.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Should `CONTRIBUTING.md` *House rules*, the bullet **Hooks stay local and quiet**, widen "Every hook that reaches the network is named in the README's privacy section" to every place the shipped plugin reaches the network, commands and workflow steps included? The tree cannot answer it, because it is a choice of contributor policy that the issue scoped out ("Nothing else changes"). No probe settles a choice of what a contributor must do | a person | (a) Leave it. The hook rule stays as it reads, and a new command's network call is held by review alone. (b) Widen it to every shipped network call. A contributor adding a `gh` call to a skill then adds a README row, but the hook-shaped conditions (an opt-in, a throttle, silence on failure) would need rewording for commands, and `docs/running/measuring-a-run.md` *Where a reading goes* argues against applying them to `--post` | (a): the rule is left as it reads, and this work builds on that | open |
