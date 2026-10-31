# Review round 9: 1793411151-judgment-where-meaning-is-the-question

target: 85874df5 against release/v0.26.0

This round has three jobs, as the spawn prompt narrows them. First, it
verifies round 8's close: the fix range `458645e2..788e866e`, which holds
`7f69767f`, `bce21a12`, the answer `7bc2132f` and the frame fold
`788e866e`. Second, it reviews phase 5 as new work, `3904967e`,
`f9edc0b2`, `5a7a5ce0`, `9310a2de` and `967bc53c`, against
`frame/design.md` *Scope* items 11, 12 and 14, the `## Rule changes` items
those carry, the scenario "The settle reads the judgments" and
`frame/plan.md` A5, A8d and A14. This is phase 5's first finding round.
Third, it reads two units as code: `85874df5` (the test-layout fix) and
`e71bbaea` (the orchestrator's ten rows in `frame/plan.md` *Judgments of
the run*). Round 6's fix commits (`6cec9edf`, `5387ce4e`, `edf90008`,
`c4e91dd2`, `59beac2a`), their answer `e768e535` and the fold `2b7eef28`
belong to round 7, which runs at the same time, and were not read.

Carried from round 8 and not established again: where `runners_in` and
`read` stand in `skills/verify/scripts/deferral_check.py`, and the class
of eight characters `str.splitlines` breaks at and YAML 1.2 does not.
Re-established here: every verdict, and the eight-row case red against the
tool before the fix.

The spawn prompt and `967bc53c`'s phase record were read as claims. One
claim did not hold. `trail/phases/phase-5.md:93-94` says `routing.rounds`
raises on a `trail/rounds` that is a file. It does not: `hooks/lib/routing.py:599-609`
catches `NotADirectoryError` and returns `[]`, which is finding 1. The
others held where this round opened them: plans read from the working tree,
the blank template row skipped, the procedure's step 3 extended rather than
a step added, and `skills/implement/SKILL.md`'s plan row corrected under
contract rule 19.

## Findings

### 1. `seal settle`'s dry run prints `0 rounds` for a work item whose `trail/rounds` is a file holding its review, and its own branch for that case is dead

severity: should
location: `skills/settle/scripts/settle.py:537-540`, `skills/settle/scripts/settle.py:860-864`, `tests/skills/test_settle.py`
evidence: executed `bin/test tests/skills/test_tmp_round9_probe.py -q -s -p no:xdist --basetemp=../basetemp`
verdict: fixed 604ec0e8

Claimed, in `trail/phases/phase-5.md:92-94`, that `routing.rounds` raises
on a `trail/rounds` that is a file, and that this branch has no case.
Found: `settle.py:537-540` catches `NotADirectoryError` around
`routing.rounds`, but `routing.rounds` catches that error itself and
returns `[]` (`hooks/lib/routing.py:599-609`, read). So the `except` never
runs, and `rounds` is never `None`. The report's other branch,
`its trail/rounds is a file, so no round was counted` at `settle.py:863`,
is never printed. The probe wrote a released work item whose
`trail/rounds` is a file holding `# Review round 1` and whose plan holds a
judgment. The dry run printed `1700000001-a  0 rounds` (executed).

It matters because the dry run reports a review as never having happened
while git carries its text. `hooks/lib/routing.py:557-566` says this is
"the one direction this module refuses". It also provides
`rounds_unreadable` (`routing.py:611-645`) so that a caller can tell the
two apart. The class is every shape `rounds_unreadable` returns true for:
a file, any link, and a directory nothing can list. All three read as
`0 rounds` today, and the fix below covers all three. The settling session
reads the round count beside each judgment to weigh what the run cost
(`skills/settle/SKILL.md:187-193`), so a false `0` is a wrong number that
it acts on.

The fix, in `skills/settle/scripts/settle.py`. It reads the working tree
at `records` and assumes nothing else: `rounds_unreadable` reads only
`os.path` and `os.listdir`, and a link is reported whatever it resolves
to.

