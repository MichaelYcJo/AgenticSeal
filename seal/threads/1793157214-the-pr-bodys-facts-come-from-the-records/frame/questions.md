# Questions for the planner: 1793157214-the-pr-bodys-facts-come-from-the-records

## Answered by the tree, not to be reopened

- **The command copies and never summarises.** Issue #1044's body,
  *What changes*: the sealer has nothing to compare in the generated part
  "because the text is the records'". A sentence the generator composes
  about a record would be a text that is not the records'.
- **What the generated part holds.** The issue's list, what changed, how it
  was built and verified, the review rounds, and what is left open, with
  the broad run's record. The divergence table of `gaps.md` and the
  `## Removes` of `frame/design.md` are not in today's bodies and stay out;
  the opening line names the thread where they stand.
- **Round records are read through `chain_check.py`'s grammar**, and the
  other records' headings through `unverified_check.py`'s reader. Each is
  the one reader of what it reads (`chain_check.py`'s docstring, the
  `records` arm; `chain_check.py#READER`).
- **The broad run's printed figures stay in the orchestrator's part.**
  `trail/gate.md` holds the commit and the base and nothing else
  (`broad_gate.py`, the docstring's `--record` paragraph).
- **The `Closes` line is the orchestrator's.** No record of a thread holds
  the issue number as a field; the branch name and the changelog's
  `(#N)` carry it as words, and a check gates only a fact it reads
  (`CLAUDE.md` *The rule a mechanism is kept against*).
  `.github/scripts/issue_claims_check.py` reads the whole body, so the line
  is read wherever it stands.
- **The generated part is in `Record language`.** The records are written
  in it (`skills/implement/SKILL.md` *The language the records are written
  in*), and translating them is a summary by another name. Its headings are
  constants and stay English, as `templates/setup/config.md` *What no row
  governs* keeps every heading a checker reads.
- **The sealer may run `seal pr-body --check`.** `agents/sealer.md` *Never*
  forbids the full suite, the repository-wide lint, the typecheck and
  `seal gate`; the check reads files and runs nothing broad.
- **No guard on the body's length.** The normal flow's largest thread so
  far copies to 33,560 bytes (`frame/design.md` *Limits*), and
  `gh pr create` refuses an over-long body with its own message. A shape
  the flow does not produce gets a limit sentence.
- **The module is `skills/code-review/scripts/pr_body.py`, run as
  `seal pr-body`.** Every command is a `seal` subcommand (`seal.py`'s
  docstring), the body belongs to the orchestrator's half of code-review,
  and its test file's place follows from `test_layout.py`'s area rule.

## Rows

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Which part of the body comes first? The issue says the orchestrator adds its own part "under a marked heading", and does not say where that heading stands. Today's bodies open with the motivation, which is the orchestrator's | a person | (a) The generated part first, then `HEADING`, then the orchestrator's part to the end of the file: one marker, and the attribution line ends the body as the session's instructions ask; a reader on GitHub meets the changelog's entries first and the motivation after the copied sections. (b) The orchestrator's part first under one heading, then the generated part under a second: the motivation first, two spellings to keep, and the attribution line inside the generated part or after it under a third rule | (a) | open |
| Q2 | Does this work item's body read `Closes #1044` or `Part of #1044`? The issue's third *Done when* item counts withholds over the body across the next three work items and posts the count on the issue, which no pull request of this work item can carry. `Closes` closes the issue when the release reaches `main` (`skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, step 3), possibly before those three work items have run | a person | (a) `Closes #1044`: the build's two items are done, and the count is a comment the owner or a later orchestrator posts on the closed issue. (b) `Part of #1044`: the issue stays open until the count is posted, and somebody closes it by hand | (a) | open |
| Q3 | How is the heading spelt? It is visible in every body routed through the chain, and the generator, the orchestrator and the sealer read it by one spelling | a person | (a) `## Not from the records`: it says what the sealer reads the part for. (b) `## Written for this pull request`, or another spelling the owner gives: the same mechanism, another sentence for the reader | (a) | open |
| Q4 | Are the five paid sealer evals (`evals/behaviour/sealer/`) run in this work item? Phase 3 changes the body each case hands the sealer, and the step phase 2 adds to `agents/sealer.md` runs `seal pr-body --check`, which the eval's sealer reaches only where the plugin under evaluation puts `seal` on its PATH | a person | (a) Not run in this work item: the scaffolds are regenerated and held equal to `rule_cases.py`'s output by the suite, and whether the cases still grade as before is `unverified`, answered by the owner's next paid run. (b) Run once by the orchestrator after the broad run, at its token cost, with the result in `gaps.md` | (a) | open |
| Q5 | The issue lists "the review rounds and their counts" among what the generated part covers. Should the generated part state a count, computed from the records? The orchestrator's spawn prompt says a generated count is the same defect moved into code | a person | (a) No count line: every round record is listed under its own heading, so a reader counts what stands, and nothing the generator states can disagree with the directory. (b) One line per section naming how many records it copies, computed from the directory listing: exact, and a figure the body states that no record states | (a) | open |
| Q6 | How are the sealer fixtures' placeholders spelt? `rule_cases.py` writes `target: BUILD_SHA against main` into the fixture's round record (`evals/scripts/rule_cases.py:535`) and the scaffold replaces it with `sed` at run time, but `chain_check.py`'s grammar reads a `target:` line only where it names 7 to 40 hexadecimal digits, so `compose` refuses the record as written | the work | Phase 3 picks a hexadecimal placeholder no other line of the fixture holds, writes it into the records and the body alike, and has the scaffold fill both with one `sed` each; the phase record says which | Phase 3's crafter chooses and records it | answered by phase 3's crafter: `rule_cases.py#BUILD_SHA` is `b0b0b0b`, filled in the two records and the body alike (`trail/phases/phase-3.md`) |
