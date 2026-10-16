# every agent is written anew from its job (#957) — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here. -->

## What the tree answered, so nobody reopens it

The ticket left these open and the repository settled them; the grounds are
in `spec.md` and in `plan.md`'s Alternatives table. What the tree answered
about the mechanics — the `Reads:` lines, the grammar's placement, the
closing mark, the red Windows case — is in #964's `questions.md`.

- **The contract is renumbered from §1**, and every citation in the tree is
  rewritten in the same commit; the never-reuse rule holds from this edition
  (`plan.md` Alternative F).
- **`Enforced by:` keeps its spelling here**; its rename is #941's, with
  `rules.py` as the reader (Alternative N).
- **No scribe case is written**; the scribe is measured on bytes, and its
  outcome is `unverified` with the owner named (Alternative K; Q3 put the
  default in front of the owner, who kept it).
- **The warden is the proof on one file**, before the contract, and the
  contract is a phase of its own (Alternative G).
- **The sealer stays on Opus until the comparison**, and drops only where
  every truth grader holds on Sonnet and spend is lower (`spec.md`
  §*The sealer's model is decided by measurement*).
- **The emoji in output printed for a person and read by no agent or check**
  — the release note's headings, the seal stamp's drawing, the hooks'
  terminal messages — stay, because the owner's rule reaches what an agent
  reads or writes and what a check reads; Q9 put the remainder in front of
  the owner, who kept the default.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | **Does this item run as one work item on this branch, or as the two of `plan.md` §*The split*?** `routing.md` names one branch. #923's one diff that did many things took ten review rounds, and `plan.md` Alternative J of that item is the lesson. Item 1 (phases 0, 1, 2, 8 of the frame as first drawn) is checks and tests verified by CI alone; item 2 (phases 3–7, 9) is the agents with the paid proof. Splitting needs a second issue or work item, which only a person opens | a person — the owner | **one work item**: the phases run in the table's order on this branch, phase 8 before phase 3, one review chain over the whole diff · **two work items**: a second `routing.md` is written for item 1 on a branch cut from `release/v0.22.1`, item 1 merges first, and this branch is rebased on it before phase 3 | one work item, in the table's order | answered 2026-10-16 by the owner: two work items; item 1 is #964 at `seal/specs/1792129100-the-mechanics-leave-before-the-agents-are-rewritten/` and merges first; this branch is rebased onto `release/v0.22.1` after it, and its phases are renumbered 1–6 |
| Q3 | **Is a scribe case worth a parity fixture generator?** The scribe has no cases, so its rewrite is measured on bytes only and its outcome is `unverified`. A case needs a fixture original and a `seal/parity.md`, which is a generator nobody has asked for, for an agent no run in this repository has spawned | a person — the owner | **no case** (the default): the scribe's outcome stays `unverified` in the phase record with the owner named, until a parity run happens · **one case**: `rule_cases.py` gains a parity fixture and the scribe set runs in phase 5 (about 2 more runs) | no case | answered 2026-10-16 by the owner: the default was shown and kept — no case |
| Q4 | **What does one run of each agent's cases cost — spend, seconds, tokens — on this tree?** The owner's figure of about $150 for about 120 runs is nobody's measurement (#923 `questions.md:149`); `plan.md` counts 126 runs from the case counts | a measurement — phase 1's baseline, whose per-run `total_cost_usd` and `duration_ms` are summed per agent in its phase record | — | the owner's figure stands as the estimate until phase 1 reads the fields | open |
| Q5 | **Which fields of the eval's per-run JSON and of the trace's `result` event carry a run's spend, seconds and tokens?** `noninferiority.py#run_cost` reads `total_cost_usd`, `duration_ms` and `usage` from the last `result` event; whether the runner still writes them in that shape is read off the first saved run (#923's Q6, moved here) | a measurement — phase 1's first saved run | — | the three names `run_cost` reads | open |
| Q6 | **Does `claude plugin eval` honour a definition's `model:` key for the subagent it spawns?** The sealer's comparison varies one line, `agents/sealer.md`'s `model:`; where the subagent's model comes from the case's `execution.model` instead, the comparison has to vary the case, not the definition | a measurement — phase 1's sealer baseline run, whose trace names the model each turn ran on | — | the definition's `model:` is honoured, as `agents/sealer.md` and `rule_cases.py#MODELS` already assume | open |
| Q7 | **Which of the pins the test modules hold on the rewritten files pin a rule, and which pin narration?** 42 modules name a file under `agents/`, 11 the contract, 12 `implement`, 6 `code-review`, 3 `writing-style` (#923's Q5, moved here) | the work — phases 2 to 5 sort them as each file is rewritten, re-pointing a pin on a rule that stays and removing one on narration with one line in the phase record | — | — | open |
| Q8 | **What are the real tokens a spawn reads after the rewrite, per agent?** `payload-meter` estimates at 3.2 bytes a token, uncalibrated (#923's Q4, moved here) | a measurement — the eval traces of phases 2 to 5, whose `usage` fields are summed in each phase record beside the meter's estimate | — | the meter's estimate stands in the changelog table, labelled as such, until the traces are read | open |
| Q9 | **Do the emoji in output a script prints for a person leave too?** `.github/scripts/publish_release_note.py` (23), the seal stamp's drawing (`seal_stamp.py` 9, `broad_gate.py` 22), the hooks' terminal messages (30 in 15 files) and the test fixtures quoting old records (521) are read by no agent and no check. The owner's rule as the frame reads it reaches what an agent reads or writes and what a check reads | a person — the owner | **stay** (the default): this item removes every mark an agent reads or writes and a check reads, and names these as out of scope in `spec.md` · **leave too, in this item**: a sweep of about 600 characters over 100 files, each a message a person reads · **leave in #940 and #942**, whose files they are | stay, named as out of scope | answered 2026-10-16 by the owner: the default was shown and kept — they stay, out of scope |

Q2, the closing word of `## Not verified`, moved to #964's `questions.md`
with its phase; the numbers here are kept so that `spec.md`'s and
`plan.md`'s references to Q3–Q9 still name the rows they did.

**`Who can answer` takes one of three values and nothing else.** They were one
shape on the page before this, and #84's second comment measured all three
inside a single run's four rows.

- **a person** — what the product should be, or a value somebody has to be
  accountable for. This is the file's stated purpose, and the only kind of row
  that blocks the build.
- **a measurement** — a probe, a command or a count settles it, so asking a
  person is the wrong instrument and queueing it behind one wastes a round
  trip.
- **the work** — unknowable at framing time. The phase that meets it decides
  it there and records a divergence row; it does not travel back to the
  framer.

**The framer opens rows and does not own their answers.** The `Status`
column is written by whoever answered, as `answered <date> by <who>`, never
by whoever asked. No row blocks the build: Q1, Q3 and Q9 are answered,
Q4–Q6 and Q8 are read off phase 1's runs, and Q7 is each rewrite phase's
own work.

Answered rows feed back into docs/ (policy clause or open-questions section)
before this directory's work merges.
