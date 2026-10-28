# Feature Specification: 1793171574-agent-definitions-restate-the-contract

Issue #1040 is the spec. Every line number below is at `4c90a988`, this
branch's HEAD when it was framed. `git diff --stat 0b75346f 4c90a988 --
agents/ skills/agent-contract/` prints nothing, so the issue's line numbers
at `0b75346f` hold here too (executed).

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `docs/the-record-layout.md`, its opening paragraph: "A file that states a rule this index gives another home links to that home and does not restate it ... Where a copy is found, the copy is the defect." | Each of the 13 sentences states a rule whose home is `skills/agent-contract/SKILL.md`. Each one is a copy, and the copy is what goes. |
| `docs/the-agent-set.md` *One contract every agent receives, and one definition each*: "what is true of every agent is shared, what is one agent's own is in that agent's definition" | A prohibition that binds every agent leaves the definitions. What one agent does under that prohibition stays in its definition. |
| `CLAUDE.md` *The rule a mechanism is kept against*: "A fact has one source, and every other place links to it." and "A change rewrites the text it amends in place, and in the same commit removes what stood on the old fact: a check, an exception, a comment, a copy." | A test assertion that reads a removed sentence is changed or removed in the same commit as the sentence. |
| `docs/the-reader-registry.md` *A frame names what its work removes* | Every removed sentence and every removed or re-pointed assertion is a row of `## Removes` below. |
| Contract rules 2, 6, 7 and 9 (`skills/agent-contract/SKILL.md`) | These four rules are the homes. A narrowing that stays in a definition cites its rule as `rule <N>`. The contract itself does not change. |

## Scope

### In

1. **The 13 restating sentences of #1040 leave `agents/*.md`.** Each one is a
   row of `## Removes`. They are:
   - Contract rule 2 (no agent runs the full suite, the repository-wide lint
     or the typecheck): `agents/crafter.md:65` and `:138-140`,
     `agents/proofer.md:61` and `:138-140`, `agents/sealer.md:109-110` and
     `:125-127`.
   - Contract rule 6 (no agent posts, pushes, opens a pull request or spawns
     an agent): `agents/crafter.md:69`, the second half of
     `agents/proofer.md:59-60`, `agents/framer.md:106` and
     `agents/tracer.md:46`.
   - Contract rule 9 (no edit through the shell): `agents/crafter.md:70-71`.
   - Contract rule 7 (probe only what reading cannot settle):
     `agents/tracer.md:34-35`, the clause after the semicolon.
2. **Each paragraph that also narrows the contract keeps the narrowing and
   cites its rule by number.** The narrowings are the ones #1040 names:
   - `agents/crafter.md` *Rules*, *The broad gate is not yours, and its
     label is.*: the meaning of `failing on base too` and `new?` beside a
     broad gate failure. The paragraph keeps its bold lead and cites
     `rule 2`.
   - `agents/proofer.md` *Rules*, *The broad gate is not yours, and its
     label is.*: the audit of the `unverified` label, the declined order
     recorded as a `## Not judged` row, and what comes due when the round
     leaves nothing open. "One of the three" loses its antecedent with the
     removed sentence, so the declined order names its rule instead (a
     check `rule 2` excludes is the wording contract rule 3 already uses).
   - `agents/sealer.md` *Rules*: the pointer to step 1 for a missing or
     stale record. The bold lead is one of the listed sentences, so the
     paragraph gets a lead that names the narrowing. It cites `rule 2` in
     lower case, because `test_the_window_the_sealer_shipped_under_is_closed`
     reads `"rule 2" in text`.
   - `agents/proofer.md:59`: "Fix the code under review." stays as a bullet
     of its own.
   - `agents/crafter.md:66`: "Name any party as the runner of the broad
     gate." stays.
