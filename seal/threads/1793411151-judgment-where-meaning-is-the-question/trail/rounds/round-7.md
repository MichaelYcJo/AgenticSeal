# Review round 7: 1793411151-judgment-where-meaning-is-the-question

target: 2b7eef28, fixes e71bbaea..2b7eef28

This is the verifying round over round 6's fix pass. It reads the fix
diff `e71bbaea..2b7eef28` alone. That diff holds `6cec9edf` and `edf90008`
(finding 2), `5387ce4e` (finding 1), `c4e91dd2` (finding 3), `59beac2a` (the
`CONTRIBUTING.md` prevention home), `e768e535` (the fix pass's answers) and
`2b7eef28` (the orchestrator's fold of the frame). It reads nothing of
phases 4 and 5 except where noted below. The repository declares no
`seal/parity.md`, so this record holds no `original:` line.

Carried from round 6 and not re-derived: where `timeline` decides a
design's listing in `skills/settle/scripts/settle.py`; that the section
runs to the next heading of level 2 or higher in
`skills/settle/scripts/rule_changes.py#parse`; that
`tests/github/test_rules.py#test_every_check_line_in_the_tree_holds` drops
its capture at exit 0. Also carried: the cheaper homes for finding 3 that
round 6 ruled out. The proofer has no step that reads a rule file. A
straight-to-the-PR change has no proofer. The gaps row leaves at the
settle. Re-derived this round: every verdict below, the mutants, and the
weighing of the new hygiene step against `skills/core/SKILL.md` *The rule a
mechanism is kept against*.

## Findings

This round opens no finding. One stale line it read outside the fix diff
is a row of `## Not judged`, for round 9, which reviews the units that
made it.

## Confirmations

confirms: round-6#1
The close holds. `timeline` now lists a design to read whole when
`parse` names a line in `unread` and gives no error. That arm stands after
`errors` and before `ops is None`
(`skills/settle/scripts/settle.py:600-608`, read). So a design holding the
exact heading and a near one no longer joins a group with half its
changes. It is also no longer listed as having nothing to write.
`test_lists_a_design_with_a_line_its_reader_did_not_read_to_read_whole`
(`tests/skills/test_settle.py:490`) holds round 6's two designs. With the
arm switched off by `Edit`, the case failed (executed).
The skill's dry-run bullet states the new member in place
(`skills/settle/SKILL.md:181-184`, read). The module and `timeline`
docstrings say the same. The fix pass claimed that a near no-change line
in `unread` never reaches the new arm alone. `unread_block` names only a
first line that opens like `- nothing` and is not it. `items` then reads
such a line as a kind outside the grammar, or as a second
`- nothing`, and refuses it (`skills/verify/scripts/unverified_check.py:638-712`,
read). So `errors` decides first, and the claim holds. Were it wrong, the
design would be read whole, which is the safe direction.

confirms: round-6#2
The close holds. `inside` takes each exact section's span with the same
end the parser computes, the next heading of level 2 or higher
(`skills/settle/scripts/rule_changes.py:122-130`, read). A near heading
below level 2 in that span is therefore not named. The parser always
refuses such a heading, for a reason this round derived from the code. A
field's continuation line opens with four spaces (`CONTINUED`,
`unverified_check.py:145`). A heading holds at most three spaces of
indentation (`heading_level`, `unverified_check.py:411-421`). So no
heading can be read as a value line. Each such heading is refused as a
line outside an item, or as a line that is not a field of the item above.
The round-7 probe parsed round 6's four designs and two more edge cases
(executed, `## Probes`). A level-3 heading after an item inside the section
was refused at its line and not named. A level-1 near heading ends the
section, so it was named, and the section above it was read. Two mutants
failed the new case (executed): the `inside` filter dropped, and the span
read to the document's end. The second mutant is the one `edf90008` was
added to catch, and it is now caught. The skill bullet, `parse`'s
docstring and `chain_check.py`'s arm line state the scope in place
(`skills/settle/SKILL.md:89-96`, read).

confirms: round-6#3
The close holds, and so does the weighing. The step
`the check lines rules.py did not read` runs `rules.py --check` and turns
each `seal rules: not read:` line into a `::notice` at its file and line.
The step never fails (`.github/workflows/hygiene.yml:167-175`, read). It
matches the output format `check` prints
(`.github/scripts/rules.py:372-376`, read). It runs on the job's full
checkout, under the `python3` the earlier steps use. Over this tree it
exits 0 and prints nothing, and `rules.py --check` takes 0.45 s with all
265 check lines held (executed). The pin runs the step's own shell over a
tree with a near line and a refused line, and checks the whole notice
(`tests/behaviour/test_release_hygiene.py:1343`). With `|| true` removed
by `Edit`, the pin failed (executed). The `broad_gate.py#PARTITION` row
gives the step's reason for having no arm, and the step-count pins moved
by one (`skills/verify/scripts/broad_gate.py:2233-2239`, read). The fix
pass answered *What it removes*. Read against the rule, its answer holds:

- The step replaces a mechanism with a report. Before this work, a near
  `check:` line was a refusal that failed the suite. The core says a
  reading guessed from words is reported, never used to block. So the
  refusal could not stay as a refusal. Without the step, its report
  reaches nobody, because the suite's capture drops it.
- The step's cost is one report-only run per pull request, one `PARTITION`
  row and the step counts.
- The sed pattern spells `rules.py`'s output prefix a second time. That
  second spelling is not kept beside the tree unchecked. The pin runs the
  real command through the step's real shell, so a change to the prefix
  fails it.
- Not every rejected home was checked. The xdist claim, that a notice
  printed from the test step might not reach the log, was not tested. No
  verdict rests on it, because the other homes it was weighed with reach no
  straight-to-the-PR change.

The gaps row is closed in `closed` exactly, and `seal unverified` reads it
as closed (executed).

confirms: none
`59beac2a` builds what `frame/design.md` *Scope* item 3 says the bullet
gains (`CONTRIBUTING.md:386-394`, read). The sentence holds for both
instances it names. In round 4, an `original:` line was named where no
arm reads one. In round 6, finding 2 named a heading inside the section
where the parser reads it as a line. The `docs:` prefix holds by this
repository's convention at this base. The base's own log uses `docs:` for
commits that change only `CLAUDE.md` or `CONTRIBUTING.md`, such as
`51eca3ac`. The commit touches `CONTRIBUTING.md` alone (executed,
`git log` over the base and `git show --stat`). #1199's rule is not on
this base.

confirms: none
The orchestrator's fold at `2b7eef28` states what the fixes built.
*Scope* item 7, the near-heading scenario, the *Removes* row and Table A's
`seal settle` row now say three things. A near heading outside the
section is named. One below level 2 inside it is a line of the section. A
design with a named line is read whole at the settle. Table A's `seal rules --check` row names the hygiene step and
"each pull request" (`frame/design.md:50`, `:83`, `:295`, `:298`, `:324`,
read). The design's `## Rule changes` parses with 22 operations, no error
and no line in `unread` (executed, `rule_changes.parse` at `2b7eef28`).
The fix pass's answers commit, `e768e535`, changes three `verdict:` lines
and three `answer:` lines of `round-6.md` and nothing else (read).

confirms: none
Each new test was read against its group. `seal layout --pairs` names no
pair in `tests/skills/test_settle.py`, `tests/skills/test_rule_changes.py`,
`tests/behaviour/test_release_hygiene.py` or
`tests/behaviour/test_the_gate_names_every_step_ci_runs.py` (executed).
Each mutant above failed only the new case of its group. The rewritten
`test_a_near_miss_of_the_heading_is_another_section_named_at_its_line`
passed under both `rule_changes.py` mutants, so it covers the heading
outside the section and the new case covers the heading inside it. The six
modules the fix diff touches pass at `2b7eef28`: 281 passed, exit 0
(executed). That run is a narrow probe and not the broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and `seal gate` over the branch; the fix pass's 2,938 and 2,750 boundary counts were not re-run, and this round ran six modules only | the branch at `2b7eef28` | the orchestrator, by `seal gate --base release/v0.26.0 --record` after the rounds settle |
| How GitHub renders the new step's `::notice` lines in a pull request's annotations; the pin holds the text printed, not the rendering | `.github/workflows/hygiene.yml:171-175` | the orchestrator, at the first CI run of the pull request |
| The closing memo's row on *Judgments of the run* ends "and this work item's own plan holds no such section", while `frame/plan.md:73` holds that section with ten rows. Phase 5 wrote the row at `967bc53c`, when the clause was true, and `e71bbaea` added the section and left the row (executed, `git log -S`). Both units are outside this fix diff. The paste-ready fix: delete that clause and the `, and` before it, so the first cell ends "nothing reads at the pull request whether a row was written" | `seal/threads/1793411151-judgment-where-meaning-is-the-question/gaps.md:12` | round 9, which reviews phase 5 and `e71bbaea` |
| The fix pass's `seal mutate` counts; this round reproduced four mutants by `Edit`, one for each changed reader and one for the step | `skills/settle/scripts/settle.py`, `skills/settle/scripts/rule_changes.py`, `.github/workflows/hygiene.yml` | the sealer, at the guarantee's sample of the crafter's claims |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_rule_changes.py tests/skills/test_settle.py tests/behaviour/test_release_hygiene.py tests/behaviour/test_the_gate_names_every_step_ci_runs.py tests/behaviour/test_one_word_one_meaning.py tests/github/test_rules.py -q -n auto`, in a `git clone --no-local` at `2b7eef28` under the scratchpad, deleted after | 281 passed, exit 0 |
| The same clone with `timeline`'s `elif found.unread` arm switched off and `inside` read to the document's end, both by `Edit`, the new and rewritten near-heading cases by `-k`, then restored | 3 failed: the settle case and both parameters of the inside case; 12 passed |
| The same clone with `and n not in inside` removed, and the step's fallback to `true` removed, both by `Edit`, the same cases and the step's pin by `-k`, then restored | 3 failed: both parameters of the inside case and the step's pin; 13 passed |
| `bin/test tests/skills/test_tmp_round7.py -q -s -p no:xdist -p no:cacheprovider`, a probe of six designs through `rule_changes.parse`, run once and deleted | 5 passed, 1 failed on the probe's own line arithmetic: it expected line 10 for the near heading of the both-headings design, and the parser named line 11, the heading's real line. That design parsed with no error, one operation and the near heading in `unread`. The `- nothing` design parsed as the no-change block, with the near heading in `unread`. The near heading alone gave `ops` None and no error. A level-3 heading inside the section was refused at its line as a line outside an item, with `unread` empty. One after an item was refused at its line, with `unread` empty. A level-1 near heading below the section was named, and the section's one item was read |
| `bash -eo pipefail -c` over the step's two `run:` lines, then `python3 .github/scripts/rules.py --check`, same clone | the step exits 0 and prints nothing; `rules.py` exits 0 in 0.45 s: "all 265 check lines in 54 rule files hold" |
| `grep -rn "rules.py\|seal rules" .github/workflows/`, round 6 finding 3's search re-run | the new step's lines at `hygiene.yml:167-175` |
| `bin/seal unverified` over the closing memo, same clone | 7 open, 1 closed, 0 unreadable; the closed row is finding 3's |
| `bin/seal layout --pairs`, same clone | 128 pairs, none in the four test modules the fix diff changed |
| `git log -S` on "holds no such section" over `gaps.md` and on "## Judgments of the run" over `frame/plan.md` | `967bc53c` wrote the row; `e71bbaea` added the section (the `## Not judged` row for round 9) |
