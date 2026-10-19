# Implementation Plan: the framer is written anew from its job (#968)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-19 by the orchestrator, under the owner's `automation` answer and Q1/Q2's answers, when `smith` was spawned for phase 1; phase 2 is scheduled after #976 and #985 merge.

## Summary

`agents/framer.md` is rewritten to the shape the warden and the smith
already have, preloads the contract alone, and opens three sections of
`implement` and one of `writing-style` at the steps that need them. Its pins
are sorted into rules re-pointed and narration removed. One paid side is
compared with #967's last framer side, which guard 1 keeps as the baseline
because the framer's read set has not changed since it was measured
(`spec.md` §*The baseline, decided by guard 1*).

## Technical context

- **The file today** (`read`): `agents/framer.md`, 367 lines, 19,545 bytes,
  eleven `##` sections and no `Enforced by:` line. The rules it holds are
  pinned by phrase across about a dozen test modules, found with
  `git grep -n -E "framer\.md|FRAMER" tests/`. The main ones:
  `tests/test_waiver_decided_at_start.py:588-770`,
  `tests/test_the_handoff_before_round_one.py:196-275`,
  `tests/test_a_question_says_who_can_answer_it.py:125-200`,
  `tests/test_a_phase_hands_the_next_one_a_record.py:192`,
  `tests/test_the_rules_have_one_owner.py:32, 135, 334, 382`,
  `tests/test_chain_hooks_hardening.py:1379-1395`,
  `tests/test_a_reference_root_is_read_and_never_taken.py:338`,
  `tests/test_every_agent_reads_the_contract.py:35`,
  `tests/test_no_passage_is_pasted_into_a_second_file.py:205-228`,
  `tests/test_one_word_one_meaning.py:203`, `tests/test_docs_line_wrap.py:151`.
- **The shape to copy** (`read`): `agents/smith.md` (172 lines, 10,276 bytes)
  and `agents/warden.md` (10,570 bytes). Both carry the same opening sentence,
  the same *every `skills/`, `templates/` and `docs/` path is the plugin's*
  sentence in step 1, a `## Never` of one line each, and `## Rules`
  paragraphs ending in `Enforced by:`.
- **The sections the framer opens** (`executed`, `grep -n`):
  `skills/implement/SKILL.md` `## The language the records are written in`
  (:33), `### 1. Read the spec before the code` (:135), `### 3. The SDD file
  set` (:294); `skills/writing-style/SKILL.md` `## English prose rules`
  (:278, 2,522 bytes) and `## 문장 규칙` (:43).
