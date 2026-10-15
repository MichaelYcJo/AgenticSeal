### Added

- **Every pull request fails where a rule's `Enforced by:` target is gone.**
  `bin/rules --check` reads every rule file — `CLAUDE.md`, `CONTRIBUTING.md`,
  `agents/*.md`, `docs/*.md`, each skill's `SKILL.md` and `orchestration.md`,
  and `templates/*.md` — and resolves every `Enforced by:` target a renderer
  shows in them. A target that is gone, renamed, defined twice or a constant
  is exit 1, named by file, line and heading. One case of the suite runs it
  over the tree, so the fact is read wherever the suite runs: locally, in
  the sealer's broad gate, and on CI's three legs. It cannot tell a test that
  exists from one that asserts the rule, and a rule with no `Enforced by:`
  line is read by nobody.
  (`1791876665-each-budget-ratchets-and-every-pull-request-measures-it`,
  #930, #923)

- **A release pull request prints one table against the last release tag,
  and the table fails nothing.** The tests workflow's `release-report` job
  runs after the suite on a pull request into `main` only. It sets each
  agent's preload bytes, the suite's seconds, each CI leg's minutes and the
  bytes of `CLAUDE.md`, `CONTRIBUTING.md` and each `docs/*.md` beside the
  same reading at the tag, in the job's summary. A leg's minutes compare one
  run with one run, which swing on the same code, and the table says so.
  (`1791876665-each-budget-ratchets-and-every-pull-request-measures-it`,
  #930, #923)
