# Questions for the planner: 1793504229-a-linked-memo-named-as-the-argument

The issue left these judgments open, and the tree or a probe answered each one. They are not reopened:

- Whether to resolve only the argument's directory, as #19's memo suggests: `frame/plan.md` *Alternatives considered*, the directory-only row.
- Which repository an argument is compared in when a link on its path leads elsewhere: `frame/plan.md` *Alternatives considered*, the chosen row and the deepest-link row.
- Whether a named directory link and a named path under a linked directory belong to this work: `frame/design.md` *Grounding*, the first probe row (P2 and P3).
- Whether a link to a memo in a second repository is fixed here: `frame/design.md` *Scope*, *Out*, the first item.
- Whether the comment #1235 edits must change: `frame/design.md` *Grounding*, the row on #1235.
- Whether a rule changes: `frame/design.md` *Rule changes*.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Do the new link cases run on the Windows legs of `.github/workflows/test.yml`, or skip there? No probe can answer this from here. The answer is a behaviour of a CI leg on another platform, and #1221 records that no Windows run names its skipped cases. | a measurement | Run: the new reader holds on Windows too, where `os.path.realpath` also resolves the link. Skip: the cases hold on the ubuntu and macOS legs alone, and #1221 owns naming the skip. | The cases make their links through `tests/conftest.py#symlink_or_skip`, and the ubuntu and macOS legs are the evidence that they hold. The build does not wait on it. | open |
