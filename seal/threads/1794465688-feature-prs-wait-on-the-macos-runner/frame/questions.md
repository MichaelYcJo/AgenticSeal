# Questions for the planner: 1794465688-feature-prs-wait-on-the-macos-runner

The tree answered these judgments that the ticket left open. Their grounds stand where each line points:

- The mechanism that chooses the legs per base: `frame/plan.md` *Alternatives considered*, A1 against A2 to A6.
- Which bases drop the two legs: `frame/plan.md` *Alternatives considered*, A7.
- The check names of the moved legs: `frame/plan.md` *Alternatives considered*, A8, and `frame/design.md` G7 and G8.
- Whether ubuntu 3.14 caught anything on a feature pull request: `frame/design.md` G12.
- Who records the wait after, and from which runs: `frame/plan.md` *Operational impact*.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | On this pull request's first `pull_request` run, does GitHub read the anchored steps, run the `pytest (…)` jobs of `frame/design.md` *Scope* item 1, and report `pytest-wide` as skipped? And under which name does the skipped check show? No probe can answer it here: only a GitHub Actions run of the changed workflow shows it, and no subagent can trigger one. | a measurement | Those jobs run and `pytest-wide` is skipped: S1 holds. The workflow fails to parse on the alias: the build replaces the alias, and A6's copy is weighed again against a reusable workflow. The skipped check shows its `name` unexpanded: cosmetic, and the run is correct. | The run behaves as the documents of `frame/design.md` G3 to G5 say: those jobs run and `pytest-wide` is skipped. | open |
