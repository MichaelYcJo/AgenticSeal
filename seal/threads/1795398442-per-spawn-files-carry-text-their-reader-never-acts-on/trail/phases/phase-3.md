# Phase 3: 1795398442-per-spawn-files-carry-text-their-reader-never-acts-on

## What this phase found

**The frame holds against the tree at `1f0880be3`, two lines lower.**
Phase 2's re-pointed citation in *Orchestrator: a phase is a fresh
crafter, and a fix pass resumes the implementer* added two lines to
`skills/code-review/orchestration.md`. So the pull request section opens
at `:235` where `frame/design.md` *Grounding* G11 read `:233`, and every
paragraph of G11's two lists stood two lines below its coordinate (read,
each opening checked against the line). The orchestrator folded *Scope*
item 5's sentence on "the opening of `skills/implement/SKILL.md`" at
`1f0880be3`, and phase 2 had already made that edit, so this phase made
none. Judged against `frame/design.md` *Scope* items 2 to 5.

**The cut, as built (`1f637cdfe`).** The section's first paragraph now
ends at "committed and unpushed." and one sentence cites
`skills/code-review/gate-to-pull-request.md` *Orchestrator: from the
preflight to the open pull request* for the steps from the preflight on.
The part from "Once `guarantee.md` reading `sealed`" moved as the new
section's first paragraph. It started mid-line, so it was rewrapped, and
no word changed. The eleven paragraphs after it moved as they stood. A
word count of the old section against the kept section and the new
section shows the only differences: the citation sentence, the new
heading, and the rewritten row 6 below (executed, a script over
`git show HEAD:<file>` at `1f0880be3` and the working tree).

**One pointer crossed the cut, and its first rewrite tripped the paste
check.** Row 6 of the `seal pr-wait` exit table said the orchestrator
"merges the base into the branch, as the next paragraph states". The
next paragraph in the new file is the stated limit, so the row now cites
`skills/code-review/orchestration.md` *Orchestrator: the pull request
opens once the sealer seals* "for a conflict with the base". The first
rewrite quoted the merge paragraph's whole bold lead. That bold lead is 18
words, and `tests/text/test_no_passage_is_pasted_into_a_second_file.py`
counts any run of 15 words that two rule documents share. `236d3c5e6`
shortened the citation. The other cross-references in the moved
paragraphs ("the `gh api -X PATCH` call below", "the repair path below",
"the stated limit above", "*A refusal about the `Broad gate` key* below")
point within the new file, so they stand (read). Judged against
`frame/design.md` *Scope* item 4.

**The paste check still refuses the tree at `236d3c5e6`, and this phase
did not reword the text to pass it.** The refusal, quoted:

> skills/code-review/gate-to-pull-request.md and
> skills/code-review/orchestration.md share 1 runs of 15 words; the
> longest is 15 words: 'that the row no fix that no round reads of
> section-citation gives to a round,'.

