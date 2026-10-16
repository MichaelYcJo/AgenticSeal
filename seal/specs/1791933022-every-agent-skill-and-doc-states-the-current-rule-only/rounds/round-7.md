# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — review round 7

target: aa0c79a6, fixes e9baf154..aa0c79a6

Extended past round 6: round 6 found 1, round 5 found 2, and the frame took round 6's fix of a fix by redesigning the record from its jobs.

A verifying round over everything after round 6, part A only: the reframe
after round 6 (0a06aee4), its approvals, phases 5d-i to 5d-iv and the two
frame edits of 2026-10-16. Round 6's one finding reads `deferred the frame`,
so this round owes it no confirmation. The redesign holds where it was aimed.
The six records keep every verdict and ground, the template reads as one
open finding, every label spelling the spec lists is refused by line, and
the last record's `fixed` or `rejected` finding is refused as owing a
verifying round.

Five findings follow, in cause order. Findings 1 and 2 are the class round
6 found, one level down: the check reads two more person-written facts, a
coordinate and a heading's number, and a spelling it did not list falls to
a side instead of to a refusal. Finding 3 is the review skill ending a run
in a state the new last-record rule refuses. Finding 4 is the upgrade note,
which a user with a work item in flight cannot follow. Finding 5 is a file
the range did not touch that still states the old record.

Findings 1 to 4 sit in units these commits added or changed, and each is a
defect the redesign made, so each names round-6#1, the finding whose fix
made the unit. By `docs/the-review-record.md` §*The run*, this round then
gets no fix pass and the work item goes back to its framer. Finding 5 sits
in a unit the range did not change and names no earlier finding.

Findings from reading and from execution are labelled in each finding and
confirmation, and every command named there is in `## Probes`. The full
suite was not run. It is `unverified`, and the sealer answers it.

## Findings

### 1. A coordinate written `path#unit` reads as a path that ends in `#unit`, so the shape the spec refuses passes, and every `fixed` commit for such a finding is refused as touching nothing

severity: should
location: `skills/code-review/scripts/chain_check.py:140-141`, `evals/scripts/replay_targets.py:293-296`, `evals/scripts/rule_cases.py:280`, `tests/test_chain_check.py:442-478`, `evals/scripts/seed_defects.py:8`, `tests/test_a_rewritten_definition_proved_non_inferior.py:658`, `evals/behaviour/warden/`, `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/changelog.md:89`
verdict: fixed f5ba02f1
regression: round-6#1

The unit: `COORDINATE_ITEM` and `COORDINATE`, which cf9b116e added for
`location_of`, and the truth patterns 71fd384f moved onto the record's
location lines. `spec.md` §*What a round records* gives a coordinate three
shapes, `path`, `path:line` and `path:first-last`, and says a line the
check cannot read is refused by name. T33's docstring says anything else is
None. The path class `[^`\s:]*` admits `#`, so `` `a.py#unit` `` is read as
the path `a.py#unit`. A finding at `open` or `deferred <home>` with it
passes the shape. A finding at `fixed <commit>` is refused with "touches no
path its location names (`a.py#unit`): it changed `a.py`", which names the
file the fix did touch as the one it missed.

The spelling is not rare. It is this repository's coordinate kernel's, and
the eval graders a warden is measured by reward it: every replay and seeded
truth grader matches `path#(?:unit)` beside `path:line`, and
`rule_cases.py:280` does the same for `src/textutil.py#shout_twice`. So the
eval passes a warden for the spelling the check later refuses at a ready
pull request. This is round-6#1's class: a fact a person wrote, in a
spelling the reader did not list, read as something other than a refusal.

executed: `test_tmp_r7_probe.py` gives `location_of` of `` `a.py#unit` ``
and of `` `a.py#unit:3` `` as `['a.py#unit']`, and a finding with it at
`deferred #9` reads with no refusal. In a scratch repository, a `fixed`
commit that changed `a.py` is refused against `` `a.py#unit` `` and passes
against `` `a.py:1` ``. executed: the three T33 values below fail on the
shipped reader (exit 1, "assert ['a.py#unit'] is None") and pass with the
paste. With the paste, `tests/test_chain_check.py`,
`tests/test_broad_gate.py`, `tests/test_the_release_seal_is_drawn.py` and
`tests/test_the_seal_is_taken_once_by_the_sealer.py` pass (exit 0, 485
passed), and `chain_check.py` still reads the six records with the same
three owed lines. read: the two generator changes and the regenerated
cases were not run.