3. **Every test assertion that reads a removed sentence reads the contract
   or the narrowing that stays, or goes with the sentence.** Rule 12 asks
   for the class, so the assertions were found by `git grep` over `tests/`
   and `evals/` on the words of each removed sentence (executed). The issue
   names three assertions in two cases. The search found three more cases
   and one module docstring:

   | Assertion | Reads today | After this work |
   |---|---|---|
   | `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:883` | "You do not run the full suite, the lint or the typecheck" in the crafter's paragraph | the narrowing's own words, `` `failing on base too` `` and `` `new?` ``, in the same paragraph |
   | `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:886` | "rule 2 holds who does" | `rule 2` in the same paragraph, the citation's spelling |
   | `tests/text/test_broad_gate_rule.py:139` (`test_the_crafter_puts_both_answers_in_the_hand_back`) | `"rule 2" in crafter`, true today only through `:139` of the crafter | unchanged. The crafter paragraph's citation keeps it true |
   | `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:1007` (`test_the_window_the_sealer_shipped_under_is_closed`) | "the orchestrator runs it", from `agents/sealer.md:126` | "is the orchestrator's run's", from `agents/sealer.md:31`, the *Job* sentence that names whose `trail/gate.md` is |
   | `tests/behaviour/test_the_sealer_guarantees.py:207` (`test_step_1_reads_the_record_and_runs_nothing`) | "the typecheck or `seal gate`" in the sealer's *Never* | removed. The same case still asserts step 1, and `tests/text/test_broad_gate_rule.py`'s `TAKES_THE_RUN` reads every definition for a sentence that hands its agent the run |
   | `tests/text/test_edits_go_through_the_edit_tool.py:111-123` (`test_the_implementer_keeps_the_half_that_makes_the_rule_its_own`) | the crafter's rule 9 bullet and `"rule 9" in crafter` | the case is removed with the bullet. The module's other cases read contract rule 9 itself (`CARRIERS`) |
   | the same module's docstring, `:8-11` | "for `agents/crafter.md` the forms a shell edit takes" | rewritten in place: the crafter keeps no half of rule 9, and the proofer's half stays |

   The docstring of `test_the_crafter_names_no_runner_of_the_broad_gate`
   (`:874-879`) says the crafter "says it does not run the broad gate". It
   is rewritten in place to say what the paragraph now holds.
4. **The `check:` lines stay as they are.** `agents/crafter.md:145`,
   `agents/proofer.md:147` and `agents/sealer.md:128` each name a test that
   reads what its paragraph keeps once item 3 lands. The sealer's line keeps
   `evals/behaviour/sealer/rule-sealer-no-gate/` and
   `rule-sealer-stale-gate/`.
5. **A changelog fragment**, `changelog.md` in this work item's directory,
   says that the five definitions no longer restate contract rules 2, 6, 7
   and 9.

## Out of scope

- **A check that catches a paraphrase.** #1040 rules it out. The docstring
  of `tests/text/test_no_passage_is_pasted_into_a_second_file.py` says why a
  constant cannot tell a paraphrase from a link.
- **An absence assertion for each removed sentence.** It would pin one
  spelling, and a restatement comes back in other words
  (`frame/plan.md` *Alternatives considered*, row E).
- **Whether a phrase pin should exist at all.** That is #1111's, which runs
  after #956 and this work. The pins this work re-points (the crafter's
  `rule 2`, `failing on base too` and `new?`; the sealer's
  "is the orchestrator's run's") are among the ones #1111 then decides.
- **`agents/crafter.md:20` and the fix-pass paragraph at `:153-162`.** #1041
  edits them after this work. This work touches `agents/crafter.md:65`,
  `:69-71` and `:138-144` only.
- **The word `spec` in the agent definitions and in
  `skills/implement/SKILL.md`.** #1110 rewords both after #1040 and #1041.
- **Restatements of the contract outside `agents/*.md`.** #1040's
  measurement and its *Done when* cover the agent definitions. A copy in a
  skill or in `bin/test`'s comment is not measured here.
- **Glosses the tree already holds as a definition's own application.** They
  stay. Each one is named, with the case that holds it, in
  `frame/questions.md`'s head, item 3.
