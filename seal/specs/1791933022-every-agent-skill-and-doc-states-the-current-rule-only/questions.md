# every agent, skill and doc states the current rule only — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. -->

**Judgments the ticket left open that the tree answered** — listed so nobody
reopens them; the grounds are in `spec.md` and `plan.md` §*Alternatives
considered*. Re-read on 2026-10-15 against #923's body as rewritten that day.

- The agent set stays five: every job needing judgment has one of them, and
  the fix pass, the broad run and the pull-request check need no sixth
  (`spec.md` §*The jobs*; alternative N).
- The record is the warden's one file, and the smith's fix pass writes two
  cells per open row. No generator, no copy, no derived field: each of the
  eleven removed fields is judged in `spec.md` §*What leaves, what stays*
  against the 19 records of 0.22.0 (alternatives B, D, E, F, O, P, Q).
- ⬜ leaves the vocabulary; a wrong sentence an agent acts on is 🟡 and a
  sentence in a record is not a finding (alternative Q).
- The `fix of a fix` stop is the warden's mark and the orchestrator's rule; the
  cap is one orchestrator rule with one number; neither is a check at the pull
  request until a run shows the need (alternatives E, F, M).
- The broad gate's one home is `broad-gate.md` on both routing answers.
- The sealer's verdict is a file in the tree, `guarantee.md`, read by the
  check; an owner's answer to `undecidable` is a line under the verdict, then
  the sealer runs again at the new HEAD (alternative I).
- The sealer pins `model: opus`; no other definition pins a model (owner,
  2026-10-15, #923 item 2).
- Every agent preloads the contract alone and opens its skill at the step; a
  case that shows the opened form falls short sends that skill back to the
  list (#923 item 4; alternative L).
- The contract numbers its rules anew; the 35 citations outside the rewritten
  files are rewritten in the same commit.
- The record lands first and the agents second, in two work items under one
  design, because the diff and the proof's baseline both ask for it
  (`plan.md` §*The split*; alternatives J, K). Overturnable at the approval
  of this plan.
- The three record documents are replaced by one; `docs/the-agent-set.md`,
  `docs/the-record-layout.md` and `docs/the-broad-gate.md` are rewritten where
  this item makes them false, and otherwise left to #941.
- Answered by the owner before this frame and still standing: the proof's run
  budget (≈ 120 runs, ≈ $150; 2026-10-14), the tree's
  `skills/writing-style/SKILL.md` as the one source (2026-10-13), no
  restatement report row (2026-10-15), `docs/one-root-by-lifetime.md` rewritten
  in #941 (2026-10-14).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | How many finding rounds may a run take before it stops and every open finding is deferred with a home? 0.22.0's runs: #944 two finding rounds then a verifying one, #930 two then one, #931 five then one, #929 six then one and the item was closed unfinished. The number is a cost a person is accountable for, and the tree holds no measurement that picks one | a person — the owner, who pays for the rounds | **3**: a run of #931's shape stops after its third finding round and defers the rest · **5**: #931 completes, #929 stops one round earlier than it did · **no cap**: the sealer and the person reading the pull request are the only bound | 3 | ✅ the owner answered on 2026-10-15: **3 by default, and variable with the run.** Past round 3 the orchestrator extends one round at a time while the latest round found fewer findings than the one before and none is a fix of a fix; a fix of a fix stops the fix passes before round 3 as well, and the item goes back to its framer. Each extension is one line in that round's record with its reason, and the sealer reads it. No person is asked mid-run |
| Q2 | What does one guarantor run cost — spend, seconds, tokens — on a real item? | a measurement — phase 4's first run of the three sealer cases, and part A's own sealer spawn | — | the estimate in `spec.md` §*The sealer*: ≈ $2–4, 5–10 min | ⬜ |
| Q3 | Which of the 70 test modules naming the three scripts keep a case in `test_chain_check.py` or `test_broad_gate.py`, and which leave whole? | the work — phase 3 sorts them as it rebuilds the arms and lists every deletion's guard in `phases/phase-3.md` | — | — | ✅ answered by the work in `phases/phase-3.md`: 28 modules left whole, two came back without the guard's cases, and the cases removed from kept modules are named there |
| Q4 | What are the real tokens a spawn reads after the rewrites, per agent? | a measurement — part B's baseline traces carry `usage`; `compare` writes both sides' pooled tokens | — | `payload_meter`'s estimate at 3.2 B/token, labelled estimated | ⬜ |
| Q5 | Of the pins the 52 test modules hold on `agents/*.md`, which pin a rule and which pin narration? | the work — each part B phase sorts its agent's and lists the dropped ones in its phase record and `overview.md` | — | — | ⬜ |
| Q6 | Which fields of the eval's per-run JSON and of the trace's `result` event carry a run's spend, seconds and tokens, on a real run? | a measurement — the first saved `raw.json` of part B's baseline, read against what `run` records (`total_cost_usd`, `duration_ms`, `usage.*`) | — | the names above | ⬜ |
| Q7 | How does a pull request into `main` read a work item that was squashed into the release branch? The check judges every `routing.md` a pull request adds, and a squashed item's last `Target SHA`, `broad-gate.md` run and `guarantee.md` commit are not ancestors of the release branch's HEAD, so the records, broad-gate and guarantee arms refuse each one (`executed` at cba5e0cd on this branch, `chain_check.py --baseline origin/main` with `GITHUB_HEAD_REF=release/v0.22.0`: four squashed 0.22.0 items each named *which HEAD does not descend from*, and none of the four carrying a `broad-gate.md`). `skills/settle/SKILL.md` says those records are still read at the release pull request | a person — the owner, who decides what a release pull request re-proves | **judge at the item's own pull request only**: the release pull request judges the declarations naming its own branch and the ones its own commits changed, never an item merged by squash · **resolve the commit elsewhere**: what the removed pull-head fetch did, and a branch deleted or squashed is again a reason to fail · **the release pull request reads the release's own guarantee**: the release seal is one guarantee over the release, and the items' files are history | the first — an item is proved at the pull request that carries it | ✅ answered by default, by the orchestrator under automation on 2026-10-15, for the owner to confirm: an item is judged at the pull request that carries it. Built in phase 5 at 27dd748d: a declaration every commit after the base touched as a GitHub squash merge (committer `noreply@github.com`, subject ending `(#N)`) is named and not judged (`chain_check.py#carried_by`, `docs/the-review-record.md` §*What the check reads at the pull request*). Probed on a scratch squash of this branch into `release/v0.22.0`: the check at af4d0c31 exits 1 naming all five items, the new one exits 0 naming each with its squash, and a commit made on the release branch itself that changes this item's `routing.md` is judged and exits 1 (`phases/phase-5.md`). Overturning it is a change to `carried_by` and its four cases |

No row waits on a person; Q7's default is built and stands until the owner
confirms or overturns it. Q2, Q4 and Q6 are a measurement's; Q5 is the
work's, in part B.
