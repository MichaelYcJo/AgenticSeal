# Feature Specification: 1793171929-the-suite-tells-the-agent-it-is-evaluated

Issue #1042. The behaviour suite under `evals/behaviour/` shows the agent
under test three things that say the run is an evaluation: the commit author
of every rule scaffold, the sealer cases' input directory, and the temporary
directory `evals/scripts/noninferiority.py#run_side` loads the plugin from.
This work removes the words from all three and adds a case in `tests/` that
refuses them in every `prompt.md` and `scaffold.sh`.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CONTRIBUTING.md` *House rules*, and `CLAUDE.md` *Repo rule: no real identifiers in examples or fixtures* | The new author's address is at `example.com`. |
| `evals/README.md` *The behaviour suite*, the paragraph that opens "The cases are generated, never edited by hand" | Every changed `prompt.md` and `scaffold.sh` is written by its generator: `rule_cases.py` for the 14 `rule-*` cases, and `seed_defects.py --case <name>` for the four `seeded-*` cases. No case file is edited by hand. |
| `evals/README.md` *The behaviour suite*, the paragraph that opens "A side already paid for is read again" | A change to a prompt or a scaffold cannot be regraded from an earlier side. This work takes no side, and the next comparison takes both sides at the new suite (`## Scope`). |
| `CLAUDE.md` *The rule a mechanism is kept against*, the sentence "A fact has one source" | The author is one constant in `rule_cases.py`, and the sealer's input directory is one constant. Today the author is spelt out at five coordinates of that file. |
| `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test* | The new case is seen red against the suite as it stands before the generators change, and each scenario below names the case that holds it. |
| `tests/behaviour/test_evals_layout.py#test_the_sealer_cases_are_the_generators_output` | The committed sealer cases equal the generator's output byte for byte, so a generator change and its regenerated cases land in one commit. |

## Scope

**In.**

1. **The author.** Every commit a `rule-*` scaffold makes is authored and
   committed as `textutil <textutil@example.com>`. `textutil` is the name of
   the project every rule case builds (its `README.md` opens `# textutil`),
   so the author names a project and not an evaluation. The value is one
   constant in `evals/scripts/rule_cases.py`, and `BY` and `base_project` are
   built from it. Today it is written out at `:205`, `:280`, `:288`, `:370`
   and `:636` (read).
2. **The seeded amend.** `evals/scripts/seed_defects.py#scaffold` (`:313`)
   drops both `-c user.name=eval` and `-c user.email=eval@example.com`. The
   amend keeps the target commit's author, and `GIT_COMMITTER_NAME`,
   `GIT_COMMITTER_EMAIL` and `GIT_COMMITTER_DATE` give its committer, so the
   two flags set nothing the commit carries (read). Dropping only
   `user.name` would leave `eval@example.com` in all four scaffolds.
3. **The sealer's input directory.** The five sealer cases keep the issue
   body and the pull request body at `.git/<work-item-id>/issue-101.md` and
   `.git/<work-item-id>/pr-body.md`. That is the shape production uses,
   `<scratchpad>/<work-item-id>/pr-body.md`
   (`skills/code-review/orchestration.md`, the paragraph that opens "You
   write the pull request body after"), placed under `.git/` so the file is
   not part of the work tree the sealer guarantees. The prompts name that
   path. The constant is `evidence` in `rule_cases.py#sealer_case` (`:660`).
4. **The run's directory name.** `noninferiority.py#run_side` makes its
   temporary directory with `tempfile.mkdtemp(prefix="agentic-")` in place of
   `prefix="agentic-eval-"` (`:611`). The tree `claude plugin eval` loads is
   `<that directory>/tree`. Its path is in every skill preamble the agent
   reads, as the base directory of the skill, and on `PATH` through
   `side_path`.
5. **The case.** A new case,
   `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py`, reads every
   `evals/behaviour/*/*/prompt.md` and `scaffold.sh` and refuses six words
   (`## Data & interfaces` states the list and the exemptions). A second
   case, in `tests/evals/test_noninferiority.py` *Test_run_side*, refuses a
   directory `run` creates whose name holds one of those words. It takes the
   list from the first file, so the list has one home.
6. **The suite's own statement of the rule.** One paragraph in
   `evals/README.md` *The behaviour suite* states the rule and names the case.
7. **The regenerated cases.** All 14 `rule-*` cases are written again by
   `rule_cases.py`, and the four `seeded-*` cases by `seed_defects.py --case`.
   Regenerating the seeded cases also moves their
   `git remote add origin` URL from `https://github.com/MichaelYcJo/SpecSeal.git`
   to `https://github.com/MichaelYcJo/AgenticSeal.git`, because
   `replay_targets.py#origin_url` reads this clone's `origin`. That line is
   the only other difference (executed: each of the four regenerated into a
   scratch directory and compared with `diff -r`; the 14 rule cases
   regenerate with no difference at all).

**Out.**

- **The truth graders in the tree the agent loads.** The issue's third
  done-when line asks for a measured tree that holds no `truth-*.md` grader
  while the graders stay where `claude plugin eval` reads them. That command
  reads cases only below the plugin it loads: `--eval-dir ../empty` exits 1
  with `--eval-dir must stay inside the plugin root (no ..)`, and an absolute
  path exits 1 with `--eval-dir must be a relative path inside the plugin`
  (executed, `claude` 2.1.312, against an empty scratch plugin). The loaded
  plugin's `bin/` is on `PATH` (`bin/seal`'s header, read), so the two
  halves of that line cannot both hold. This work builds the directory name
  and leaves the graders where they are. `questions.md` Q1 asks the owner
  whether to grade truths outside the eval instead.
