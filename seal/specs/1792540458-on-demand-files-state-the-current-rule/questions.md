# what an agent opens on demand states the current rule, and the CLAUDE.md block has one copy (#940) — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here. -->

**What the ticket left open and the tree answered**, so nobody reopens it.
Each line names where the answer was read or how it was counted.

- *Do behaviour cases exercise the files this item rewrites?* Yes. Every
  case spawns its agent on the plugin tree at the measured revision
  (`evals/scripts/noninferiority.py#run_side`, read), and each definition
  directs its agent to open rewritten files (`plan.md` *Technical context*
  lists the lines, read). So the owner's 2026-10-20 condition for skipping
  the paid run (#941 Q1: no case exercises the changed files) does not hold
  here; Q1 below.
- *Does `chain_check` read the approval line?* No longer: `APPROVED_RE` left
  in 8350c578 (#923; executed `git show`), and nothing else in the tree reads
  it (executed `git grep`). The owner's shape stands as a stated rule whose
  reader is the warden (`plan.md` A14, A15).
- *Which skills does this item rewrite?* Not `implement/SKILL.md`,
  `code-review/SKILL.md`, `writing-style/SKILL.md` (#968 and the warden's
  rewrite, `seal/specs/1792251842-*/spec.md` orchestrator decisions 2 and 3,
  read) or `settle/SKILL.md` (#953, the issue body). They take only Scope 1,
  8, 9 and 10.
- *Which syntax outside `docs/` is this item's?* `spec.md` Scope 8: the
  heading citations' section sign, the template's arrow heading and its
  coordinate hint here; the contract's numbering, the agents, the scripts,
  `coordinates.py`'s grammar and the changelog markers in a later item.
- *Does the block carry the design direction?* No (`plan.md` A4). *A line
  for the writing directions?* No (A8).
- *Where do the writing directions live?* `skills/writing-style/SKILL.md`,
  with a compact rule in `CLAUDE.md` (`plan.md` A5 to A7).
- *Which `CLAUDE.md` rows stay?* `spec.md` Scope 3, each with the premise
  the build checks.
- *Where is the local-install sentence?* `skills/update/SKILL.md` step 4,
  beside the step the issue names.
- *D7's moment?* Before the party that opens the pull request spawns the
  sealer (`spec.md` Scope 9).
- *Is `docs/` edited?* No; three citations are `## Rule changes`, and a
  renamed heading another `docs/` line cites adds one.
- *Does `seal/follow-up.md` hold an item this work is a prerequisite of?*
  No (executed `grep` for the files in scope).
- *Does a subagent spawned here load this repository's `CLAUDE.md`?*
  Assumed yes, as `skills/verify/scripts/payload_meter.py` counts it among a
  spawn's harness files (`tests/test_the_payload_meter_says_what_it_measured.py:262`,
  read). Either answer builds the same thing: the agents also reach the
  writing rules through `writing-style`.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Is the paid non-inferiority run made for this item? The tree cannot weigh the spend, and a run as shipped cannot pass: rule 4 refuses a preload not below the baseline's, and this item changes no preload. Prices from #941's Q1 (read): about 65 USD and 3.2 hours a side for the four agents, framer about 15, smith 6, sealer 4, warden 40 | a person | (a) all four agents, both sides, after phase 9, about 130 USD and 6.4 hours serial, after a change making rule 4 pass an unchanged preload (one branch of `noninferiority.py#verdict` and its case); (b) the smith and the sealer only, both sides, about 20 USD, the two whose opened text changes most (the `verify` split), with the same rule-4 change; (c) not run: S13's on-demand bytes per agent read with `wc -c`, S11's census and S10's review | (c). The build proceeds without the run. A run not made can still be ordered at the pull request and made before the merge with the commands in `plan.md`; a run made cannot be taken back. This departs from the owner's 2026-10-20 condition, which does not hold here (head of this file), and the pull request body names the departure | open |
| Q2 | Does this item write #945's orchestrator rules (sections 1 and 2 of its body: a fresh spawn per phase and the resume threshold, `mergeable` read before waiting on CI, a rebase after review followed by one verifying round, a decision folded into the one source the next reader reads, a prevention home for a recurring problem)? #945's body says #940 writes them, on the condition that #945 is framed first; it is not (no directory under `seal/specs`, executed `ls`), and its milestone is 0.22.4 | a person | (a) here, in phases 2 and 4, framed from #945's body; the threshold of section 1 has no value in the body, so it would be a row of its own; (b) not here: phases 2 and 4 state the rules as they rule at b3154f43, and #945's frame edits the two files in place | (b) | open |
| Q3 | Which `BASELINE` pairs reach zero, and what residue each keeps? Unknowable until the files are rewritten | the work | each phase measures the pairs of its files and records the count with whose the residue is | phase 9 lowers each entry to its measured count and removes those at zero | open |
| Q4 | Can the block hold Scope 2's rules in 1,500 bytes? Unknowable until the bullet is written | the work | phase 3 writes the rules and measures | over 1,500, the phase record names each sentence over and why it is a rule rather than reasoning | open |

**`Who can answer` takes one of three values and nothing else.** They were one
shape on the page before this, and #84's second comment measured all three
inside a single run's four rows.

- **a person** — what the product should be, or a value somebody has to be
  accountable for. This is the file's stated purpose, and the only kind of row
  that blocks the build.
- **a measurement** — a probe, a command or a count settles it, so asking a
  person is the wrong instrument and queueing it behind one wastes a round
  trip. Measured: six probes at about three seconds each answered a row that
  had been written into the human batch, and they showed the ticket's own
  instruction was wrong.
- **the work** — unknowable at framing time. The phase that meets it decides
  it there and records a divergence row; it does not travel back to the
  framer, which would spend the interruption the framing phase exists to spend
  once.

**The framer opens rows and does not own their answers.** A row is a question
put to somebody else, so opening one costs little and closes nothing — and the
`Status` column is written by whoever answered, as `answered <date> by <who>`,
never by whoever asked. Sorting the rows this way is also what keeps the
batch short enough to answer in one sitting: two of the three kinds never
needed a person at all.

Answered rows feed back into `spec.md`'s `## Rule changes` (a policy clause
or an open-questions section) before this directory's work merges.
