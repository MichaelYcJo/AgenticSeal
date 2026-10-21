# Phase 7: 1792540458-on-demand-files-state-the-current-rule

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md holds what this
phase of the build did, written by the party that builds it when the phase
closes. It is the build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 7 |
| Commit | 5048ee94 |


## What this phase was asked

Every file under `templates/` but `claude-md-block.md` rewritten to the
current rule: `config.md`, `sdd-routing.md`, `sdd-round.md`, `sdd-plan.md`
with its comment linking the approval line's shape, `sdd-spec.md` with the
heading and the coordinate hint of `spec.md` Scope 8, `sdd-questions.md`,
`sdd-overview.md`, `sdd-phase.md`, `sdd-guarantee.md`, `seal-README.md`,
`pact.md`, `parity.md` and the comments of `hygiene.yml`. `templates/config.md`
*What no row governs* stays derived from the checkers' constants. Where the
criterion heading of `templates/config.md` is renamed, its citations in
`skills/config/SKILL.md`, `skills/verify/orchestration.md` and
`tests/test_the_rules_have_one_owner.py` move with it. Every imperative
sentence whose actor or condition the smith chose is listed here.

## What this phase found

**The frame holds for this phase, with two notes.** First, `seal/README.md`
is in no cell of `plan.md`, and `tests/test_first_setup_asks_once.py` holds
it byte for byte equal to `templates/seal-README.md`, so it was rewritten as
the template's copy (executed `diff`). Second, Scope 8's premise that no
script reads the `## Removes` coordinate column holds: `chain_check.py`
reads `path#unit` only on a round record's `location:` line (read
`skills/code-review/scripts/chain_check.py:876`). The hint now names the
citation form first and keeps `path#unit` for a unit of code, because
`coordinates.py`'s grammar is the later item's.

**The record titles carry no dash.** Every template that a record is copied
from now titles it `Kind: id`, the shape `sdd-spec.md` and `sdd-plan.md`
already had: `# Routing: <work-item-id>`, `# Review round <N>: …`,
`# Phase <N>: …`, `# Guarantee: …`, `# Overview: …`,
`# Questions for the planner: …`. No checker reads a title (executed
`git grep` over the scripts and the eval graders). Records already committed,
the test fixtures and the eval scaffolds keep the old title; each writes its
own text and none is read for it. This record and phases 8 and 9 take the new
title because they are written from the template as it now stands.

**Headings renamed** (S14, executed `git grep -F` for each old text outside
`seal/specs`, `changelog/` and `docs/`; none is cited in `docs/`, so no
`## Rule changes` item is added):

| Old | New |
|---|---|
| `templates/config.md` `### Choosing a value — the criterion` | `### The criterion for choosing a value` |
| `templates/sdd-spec.md` `## Open questions → questions.md` | `## Open questions` |
| `templates/seal-README.md` `# seal/ — what this plugin maintains` | `# What this plugin maintains in seal/` |
| `templates/seal-README.md` `## Export rules — drain before closing` | `## Export rules` |