```python
        where = under(records, f"{SPECS}/{work_item_id}")
        # `routing.rounds` returns [] both for no record and for a
        # `trail/rounds` it cannot list; `rounds_unreadable` says which.
        rounds = (
            None if routing.rounds_unreadable(where) else len(routing.rounds(where))
        )
```

and at `:863`:

```python
                    else "its trail/rounds is not a directory this can list, "
                    "so no round was counted"
```

The `judgments` docstring at `:506-508` says "or None where that is not a
directory this can list". The case, in `tests/skills/test_settle.py`
beside `test_a_judgments_section_it_cannot_read_is_named_and_refuses_nothing`,
was seen red here at `85874df5`, where the dry run printed `0 rounds`:

```python
    def test_a_work_item_whose_rounds_cannot_be_listed_is_not_counted_as_none(
        self, repo, capfd
    ):
        """A `trail/rounds` that is a file holds a review git carries, so
        the dry run says it counted none rather than that none happened."""
        item(repo, "1700000001-a", "- nothing\n  why: x.")
        (specs_dir(repo, "1700000001-a") / "frame" / "plan.md").write_text(
            "# Implementation Plan: a\n\n## Judgments of the run\n\n"
            "| Date | Judgment | Grounds | Judged against |\n|---|---|---|---|\n"
            "| 2026-10-01 | x | y | z |\n",
            encoding="utf-8",
        )
        trail = specs_dir(repo, "1700000001-a") / "trail"
        trail.mkdir()
        (trail / "rounds").write_text("# Review round 1\n", encoding="utf-8")
        commit(repo, "a")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert (
            "    1700000001-a  its trail/rounds is not a directory this can "
            "list, so no round was counted\n"
        ) in text, text
        assert "0 rounds" not in text, text
```

answer: Fixed as the round grounds it, in my own case. `judgments` asks `routing.rounds_unreadable` and counts only where it is false, the report prints "its trail/rounds is not a directory this can list, so no round was counted", and the docstring names the file, the link and the unlistable directory. The case is parametrised over a file and a link to a directory holding `round-1.md`, and asserts no count line at all rather than only "0 rounds", so a link that would read as "1 round" is caught too; both rows were seen red at `5b1dc057`, printing `0 rounds`. The unlistable directory has no case, since `chmod 000` does not bar a root runner. `seal mutate` with the call reverted to `len(routing.rounds(where))` went red. `skills/settle/SKILL.md` *What the dry run shows* and the fragment now say the count is replaced by a name in that case. My `trail/phases/phase-5.md` claim that `routing.rounds` raises on a file, and that the branch only lacked a case, was wrong: it catches `NotADirectoryError` and returns `[]` (`hooks/lib/routing.py:599-609`), so the branch was dead; this line corrects that record, which a fix pass does not edit.

### 2. `seal settle`'s dry run says nothing of a plan whose judgments stand under `## Judgments of the Run` or any other near heading, and `--apply` then removes the rows unread

severity: should
location: `skills/settle/scripts/settle.py:524-526`, `skills/settle/SKILL.md:190-191`, `seal/threads/1793411151-judgment-where-meaning-is-the-question/changelog.md:3`, `tests/skills/test_settle.py`
evidence: executed `bin/test tests/skills/test_tmp_round9_probe.py -q -s -p no:xdist --basetemp=../basetemp`
verdict: fixed 604ec0e8

Claimed, in `3904967e`'s message and `skills/settle/SKILL.md:190-191`:
"a plan with no such section prints nothing, and a section whose table is
not under the exact header is named as not read". Found:
`settle.py:525` looks for a heading whose text is exactly
`Judgments of the run` and otherwise `continue`s, so it names nothing. The
probe wrote three released plans, each holding one judgment row under the
exact table header. Their headings were `## Judgments of the Run`,
`## Judgments Of The Run` and `## judgments of the run`. The dry run
printed no line for any of the three, exited 0, and its judgments block
held only a fourth plan's row (executed).

