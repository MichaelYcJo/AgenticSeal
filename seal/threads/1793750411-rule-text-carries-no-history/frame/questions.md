# Questions for the planner: rule text carries no history (#1317)

The ticket left these judgments open, and the tree answered each one:

- Whether this item edits `docs/` directly or states rule changes: `frame/design.md` *Grounding*, the `skills/implement/SKILL.md` *Document layout* row, and *Rule changes*.
- Whether `docs/experiments/` is in the scope: `frame/design.md` *Grounding*, the `docs/README.md` row, and *Scope* O3.
- What counts as history and what stays: `frame/design.md` *D2*.
- Which side of a copy stays: `frame/design.md` *D3*.
- How the census is taken, and why no check is built: `frame/design.md` *D4*, and `frame/plan.md` *Alternatives considered* A2 and A3.
- What happens to `skills/implement/acts.md` and its pairs: `frame/design.md` *Scope* O2, and `frame/plan.md` A6.
- Whether the sentences that pending `from` lines quote may change: `frame/design.md` *Grounding*, the unsettled `## Rule changes` row, and *Scope* O4.
- Which commit moves the version: `frame/plan.md` *Phases*, the paragraph under the table.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | For a sentence that D2 leaves borderline, such as the candidates listed under `frame/design.md` *Removes*, does it go? | the work | Removing it shortens the rule text. Keeping it keeps an example or a reason that a reader at that step may need. The tree cannot answer this before the phase reads the sentence in its paragraph, and no probe measures whether a reader needs it | The phase applies D2. Its record states the sentence, the keep case or the history class it found, and its grounds | answered 2026-11-04 by the work: `trail/phases/phase-1.md` to `phase-3.md` state each borderline sentence with its grounds |
| Q2 | Which paraphrase copies stand in the scope? | the work | The census lists only verbatim runs, and no probe lists a restatement in other words. The whole reading of each file meets them | Each phase removes the paraphrases it meets under D3, and its hand-back calls that list a sample, as contract rule 12 asks | answered 2026-11-04 by the work: each phase record lists the paraphrases it removed or kept, as a sample |
