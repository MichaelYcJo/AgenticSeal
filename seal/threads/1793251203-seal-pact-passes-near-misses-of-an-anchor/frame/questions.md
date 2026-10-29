# Questions for the planner: 1793251203-seal-pact-passes-near-misses-of-an-anchor

## Answered by the tree, not to be reopened

- **Each refusal `seal pact` makes is at exit 2, not printed in no exit
  class.** `docs/the-record-layout.md` *Whether a line is live is asked by
  what the line does* reads a line that holds an anchor on doubt and wants
  the wrong answer loud (`plan.md` A7).
- **A remote near miss in the anchor table is caught by the signer's
  declared remotes, not by closeness to the pact's.** The declared list is a
  fact in the signer's `seal/config.md`; one letter off is a guess
  (`plan.md` A5, A6). A row naming a declared other pact is still passed
  over.
- **`PACT:` and `Pact:` are refused, and `pact: ` and `pact :` are a stated
  limit.** Case folding matched no prose at four revisions; a space beside
  the colon matched prose at three of them (`frame/design.md` *Grounding*,
  the probes). The issue accepts a limit sentence for the inline near
  misses. The owner's later direction does not reach the token (`plan.md`
  A8).
- **The inline form stays refused, as #913 decided.** Its `questions.md` Q1
  default (a) is the standing answer; this work widens the spellings it
  reaches and does not reopen it.
- **Whether a header means the same as `| Pact | Clause | Hash |` is not
  decided by spelling.** The owner's answer in `guarantee.md` settles it
  (`plan.md` A1, A2, A15).
- **What the normalisation holds.** It holds case, and one `*` or `_` run of
  one to three characters wrapping a whole cell with no space just inside
  it. Whitespace around a cell is already stripped by `table_cells`. Code
  spans, strikethrough, HTML tags, nested or mixed runs and escaped
  delimiters stay out (`frame/design.md` *Grounding*, the rendering row;
  `plan.md` A12).
- **The normalisation applies to the anchor table alone.** The map, the
  `Signer` table and `seal/config.md` are refused where their exact header
  is missing, so a near miss there is already loud (`frame/design.md`
  *Out*).
- **The row scan goes.** Three of four rounds found a shape in it, and no
  release recorded a catch (`plan.md` A3, A11, A14).
- **The judgment of intent for the shapes the normalisation leaves out
  sits with the proofer, at stage 1 of the signer's review, and reads only
  the signer's own repository.** So
  `docs/the-pact.md` *A signer's CI reads nothing of the pact* stands
  unchanged (`frame/design.md` *Grounding*).
- **The `Reframed` line names `framer`.** `skills/code-review/scripts/chain_check.py#frame`
  refuses one naming anyone other than `hooks/lib/routing.py`'s `BY_FRAMER`,
  which is `framer` (executed, `git grep`).
- **No file a parallel work item edits is touched.** #1123 edits
  `skills/verify/scripts/deferral_check.py`, #1127 a case under
  `tests/text/`, and #1158 `agents/framer.md` and the `rule-framer-sharp-s`
  eval. This work edits `pact_check.py`, `tests/skills/test_pact_check.py`
  and `skills/code-review/SKILL.md` (`frame/design.md` *Scope*).
- **The cases are seen red against `28edee12`, which is the issue's
  `5287dd42` for this code.** `git diff --stat 5287dd42 28edee12` over the
  pact files prints nothing (executed by the first frame; re-run by the
  sealer).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| W1 | The names and exact words of the two new refusal sentences. `frame/design.md` *Data & interfaces* fixes what each says. The words are written where they are built and pinned there | the work | Any wording that names the cell as written, says why nothing grades the row, gives the remedy, and passes `tests/behaviour/test_one_word_one_meaning.py`. The choice goes into the phase record | Phase 1's wording, pinned by S1's and S3's cases | answered 2026-10-29 by the crafter: `UNDECLARED` and `OUTSIDE_TABLE`, worded as `trail/phases/phase-1.md` records |
| P1 | The owner's answer in `guarantee.md` says a header that differs from `| Pact | Clause | Hash |` only by case or emphasis is read as the anchor table, so its rows are graded and an undeclared remote under it is refused `UNDECLARED`. This reframe does not build that. It takes the later direction instead: `seal pact` reads the exact header alone, and the proofer judges a near-miss header at the signer's review (`plan.md` A12 against A13). Under A13 a lower-case anchor table is graded by nothing in code, and #1132's second *Done when* bullet is met by no refusal at all. Does A13 stand, and does #1132 close with that bullet set aside? | a person | (a) A13 as framed: phases 3 and 4, the scan removed, one proofer sentence, and #1132's bullet 2 met by no code. (b) A12: phase 3 removes the scan and adds the normalisation, one function in `pact_check.py` that case folds each header cell and strips one emphasis run wrapping it, used by `first_table` for the anchor table and its second-header scan, with a case per member seen red against `a5533a3d`. Phase 4 is dropped. Bullet 2 is then met for case and emphasis by grading, and the plural stays another table. (c) Both: A12 in code and the proofer sentence beside it | (a) | answered 2026-10-29 by the orchestrator, under the owner's direction that a script answering "these differ" where the meaning is the same is the worst outcome: (c). A header differing from the anchor header only by case, or by one emphasis run wrapping a whole cell, is the anchor table by definition, not by a guess, so seal pact grades its rows; whether a plural header or a headerless row was meant as an anchor is a judgment of meaning, and the proofer makes it at the signer's review. |
| W2 | The exact words and the placement of the proofer's sentence in `skills/code-review/SKILL.md` stage 1 | the work | Any sentence that names the shape by `pact_check.py`'s docstring *What each frame is read for* and the `Pact` row of the repository's `seal/config.md`, and makes a line meant as an anchor that `seal pact` does not read a finding. It must not restate the shape as a second source. It must pass the modules that read the skill | Phase 4's wording, recorded in its phase record | answered 2026-10-29 by the crafter: three sentences under stage 1, as `trail/phases/phase-4.md` records |
