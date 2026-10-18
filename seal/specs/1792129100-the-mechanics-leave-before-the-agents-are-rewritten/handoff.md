# 1792129100-the-mechanics-leave-before-the-agents-are-rewritten — handoff

Written 2026-10-16 by the orchestrating session, at the owner's call, after
phase 4. The next session runs on another machine, so nothing here lives in
that machine's memory: what follows is the part of the run's state that the
frame, the phase records and the issues do not already hold.

## Where the work stands

- **#964** (this item), branch `chore/964-the-mechanics-leave-before-the-agents-are-rewritten`,
  based on `release/v0.22.1` at d426fbdb (#963 merged). Phases 1–4 are built;
  `plan.md`'s Status column names each closing commit. Phase 4's record is
  d1ff02a5. Nothing of the review chain has run: no `rounds/`, no
  `broad-gate.md`, no `guarantee.md`, no pull request.
- **#957**, branch `chore/957-every-agent-is-written-anew-from-its-job`, holds
  only its frame (spec, plan, questions; last commit ba14fd90, the sealer's
  verdict words). It is based on d4552372 and is rebased onto
  `release/v0.22.1` after #964 merges. Its plan is not approved yet.
- CI was dispatched on this branch after every phase (`gh workflow run
  test.yml --ref <branch>`; a pushed branch with no pull request runs nothing
  on push). Phase 1 green (38859692605). Phase 2 failed one pinned sentence,
  fixed at 1459b214. Phase 3 failed two cases, fixed at d4242aff. Phase 4's
  run 38867411967 at d1ff02a5 is green on all three legs, and the rows it
  answers are closed. Two stay open: the hygiene step at the pull request
  (the orchestrator), and in-flight user records (the owner).

## Next, in order

1. The review chain on #964 (`skills/code-review/orchestration.md`): warden
   rounds, default cap 3, counted from the last design change; a regression
   routed to the fix pass earns one more verifying round. Ask the warden to
   look at `chain_check.py`, which grew from 1,597 to 1,850 lines in phase 3
   (constants out, the loader in), for what can go.
2. The broad gate by script, nothing else running: `bin/broad-gate --base
   origin/release/v0.22.1 --record
   seal/specs/1792129100-the-mechanics-leave-before-the-agents-are-rewritten`
   (the item's directory). Then the sealer
   (Opus), which reads `broad-gate.md` and audits; it does not run the gate.
3. The pull request into `release/v0.22.1`, opened ready after the sealer
   (#943). The owner merges 0.22.x pull requests directly, past CI where only
   the 0.21.x rules still fail it. Squash.
4. #957: rebase onto `release/v0.22.1`, show the owner the frame's phases
   again only if the rebase changed them, fill `plan.md`'s `Approved` line,
   and spawn the smith for its phase 1, the baseline (paid; read its spend
   before phase 2).

## Decisions of 2026-10-16 the tree does not show on its own

- The split: #964 first, #957 after (owner's answer to Q1, both in
  `release: 0.22.1`). Q2, Q3 and Q9 took their defaults.
- Phase 3 also refuses a finding without exactly one `severity:` (`must` or
  `should`) and one `answer:`. Kept as a divergence; the owner may overturn
  it.
- Phase 4 rewrote 31 overviews, not the plan's four, because `hygiene.yml`
  reads every overview under `seal/specs/` and the new reader refuses the
  old mark; round records keep their old marks (#923's Q10).
- The sealer's verdict becomes `sealed`, `withheld — <reason>`,
  `undecided — <question>` in #957's sealer phase (#957's body, item 2).
- The framer runs on Fable for #957's frame and its splits; smith, warden
  and sealer on Opus. Two agents at a time; a fresh spawn per phase.

## How the agents were run, and what slipped

- Every spawn prompt carried: edit with Edit and Write only; no `sed -i`, no
  heredoc of any kind, no `git stash`, no `bash -c`, never `cd`; the
  repository by its literal path in every git command; author the address
  the clone pins repo-local (`git config user.email`), never another;
  `Co-Authored-By` with the model; no push (the orchestrator pushes);
  scratch under the session's scratchpad, deleted at the end; clean up only
  what you started; the removed ledger machinery named as removed.
- Phase 3's smith still broke four of these (one `sed -i`, one scratch
  heredoc, one `cd`, one variable in a commit, which the gate refused). The
  instructions alone do not hold this; #957's smith rewrite is where it is
  answered.
- Phase 2 changed a doc sentence and missed the test that pinned it word for
  word. Phases 3 and 4 were told to `git grep -n -F` a fragment of every
  changed sentence over `tests` and `evals` and run what it finds; keep
  telling them.
- The frame's counts were off twice (364 `Reads:` lines were 304; 55 stamps
  were 12, in 55 files). Tell each smith to count from the tree.
- The shell here is zsh: an unquoted variable does not split, so use
  `${(f)VAR}` or `${=VAR}`. The commit gate refuses `bash -c` and a variable
  in `git -C $W commit`.
