# Implementation Plan: 1793157214-the-pr-bodys-facts-come-from-the-records

Approved 2026-10-28 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phase 1.
Approved 2026-10-28 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phase 2.

## Summary

Three phases, each a fresh crafter, each leaving the tree green under its
own narrow run. Phase 1 builds `seal pr-body`: the module that copies a work
item's records into the generated part of a pull request body and checks a
body against them, its subcommand, its cases, and the literals it reads on
the no-row list. Phase 2 rewrites the readers: the orchestrator's section
on opening the pull request runs the command, the sealer checks the copy
and reads only the orchestrator's part, and the prose and language rules
for a body name the two parts. Phase 3 writes the sealer's eval fixtures in
the new body shape and writes the changelog fragment.

## Technical context

**Who writes the body today, and who reads it.**
`skills/code-review/orchestration.md:214-237` has the orchestrator write
the body to a file once the rounds settle, before `seal gate --preflight`,
then run the broad gate, commit `trail/gate.md` and spawn the sealer with
the file. `:166-168` opens the pull request with that file
(`gh pr create --body-file <that file>`), and `:204-207` gives a repaired
body to an open pull request with `gh api -X PATCH`. `:254-259` sends a
`withheld` whose repair touches only the records or the body back to the
sealer at the new HEAD. `agents/sealer.md:33-38` reads the file the prompt
names; step 2 (`:64-67`) reads it with the other parties, step 4 (`:74-78`)
weighs it as one of five stories, and *Never* (`:105-107`) counts
`the pull request body's list of changes` among the claims.

**What the withheld verdicts were over.** The guarantee histories, read on
the feature branches with `git log -p` (executed):

| Work item | Withheld over the body | The record the sentence restated |
|---|---|---|
| #1051, `b3d1c521` | a Windows failure of run 40497220069 left out; a `seen red` carried from `trail/rounds/round-1.md:48` that held only where `~/.claude/agentic/` existed; the chain check's refusal left out | a CI run, which no record holds; a round record's answer; the gate's printed output |
| #1051, `8e71764d` | `pr-body.md:27` said four review rounds, and the list ended at round 4, while `trail/rounds/` held five | `trail/rounds/` |
| #1060, `9057b5e3` | five sentences that claimed more than `trail/phases/phase-1.md`, `phase-3.md`, `phase-4.md` and `phase-5.md` said, and *Decisions left* naming Q1 and leaving out Q2, `open` | the phase records; `frame/questions.md` |
| #857, `698f323c` | item 5 said the owl's entry draws three files again where its command draws one; *Decisions left* left out Q2, `open` | `assets/seals/README.md`, which the changelog entry described; `frame/questions.md` |

A copied *Review rounds* section closes the round count of `8e71764d`. A
copied *Questions* section closes the omitted rows of `9057b5e3` and
`698f323c`. A copied changelog closes the restated entry of `698f323c`. A
copied phase table, and an orchestrator's part that restates no record,
close the over-claiming phase summaries of `9057b5e3`. What stays with the
orchestrator is what no record holds: the CI run and the gate's printed
figures of `b3d1c521`. The sealer reads that part exactly as it reads the
whole body today.