The core requires a script to name such a line. `skills/core/SKILL.md:121-126`
says a script "names as not read a line or a file that looks like one of
its form's and is not one". The frame lists `seal settle` among the checks
that gate, with *Judgments of the run* among what it reads
(`frame/design.md:298`). The same reader already follows the rule one
level down: a near table header is named (`settle.py:532-536`, and the
case at `tests/skills/test_settle.py:938`). `rule_changes.py#parse` names
a heading near `## Rule changes` the same way (`rule_changes.py:126-130`).
So within one reader a near header is named and a near heading is not.
Here the silence costs more than in a gate at the pull request. The dry
run is "the one reading the rows get" (`SKILL.md:192-193`), so a title-cased
heading, which a person writes by habit, loses every judgment of that run
without a word.

The scope where this reader reads the form is every live heading of the
plan, because `:525` scans them all for the exact one. So the fix names a
near heading anywhere in the plan outside a fence, and the fence is the
edge that takes a case. `rules.letters` is the comparison `parse` already
uses (`rule_changes.py:94-97`). It is a case fold and a letter filter
applied once, not a list of spellings. The fix, in
`skills/settle/scripts/settle.py`, with no OS precondition:

```python
# What the dry run says of a heading near the judgments section, at its line.
NEAR_JUDGMENTS = (
    "line {line}: `{written}` opens like `## {heading}` and is not it, so "
    "none of its rows were read"
)
```

```python
        lines = rules.reader().gfm_lines(text)
        marks = rules.headings(lines)
        unread += [
            (
                work_item_id,
                NEAR_JUDGMENTS.format(
                    line=n + 1, written=lines[n].strip(), heading=JUDGMENTS
                ),
            )
            for n, _lv, t in marks
            if t != JUDGMENTS and rules.letters(t) == rules.letters(JUDGMENTS)
        ]
        if not any(t == JUDGMENTS for _n, _lv, t in marks):
            continue
```

The sentence at `skills/settle/SKILL.md:190-191`, and its copy at
`changelog.md:3`, become: "A plan with no such section prints nothing. A
heading whose letters, case folded, are the section's and that is not it
is named as not read, and so is a section whose table is not under the
exact header." The `judgments` docstring at `settle.py:509-512` says the
same. The cases go in `tests/skills/test_settle.py` beside the one at
`:938`. The first was seen red here at `85874df5`, where no line was
printed:

```python
    @pytest.mark.parametrize(
        "heading",
        ["## Judgments of the Run", "## judgments of the run", "### Judgments Of The Run"],
    )
    def test_a_heading_near_the_judgments_section_is_named(self, repo, capfd, heading):
        item(repo, "1700000001-a", "- nothing\n  why: x.")
        (specs_dir(repo, "1700000001-a") / "frame" / "plan.md").write_text(
            f"# Implementation Plan: a\n\n{heading}\n\n"
            "| Date | Judgment | Grounds | Judged against |\n|---|---|---|---|\n"
            "| 2026-10-01 | x | y | z |\n",
            encoding="utf-8",
        )
        commit(repo, "a")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        block = text.split(f"\n{settle.JUDGMENTS_HEADING}\n")[1]
        assert block.startswith(
            "    1700000001-a  seal/threads/1700000001-a/frame/plan.md  not read: "
            f"line 3: `{heading}` opens like `## Judgments of the run`"
        ), block

    def test_accepts_a_near_heading_inside_a_fence_without_a_word(self, repo, capfd):
        fence = "`" * 3
        item(repo, "1700000001-a", "- nothing\n  why: x.")
        (specs_dir(repo, "1700000001-a") / "frame" / "plan.md").write_text(
            f"# Implementation Plan: a\n\n{fence}\n## Judgments of the Run\n{fence}\n",
            encoding="utf-8",
        )
        commit(repo, "a")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert settle.JUDGMENTS_HEADING not in text, text
```

Table A's `seal settle` row in `frame/design.md:298` names in its Unread
cell only what the reader does with `## Rule changes`. Once the fix lands,
the orchestrator folds the near judgments heading into that cell. This is
a row of `## Not judged`.

