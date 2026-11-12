# Questions for the planner: 1794465690-a-passing-release-note-reads-like-a-failure

The ticket left these judgments open, and the tree answered each one. They are not questions:

- How the new header stays findable exactly once by the seal's reading: `frame/design.md` G5, and `frame/plan.md` *Alternatives considered* A1 to A4.
- Whether the sealed header is written on one source line or on several: `frame/design.md` G10 and G11, and `frame/plan.md` A6.
- The colour of a label the issue does not name, such as `outside contributors`, or one added later, and of a `not read` value: `frame/plan.md` A9.
- Whether the pull request edits `docs/releasing/branch-and-release.md` or states the change for the settle: `frame/design.md` G4.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does the release page draw the one-line paragraph headers of `frame/design.md` *Data & interfaces* as the `/markdown` endpoint did (G11, G12): the seal floated left, the badges of one line side by side, and the float cleared before the theme? | a measurement | A draft release whose body holds both headers, read back through `gh api` with `Accept: application/vnd.github.html+json` as the owner did on 2026-11-10, or the 0.38.0 note itself after its seal job runs. If the page differs, the header's shape changes before 0.38.0 is tagged, or in a patch after it. No framer probe could answer this, because the probe would have to create a release on GitHub, and a framer makes no write outside its scratch directory. G9 shows that the endpoint strips a table's `border` and `style` just as the issue records for the release page, which supports the default. | The release page renders as the `/markdown` endpoint does | open |
