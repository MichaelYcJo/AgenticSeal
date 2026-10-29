# Implementation Plan: 1793232075-the-living-text-still-calls-the-design-a-spec

Approved 2026-10-29 by the orchestrator under the owner's automation answer, when `crafter` was spawned.

## Summary

0.23.0 moved a work item's design from `spec.md` to `frame/design.md` and
kept the word: C1 of `frame/design.md` *The class, enumerated* finds 255
lines in 53 living files that hold `spec` or `specs` (executed at
`884b6ba8`), and most of them name the design. This work names the design
"the design" everywhere a person or an agent reads it, renames the closing
memo's template from *Overview* and the design's template from *Feature
Specification*, retitles `implement`'s step 1 and `code-review`'s first
stage, which both carried the word, and re-points two cases that the 0.23.0
move left reading an empty directory. `spec` stays only where it names
something else, and `frame/design.md` *The term* says how a reader tells
each from the design.

The work runs in three phases. The third touches #1020's files and waits
for #1020 to merge into `release/v0.24.0`.

## Technical context

- The word is read by people and agents in Markdown, and by people in five
  printed strings and one prompt (`frame/design.md` *Data & interfaces*).
  No checker reads it, except where `frame/design.md` *Occurrences kept,
  and why* names checker vocabulary that stays.
- `tests/behaviour/test_a_cited_section_stands_in_its_file.py` reads every
  citation of a section against its file's headings and bold leads. Two of
  the changed texts are cited: the heading `### 1. Read the spec before the
  code` (twelve citations, `CLAUDE.md:10` among them) and the tracer's rule
  lead *Start from the spec's coordinates* (`agents/tracer.md:57`, pinned at
  `tests/text/test_a_moved_rule_leaves_its_definition.py:555`). A heading
  and all of its citations move in one commit, or the case goes red between
  commits.
- `settle.py#GROUPS_HEADING` and `#WHOLE_HEADING` are read by
  `tests/skills/test_settle.py` through the module (`:461`, `:507`, `:781`,
  `:1495`), so their text can change without touching those cases. The
  purpose sentence at `settle.py:100` is pinned literally at
  `tests/skills/test_settle.py:1532`.
- `templates/setup/seal-README.md` and `seal/README.md` are identical
  (executed `diff`), and both are read by
  `tests/behaviour/test_the_set_a_work_item_always_has.py:172` and
  `tests/text/test_settle_reads_before_it_removes.py:195`.
- #1020's branch `fix/1020-one-kind-of-finding-recurs-across-review-rounds`
  holds only its routing commit `1d84fefe` at framing (executed `git log`),
  so its files read the same at both commits. Its build may move the lines
  phase 3 rewrites.

