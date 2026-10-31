# Questions for the planner: 1793457436-row-deletion-check-and-a-symlink

The issue left these judgments open, and the tree answered each one. They are not reopened:

- Whether to prefer the real file or to refuse to compare: `frame/plan.md` *Alternatives considered*, the chosen row and the literal-box row.
- Whether the `show()` decoding box still needs a fix: `frame/design.md` *Grounding*, the row on `#show`.
- Whether the defect still stands after #1198: `frame/design.md` *Grounding*, the first probe row.
- What a link to a file outside the repository does once the real path is kept: `frame/design.md` *Grounding*, the second probe row.
- Whether a rule changes: `frame/design.md` *Rule changes*.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Do the new link cases run on the Windows legs of `.github/workflows/test.yml`, or skip there? No probe can answer this from here. The answer is a behaviour of a CI leg on another platform, and #1221 records that no Windows run names its skipped cases. | a measurement | Run: the cases hold on Windows too. Skip: they hold on the ubuntu and macOS legs alone, and #1221 owns naming the skip. | The cases make their links through `tests/conftest.py#symlink_or_skip`, and the ubuntu and macOS legs are the evidence that they hold. | open |
