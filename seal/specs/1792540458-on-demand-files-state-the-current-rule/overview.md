# 1792540458-on-demand-files-state-the-current-rule — overview

## Why this work exists

The files an agent opens on demand carried history and restated rules, and the CLAUDE.md block was read twice from two copies; after this work each file states the current rule once and the block holds its rules alone, in one copy.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| what refuses a real identifier | Scope 3: "`plugin_directory_check.py` refuses only at the pull request" / the script reports the marketplace listing, and `tests/test_no_real_identifiers.py` is the check (`CONTRIBUTING.md` *House rules*) | the row stays, on the test's ground | the conclusion Scope 3 draws holds on either: nothing a smith opens before the suite states the rule |
| what the block keeps beyond Scope 2's list | Scope 2 lists the routing bullet's content / the block also says where the root lands is the user's decision, and spells the waiver `: '[no-review]';` | both kept, 1,498 bytes in all | each is an instruction rather than reasoning: the first stops a session choosing the place, the second stops a waiver typed as a pathspec (`phases/phase-3.md`) |
| the block's reason for the Bootstrap | `tests/test_first_setup_asks_once.py` pinned *opts the repository in* in the block / Scope 2: every other sentence of the bullet is reasoning and leaves | the spec | Scope 2; the reason is pinned where it lives now, *Orchestrator: Bootstrap* |

## Not verified

| Item | Who must answer |
|---|---|
| that the rewritten files leave each agent no worse at its cases, which only the paid non-inferiority run measures; this work reads bytes, a census and a review instead (`questions.md` Q1, default (c)), and the owner can order it at the pull request | the repository owner |

## Not done

`skills/update/SKILL.md` and `skills/preset-setup/SKILL.md` had their copy
sentences and the anecdotes beside them rewritten in phase 3, and no more:
Scope 7 rewrites every skill, and no phase's cell in `plan.md` names these
two. Whether phase 6 takes the rest of their prose is the orchestrator's to
decide.

## Fed back into the spec

None.
