# 1791781864-the-idle-session-rows-ask-nobody — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 17d7ed5f |
| Ran by | specseal:smith on claude-opus-5-5 |

## What this phase was asked

Phases 1 and 2 of the approved `plan.md`, in this worktree, on
`fix/896-the-idle-session-rows-ask-nobody` from `0b52518f`, base
`origin/release/v0.21.0` at `c38f97d7`. Phase 1 is `spec.md` In 1:
`fmt_sessions`'s unidentified branch prints `<kind> <age>` in both
languages, and S1 and S2 are cases in `tests/test_worktree_guard.py` beside
`test_switch_idle_sessions_offer_both_ways_on`, seen red at `c38f97d7`.
Phase 3 waits for #894, so the module docstring's rows, the policy
document, the READMEs, the ledger fragment and `changelog.md` are not
touched. The P-rows stand at their defaults, P1 (b) and P2 (a).

## What this phase found

**The frame holds for phase 1.** One function prints the clause, the six
sites `spec.md` In 1 names are its six callers, and no case in the suite
drove the unidentified branch before S1 (`grep` over `tests/` for the
function's name and both clauses found nothing).

**How S1 and S2 were shown red.** Both cases were written first and run
against the hook as it stood at `c38f97d7`, unchanged on this branch
(`git diff c38f97d7 0b52518f -- hooks` is empty): `bin/test
tests/test_worktree_guard.py -k "unidentified_sessions_line or
says_an_unidentified" -p no:xdist` gave 2 failed, each on the line
equality, because each line ended with the clause. After the edit, the same
modules gave 165 passed, 1 skipped.

**The docstring explains the removal without quoting the clause.** S2
asserts that the source holds neither clause, so the docstring paraphrases
it. A docstring that quoted it would fail S2.

**S2 checks that each site prints the entry.** It asserts the kind-and-age
line is present at each site, so a site that printed no session line at all
could not pass by printing no clause.

## What this phase removes

| Removed item | Where it must land |
|---|---|
| The clause *working on this tree right now* / *지금 이 트리에서 작업 중* at the end of `fmt_sessions`'s unidentified line | none. The header above every list already carries the judgment. `docs/worktree-guard-spec.md` §*What a blocking prompt must show* gets its sentence in phase 3 |
