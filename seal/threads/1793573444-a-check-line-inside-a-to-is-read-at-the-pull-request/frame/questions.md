# Questions for the planner: a check line inside a `to` is read at the pull request

The ticket left these judgments open. The tree or a probe answered each one, so none is a row below:

- Where the check-line reading runs, in `chain_check.py` or inside `rule_changes.py#parse`: `plan.md` *Alternatives considered*, rows 1 and 2.
- Whether the grammar's reader moves out of `.github/scripts/rules.py` so that `chain_check.py` can reach it: `plan.md` *Alternatives considered*, row 3, and `frame/design.md` *Grounding* G9.
- How a refused line is named at its line in the design: `plan.md` *Alternatives considered*, row 7, and `frame/design.md` *Grounding* G7.
- What the reading leaves for #1216 and #1217: `frame/design.md` *Grounding* G13.
- Whether a near line in a `to` refuses, is named, or is left unnamed: `plan.md` *Alternatives considered*, rows 8 and 9, and `frame/design.md` *Grounding* G12 and G20.
- Whether a `from`, or a `to` landing in a file outside `rules.py#RULE_FILES`, is read: `frame/design.md` *Scope*, item 3 and *Out*, and `plan.md` *Alternatives considered*, row 6.
- Whether the new read fails a design already on `release/v0.28.0`: `frame/design.md` *Grounding* G8.
- Which marker the rule's check line names: `plan.md` *Alternatives considered*, row 10.

No question is left for a person, a measurement or the work. What the suite does beyond the phase's narrow run is `unverified` in each hand-back, answered by the orchestrator's broad gate, as contract rule 2 states for every work item.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
