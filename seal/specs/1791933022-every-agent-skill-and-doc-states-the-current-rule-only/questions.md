# every agent, skill and doc states the current rule only — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. -->

**Judgments the ticket left open that the tree answered** — listed so nobody reopens them; the grounds are in `spec.md` and `plan.md` §*Alternatives considered*.

- What the check reads: the tree, not the diff (alternative B's failure needs the merge base and refuses a moved section); two ratchet families per file in #930's checker, no new step or reader.
- What it refuses: a file over its bytes band, a narrative line outside a rule paragraph, two rule paragraphs in different files held by one enforcer; what it does not read: meaning, which is review's stage 1 against `spec.md` §*The shape of a compact file*, and behaviour, which the suite reads.
- How a restated rule is caught: identity by enforcer as the gate, the round's reading of a candidates list the checker emits for unenforced rules, and a paraphrase count reported not gated (alternatives R1–R5); the gate's reach is 302 of 1,176 paragraphs today and grows with every rewrite.
- How a rewrite is proved not worse: `claude plugin eval` over replay, seeded and rule-exercise cases, old tree against new on the same inputs, pooled over N = 2 runs a side, with a per-rule clause; the baseline taken once; a test holds the record (alternatives E1–E7).
- The unit is bytes (#930 alternative E); the token fit is stated once in `spec.md` and the saving is posted by `measuring-a-run`, never promised here.
- Where removed narration goes: nowhere new — the issue it cites, git history and the work item's records already hold it (alternative I).
- Preload first, `agents/warden.md` first (alternative K; the owner's item 6).
- The ledger plan: headings kept so rows drift rather than break; `--reverify --into` for the drifted, a `Corrected ·` row per broken row, onto the test that holds the claim; never a bulk pass (`docs/the-evidence-ledger.md` §*A claim held by a test*, the owner's 2026-10-08 answer).
- The boundary with #929: a module that asserts on a prose file's text moves with the text; every other module is #929's (`spec.md` §*Scope*).
- `skills/writing-style/SKILL.md`, both READMEs, the round records and `seal/specs/`: out, with the reasons in `spec.md` §*Scope*.
- Parts B (#940) and C (#941) are in 0.22.0, framed separately on phase 1's check and phase 2's harness (the owner, 2026-10-14); this item is part A.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | `docs/one-root-by-lifetime.md` and its `.ko.md` describe themselves as "the design 0.4.0 starts from", which `docs/the-record-layout.md` §*docs/* indexes as history. Rewrite the pair to the current rule, retire it, or leave it? | a person — the owner keeps the Korean edition | rewrite · retire to `docs/experiments/` · leave | — | ✅ answered 2026-10-14 by the repository owner: **rewritten** to the current rule, in #941 |
| Q2 | What are the real tokens per preload after the rewrites? The frame's fit (2.79 B/token above 39,249) rests on four medians, residual up to 3,539 | a measurement — the orchestrator spawns the `general-purpose` baseline once and runs `payload_meter.py --calibrate <main transcript>` (#930 Q2, unanswered there too); a subagent cannot spawn | the fit, labelled estimated, in each phase record | ⬜ |
| Q3 | Of the 101 literals 28 modules pin in `agents/warden.md`, which pin a rule and which pin narration? | the work — phase 3 sorts them as it rewrites and lists the dropped ones in `phases/phase-3.md` and `overview.md` | — | ⬜ |
| Q4 | How many lines do the four widened marks add to each file's `history:` row at today's tree, and does any over-count a rule sentence? | the work — phase 1 lists the per-file delta in `phases/phase-1.md`; the rows start at the measured value either way | — | ⬜ |
| Q5 | Is 16,000 B the right family ceiling for an unlisted `bytes:` file? | the work — phase 1 writes it; a later file that needs more raises it with its line | 16,000 | ⬜ |
| Q6 | The proof the owner's condition asks for costs agent runs: the baseline once (38 runs, ≈ 2.5 h at `-j 4`, ≈ 25 M uncached input and ≈ 1 B cache-read tokens by the run medians) and then 16–38 runs per rewrite phase, ≈ 120 runs over the item, ≈ 8 h of wall clock at `-j 4` on the orchestrator's account. Is that budget accepted, or should the suite be smaller? | a person — the owner pays for the runs and set the condition | **accept**: K = 8 warden, 4 smith, 4 framer, 3 sealer, N = 2, as `spec.md` states. **halve K**: half the cost; a lost rarely-exercised rule has half the chances to show and pass rule 4 reads fewer graders. **N = 1**: the pooled rule loses its noise reading and a single unlucky run fails a sound rewrite, which then costs a rerun | accept | ⬜ |
| Q7 | Does `claude plugin eval` run on the owner's account, and does a case's session spawn `specseal:warden` through the `Agent` tool as production does? `evals/README.md` calls it early access; the command and its flags are on this machine at 2.1.296 | a measurement — phase 2's first act runs one case with a deliberately broken definition and reads the result; where it does not run, alternative E7's `claude -p --agent` fallback takes the same comparator | the harness as designed | ⬜ |
| Q8 | Which of the 21 paraphrase pairs at Jaccard ≥ 0.5 beyond the 12 deliberate copies are one rule, and where does each home go? | the work — phase 1 reads the nine as it links the four enforcer pairs; a pair it judges one rule is linked in the same phase, the rest are the `restated` row's starting count | — | ⬜ |

Two rows wait on a person; Q6 blocks phase 2's baseline run and nothing before it; Q1 is answered. The three kinds are the template's.
