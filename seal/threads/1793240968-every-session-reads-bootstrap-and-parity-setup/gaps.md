# Closing memo: 1793240968-every-session-reads-bootstrap-and-parity-setup

## Why this work exists

Every orchestrating session read the bootstrap and the parity setup before its first edit, though they apply only where no `seal/` root exists; the parity setup is now stated once, in `skills/parity-setup/SKILL.md`, and the bootstrap is read from its own file only when it applies.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| What the re-pointed parity assertion reads | `frame/plan.md` *Phases* row 1: "`tests/behaviour/test_chain_hooks_hardening.py:237-247` asserts that `orchestration.md` names `skills/parity-setup/SKILL.md`". The code reads the *Orchestrator: Bootstrap* section of `orchestration.md` alone | the code | The same row moves the parity grounds into the acts table's Bootstrap row, which names `skills/parity-setup/SKILL.md` too, so a whole-file needle stays green with the step 3 sentence deleted, and the row's own red-first run could not be made |
| Two docstrings the frame lists for a change | `frame/design.md` *Data & interfaces* lists `tests/behaviour/test_first_setup_asks_once.py:175` among the comments "that state where the bootstrap or the parity rule is now", and `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py:284` among the docstrings where "both" becomes what the tuple holds. The code leaves both | the code | `:175` says the slice of a round finding ran to "the end of the whole Bootstrap section" and names no file. `:284` is `_tree`'s docstring, "A root with both orchestration files", and the planted root still holds exactly those two: it carries no bootstrap file, and `acts` skips a path that does not resolve |

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the typecheck over this branch | executed by the orchestrator's broad gate at `79d1369c` against `1e82fd0a`, passed (`trail/gate.md`), and this repository declares no typecheck (`seal/config.md` *Broad gate*; #951 would add one) |

## Not done

nothing

## Fed back into the design

none
