### Changed

- **Text an agent or a check reads has three writing rules of its own
  (#940).** `skills/writing-style/SKILL.md` states them in one section under
  its structure rules: no symbol used as syntax, no value stated twice and no
  shape a near miss passes; one word, one meaning; and an instruction names
  who acts, when, on which file and what counts as done. Each ends with the
  `check:` line naming what reads it, both language sections link the
  section, and the skill's description names this kind of text, so a session
  writing a skill, an agent definition, a template or a frame loads it.
- **The orchestrator's half of `implement` states the current rule, once
  (#940).** `skills/implement/orchestration.md` drops the history it
  narrated, says its order in words and names the party of each act. The
  approval line's shape is stated at the step where the orchestrator spawns
  the smith: `Approved <date> by <who>, when `smith` was spawned.`, ending
  at its full stop, with anything more on a line of its own. The routing
  section holds the reasoning the CLAUDE.md block no longer carries, and
  its headings are *Orchestrator: Bootstrap*, *Orchestrator: Parity setup*,
  *Orchestrator: how the work is routed*, *Question 1* and *Question 2*.
- **The CLAUDE.md block holds its rules alone, in 1,669 bytes, and has one
  copy (#940).** `templates/claude-md-block.md` keeps its four headings and
  eight rules and drops the reasoning, which is in
  `skills/implement/orchestration.md`. The routing rule says, in order: where
  no `seal/` root exists, follow the Bootstrap first, and where the root
  lands is the user's decision; ask question 1 alone, its answers
  `automation`, `per axis` and `no work item`, and the boxes in a second
  call only under `per axis`, with the orchestration file's routing section
  named as where the question and the boxes are stated; except under `no
  work item`, write `routing.md` in a command of its own before the first
  edit, then commit it; and under `no work item` put `: '[no-review]';` in
  front of every commit. The lint rule is scoped: before each commit, lint,
  format and typecheck run over the files the commit changes, and the
  repository-wide lint runs once after the rounds settle. `/specseal:update`
  replaces the block as before. The plugin's own repository no longer
  carries a generated copy in its `CLAUDE.md`, and the pull-request step that
  held the copy to the template is gone with the script it ran; a session in
  a clone of the plugin installs that clone's block with
  `bash install.sh "$HOME/.claude/CLAUDE.md"` run there, since `--project`
  would write a copy into the clone's `CLAUDE.md`.
- **The orchestrator's half of `code-review` states the current rule, once
  (#940).** `skills/code-review/orchestration.md` drops the measurements and
  issue history it narrated and names the party of each act. The step before
  the preflight says who writes the work item's `changelog.md`: the party
  that builds it, the smith, or the orchestrator where `routing.md` answers
  `Implementation` with `the session`. A redesign's second approval line
  takes the shape `skills/implement/orchestration.md` states at the spawn.
- **`verify` splits along its headings (#940).** The broad gate and the
  measurement of each segment, the two acts no agent takes, move to a new
  `skills/verify/orchestration.md`, which the orchestrator reads and the smith
  and the sealer do not. `skills/verify/SKILL.md`, titled *The Seal Test*,
  keeps the four conditions, `arm-check` and `mutation-check`, the hand-back's
  labels, the scope rule, the cost of a repeated run and the counterfeits, at
  about two fifths of its size, and names the party making a claim where it
  said "you". The section the closed flow-measurement log's comment cites
  is the new file's.
- **A branch cut from an issue carries the issue's number (#940).**
  `commit-pr-convention` *Branch names* states the shapes once:
  `<prefix>/<issue number>-<slug>` for a branch cut from an issue, two
  numbers joined by a hyphen for two issues, the slug alone for a change with
  no issue, and `release/vX.Y.Z` for a release branch. The smaller skills
  (`config`, `legacy-parity`, `gap-analysis`, `parity-setup`,
  `security-audit`, `testing`, `feature-planner`, `confidence-check`,
  `learn`, `audit`, `debug`, `build-fix`, `checkpoint`, `update`,
  `preset-setup`, and `writing-style`'s file for text outside a review) drop
  the history they narrated and the symbols used as separators, and name who
  acts. `/specseal:config` lists every row of its table where it used to
  count nine over eight.
- **The templates state the current rule (#940).** Every file under
  `templates/` drops the history and issue numbers it narrated, says in
  words what it drew with dashes, arrows and middle dots, and names who acts
  where it said "you" or gave a bare imperative. A record copied from a
  template is titled `Kind: id`, as `# Review round <N>: <work-item-id>`,
  the shape the spec and plan templates already had. `templates/config.md`'s
  criterion section is now *The criterion for choosing a value*, and
  `broad-gate`'s refusal names it so. The spec template's last section is
  `## Open questions`, and the comments of the plan, overview and routing
  templates link the rules they used to restate.
- **`CONTRIBUTING.md` states the current rule (#940).** It names the
  contributor where it said "you", drops the issue numbers and anecdotes it
  carried, and names the constant or the workflow file where it restated
  CI's job and shard counts, the case ceiling and the artifact's retention.
- **The orchestrator drains a work item's unresolved rows before the broad
  run (#940).** `skills/implement/SKILL.md` section 6, now *6. Drain the rows
  before the broad run, and keep the records*, names the orchestrator as the
  party and the moment as after the last round has no finding open and
  before `broad-gate --preflight`, since a commit after the broad run, a
  `seal/follow-up.md` row among them, leaves `broad-gate.md` stale for the
  sealer; it used to say only "before the PR merges". The orchestration
  file's step before the preflight names that drain among its
  preconditions, and `seal/README.md` and the questions template name the
  section instead of stating their own moment and destinations. The skills and templates cite a heading as the backticked path
  followed by the heading in italics, with no section sign; a citation of
  the agent contract's numbered sections keeps its number.
