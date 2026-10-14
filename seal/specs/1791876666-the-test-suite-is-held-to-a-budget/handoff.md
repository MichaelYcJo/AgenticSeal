# 1791876666 — handoff

Written 2026-10-14 by the orchestrating session (Opus 5.5) at a pause the owner asked for. Delete this file when the next session has read it. `plan.md`, `overview.md` and `phases/phase-2.md` hold what was built; this file holds only what the next session does first.

## Where it stands

- Phases 1–2 are built and pushed (tip 32457021). PR #939 is open into `release/v0.22.0`, and its CI run at 32457021 was pending at the pause.
- Since 0f2b8a33 the work has added: the Windows e2e fix (CRLF), the end-to-end paths merged into one case, removal of the value `mutation_run` returned that nothing read, removal of the stale interpreter census (it flagged 3.10/3.11 constructs as above the 3.12 floor), and **one launcher, `hooks/launch.py`, holding the floor** for all 17 `bin/` wrappers and their `.cmd` twins, replacing eight `FLOOR` copies.

## Next, in order

1. **Read the CI run at 32457021.** `ledger` is expected to fail: the cuts drifted ledger rows, and they disappear with #944, so do not `--reverify`. Any other red is this branch's to fix.
2. **Wait for #944 to merge, then rebase onto it.** On rebase: drop `survivors.md` and every ledger fragment (#944 deletes survivor-check and the ledger), and resolve the `bin/` wrapper conflicts (#944 deleted some wrappers and moved `pact-check`'s path; every remaining wrapper goes through `hooks/launch.py`). Then run the narrow modules, `case_check.py`, and a warden verification round against the rebased tip.
3. **Write this item's changelog fragment** (`seal/specs/<id>/changelog.md`; there is none yet). Its user-visible changes: the 17 commands' below-floor refusal now comes from the launcher, and the Stop hook draws its stamp on a python3 below 3.12 too.
4. Sealer (Sonnet 5.5), then merge (squash).

## Decided at the pause, with the premise checked

- **`hooks/hooks.json` and the git hook stubs do not go through the launcher.** In a hook, exit 2 means "block": a below-floor launcher would deny every tool call or stop every turn. `docs/commit-review-gate-spec.md` §*Registration* requires a failing gate to step aside and say so. The smith ran the gates on 3.9 and got the same verdicts as on 3.12, so the hooks need no floor. What is not yet held by a check is that the hooks keep parsing below 3.12; `arm-check-grammar` runs only on newer interpreters.
