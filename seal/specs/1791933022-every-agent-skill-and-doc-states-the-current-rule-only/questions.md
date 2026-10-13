# every agent, skill and doc states the current rule only — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. -->

**Judgments the ticket left open that the tree answered** — listed so nobody reopens them; the grounds are in `spec.md` and `plan.md` §*Alternatives considered*.

- What the check reads: the tree, not the diff (alternative B's failure needs the merge base and refuses a moved section); two ratchet families per file in #930's checker, no new step or reader.
- What it refuses: a file over its bytes band, a narrative line outside a rule paragraph; what it does not read: meaning, which is review's stage 1 against `spec.md` §*The shape of a compact file*.
- The unit is bytes (#930 alternative E); the token fit is stated once in `spec.md` and the saving is posted by `measuring-a-run`, never promised here.
- Where removed narration goes: nowhere new — the issue it cites, git history and the work item's records already hold it (alternative I).
- Preload first, `agents/warden.md` first (alternative K; the owner's item 6).
- The ledger plan: headings kept so rows drift rather than break; `--reverify --into` for the drifted, a `Corrected ·` row per broken row, onto the test that holds the claim; never a bulk pass (`docs/the-evidence-ledger.md` §*A claim held by a test*, the owner's 2026-10-08 answer).
- The boundary with #929: a module that asserts on a prose file's text moves with the text; every other module is #929's (`spec.md` §*Scope*).
- `skills/writing-style/SKILL.md`, both READMEs, the round records and `seal/specs/`: out, with the reasons in `spec.md` §*Scope*.
- The split into parts A, B and C: proposed and written as the plan; the approval of `plan.md` is the answer, so it is no row here.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | `docs/one-root-by-lifetime.md` and its `.ko.md` (728 + 700 lines, 115 KB, 72 history lines, 6 ledger anchors, 62 test modules pinning them) describe themselves as "the design 0.4.0 starts from", which `docs/the-record-layout.md` §*docs/* indexes as history, not a standing rule. Part C can rewrite the pair to the current rule, which is mostly a deletion into the other docs, or retire it. Which? | a person — the owner wrote and keeps the Korean edition, and whether a design record stays in `docs/` is a product decision | **rewrite**: both editions cut to what still rules, their anchors re-read, ~55 KB left. **retire to `docs/experiments/`**: the pair leaves `docs/`, its 6 anchors take `Corrected ·` rows, its pins move or go, `history:` rows removed with their lines. **leave as is**: its two rows stay at 39 and 33 and the pair is the one history file in the corpus | retire, framed as its own part-C item; nothing in part A depends on it | ⬜ |
| Q2 | What are the real tokens per preload after phase 2 and after phase 5? The frame's fit (2.79 B/token above 39,249) rests on four medians, residual up to 3,539 tokens | a measurement — the orchestrator spawns the `general-purpose` baseline once and runs `payload_meter.py --calibrate <main transcript>` (#930 Q2, unanswered there too); a subagent cannot spawn | the fit, labelled estimated, in each phase record | ⬜ |
| Q3 | Of the 101 literals 28 modules pin in `agents/warden.md`, which pin a rule and which pin narration? A pin on narration goes with its sentence; a pin on a rule is re-pointed | the work — phase 2 sorts them as it rewrites and lists the dropped ones in `phases/phase-2.md` and `overview.md` | — | ⬜ |
| Q4 | How many lines do the four widened marks (`used to` 88 hits, `no longer` 25, `arrived at` 13, `before this` 12 over the corpus, rule blocks included) add to each file's `history:` row at today's tree, and does any mark over-count a rule sentence? | the work — phase 1 lists the per-file delta in `phases/phase-1.md`; the rows start at the measured value either way, so nothing fails on the widening | — | ⬜ |
| Q5 | Is 16,000 B the right family ceiling for an unlisted `bytes:` file (a new agent or skill)? The largest compact target in the preload set is 15,000 | the work — phase 1 writes it; a later file that needs more raises it with its line | 16,000 | ⬜ |

One row waits on a person, and nothing in part A waits on it: Q1 decides a part-C item's shape. The three kinds are the template's.