`skills/code-review/scripts/chain_check.py:140-141`:

```python
COORDINATE_ITEM = r"`[^`\s:/#][^`\s:#]*(?::[0-9]+(?:-[0-9]+)?)?`"
COORDINATE = re.compile(r"`([^`\s:/#][^`\s:#]*)(?::[0-9]+(?:-[0-9]+)?)?`")
```

`tests/test_chain_check.py`, T33's refused values, after `` "`a b.py`", ``:

```python
            "`a.py#unit`",
            "`a.py#unit:3`",
            "`a.py:1`, `b.py#unit`",
```

`evals/scripts/replay_targets.py:293-296`, so a truth reads a line window
and never a unit (`alternatives` still finds the window through
`unit_span`):

```python
    options = []
    if lines:
```

`evals/scripts/rule_cases.py:280`:

```python
            r"^location: .*src\/textutil\.py:(?:[4-9]|1[0-9])(?!\d)",
```

Then the cases, regenerated as phase 5d-iii regenerated them, and
`seed_defects.py`'s docstring (`:8`) saying a line window rather than
`path#unit`:

```sh
python3 evals/scripts/replay_targets.py --case replay-1791382684-r2 --case replay-1791382684-r5 --case replay-1791384160-r2 --case replay-1791779434-r5
python3 evals/scripts/seed_defects.py --case seeded-279a580b --case seeded-4d316179 --case seeded-9b644676 --case seeded-ad447367
python3 evals/scripts/rule_cases.py
```

answer: Fixed at f5ba02f1. `COORDINATE_ITEM` and `COORDINATE` take no `#` in a path, and T33 refuses the three values, red on the old reader (exit 1, "assert ['a.py#unit'] is None"). `truth_pattern` reads a line window, taken from the unit's lines where an old location names a unit, and its path-only fallback refuses a following `#`; the new case `test_a_truth_never_matches_a_coordinate_the_check_refuses` was red on the old pattern. `rule_cases.py`'s grader reads the line window alone, and `seed_defects.py`'s docstring says a line window. The eight graders that held a `path#unit` option were regenerated with `--case` and `rule_cases.py`, and all twelve warden truths now read a line window, so the round's second Not judged row is answered. The fix also went to `seed_defects.py`, the new case's module, the regenerated graders under `evals/behaviour/warden/` and the changelog fragment, appended to `location:`. The `regression:` line stands as written: the owner ruled on 2026-10-16 that a defect in a phase the owner approved is new work, so this round got its fix pass (a6075755).

### 2. A finding heading with no number, or with a number a second heading also carries, is read anyway, so one confirmation answers two fixed findings and an unnumbered one is told to be named `round-<N>#None`

severity: should
location: `skills/code-review/scripts/chain_check.py:642-647`, `skills/code-review/scripts/chain_check.py:711-741`, `skills/code-review/scripts/chain_check.py:1029-1043`, `docs/the-review-record.md:126-134`, `tests/test_chain_check.py:575`, `templates/sdd-round.md:59-60`, `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/changelog.md:90-91`
verdict: fixed 7055985e
regression: round-6#1

The unit: `findings` and `finding_number`, which 193ce92e added and
cf9b116e changed, and `channel`, which cf9b116e added and 4ed5dd39 changed.
A finding's number is its id. The template numbers the sections from 1, the
review skill says the number in the heading is the id, and `channel` keys
every confirmation on it. `finding_number` returns None for a heading such
as `### a thing`, and nothing refuses that. Two sections both headed
`### 1.` are both read. So one `confirms: round-1#1` in the next record
covers two `fixed` findings, and the check passes one that no round named
on its own. An unnumbered `fixed` finding is refused with "one of them reads
`round-1#None`", a reference `reference_of` refuses, so the refusal asks
for a line that cannot be written. An unnumbered `deferred` finding passes.
`docs/the-review-record.md:126-140` lists what the check cannot read and the
two ways it errs, and names neither.

executed: `test_tmp_r7_probe.py`. Two `### 1.` sections at `fixed`, and
in the next record one `confirms: round-1#1`, give no error, and `channel`
names nothing. `### x with no number` at `fixed` gives the `round-1#None`
refusal. A heading with no number at `deferred #9` reads clean. executed:
the case below fails on the shipped reader (exit 1, "assert [1, 1, None, 3]
== [1, 3]") and passes with the paste, in the run named under finding 1.

`skills/code-review/scripts/chain_check.py:711-715`, the head of the loop
over the finding sections in `findings`:

```python
    numbers = set()
    for first, stop in spans:
        heading = lines[first].strip()
        number = finding_number(heading)
        if number is None or number in numbers:
            errors.append(
                (
                    rel,
                    first + 1,
                    f"{heading} {DASH} "
                    + (
                        "no number: a finding's heading reads `### <n>. "
                        "<symptom>`, and a later round names it by that `n`"
                        if number is None
                        else f"a second finding numbered {number}: a later "
                        f"round's `round-<N>#{number}` would name both"
                    ),
                )
            )
            continue
        numbers.add(number)
        said = [
            (i, label) for i in range(first + 1, stop) if (label := misspelt(lines[i]))
        ]
