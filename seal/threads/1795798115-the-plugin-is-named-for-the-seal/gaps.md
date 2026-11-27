# Closing memo: 1795798115-the-plugin-is-named-for-the-seal

## Not verified

| Item | Who must answer |
|---|---|
| The broad gate over phase 1's commits: the full suite, the repository-wide lint and the format check of `seal/config.json`'s `Broad gate` key. The crafter ran the phase-boundary set and linted the files it changed | the orchestrator, at the broad run |
| The broad gate over phase 2's commits. The crafter ran the phase-boundary set and linted and formatted the Python files it changed | the orchestrator, at the broad run |
| Whether the five eval cases under `evals/behaviour/inspector/` reach their graders in a model session. Each case spawns `agentic:inspector`, which no installed release defines, and no paid run was made | the repository owner, at the next run of `evals/scripts/noninferiority.py` over those cases |

## Not done

Phase 1 left two readers that still compute the root's name, though the name is now always `lib/optin.py#HOME`: `skills/implement/scripts/seal.py#display`, called with the shared place, and `skills/settle/scripts/settle.py#threads`, which reads the basename of the root it is given. Both read a path they are handed and fall back to nothing for a second name, so neither stands on the removed fact.

Phase 2 changed the word of the messages that name the final party, and added no case that pins the new word where none pinned the old one. The messages without such a case are in `skills/code-review/scripts/chain_check.py`, such as *the inspector's verdict reads* and *the inspector writes it from*, and in the help lines of `skills/verify/scripts/seal_stamp.py`, `skills/verify/scripts/broad_gate.py` and `skills/implement/scripts/seal.py`. Contract rule 14 asks a change to a message to pin it. The phase did not add one case per message because the change is a rename that the frame proves by search A1 (`frame/design.md` *User scenarios & acceptance*, row *The party's old name is gone*), and the design adds no check (`frame/design.md` *Removes*, its last paragraph). A1 shows the old word gone, and it does not show which word took its place. The two messages that already had a case were shown red with the old word put back, as `trail/phases/phase-2.md` states.
