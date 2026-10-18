# the smith is written anew from its job (#967) — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here. -->

## What the tree answered, so nobody reopens it

The ticket and the orchestrator's six decisions left these open and the
repository settled them; the grounds are in `spec.md` and in `plan.md`'s
Alternatives table.

- **The framer is measured here** although its rewrite is #968's: its
  preload holds `implement` and `writing-style`, and the contract changed
  after #957's phase 3, so guard 1 of #967's body fires (`spec.md` §*The
  tree as it stands, measured*; Alternative H).
- **#957's phase-3 records are not this item's baselines**: the contract's
  sha256 differs (Alternative I).
- **Two build phases, not one**: T6 is seen red at phase 3's start only if
  the proof block has already left (Alternative C).
- **The smith's definition keeps its `## Rules`** rather than moving them
  into `implement`, which a session also loads directly; the ladder, the
  file set and the second-rung list move the other way and live in
  `implement` alone (Alternative B).
- **`writing-style` stays one file** with its two language headings as
  `agents/warden.md:40-43` names them (Alternative D), and no rule of it
  leaves (decision 3; Alternative E).
- **`implement` keeps the headings other files cite** — `### 1.` to
  `### 6.`, `## The language the records are written in`, `## Document
  layout — two roots, three lifetimes` — because 12 sites in 9 files and
  the contract's §11 name them, and T5 holds that they resolve.
- **The smith names no runner of the broad gate** and says only that it
  does not run it (decision 6; Alternative L).
- **`skills/legacy-parity/SKILL.md`'s four emoji are #970's**, and T6 skips
  the file by name until then, the way `NOT_YET_REWRITTEN` skips a
  definition.
- **The question status words are `open` and `answered <date> by <who>`**
  (#957's `spec.md` §*Marks and labels*, the owner's rule), and the template
  changes here because T6 reads `templates/`.
- **Nothing is re-measured by hand**: every figure in the changelog comes
  from an eval record or `payload-meter` with its commit.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | **What is the spend stop for a paid phase?** Phase 1 and phase 4 each run 34 cases on the orchestrator's account, about $60 by #957's phase-3 figures (smith 5.9980, warden 36.6656, framer 17.3532), and phase 4 may run one agent a second time. #957's phase 3b stopped before the next agent past $90 | a person — the owner | **$90 a phase** (the default): the run stops before the next agent once the phase's summed `total_cost_usd` passes it, records what ran, and hands back · **a higher figure**: the second run of the warden ($37) fits inside the phase · **no stop**: `--max-cost-usd` (100 per invocation) is the only bound | $90 a phase, agents in the order smith, warden, framer; the run does not stop to ask | answered 2026-10-18 by the owner, through the night's budget: $200 for #967 and #969 together; this item stops before the next agent once its summed spend passes $150 or the two items' together pass $200 |
| Q2 | **Does the smith join `tests/test_docs_line_wrap.py#COVERED` at its rewrite, alone?** `seal/follow-up.md`'s row says the smith and the scribe go in together, with the argument that covering one and not the other reads as an oversight. That row was written when both needed a three-line rewrap; now each is rewritten anew in its own issue, and the warden and the sealer joined `COVERED` one at a time at theirs | a person — the owner | **join now, narrow the row** (the default): `agents/smith.md` and `skills/implement/SKILL.md` are written wrapped and added to `COVERED` in phase 2; the follow-up row is narrowed to the scribe for #970 in phase 5 · **wait for #970**: neither joins, and the row stands as written | join now, narrow the row | answered 2026-10-18 by the work: the default was taken in phase 2, and both files are in `COVERED` at aea8c8e5, and phase 5 narrowed the follow-up row to the scribe, answered by #970 |
| Q3 | **Do `skills/audit/SKILL.md`'s five emoji leave in this item?** They sit in the skill's result block (`:53-58`), text a session reads and writes; the owner's rule (#957, 2026-10-16) reaches text an agent reads or writes. T6 reads every `skills/*/SKILL.md`, and no issue owns `audit` for a skip entry to name | a person — the owner | **leave here** (the default): the five become the words `passed`, `warnings`, `violations` in phase 3, one line each · **skip by name**: T6 carries an `audit` entry naming #940, and the marks stay until #940 | leave here | answered 2026-10-18 by the work: the default was built, the five marks are the words (`phases/phase-3.md`) |
| Q4 | **What does one side cost for the three agents at 2fc33333?** #957's phase 3 read $60.0168; the contract grew by 134 bytes since | a measurement — phase 1's `total_cost_usd`, summed per agent in its phase record | — | about $60 | answered 2026-10-18 by the work: 65.7598 USD for the three sides that stand, 38.3854 more lost to the host's sleep (`phases/phase-1.md`) |
| Q5 | **Which pins on the three files pin a rule, and which pin narration?** 18 modules name the smith, 12 `implement`, 3 `writing-style` (#957's Q7, continued) | the work — phases 2 and 3 sort them, re-pointing a pin on a rule that stays and removing one on narration with a line in the phase record | — | — | answered 2026-10-18 by the work for the smith and `implement`: `phases/phase-2.md` §*The pins (Q5), sorted*; and for `writing-style`, whose three modules ran green in phase 3 (`phases/phase-3.md` §*Commands*) |
| Q6 | **Does the smith open `skills/implement/SKILL.md` in every run, and `writing-style`'s section before its records?** The definition says so; only the traces show it | a measurement — phase 4's traces, counted in the phase record (S3) | — | — | answered 2026-10-18 by the work: 8 of 8 runs opened each in phase 4's first take (`phases/phase-4.md`), and 8 of 8 in its second, counted from the kept traces (`phases/phase-5.md`) |
| Q7 | **Does the framer's rule 5 still fail on the restructured skills?** At #957's phase 3 it read 33,595.1 tokens per call against 28,253.1 for reasons the traces did not show | a measurement — phase 4's `evals/framer-phase-4.md`; a `fail` whose cause is `agents/framer.md` is carried to #968 (decision 5) | — | — | answered 2026-10-18 by the work: yes, rule 5 alone, +9.5% per call with total tokens down 0.5% and every grader passing; carried to #968 (`phases/phase-4.md`) |

**`Who can answer` takes one of three values and nothing else.**

- **a person** — what the product should be, or a value somebody has to be
  accountable for. Q1 to Q3 are this kind, and none blocks the build: each
  carries the default the run takes.
- **a measurement** — a probe, a command or a count settles it. Q4, Q6 and
  Q7 are read off phase 1's and phase 4's runs.
- **the work** — unknowable at framing time. Q5 is each build phase's own.

**The framer opens rows and does not own their answers.** The `Status`
column is written by whoever answered, as `answered <date> by <who>`, never
by whoever asked.

Answered rows feed back into docs/ (policy clause or open-questions section)
before this directory's work merges.
