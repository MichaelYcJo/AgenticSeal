# Questions for the planner: a keyword inside an HTML comment reads as a claim (#1181)

The ticket left these judgments open, and the tree answered them. Nobody reopens them:

- Which readers R26 and R27 are: `frame/design.md` *Grounding*, the row on #956's audit.
- Whether the side reading of #1402 bears on a reader: `frame/design.md` *Grounding*, the side-reading row.
- Whether the labeler and the release note need an edit of their own: `frame/design.md` *Grounding*, the row on the class of readers.
- Whether the closer keeps its own patterns or moves onto a shared walk: `frame/plan.md` *Alternatives considered*, rows C and D.
- In which order the fence, the comment and the span are masked: `frame/plan.md` *Alternatives considered*, rows A, B and B2.
- Whether `pr_body`'s `details` tag reading follows the keyword reading: `frame/plan.md` *Alternatives considered*, row F.
- Whether R26 follows the closer: `frame/plan.md` *Alternatives considered*, row G.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | GitHub creates no closing reference from `<!-- Closes #1181 -->` (#1402). Does it also create none from a keyword in a comment in the middle of a line, in a comment over several lines, and in a comment under a list item? The tree cannot answer it: GitHub's page on linking a pull request to an issue does not say (#1181's body, read 2026-10-29). No probe of mine can answer it either, because the answer needs a pull request into `main` and a framer opens none (contract rule 6) | a measurement: the orchestrator, from a throwaway pull request into `main` read through `closingIssuesReferences`, as for #1402 | (a) GitHub reads none of the three. `HIDDEN` stands as framed. (b) GitHub reads one of them. `COMMENT` narrows to leave that shape read, and until it does the closer closes fewer than GitHub for that shape, which is its safe direction | (a). CommonMark renders all three as comments, as it renders the measured one, and the build proceeds on (a) | open |
| Q2 | Does GitHub read a keyword after a `<!--` that no `-->` follows anywhere in the body? CommonMark makes a line that opens with `<!--` an HTML block running to the end of the document, and leaves one in the middle of a line as text. The tree cannot answer it and no probe of mine can, for Q1's reasons | a measurement: the orchestrator, as in Q1 | (a) GitHub reads it. The row in `test_accepts_a_shape_left_unmasked_as_a_claim` stays, and the readers already agree with GitHub. (b) GitHub does not read it where the opener begins a line. Masking that opener to the end of the body would close fewer, and the row turns into a masked case | (a): the shape stays read as a claim, as it is today, and keeps its pinned row (`frame/design.md` *Scope* 6) | open |
