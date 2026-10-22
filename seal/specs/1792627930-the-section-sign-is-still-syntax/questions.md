# Questions for the planner: #1005 the section sign is still syntax

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md holds the decisions
only a human can make, extracted so nothing ships on a silent assumption.
Before adding a row, the framer checks the inheritance rule: where policy is
silent but existing behaviour answers the question, the framer inherits that
answer and records it; only a new rule belongs here. -->

**What the issue left open and the tree answered.** Nobody reopens these;
the grounds are in `spec.md` and `plan.md`.

- **Number or heading text for the contract's rules: number.**
  `docs/the-agent-set.md` *One contract every agent receives, and one
  definition each* makes the numbers stable and cited, and a heading-text
  citation grows every preload (`plan.md` A1).
- **The spelling: `contract rule N`, and `rule N` inside the contract and
  `agents/`.** The free simulation in `plan.md` *Technical context* is the
  only spelling of four that lowers every preload (executed).
- **The records of a moment are not rewritten.** `seal/specs/`,
  `changelog/`, `CHANGELOG.md` and `evals/behaviour/`: a record states what
  was true when written, `CONTRIBUTING.md` *House rules* gives `changelog/`
  to the branch based on `main`, and `evals/README.md` says the cases are
  generated and never edited by hand.
- **The old spelling is refused by one case, not by each reader.** One fact
  read in one place (`plan.md` A6, A7).
- **`skills/verify/scripts/coordinates.py` needs no reader change for the
  section sign.** At a16acb40 it carries one, in a docstring, and its grammar
  reads none (executed). Its `#` and `>` are Q2.
- **The dash in the release heading `## X.Y.Z — <date>` is not this item's.**
  Neither the issue nor #941's Q2 names it (`spec.md` *Scope*).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Do the changelog markers `<!-- specs/<id> -->` change? The issue lists them as left over, and #941's Q2 called them syntax a check reads. **Why the tree cannot answer:** `docs/branch-and-release.md` *Work accumulates on a release branch* states the HTML comment and why it is invisible, so changing it changes a docs rule, and whether the owner meant that is the owner's to say | a person | (a) **Unchanged**: `gather_changelog.py` loses only its two section signs, and nothing reads a new spelling. (b) **A visible line**: a docs rule change, and a rewrite of the markers in 54 release files, which only the branch based on `main` may make, so it lands at a release and not here; the release note shows each id twice, once in the line and once in the entry's own trailer. (c) **Near misses refused**: fails on 27 lines of an older convention in 11 release files (executed), which this branch may not edit | (a). The build proceeds on it; `plan.md` A11 to A13 hold the grounds | open |
| Q2 | Does this item also take the coordinate grammar's `#` and `>` and the pact anchors `skills/verify/scripts/coordinates.py` reads? `seal/specs/1792540458-on-demand-files-state-the-current-rule/spec.md` scope item 8 named them for "a later item", and #1005 is that item, but the issue's text names only the section sign and the changelog markers. **Why the tree cannot answer:** which of two texts sets the scope is the owner's, and a pact anchor is written in another repository's tree | a person | (a) **Not here**: a later item takes them, with the cross-repository migration a pact anchor needs. (b) **Here**: a new phase that changes `coordinates.py`'s grammar, `pact_check.py`, `chain_check.py`'s anchor reading, `templates/sdd-spec.md`'s `## Removes` hint and the pact clauses in other repositories | (a) | open |
| Q3 | Is the paid non-inferiority run made? The issue says #923's proof is owed, because the contract and the five definitions are preloaded. **Why the tree cannot answer:** the spend is the owner's. The price, read from #941's Q1: about 65 USD and 3.2 hours a side for framer, smith, sealer and warden (framer about 15, smith 6, sealer 4, warden 40); scribe has no cases | a person | (a) **Both sides, four agents**, after phase 3: about 130 USD and 6.4 hours serial, and rules 1, 2, 3 and 5 read. (b) **The new side only**, against the newest recorded sides: about 65 USD, but those sides were taken on preloads that have changed since, and `evals/README.md` refuses a warden pair taken across #986's squash. (c) **Not run**: rule 4 is read for free at phases 1 and 3; the change is the spelling of citations, with no rule added or removed, and the precedent is #941's Q1, answered (c) by the owner on 2026-10-20 | (c). The build proceeds without a run, and the pull request body names the departure from the issue. A run not made can still be ordered at the pull request | open |
| Q4 | What does a touched citation become where its file has no such heading? Two are known (`spec.md` scope item 9); the rest are known only when each line is read. **Why the tree cannot answer now:** it needs each citation read against the rule it points at | the work | The phase that meets one names the heading that now holds the rule, or, where none does, rewrites the pointer in words | The heading that holds the rule; each one listed in the phase record | open |
| Q5 | Is every agent's preload below its baseline at the end, measured against the base this branch has once #988 and #1009 merge? #988 changes `agents/warden.md`. **Why the tree cannot answer now:** the base is not cut yet | a measurement | `noninferiority.py#preload_bytes` for the five agents at the base and at head, run by the smith at phases 1 and 3 | The simulation's figures: every preload falls by 18 to 38 bytes (`plan.md` *Technical context*) | open |

**`Who can answer` takes one of three values and nothing else.**

- **a person**: what the product should be, or a value somebody has to be
  accountable for. This is the file's stated purpose, and the only kind of row
  that blocks the build.
- **a measurement**: a probe, a command or a count settles it, so a person is
  the wrong instrument, and queueing the row behind one wastes a round trip.
- **the work**: unknowable at framing time. The phase that meets it decides
  it there and records a divergence row; it does not travel back to the
  framer, which would spend the interruption the framing phase exists to spend
  once.

**The framer opens rows and does not own their answers.** A row is a question
put to somebody else, so opening one costs little and closes nothing, and the
`Status` column is written by whoever answered, as `answered <date> by <who>`,
never by whoever asked. Sorting the rows this way also keeps the batch short
enough to answer in one sitting: two of the three kinds never need a person.

The orchestrator carries each answered row into `spec.md`'s `## Rule
changes` (a policy clause or an open-questions section) when it drains the
work item's rows, at the moment `skills/implement/SKILL.md` *6. Drain the
rows before the broad run, and keep the records* names.