```

`tests/test_chain_check.py`, a case at the end of `TestFindings`:

```python
    def test_a_heading_with_no_number_or_a_number_twice_is_refused(self):
        """A finding is named across rounds by its heading's number, so a
        heading with none, or a number a second heading also carries, is a
        finding no `round-<N>#<n>` names alone: both are refused at the
        heading, and the record's other findings still read."""
        text = record(
            "abc1234",
            [
                finding(1, "fixed abc1234"),
                finding(1, "fixed abc1234", title="a second one"),
                finding(2, "deferred #9").replace("### 2. ", "### "),
                finding(3, "open"),
            ],
        )
        lines = reader.readable(text)
        found, errors = chain.findings(reader, lines, "r.md")
        assert [f.number for f in found] == [1, 3]
        assert [(line, why.split(" — ")[0]) for _r, line, why in errors] == [
            (lines.index("### 1. a second one") + 1, "### 1. a second one"),
            (
                lines.index("### the parser drops a row") + 1,
                "### the parser drops a row",
            ),
        ]
        assert "a second finding numbered 1" in errors[0][2]
        assert "no number" in errors[1][2]
```

`docs/the-review-record.md:130`, the list of what the check cannot read,
one clause added after the doubled-line clause, and the paragraph's
`Enforced by:` gaining the case above:

```markdown
place; a finding with no `verdict:` or `location:` line, or two of either;
a finding heading with no number, or with a number another heading of the
record carries;
```

answer: Fixed at 7055985e. `findings` refuses a heading with no number, or with a number an earlier heading carries, at the heading's line before reading its labels, so `channel` never meets `round-<N>#None` and one `confirms:` line answers one finding. The round's case, `test_a_heading_with_no_number_or_a_number_twice_is_refused`, was red on the old reader (exit 1, "assert [1, 1, None, 3] == [1, 3]") and passes. `docs/the-review-record.md` lists the refusal and names the case on its `Enforced by:` line. The template's list of what fails a ready pull request and the changelog fragment say the same, appended to `location:`.

### 3. The review skill ends a run on a verifying round whose `should` finding the smith closed `rejected`, and the check refuses that record as the last one

severity: should
location: `skills/code-review/orchestration.md:113-116`
verdict: fixed 46cd674a
regression: round-6#1

The unit: the sentence 9d61c520 rewrote, after cf9b116e added the
last-record rule and 4ed5dd39 renamed `answered` to `rejected`. It now says
a verifying round that raises a `should` finding the smith closes
`rejected` "has opened nothing needing a fix, and the run ends there".
`channel` refuses a `fixed` or `rejected` finding in the last record as
owing a verifying round. `docs/the-review-record.md` §*What the check
reads* says none of the last record's findings is `fixed` or `rejected`,
and Alternative AT chose that rule. An orchestrator following the sentence
stops with that record last. The sealer's broad run asks the records arm
first, and the ready pull request fails on it, after the run was declared
over. The first half of the sentence still holds: such a round opens
nothing needing a fix, so it does not consume the cap.

executed: `test_tmp_r7_probe.py`, a round 2 holding one `verdict: rejected`
finding as the last record: "reads `verdict: rejected` in the last record,
and no round after it read it: a verifying round is owed". executed: the
paste below applied in the clone, with finding 4's paste, and
`test_the_record_is_written_in_words.py`, `test_no_real_identifiers.py`,
`test_docs_line_wrap.py`, `test_one_word_one_meaning.py`,
`test_no_passage_is_pasted_into_a_second_file.py` and
`test_the_rules_have_one_owner.py` pass (exit 0, 92 passed), and
`bin/rules --check` exits 0.