answer: Fixed within the scope the reader scans, every live heading of the plan. `judgments` names each heading whose `rules.letters` equal the section's and that is not it, as `line N: <heading> opens like ## Judgments of the run and is not it, so none of its rows were read` (`NEAR_JUDGMENTS`), before it looks for the exact section, so a plan holding both gets the line and its rows. The round's paste-ready code was read against its grounds and taken as written; its cases were rewritten so the parametrised one asserts the whole line, and its fenced edge kept. The three headings were seen red at `5b1dc057` with no line printed; the fenced case passes on both trees, as an edge does, and `seal mutate` with `rules.headings` replaced by a scan of raw lines that sees the fence went red on it. Five more mutants went red: the exact heading named too, every heading named, the letters test dropped, the naming dropped, the line number off by one. The module docstring, `skills/settle/SKILL.md` *What the dry run shows* and the fragment say it. Stale in the frame, for the orchestrator to fold: Table A's `seal settle` Unread cell (`frame/design.md:298`) and *Scope* item 12 (`frame/design.md:55`), whose "A plan with no such section prints nothing for it" now has the near heading and the unlistable `trail/rounds` beside it.

### 3. `gaps.md` says this work item's plan holds no *Judgments of the run* section, and since `e71bbaea` it holds one with ten rows

severity: should
location: `seal/threads/1793411151-judgment-where-meaning-is-the-question/gaps.md:12`
evidence: executed `git log --oneline -S "this work item's own plan holds no such section" -- seal/`, `git log --oneline -S "## Judgments of the run" -- seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/plan.md`
verdict: fixed 3b484a3c

