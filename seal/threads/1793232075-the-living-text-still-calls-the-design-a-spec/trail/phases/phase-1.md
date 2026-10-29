# Phase 1: 1793232075-the-living-text-still-calls-the-design-a-spec

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | e3c6503f |

## What this phase was asked

Build phase 1 of `frame/plan.md` against the frame at `d4b88f70`, with
phase 2 in the same spawn. Phase 3 waits for #1020 to merge
(`frame/questions.md` Q1, default (a)), so it is not built here. Routing is
automation, and nobody is asked anything mid-run. Q1 stands on (a) and Q2 on
its default, and each default the build rests on is recorded. Every rewrite
stays inside the frame's two tables. The phase edits no file under `frame/`
other than its Status cell, and none of #1020's files: `CLAUDE.md`,
`skills/agent-contract/SKILL.md`, `skills/code-review/` and
`agents/proofer.md`. Commands C1 to C6 of `frame/design.md` *The class,
enumerated* run at the phase's close, and their output is recorded here.
C5 guards against `spec` turning into `design` inside a longer word.

## What this phase found

- **The frame held, with two omissions in its lists.** Every line the
  phase-1 rows name stood at the coordinate the frame gives (read, against
  C1 at `d4b88f70`: 255 lines in 53 files, the frame's own count).
  - **Five pins the frame's pin list does not name.**
    `tests/text/test_settle_reads_before_it_removes.py` pins five sentences
    this phase rewrites, at base lines `:81`, `:112`, `:150`, `:177` and
    `:223`: the settle skill's opening lead, step 3 of its procedure, the
    `from` lead, the removed-designs sentence, and `implement`'s model row.
    Scope item 7 covers them, so each moved with its sentence in
    `e3c6503f`.
  - **`README.ko.md:438`** ("스펙 체인") is in neither table. Its English
    edition, `README.md:445` ("the spec chain"), is a phase-1 row. Q2 (a)
    applies: the line names the documents a crafter reads, so it was
    rewritten to "정책과 설계와 계획" in step with the English "the policy,
    the design and the plan".
- **Q2 (b), lines that stay because they name something else.**
  - `hooks/root-migrate.py:98` maps the 0.22.x file name `overview.md` to
    `gaps.md`, so it is history.
  - `skills/writing-style/SKILL.md:167` cites the word "overview" as an
    example of a bad translation, and names no closing memo.
  - C2 prints `README.ko.md:167`, `:280`, `:304`, `:306`, `:312`, `:317`,
    `:388`, `:395` and `:396` because they hold the old brand `specseal`.
    That is the plugin's former name, not the design.
- **Choices of wording the rows left open.**
  - `implement`'s "the spec chain" became "the policy, the SDD set and the
    ticket". These are the three documents step 1 ranks above the code.
  - `legacy-parity`'s title became "the original is the fallback authority".
  - `orchestration.md:11` names "the procedure that reads the documents
    before the code" in place of "the spec-first procedure".
  - The settle skill's step 9 says "the work item ids in merge order".
  - The pact template, and `orchestration.md`'s pact bullet, say "framed by
    a work item's design in this repository".
- **The longer words pushed three paragraphs past the wrap limit.**
  `tests/behaviour/test_docs_line_wrap.py` refused
  `skills/implement/SKILL.md:216` at 92 columns and
  `skills/implement/orchestration.md:12` at 101 (executed). Both
  paragraphs, and the legacy-parity and settle paragraphs the edits
  shortened, were reflowed. No word of them changed.
- **Each moved pin was seen red.** With the old sentences in place and the
  pins moved, all seven cases failed: the tracer's rule lead, the closing
  memo's diff, and the five settle pins. They are
  `test_the_tracers_rules_stand_with_their_enforcers`,
  `test_the_skill_states_the_closing_convention`, and five cases of
  `test_settle_reads_before_it_removes.py` (executed, `7 failed, 269
  passed`). Each sentence was put back through the `Edit` tool, and the
  three modules passed.
- **One case was red before this phase and stays red until the closing
  memo lands.** `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`
  refuses a work item with a `frame/design.md` and no `gaps.md`. That held
  at `d4b88f70` already. The closing memo is opened in the commit that
  writes this record.
- **The test modules this phase touches.** 66 modules under `tests/` name
  a phase-1 file, and `tests/test_censuses.py` was run with them. The run
  gave `1 failed, 2399 passed`, and the one failure is the case above
  (executed, `bin/test -q`, exit 1). `uvx ruff check` and `uvx ruff format
  --check` over the three changed test files exited 0.

### C1 to C6 at `e3c6503f`

| Command | Output |
|---|---|
| C1 | 208 lines in 46 files, from 255 in 53. Every line is in *Occurrences kept, and why*, or is a phase-3 row: `README.md:38`, `:40`, `:177`, `agents/framer.md:51`, `skills/implement/SKILL.md:139`, `skills/implement/orchestration.md:305`, and #1020's files. The phase-2 files still hold their rows |
| C2 | 23 lines. `README.ko.md:38`, `:40` and `:171` are phase 3. `:160` is the policy document's name, and `:374` to `:399` are the 0.3.x move. The `specseal` lines are Q2 (b) above. `docs/one-root-by-lifetime.ko.md:17` changes through `## Rule changes`, and `:23` to `:26` are a reference root |
| C3 | 29 lines, none in a phase-1 file but `hooks/root-migrate.py:98` and `skills/writing-style/SKILL.md:167`, which are Q2 (b). The rest are phase 2's `unverified_check.py` lines and identifiers |
| C4 | 63 lines. Four are phase-2 rows: `skills/commit-pr-convention/SKILL.md:210` and the three lines of the two blinded cases. The rest are fixtures under `tests/`, and `evals/scripts/replay_targets.py:132`, which `trail/phases/phase-2.md` describes |
| C5 | `design`, `Design`, `designs`. No word holds `design` inside another word |
| C6 | 845 hits in 80 files under `tests/`, from 852 in 81 at `475653e7`. The seven moved pins account for the drop, and `tests/text/test_a_moved_rule_leaves_its_definition.py` held only its one |
