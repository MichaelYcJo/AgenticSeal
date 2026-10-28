# Questions for the planner: 1793171930-no-check-reads-a-citation-of-most-files

## Judgments the ticket left open that the tree answered

Listed so nobody reopens them. Each one's grounds are in `frame/design.md` or
in `frame/plan.md`'s Alternatives table.

1. **How a cited text matches a heading.** Equal to it, or the heading's
   opening words with the next character neither a letter nor a digit, case
   for case. Four living citations name a section by its opening words, and
   `skills/writing-style/SKILL.md` refuses a near-miss spelling.
2. **What a bold rule lead is.** A live paragraph or list item opening with
   `**`, read to the closing `**`. Three living citations name one, and a
   rule here opens with a bold sentence by design.
3. **Which spellings are citations.** The backticked path with or without
   `'s`, and the two name forms the old case read, widened from `implement`
   to every skill whose `SKILL.md` is tracked (contract rule 12).
4. **A path that is not the repository's.** Not read when its first segment
   is no tracked top-level entry; refused when it is one and names no
   tracked file, since a moved file dangles as a renamed heading does.
5. **`<commit>:<path>` and placeholders.** Neither is read. The comment that
   cites the removed *Where the stamp is drawn* takes the `<commit>:<path>`
   form `docs/the-record-layout.md` prescribes.
6. **What the case skips.** `tests/censuses.py#RECORDS`, one list, in place
   of the old case's own copy.
7. **What "reported, not failed" reads.** The pending items of every
   `seal/threads/*/frame/design.md`, through `rule_changes.parse`, for
   citations in files of the policy root only.
8. **Where the rule lives.** In `skills/writing-style/SKILL.md`, which a
   pull request edits; `## Rule changes` holds the no-change block.
9. **Where the module stands.** `tests/behaviour/`, because it loads
   `rule_changes.py` and `hooks/lib/config.py`.
10. **The pin in `tests/text/test_broad_gate_rule.py`.** Kept: it holds that
    the broad gate section names its owner, which a resolver does not, and
    the file is #1040's.

## Rows

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does a `warnings.warn` raised inside a case reach the output of `bin/test -q`, which runs under `pytest-xdist` (`bin/test`, read), and the record `seal gate --record` writes? The tree states neither, and no case in it raises a warning to report anything (`git grep` executed). | a measurement | (a) It prints in the warnings summary: S9 reports through it as framed. (b) It does not: S9's report needs another channel the run shows, chosen at the build. | (a). Phase 2 runs the S9 fixture once under `bin/test -q`, reads whether the warning is printed, and on (b) picks the channel and records it as a divergence in `trail/phases/phase-2.md`. | answered 2026-10-28 by a measurement in phase 2: (a), the warning prints in `bin/test -q`'s warnings summary under xdist; `trail/gate.md` keeps no test output, so whether the gate's kept output shows it is a `gaps.md` row (`trail/phases/phase-2.md`) |
| Q2 | Does a sibling branch merged into `release/v0.24.0` before this one change what S1 meets? #1053 edits `.github/scripts/gather_changelog.py`, and #1040 edits `agents/*.md`, whose rule leads this case resolves; neither branch's diff is in this tree to read. | the work | (a) Nothing changed: the three corrections stand as framed. (b) A citation of *Scope* item 2 is gone, or a new one dangles: the phase that meets it at rebase corrects the citing line, or drops a correction whose line is gone. | (a). On (b), the phase records the coordinate in its divergence row and never edits a file only to keep a sibling's text. | open |
