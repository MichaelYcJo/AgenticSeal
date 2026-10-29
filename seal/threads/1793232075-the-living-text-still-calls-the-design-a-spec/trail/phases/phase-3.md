# Phase 3: 1793232075-the-living-text-still-calls-the-design-a-spec

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 3816dfca |

## What this phase was asked

Build phase 3 of `frame/plan.md` from HEAD `6d33f30b`, in the same build
context as phases 1 and 2. #1020 left `release: 0.24.0` for 0.25.0 by the
owner's decision, and its branch will not merge in this release. So
`CLAUDE.md`, `skills/agent-contract/SKILL.md`, `skills/code-review/` and
`agents/proofer.md` are this work item's to edit, and `frame/questions.md`
Q1's Status records that at `6d33f30b`. `origin/release/v0.24.0` is still
`475653e7`, this branch's base, so no merge comes first. The phase re-runs
C1 at HEAD and records its hits. It then rewrites the occurrences the frame
lists in those files, retitles the step-1 heading with all its citations,
and renames the review stage, `hooks/review-skill-gate.py` included. It
also rewrites `chain_check.py:1604`, `:1612` and `:2268`, with the pin at
`tests/skills/test_chain_check.py:1691`. A C1 hit the frame's tables do not
list follows Q2's default. The phase amends `changelog.md` where it changes
what the fragment says.

## What this phase found

- **C1 at `6d33f30b` matched the frame's phase-3 rows.** It gave 163
  lines, the same list as at `92bd9acc` (executed, `diff` empty), since
  `6d33f30b` changed only `frame/questions.md`. In #1020's files, C1 found:
  - `CLAUDE.md:10`;
  - `agents/proofer.md:4`, and `:89`, which is a reference root and is
    kept;
  - `skills/code-review/SKILL.md:4`, `:9`, `:13`, `:22` (twice), `:31`,
    `:50`, `:53` and `:115`;
  - `skills/code-review/orchestration.md:393`;
  - `chain_check.py:1570` and `:1577` (identifiers, kept), and `:1604`,
    `:1612` and `:2268`.

  `skills/agent-contract/SKILL.md` had no hit. No hit fell outside the
  frame's tables, so Q2 did not apply.
- **The step-1 heading has ten citations, not twelve.** `plan.md`'s row and
  `frame/design.md` *Scope* item 5 say twelve. The frame's own list, and
  `git grep -n -i 'Read the spec'`, give ten (executed):
  - `CLAUDE.md:10`, `CONTRIBUTING.md:388`, `agents/framer.md:51`,
    `hooks/mode-gate.py:38` and `skills/implement/orchestration.md:305`;
  - `tests/hooks/test_question_gate.py:437`,
    `tests/text/test_the_rules_claude_md_names_have_one_home.py:83`,
    `tests/hooks/test_mode_gate.py:52` and `:94`, and
    `tests/behaviour/test_chain_hooks_hardening.py:596`.

  A search for the heading's words split across two lines found no
  others (executed). The heading and all ten citations moved in
  `3816dfca`, and `git grep -n -i 'Read the spec'` outside `seal/threads/`
  now prints nothing (S6, executed, exit 1).
- **Wording the rows left open.**
  - In `skills/code-review/SKILL.md`, stage 1 reads "**Compliance**: the
    code against the documents that outrank it".
  - The comparison-axis cells say "the policy or the design".
  - `must` is "a compliance violation or a defect to fix".
  - `skills/code-review/orchestration.md:393` reads "Citations of a
    policy's or a design's clauses".
  - In Korean, "스펙 준수" became "준수".
- **The gate's option text had no pin, so this phase added one.**
  `hooks/review-skill-gate.py#REASON` is a prompt a person reads (contract
  rule 14). `test_refuses_the_builtin_with_a_reason_asking_a_two_option_question`
  now asserts "/agentic:code-review: compliance first, then quality" in
  the prompt, with whitespace folded. The pin names the skill because the
  old text, "spec compliance first, then quality", contains the bare
  phrase. A first form of the pin carried a negative assertion on the old
  phrase. That line printed under S7's own `git grep`, so it went before
  the commit.
- **Each pin was seen red through `bin/seal mutate` at `3816dfca`.**
  - The refusal in `chain_check.py` was put back to "this spec", and
    `test_refuses_a_section_the_parser_refuses_at_its_line` went red: 3
    cases at the edit, then `red` under the mutation (executed).
  - The gate's option was put back to "spec compliance first", and the
    pinned case went red (executed).
  - The heading was put back to "Read the spec before the code", and 4
    cases across `test_question_gate.py`,
    `test_the_rules_claude_md_names_have_one_home.py` and
    `test_a_cited_section_stands_in_its_file.py` went red (executed,
    `4 failed, 50 passed`).

  Each run exited 0 with the verdict `red`. `git status` was clean after
  each.
- **Reflows.** Each moved citation was longer than the old one. Its
  paragraph was reflowed in `CLAUDE.md`, `CONTRIBUTING.md`,
  `hooks/mode-gate.py`, `skills/implement/orchestration.md` and
  `tests/hooks/test_mode_gate.py`, and no other word changed. No added
  line outside a table passes 88 columns (executed).
- **`docs/` still calls the design a spec at the lines the nine
  `## Rule changes` operations name.** Those operations cover
  `docs/README.md:4`, `docs/one-root-by-lifetime.md:17`,
  `docs/release-checklist.md:100`, `docs/the-pact.md:84`,
  `docs/the-record-layout.md:98` to `:107`, `docs/the-review-record.md:282`
  to `:292`, and the Korean `docs/one-root-by-lifetime.ko.md:17`. The
  settle after 0.24.0 writes them. S1 reads every other C1, C2 and C3 hit
  against *Occurrences kept, and why*, and each is there or is one of
  phase 1's Q2 (b) lines (read).
- **The test modules this phase touches.** 88 modules name a phase-3 file.
  They include `tests/skills/test_chain_check.py`,
  `tests/behaviour/test_docs_line_wrap.py`,
  `tests/text/test_no_passage_is_pasted_into_a_second_file.py`,
  `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and
  `tests/test_censuses.py`. The run gave `3564 passed, 11 skipped`
  (executed, `bin/test -q`, exit 0).

### C1 to C6 at `3816dfca`

| Command | Output |
|---|---|
| C1 | 140 lines in 39 files. Each is in *Occurrences kept, and why*, is an identifier, or is a `docs/` line one of the nine `## Rule changes` operations names |
| C2 | 20 lines: `README.ko.md:160` (the policy document's name), the `specseal` brand lines (phase 1's Q2 (b)), `:374` to `:399` (the 0.3.x move), and `docs/one-root-by-lifetime.ko.md:17` (a rule change) and `:23` to `:26` (a reference root) |
| C3 | 18 lines, the same as at `92bd9acc` |
| C4 | 59 lines, the same as at `92bd9acc` |
| C5 | `design`, `Design`, `designs`. No word holds `design` inside another word |
| C6 | 830 hits in 77 files under `tests/`, from 837 in 79. Five test citations of the heading, the refusal pin and `tests/hooks/test_review_skill_gate.py`'s docstring account for the 7 |
