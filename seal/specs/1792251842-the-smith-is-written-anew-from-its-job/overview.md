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
name were made, and closed at phase 5. Each row is one; the phase records
named in each row hold the detail.

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Phase 1 taken twice (phase 1) | `plan.md` row 1 runs each agent's baseline once, and stops before the next agent past $75 | the smith's side stands from the first attempt; the warden's and the framer's were taken again with the lid open, and the first attempt's 38.3854 USD bought no result | the host slept with the lid closed from 01:21 KST (`pmset -g log`, `phases/phase-1.md`); 15 of the warden's 18 runs timed out and the framer's side was stopped after 58 s. A cut-short side is no result, and the cause was the host, not an agent. The $75 stop was read as a bound on the sides that stand (65.7598), and the phase spent 104.1452 in all |
| Phase 2 taken in two parts, a and b (phase 2) | `plan.md` row 2 is one phase whose pin list comes from `git grep "smith\|implement/SKILL"` (18 modules) | part a wrote `agents/smith.md` and `skills/implement/SKILL.md` (e61ac4e1); part b made the tree agree with them (aea8c8e5) | the frame's list was a floor: no grep it or the spawn named matches a module that opens the file as `flat("agents", "smith.md")`, which is how `tests/test_broad_gate_rule.py` and `tests/test_a_probe_does_not_outlive_its_round.py` read it, and each held a pin part a had broken. The grep that finds them named 69 modules, then 68 (`phases/phase-2.md`) |
| `skills/verify/SKILL.md`'s seal section retitled | `## Removes` names the section's coordinate and says it is rewritten to the fact; it does not say the heading changes. The heading is now *The hand-back's labels carry the claims, and the one seal is the sealer's* | the retitle, with `agents/sealer.md:28-30` and `docs/one-root-by-lifetime.md:136-138`, which link to it by title, re-pointed in the same commit | the old title, *Every agent seals what it verified*, states the fact the work removes; CLAUDE.md §*subtract before you add*: a change "removes what stood on the old fact" |
| Pins on smith sentences the frame did not list | `## Removes` names five narration pins in the smith; phase 2 removed eight more assertions or allowances on smith text that left: `test_a_citation_is_not_a_copy`'s waiver phrases, `test_the_release_target_is_asked_before_the_work_starts`'s smith half, `test_the_ladder_does_not_still_say_at_the_end`'s smith half, `test_the_start_is_the_moment_before_the_first_edit`'s smith entry, `test_every_link_names_the_owner`'s two smith links (rules 14 and 15), the smith's `KNOWN_PROSE` allowance, `RELEASE_BRANCH_HISTORY`'s smith entry | removed, one line each in the phase record | each pinned a sentence `## Removes` already sends away (the design-gate narration, the ladder's copy, the RIDER block); the frame named the class and five of its members, and the rest were found by running the pins |
| Pins on the proof block the frame did not list | `## Removes` names two cases in `tests/test_broad_gate_rule.py` and two lines of `tests/test_one_word_one_meaning.py`; phase 2 also removed the second half of `test_the_broad_gate_state_survives_a_handoff` and the two `SEAL_BARE_IS_THE_CONCEPT` allowances for the seal block and its `cost` row | removed | each read the `## Seal block` section, which `## Removes` names |
| `(§3)` written into the smith's hand-back step | §*The shape this item gives each file* lists the hand-back's contents and cites no section; `test_the_smith_puts_both_answers_in_the_hand_back` asks for `§2` and `§3` | the citation added, five bytes | a citation of the rule the declined-instruction line answers, not a new rule; the pin stays as strong as it was |
| Two `Enforced by:` lines re-pointed to T6 (phase 3) | `## Removes` names the case T6 replaces and not its citers; `docs/the-review-record.md:19` and `skills/code-review/SKILL.md:132` cited it | both name T6 | `bin/rules --check` exit 1 on both once the case left; T6 reads every file the old case read |
| The audit block's per-violation line (phase 3) | Q3's default: the words `passed`, `warnings`, `violations` at the start of each line; the fourth line is one violation, not a count | `violation:` there, the three words on the three count lines | the line describes one finding, and the singular is the same word |
| T6 refuses a stale skip entry (phase 3) | the spec's skip map leaves with #970 and says nothing about a skip that outlives its marks | the case fails when the skipped file has no mark left | a skip with nothing to skip is the next session's hole in the corpus, and #970's repair then has to remove it in the same commit |
| Phase 4 taken twice, the second on the merged tree (phase 4) | `plan.md` row 4 runs the three agents once at phase 3's commit, against phase 1's baselines | the first take at 7053c184 (records 668fd5f4, a3bf3832) is history; the record is the second take at af716289, this branch with `release/v0.22.1` merged in at 16e8d4c8 plus two test fixes no agent reads; the baselines stay phase 1's at 2fc33333 by the orchestrator's decision (2026-10-18) | #969 merged into `release/v0.22.1` (4a6e24f6) before the framer's re-run was taken, changing contract §2, which all three agents preload, one sentence of `agents/warden.md`, and `docs/the-review-record.md`, `skills/code-review/scripts/chain_check.py` and `agents/sealer.md`, which the warden reads in the evaluated tree; an agent whose read set changed is measured again. Re-taking the baselines would have cost about $60, so the comparison includes #969's changes named here as well as this item's (`phases/phase-4.md`) |
| Two conflicts in the merge of `release/v0.22.1` (16e8d4c8) | the plan names no merge; `agents/sealer.md:23-35` and `tests/test_the_seal_is_taken_once_by_the_sealer.py#test_the_unmeasured_word_says_so_and_every_reader_is_told_it` were edited on both sides | `agents/sealer.md` keeps #969's sentence (the last seal is "the one over the whole work", and `broad-gate.md` is the orchestrator's run's) with this item's section title; the test keeps #969's reader of `skills/code-review/orchestration.md` and drops the sealer reader, with this item's smith phrase `` `new?` means nothing at the base measured that file `` | each side's fact stands where it is the owner: #969 owns who runs the gate and what the sealer reads, this item owns the verify section's title and the smith's sentence (`git show --remerge-diff 16e8d4c8`) |
| T5's walk of tracked files given `on_disk` (09d49365) | phase 2 planted `tests/test_the_set_a_work_item_always_has.py#cited_files` as a `git ls-files` walk that skips a missing file by `os.path.isfile` | the walk applies `conftest.on_disk`, and `tests/test_a_shrunken_corpus_declines_to_judge.py#APPLIES_THE_SHARED_GUARD` lists it beside the other positive sweeps | that guard, in the tree since af9c924b, requires every positive sweep to apply the shared predicate; the suite on the merged tree found T5's walk unguarded |
| `evals/scripts/behaviour.py#write_case` writes LF (af716289) | outside the plan; the defect came in with #969 through the merge | each file is opened with `newline="\n"` | the committed cases are LF (`.gitattributes`) and are compared byte for byte with the generator's output, so on Windows the platform newline made them differ: `windows-latest` group 1 went red at #973's head (run 39094763103, `c2ba7035`); this branch's dispatched run 39095623463 at af716289 is green on every job |
| Q1's spend stop passed (phase 4's second take) | `questions.md` Q1: this item stops before the next agent once its summed spend passes $150 | phase 1 spent 104.1452 and phase 4's first take 60.5128, so the item stood at 164.6580 before the second take, which spent 63.2295 more and brought it to 227.8875; the smith's third take in the row below brings it to 233.3384 | the owner, asked on 2026-10-18 whether to spend about $60 past the night's $200, answered "decide and go with your recommendation", and the orchestrator took the second take; the `## Not verified` row below is closed with that answer |
| The smith's side taken a third time, after round 1 (phase 4) | `plan.md` row 4 runs an agent's set a second time only for a `fail` its own sentence caused, and no third run; `questions.md` Q1 stops this item before the next agent once its spend passes $150 | the side at 28d6a453 (committed at 2c7716bd) is the smith's record in `evals/smith-phase-4.json` and `.md`; the af716289 side is history | the take was the orchestrator's: round 1's fixes changed `agents/smith.md` at a72d5b53 after that side was measured, and an agent whose read set changed is measured again (`phases/phase-4.md`), so the record measures the text that ships. It spent 5.4509 with the item at 227.8875, so the item's evaluation total is 233.3384 (phase 1 104.1452, phase 4 129.1932). The owner's answer of 2026-10-18, "decide and go with your recommendation", was given to the orchestrator's recommendation to re-measure on the merged tree, and the orchestrator applied the same delegation to this take; the tree records no separate answer for it |

