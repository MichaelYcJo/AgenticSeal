# 1792311781-the-stamp-is-drawn-from-the-sealers-verdict — phase 7

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 7 |
| Commit | ffefb57e |


## What this phase was asked

The close after the reframe. In `overview.md`, the round-3 row of
§*Where spec and implementation diverged* says the condition as built: any
earlier `sealed`, whatever it named, with round 4's narrowing undone by the
reframe on the grounds of `rounds/round-5.md` and `questions.md` Q8, and
the amend limit kept. §*Fed back into the spec*'s first bullet says the
same, and `## Not done` gains the accepted missing stamp with Q7, Q8 and
#976. `phases/phase-6.md` records how phase 6's case was seen red and what
the mutation showed, and this record closes phase 7. Nothing in
`questions.md`: Q8 is answered and no row is new.

## What this phase found

**This record is one commit after the phase it records.** A phase record
carries the commit that closed its phase, so it cannot sit inside that
commit. Phase 7's memo and phase 6's record landed at ffefb57e, and this
file and phase 7's Status cell land in the commit after it, the way phase
5's record followed 55747b46.

**The checks the plan named** (executed, on the staged records before
ffefb57e): `bin/unverified-check` on this item exit 0, with three rows open
and one closed, the same rows as before; `chain_check.py --baseline
origin/release/v0.22.1 --worktree` exit 0, judged as a draft, reporting the
verifying round owed after b2f97fb1 and the absent `broad-gate.md` and
`guarantee.md`; `routing.md` reads `Planning | framer` and `spec.md`'s foot
carries the `Reframed 2026-10-18 by framer, after round 5.` line;
`test_the_record_is_written_in_words.py`, `test_no_real_identifiers.py` and
`test_a_phase_hands_the_next_one_a_record.py`, 23 passed; `git grep -n -F
'over a commit then in its history'` of `overview.md` prints nothing.

**A verifying round is owed.** b2f97fb1 changed `docs/the-review-record.md`
and the module after round 5's `target:`, so the pull request's check stays
red until a round reads b2f97fb1..HEAD. That round is the orchestrator's to
spawn.
