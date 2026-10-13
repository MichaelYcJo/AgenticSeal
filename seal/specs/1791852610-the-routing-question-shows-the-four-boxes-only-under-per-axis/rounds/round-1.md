# 1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis — review round 1

| Field | Value |
|---|---|
| Target SHA | bb9eed9b1e1549650cd49656c06c75903fe93db1 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #917 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are written and no round has opened them |
| Fix range | `ab8212989a29f53006eb015da54ecf876baeda26..4d55d7a50795af1978f8de426fd4c0425f8b621e`, 2 commits |
| Contract changes | none |
| New units | boxes_alone (depth 1); test_the_boxes_asked_alone_neither_give_nor_take_back_the_press (depth 1) |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1 (the §1 citation in the routing section), 🟡 2 (the batching test still pinning the retired one-call rule), 🟡 3 (five for six) |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Round 1 of #911, target bb9eed9b against `origin/release/v0.21.1` at 321e9de1, over the whole build, phases 1–3. The reviewer was asked to judge the smith's divergences in `overview.md` — the shared sentence cut to 14 words under the pasted-passage check, the heading cut to fit the 88-column wrap, five `Corrected ·` and 22 `Re-read ·` rows for the heading move, the renamed S1 case, `agents/smith.md`'s case moved onto the shared STALE tuple — to check that every live copy of the retired one-call rule is gone or rewritten, and that `hooks/worktree_consent.py#_routing_preset` is byte-identical to the base.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | The routing section says the batch rule forbids only a late question and not a second click, citing §1; §1 says each interruption is a wait | `skills/implement/orchestration.md:270` | **fixed** `44e0d652` | fixed at 44e0d652; `skills/implement/SKILL.md:205-206` says *three interruptions cost three waits*; the trade is the owner's from #911 (Q1), not §1's |
| 🟡 2 | A batching test still pins the retired one-call rule in its message and comment, and its `in one call` assertion is satisfied by a sentence meaning the reverse | `tests/test_chain_hooks_hardening.py:1275` | **fixed** `44e0d652` | fixed at 44e0d652; Message: *the questions go in one call, which is what makes the batch one wait*; comment at :1298 says `agents/framer.md` uses `in one call`, which it no longer does; contract §12 |
| 🟡 3 | The ceiling sentence the build carried into its paragraph counts two presets beside four boxes as five | `skills/implement/orchestration.md:274` | **fixed** `44e0d652` | fixed at 44e0d652; Two presets (`automation`, `no work item`) plus four boxes is six; wrong since #88 (`865a9807`), reflowed by this build |
| ⬜ 4 | The resume paragraph puts question 1 in the same call as other questions, while the new opening says it goes in a call of its own | `skills/implement/orchestration.md:301` | open | Behaviour right (the reader takes both, and a resume asks no boxes); the two sentences need a word saying which moment each governs |
| ⬜ 5 | A reflow left `Nothing that` on a line of its own | `docs/worktree-guard-spec.md:981` | open | Cosmetic; rejoin with the next line |
| ⬜ 6 | `overview.md` reports the approval line and the `Ran by` rows as unfilled; `bb9eed9b` filled both | `seal/specs/1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis/overview.md` | open | `plan.md:7` and `phases/phase-1.md:7`, `phase-2.md:7`, `phase-3.md:7` at the target; a record correction, outside `Needs a fix` |
| 🟢 | The press reader is byte-identical to the base | `hooks/worktree_consent.py#_routing_preset` | confirmed | Executed: `git diff --quiet` on `hooks/` exit 0, blob `079cbb10` at both ends |
| 🟢 | Every live copy of the retired *two questions in ONE call* sentence is gone or rewritten | `skills/implement/orchestration.md`, `templates/claude-md-block.md`, `CLAUDE.md`, `skills/implement/SKILL.md`, `agents/framer.md` | confirmed | Executed `git grep` sweep at the target; what remains is out of scope by the spec, or is 🟡 1 and 🟡 2 |
| 🟢 | The smith's six divergences hold on their grounds: the 14-word sentence, the 87-column heading, five `Corrected ·` and 22 `Re-read ·` rows, the renamed S1 case, `agents/smith.md` on STALE, the Removes sub-heading | `seal/specs/1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis/overview.md` | confirmed | Each `Corrected ·` row compared coordinate by coordinate with the released row it replaces; the refusing checks named exist at the cited names |
| ❓ | That the harness shows question 1 alone with no boxes, and that a session following the new block puts the second call only after `per axis` | `templates/claude-md-block.md:16` | ❓ out of verified scope | No session was run against the block; the orchestrator answers it at the next routing question it puts from a block carrying this change |

## Paste-ready fixes

```markdown
Under `per axis` the second call follows the first at once, before the first
edit. That is a second wait, and it is the trade #911 took: the boxes depend
on question 1's answer, so putting them beside it shows them under the two
answers they mean nothing for. Asked at once and before the first edit, the
second wait still costs a reply rather than a stopped session, which is how
`skills/implement/SKILL.md` §1 prices a question. `AskUserQuestion` allows at
most four options per question, and two presets beside the four boxes is six
— so the shape below is two questions rather than one, and that is what
makes both fit.
```
```python
    assert "Question 1 goes in one call of its own" in " ".join(
        orchestration.split()
    ), (
        "the orchestrator's routing section no longer says question 1 is put "
        "in a call of its own before the first edit, with the boxes after it "
        "only under `per axis` (#911)"
    )
```
```python
    # The second is true and a definition may need to say it — `agents/
    # framer.md` does, in its diagram's first line (*asks question 1; boxes
    # only if per axis*), which stays clear of this. A definition that needs
    # the other wording will
```

## Executed probes

| What was run | Result |
|---|---|
| `git diff --quiet 321e9de1 bb9eed9b -- hooks/`; `git rev-parse` of `hooks/worktree_consent.py` at both ends | exit 0; `079cbb10` at both |
| `git grep` at `bb9eed9b` for the retired phrasings and the old headings, outside released records and earlier work items | every hit read; the stale ones are 🟡 1 and 🟡 2 |
| One-file test_tmp probe in the clone's `tests/`: `per axis` then a boxes-only call (all, first, none ticked), and an earlier press taken back by `per axis` and its boxes call; run once with `bin/test … -q -p no:xdist`, then deleted | exit 0, 2 passed |
| `SPECSEAL_CASE_CEILING_S=600 bin/test tests/test_first_setup_asks_once.py tests/test_a_signer_declares_its_pact.py tests/test_one_word_one_meaning.py tests/test_a_section_marked_for_one_role_reaches_only_that_role.py -q` in the clone at `bb9eed9b` | exit 0, 2732 passed |
| Broad gate: the full suite, the repository-wide lint and the typecheck | not yet. Not run by this round; it is the sealer's, once the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
