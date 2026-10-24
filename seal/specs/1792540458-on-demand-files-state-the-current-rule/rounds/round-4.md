# Review round 4: 1792540458-on-demand-files-state-the-current-rule

target: 0f7fb366, fixes 623c771e..0f7fb366

This is a verifying round over round 3's fix pass: 0874e5bc and its record
0f7fb366. `docs/the-review-record.md` *The run* owes this round after a
regression's fix pass whatever the count, so it is not an extension. The
round read only that fix, in a `git clone --no-local` at 0f7fb366.
Carried from round 3 without re-searching: the coordinates of its two
findings, and that `tests/test_first_setup_asks_once.py` holds
`seal/README.md` equal to `templates/seal-README.md`. Both verdicts were
reached again on the tree at 0f7fb366.

## Findings

This round opens no finding. The fix introduced nothing this round could
find wrong.

## Confirmations

confirms: round-3#1
Both READMEs' delete sentence now reads "A work item's directory is safe to delete wholesale **once its open rows have been moved out**, which *Export rules* below says where to read" (read, `templates/seal-README.md:11-13`, `seal/README.md:11-13`). It no longer says rules stand below, and *Export rules* below is the pointer that names section 6. The two files are byte-equal (executed `diff seal/README.md templates/seal-README.md`, no output). `git grep` for "export rules below", "rules below have run" and "feed back into" outside `seal/specs` and `changelog/` finds nothing (executed, exit 1). Against the owner's rules, the sentence states its condition once, uses no symbol as a separator, and reads one way: the moved-out rows are what *Export rules* tells the reader where to read about.

confirms: round-3#2
`templates/sdd-questions.md:31-34` reads "The orchestrator carries each answered row into `spec.md`'s `## Rule changes` ... when it drains the work item's rows, at the moment `skills/implement/SKILL.md` *6. Drain the rows before the broad run, and keep the records* names" (read). It names the party, which is the one section 6 names for the drain, plus the act, the file and the moment. A framer reading the template no longer takes the act as its own. The template's pins and the README pins pass (executed `bin/test tests/test_first_setup_asks_once.py tests/test_a_question_says_who_can_answer_it.py -q`, 56 passed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The tests runs 39534663738 at 623c771e and 39535133679 at 0f7fb366, which the spawn prompt says are running | CI | the orchestrator, who relays a failure |
| The full suite, the repository-wide lint and the typecheck: not run by this round, as contract §2 requires; the suite stays `unverified` | the branch | the orchestrator's `broad-gate` run, which comes due now that this round leaves no finding open |
| Whether the rewritten files leave each agent no worse at its cases, which only the paid non-inferiority run measures | `questions.md` Q1 | the repository owner |

## Probes

| Command | Result |
|---|---|
| `diff seal/README.md templates/seal-README.md` | no output; the files are equal |
| `git grep -n 'export rules below\|rules below have run\|feed back into' -- ':!seal/specs' ':!changelog' ':!CHANGELOG.md'` | exit 1, no line |
| `bin/test tests/test_first_setup_asks_once.py tests/test_a_question_says_who_can_answer_it.py -q` | exit 0, 56 passed |