- **The measurement** (`read`): `evals/behaviour/framer/` holds four cases of
  eight graders, two runs each, on `claude-fable-5-1`, 12 turns, 1,200 s. The
  suite is af9c924b's for every side. The four recorded framer sides cost
  $16.5896 (#957 baseline), $17.3532 (#957 phase 3), $16.9055 (#967
  baseline) and $16.1196 (#967 phase 4).

**What breaks in six months.** A heading the framer reads by name is
renamed in `implement` or `writing-style`, and the framer's section read
finds nothing. The step therefore says to read the file whole where the
heading is not found, so a rename costs bytes and not the rule. S2 checks
the path and cannot see a heading, which is why the fallback is in the
sentence and not in a check.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. The shape, `skills: [agent-contract]`, `implement` read as three sections at the ladder step and `writing-style` as one section before the writing | a renamed heading; the fallback above reads the file whole | **chosen** |
| B. The shape, but `implement` and `writing-style` stay in `skills:` (keep the structure) | the per-request context stays within about 10 KB of the baseline that failed rule 5 twice; the shape case (S1) refuses the list; #957's shape forbids it | rejected |
| C. The shape, both skills opened whole, as the smith does | after both opens each request carries only the definition's saving, about 10 KB; the smith's precedent (−16.4% per call) had a larger preload share to lose than the framer keeps after the opens | rejected for A; A falls back to C where a heading is missing |
| D. Replace the agent: `Planning` answered `the session`, and the orchestrator draws every frame (the alternative that removes the structure) | the frame is drawn in the one context a release cannot replace mid-run (`templates/sdd-routing.md`'s `Implementation` comment), and the anchor argument holds only where the writer of the frame does not build. #968 asks for the framer rewritten, and #957 keeps the agent | rejected; outside the issue |
| E. A fresh baseline side at 43cbc361, as the issue expected | about $17 to learn what the four sha256 values already say; guard 1 reuses a measurement whose read set did not change | rejected; Q2 holds the file-granularity reading |
| F. A `shape-` grader for the replace-or-keep rule in the four framer cases | the suite is fixed at af9c924b, so no side of this milestone runs it, and `compare` refuses a side on another suite | rejected; a test pin holds the sentence, Q5 holds the grader |
| G. Drop the per-call bound and the skeleton from the opening, leaving contract §10 | batching is the half of rule 5 the rewrite does not control, and #967's `fail` came from it; removing the instruction that governs it invites that cause | rejected; the opening stays as rules, its readings leave |
| H. Edit `implement`'s *Opened by the `smith` agent* to name the framer | the sentence is not false; any edit to `implement` changes the smith's read set, and guard 1 re-measures the smith (about $5.45) | rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **The rewrite.** `agents/framer.md` written to `spec.md` §*Data & interfaces*. The framer's `NOT_YET_REWRITTEN` entry deleted and the docstring's *#968 to #970* corrected; the case seen red on the old file first. The pins sorted per Q3: each on a rule re-pointed to the new sentence, each on narration removed with one line in `phases/phase-1.md`. One new case for the replace-or-keep rule (S6), seen red on the old file. The allowances in `tests/test_no_passage_is_pasted_into_a_second_file.py` re-measured. `README.md:38` and `README.ko.md:37` rewritten in place. The phase record names the read set's sha256 at 43cbc361 against the baseline side's (`spec.md` §*The baseline*), `payload-meter --agent framer` before and after, and the `git grep` of each removed phrase | `bin/test` over every module the sort touched exit 0; `bin/rules --check` exit 0; `payload-meter --agent framer` below 86,353 bytes (rule 4); the greps finding nothing outside `seal/specs/` and `changelog/` | 2cb43374 |
| 2 | **The evaluation. Paid, about $17; the orchestrator schedules it.** `evals/baseline-framer.json` as a byte copy of #967's `evals/framer-phase-4.json` (`cmp` exit 0). One side at phase 1's commit with `--suite-rev af9c924b --runs 2 -j 4 --max-cost-usd 25`; the raw output kept outside the tree at a path the record names; `evals/framer-phase-2.json` by `--from-raw` and `evals/framer-phase-2.md` by `compare --phase 2`. The phase record holds, per run from the traces, the framer's requests, tool calls, tools per request, tokens per request, and the request and bytes of each opening of `implement` and `writing-style` (S3, S10, Q4) | `evals/framer-phase-2.md` reading `pass`, or `fail` with its cause read as `spec.md` §*What moves rule 5* says; `noninferiority.py check` exit 0; `tests/test_a_rewritten_definition_proved_non_inferior.py` exit 0 | |
| 3 | **Only on a `fail` in phase 2. Paid, about $17; the orchestrator schedules it.** The cause phase 2 read, fixed once in one commit to `agents/framer.md`, then one second side as in phase 2 with `--phase 3`. No third side: a second `fail` is recorded as it reads, with its decomposition, and goes to `overview.md`'s Not done with the owner named | `evals/framer-phase-3.md` and `noninferiority.py check` exit 0, whatever it reads | |
| 4 | **The close.** `changelog.md` with the framer's row (preload bytes, tokens per call, spend, graders, verdict, each with its commit, read from the records). Before the pull request, the read set's sha256 at the branch head compared with the measured commit (S12, Q2): where it moved, phase 2's commands run again on the rebased tree, about $17, scheduled by the orchestrator. `overview.md` where a divergence or an unverified item arose | the comparison's table in `phases/phase-4.md`; the fragment's figures equal the records' | |

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past one
— someone can open it — which is the same trick that lets a round record live
beside the contract rather than in tool state.

Fill it in as each phase closes, not at the end. A phase reconstructed
afterwards is reconstructed from the diff, which is where it already was.

What a phase discovers while it is being built, and needs the next phase to
know, does not fit in this table's cells. Write it to
`seal/specs/<work-item-id>/phases/phase-N.md`, from `templates/sdd-phase.md`,
when the phase closes.

One caveat, so nobody builds on it, and it has two halves. Where feature
branches squash, these commits stop resolving at the merge — and **a rebase
during the work does the same thing earlier and far more quietly**, because the
orphaned object still answers `git cat-file` in the worktree that wrote it.
The quiet half is the one that bites: this column was wrong on its own first
use, nine SHAs deep, and only a reviewer opening them found it. **Re-read the
column after any rebase**, or it names commits that resolve in one clone and
nowhere else. That is tolerable because nothing measures from this column.

## The paid runs and what each is estimated to cost

Each estimate is read from the recorded framer sides ($16.1196 to $17.3532,
mean $16.74), and nobody has measured a side on the rewritten tree. The
smaller context should lower spend, as it did for the smith (−18.9%), and
the estimate does not count on it.

| Run | When | Estimate |
|---|---|---|
| Baseline side | not taken: guard 1 keeps #967's side | $0 |
| New side (phase 2) | always | about $17, capped at $25 |
| Second side (phase 3) | only on a phase-2 `fail` | about $17, capped at $25 |
| Re-measure (phase 4) | only where a rebase moves the read set | about $17 a time, capped at $25 |

The expected spend is about $17. With a `fail` it is about $34, and each
re-measure a rebase forces adds about $17.

## Operational impact

None for a deployer: no migration, no new variable, no dependency. A user
reading the README sees the framer's preload as `agent-contract`. A framer
spawned after the merge reads less at startup and opens two skills by
section. No in-flight work item's records change.