`skills/code-review/orchestration.md:113-116`:

```markdown
The condition is not *this round found nothing* — that would be unbounded, and
it was considered and rejected. A verifying round that raises a `should`
finding the smith closes `rejected`, with its grounds, has opened nothing
needing a fix, and it does not consume the cap. Its record is still not the
last one: the check refuses a `rejected` finding in the last record, so one
more verifying round reads that answer alone and names it on a `confirms:`
line, or on a finding's `regression:` line where the rejection does not
hold, and the run ends at that round.
```

answer: Fixed at 46cd674a with the round's paste. Such a round opens nothing needing a fix and does not consume the cap, its record is still not the last one, and one more verifying round reads the rejection and ends the run. The other statements of where a run ends, the two cases `agents/smith.md` gives for a failing ready pull request and the section's own paragraph on the cap, already agree.

### 4. The upgrade note cannot be followed for a 0.21.1 record: it names a script path no user's repository has, and it maps none of the note, carried and fragment rows or the `withdrawn`, `not a defect` and `agreed, fixed` verdicts such a record carries

severity: should
location: `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/changelog.md:28-43`
verdict: fixed e3c73c89
regression: round-6#1

The unit: the paragraph *A work item in flight when you update*, which
9a4ce364 wrote and 8445feb8 changed. Three gaps, each one the check turns
into a refusal the user has no word for.

- The command. `python3 skills/code-review/scripts/chain_check.py` is a
  path inside the plugin. A user's repository carries no `skills/`, and CI
  runs the same file from its clone of the plugin
  (`templates/hygiene.yml:92`). The plugin's files sit under
  `~/.claude/plugins/cache/<marketplace>/<plugin>/<version>/`
  (`skills/update/SKILL.md:147`).
- The rows. A 0.21.1 record carries open note rows that close once at the
  run's end (`round_record.py`'s `notes` at ce448bbe), `carried` rows, and
  the `fix-surface` and `fragment` confirmations
  (`docs/round-record-spec.md:146`, `:163` at ce448bbe). Its check closed
  rows with `withdrawn`, `not a defect` and `agreed, fixed` as well
  (`chain_check.py:431-436` at ce448bbe). The note maps none of them, and
  the new check refuses each.
- The channel. The note never says that a row marked `fix of a fix` needs
  a regression line naming the earlier finding, or that the last record may
  hold no `fixed` or `rejected` finding. A user who maps only the
  confirmation rows meets both refusals with nothing in the note to write.

read: `changelog.md:28-45`, `templates/hygiene.yml:45-95`,
`skills/update/SKILL.md:140-150`, and at ce448bbe `round_record.py`,
`docs/round-record-spec.md` and `chain_check.py`. executed: the
replacement below, with the old marks the paragraph already quotes written
out, passes the document tests named under finding 3. Each block replaces
the words of the paragraph named before it. The marks the paragraph
already quotes stay where they are.

`changelog.md:33-34`, the location clause's end:

```markdown
  `location:` holding its Location cell's coordinates, each backticked and
  joined by `, ` (a `path#unit` becomes its `path`),
```

`changelog.md:34-38`, from the verdict clause to `answer:`:

```markdown
  `verdict:` holding its Verdict cell, where `answered`, `withdrawn` and
  `not a defect` become `rejected` if the finding did not hold,
  `fixed <commit>` if a commit repaired it and
  `deferred <where it was repaired>` if it was repaired outside the tree
  with no commit, `agreed, fixed` becomes `fixed <commit>`, and a bare
  `fixed` takes the commit its grounds name; a `regression: round-<N>#<n>`
  line where the row was marked `fix of a fix`, naming the finding whose
  fix made the unit; its block from `## Paste-ready fixes`; and
  `answer:` holding what the fix pass wrote;
```

`changelog.md:39`, after *with its text on the next line;*:

```markdown
  a `carried` row and a `fix-surface` or `fragment` row become
  `confirms:` lines the same way; a note row has no place in the new
  record, so keep its text as prose under the `target:` line or open an
  issue for it;
