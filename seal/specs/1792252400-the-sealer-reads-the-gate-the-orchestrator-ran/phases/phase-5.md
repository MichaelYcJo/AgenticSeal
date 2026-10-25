# 1792252400-the-sealer-reads-the-gate-the-orchestrator-ran — phase 5

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | the commit that adds this record; `plan.md`'s row 5 Status names it |


## What this phase was asked

Rename the verdict words: `sound` → `sealed`, `not sound` → `withheld —
<reason>`, `undecidable` → `undecided — <question>`, in every site phase 5's
row lists, found by the class grep rather than by the row's line numbers. An
old word is refused at a ready pull request on its `Verdict:` line, and the
line says the word changed. "The sealer's two files" becomes "the closing
records", constant `CLOSING_RECORDS`, with the rule it states unchanged.
`skills/verify/SKILL.md` is #967's and stays untouched. T8 is written red
first, each new or rewritten unit is mutation-checked, and the changelog
fragment carries the paragraph for an item in flight at the update.

## What this phase found

**The plan's grep finds less than it seems to.** In `git grep -E`, `\b` does
not match a word boundary, so `\bsound\b` found nothing: `SOUND = "sound"` in
`chain_check.py` was not among its hits. The class was measured with
`git grep -w` over `sound` and `undecidable` in every case, and the plan's
form is reported beside it in the table below.

**`rule-sealer-sound` is now `rule-sealer-sealed`.** The case's slug is
`SEALER_RUNS`' first field, and it names the verdict, so it was renamed with
the word. Its directory, work item `1790000030-guarantee-sealed` and branch
`feat/guarantee-sealed` follow from the slug. Phase 6 reads its graders as
the phase-4 side's `rule-sealer-sound` graders. Only the verdict regex
changed: `^Verdict:\s*\**sealed\**\s*$` and, for the other three cases,
`^Verdict:\s*\**withheld\b`.

**The refusal keeps the old words in one constant.**
`chain_check.py#RETIRED_VERDICTS` holds `sound`, `not sound` and
`undecidable`. `verdict_word` reads each one, and `guarantee` refuses it
before the generic `sealed` check, with its line and `RETIRED_SAYS`. The
comment over the constant says why it exists: a guarantee written by a
sealer that ran before the rename. It can go once no item can carry one.

**Prose that used `sound` to mean the verdict was reworded.** Four sentences
used the adjective for the sealer's finding. `agents/sealer.md` and
`docs/the-review-record.md` now say *the work … holds*, and
`docs/the-record-layout.md` says *whether the sealer sealed the work*. In
`agents/sealer.md`'s last-but-one rule, *read sealed at HEAD* became *read at
HEAD*, so `sealed` names the verdict alone (S9). The `Broad gate` cell of the
test fixture's `guarantee.md` read `sealed`, and it now quotes the run.

**A stale owner in a sentence this phase rewrote.**
`docs/the-review-and-parity-arms.md:100` said *the one broad run the sealer
took*. Phase 3's class missed it, and it now says the orchestrator took it.
The same miss stood in `chain_check.py#guarantee`'s refusal of a missing
file, *after its broad run*, which 53d5c471 changed to *after the
orchestrator's broad run*. `git grep -F "after its broad run"` outside
`seal/specs/` and `changelog/` then found nothing.

**There was no `templates/sdd-changelog.md`.** The fragment follows the
shape of the work items' existing `changelog.md` files: a `### Changed`
bullet ending with the item and the issue. It carries only the in-flight
paragraph, and phase 7 completes it.

**Three prose lines over the wrap limit stood at 2f901974.** They are
`agents/sealer.md:95` (92 columns), `docs/the-broad-gate.md:123` (98) and
`docs/the-review-and-parity-arms.md:108` (91), so `test_docs_line_wrap.py`
was red at phase 4's tree. This phase rewrapped one line it had lengthened
itself, `agents/sealer.md:72`, and the three above, without changing a word.

**Sites changed, by file:**

