# Implementation Plan: docs/ states the current rule in one read (#941)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-20 by the orchestrator, under the owner's `automation` answer and Q1–Q3's answers, when `smith` was spawned for phases 1–3; phases 4–6 and 7–9 follow in later spawns.

<!-- The line above is the record that the gate happened. Fill it in at the
spawn: reading this plan and spawning the builder IS the approval, so nothing
extra is being asked for here — only that the approval stop living in a
transcript. A later session, a reviewer and CI all read the tree, and a plan
with nobody's name on it is indistinguishable from one nobody approved.

Where the session builds the work itself, `<who>` is still a person and the
moment is still the first edit rather than a spawn — say so in place of the
clause about `smith`, and keep the shape.

That shape is `templates/sdd-routing.md`'s, whose `Answered <date> by <who>,
before the first edit.` line records the other batch the same way: the verb,
the date, who, and the moment it was given. The two are pinned against each
other, so neither spelling can drift into a second convention for one kind of
fact. -->

## Summary

Three mechanical slices first, each green on its own: the `check:` line
replaces `Enforced by:` in every rule file, the fold markers and their
readers leave, and the no-change block replaces the em-dash form. Then five
document groups, each rewritten to the current rule, split where still past
one read, with the backlog specs of its domain read, their missing decisions
written in, their rows closed and a no-change block added. The last of them
removes what can leave now and reads the preload bytes; no paid proof runs
(owner, `questions.md` Q1).

## Technical context

What this builds on (read at ac83bdf3 unless labelled):

- `.github/scripts/rules.py`: `RULE_CLOSER` (line 47), `RULE_FILES` (48),
  `enforcer_lines` (121), `targets_of` (144), `target_problem` (153), which
  delegates to `skills/settle/scripts/fold_check.py#target_problem` (228),
  and `render` (271). It is the reader the `check:` grammar moves into; the
  resolver comes with it, because once the shape arm is gone `fold-check`
  reads no rule line.
- `skills/settle/scripts/fold_check.py`: the shape arm (`numbered_statements`
  156, `shape_problems` 281) binds statements by `FOLD_MARKER` id at or above
  `Fold shape from`; the ceiling (`past_ceiling` 351) and index
  (`index_problems` 367) arms stay.
- `skills/verify/scripts/unverified_check.py`: `NOTHING` (90), `FOLD_MARKER`
  (98), `settled` (1270), `open_record_rows` (1360). `hygiene.yml` line 160
  runs it with `--baseline origin/<base>`, so a release pull request asks at
  main's tip.
- `skills/settle/scripts/rule_changes.py#parse` (71), the nothing branch at
  lines 101 to 114; `skills/settle/scripts/settle.py#write_outcome` prints the
  nothing heading.
- Counts (executed at ac83bdf3, scripts over the tree): 240 `Enforced by:`
  lines (docs 163, agents 43, skills 34), 57,801 bytes, median 176
  characters; 549 targets over 106 distinct paths (97 test files, 6 eval case
  directories, `hygiene.yml`, `fold_check.py`, `arm_check.py`); 206 lines
  hold `::`; 18 are the `nothing` form. 127 marker lines over 80 ids in 16
  files; 67 of those ids name no directory any more. 21 test files mention
  `Enforced by`; up to 73 name a `docs/` file. `bin/settle`'s dry run: 117
  released specs, 0 to apply, all with no `## Rule changes`; 4 no-spec
  directories retired by the rule and 4 kept by it; 51 test files read
  `seal/specs`. Open `## Not verified` rows: 305 across 117 of the 125
  released directories, 123 about the suite, lint, typecheck or broad run.