## Not verified

| Item | Who must answer |
|---|---|
| `CLAUDE.md:69` still names *a seal block* as a format name, and decision 1's grep finds it | the repository owner: a subagent does not edit `CLAUDE.md` |
| closed `skills/writing-style/SKILL.md:225` still lists *the smith's seal* as an instance | a6a0c692, phase 3, 2026-10-18: the row now reads *the sealer's seal · the warden's review mark · the smith's labels* |
| closed `agents/sealer.md` and `skills/verify/SKILL.md` are edited here and by #969 in its own worktree | the merge 16e8d4c8, 2026-10-18: `agents/sealer.md` conflicted and keeps #969's sentence with this item's section title; `skills/verify/SKILL.md` merged without a conflict (row above) |
| the full suite on this branch | the orchestrator's broad gate, still to run; CI's run 39095623463 at af716289 passed every pytest job on three platforms, which is not that gate |
| closed `windows-latest` on the merged tree | run 39095623463, dispatched on this branch at af716289: every job `success`, read with `gh run view` in phase 5 |
| closed The second take of phase 4 was run past `questions.md` Q1's $150 stop for this item | the owner: asked on 2026-10-18 whether to spend about $60 past the night's $200 for the three agents' second take, the owner answered "decide and go with your recommendation", and the orchestrator took it (63.2295 USD; `phases/phase-4.md`) |

## Not done

The framer's `fail` on rule 5 (+9.5% tokens per tool call, every grader
passing) goes to #968, which rewrites `agents/framer.md` (decision 5) and
measures the framer on a tree carrying this item. The framer preloads
`implement` and `writing-style`, so all eight runs read both; its total
tokens fell 0.5% and its tool calls fell 11, so the rise is fewer calls on
a smaller read, and no sentence of this item's files is identified as the
cause. The warden's
`fail` on rule 5 (+0.8%) is recorded as it reads and not rerun: the same
`writing-style` text gave 6.0% below the baseline in the first take, and
two takes 6.8 points apart is the spread #966 holds.
`skills/legacy-parity/SKILL.md`'s four emoji are #970's, and T6 skips the
file by name until then. `.test_durations` still names five cases this item
removed or replaced (`:1957`, `:1958`, `:5897`, `:6583`, `:6644`); CI
rewrites that file. The white square in 72 lines of 35 files
outside T6's corpus is code comments and eval prompts quoting past rounds,
and it stays.

## Fed back into the spec

none — the answered questions are measurements and sorting work, and none of
them states a rule a `docs/` policy would carry.