```

`changelog.md:41-42`, from *Then run* to *fix what it still names.*:

```markdown
  Every `fixed` or `rejected` finding needs a `confirms:` or `regression:`
  line in the next record, and the last record may hold neither, so a run
  whose last round closed a finding takes one more verifying round. Then,
  in the work item's worktree, run
  `python3 ~/.claude/plugins/cache/<marketplace>/specseal/<version>/skills/code-review/scripts/chain_check.py
  --baseline origin/<base> --worktree` and fix what it still names.
```

answer: Fixed at e3c73c89, from the round's pastes. The note runs the plugin's installed copy, `python3 ~/.claude/plugins/cache/<marketplace>/specseal/<version>/skills/code-review/scripts/chain_check.py --baseline origin/<base> --worktree`, in the work item's worktree. It maps `answered`, `withdrawn`, `not a defect`, `agreed, fixed` and a bare `fixed`, the note, `carried`, `fix-surface` and `fragment` rows, the `Fix of a fix` row to a `regression:` line, a two-commit `Target SHA` to its later commit and a `path#unit` to its path, and says the last record may hold no `fixed` or `rejected` finding, so such a run takes one more verifying round.

### 5. The orchestrator's delivery table still names a round's `Target SHA` and the warden's `fix of a fix` mark, and says a record carries two commits where HEAD moved, which the `target:` line refuses

severity: should
location: `skills/implement/orchestration.md:636-637`, `skills/implement/orchestration.md:639`
verdict: fixed dcc00054

e9baf154..aa0c79a6 does not touch this file, so the finding names no
earlier one. 5b637fee's message says the documents that named a round's
commit as `Target SHA` now name the `target:` line, and contract §12 makes
the class every statement of the shape. The phase record names `:637` as
part B's and does not name `:636` or `:639`. Plan row 8 gives part B
`skills/implement/SKILL.md`, not this file. Row `:639` tells the
orchestrator a record carries "both SHAs in `Target SHA` where HEAD moved".
`TARGET_VALUE` reads one commit, so `abc1234, def5678 against main` is
refused, and `skills/code-review/orchestration.md:253` already says the
next round's line names the new HEAD alone. Row `:636` says the check fails
only on a commit after the last record's. It also fails on a `fixed` or
`rejected` finding of that record. Row `:637` says the `fix of a fix` mark
is read by nothing. The mark is now a regression line, which `channel`
reads as a reference, and it still stops no fix pass mechanically.

executed: `TARGET_VALUE` against `abc1234, def5678 against main` gives no
match. executed: the paste applied in the clone, and
`tests/test_every_orchestrator_act_names_its_delivery.py`,
`tests/test_no_passage_is_pasted_into_a_second_file.py` and
`tests/test_docs_line_wrap.py` pass (exit 0, 59 passed). `git grep
"Target SHA"` over the file then finds nothing (exit 1).

`skills/implement/orchestration.md:636-637`:

```markdown
| Orchestrator: the run ends with a verifying round | `skills/code-review/orchestration.md` | check: `skills/code-review/scripts/chain_check.py` | It fails a ready pull request when a commit touching a file outside the work item's records follows the commit on the last record's `target:` line, or a finding of that record reads `fixed <commit>` or `rejected`, which is the run whose own last fixes nobody opened; on a draft it prints and names the verifying round. What it cannot read is the cap: the extension lines are the warden's, and the sealer reads the count |
| A fix of a fix sends the work item back to its framer | `skills/code-review/orchestration.md` | still a sentence | The warden's `regression:` line stops nothing mechanical: `skills/code-review/scripts/chain_check.py` reads it only as a reference to an earlier finding, and reads the `Reframed` line only for its author against the declaration, and the sealer reads the records |
```

`skills/implement/orchestration.md:639`:

```markdown
| Orchestrator: verify before posting | `skills/code-review/orchestration.md` | still a sentence | The four checks are readings the orchestrator takes before posting, and nothing in the tree records that any of them happened. The one part a record carries is the new HEAD on the next round's `target:` line where HEAD moved |
```

answer: Fixed at dcc00054 with the round's pastes for the three rows. `git grep -E "Target SHA|both SHAs|fix of a fix. mark"` over the file then finds nothing (exit 1).

## Confirmations