- **The paste check's `BASELINE`.** The agent pairs share no 15-word run
  that a removed sentence makes up. The ratchet passes a count that goes
  down, and its comment says nothing has to lower an entry.
- **The files of the parallel work items.** #1039, #1058 and #913 own no
  file this work edits (`frame/questions.md` head, item 7).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. The copies are gone | Given the five definitions at the phase's commit, when each of the 13 sentences is searched for, then none is found | One distinctive phrase per sentence, searched in each `agents/*.md` with runs of whitespace collapsed, as `tests/conftest.py#flat` reads a file, because several of the sentences wrap across lines and a line search misses them: "repository-wide lint", "post, push", "Spawn the build or any agent", "open a pull request or spawn", "Edit through the shell", "reading cannot settle", "You do not run the full suite", "the lint and the typecheck run once", "its record is what you read", "By rule 2 the orchestrator". At `4c90a988` every phrase is found in the file its sentence stands in (executed by the framer), so the search can fail. The phase record lists the search and its empty result |
| S2. Each narrowing stays and cites its rule | Given the crafter's, the proofer's and the sealer's broad gate paragraphs, when each is read, then it keeps the narrowing `## Scope` item 2 names and cites `rule 2` | `tests/text/test_broad_gate_rule.py` (`test_the_crafter_puts_both_answers_in_the_hand_back`, `test_the_proofer_audits_the_scope_of_a_seal`, `test_the_reviewer_has_a_field_for_the_question_the_default_produces`) and `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py` (`test_the_crafter_names_no_runner_of_the_broad_gate`, `test_the_proofer_says_what_comes_due`, `test_the_window_the_sealer_shipped_under_is_closed`), green |
| S3. A re-pointed assertion can fail | Given each assertion `## Scope` item 3 re-points, when the sentence it now reads is broken, then the case goes red | `seal mutate` over each sentence: the crafter's `rule 2` citation, its `` `failing on base too` `` clause, and the sealer's "is the orchestrator's run's", each with `--tests` naming the case. The phase record names each run and its verdict (rule 15) |
| S4. Nothing else reads a removed sentence | Given the tree at the phase's commit, when the modules that read agent definitions run, then they pass | `bin/test` over each module, one at a time: `tests/text/test_broad_gate_rule.py`, `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`, `tests/behaviour/test_the_sealer_guarantees.py`, `tests/text/test_edits_go_through_the_edit_tool.py`, `tests/behaviour/test_a_probe_that_commits_says_so.py`, `tests/text/test_a_moved_rule_leaves_its_definition.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/text/test_every_agent_reads_the_contract.py` |
| S5. No narrowing becomes a copy | Given the rewritten paragraphs, when each contract section is compared with each definition in 15-word runs, then no run is shared | `tests/text/test_a_moved_rule_leaves_its_definition.py` and `test_the_sealer_cites_the_section_without_carrying_it` in `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`, green |
| S6. Every definition still receives the contract | Given the five definitions, when their front matter is read, then each lists `agent-contract` under `skills:` and opens with the contract sentence | `tests/text/test_every_agent_reads_the_contract.py`, green. This is the premise the removal rests on (`frame/plan.md` *Technical context*) |

## Data & interfaces

None. No schema, command, output or file format changes. What changes is
the text five agent definitions give their agents, and the assertions that
read that text.

## Rule changes

- nothing
  why: The policy already states the rule this work applies. `docs/the-record-layout.md` says a copy of a rule outside its home is the defect, and `docs/the-agent-set.md` puts what is true of every agent in the contract. The work removes copies from `agents/*.md` and edits no sentence of the policy root.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| "Run the full suite, the repository-wide lint or the typecheck." | `agents/crafter.md` *Never*, `:65` | Contract rule 2: "no agent runs any of the three" |
