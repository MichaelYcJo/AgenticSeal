# Questions for the planner: 1794289597-pr-md-copies-the-changelog-below-the-fold

The ticket left these judgments open, and the tree answered each. Their
grounds stand where each line points, and none is reopened here.

- Whether this work item edits `docs/` or states its rule changes: `frame/design.md` *Grounding* G1, and `frame/plan.md` *Alternatives considered* row L.
- Where in the body the changelog fragment stands: `frame/design.md` *Grounding* G7, and `frame/plan.md` *Alternatives considered* rows A to D.
- Whether `pr.md` stays: `frame/plan.md` *Alternatives considered* row E.
- How #1478 *Change* reads where it says `pr.md` keeps "quotations of records the fold does not carry": `frame/design.md` *Grounding* G5 and G6.
- What `pr.<lang>.md` translates in the new shape: `frame/design.md` *Grounding* G8, and `frame/plan.md` *Alternatives considered* rows F to H.
- How much of the paragraph #1478 *Change* says goes does go: `frame/design.md` *Grounding* G9, and `frame/plan.md` *Alternatives considered* row I.
- Which file owns the rule: `frame/design.md` *Scope* item 3 and *Data & interfaces* D3.
- Whether `skills/implement/orchestration.md` is edited, and whether #1477's bound holds: `frame/design.md` *Grounding* G10, and `frame/plan.md` *Alternatives considered* row J.
- Whether `skills/code-review/scripts/chain_check.py` is edited: `frame/design.md` *Grounding* G3, and `frame/plan.md` *Alternatives considered* row M.
- How a body an earlier release composed is read: `frame/design.md` *Grounding* G11, `frame/plan.md` *Alternatives considered* row K and *Operational impact*.

No row waits on a person.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does a case hold a sentence this work rewords, or a line of the body's old layout, through a string the framer's searches did not list? The framer read the string pins by `git grep -F` on the phrases of each sentence `frame/design.md` D2, D3 and `## Rule changes` name, which lists the spellings searched for and no pin built at run time, and the framer runs no test module (contract rule 2), so the tree could not answer it at framing | the work | A narrow run of the modules `frame/plan.md` *Phases* names goes red on such a pin. Where the pinned sentence states a fact this work keeps, the phase keeps its words. Where it states what `pr.md` or `pr.<lang>.md` holds outside the owner, or the changelog inside the fold, the phase moves the pin to the new fact and names the case in its phase record | The phase treats a red case outside the cases `frame/design.md` *Scope* items 2 and 7 name as this row, and repairs the case to the new fact | answered 2026-11-10 by the work: phase 1 repaired three cases that pinned body line numbers to the new layout, and phases 2 and 3 met no case pinning a sentence this work rewords (`trail/phases/phase-1.md`, `trail/phases/phase-3.md`) |
| Q2 | Does `chain_check.py`'s notice for a rule change (`docs/checks/the-pull-request-check.md` *What the check reads at the pull request*, the rule on pins and copies) name a pin or a copy for an operation of `frame/design.md` *Rule changes*? The notice is printed by a run of the check, which the framer does not run, and the framer's `git grep -F` on phrases of each `from` found no pin under `tests/` | a measurement | The orchestrator's `seal gate --preflight` runs the check, which prints one notice per pin or copy at the operation's line, and the proofer weighs each at review, as that rule says. A pin of a rule's wording is a finding the fix pass repairs. A copy a `to` shares with another rule document goes to the framer as a fold, since the framer writes `frame/design.md` | The build proceeds as if no notice is printed | answered 2026-11-10 by the proofer: `chain_check.py` printed no pin or copy notice for any operation, in two runs at round 1 (`trail/rounds/round-1.md`) |
