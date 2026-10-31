# Review round 6: 1793411151-judgment-where-meaning-is-the-question

target: ce2bc211 against release/v0.26.0

This round reads phase 3 alone: `7106857a..ce2bc211`, the four `feat:`
commits for *Scope* items 6 to 9, the `test:` commit `9701ff87` and the
records commit. It is the first finding round over phase 3. It reads
nothing of phases 4 and 5, which are not built.

Carried from rounds 3 to 5, not re-derived: where `unread`, `annotate` and
the `notices` list stand in `chain_check.py#main`, and that the check
prints a notice as a `::notice` annotation in CI. Round 5's `## Not judged`
row on departure e named this round as its answerer, and the fourth
confirmation below answers it. Re-derived this round: every verdict, the
naming scope of each new reader against where that reader reads its form
(round 4's regression came from a naming wider than the reading), and the
plan's five modules at `ce2bc211`. The repository declares no
`seal/parity.md`, so this record holds no `original:` line.

## Findings

### 1. A design holding `## Rule changes` and a heading near it loses the near section at the settle, and nothing there names it

severity: should
location: `skills/settle/scripts/settle.py:518-526`, `skills/settle/SKILL.md:180-181`, `tests/skills/test_settle.py`
evidence: executed `bin/test tests/skills/test_tmp_round6.py -q -s -p no:xdist`
verdict: fixed 5387ce4e

*Scope* item 7 names the near heading in the parse result "so
`chain_check.py` prints it and passes, and the settle's dry run lists the
design among those to read whole". The phase record claimed that the
dry-run clause held before the phase by another path, and that `settle.py`
needed no change. That holds only for a design that holds the near heading
alone. The probe parsed two designs that hold both headings:

- `## Rule changes` holding one `change`, then `## Rule Changes` holding
  another, parses with `errors` `[]`, one operation, and the near heading
  in `unread`.
- `## Rule changes` holding `- nothing`, then `## Rule Changes` holding a
  `change`, parses as the no-change block ("no rule"), with the near
  heading in `unread`.

`timeline` reads `errors` and `ops` and never `unread`
(`skills/settle/scripts/settle.py:518-526`, read). So the first design
joins a group with one of its two changes. The second is listed under
"nothing to write". Before this phase the near heading was a parse error,
and the dry run listed both designs to read whole. The phase turned that
into a silent drop in the one reader that writes the policy root. The
pull request's notice is the only place the heading is named, and the
check passes beside it. The core sentence phase 1 wrote says a script
names such a line and decides nothing on it. Here the settle decides that
the design has nothing more to write. `parse` is right to read the exact
section beside the near one
(`test_a_near_miss_of_the_heading_is_another_section_named_at_its_line[beside-the-heading]`).
The settle is the reader that has to show the line.

```python
        found = rules.parse(text, policy)
        if found.errors:
            whole.append((work_item_id, *found.errors[0]))
        elif found.unread:
            # A line the reader did not read can hold a rule change the
            # groups would drop, so the design is read whole, with that line.
            whole.append((work_item_id, *found.unread[0]))
        elif found.ops is None:
            whole.append((work_item_id, 0, NO_SECTION))
```

```markdown
- **The designs to read whole**: one whose `## Rule changes` does not parse,
  with the reader's reason, one with no such section, and one in which the
  reader names a line it did not read, a heading near `## Rule changes`
  among them, with that line and its reason.
```

The case goes in `tests/skills/test_settle.py`: two released designs, one
with both headings and two items, one with `- nothing` under the exact
heading and an item under the near one. The dry run lists each among the
designs to read whole with the near heading's line. It is seen red against
`ce2bc211`, where the first joins a group and the second is listed under
nothing to write.

answer: The finding holds. Read against its grounds, the paste holds: a design with `unread` is read whole, and `errors` stays first. A near block line comes only with an items error, so it never reaches the new arm alone. A near-only design now lists the heading's line and reason in place of "no `## Rule changes` section", which says more and changes no listing. `5387ce4e` applies the `timeline` arm and the skill's dry-run bullet as written, and rewrites `timeline`'s docstring and the module docstring in place. `test_lists_a_design_with_a_line_its_reader_did_not_read_to_read_whole` in `tests/skills/test_settle.py` holds both designs. It was red at `6cec9edf`: alpha grouped with one change, beta listed under nothing to write (executed). With the arm switched off by `seal mutate`, the case is red (executed). Other statements, found by `git grep` on "read whole", "to read whole" and "another section" outside `seal/threads` and `docs/`: `settle.py`'s two docstrings, changed; `skills/settle/SKILL.md:87` and `:210`, which still hold; `README.md:267`, which names the list and not its members, and stands. `frame/design.md` *Scope* item 7, Table A's `seal settle` row inside the `add` for `docs/what-a-script-gates.md`, and the *Removes* row state the near heading without the read-whole arm. The frame is not this pass's to edit, so the hand-back names them.

### 2. A level-3 heading near `## Rule changes` inside the section is named as another section whose lines were not read, while the parser reads them

severity: should
location: `skills/settle/scripts/rule_changes.py:116-121`, `skills/settle/SKILL.md:88-95`, `tests/skills/test_rule_changes.py`
evidence: executed `bin/test tests/skills/test_tmp_round6.py -q -s -p no:xdist`
verdict: fixed 6cec9edf

The probe parsed `## Rule changes`, then `### rule changes`, then a
`change` item. It returned the error `a line outside an item` at line 5,
and at the same line the `unread` entry "so it is another section and
none of its lines were read". The section runs to the next heading of
level 2 or higher (`skills/settle/scripts/rule_changes.py:131`, read). A
level-3 heading inside it is therefore a line of the section, and the lines
under it are read as items. The notice says the opposite of what the
parser did. This is round 4's class. The naming covers every heading at
any level. The reader treats a heading as another section only outside the
exact section's span, or at level 2 or higher. The refusal at the same
line is right. The orchestrator reads both lines at the preflight, so the
false one is a sentence somebody acts on. The skill's bullet says the same
false thing ("A heading at any level ... is another section").

```python
    found = [(n, lv) for n, lv, t in marks if lv == 2 and t == HEADING]
    # A heading below level 2 inside a section is a line of that section,
    # read and refused as the items refuse it, so it is not named.
    inside = set()
    for s, _ in found:
        e = next((n for n, lv, _ in marks if n > s and lv <= 2), len(lines))
        inside.update(range(s + 1, e))
    unread = [
        (n + 1, NEAR_HEADING.format(written=lines[n].strip(), heading=HEADING))
        for n, lv, t in marks
        if letters(t) == letters(HEADING)
        and (n, lv) not in found
        and n not in inside
    ]
```

In `skills/settle/SKILL.md`, the bullet's second sentence reads: "A
heading whose letters, case folded, are those of `Rule changes`, that is
not that heading and that stands outside the section, is another section:".
A case in `tests/skills/test_rule_changes.py` pins `unread == []` and the
refusal at the heading's line for the nested heading. It is seen red
against `ce2bc211`.

answer: The finding holds. Read against its grounds sentence, the paste holds: each span ends at the next heading of level 2 or higher, the same `end` the parser computes. `6cec9edf` applies it, as `inside` over each exact heading's span. It rewrites the skill bullet in place to "that stands outside the section" and adds that a heading below level 2 inside the section is a line of it, refused as any line outside an item is. `parse`'s docstring and `chain_check.py`'s arm line change the same way. `test_a_near_heading_inside_the_section_is_a_line_of_it_and_not_named` was red at `ce2bc211` (executed). Phase 3's own case `test_a_near_miss_of_the_heading_is_another_section_named_at_its_line[beside-the-heading-### Rule changes]` had pinned the wrong reading, because it put the level-3 heading inside the section. It now puts the near heading above the section, outside at every level. `seal mutate` (executed): dropping `n not in inside` is red. A span read to the document's end survived the first draft, so `edf90008` adds the same heading under `## Open questions`, below the section's end, and that mutant is then red. Other statements, by `git grep` on "another section" and "at any level": the skill bullet, `parse`'s docstring and `chain_check.py:34`, all changed. `frame/design.md` *Scope* item 7, the scenario table's row and Table A's `seal settle` row say "a near heading ... is another section" with no scope, and the hand-back names them for the orchestrator.

### 3. The `not read:` lines of `seal rules --check` reach nobody at a pull request, and the answerer the gaps row names has no step that reads them

severity: should
location: `tests/github/test_rules.py:636-637`, `.github/workflows/hygiene.yml:169`, `seal/threads/1793411151-judgment-where-meaning-is-the-question/gaps.md:9`
evidence: executed `grep -rn "seal rules\|rules.py\|test_rules" .github/workflows/`, `git grep -n -i "seal rules\|rule file\|check: line\|check line" -- agents/proofer.md skills/code-review/SKILL.md skills/code-review/orchestration.md`
verdict: fixed c4e91dd2

The gaps row claimed that the proofer answers, at review of each diff that
touches a rule file. Found: CI runs the check only inside
`test_every_check_line_in_the_tree_holds`. That case reads
`capsys.readouterr()` and drops the output when the exit is 0
(`tests/github/test_rules.py:636-637`, read). No workflow runs
`rules.py`: the grep printed nothing. Before this phase a near check line
was exit 1, and the suite went red. Now the line is printed into a
capture that nobody sees. Frame Table A's row says the check "names a near
line as not read". A name nobody can read is the silent pass the core's
rule removes.

The named answerer does not hold as a home, for three reasons:

- `agents/proofer.md` and `skills/code-review/SKILL.md` give the proofer
  no step that reads a rule file for a near check line. The grep found
  only `agents/proofer.md:104`, which names `seal rules --check` for a
  target that is gone.
- A straight-to-the-PR change has no proofer.
- The row leaves with this work item's directory at the settle, so the
  proofer of a later diff never reads it.

`chain_check.py`'s `not read:` lines reach the pull request as notice
annotations. This reader's lines can reach it the same way, through the
report-not-gate step pattern that `hygiene.yml` already uses for the two
READMEs.

```yaml
      # A report, not a gate: `seal rules --check` gates inside
      # `tests/github/test_rules.py`, whose capture keeps its output, so the
      # check lines it did not read are printed here as notices (#1167).
      - name: the check lines seal rules did not read
        shell: bash
        run: |
          out=$(python3 .github/scripts/rules.py --check) || true
          printf '%s\n' "$out" | sed -n 's/^seal rules: not read: \([^:]*\):\([0-9]*\): /::notice file=\1,line=\2::not read: /p'
```

Preconditions: the step runs at the checkout's root, and `rules.py --check`
reads the repository the current directory is in. `rules.py` imports only
the standard library and the tree's own modules
(`.github/scripts/rules.py:56-62`, read). The system `python3` runs it at
exit 0 over this tree (executed). `|| true` is there because the refusal is
the suite's to gate, and this step only reports. The step goes before
*both READMEs move together*. A case in
`tests/behaviour/test_release_hygiene.py`, which already reads
`hygiene.yml`, holds the step's command (contract rule 14). The gaps row is
then closed with the commit.

answer: The finding holds, and the step is built, weighed against `skills/core/SKILL.md` *The rule a mechanism is kept against*. It removes no mechanism. It carries the report of the reader that replaced the near-line refusal. Without it, item 8 amounts to `frame/plan.md` A2, nets removed with no report, which the frame rejected. Cheaper homes were weighed and none reaches every pull request. The proofer has no step that reads a rule file for near lines. A straight-to-the-PR change has no proofer. The gaps row leaves at the settle. The suite case drops its capture. A `::notice` written from the test step would pass through pytest-xdist's workers, which nothing here showed reaching the log. `chain_check.py` ships to users' repositories, whose rule files are not this plugin's globs. Its price is one `python3` run per pull request, report-only, plus one `broad_gate.py#PARTITION` row with its reason. Adding a step moves the partition's pinned step counts (`tests/behaviour/test_the_gate_names_every_step_ci_runs.py`), and those changed in the same commit. The paste's YAML was applied with two changes. First, the step is named `the check lines rules.py did not read`: the paste's name put the bare word `seal` into `broad_gate.py`, which `test_one_word_one_meaning.py#test_the_gate_calls_its_run_no_seal_by_construction` refuses (executed, red, then folded into `c4e91dd2` before it left the clone). Second, the pin runs the step's own shell, taken out of `hygiene.yml`, over a tree holding a near line and a refused line. It reads the whole notice and exit 0 in place of matching the command's text. `seal mutate` over `hygiene.yml` (executed): the step renamed, `|| true` dropped, and the notice without file and line are each red. The gaps row is closed in the same commit. Other statements: `skills/settle/SKILL.md` *What this plugin checks* describes the shipped command and not this repository's CI, so it stands. Table A's `seal rules --check` row (`Runs at: the suite`) is the frame's, named in the hand-back.

## Confirmations

confirms: none
Item 9's reading that `Closed` and `CLOSED` are open rows holds. The
crafter claimed it removed the whole near-closed branch, so a row opening
`Closed`, `CLOSED`, `closed.` or `closed:` is open. The code reads a closed
row only where the first word is `closed` exactly
(`skills/verify/scripts/unverified_check.py:811-823`, read). Item 9's
heading says "reads `closed` exactly", and its body calls the open reading
"the safe direction". The base comparison counts rows and not their kind
(`unverified_check.py:1627-1637`, read), so the reading moves no count.
The row is printed with its text as an open row (`unverified_check.py:1601`,
read). `skills/implement/SKILL.md:449-450` says the silent direction is
"still open". The row is read, as an open row, so the core's duty to name a
line the tool did not read does not reach it.

confirms: none
The one `NEAR_NOTHING` use that stays, in the base-revision reading,
holds. The frame's *Removes* row cites `:717` among the coordinates of
"`NEAR_NOTHING`'s refusal". At `f80f48e6`, line 717 is the base reading
and not a refusal (executed, `git show f80f48e6:skills/verify/scripts/unverified_check.py`).
Item 9's text names the refusal alone. The grounds are beyond the
crafter's account:

- `test_accepts_what_a_base_revision_wrote_before_the_word[the old line]`
  pins the base reading beside the old mark and the old column
  (`tests/skills/test_unverified_check.py:1052-1070`, read).
- Removing the base reading alone would turn a legacy base memo into a
  "cannot be read" entry of `open_record_rows`, and `seal settle --apply`
  refuses on such an entry (`unverified_check.py:1325-1350`, read).

The frame's `:717` is a coordinate the frame mis-cites. That is no defect
of the build.

confirms: none
The naming of a near no-change block in `rule_changes.py#parse` holds as
contract rule 12's class. Both readers reach the block through
`nothing_block` (`skills/settle/scripts/rule_changes.py:165`,
`unverified_check.py:735`, read), so the refusal left both readers at once.
In `## Not verified` the naming rides in the refusal
(`unverified_check.py:742-748`). In `## Rule changes` it goes to `unread`
beside the items' refusal (`rule_changes.py:169-173`). Both are pinned:
`test_a_line_that_opens_like_the_block_is_named_beside_its_refusal`
(`tests/skills/test_rule_changes.py:362`) and
`test_refuses_a_section_holding_the_old_line_and_names_the_line`
(`tests/skills/test_unverified_check.py:1179`). `skills/settle/SKILL.md:79-85`
states both readers in place.

confirms: none
Phase 2's departure e is closed, which answers round 5's `## Not judged`
row. `rule_changes_read` and `rule_changes_of` take `notices`
(`skills/code-review/scripts/chain_check.py:1662-1700`, read). `main`
passes the list at both calls (`chain_check.py:2401`, `:2417`). The
notices come from the same `parse` call as the refusals, so the arm names
a line only in a design it reads. With the judged call's `notices`
removed, two of the three near-heading cases failed (executed). The third,
the edited spec of another work item, goes through the second call, and
the crafter's mutant of that call covers it.

confirms: none
Item 7's claim that the dry run held before the phase holds for a design
that holds the near heading alone. The probe's near-only design parsed
with `ops` None and `errors` `[]`, which `settle.py:521` lists to read
whole as `NO_SECTION` (executed). Finding 1 is the design this claim does
not cover.

confirms: none
Each other new naming covers the scope its reader reads, and round 4's
class does not recur outside finding 2:

- `near_headers` walks `config.unfenced`, as `first_table` and `gfm_table`
  do (`skills/verify/scripts/pact_check.py:333-370`,
  `hooks/lib/config.py:239`, read). It runs only over the frames
  `anchor_files` reads.
- `unread_lines` and `check_lines` walk the same `shown_lines` and
  `visible` flag over the same `rule_files` (`.github/scripts/rules.py:162-181`,
  read).
- `unread_block` names a line only on the working tree's path. The base
  path returns before it (`unverified_check.py:732-748`, read).

confirms: none
Each new test is read against its group. `seal layout --pairs` names one
pair: `test_a_line_not_read_is_printed_as_one_and_holds_nothing` and
`test_a_heading_that_opens_like_a_check_line_is_printed_under_itself` in
`tests/github/test_rules.py`. With `render`'s heading-branch naming
removed, only the second failed (executed). It covers a branch that the
first does not reach. The crafter claimed the same, and that claim is
reproduced. The three scenarios of phase 3 that the plan names each have a
case asserting the scenario's exit and text: the near pact header
(`test_names_a_table_under_a_near_header_and_grades_none_of_it`), the
`Check:` line (`test_names_a_line_that_opens_like_one_and_is_not_one_at_exit_0`)
and the `closed.` row (read). A fourth case covers the near
`## Rule Changes` heading
(`test_names_a_near_heading_as_not_read_and_passes`).

confirms: none
The plan's five modules pass at `ce2bc211`: 844 passed, exit 0. Over this
tree, `seal rules --check` reads 265 check lines in 54 rule files, all
hold, and it names no line (executed). The crafter's `seal mutate` counts
were not re-run whole. One mutant each was reproduced for `chain_check.py`
and `rules.py`, and each failed. A mutation score licenses *tested*, never
*safe*.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and `seal gate` over the branch, labelled `unverified` in `gaps.md` | the branch at `ce2bc211` | the orchestrator, by `seal gate --base release/v0.26.0 --record` after the rounds settle |
| The crafter's `seal mutate` counts for `rule_changes.py`, `unverified_check.py` and `pact_check.py`; this round reproduced one mutant each for `chain_check.py` and `rules.py` only | `trail/phases/phase-3.md` *Mutation* | the sealer, at the guarantee's sample of the crafter's claims |
| `.test_durations` still holds keys for cases this phase renamed, such as `Test_nothing_block::test_refuses_a_near_miss_and_a_second_item`; whether `pytest-split` passes over a stale key without moving a shard | `.test_durations:5321-5324` | the orchestrator, at the broad run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_round6.py -q -s -p no:xdist`, a probe of four designs through `rule_changes.parse`, in a `git clone --no-local` at `ce2bc211` under the scratchpad, deleted after | 4 passed. Both headings with an item each: `errors` `[]`, 1 operation, the near heading in `unread` (finding 1). `- nothing` under the exact heading with an item under the near one: the no-change block, the near heading in `unread` (finding 1). The near heading alone: `ops` None, `errors` `[]`, the heading in `unread`. `### rule changes` inside the section: `a line outside an item` at line 5, and line 5 in `unread` as another section (finding 2) |
| `bin/test tests/skills/test_pact_check.py tests/skills/test_rule_changes.py tests/github/test_rules.py tests/skills/test_unverified_check.py tests/skills/test_chain_check.py -q -n auto`, same clone | 844 passed, exit 0 |
| The same clone with `notices` removed from the judged call at `chain_check.py:2401` by `Edit`, `-k near_heading` over `tests/skills/test_chain_check.py`, then restored | 2 failed, 1 passed |
| The same clone with the naming removed from `render`'s heading branch in `.github/scripts/rules.py` by `Edit`, the two paired cases by `-k`, then restored | 1 failed, the heading case; 1 passed |
| `python3 .github/scripts/rules.py --check`, system interpreter, same clone | exit 0; "all 265 check lines in 54 rule files hold", no line named |
| `bin/seal layout --pairs`, same clone | one pair, the two `render` cases of `tests/github/test_rules.py` |
| `grep -rn "seal rules\|rules.py\|test_rules" .github/workflows/` | no line (finding 3) |
