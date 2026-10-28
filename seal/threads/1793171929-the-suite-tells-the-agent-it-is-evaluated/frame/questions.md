# Questions for the planner: 1793171929-the-suite-tells-the-agent-it-is-evaluated

## Answered by the tree, not to be reopened

- **The author is `textutil` at `textutil@example.com`.** The issue asks for
  a person or a project. Every rule case builds the project its `README.md`
  calls `textutil`, so the project's name is the one that reads as ordinary.
  A different name changes one constant and nothing else.
- **The sealer's input directory is `.git/<work-item-id>/`.** Production
  keeps the pull request body at `<scratchpad>/<work-item-id>/pr-body.md`
  (`skills/code-review/orchestration.md`). A scaffold can write only inside
  the clone, and `.git/` keeps the two files out of the work tree the sealer
  guarantees, as `.git/agentic-eval/` did.
- **Both `-c` flags leave the seeded amend, not only `user.name`.** Dropping
  `user.name` alone leaves `eval@example.com` in all four seeded scaffolds,
  which the new case refuses.
- **The seeded cases take the generator's whole output, remote URL
  included.** The README says the cases are generated and never edited by
  hand. Regenerated, each differs from the committed case only in the
  `git remote add origin` line, which moves from `SpecSeal.git` to
  `AgenticSeal.git` (executed). The scaffold removes the remote before the
  agent starts.
- **The rule cases regenerate with no other change.** All 14 committed rule
  cases equal `rule_cases.py`'s output at `c825fd2c` (executed), so the
  regenerated diff is this work's change and nothing else.
- **#1040 does not reach the generated prompts.** `rule_cases.py` builds its
  prompts from its own constants, `skills/code-review/scripts/pr_body.py`
  and `hooks/lib/optin.py#MARKER`, and reads no `agents/*.md` file and not
  `skills/agent-contract/SKILL.md` (read: the module's imports and
  `#orchestrate`). The sealer case directories keep their names, so
  #1040's check lines still resolve.
- **The new case reads `prompt.md` and `scaffold.sh` and not `case.yaml`.**
  The agent is shown the prompt and nothing else of the case file
  (`evals/scripts/behaviour.py` module docstring), and `case.yaml`'s
  `fixture` tag is read by the eval alone.
- **No rule of `docs/` changes.** `## Rule changes` holds the no-change
  block, and the suite's rule is a paragraph of `evals/README.md`.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | The issue's third done-when line asks for two things: the tree the agent's `PATH` reaches holds no `truth-*.md` grader, and the graders stay where `claude plugin eval` reads them. That command reads cases only below the plugin it loads, and it puts that plugin's `bin/` on `PATH`. So both cannot hold. Which half gives way? The tree cannot answer this, because it is a choice about what the measurement owes, and the issue states both halves as required | a person | (a) Keep the graders in the loaded tree and rename its temporary directory. The agent no longer sees the word in any path, but the truth graders stay one directory listing away under the plugin root its skill preamble names, as in every installed copy of the plugin. (b) Take `truth-*.md` out of the tree before the run and grade every truth after it. Proofer truths over a round record are already graded from `report_text` and lose nothing. The four sealer truths read `guarantee.md`, so the sealer case would print that file and `noninferiority.py`'s reader would keep it, which changes how the sealer is scored and edits the file #992 works in next. This is a work item of its own | (a). Phase 2 builds the rename only, and `gaps.md` names the third done-when line's first half as not done, with this row | open |
| Q2 | Does `claude plugin eval` load the plugin in place, so the base directory in the agent's skill preamble is `<run's temporary directory>/tree`? The CLI's help says results go to `<plugin>/<dir>/results/` and warns that files written there may be loaded as plugin components, which reads as in place, but no trace was opened | a measurement | Read the `Base directory for this skill:` line of one trace a side already saved under `<out>.raw/traces/`, at no cost. In place, Q1's option (a) leaves the graders under the root the agent is told. Copied elsewhere, the graders are less reachable than Q1 assumes | In place. No phase of this work depends on it | open |
| Q3 | Does the seeded amend run when git has no identity configured at all, as in the eval's sandbox home? The amend keeps the target's author and takes its committer from the three `GIT_COMMITTER_` variables, so it should, but no run without an identity was made | the work | Phase 1 runs the seeded scaffold case with `HOME` set to an empty directory and `GIT_CONFIG_NOSYSTEM=1`. If it exits 0, the flags go. If git asks for an identity, the amend takes the rule cases' author constant as its `-c` flags, and the phase records the divergence | Drop both flags, as the issue asks | open |