The criterion's citations moved in the same commit:
`skills/config/SKILL.md`, `skills/implement/orchestration.md` (two),
`skills/verify/orchestration.md`, the refusal message in
`skills/verify/scripts/broad_gate.py` (its section sign stays, as the `.py`
files are the later item's), and four pins in three test modules.

**The routing comment's row labels lost their dash.** `Planning — ` became
`Planning: `, and the same for `Automation` and `Answer pressed`;
`tests/test_waiver_decided_at_start.py` reads those three lines with a
regular expression, and both of its patterns follow.

**What stays.** Two dashes remain in `templates/config.md`, each inside a
literal another file owns: the refusal sentence `` `<item>` appears N times —
one value `` that `hooks/config.py` prints, and the release heading
`## X.Y.Z — <date>` the changelog gatherer writes. `sdd-overview.md` cites
`skills/implement/SKILL.md` *4. The closing memo — only what the diff cannot
show* by its current heading, which is outside this item. No template holds
a section sign, an arrow, a middle dot or an issue number (S8, executed
`git grep`).

**Census (S11): what left, and why it could go.**

| What left | Grounds |
|---|---|
| `sdd-routing.md`: "Committed, because the check happens at the pull request and CI sees only what is in the tree" | restates `skills/implement/orchestration.md` *Orchestrator: how the work is routed*; the comment links it |
| "A second copy of that reasoning here is how the two rows drift apart, which is the failure contract §11 was written to end" | reasoning about the file itself |
| `(#88)`, `(#151)`, "#263 is where answering this row by habit was measured" | history; the criterion and its axis stay |
| the `Answer pressed` paragraph *WHY THE ROW EXISTS* | restates *What the answer writes* in the orchestration file |
| `sdd-plan.md`: "reading this plan and spawning the builder IS the approval, so nothing extra is being asked for here", and the paragraph on the session building the work itself | both are *The plan is approved at the spawn*, which the comment links |
| "the same trick that lets a round record live beside the contract", "this column was wrong on its own first use, nine SHAs deep" | aside and anecdote; the rebase rule stays with its actor |
| `sdd-spec.md`: the #107 story of a rule lost from `agents/smith.md` | history; the reason a removal is recorded stays as a property |
| why the framer mark is needed | restated `agents/framer.md`; the comment links it |
| `sdd-questions.md`: "#84's second comment measured all three", "six probes at about three seconds each" | history and anecdote; the reason a measurement is not a person's row stays |
| `sdd-overview.md`: the account of `git diff --stat`, of a deleted row failing the next pull request, and of the check counting rows | restated `skills/implement/SKILL.md` *4.*; the comment links it and keeps the shapes a writer fills in |
| `sdd-phase.md`: `#119`, `#107`, `#121`, `#835` | history; each section's reason stays as a property of the record |
| `seal-README.md`: the pointer to the plugin README's *Shared or local* | the commands stay here; the pointer named a second copy |
| the predecessor `.specseal/scratch` sitting in a committed directory | history; why the opt-out lives under the git directory stays |
| `config.md`: "`Mode` is the exception, twice over …", "The section on it below says …" | restated *Mode* below; the opening states the rule and links it |
| "They are what somebody opens six months later" | aside |
| `#401`, `#448`, `#429`, `#667`, `#688`, `#825` | history; each rule stays |
| "nothing said where in `seal/config.md` it had to land … the example WAS the table every gate read" | history; what the fence rule prevents stays in the present |
| "Rules 1 and 2 were derived under pressure … Rule 3 was already here and in the config skill" | history |
| "because a rule written in three places is three places for it to disagree with itself" | the one-source tenet restated; the section still says it is the one home |
| "An earlier release read a second pact row … since the pact's records of changes left" | history; the rule on the row stays |
| `hygiene.yml`: nothing; every sentence reworded in place | |

**Cases rewritten** (each seen red after 5048ee94 by `mutation-check` on the
new text, executed):

| Case | What changed |
|---|---|
| `tests/test_a_phase_hands_the_next_one_a_record.py#test_each_section_comment_states_the_failure_it_prevents` | replaces `test_each_section_comment_names_its_measured_failure`, which held the issue numbers; it holds each comment's reason. Red with "with the spawn" mutated |
| `tests/test_a_phase_hands_the_next_one_a_record.py#test_the_spec_template_carries_the_rule_changes_section_above_removes` | the citation without the section sign |
| `tests/test_a_signer_declares_its_pact.py#test_the_template_and_the_config_skill_carry_the_pact_row_alone` | the `Pact notify` sentence without its history, said once. Red with the deleting clause mutated |
| `tests/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py#test_the_paragraph_above_the_lists_no_longer_says_it_names_what_to_write` | holds the reason in place of `#401`. Red with the reason mutated |
| the same module's `CRITERION` and the refusal case, `tests/test_first_setup_asks_once.py`'s pointer, `tests/test_the_rules_have_one_owner.py#CRITERION_OWNER` | the renamed heading. Red with the old heading put back in the template, and with the message's old wording put back in `broad_gate.py` |
| `tests/test_the_pull_request_language_is_the_repositorys.py#GRAMMAR_TABLE` | the citation without the section sign. Red with the sign put back |
| `tests/test_the_seal_is_taken_once_by_the_sealer.py#test_the_measurement_its_cost_and_its_limits_are_told_where_the_row_is_written` | rule 3's sentences without `(#825)` and with parentheses for the dashes. Red with one dash pair put back |
| `tests/test_waiver_decided_at_start.py`, the two row-label patterns | `Label: ` in place of `Label — `. Red with each dash put back |
| `tests/test_the_root_migrates_itself.py#test_the_readme_is_rewritten_from_the_new_template` | compares the rewritten README with the template instead of reading its first word. Red with `hooks/root-migrate.py` pointed at another template |

**Imperative sentences whose actor or condition the smith chose.**

| Sentence | What was chosen |
|---|---|
| `sdd-routing.md`: "The orchestrator commits it, and CI reads it at the pull request" | the actor of the commit |
| "the orchestrator RECORDS here which way it went" | the actor, which the old text left to the row |
| "The orchestrator deletes the row rather than inventing a third answer" | the actor of a bare imperative |
| "The orchestrator asks whether this work is FINDING OUT or WRITING DOWN"; "the orchestrator that reads those facts back and writes the code still answers `the session`" | the orchestrator named where the text said "the session", which is also a row value |
| `sdd-plan.md`: "The orchestrator writes it when it spawns the build" | the actor and the moment, from the orchestration file |
| "The party that builds a phase fills its cell as the phase closes"; "The party that builds the phase writes it to `phases/phase-N.md`" | the smith, or the orchestrator under `the session`, named as one party |
| "The party that rebases the branch re-reads this column after the rebase" | the actor and the moment |
| `sdd-spec.md`: "Whoever drew the frame fills in the date and `<who>`" | the framer, or the orchestrator under `the session` |
| "the party that builds the phase records it in `overview.md`" | the actor of a divergence |
| `sdd-questions.md`: "the framer checks the inheritance rule … inherits that answer and records it" | the actor of a bare imperative |
| `seal-README.md`: "whoever ran the command commits the change" | in place of "you commit" |
| `config.md`: "Whoever writes the file repairs it by deleting the extra row, or by writing the file as UTF-8" | the actor of "Delete the extra row" |
| "A disagreement is the input the command consumes: a person edits the row, runs `seal mode --apply`" | the actor of the edit |
| "The mirror then goes beside the documents the pull request already touches" | stated as a rule on the file, which was a bare imperative |
| "The person writing the row puts the row's directory in front of the variable instead" | the actor of "Put the row's directory" |
| "**What it asks of the party that frames or builds a change.** That party reads a reference root …" | in place of "a session" |
| "whoever next edits the file deletes it" | the actor of "delete it when the file is next edited" |
| `hygiene.yml`: "The line moves when a person edits it"; "a person copies this file"; "whoever ran it commits" | the actor, in place of "you" and bare imperatives |

**Restatement pairs of these files** (Scope 10, measured at 5048ee94 with the
module's own `shared_counts`, executed):

| Pair | Measured | `BASELINE` | Whose the residue is |
|---|---|---|---|
| `skills/implement/SKILL.md`, `templates/sdd-overview.md` | 0 | 4 | drained; phase 9 removes the entry |
| `skills/implement/orchestration.md`, `templates/sdd-routing.md` | 0 | 10 | drained; phase 9 removes the entry |
| `README.md`, `templates/seal-README.md` | 0 | 1 | drained; phase 9 removes the entry |
| `skills/code-review/orchestration.md`, `templates/sdd-phase.md` | 0 | 20 | drained before this phase; phase 9 removes the entry |
| `skills/verify/SKILL.md`, `templates/sdd-phase.md` | 0 | 10 | drained before this phase; phase 9 removes the entry |

One pair appeared while the phase was written and was drained before the
commit: the spec template's framer-mark comment, reworded, matched
`agents/framer.md` for 18 words; the comment now links the definition.

**Bytes, for S13** (executed `wc -c`, b3154f43 and 5048ee94):
`config.md` 34,363 to 33,313, `sdd-spec.md` 3,230 to 3,066, `sdd-plan.md`
3,278 to 2,903, `sdd-questions.md` 1,996 to 1,720, `sdd-round.md` 5,766 to
5,759, `sdd-phase.md` 1,854 to 1,759, `sdd-guarantee.md` 1,640 to 1,637.
The framer's set stands at 112,126 against 110,562 at b3154f43 and the
warden's at 78,710 against 76,287 (executed, summed from `git cat-file -s`).
Both are over because phase 1's writing section added 3,447 bytes to
`skills/writing-style/SKILL.md`, which both sets open; phase 9 reads the sets
again after its own edits.