Round 7 handed this line to this round as outside its fix diff (the
orchestrator's message, read). This round did not rest on that hand-off
and traced the line itself. `967bc53c` wrote the row's last clause, "and
this work item's own plan holds no such section", and it was true then.
`e71bbaea` added `## Judgments of the run` to `frame/plan.md:73-86` with
ten rows, and left the clause standing (both executed). Contract rule 19
asks the change that makes a sentence false to correct it in the same
commit.

The row is a `## Not verified` row, and the sealer, `seal unverified` and
the settling session read it as the state of the work item. Its question
is whether the orchestrator writes a row for each judgment. A reader told
the plan holds no section skips the ten rows that answer it in part. A
fold made after the table existed, `788e866e`, wrote no row, and that
question goes to the settling session through this row. That makes the
row's own claim matter more, not less.

The fix deletes the clause and leaves the rest of the row as it stands:

```markdown
| Whether the orchestrator writes a row of `frame/plan.md` *Judgments of the run* for each judgment of a run; nothing reads at the pull request whether a row was written | the settling session, at the dry run's judgments after 0.26.0 ships |
```

answer: Fixed as the round's paste-ready row gives it: the clause and the `, and` before it are gone, and the rest of the row stands (`3b484a3c`). The row's question stays open for the settling session, since nothing reads at the pull request whether a fold wrote its row.

## Confirmations

confirms: round-8#1
The close `fixed 7f69767f` holds. `runners_in` splits at `"\n"`
(`skills/verify/scripts/deferral_check.py:105`, read), after `read` opens
the file in text mode with universal newlines (`:153-158`, read), so CR
and CRLF arrive as LF. The fix pass's reason for not applying the round's
regex holds: the two other arms could not be reached. With
`deferral_check.py` checked out from `27dcf020`, all eight rows of
`test_a_step_is_printed_whole_where_a_comment_holds_a_break_yaml_does_not_take`
failed and 18 cases passed. Restored, the module passed 26 of 26
(executed). Each row asserts the whole output, so the step prints with its
comment. The CRLF and CR case passes at HEAD (executed). The stale census
exemption `# exempt from splitlines: YAML keys` is gone, and
`seal layout --check` exits 0 (executed). `bce21a12` renames the one
accepting case back to `test_accepts_` and leaves its body as it was
(read). `788e866e` rewrites `frame/design.md:28`, `:53` and the
`## Removes` row at `:328`. All three now say that the tab-indented block
closes with the scan and that U+2028 closes in `runners_in`. `:53` also
folds round 8's `## Not judged` row: it now says the tool "exits 1 only
where no CI file holds a runner" (read). `changelog.md:14` still holds as
written (read).

confirms: none
The rewritten guidance follows `skills/core/SKILL.md` *A rule is guidance
for a judgment, not a sequence to execute*. In
`skills/code-review/orchestration.md:132-151` the cap reads as the point
where the orchestrator weighs, with the four signals, what going on costs
and what stopping costs. The second regression on one unit is now a
signal the orchestrator answers with a written row (`:186`, read). The
invariant stays a sequence. "A regression's fix pass is owed one verifying
round whatever the count" names the core's invariants table as its reason
(`:144-146`, read). The records-only exception at `:104-111` matches the
table's "or by the sealer" cell (`skills/core/SKILL.md:101`, read).
*Orchestrator: the pull request opens once the sealer seals* is unchanged,
and *the order inside a ticket* gains one sentence and stays a sequence
(`skills/implement/orchestration.md:49-60`, read), as frame A14 asks. A
`git grep` for the old cap wording outside `docs/` and the records found
no statement left in the skills, agents, templates or READMEs. It found
only the pins in `tests/text/test_the_rules_have_one_owner.py`, which read
the policy root and go red at the settle as the plan's operational impact
says (executed).

confirms: none
The judgments reader reads its own form correctly. Over this work item's
plan, `settle.judgments` returned ten rows in nine groups. Their lines are
77 to 86, the plan's own lines, and no plan was unread (executed). The
shipped template, blank row and all, printed nothing (executed): the empty
row is skipped as `trail/phases/phase-5.md:39-44` says. The template puts
a blank line between its placeholder paragraph and the header, which
`hooks/lib/config.py#gfm_table` requires (`templates/records/sdd-plan.md:23-29`,
read). The narrow run over `tests/skills/test_deferral_check.py`,
`tests/skills/test_settle.py`, `tests/skills/test_unverified_check.py`,
`tests/behaviour/test_the_set_a_work_item_always_has.py`,
`tests/text/test_the_rules_have_one_owner.py`,
`tests/behaviour/test_every_orchestrator_act_names_its_delivery.py` and
`tests/behaviour/test_a_cited_section_stands_in_its_file.py` passed 567
cases (executed).

confirms: none
The ten rows of `e71bbaea` each hold a judgment, its grounds and a
document with a heading. Each `Judged against` cell names a section that
stands. Eight are headings (`git grep` of each, executed). The other two
cite the core's bold rule lead *Judgment is spent where meaning is the
question, and a script answers the rest* (`skills/core/SKILL.md:36`),
which `tests/behaviour/test_a_cited_section_stands_in_its_file.py:6`
accepts as a section. The grounds match the document they cite where this
round checked them. Row 4's "no verifying round" is the records-only
exception of `skills/code-review/orchestration.md:104-111`. Row 7's route
is the second row of the comparison table (`:185`). Row 10's grounds are
`docs/the-review-record.md:158-161`, which says round N's closes are named
by round N+1 (read). Row 1 gives grounds for three of its four proposals.
The fourth, the core's size against the hook's cap, has its grounds in
`frame/design.md:37` (read). Row 9's grounds, "The owner asked for
parallel work", have no coordinate in the work item; that is a row of
`## Not judged`.

confirms: none
`85874df5` holds. `test_refuses_a_verdict_line_inside_a_fence` covers
something its group does not. A mutant that made `verdicts_of` read
`reader.gfm_lines`, which blanks no fence, survived the other four cases
of `Test_verdicts_of` and turned the new case red (executed, `seal
mutate`). The existing fence case used `**Verdict:** withheld`, which
`verdicts_of` would not read even unfenced. The two `Test_unread_block`
cases changed their names and gained a docstring, and their bodies are
unchanged (read). `seal layout --check` exits 0, and `seal layout --pairs`
names no pair in `test_settle.py`, `test_deferral_check.py`,
`test_chain_check.py` or `test_unverified_check.py` (executed).

confirms: none
`5a7a5ce0` moves `.claude-plugin/plugin.json` to `0.26.0`, and
`marketplace.json` carries no version (read), as `frame/design.md` *Scope*
item 14 asks. `9310a2de` re-wraps the folded-decision paragraph and takes
the clause copied from the phase template out of `skills/implement/SKILL.md`'s
row, which leaves the clause in `templates/records/sdd-phase.md:5` and
`agents/crafter.md:60-62` (read). Both READMEs state the cap as the point
where the orchestrator weighs, and say where the decision is written
(read). `seal rules --check` exits 0 (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and `seal gate` over the branch, labelled `unverified` in `gaps.md` | the branch at `85874df5` | the orchestrator, by `seal gate --base release/v0.26.0 --record` after the rounds settle |
| The crafter's `seal mutate` run over `settle.py` (11 of 11 red) and its 114-module run (4,982 passed), not re-run whole here; this round ran the narrow modules and one mutant of its own | `skills/settle/scripts/settle.py`, the modules `trail/phases/phase-5.md:100-111` names | the orchestrator's broad run |
| `tests/skills/test_settle.py`'s judgments cases on Windows | `tests/skills/test_settle.py:808`, `:938` | the orchestrator, at the Windows legs of the pull request's CI run |
| Whether `788e866e`, which folded round 8's change to how the U+2028 misreading closes, owed a row of *Judgments of the run* under `skills/implement/orchestration.md:49-56` | `seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/plan.md:73-86` | the orchestrator, before it commits the records |
| Row 9's grounds, "The owner asked for parallel work where it is safe", name no coordinate this round could open | `seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/plan.md:85` | the orchestrator |
| Table A's `seal settle` row names in its Unread cell nothing the reader does with the judgments section, which finding 2's fix gives it | `seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md:298` | the orchestrator, by folding the cell after finding 2's fix |
| Round 7 reads round 6's fixes at the same time, and this record names none of round 6's findings | `trail/rounds/round-7.md` | the orchestrator, before it commits the records |

## Probes

| Command | Result |
|---|---|
| `tests/skills/test_tmp_round9_probe.py`, two cases, run once with `bin/test ... -q -s -p no:xdist --basetemp=../basetemp` in a `git clone --no-local` at `85874df5` under the scratchpad, then deleted with its temp directory | a released work item whose `trail/rounds` is a file printed `0 rounds` (finding 1); three plans under `## Judgments of the Run`, `## Judgments Of The Run` and `## judgments of the run` printed no line, exit 0 (finding 2); the shipped template printed nothing; this work item's plan gave ten rows in nine groups at lines 77 to 86 and no unread plan; the eight characters inside a step's comment exited 0 with a `ci` line opening with the step |
| `bin/test tests/skills/test_deferral_check.py -q -p no:xdist` with `deferral_check.py` checked out from `27dcf020`, then restored and run again | 8 failed (the eight rows), 18 passed; restored, 26 passed |
| `bin/test` over the seven narrow modules named in the third confirmation, `-q` | 567 passed, exit 0 |
| `bin/test tests/skills/test_chain_check.py -q -k "Test_verdicts_of or Test_unread"` | 5 passed, exit 0 |
| `bin/seal mutate skills/code-review/scripts/chain_check.py` with `verdicts_of` reading `reader.gfm_lines`, against `Test_verdicts_of` without the new case, then against the new case alone | survived the four; red on `test_refuses_a_verdict_line_inside_a_fence` |
| `bin/seal layout --check`; `bin/seal layout --pairs`, filtered for the four modules; `bin/seal rules --check` | exit 0; no line; exit 0 |
| `git log --oneline -S` for the `gaps.md:12` clause and for `## Judgments of the run` in the plan | `967bc53c` wrote the clause; `e71bbaea` added the section (finding 3) |