**What breaks in six months.** A `check:` line names a test file #942
splits or renames: `rules --check` is red on the pull request that moves it,
which is where the fix belongs. A rule paragraph is written with no `check:`
line: nothing reads it, the same limit `rules.py`'s docstring states today
for every paragraph outside a marker group; the warden reads it. Fewer cases
pin `docs/` prose after the pins of narrative go, so a sentence can drift
from its test; the test's docstring is the rule's source, and `bin/rules
<doc>` prints the two side by side.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. The no-target form on one line, `check: none reader: <who>` | A reader writes `check: none, reader: x` or `check: none reader x`; both are refused at their line, never passed | **chosen**: the issue says one line, and two field words with colons read without a symbol |
| A2. The no-target form as two lines, `check: none` then `reader: <who>` | A second line under a rule paragraph reads as prose, and a lone `reader:` line elsewhere becomes a second label to police | rejected |
| A3. Keep `check: none — <who>` as the issue wrote it | The em dash is syntax a hyphen near-misses; the owner refused it (2026-10-20) | rejected |
| A4. Targets separated by spaces | A path holding a space cannot be named; no target in the tree holds one (executed, the 106 paths) | **chosen** |
| A5. Targets separated by commas, as today | The comma is a symbol as syntax, and a trailing comma or a missing space is a near miss | rejected |
| A6. Remove the shape arm and the `Fold shape from` row (replace the structure) | A rule written without a `check:` line goes unread by any check; premise checked: settle writes no marker since #953 (`skills/settle/SKILL.md` *What --apply does*: "No marker is written"), so the arm binds a set that only shrinks to zero | **chosen** |
| A7. Keep the shape arm, rebound to every bold-opened paragraph | `docs/` opens many grounds paragraphs bold ("**What it costs.**"), so it refuses prose that is not a rule; a reading guessed from emphasis is a report under `CLAUDE.md`, not a gate | rejected |
| A8. Keep the markers and the arm as they are (keep the structure) | The markers are the symbols the owner named for removal, and they mark nothing any reader since #953 replays | rejected |
| A9. Convert the label first, then rewrite the documents | The conversion is over text the rewrite then changes, so a converted line can be rewritten again; it is mechanical and reviewed once | **chosen**: rewriting first would leave 163 old-label lines in rewritten text, or convert by hand inside each rewrite, which is the error-prone half |
| A10. The one-shot conversion script committed to the tree | Kept beside the tree, it is a script with no second use that the census tests of `.py` files then judge | rejected: run from the builder's scratch, its marker mapping recorded in `phases/phase-1.md`, the diff is the result |
| A11. Backlog specs gain a no-change block and leave at the owner's next `settle --apply` | 117 spec files edited; the block's `why:` is the census record and leaves with the directory | **chosen**: the shipped command removes them, no step by hand |
| A12. Remove the 117 backlog directories in this item's pull request | The release pull request's readers ask at main's tip, where the rows are open, and refuse every one (`unverified_check.py` main, lines 170 to 215) | rejected |
| A13. Teach `settle --apply` to remove a released spec with no `## Rule changes` | A consuming repository's pre-#953 spec, never read against its `docs/`, leaves with its decisions unwritten; a mechanism added to save 117 edits | rejected |
| A14. Remove the backlog by hand after the release | Works, and leaves `bin/settle` listing them as staying until then; a hand step nothing records | rejected in favour of A11 |
| A15. Rewrite `docs/one-root-by-lifetime.md` in place, both editions (keep the file) | Much of what still rules there is also stated in `docs/the-record-layout.md`; one source wins, so the file may end short | **chosen**: the issue names it rewritten (#923 Q1, owner 2026-10-14); the duplicate goes to its owner document |
| A16. Dissolve `docs/one-root-by-lifetime.md` into the topical documents (replace the file) | Its index row and every citation move; the dependency rule and the opt-in signal lose the one place a newcomer reads them together | rejected for this item; open to the work if the rewrite leaves only pointers, recorded as a divergence |
| A17. Split along `##` headings into new flat files | A split file is named after its heading, and every citation of a moved section changes path | **chosen** (owner, 2026-10-20) |
| A18. A topic taxonomy for `docs/` | | refused by the owner |
| A19. One phase per document group, the backlog read with its group | A spec spanning two groups is read twice | **chosen**: each phase stands alone with its documents, pins and specs; the assignment rule in `spec.md` gives each spec one group |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The `check:` line. `rules.py` reads the grammar of `spec.md` and refuses every other spelling; the resolver moves into it; `fold-check`'s shape arm and `Fold shape from` go; the `rule` marker is registered and carried by the gate tests; all 240 lines converted, the 18 `nothing` lines by hand; the prose naming the label rewritten; the cases pinning the old label updated | each refusal of S5 seen red with its branch deleted (contract 15); `bin/rules --check` exit 0 over the tree; `bin/rules docs/the-review-record.md` prints a marker's docstring; the S7 comparison (the base's target paths before `::`, from `git grep -hE '^\s*Enforced by:' ac83bdf3 -- <RULE_FILES>`, minus the paths HEAD names or a marker carries, is empty or each remainder a `## Removes` row); the modules of `rules.py`, `fold_check.py` and the 21 test files naming the label | f60117a3 |
| 2 | The markers out: 127 lines from `docs/`, the marker arm and exemption, the `CONTRIBUTING.md` sentence, `FOLD_MARKER` where no reader is left | `git grep -c '<!-- specs/' -- docs` prints nothing; `tests/test_both_editions_carry_the_same_folds.py`, `tests/test_docs_line_wrap.py`, `fold_check.py`'s and `unverified_check.py`'s modules | 4b40d109 |
| 3 | The no-change block in `## Rule changes` and `## Removes`: `rule_changes.py`, `unverified_check.py#NOTHING`, `settle.py`, `templates/sdd-spec.md`, `skills/settle/SKILL.md`, `docs/the-reader-registry.md`, and #953's spec rewritten to it | S10's cases seen red; `bin/settle` dry run lists #953's spec and this one as nothing to apply, not as refused; the modules of the three scripts | 346369b7 |
| 4 | Commit gate group: `docs/commit-review-gate-spec.md`, `docs/the-commit-gate-inside-git.md`, `docs/the-review-and-parity-arms.md` rewritten; their backlog specs read, rows closed, blocks added | per group, the same six: `bin/fold-check` (no group document past 25000, index passes); `bin/rules --check` exit 0; the S7 comparison for the group; `unverified_check.py` over each group backlog directory reports no open row; `bin/settle` dry run lists each as nothing to apply; the pin cases of the group's documents and the modules they touch. Plus the census table in `phases/phase-4.md` and S14's grep per renamed heading | |
| 5 | Worktree guard: `docs/worktree-guard-spec.md` rewritten, split along its `##` headings if still past 25000, the new files on `docs/README.md` rows; its backlog | the six of phase 4; S14 for every moved section's citations in `skills/`, `agents/` and tests | |
| 6 | Review and records: `docs/the-review-record.md`, `docs/the-record-layout.md`, `docs/the-reader-registry.md`, `docs/the-agent-set.md`; its backlog | the six of phase 4 | |
| 7 | Release and tracker: `docs/branch-and-release.md`, `docs/release-checklist.md`, `docs/issues-and-milestones.md`; its backlog | the six of phase 4 | |
| 8 | Runs, broad gate, pact: `docs/measuring-a-run.md`, `docs/the-broad-gate.md`, `docs/the-pact.md`; its backlog | the six of phase 4 | |
| 9 | One root: `docs/one-root-by-lifetime.md` and `.ko.md` rewritten to what still rules, split if still past 25000; every backlog spec no group took; the 8 directories removed, each check that reads `seal/specs` answered; `docs/README.md`'s rows final | the six of phase 4; S13's two `--baseline` runs; S15; S11 over all 117; S16's `wc -c` at ac83bdf3 and here | |

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

## Operational impact

- **A consuming repository's `fold-check` stops reading rule shape.** Its
  `Fold shape from` row is read by nothing, and its `Enforced by:` lines are
  refused by `bin/rules --check` if it runs that, with the new spelling named.
  The changelog fragment says both.
- **No consumer has written the em-dash no-change form**: the `## Rule changes`
  grammar first ships in 0.22.3 with this item, so the block change breaks no
  released record.
- **The owner's settle after 0.22.3 merges removes about 121 directories**
  (the 117 backlog specs and the 4 no-spec directories whose rows this item
  closes), and owes an answer to each of the 51 checks that read `seal/specs`.
- No new dependency, environment variable or migration.