- **#992**, which comes after this work item: rule 5's statistic in
  `noninferiority.py#verdict`, its edits to `evals/README.md` and its re-read
  of recorded sides.
- **A paid side.** This work takes no side and regrades none. A side
  recorded before it cannot be regraded onto the new suite, and the issue
  pays for no new pair.
- **Words in `case.yaml`.** Its `tags` carry `fixture`, but the eval reads
  that file and the agent is shown only `prompt.md` (`evals/scripts/behaviour.py`
  module docstring: "`prompt.md` (the prompt and nothing else)", read).
- **This repository's own content in the `replay-*` and `seeded-*` cases.**
  The commits they check out carry their real authors, subjects and files.
  The case exempts those values (`## Data & interfaces`).
- **The installed plugin shipping `evals/`.** The plugin cache at 0.23.1
  holds `evals/behaviour/` with its graders (read: a directory listing).
  Packaging is not this issue's.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | Given a `rule-*` case's scaffold, when it has run, then every commit's author and committer is `textutil <textutil@example.com>` | `tests/behaviour/test_evals_layout.py#test_the_sealer_cases_are_the_generators_output` holds the sealer cases to the generator; S4's case refuses `eval` in every scaffold |
| S2 | Given a `seeded-*` scaffold run where git has no identity configured, when the amend runs, then it exits 0 and the commit keeps the target's author, committer and date | `tests/evals/test_seed_defects.py#Test_module::test_the_seeded_scaffold_leaves_round_1s_tree_and_no_copy_of_it`, run once with `HOME` set to an empty directory and `GIT_CONFIG_NOSYSTEM=1` |
| S3 | Given a sealer case, when its prompt is read, then it names `.git/<work-item-id>/issue-101.md` and `.git/<work-item-id>/pr-body.md`, and the scaffold writes both there | `tests/evals/test_rule_cases.py#Test_main::test_a_sealer_case_body_is_its_records_then_its_own_part`, its body path read from the generator's constant |
| S4 | Given every `evals/behaviour/*/*/prompt.md` and `scaffold.sh`, when the case reads them, then none holds a refused word outside the exemptions, and each hit is reported as its file, line and word | `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py`, seen red against the suite at `c825fd2c` before the generators change |
| S5 | Given a replay prompt whose generator's own text gains a refused word, when the case reads it, then the case refuses it, while the same word in the copied asked paragraph passes | the same file, shown red by planting the word in the generator's template text of a scratch copy |
| S6 | Given `noninferiority.py run` with the eval replaced by a fake, when it makes its temporary directory, then no component of that directory's path below the system temporary directory holds a refused word | `tests/evals/test_noninferiority.py#Test_run_side`, seen red with `prefix="agentic-eval-"` |

## Data & interfaces

