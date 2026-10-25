# the sealer reads the gate the orchestrator ran (#969) — questions for the planner

## What the tree answered, so nobody reopens it

The issue left these open and the frame decided each from the tree; the
grounds are in `spec.md` and `plan.md`'s Alternatives.

- **How the comparison survives the rename** — two steps (orchestrator's
  decision 3): step A on a regenerated suite with the old words, step B's
  single run as a new reference, never compared across. Grounds:
  `noninferiority.py:912-920` refuses differing suites; a one-step order
  would measure the rename (`plan.md` Alternatives, row 5).
- **What the `Broad gate` cell of `guarantee.md` reads** — the run
  `broad-gate.md` names, not `sealed`; the sealer no longer sees the gate
  print, and `sealed` then has one meaning in the file (`spec.md` S9).
- **How step 1 reads the record** — the sealer applies
  `docs/the-review-record.md` §*The broad run has one home* with one `git log
  --name-only`, not a `chain_check.py` run (`plan.md` Alternatives, row 1).
- **Whether the sealer's own rule is graded by a case** — yes: a fourth case
  `rule-sealer-no-gate` and a `shape-runs-no-broad-gate` grader on every
  sealer case, added in phase 1 so both sides run them (about $1.30 a side).
- **Whether the model decision is code** — yes, `noninferiority.py model`,
  so S7 is recomputed rather than read.
- **`agents/smith.md:299` and `agents/framer.md:24`** — left to #967 and
  #968, which rewrite those files whole now; an edit here would put another
  agent's preload in this item's read set (`spec.md` §*Scope*, *Out*).
- **`hooks/sealer-stamp.py`'s name** — kept; the docstring is rewritten
  (`plan.md` Alternatives, row 4).
- **A `fail` on a cost rule alone** — recorded as it reads; the item goes to
  its pull request, where the owner reads it (`spec.md` §*What a fail means
  here*, #923 Q7, #957's framer record).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | **Are the warden, the smith and the framer measured again in this item because contract §2 changes?** #969's guard 1 says an agent whose read set this issue touched is measured again, here; §2 is in every preload. At #957's phase-3 spends that is about $59 (warden 36.67, smith 6.00, framer 17.35), over the $40 the orchestrator set for this item. Against it: §2's new sentence forbids the three an act none of them performed, #967 and #968 measure the smith and the framer on trees carrying this §2 once they rebase, and guard 2 judges every agent's last side at the milestone's close | a person — the owner | **not here** (the default): the §2 edit is named in phase 3's record as a read-set change for #967, #968 and the milestone's close, and the warden's last side (`#957/evals/warden-phase-3.json`) is named as predating it · **here**: three more `run`/`compare` pairs in phase 4, about $59, with the records committed under this item's `evals/` | not here | open |
| Q2 | **Does the drop to Sonnet also require every shape and reach grader to pass as often, or the truth graders alone?** #957's §*The sealer's model is decided by measurement* says truth graders and spend. The sealer's shape graders are *commits nothing*, *writes only `guarantee.md`*, *the verdict line's shape* and, from phase 1, *runs no broad gate*; a Sonnet that commits or writes elsewhere passes every truth grader. The frame's rule in `spec.md` S7 adds the shape and reach graders, which is `compare`'s rule 3 read over the two model sides | a person — the owner | **truths, shapes and reach** (the default): `noninferiority.py model` prints `sonnet` only where no grader passes less often on the Sonnet side and its spend is lower · **truths alone**, as #957 wrote it: a lost shape grader on the cheaper side still prints `sonnet` | truths, shapes and reach | open |
| Q3 | **Does the sealer's step-3 re-run meet the eval sandbox's interpreter refusal?** #957 phase 3 saw every `broad-gate` first call exit 134 (`libpython3.12.dylib … blocked by sandbox`) and the runs work round it with a shim. The gate leaves the sealer's runs here; `python3 -m unittest` in the at-base clone is the sealer's remaining interpreter call | a measurement — phase 4's traces, the first `Bash` call of step 3 in each run, read for exit 134 and the shim | — | the re-run works, as the baseline's did after its shim | answered 2026-10-18 by the work: the refusal is in 6 of 8 Opus traces and every run reached its verdict (`phases/phase-4.md`) |
| Q4 | **Does `run --tree <copy>` honour the copy's `model: sonnet` as `--rev` honoured `model: opus`?** #957 Q6 measured `--rev`; `--tree` copies the directory with `shutil.copytree` and the eval reads the same `agents/sealer.md` (`noninferiority.py:435-439`) | a measurement — the Sonnet side's first trace, every assistant event's `message.model` | — | honoured; a trace naming Opus stops phase 4 and the copy is checked for the edit | answered 2026-10-18 by the work: the sealer's 60 events on Sonnet, none on Opus, counted from the kept traces by `type` `assistant`, `message.model` and `parent_tool_use_id` (`phases/phase-4.md`) |
| Q5 | **What do the four sides cost?** #957's sealer sides read $3.04 and $4.08 for 6 runs; a fourth case adds about a third | a measurement — each side's `costUsd` summed in its phase record; the item's total in `overview.md` | — | about $17 to $22, under decision 4's $40 | answered 2026-10-18 by the work: 20.2197 USD for seven sides, 7.4013 for phases 2 and 4, 2.9882 for the four-case reference, 3.0973, 3.3431 and 3.3898 for the five-case ones rounds 1 to 3 called for (`phases/phase-4.md`, `phases/phase-6.md`) |
| Q6 | **Which of the fourteen modules naming `agents/sealer.md` pin a rule, and which pin narration?** `spec.md` §*The tree as it stands* names the eight with assertions on the run; the rest are read as each is met | the work — phase 3 sorts them, re-pointing a pin on a rule that stays and removing one on narration with one line in the phase record (#957 Q7's shape) | — | — | answered 2026-10-18 by the work: phase 3 re-pointed each pin on a rule that stays and replaced four with T1 and T2, each named with the mutation it went red on (`phases/phase-3.md`, *Pins changed*) |
| Q7 | **Which of #967, #968 and #970 merges before this item, and what does the rebase carry into the class grep?** `agents/smith.md:299`, `agents/framer.md:24` and `skills/verify/SKILL.md` §*Every agent seals* are theirs; whichever merges first changes what the grep finds | the work — the grep of phase 3 is re-run after each rebase and its result named in the phase record; a sentence an earlier merge removed is one fewer site, never a new edit here | — | — | answered 2026-10-18 by the work: none merged before the close (`origin/release/v0.22.1` at 2fc33333, fetched at phase 7), so the branch was not rebased and phase 3's grep stands, its `agents/smith.md` lines #967's (`phases/phase-7.md`) |

**`Who can answer` takes one of three values and nothing else.**

- **a person** — what the product should be, or a value somebody has to be
  accountable for. The only kind of row that blocks the build; under this
  run's `automation` answer it blocks nothing and the default is built.
- **a measurement** — a probe, a command or a count settles it; asking a
  person is the wrong instrument.
- **the work** — unknowable at framing time; the phase that meets it decides
  it there and records a divergence row.

**The framer opens rows and does not own their answers.** The `Status`
column reads `open` or `answered <date> by <who>`, written by whoever
answered. Answered rows feed back into `docs/` before this directory's work
merges.