**What the records hold, by their readers.** Round records have one reader,
`skills/code-review/scripts/chain_check.py`, which loads its grammar from
`docs/the-review-record.md` *The round record* at import (`:505-515`) and
splits a record with `read_whole` (`:1252`), `finding_spans` (`:948`) and
`finding_of` (`:1092`); its markdown reader is
`skills/verify/scripts/unverified_check.py` (`readable` at `:601`,
`headings` at `:623`), whose `HEADING` (`:134`) is `gaps.md`'s
`## Not verified`. `trail/gate.md` holds one `Broad gate` row, `<tree>
against <base>`, and nothing else (`skills/verify/scripts/broad_gate.py`,
the docstring's `--record` paragraph); the suite's counts are printed in
the panel and recorded nowhere. `changelog.md` holds no `## ` line
(`docs/the-record-layout.md` *A change writes fragments, never a shared
file*). `frame/plan.md`'s phases are its `## Phases` section
(`templates/records/sdd-plan.md`).

**Where a command goes.** `skills/implement/scripts/seal.py:127-180`
(`TOOLS`) maps each subcommand to its script; `seal.py#tool_command`
(`:2814`) runs it with every argument handed on. A new entry is held by
`tests/skills/test_seal.py`'s
`Test_main::test_accepts_each_tool_and_hands_its_script_every_argument`
(`:3800-3832`, a parametrize row per tool),
`tests/behaviour/test_a_reference_root_is_read_and_never_taken.py`'s
`SHIPPED` (`:54-71`), and
`tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py`'s
`SUBCOMMANDS`, whose `test_the_enumeration_is_not_empty` (`:444`) states
the count 13. The module's test file stands in `tests/skills/` by
`skills/verify/scripts/test_layout.py`'s area rule.

**The no-row list.** `templates/setup/config.md:110-146` lists what stays
English. `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#_literal_strings`
(`:1094-1122`) derives the checkers' literals from their constants and
`test_the_exclusion_list_holds_every_string_a_checker_matches` asserts each
one stands in the list, backticked.

**The pins on what this work rewrites.**
`tests/text/test_the_rules_have_one_owner.py#test_the_orchestrator_writes_the_body_file_the_sealer_reads`
(`:208-222`) pins `once you have written the pull request body to a file`,
`the issue and the file holding the pull request body`, the
`--body-file` command and the `PATCH` command.
`tests/behaviour/test_the_sealer_guarantees.py:209-227` pins
`a file holding the pull request body` and
`or is given it where already open` in the sealer's introduction.
`tests/text/test_the_chain_section_has_one_shape.py:63-80` pins
`the comparison table first, then what the rounds found`.
`evals/scripts/rule_cases.py:559-565` (`PR_BODY`) is the sealer fixtures'
body, written at `:687`, and `tests/behaviour/test_evals_layout.py:248-252`
holds the committed cases equal to the generator's output.

**This run's own parties are the installed plugin's.** The contract this
framer received names its base directory under
`~/.claude/plugins/cache/agenticseal/agentic/0.23.0/` (read, at this
framer's startup), so this work item's sealer reads `agents/sealer.md` as
0.23.0 ships it and reads the whole body. The orchestrator can write this
work item's own body with the tree's `bin/seal pr-body` once phase 1 has
landed; the installed sealer then reads the generated part as an ordinary
part of the body.

**The failure scenario of the chosen approach.** In six months a record
gains a section the body should carry, such as a new heading in
`templates/records/sdd-gaps.md`, and nobody adds it to the generator; the
body stops carrying that fact and nothing says so. Or a template renames
`## Phases`, and every body then reads
`` `frame/plan.md` is not in this work item. `` style lines where a
section stood; that one is visible, and `## Phases` is on the no-row list
so a translated plan keeps the spelling. The second risk is the
orchestrator's part growing back into a restatement of the records; the
sealer still reads that part against the tree, so the cost returns to
today's and goes no higher.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep the hand-written body, which the sealer reads whole (keep the structure) | The premise that keeps it is that an orchestrator writing with the records open restates them correctly. Checked against the three guarantee histories of this release: four of five withheld runs were a restatement that was wrong, each costing a body repair and a whole sealer run | Rejected |
| The command copies the records into the part above `HEADING`, and the orchestrator writes the rest under it (chosen) | A record section the generator does not copy is silently absent from the body; stated as the failure scenario above | Chosen |
| The command writes a summary: a count of rounds, a count of findings by severity, one line per phase | A count or a summary computed by code is a second statement of the records, and its rounding or its omission is the same defect moved into code. `questions.md` Q5 keeps the count line as the other answer | Rejected |
| The body links the records and copies nothing | `skills/writing-style/SKILL.md` asks that a reader learn what changed without opening a file, and the thread leaves the tree at the settle after the release, so a path stops opening | Rejected |
| The generator copies every record whole: `gaps.md` with its divergences, the whole `frame/questions.md`, the whole `frame/plan.md` | #1051's `changelog.md`, `gaps.md`, `frame/questions.md`, `frame/plan.md` and `trail/gate.md` whole, with its rounds' copied lines, measure 61,338 bytes (executed: `wc -c` at `4420ebd5`; its `gaps.md` is 16,223 and its `frame/plan.md` 16,912), close to GitHub's body limit before the orchestrator writes a word, for sections today's bodies do not carry | Rejected |
| Only `open` rows of `frame/questions.md` are copied | The filter reads a `Status` value, and a record written in another language spells it otherwise, so an open row drops out without a word: the omission #857 and #1060 were withheld for | Rejected: every table line is copied, and the `Status` cell says which are open |
| The orchestrator's part first, the generated part between two HTML comments | A reader on GitHub cannot see which text the sealer checked, and two markers are two spellings to keep | Rejected; `questions.md` Q1 holds the order |
| The orchestrator's part first under one heading, the generated part under a second | Two headings to keep in one spelling each, and the attribution line that ends a body falls inside the generated part | Rejected; `questions.md` Q1 |
| The sealer reads the generated part against the records itself, with no `--check` | The sealer spends each run comparing a copy by reading, which is a judgment where a byte comparison decides | Rejected |
| A CI arm compares the live pull request body with the records | A new gate for a body edited on GitHub after it opened, which the one-issue flow does not produce; `CLAUDE.md` *The rule a mechanism is kept against* asks for a history of what it would catch | Rejected: a limit sentence |
| `trail/gate.md` records the suite's counts, so the body copies them | Changes the gate record's grammar and `chain_check.py#broad_gate`'s reader, which the issue does not ask for | Rejected for this work item; the orchestrator's part states the figures |
| The module under `skills/verify/scripts/` | The body is the orchestrator's half of code-review (`skills/code-review/orchestration.md`), and the module reads round records through `chain_check.py` beside it | Rejected: `skills/code-review/scripts/pr_body.py` |
| Keep the stored count 13 and make it 14 | A number kept beside the tree to stay in step with it (`CLAUDE.md` *The rule a mechanism is kept against*); the equality beside it already refuses two tools sharing a script | Rejected: the count goes, the equality stays |

## Verification this work item owes

The owner decided this on 2026-10-27 for #1051, carried it to #1060 and
#857 on 2026-10-28, and carried it to this work item in the spawn of its
framer. It binds every crafter, proofer and sealer of this work item, and it
overrides any wording in the phase rows below.

- A case is written new, and seen red once, only for behaviour that did not
  exist before. The behaviour that is new here is the generator and its
  check (S1 to S9), the sealer's check of the copy (S13), the
  orchestrator's generating step (S12), the literals' derivation (S11) and
  the fixture's new body (S14). The phase rows name the cases.
- A name, a path or a sentence that moves is proved by the existing cases
  passing at the new place. It owes no new case, no red run and no
  `seal mutate`. A pin rewritten to a sentence this work rewrites is a
  move; a pin that holds a new rule is new and is seen red by deleting the
  sentence it pins. No phase runs `seal mutate`.
- A case that is removed, or a stored count taken out, owes no red run.
- A phase runs, in one `bin/test` command, the cases its row names plus the
  modules `git grep -l` finds reading what it changed. The orchestrator's
  broad run after the review rounds is the only sweep of the suite.
- A proofer does not raise a finding that a moved name lacks red-first
  evidence or a mutation run. A sealer does not withhold over it.
- Each phase record names the cases it wrote new, how each was seen red,
  and the existing cases it relied on.
- No phase runs a paid eval. `questions.md` Q4 holds the sealer evals.

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `skills/code-review/scripts/pr_body.py` with `HEADING`, `FIXED`, `Refused`, `read_item`, `compose`, `split` and `main`, as `frame/design.md` *Data & interfaces* lays them out, its docstring holding the three limit sentences; `"pr-body"` in `seal.py#TOOLS` with its help line; the `("pr-body", "skills/code-review/scripts/pr_body.py")` row in `tests/skills/test_seal.py`'s tool parametrize; the `"seal pr-body"` row in `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py#SHIPPED`, classified `NO_WALK`; the stored `== 13` taken out of `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py:444`; `HEADING`, `## Phases` and `## Not done` added to `templates/setup/config.md` *What no row governs*, and `_literal_strings` extended to read them from `pr_body.py`'s constants | New cases in `tests/skills/test_pr_body.py`, each seen red once against the tree before the phase (the module absent, so each fails at import or at the missing name): `Test_compose` S1 to S6, `Test_split` S7, `Test_main` S8, S9 and S6's exit, `Test_read_item` accepting a work item and refusing a path that is not a directory; the extended `_literal_strings` seen red with one of the three list items deleted. Then one `bin/test` over `tests/skills/test_pr_body.py`, `tests/skills/test_seal.py`, `tests/skills/test_test_layout.py`, `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py`, `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py`, `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`, `tests/skills/test_chain_check.py` and the modules `git grep -l -e TOOLS -e "What no row governs" -- tests` lists; `bin/seal layout --check tests/skills/test_pr_body.py` exits 0; `bin/seal pr-body seal/threads/1793152332-the-stamps-mark-is-an-owl --body <scratchpad>/owl-body.md`, the output read by the crafter against that thread's records section for section, with what it found in the phase record | 7d38665c |
| 2 | `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*, rewritten in place: the body is written by `seal pr-body <item> --body <file>` after `trail/gate.md` is committed and before the sealer's spawn, the orchestrator writes its part under `HEADING` and restates no record there, and every repair of a record, the broad run again and a repaired body among them, runs the command again; `agents/sealer.md`: a step that runs `seal pr-body <item> --body <file> --check` and withholds on any exit but 0, naming the line it printed, and steps 2 and 4 and *Never* reading the part under the heading; `skills/writing-style/outside-the-review.md` *PR 본문에만 해당하는 것*, a paragraph on the two parts, and *검증한 것을 표로 남긴다* rewritten for the orchestrator's part; `skills/commit-pr-convention/SKILL.md` *Pull request bodies*, the chain section's sentence and the language of each part; `templates/setup/config.md` *Commit and pull request language*, the row governing the orchestrator's part; `README.md` and `README.ko.md`, the sealer's row; `skills/implement/orchestration.md` *Orchestrator: which of these acts runs itself*, the Grounds of the row for opening the pull request naming the sealer's check | New pins, each seen red by deleting the sentence it pins: S13 in `tests/behaviour/test_the_sealer_guarantees.py`; the new sentences of S12 in `tests/text/test_the_rules_have_one_owner.py#test_the_orchestrator_writes_the_body_file_the_sealer_reads`. Moved pins, proved by passing: the rewritten phrase of `tests/text/test_the_chain_section_has_one_shape.py`, and the language row's cases in `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`. Then one `bin/test` over those four modules, `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`, `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py`, `tests/text/test_a_moved_rule_leaves_its_definition.py` and the modules `git grep -l -e "pull request body" -e "agents/sealer.md" -e "outside-the-review" -e "commit-pr-convention" -- tests` lists; `git grep -n "list of changes" -- agents skills` matching nothing | 452cea8b |
| 3 | `evals/scripts/rule_cases.py`: each sealer case's `pr-body.md` holds `pr_body.compose` over the case's own records, then the hand-written part, `Closes #101.` with the untrue-body case's sentence before it; the records' placeholders spelt so `chain_check.py`'s grammar reads the fixture's round record, and filled by the scaffold in the body as in the records (`questions.md` Q6); the five `evals/behaviour/sealer/*/scaffold.sh` regenerated by `rule_cases.py`; the work item's `changelog.md` | A new case in `tests/evals/test_rule_cases.py`, seen red against the tree before the phase: each sealer case's body, its placeholders filled as the scaffold fills them, splits at `HEADING`, and its generated part equals `compose` over that case's records. Then one `bin/test` over `tests/evals/test_rule_cases.py`, `tests/behaviour/test_evals_layout.py`, `tests/behaviour/test_the_sealer_guarantees.py`, `tests/skills/test_pr_body.py` and the modules `git grep -l -e rule_cases -e "behaviour/sealer" -- tests` lists | |

## Operational impact

- **Every pull request routed through the review chain gets a body in two
  parts from the release that ships this.** The copied sections come first,
  then the heading `## Not from the records`, then the orchestrator's part.
  A repository's reviewers see the change the first time a body is written
  by an orchestrator on the new release.
- **A new withhold.** A body whose part above the heading is not what the
  records give is withheld, naming the line. Its repair is
  `seal pr-body <item> --body <file>` again, which keeps the orchestrator's
  part.
- **Where `Commit and pull request language` and `Record language` differ,
  the body is in two languages**: the copied part in the records', the
  orchestrator's part in the row's. No repository migrates; no row changes.
- **This run's own sealer is the installed 0.23.0's**, so it reads this
  work item's whole body as before, whichever way the body is written.
- **The sealer eval fixtures change.** Their committed scaffolds are
  regenerated in phase 3. Whether the five paid cases still grade as before
  is unverified; `questions.md` Q4 names who answers it.
- **`.test_durations`.** The new cases in `tests/skills/test_pr_body.py`
  and `tests/evals/test_rule_cases.py` are unpriced until a CI run's
  durations are committed; the orchestrator's broad run reads whether they
  stay under `STALE_SHARE`.
- No new dependency, no new environment variable, and no gate other than
  the sealer decides anything differently.