**The refused words.** Case-insensitive, at the start of a word (preceded by
a character that is not a letter): `eval`, `evaluation`, `grader`, `judge`,
`fixture`, `scenario`, and their inflections. The case writes them as the
stems `eval`, `grader`, `judg`, `fixture` and `scenario`, so `evaluated`,
`graders`, `judged` and `scenarios` are refused too. `test` is not refused.
The list is one constant of the new file.

**The exemptions, each stated in the case with its reason.**

1. The record shapes this plugin's templates write, as whole lines:
   `## User scenarios & acceptance` and
   `| Scenario | Given / When / Then | Verifiable how |` (from
   `templates/records/sdd-design.md`, whose heading also carries
   ` *(mandatory)*`), and `## Not judged` (from
   `templates/records/sdd-round.md`). They occur in rule scaffolds today
   (executed).
2. In a `replay-*` or `seeded-*` case, every value its generator copies from
   this repository: the work item id, the branch, the report path, the base
   and its ref, the asked paragraph (`replay_targets.py#prompt`) or the
   commit subject (`seed_defects.py#prompt`), and the mutation's path, old
   line and new line (`seed_defects.py#scaffold`). Today these give `judge`
   in `replay-1791382684-r2/prompt.md`, `grader` twice in
   `seeded-8a100e13/prompt.md`, and `evals` in
   `seeded-8a100e13/scaffold.sh`'s mutation line (executed). The generator's
   own template text in those cases is not exempt.

Nothing else is exempt. Before this work the words hit 18 scaffolds and 7
prompts (executed, the enumeration over the stems above at `c825fd2c`).

**The constants that change.**

| Where | Before | After |
|---|---|---|
| `evals/scripts/rule_cases.py`, `base_project`, `proofer_case`, `crafter_case`, `BY` | `git -c user.name=eval -c user.email=eval@example.com commit -q -m`, written out five times | one author constant, `textutil` at `textutil@example.com`, read by `BY`, and `BY` used at all five sites |
| `evals/scripts/rule_cases.py#sealer_case`, `evidence` | `.git/agentic-eval` | `.git/<work-item-id>` |
| `evals/scripts/seed_defects.py#scaffold` | `git -c user.name=eval -c user.email=eval@example.com commit -q -a --amend --no-edit --no-verify` | `git commit -q -a --amend --no-edit --no-verify`, the three `GIT_COMMITTER_` variables unchanged |
| `evals/scripts/noninferiority.py#run_side` | `tempfile.mkdtemp(prefix="agentic-eval-")` | `tempfile.mkdtemp(prefix="agentic-")` |
| `tests/evals/test_rule_cases.py#Test_main::test_a_sealer_case_body_is_its_records_then_its_own_part` | reads the body at the literal `.git/agentic-eval/pr-body.md` | reads it at the path the generator's constant gives for the case |

## Rule changes

- nothing
  why: no section of the policy root `docs/` states how the behaviour suite's cases are written. The rule this work adds lives in `evals/README.md`, outside the policy root, and the case in `tests/text/` holds it.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The author `eval` at `eval@example.com`, written out five times | `evals/scripts/rule_cases.py#base_project`, `#proofer_case`, `#crafter_case` and `BY` | one author constant in the same file, read by `BY` |
| The two `-c user.name=eval -c user.email=eval@example.com` flags of the seeded amend | `evals/scripts/seed_defects.py#scaffold` | nothing needs them: the amend keeps the target's author, and the `GIT_COMMITTER_` variables give the committer |
| The sealer's input directory `.git/agentic-eval` | `evals/scripts/rule_cases.py#sealer_case` | the `.git/<work-item-id>` constant in the same function |
| The literal body path `.git/agentic-eval/pr-body.md` | `tests/evals/test_rule_cases.py#Test_main::test_a_sealer_case_body_is_its_records_then_its_own_part` | the generator's constant, read by the case |
| The temporary directory prefix `agentic-eval-` | `evals/scripts/noninferiority.py#run_side` | `agentic-` in the same call |
| The `user.name=eval` lines, the `.git/agentic-eval` paths, and the `SpecSeal.git` remote URL of the seeded cases | the 14 `evals/behaviour/*/rule-*/` and 4 `evals/behaviour/proofer/seeded-*/` case directories, their `prompt.md` and `scaffold.sh` | the generators' output, written again in the same commit as each generator change |

## Open questions

<none here: each is a row of `questions.md`>

Framed 2026-10-28 by framer, before the build.