| File | What changed |
|---|---|
| `skills/code-review/scripts/chain_check.py` | `SEALED`, `WITHHELD`, `UNDECIDED`; `RETIRED_VERDICTS` and `RETIRED_SAYS`; `verdict_word`; the refusal by line; `CLOSING_RECORDS` and the follow message; the module docstring's guarantee arm |
| `agents/sealer.md` | description, Job, step 1's verdict, steps 4 and 5, the gate rule, the verdict rule, the `sealed` rule and its `Enforced by:` |
| `templates/sdd-guarantee.md` | the comment and the `Verdict:` line |
| `docs/the-review-record.md` §*The guarantee* | the first sentence, the verdict list, the pass rule with the closing records and the old-word refusal, its `Enforced by:` |
| `docs/the-record-layout.md` | the `guarantee.md` row |
| `docs/the-review-and-parity-arms.md` | the `straight to the PR` row; one heading line rewrapped |
| `docs/the-broad-gate.md` | one line rewrapped |
| `skills/code-review/orchestration.md` | `withheld — no broad run at HEAD`, the draft rule, `undecided` |
| `README.md`, `README.ko.md` | the sealer row's verdict sentence |
| `.github/workflows/hygiene.yml`, `templates/hygiene.yml` | the comment |
| `evals/scripts/rule_cases.py` | `SEALER_RUNS`, the verdict regex, the docstrings |
| `evals/behaviour/sealer/` | the four cases regenerated; `rule-sealer-sound` → `rule-sealer-sealed` |
| `tests/test_the_sealer_guarantees.py` | T8 (below), the fixture, the definition pin, the gate cell |
| `tests/test_chain_check.py` | `guarantee_file`'s default verdict; the closing records in two docstrings and two commit messages |
| `seal/specs/<this item>/changelog.md` | created with the in-flight paragraph |

**The class grep, before (2f901974) and after (062eb02f):**

| Grep | Before | After |
|---|---|---|
| `git grep -n -w -E "sound\|Sound\|SOUND\|undecidable\|Undecidable\|UNDECIDABLE"` outside `seal/specs/`, `changelog/` | 108 lines in 26 files | 8 lines in 5 files |
| the plan's `git grep -n -E "\bsound\b\|not sound\|undecidable"` outside `seal/specs/`, `changelog/` | 37 lines | 3 lines |
| the plan's grep, whole tree | 132 lines | 100 lines |

The 8 lines left are these, and nothing else:
- `chain_check.py:90`, `RETIRED_VERDICTS`, the refusal itself.
- `tests/test_the_sealer_guarantees.py:277, 280, 284`: the old-word case, which
  quotes history.
- Adjectives that are not the verdict: `seal/follow-up.md:45` (*a sound
  argument*), `tests/test_a_document_that_names_a_script_says_how_to_reach_it.py:71, 169`,
  and `tests/test_a_moved_rule_leaves_its_definition.py:335`.

`skills/verify/SKILL.md` carries none of the words, so nothing of #967's is
listed. Neither `SEALERS_FILES` nor *the sealer's two files* remains outside
`seal/specs/`.

**T8, seen red against phase 4's code.** `bin/test
tests/test_the_sealer_guarantees.py -q -p no:xdist -k "TestVerdictsOf or
other_than_sealed or old_words or unfilled_template or step_1"` exited 1 with
5 failed and 1 passed, after the tests were edited and before `chain_check.py`
and `agents/sealer.md` were:
- `test_the_old_words_are_refused_by_line`: `assert 0 == 1`, because `sound`
  passed the ready pull request.
- `test_a_verdict_other_than_sealed_fails_a_ready_pull_request`: the fixture's
  `sealed` was refused as needing `sound`.
- `TestVerdictsOf::test_each_verdict_is_read_through_emphasis`: `withheld — …`
  was read whole.
- `test_the_unfilled_template_is_no_guarantee`: `no attribute 'SEALED'`.
- `TestDefinition::test_step_1_reads_the_record_and_runs_nothing`: step 1
  still said `not sound`.