The two clauses cite the core's row in the form
`tests/text/test_the_rules_have_one_owner.py#THE_CORES_ROW` requires of a
link. One clause is in the moved exit-1 paragraph ("Review a repair that
the row … gives to a round, and run the gate again"). The other is in
*Orchestrator: the run ends with a verifying round*, which this work does
not edit. The same file held both before the cut, so the check had no pair
to count. The check folds a `.md` path followed by its `*section*` into one
token, but not the row's italic name in front of it. So a link in this
form is counted as a copy. Contract rule 18 forbids bending correct text
to pass a check. *Scope* item 4 moves the paragraphs "with their words".
Changing `skills/settle/scripts/passages.py#words`, which
`chain_check.py` also reads through, is outside phase 3's Delivers cell.
It goes to the hand-back for the orchestrator to decide (`gaps.md`
*Not done*).

**Citations and cases the frame did not name followed the move.** The
census was every tracked file outside `seal/threads/`, with its whitespace
folded. It searched for the heading's words, then for every citation of
`skills/code-review/orchestration.md` by path. Then it searched for the
moved paragraphs' bold leads and commands, and each hit was read for which
paragraph it meant (executed). It found these:

- two comments in `skills/verify/scripts/broad_gate.py` (the docstring of
  `moved_line` and the comment over the command line in `gate`), which said
  `skills/code-review/orchestration.md` has the orchestrator quote the
  gate's lines;
- the network table's row in `README.md` and `README.ko.md`, whose link
  named the one file for `gh pr create` and the body's rewrite; it now
  names both files;
- three cases outside G13's list that read a moved fact:
  `tests/behaviour/test_the_sealer_guarantees.py#TestDefinition::test_the_orchestration_quotes_the_gates_outputs_line`,
  `tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py#test_the_review_orchestrator_names_the_command_that_answers_the_row`
  and
  `tests/text/test_the_rules_have_one_owner.py#test_the_orchestrator_writes_the_body_file_the_sealer_reads`,
  with rule 28's link in the same module;
- the comment in `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`
  saying `skills/code-review/orchestration.md` cites *The broad gate* for
  the words beside a failing file.

The hits that cite the rule, the merge, `pr.md` or the rebase rule
resolve under the kept heading and were left as they stand. They are
`skills/core/SKILL.md`, `CONTRIBUTING.md`, `docs/forms/the-guarantee.md`,
`docs/releasing/branch-and-release.md`,
`docs/releasing/release-checklist.md`, both lines of
`skills/commit-pr-convention/SKILL.md`, both of
`skills/writing-style/outside-the-review.md`, `templates/setup/config.md`,
both of `skills/implement/SKILL.md` and step 2 of
`skills/implement/orchestration.md` (read). This list is a sample in
contract rule 12's sense: a sentence that states a moved step in other
words, without the heading, the path or a moved paragraph's lead, is not
reached.

**The core-sentence case reads the orchestrator file's opening, not the
whole file.** `skills/code-review/orchestration.md` names
`skills/core/SKILL.md` six times, five of them in the core's row
citations. So a case over the whole file would stay green with T4 deleted.
`tests/behaviour/test_chain_hooks_hardening.py#test_the_review_skill_opens_the_core_once_where_it_orchestrates`
reads the text before the first `## Orchestrator:` heading. Judged
against `frame/design.md` *Scope* item 9 and contract rule 15.

**The moved text owes no case of its own.** The phase moves paragraphs,
removes three sentences and re-points citations. So it is proved as
`skills/verify/SKILL.md` *The narrow command still has to be able to
fail* says for a move: by the existing cases at the new place and by the
census of the old spelling. No unit adds behaviour, so `seal mutate` ran
for no unit. It ran for the re-pointed cases instead, as contract
rule 15 asks.

**Seen red (executed).**
- Before any case was re-pointed, with the text moved and nothing
  committed, the plan row's modules gave 11 failed and 2255 passed. Each
  failure was a case reading a moved fact where it no longer stood, plus
  one line over the wrap limit, which was rewrapped.
- After `1f637cdfe`, `bin/seal mutate`, each run alone. Each verdict was
  `red` (exit 0), and each failing line names the guard broken.
  - In `skills/code-review/gate-to-pull-request.md`:
    - `--once` dropped from the wait: the mergeable case, "no longer says
      '`seal pr-wait <N> --once`'".
    - `--body-file <that file>` dropped: the body-file case.
    - *What the gate runs* dropped from the base's citation: rule 28's
      link case, naming the new file.
    - `<work-item-id>` dropped from `gate.log`: the broad-run-command
      case and the capture-file case, each run.
    - `seal stamp --from` changed: the stamp case.
    - `/agentic:config` changed: the broad-gate-row case.
    - The outputs line shortened: the capture-file case and the sealer
      case, each run.
    - `--preflight` dropped: the broad-run-command case.
  - In `skills/code-review/orchestration.md`:
    - T4's `AgenticSeal core from` shortened: the core-sentence case.
    - T4's `skills/core/SKILL.md` replaced: the same case. This run is
      red only because the case reads the opening.
  - In `skills/verify/orchestration.md`, the citation's path turned back
    to `orchestration.md`: the timing case.

  The tests named each case by `-k` over its module, with
  `bin/test -q -p no:xdist`. The tree was clean after the runs (executed:
  `git status --short`).

**The plan row's census (executed at `1f637cdfe`).** These searches each
printed nothing: `git grep -n -F` for `AgenticSeal core from` in
`skills/code-review/SKILL.md`, and for `preloads that one` and
`0.22.0 run` in `skills`. Each pattern found its line at `1f0880be3`. All
twelve paragraphs of G11's second list were found in the new file by their
opening words, and none in `skills/code-review/orchestration.md`. The six
paragraphs of the first list that follow the section's first paragraph
were found in `skills/code-review/orchestration.md` by their bold leads
(executed, a script over both files with whitespace folded).

**The phase boundary set was run in one command (executed).** It was
`bin/test -q tests/text tests/behaviour` and the modules outside those
directories that one of two lists names. The first was the plan row's
`git grep -l -E 'code-review' -- tests`. The second was the files that
name `broad_gate`, `pr_wait`, a README or either orchestration file this
phase changed. `tests/conftest.py` and `tests/run_tests.py` were left out.
At `236d3c5e6` it gave 1 failed, 3753 passed and 10 skipped. The failure
is the paste check above. At `1f637cdfe` the same command gave the same
count, with the longer 18-word run. The plan row's command alone gave
2267 passed and 9 skipped over the working tree before two edits that
`1f637cdfe` also holds: the section reader of the mergeable case split
into two names for the formatter, and a comment in
`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`. The
boundary runs at both commits cover those edits.
Lint and format of the changed Python files passed
(`uvx ruff check` and `uvx ruff format --check`, executed).

**The measurement at `236d3c5e6` (executed).**
`python3 .github/scripts/release_report.py --against v0.38.5 --at <clone>`
was run from a `git clone --no-local` of the branch checked out at
`236d3c5e6`, and `<clone>` was a second clone checked out at `641b6bfb5`,
which `git describe --tags --exact-match` names `v0.38.5`. Both clones
are under this phase's scratch directory.

| What | v0.38.5 | Now | Change |
|---|---|---|---|
| preload `crafter` (bytes) | 31,032 | 30,613 | -419 (-1.4%) |
| preload `framer` (bytes) | 37,367 | 37,028 | -339 (-0.9%) |
| preload `proofer` (bytes) | 31,678 | 31,379 | -299 (-0.9%) |
| preload `sealer` (bytes) | 32,070 | 31,909 | -161 (-0.5%) |
| preload `tracer` (bytes) | 24,352 | 24,191 | -161 (-0.7%) |

`git show <rev>:<path> | wc -c`, at `6edff124a` then `236d3c5e6`:
`skills/agent-contract/SKILL.md` 11,932 then 11,625 (12,029 at v0.38.5);
`skills/implement/SKILL.md` 26,353 then 22,114;
`skills/code-review/SKILL.md` 15,859 then 15,737;
`skills/code-review/orchestration.md` 38,635 then 23,920; and
`skills/code-review/gate-to-pull-request.md`, new, 15,665. Every preload
row is negative, the contract is below 12,029, and the three files S3
names are smaller, so S1, S2 and S3 hold at `236d3c5e6`. Phase 2's 72
bytes are inside the orchestration file's figure. A later commit that
changes a measured file owes the measurement again (*Scope* item 12).
