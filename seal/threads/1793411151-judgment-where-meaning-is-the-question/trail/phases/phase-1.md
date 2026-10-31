# Phase 1: 1793411151-judgment-where-meaning-is-the-question

## What this phase found

**Scope item 4 is not built: the frame does not hold there.** Removing
`tests/behaviour/test_one_word_one_meaning.py` leaves three `check:` lines
under the policy root naming a file that is gone: `docs/the-broad-gate.md:33`,
`docs/the-pact.md:18` and `docs/the-pact.md:31`. `seal rules --check` refuses
each one (executed: a probe hid the file from
`.github/scripts/rules.py#unresolved` without touching the tree, and it
printed four refusals, those three and `skills/writing-style/SKILL.md:275`,
and excused none). The only excuse `rules.py` gives is a pending `remove` of
a whole section. Its docstring says a line that a pending `change` rewrites
"excuses nothing, so the test the line names stays until the settle". A pull
request does not edit the policy root (`skills/implement/SKILL.md` *Document
layout — two roots, three lifetimes*), and `frame/plan.md` A15 keeps every
`docs/` change for `## Rule changes`. `frame/design.md` has no rule change for
those three lines, and its `## Removes` does not name them. So the module
stays. The writing-style rule it holds keeps its `check:` line, because that
line names the module, and changing it alone stands on the removal. Item 4
needs a decision before any phase builds it: either three `change` items in
`## Rule changes` drop the module from those lines and the module goes at the
settle, or this pull request edits the three lines against A15. Judged
against `skills/implement/SKILL.md` *Document layout — two roots, three
lifetimes* and the module docstring of `.github/scripts/rules.py`.

The removal also reaches places `## Removes` does not name, enumerated with
`git grep -n test_one_word_one_meaning` outside `seal/threads/`. Whichever
phase removes the module owes each of them:

- `tests/text/test_a_language_section_of_writing_style_opens_alone.py#WRITING_RULE_CHECKS`
  pins the writing-style check line that names the module.
- `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py#APPLIES_THE_SHARED_GUARD`
  classifies the module's case `test_no_live_text_says_the_word_0_19_0_renamed`.
- `skills/writing-style/SKILL.md` *여럿이 가질 수 있는 것은 누구 것인지 밝힌다*
  says the module is the check on the word `seal`.
- `skills/verify/scripts/session_cost.py:63` says the module holds the
  meaning of a segment, and `hooks/lib/config.py:1414` has a comment naming it.
- Docstrings and comments in `tests/behaviour/test_a_release_is_sized_by_a_criterion.py`,
  `tests/behaviour/test_chain_hooks_hardening.py:637`,
  `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:19`
  and `tests/text/test_edits_go_through_the_edit_tool.py:19`.
- 24 entries in `.test_durations`.

**Scope item 1.** The core's script sentence is rewritten in place. Table B
stands under *Judgment is not licence to skip a party*, with the five rows in
the frame's order. The frame prints a paragraph between Table B's fourth and
fifth rows (`frame/design.md:107`), and the fifth row is read from below it.
The second row's claim was checked at its coordinate:
`chain_check.py#is_ancestor` holds each `fixed` commit to the branch
(`:1536`, `:1700`), and the last record's `target:` is HEAD or followed only
by the work item's records (read). `core.output` over the committed core,
measured as `hooks/lib/core.py#CAP` is measured, prints 8,017 characters, a
margin of 1,983 (executed, with this clone's path in the header line). The
margin is over 1,000, so the `Held by` cells keep their explanation.

**Scope item 2 is built before the readers it describes.**
`frame/design.md` *Grounding* says the writing-style sentence changes "in the
commit that changes the readers" (contract rule 19). `frame/plan.md` puts it
in phase 1, before phases 2 to 4 change those readers, and this phase builds
to the plan. Until phase 4 closes, the core and writing-style say a line spelt
otherwise is named, while `chain_check.py`, `pact_check.py`,
`rule_changes.py`, `rules.py` and `unverified_check.py` still refuse it. The
pull request ships both. The paragraph's `check:` line gains
`tests/skills/test_chain_check.py` and keeps the four modules it named, which
hold the paragraph's other two rules.

**The pin change was seen red.** The base copy of
`tests/text/test_a_language_section_of_writing_style_opens_alone.py`, run as
a `test_tmp_` probe against the new skill, failed at its check-line assertion,
and the probe was deleted (executed).

**No unit adds behaviour, so nothing was mutated.** The phase changes prose
and one pinned string; `skills/verify/SKILL.md` *The narrow command still has
to be able to fail* gives prose the tests that parse it, and those ran.

**`CONTRIBUTING.md`.** The bullet *What it reads* stands after *What it
removes*. `.github/PULL_REQUEST_TEMPLATE.md` lists some of the section's
bullets in a comment and names `CONTRIBUTING.md` as the whole of it, so it
stays as it is: one more bullet there would be a second copy.