| "Spawn an agent, post, push, or open a pull request." | `agents/crafter.md` *Never*, `:69` | Contract rule 6: "four acts are withheld from every agent" |
| "Edit through the shell: no `sed -i`, no heredoc, no script that rewrites a file (rule 9)." | `agents/crafter.md` *Never*, `:70-71` | Contract rule 9, which names the same forms: "a `sed -i`, a redirection or a script" |
| "You do not run the full suite, the lint or the typecheck; rule 2 holds who does. You hand the suite over labelled `unverified`." | `agents/crafter.md` *Rules*, *The broad gate is not yours, and its label is.*, `:138-140` | Contract rule 2. The paragraph keeps the meaning of `failing on base too` and `new?` and cites `rule 2`. The hand-back's `unverified` label stays in the crafter's *Order of work* step 10 |
| ", post, push, open a pull request or spawn an agent" | `agents/proofer.md` *Never*, `:59-60` | Contract rule 6. The bullet keeps "Fix the code under review." |
| "Run the full suite, the repository-wide lint or the typecheck." | `agents/proofer.md` *Never*, `:61` | Contract rule 2 |
| "The full suite, the lint and the typecheck run once, by `seal gate`, after the rounds settle, and `trail/gate.md` holds that run." | `agents/proofer.md` *Rules*, *The broad gate is not yours, and its label is.*, `:138-140` | Contract rule 2, which names the run, its command and its record. The paragraph keeps the label audit, the `## Not judged` row and what comes due |
| "Run the full suite, the repository-wide lint, the typecheck or `seal gate`: the record is the run, and you read it." | `agents/sealer.md` *Never*, `:109-110` | Contract rule 2. Reading the record is the sealer's *Order of work* step 1 |
| "The broad gate is not yours; its record is what you read. By rule 2 the orchestrator runs it" | `agents/sealer.md` *Rules*, `:125-127` | Contract rule 2. Whose the run is stays in the sealer's *Job* (`:31`, "`trail/gate.md` is the orchestrator's run's"). The paragraph keeps the pointer to step 1 and cites `rule 2` |
| "Spawn the build or any agent, post, push, or open a pull request." | `agents/framer.md` *Never*, `:106` | Contract rule 6. Spawning the build is an agent spawn |
| "Spawn an agent, post, push or open a pull request." | `agents/tracer.md` *Never*, `:46` | Contract rule 6 |
| "; probe only what reading cannot settle (rule 7)" | `agents/tracer.md` *Order of work* step 5, `:34-35` | Contract rule 7's first sentence. The tracer's rule *Constraints, enums and defaults are read, not probed.* keeps its rule 7 citation |
| The assertions on "You do not run the full suite, the lint or the typecheck" and "rule 2 holds who does" | `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py#test_the_crafter_names_no_runner_of_the_broad_gate` | Re-pointed to the kept paragraph: its `rule 2` citation and its `failing on base too` clause. The docstring is rewritten in place |
| The assertion on "the orchestrator runs it" | `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py#test_the_window_the_sealer_shipped_under_is_closed` | Re-pointed to "is the orchestrator's run's", the sealer's *Job* sentence |
| The assertion on "the typecheck or `seal gate`" in the sealer's *Never* | `tests/behaviour/test_the_sealer_guarantees.py#test_step_1_reads_the_record_and_runs_nothing` | Removed with the bullet. The case keeps its step 1 assertions, and `TAKES_THE_RUN` in `tests/text/test_broad_gate_rule.py` reads every definition for a sentence that hands its agent the run |
| The case that pins the crafter's rule 9 bullet | `tests/text/test_edits_go_through_the_edit_tool.py#test_the_implementer_keeps_the_half_that_makes_the_rule_its_own` | Removed with the bullet. The fact it stood on, that the crafter keeps a half of rule 9, is gone. The module's other cases read contract rule 9 itself |
| "for `agents/crafter.md` the forms a shell edit takes" | `tests/text/test_edits_go_through_the_edit_tool.py`, module docstring, `:8-11` | Rewritten in place to name the proofer's half alone |

## Open questions

<none here: each is a row of `questions.md`>

Framed 2026-10-28 by framer, before the build.
