# Questions for the planner: 1795736973-the-preflight-passes-where-a-round-is-owed

The judgments the issue left open that the tree answered, each with its grounds where it stands:

- Which of the issue's two outcomes: the preflight refuses and names the line. `frame/plan.md` *Alternatives considered*, A1 against A8.
- Whether the preflight skips the verifying-round reading or reads it and does not refuse: it reads it and prints it as a notice. `frame/design.md` `## Grounding`, the probe of `e902ea9a3`.
- Whether the broad run passes over the same line: it does, by the same arm. `frame/design.md` `## Grounding`, the probes of the 0.39.0 and 0.39.1 gate runs.
- How the gate learns what the check judged: by the exit code of a check run under `--sealing`, which judges as a ready pull request. `frame/plan.md` *Alternatives considered*, A1 against A2, A3 and A4.
- Whether the orchestrator's `--worktree` read after a fix pass changes: it does not. `frame/plan.md` *Alternatives considered*, A6.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does a fixture that the suite's gate and chain cases build, `a_sealed_run` among them, carry a records refusal that the check prints today as a notice under `--sealing` with no payload, and that the strict arm now fails? The framer could not answer it: the fixtures are built by the test modules, and a framer's probe runs no test module. | the work | None refuses: the cases stand as they are. One refuses: the phase repairs the fixture so that it holds settled records, since a fixture that only passes unstrict was passing over what CI refuses. The phase does not narrow the arm to keep the fixture | Phase 1 repairs any such fixture, and records each in its phase record | open |
