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
| what each agent opens is not larger | S13: the bytes of each agent's set are no larger at phase 9's commit than at b3154f43 / the framer's set is 2,041 bytes over and the warden's 2,419 (`phases/phase-9.md`) | shipped over, and reported | both sets open `skills/writing-style/SKILL.md`, where Scope 1 put the three writing rules (3,447 bytes); the files phases 7 and 9 could shorten in those sets gave back less without cutting a rule. Closing the gap is a choice between trimming `templates/config.md`'s rule 3 and the cmd.exe paragraph, which are rules, or the writing section, which the owner asked for |
| the heading of section 6 | Scope 9: "`skills/implement/SKILL.md` *6. Close before merge* names its moment and its party" / the heading named the merge as the moment | renamed to *6. Drain the rows before the sealer is spawned, and keep the records* | a heading naming the merge would contradict the moment the section now states; nothing cites the old heading (`phases/phase-9.md`) |
| D7's party | Scope 9: "the orchestrator, or the session where `routing.md` answers `Implementation` with `the session`" / under that answer the session is the orchestrator | one name, the orchestrator, "whichever party `routing.md`'s `Implementation` row names" | Scope 1 (b): one word, one meaning; "the session" there would be a second name for the orchestrator |

## Not verified

| Item | Who must answer |
|---|---|
| that the rewritten files leave each agent no worse at its cases, which only the paid non-inferiority run measures; this work reads bytes, a census and a review instead (`questions.md` Q1, default (c)), and the owner can order it at the pull request | the repository owner |
| the full suite, the repository-wide lint and the typecheck over the branch; each phase ran its own module set and the meta modules only | the orchestrator |

## Not done

Every file Scope 7 names has a phase. Left for the later item Scope 8 names
(#1005): the section signs in `agents/*.md`, in the `.py` files and in the
contract's numbering, among them `broad_gate.py`'s refusal message, which
still cites `templates/config.md` with a section sign under the renamed
heading, and the line `skills/verify/orchestration.md:258` calls "A §6
line", the label `session_cost.py` prints; and `agents/sealer.md:56`, which
cites a bold sentence of `docs/the-review-record.md` as a heading. The test
fixtures and the eval scaffolds that write a record keep the record title
with a dash; no reader reads a title, and the templates' new `Kind: id`
title is what a session copies.

## Fed back into the spec

None.
