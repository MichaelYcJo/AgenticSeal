# Closing memo: 1793240968-every-session-reads-bootstrap-and-parity-setup

## Why this work exists

Every orchestrating session read the bootstrap and the parity setup before its first edit, though they apply only where no `seal/` root exists; the parity setup is now stated once, in `skills/parity-setup/SKILL.md`, and the bootstrap is read from its own file only when it applies.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| What the re-pointed parity assertion reads | `frame/plan.md` *Phases* row 1: "`tests/behaviour/test_chain_hooks_hardening.py:237-247` asserts that `orchestration.md` names `skills/parity-setup/SKILL.md`". The code reads the *Orchestrator: Bootstrap* section of `orchestration.md` alone | the code | The same row moves the parity grounds into the acts table's Bootstrap row, which names `skills/parity-setup/SKILL.md` too, so a whole-file needle stays green with the step 3 sentence deleted, and the row's own red-first run could not be made |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck over this branch | the orchestrator, at `seal gate --record` after the review rounds settle |

## Not done

nothing

## Fed back into the design

none
