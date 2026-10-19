# 1792368013-the-scribe-is-written-anew-from-its-job — phase 3

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | ef570495 |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

Run `payload-meter --agent scribe` at 1d665d48's tree and at the build's,
and hold the read set (the preload plus `legacy-parity`, which the scribe
opens at step 1) at or below 25,691 B. Write `overview.md` and the changelog
fragment. The outcome stays `unverified`, with the owner named, until a
parity run happens.

## What this phase found

**The read set holds, by 81 bytes.** The agent's share is 25,691 B at
1d665d48 and 25,610 B at c8391342. The preload fell by the 5,325 B of
`legacy-parity` and 444 B of the scribe; the skill came back at step 1 at
5,688 B, 363 more than it was.

| Figure | 1d665d48 | c8391342 |
|---|---|---|
| `agents/scribe.md` | 3,763 | 3,319 |
| `skills/agent-contract/SKILL.md` | 16,603 | 16,603 |
| `skills/legacy-parity/SKILL.md`, preloaded | 5,325 | — |
| `CLAUDE.md` pair on this machine | 14,775 | 14,775 |
| preload, `payload-meter`'s total | 40,466 | 34,697 |
| `skills/legacy-parity/SKILL.md`, opened at step 1 | — | 5,688 |
| read set | 40,466 | 40,385 |
| read set, the agent's share | 25,691 | 25,610 |

The contract and `CLAUDE.md` are the same bytes on both sides (`git diff
--stat 1d665d48 HEAD -- CLAUDE.md skills/agent-contract/SKILL.md` printed
nothing), so the comparison of the two files the item writes says the same:
9,088 B at 1d665d48 and 9,007 B at c8391342.

**Where each side was measured.** 1d665d48's side is that commit's `agents/`,
`skills/` and `CLAUDE.md`, taken with `git archive` into the scratchpad and
measured with this branch's `bin/payload-meter --root <copy>`; the copy was
removed after. The build's side ran on the worktree at cdd1cbde, whose
`agents/`, `skills/` and `CLAUDE.md` are c8391342's: the commits after it
touch only this work item's records.

**What stays unverified.** No case runs the scribe (#957's Q3), so whether a
spawn opens `legacy-parity` at step 1, reads only the sections it names, and
returns `original not found` rather than a guess is unread by anything. That
row is in `overview.md` §*Not verified* with the repository owner as its
answerer, and in the changelog's table as the outcome.

**Q5 stays open.** Which item rebases on the lines #968 also edits is decided
at that rebase, after this item; the plan says this item lands first.

### Commands, each with its exit code

| Command | Exit |
|---|---|
| `bin/payload-meter --root <1d665d48 copy> --agent scribe` | 0 |
| `bin/payload-meter --root <worktree> --agent scribe` at cdd1cbde | 0 |
| `git diff --stat 1d665d48 HEAD -- CLAUDE.md skills/agent-contract/SKILL.md` | 0: nothing printed |
| `bin/rules --check --root <worktree>` | 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.22.2 --root <worktree> --worktree` | 0: it names the round record, `broad-gate.md` and `guarantee.md` as not yet written, which the review chain, the orchestrator's broad run and the sealer write |
| `bin/unverified-check <worktree>` | 0 |
| `bin/test tests/test_the_changelog_is_gathered_at_release.py tests/test_a_question_says_who_can_answer_it.py tests/test_the_set_a_work_item_always_has.py tests/test_unverified_rows_close.py tests/test_chain_hooks_hardening.py -q` | 0: 352 passed |
