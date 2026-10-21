# 1792540458-on-demand-files-state-the-current-rule — overview

## Why this work exists

The files an agent opens on demand carried history and restated rules, and the CLAUDE.md block was read twice from two copies; after this work each file states the current rule once and the block holds its rules alone, in one copy.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| what refuses a real identifier | Scope 3: "`plugin_directory_check.py` refuses only at the pull request" / the script reports the marketplace listing, and `tests/test_no_real_identifiers.py` is the check (`CONTRIBUTING.md` *House rules*) | the row stays, on the test's ground | the conclusion Scope 3 draws holds on either: nothing a smith opens before the suite states the rule |
| what the block keeps beyond Scope 2's list | Scope 2 lists the routing bullet's content / the block also says where the root lands is the user's decision, and spells the waiver `: '[no-review]';` | both kept, 1,498 bytes in all | each is an instruction rather than reasoning: the first stops a session choosing the place, the second stops a waiver typed as a pathspec (`phases/phase-3.md`) |
| the block's reason for the Bootstrap | `tests/test_first_setup_asks_once.py` pinned *opts the repository in* in the block / Scope 2: every other sentence of the bullet is reasoning and leaves | the spec | Scope 2; the reason is pinned where it lives now, *Orchestrator: Bootstrap* |
| who writes the changelog fragment | Scope 3: `skills/code-review/orchestration.md` names `changelog.md` "at the step where the orchestrator writes it" / `docs/the-record-layout.md` *A commit after the build brings its changelog fragment along*: "The build's last phase writes the fragment" | the policy | policy outranks the frame; the step names the party that builds the work item, the smith or the orchestrator under `the session` (`phases/phase-4.md`) |
| the second writer of the parity mark | `skills/legacy-parity/SKILL.md` named it "a session where it compared without one" / Scope 1 (b): a file two parties read names the party | the orchestrator | the scribe, the smith and the warden are each a session; the orchestrator is the one that compares with no review round (`phases/phase-6.md`) |
| which phase takes the rest of the update and preset-setup skills | no phase's cell in `plan.md` names `skills/update/SKILL.md` or `skills/preset-setup/SKILL.md`, and Scope 7 rewrites every skill | phase 6 takes both | the orchestrator's decision, relayed in phase 4's spawn; phase 3 had rewritten only their copy sentences |

## Not verified

| Item | Who must answer |
|---|---|
| that the rewritten files leave each agent no worse at its cases, which only the paid non-inferiority run measures; this work reads bytes, a census and a review instead (`questions.md` Q1, default (c)), and the owner can order it at the pull request | the repository owner |

## Not done

None: every file Scope 7 names has a phase.

## Fed back into the spec

None.
