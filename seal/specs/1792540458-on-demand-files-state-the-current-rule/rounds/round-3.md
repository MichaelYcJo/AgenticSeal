# Review round 3: 1792540458-on-demand-files-state-the-current-rule

target: 623c771e, fixes ac92a9e6..623c771e

This is a verifying round over the fix range ac92a9e6..623c771e: round 2's
record 275ba5f2, the smith's fixes 1f1dae03, their record d788e50b and the
framer's 623c771e. The round worked in a `git clone --no-local` at 623c771e.
Carried from round 2 without re-searching: its two findings' coordinates,
and that `tests/test_first_setup_asks_once.py:635` holds `seal/README.md`
equal to `templates/seal-README.md`. Every verdict below was reached again
on the tree at 623c771e.

## Findings

### 1. The seal README still says the export rules are below, where the fix left only a pointer

severity: should
regression: round-2#2
location: `templates/seal-README.md:11-13`, `seal/README.md:11-13`
evidence: read `templates/seal-README.md:11-13`, `templates/seal-README.md:65-69`, `seal/README.md:11-13`
verdict: open

The unit is `templates/seal-README.md`, with `seal/README.md` held equal to
it. `spec.md` Scope 7 asks each on-demand file to state the current rule
once, and Scope 1 (a) refuses a sentence a near miss could pass; the fix
1f1dae03 took the drain table out of *Export rules* and put a pointer to
section 6 in its place, but it left line 12's "A work item's directory is
safe to delete wholesale **after the export rules below have run**", so the
defect came from the fix's own change to the section that sentence points
at. A reader of line 12 now goes below for rules and finds a sentence naming
another file, and "have run" names an act the README no longer describes.
The fix pass's class sweep (round 2's answer) searched for `export rules`
and listed what it found; line 12 is not on its list.

```markdown
the command behind it. A work item's directory is safe to delete wholesale
**once its open rows have been moved out**, which *Export rules* below says
where to read: nothing that must survive is allowed to live only there.
```

answer:

### 2. The questions template's feed-back sentence names when answered rows move, and not who moves them

severity: should
location: `templates/sdd-questions.md:32-34`
evidence: read `templates/sdd-questions.md:32-34`, `skills/implement/SKILL.md:474-487`
verdict: open

The fix pass rewrote this line in its class sweep, from "before this
directory's work merges" to "at the moment `skills/implement/SKILL.md` *6.
Drain the rows before the broad run, and keep the records* names". The
moment now agrees with section 6. The sentence still reads "Answered rows
feed back into `spec.md`'s `## Rule changes`", which has no party, so rule
(b) of `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만
읽히게 쓴다* is not met. Two parties open this template. The framer writes
`questions.md` from it and also writes `spec.md`, and the orchestrator
drains the rows. Section 6 names the orchestrator for the drain
(`skills/implement/SKILL.md:474-475`), and its table sends a decision to an
`add` in `## Rule changes`. A framer reading this line can take the feed-back
as its own act, which happens at framing time, and that is the wrong moment.
The missing party predates the fix; the base line had none either. Round 2
read this template and confirmed it, so round 2 missed this sentence.

```markdown
The orchestrator carries each answered row into `spec.md`'s `## Rule
changes` (a policy clause or an open-questions section) when it drains the
work item's rows, at the moment `skills/implement/SKILL.md` *6. Drain the
rows before the broad run, and keep the records* names.
```

answer:

## Confirmations

confirms: round-2#1
`tests/test_first_setup_asks_once.py:768-781` holds both clauses of the block's routing bullet, "Except under `no work item`" and the pointer to *Orchestrator: how the work is routed*, in the lead before the write. The fix pass's answer says it was seen red twice under `mutation-check`, once with each clause removed. The case passes at 623c771e (executed `bin/test tests/test_first_setup_asks_once.py -q -k "no_declaration_under_no_work_item or points_at_the_drain or seal_readme_is_the_template"`, 3 passed).

confirms: round-2#2
Both READMEs' *Export rules* is one sentence naming section 6 as where the party, the moment and each destination are stated, so the disagreement on all three is gone (read, `templates/seal-README.md:65-69`). The smith took a pointer instead of round 2's replacement table. That holds on its grounds: the party that drains, the orchestrator, opens the implement skill, and a second table is the value stated twice that round 2 found. `tests/test_first_setup_asks_once.py:638-652` refuses a destination table there and passes (executed, the run above). Finding 1 is a defect this fix introduced on line 12 of the same file, and it does not undo the close.

confirms: none
The six description lines the class sweep rewrote read one way and agree with the file they describe. The six are `skills/implement/SKILL.md:101`, `skills/implement/orchestration.md:65-66`, `README.md:120`, `README.md:420`, `README.ko.md:115` and `README.ko.md:414`. Each says what the README holds and where the export rules are. None still says the README carries them. The orchestration line names the party's file, which is the file section 6 lives in (read).

confirms: none
The framer's parse defect is real, and nothing else in the tree carries it. `rule_changes.parse` over this item's `spec.md` refuses at 2bbf5866 and at ac92a9e6 ("a line that is not a field of the item above", lines 282 and 285), and reads four `change` items at 623c771e. Each of the four applies in memory and changes its document, through `apply_op` against `docs/` at 623c771e. Over every `seal/specs/*/spec.md` in the tree, 118 files, the parse reports no error: 115 hold the no-change block, and three hold items. The three are `1792473741-dash-shapes-become-field-words` with one, `1792533444-automation-refuses-mid-run-questions` with one, and this item with four (executed, a probe over all 118, deleted after the run). Rounds 1 and 2 did not run the parser over this item's section, so neither saw the defect; the framer found it. The `docs/the-record-layout.md` *seal/* item's `from:` is that row's text at 623c771e, `docs/the-record-layout.md:217` (read).

confirms: none
The framer's new paragraph in *Data and interfaces*, "A `docs/` line this item makes false gets a `change` item in `## Rule changes`, added by the phase whose commit makes it false", names the party, the moment and the file, and says why the section holds only items (read, `spec.md:264-269`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The tests run 39534663738 at 623c771e, which the spawn prompt says is running | CI | the orchestrator, who relays a failure |
| The full suite, the repository-wide lint and the typecheck: not run by this round, as contract §2 requires; the suite stays `unverified` | the branch | the orchestrator's `broad-gate` run once the rounds settle |
| Whether the rewritten files leave each agent no worse at its cases, which only the paid non-inferiority run measures | `questions.md` Q1 | the repository owner |

## Probes

| Command | Result |
|---|---|
| `python3 test_tmp_rule_changes.py` in the clone: `rule_changes.parse(text, "docs")` over every `seal/specs/*/spec.md`, then `apply_op` for this item's items | 118 specs, 0 errors, 115 no-change blocks, 3 with items (1, 1, 4); all four of this item's items apply and change their document; the file was deleted after the run |
| `rule_changes.parse` over this item's `spec.md` at 2bbf5866, ac92a9e6 and 623c771e | refused at lines 282 and 285 at the first two; four items at 623c771e |
| `bin/test tests/test_first_setup_asks_once.py -q -k "no_declaration_under_no_work_item or points_at_the_drain or seal_readme_is_the_template"` | exit 0, 3 passed |
