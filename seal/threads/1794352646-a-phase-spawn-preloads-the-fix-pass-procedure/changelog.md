### Changed

- **A crafter spawned to build a phase no longer preloads the fix pass's procedure (#1471).** The procedure moved out of `agents/crafter.md`, which every crafter spawn preloads, into a new file, `skills/implement/fix-pass.md`, which only a fix pass opens. A phase spawn's preload, measured by `.github/scripts/release_report.py#preloads`, is 33,717 bytes, where it was 35,883. Step 9 of the crafter's definition now reads "In a fix pass, open `skills/implement/fix-pass.md` and follow it in place of steps 5 to 8."
- **`skills/implement/SKILL.md` *5. Incorporate review — read the round records first* names the new file in one paragraph (#1471).** The section held the same procedure a second time, and every crafter read it at its first step, in a phase as in a fix pass. A session that fixes review feedback reads the paragraph and opens the file before it judges the first finding. The paragraph on draining the open rows stays.
- **The new file holds five sections, in the order a fix pass takes them (#1471).** It starts at the round records and judges each finding at its coordinate. It reads a paste-ready fix against the frame and the code before applying it. It runs the round's narrow set and reads its range and the work item's records whole. It appends the close blocks last, uncommitted. And it brings the changelog fragment along. A moved sentence that was written to "you" now names the fix pass, and one that stated the round-record form's facts about a close block now cites the form (below).

### Removed

- **Three copies of what the round-record form already states about a close block (#1471).** The crafter's definition listed the three `verdict:` values. It, `skills/implement/SKILL.md` *5.* and `skills/code-review/orchestration.md` each restated when a close block carries a `location:` line of its own. `docs/forms/the-round-record.md` states both, and `skills/implement/fix-pass.md` cites its two paragraphs by their bold leads. `tests/text/test_a_moved_rule_leaves_its_definition.py` refuses a copy of either fact in the crafter's definition, the new file, `skills/implement/SKILL.md` and `skills/code-review/orchestration.md`.

### Process changes

| Date | Change | Why | Source |
|---|---|---|---|
| 2026-11-11 | A fix pass, the crafter's at step 9 or a session's from `skills/implement/SKILL.md` *5.*, opens `skills/implement/fix-pass.md` and follows it; `agents/crafter.md` no longer holds the rule **A fix pass appends close blocks and writes no phase record.**, and `skills/code-review/orchestration.md` cites the round-record form for what a close block holds | Every phase spawn paid about 2.2 KB of preload and 1.6 KB of reading for a procedure only a fix pass acts on, and the close block's values and `location:` rule stood in four places | https://github.com/MichaelYcJo/AgenticSeal/issues/1471 |
