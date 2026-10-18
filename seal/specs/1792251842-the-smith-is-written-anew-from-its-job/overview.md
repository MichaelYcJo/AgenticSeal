# 1792251842-the-smith-is-written-anew-from-its-job — overview

<!-- The closing memo (implement skill, step 4). Not a summary of the work:
`git diff --stat` holds the file list and the diff holds the detail. Only what
the diff cannot show goes here, and each part is written when it happens rather
than reconstructed at the end. A rule that must outlive this work item goes
to its home under `docs/` with the test that holds it, not here. -->

## Why this work exists

The smith's definition is written to the warden's shape and preloads the
contract alone, and the proof block leaves every file an agent reads, so a
smith spawn pays for one page and hands its claims back under three labels.

## Where spec and implementation diverged

Opened at phase 2, where the first removals the frame's `## Removes` did not
name were made. Each row is one; `phases/phase-2.md` §*The pins* has the
case-by-case table.

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| `skills/verify/SKILL.md`'s seal section retitled | `## Removes` names the section's coordinate and says it is rewritten to the fact; it does not say the heading changes. The heading is now *The hand-back's labels carry the claims, and the one seal is the sealer's* | the retitle, with `agents/sealer.md:28-30` and `docs/one-root-by-lifetime.md:136-138`, which link to it by title, re-pointed in the same commit | the old title, *Every agent seals what it verified*, states the fact the work removes; CLAUDE.md §*subtract before you add*: a change "removes what stood on the old fact" |
| Pins on smith sentences the frame did not list | `## Removes` names five narration pins in the smith; phase 2 removed eight more assertions or allowances on smith text that left: `test_a_citation_is_not_a_copy`'s waiver phrases, `test_the_release_target_is_asked_before_the_work_starts`'s smith half, `test_the_ladder_does_not_still_say_at_the_end`'s smith half, `test_the_start_is_the_moment_before_the_first_edit`'s smith entry, `test_every_link_names_the_owner`'s two smith links (rules 14 and 15), the smith's `KNOWN_PROSE` allowance, `RELEASE_BRANCH_HISTORY`'s smith entry | removed, one line each in the phase record | each pinned a sentence `## Removes` already sends away (the design-gate narration, the ladder's copy, the RIDER block); the frame named the class and five of its members, and the rest were found by running the pins |
| Pins on the proof block the frame did not list | `## Removes` names two cases in `tests/test_broad_gate_rule.py` and two lines of `tests/test_one_word_one_meaning.py`; phase 2 also removed the second half of `test_the_broad_gate_state_survives_a_handoff` and the two `SEAL_BARE_IS_THE_CONCEPT` allowances for the seal block and its `cost` row | removed | each read the `## Seal block` section, which `## Removes` names |
| `(§3)` written into the smith's hand-back step | §*The shape this item gives each file* lists the hand-back's contents and cites no section; `test_the_smith_puts_both_answers_in_the_hand_back` asks for `§2` and `§3` | the citation added, five bytes | a citation of the rule the declined-instruction line answers, not a new rule; the pin stays as strong as it was |
| Two `Enforced by:` lines re-pointed to T6 (phase 3) | `## Removes` names the case T6 replaces and not its citers; `docs/the-review-record.md:19` and `skills/code-review/SKILL.md:132` cited it | both name T6 | `bin/rules --check` exit 1 on both once the case left; T6 reads every file the old case read |
| The audit block's per-violation line (phase 3) | Q3's default: the words `passed`, `warnings`, `violations` at the start of each line; the fourth line is one violation, not a count | `violation:` there, the three words on the three count lines | the line describes one finding, and the singular is the same word |
| T6 refuses a stale skip entry (phase 3) | the spec's skip map leaves with #970 and says nothing about a skip that outlives its marks | the case fails when the skipped file has no mark left | a skip with nothing to skip is the next session's hole in the corpus, and #970's repair then has to remove it in the same commit |

## Not verified

| Item | Who must answer |
|---|---|
| `CLAUDE.md:69` still names *a seal block* as a format name, and decision 1's grep finds it | the repository owner: a subagent does not edit `CLAUDE.md` |
| closed `skills/writing-style/SKILL.md:225` still lists *the smith's seal* as an instance | a6a0c692, phase 3, 2026-10-18: the row now reads *the sealer's seal · the warden's review mark · the smith's labels* |
| `agents/sealer.md` and `skills/verify/SKILL.md` are edited here and by #969 in its own worktree | the orchestrator, when the two branches meet |
| the full suite on this branch | the orchestrator |

## Not done

Phase 5 closes this memo.

## Fed back into the spec

none