All of them were green after 284b3597.

**Mutations**, each one `mutation-check` command with `-p no:xdist`, exit 0,
`red: the cases failed against the mutation (exit 1)`:

| Unit | Mutation | Cases |
|---|---|---|
| `verdict_word`, an old `sound` | `return s` → `return SEALED` | `-k old_words` |
| `verdict_word`, `withheld` | `WITHHELD` dropped from the prefix loop | `-k TestVerdictsOf` |
| `guarantee`, the old-word branch | `… in RETIRED_VERDICTS:` → `False:` | `-k old_words` |
| `guarantee`, the old word's line | `line,` → `0,` | `-k old_words` |
| `guarantee`, the `sealed` check | `!= SEALED` → `== 'never'` | `-k other_than_sealed` |
| `guarantee`, `CLOSING_RECORDS` | `only=(GUARANTEE_FILE,)` | `-k sealed_verdict_at_head` |
| `rule_cases.py`, the `sealed` regex | `verdict == "sealed"` → `== "sound"` | `tests/test_evals_layout.py -k sealer` |

**Left standing, with its answerer:**
- `tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py`
  exits 1 on `tests/test_a_rewritten_definition_proved_non_inferior.py:508, 529`
  (`.read_text()` with no encoding, in phase 3's T7 case). This phase did not
  touch that file, and it ran the module only because the grep's substring
  `sound` matched `winsound`. The answer is the orchestrator's, before the
  sealer's broad run: two `encoding="utf-8"` arguments.
- Phase 6's reference side reads `rule-sealer-sealed` where phase 4's sides
  read `rule-sealer-sound`. That matters only to the phase record's
  per-grader table, which compares the two by hand. The answer is phase 6's.

## Commands

| Command | Exit |
|---|---|
| T8 red: `bin/test tests/test_the_sealer_guarantees.py -q -p no:xdist -k "…"` before the code | 1, 5 failed, 1 passed |
| `bin/test tests/test_the_sealer_guarantees.py tests/test_chain_check.py tests/test_evals_layout.py -q` after 284b3597's code | 0, 108 passed |
| `python3 evals/scripts/rule_cases.py --out <scratch>/cases` | 0 |
| `diff -r <scratch>/cases/sealer evals/behaviour/sealer` | 0 |
| `bin/test` over the 68 modules reading an edited file, plus `test_evals_layout`, `test_one_word_one_meaning`, `test_a_moved_rule_leaves_its_definition` | 1, 3 failed (`test_docs_line_wrap`: one line of this phase, three of 2f901974), 3377 passed, 6 skipped |
| `bin/test tests/test_docs_line_wrap.py` and the modules reading the rewrapped files, after the rewrap | 0, 731 passed |
| `bin/test tests/test_the_sealer_guarantees.py tests/test_evals_layout.py tests/test_one_word_one_meaning.py tests/test_chain_check.py tests/test_a_document_that_names_a_script_says_how_to_reach_it.py tests/test_a_moved_rule_leaves_its_definition.py tests/test_docs_line_wrap.py -q` at 373bcba9 | 0, 416 passed, 6 skipped |
| `bin/test tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py -q` | 1, the pre-existing failure above |
| `bin/test tests/test_the_sealer_guarantees.py tests/test_one_word_one_meaning.py -q` at 062eb02f | 0, 37 passed |
| `bin/test tests/test_the_sealer_guarantees.py tests/test_chain_check.py -q` at 53d5c471 | 0, 94 passed |
| `chain_check.py --baseline origin/release/v0.22.1 --root <worktree> --worktree` | 0; not judged as a ready pull request; it prints no round, no `broad-gate.md` and no `guarantee.md`, which phases 6 and 7 and the chain owe |
| `bin/rules --check --root <worktree>` | 0, 465 targets in 60 files resolve |
| `uvx ruff check` / `uvx ruff format --check` over the changed `.py` | 0 / 0 |
| `mutation-check` × 7, as the table above | 0 each, every one `red` |