confirms: none
The six records keep every verdict, reference and ground through the three rewrites, at `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/rounds/round-1.md` to `round-6.md`. executed: `test_tmp_r7_records.py` read each record at e9baf154 through that commit's `verdict_table` and at aa0c79a6 through `findings`, `confirmations` and the `## Not judged` table. The finding verdicts are equal in order for all six (7, 3, 2, 2, 2, 1 findings). The confirmation rows become as many `confirms:` lines (5, 7, 7, 5, 6, 5), and the three question rows of rounds 1 and 4 become rows of `## Not judged`. One location changed, round-1#5 gaining `.test_durations`, which `plan.md` Alternative AU decided. The words the old text holds and the new does not are the table's own: the `confirmed` verdict cells, the `fix pass` tails that became answer lines, the field table's words and the old probes heading. read: no ground lost a sentence

confirms: none
The check fails closed at every edge probed beyond the two findings above, at `skills/code-review/scripts/chain_check.py:650-660`, `:757-827`, `:869-908`, `:987-1057`, `:1225-1268`. executed: `test_tmp_r7_probe.py`. A trailing space after a verdict, a bare `verdict:` and a prose line opening `Target:` inside a finding are each refused by line. A record with CRLF line ends reads the same as with LF. The template reads as one `open` finding and no refusal. A `fixed` commit that touches a located path passes, and one that touches none is refused. A `fixed` finding no next record names is refused at its own heading. A last record holding `rejected` is refused as owing a verifying round. executed: the suite's cases for the label spellings, doubled and missing lines, references, confirmations, the target line and unclosed regions pass at the target (exit 0, 620 passed over eight modules)

confirms: none
T41 holds the fix-pass sentence it names, at `tests/test_the_record_is_written_in_words.py` and `docs/the-review-record.md:56-67`. executed: with the sentence put back to close such a repair `rejected`, the module fails (exit 1, 1 failed, 1 passed), and it passes at the target. read: the template's `deferred <home>` line, the smith's fix-pass sentence, the document's paragraph and the changelog's mapping all give a repair with no commit `deferred <where it was repaired>`, and each other text this item touches gives `rejected` the one meaning that the finding does not hold. The exception is the sentence of finding 3

confirms: none
The sealer's step 3 holds two acts and reads no location, and the document and the template still point at it, at `agents/sealer.md:60-65`, `docs/the-review-record.md` §*The guarantee*. read: step 3 names the sample re-run and the removals, and says a finding's verdict and its commit are the check's. executed: `tests/test_the_sealer_guarantees.py` passes in the narrow run, T40 among it