**The chosen approach's failure scenario, six months on.** A new sentence
in a skill calls a work item's design "the spec" again, and nothing
refuses it: no census reads the word (*Alternatives considered*, A3). The
proofer finds it at review if it re-runs C1, and otherwise a reader meets
two names for one document again, which is where #1110 started. The other
risk is the word "design" itself: it has an ordinary meaning ("by design",
"the Design Gate"), and a sentence that drops the owner, such as "the
design is wrong", reads either way. *The term* asks for the owner or the
path, and only a reader holds that.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1a. Name the design "the design", with its owner or its path (chosen) | "Design" also means an approach. A sentence without the owner can read as either, and only a reader catches it | Chosen. It is the file's own name since 0.23.0, the process archive's word ("the frame's design"), and already the living text's word where it is not "spec": `agents/sealer.md:111`, `docs/the-review-record.md:358`, `rule_changes.py:266` (read) |
| A1b. Name it "the frame" | The frame is three files, `design.md`, `plan.md` and `questions.md` (`skills/implement/SKILL.md` *Document layout*). "The frame's `## Rule changes`" would send a reader to look in `plan.md` too | Rejected: it gives one word two extents |
| A1c. Name it only by its path, `frame/design.md` | Every sentence about released designs in the plural, as in `skills/settle/SKILL.md:18-20`, has to say "released `frame/design.md` files", and the settle's printed headings grow a path where a noun did the work | Rejected for prose. The path stays where it is already written |
| A1d. Keep "spec" and rename the file back to `spec.md` | Undoes 0.23.0's recorded decision (`v0.23.1:seal/process/0.23.0.md` row 2) and every reader of the path: `hooks/lib/optin.py#DESIGN`, `chain_check.py#SPEC_FILE`, `rule_changes.py#DESIGN`, the session-start migration | Rejected: the decision is made, and the path has readers |
| A2a. Rewrite text only, and keep identifiers such as `settle.py#SPECS` (chosen) | A reader of `settle.py` meets `SPECS = "seal/threads"` beside prose that says "designs" | Chosen. `CLAUDE.md` *The rule a mechanism is kept against* names an identifier renamed across files as `no work item` work. The premise checked: no printed string spells an identifier's name (read: `settle.py:334` and `:927`, where `SETTLED` formats the value `seal/threads`, not the name) |
| A2b. Rename the identifiers too | A rename across `settle.py`, `rule_changes.py`, `chain_check.py`, `unverified_check.py` and their test modules, which import them by name, multiplies the diff and the review for no change a person sees | Rejected for this work item |
| A3a. Add no check for the word (chosen) | The failure scenario above: the word comes back and nothing refuses it | Chosen. `spec` keeps five legitimate meanings in living text (*The term*), so a census that refuses the word reads a word to guess a meaning, which `CLAUDE.md` *The rule a mechanism is kept against* calls a report and not a gate. The C1 to C6 commands are kept in the design, where a review re-runs them |
| A3b. A census refusing `\bspecs?\b` in living Markdown outside a list of kept spellings, after the pattern of `tests/censuses.py#old_names` | It is red on this branch until the settle after the release, because the policy root keeps the old words until then (`skills/implement/SKILL.md` *Document layout*), so it would need `docs/` excluded or a list kept beside the tree in step with it. It also needs an exemption for each kept meaning, and each new legitimate use, a policy file named `*-spec.md` or a quoted reference root, costs an exemption line | Rejected. Its history is one rename, and it has caught nothing yet |
| A4a. No census case for a new agent name inside a longer word (chosen) | Another substitution like #1109's `detracer` lands and nothing refuses it | Chosen. #1109 found one instance of the class, made by a shell substitution, and its search found no other (read, #1109's body). Contract rule 9 routes every edit through the `Edit` tool. The reading has a false positive at framing: `\ncrafter` in `tests/skills/test_session_cost.py:6298`, which #1109 names. This work's own risk of the same class, `spec` becoming `design` inside `specific` or `inspect`, is read by C5 at each phase's close |
| A4b. A census case refusing `[a-z]+(crafter|proofer|tracer|framer|sealer)` and the reverse | It refuses `\ncrafter` today, and every escape sequence or compound a later file writes. Each needs an exemption | Rejected: a reading guessed from words |
| A5a. Retitle step 1, and move its twelve citations, in the last phase with `CLAUDE.md` (chosen) | Phase 3 waits on #1020, so the old heading stands while phases 1 and 2 are reviewed | Chosen. The heading and every citation move in one commit, so `test_a_cited_section_stands_in_its_file.py` never sees a dangling citation |
| A5b. Retitle step 1 in phase 1 and leave `CLAUDE.md:10` dangling until phase 3 | The citation case is red from phase 1 to phase 3, and `CLAUDE.md` is #1020's to edit | Rejected |
| A5c. Keep the heading `1. Read the spec before the code` | The issue names it as an example (#1110 *Where it stands*). Under *The term*, "the spec" would read as a policy document, while the step covers the policy, the SDD set and the ticket | Rejected |
| A6a. Rename `code-review`'s first stage from "spec compliance" to "compliance" (chosen) | #1020 may reword `code-review` first, and phase 3 then rewords its new text | Chosen. The stage checks the code against the policy and the work item's SDD set (`skills/code-review/SKILL.md:22-24`), which is what step 1 calls the documents that outrank the code |
| A6b. Keep "spec compliance" | `spec` there means the policy and the design together, a sixth meaning beside *The term*'s five | Rejected |
| A7a. Keep the eval scaffolds' titles and headings (chosen) | A crafter under eval reads `# Feature Specification:` while the template says `# Design:` | Chosen. The premise that keeps them, checked: `evals/README.md` says a scaffold change "asks the agent something its runs never answered", and `regrade` refuses a suite whose scaffold differs (read) |
| A7b. Regenerate the scaffolds with `rule_cases.py` | Every recorded side of the changed cases stops comparing, and only a paid run measures the new ones | Rejected for this work item |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The prose rows of `frame/design.md` *Living occurrences this work rewrites* marked phase 1: the three record templates, `templates/setup/pact.md`, `templates/setup/seal-README.md` with `seal/README.md` kept identical, `agents/framer.md:55` and `:151`, `agents/tracer.md`, `agents/sealer.md`, `skills/implement/SKILL.md` (not `:139` and not `:421`), `skills/implement/orchestration.md:11`, `:468`, `:599`, `skills/settle/SKILL.md`, `skills/legacy-parity/SKILL.md`, `README.md` and `README.ko.md`. The pins `tests/text/test_a_moved_rule_leaves_its_definition.py:555` and `tests/behaviour/test_unverified_rows_close.py:207` move with their sentences | S2, and S8 (C5). C1 and C3 over the phase's files print only kept lines. `bin/test` over `tests/text/test_a_moved_rule_leaves_its_definition.py`, `tests/behaviour/test_unverified_rows_close.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_the_set_a_work_item_always_has.py`, `tests/text/test_settle_reads_before_it_removes.py`, `tests/behaviour/test_both_editions_carry_the_same_folds.py` and `tests/test_censuses.py`. Each moved pin seen red with its old sentence restored | |
| 2 | The code rows marked phase 2: the docstrings, comments and printed strings of `skills/settle/scripts/settle.py`, `skills/settle/scripts/rule_changes.py`, `skills/verify/scripts/unverified_check.py` and `skills/implement/scripts/seal.py`, with the pins `tests/skills/test_settle.py:1532` and `tests/skills/test_unverified_check.py:2107`. The mirror path at `skills/commit-pr-convention/SKILL.md:210`, and the two blinded cases re-pointed at `seal/threads/` | S3, S4, S5, and S8 (C5). C1, C3 and C4 over the phase's files print only kept lines. `bin/test` over `tests/skills/test_settle.py`, `tests/skills/test_rule_changes.py`, `tests/skills/test_unverified_check.py`, `tests/skills/test_seal.py`, `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` and `tests/behaviour/test_the_sealer_guarantees.py`. Each moved pin and each re-pointed case seen red as S3 to S5 say | |
| 3 | Runs after the orchestrator merges `release/v0.24.0` into this branch with #1020 in it (`questions.md` Q1). First C1 is re-run over #1020's files at the merged head and the list compared with *Living occurrences* rows marked phase 3; a line #1020 added that calls the design a spec joins the phase. Then: the step-1 heading retitled `### 1. Read the documents that outrank the code first`, with all twelve citations in the same commit; `code-review`'s first stage named "compliance" in `skills/code-review/SKILL.md`, `skills/code-review/orchestration.md:393`, `agents/proofer.md:4`, both READMEs and `hooks/review-skill-gate.py:69`; `chain_check.py:1604`, `:1612`, `:2268` with the pin `tests/skills/test_chain_check.py:1691` | S1, S6, S7, and S8 (C5). `bin/test` over `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/hooks/test_question_gate.py`, `tests/hooks/test_mode_gate.py`, `tests/text/test_the_rules_claude_md_names_have_one_home.py`, `tests/hooks/test_review_skill_gate.py`, `tests/skills/test_chain_check.py` and `tests/behaviour/test_chain_hooks_hardening.py`. The refusal pin seen red with its old text restored | |

## Operational impact

No migration, environment variable, dependency or compatibility break. A
work item framed before this change keeps the title `# Feature
Specification:`, because a record keeps the words it was written under. A
repository that installed an earlier release keeps its `seal/README.md`
sentence until its root's README is rewritten from the template; no checker
reads that sentence. The `docs/` wording lands at the settle after 0.24.0,
from `frame/design.md` *Rule changes*.