confirms: none
The branch's own check and rules read clean apart from what is owed later, at the target. executed: `chain_check.py --baseline origin/release/v0.22.0` on the clone exits 0 with three lines: round 6's target is behind HEAD (193ce92e), and `broad-gate.md` and `guarantee.md` are the sealer's. `bin/rules --check` resolves all 420 targets in 60 rule files

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the warden's proof block lands in the round record. §*Report* ends "End with the proof block" right after "no emoji anywhere in it", and the review skill's block opens with an emoji character. The frame's `## Removes` row left that marker to part B and #940. A block in the record would trip the `shape-words-only` grader | `agents/warden.md` §*Report*, `skills/code-review/SKILL.md:296-302`, `evals/scripts/behaviour.py` (`EMOJI_RANGES`) | the framer, for part B |
| Whether the regenerated replay and seeded cases still find their truth with a line window alone, after finding 1's fix | `evals/behaviour/warden/` | the fix's author, through the generators' output |
| `agents/framer.md:302` still says a round marks a finding `fix of a fix`, and `skills/agent-contract/SKILL.md:284` names `Target SHA`, `Fixes checked by` and the `Pass` checkbox as words a checker reads. Plan rows 6 and 8 rewrite both files in part B | `agents/framer.md:302`, `skills/agent-contract/SKILL.md:284` | the framer, for part B |
| Whether a prose line that opens with a quoted label is a label in another spelling. The spec's rule strips backticks before it compares the first word, so a line opening with a code span such as the confirmation reference in finding 2's grounds is refused, though it quotes a label and writes none. This record's own draft met it at that line and was rewrapped. Neither `agents/warden.md` §*Report* nor the template says a quotation may not open a line | `spec.md` §*What a round records*, the first rule; `skills/code-review/scripts/chain_check.py:119-124` | the framer |
| The full suite | the tree at aa0c79a6 | the sealer |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the worktree into `<scratchpad>/923-r7/clone`, checked out at aa0c79a6, with `origin/release/v0.22.0` fetched from the worktree (ce448bbe) | every run below ran there. The worktree was only read, apart from this file |
| `bin/test tests/test_chain_check.py tests/test_the_record_is_written_in_words.py tests/test_broad_gate.py tests/test_the_seal_is_taken_once_by_the_sealer.py tests/test_the_release_seal_is_drawn.py tests/test_the_sealer_guarantees.py tests/test_the_pull_request_language_is_the_repositorys.py tests/test_no_passage_is_pasted_into_a_second_file.py -q` | exit 0, 620 passed |
| `chain_check.py --baseline origin/release/v0.22.0 --root <clone>`, before this file | exit 0. The pull request's state is unknown, so nothing was judged as ready. Three lines owed later: round 6's target is behind 193ce92e, so a verifying round is owed, and `broad-gate.md` and `guarantee.md` are the sealer's |
| `bin/rules --check --root <clone>` | exit 0: all 420 targets in 60 rule files resolve |
| `test_tmp_r7_probe.py` (plain `python3 -I`): `location_of`, `record_findings`, `verdict_problems` and `channel` over one-record texts and a scratch repository with one fix commit | as in the grounds of findings 1, 2 and 3 and of the second confirmation |
| `test_tmp_r7_records.py` (plain `python3 -I`): the six records at e9baf154 through that commit's `verdict_table`, at aa0c79a6 through `findings`, `confirmations` and the `## Not judged` table | verdicts equal in order for all six; confirmations 5, 7, 7, 5, 6, 5; three question rows to three rows of `## Not judged`; one location gained, round-1#5's `.test_durations` |
| findings 1 and 2's cases on the shipped reader: `bin/test tests/test_chain_check.py -q -p no:xdist -k "test_a_heading_with_no_number_or_a_number_twice_is_refused or test_one_or_more_backticked_coordinates_read_and_nothing_else_does"` | exit 1, 2 failed: "assert ['a.py#unit'] is None" and "assert [1, 1, None, 3] == [1, 3]" |
| findings 1 and 2's pastes applied with `Edit`; `bin/test tests/test_chain_check.py tests/test_broad_gate.py tests/test_the_release_seal_is_drawn.py tests/test_the_seal_is_taken_once_by_the_sealer.py -q`; `chain_check.py` on the clone | exit 0, 485 passed; the same three owed lines |
| findings 3 and 4's pastes applied with `Edit`; `bin/test tests/test_the_record_is_written_in_words.py tests/test_no_real_identifiers.py tests/test_docs_line_wrap.py tests/test_one_word_one_meaning.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_the_rules_have_one_owner.py -q`; `bin/rules --check` | exit 0, 92 passed; rules exit 0 |
| finding 5's paste applied with `Edit`; `bin/test tests/test_every_orchestrator_act_names_its_delivery.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_docs_line_wrap.py -q`; `git grep "Target SHA"` over the file; `TARGET_VALUE` against `abc1234, def5678 against main` | exit 0, 59 passed; grep exit 1; no match |
| T41's sentence put back to close a repair `rejected`, `bin/test tests/test_the_record_is_written_in_words.py -q -p no:xdist` | exit 1, 1 failed, 1 passed. The file was restored |
| `git grep` over `agents/`, `skills/`, `docs/`, `templates/`, both READMEs, `evals/scripts/`, `.github/`, `hooks/` and `bin/` for the old record's words (`Target SHA`, `fix of a fix`, `answered`, `Needs a fix`, `Paste-ready fixes`, `Executed probes`, `## Verdicts`, `out of verified scope`, `with grounds`) | the hits named in findings 3 and 5 and in `## Not judged`; the rest are history in comments, the guarantee's own `Target SHA`, `docs/one-root-by-lifetime.md` kept as a design record (`overview.md`), or the refused spellings the check names on purpose |
| this file through `chain_check.py --worktree` on the clone, then staged, `bin/test tests/test_no_real_identifiers.py tests/test_docs_line_wrap.py tests/test_one_word_one_meaning.py -q`; an emoji scan of the file | the first draft was refused at one prose line opening with a quoted `confirms:` reference, and rewrapped. Then exit 0: the five findings named as `open`, `broad-gate.md` and `guarantee.md` owed to the sealer, round 6 no longer behind HEAD, no refusal of the record's shape. Tests exit 0, 64 passed. No emoji character |
| the full suite | not run: `unverified`, the sealer's |

Every probe file and the clone sat under `<scratchpad>/923-r7/` and were
deleted with it.
