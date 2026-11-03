# Review round 1: 1793688270-a-check-line-names-a-case-or-the-rule-carries-none

```seal
target: bb5ad7a80 against origin/release/v0.30.1
```

The target is `git diff 147285fda...bb5ad7a80`, read in a `git clone --no-local` of the repository at `bb5ad7a80` under the session's scratchpad. The request is issue #1277 whole, its body and three comments (executed: `gh issue view 1277 --json title,body,comments`). This is round 1, so no earlier round's coordinate or verdict is carried. `seal/parity.md` is not declared, so the round block holds no `original:` line. `seal/config.md` has no `Record language` row, so the record is English.

## Findings

### 1. No standing case pins that a `routing.md` still carrying the `Answer pressed` row reads with the same answers, and the one case that holds it today stops holding it at the settle

```seal
severity: should
location: `tests/hooks/test_routing.py:400-445`, `seal/threads/1793688270-a-check-line-names-a-case-or-the-rule-carries-none/changelog.md:6`, `seal/threads/1793688270-a-check-line-names-a-case-or-the-rule-carries-none/frame/plan.md:40`
evidence: executed `git grep -n -E 'Answer pressed' -- tests`, `git grep -n -E 'with_row' -- tests/hooks/test_routing.py`, `git grep -n -E 'seal.*threads' -- tests/hooks/test_routing.py`
```

Why it matters: the changelog fragment tells every user that "A `routing.md` that still carries the row reads with the same answers as before, because the reader passes over a row it does not read" (`changelog.md:6`). `frame/plan.md:40` (*Operational impact*) and `frame/design.md` *Scope* 8 state the same. Every user repository with a work item in flight at the upgrade holds such a declaration. The edit gate, the question gate and `chain_check.py` all go through `hooks/lib/routing.py#parse`, so a reader that one day refused a row it does not read would turn each of those declarations into "not a declaration" and the edit gate's refusal back on.

Claimed (`trail/phases/phase-4.md`, *The probe*): a declaration that carries the row reads as before, and a one-off probe showed it, exiting 0 at `4be95d4ed` and 1 against the old reader. Found: the reader is right today. `hooks/lib/routing.py:227` builds `found` from every row and reads only the labels it names, so an unknown label changes no answer (read). What holds that property in the suite is only `test_every_declaration_in_this_repository_still_parses` (`tests/hooks/test_routing.py:400-445`). It reads the committed `seal/threads/*/routing.md` files, and all four of them carry the row (executed: `ls seal/threads/*/routing.md`, four files). No case builds a declaration with a row the reader does not read: `git grep -n -E 'Answer pressed' -- tests` exits 1, and every `with_row` call in `tests/hooks/test_routing.py` passes `PLANNING`, `IMPLEMENTATION` or `AUTOMATION` (executed). The settle after 0.30.1 removes those four directories (`skills/settle/SKILL.md`), and no work item drawn from the new template writes the row. From then on, nothing in the suite holds the sentence the release note gives users. `skills/code-review/SKILL.md` *A finding is not closed too early* says a claim written into a document closes when a test pins it. This one is pinned only by history that leaves.

The fix is one case in `Test_parse` of `tests/hooks/test_routing.py`, beside `test_accepts_a_two_axis_declaration_with_no_optional_row_answered` (`:108`). `with_row` and `two_axis_text` are already imported from `tests/conftest.py` at the module's head. Contract rule 15 asks to see it red before it is committed: for example, a `seal mutate hooks/lib/routing.py --replace` that makes `parse` return `None` where a row's label is outside the six it reads. The plan's row 4 command, `git grep -n -E 'Answer pressed|ANSWER_PRESSED' -- ':!seal/'`, allows lines in the tests that read an old `routing.md` (`frame/plan.md` *Phases*, row 4), so this case keeps that row's wording true. `trail/phases/phase-4.md` *The plan row's command* says the grep exited 1 "the tests included" at `f0d8cd6d8`, and that sentence stays true of the commit it names. No other sentence states the property, so the case reaches every statement of it.

```python
    def test_a_row_the_reader_does_not_read_changes_no_answer(self):
        """#1277: a declaration written before the `Answer pressed` row left
        the template still carries it, and reads with the answers it gives
        without the row. The committed declarations held this until the
        settle removes them; this case holds it after."""
        legacy = with_row("Answer pressed", "automation")
        assert routing.parse(two_axis_text()) is not None
        assert routing.parse(legacy) == routing.parse(two_axis_text())
```

```seal
verdict: fixed c87f09304
answer: The finding holds: no built declaration carried a row the reader does not read, and the four committed ones leave at the settle. The paste-ready case was added as written to `Test_parse` beside `test_accepts_a_two_axis_declaration_with_no_optional_row_answered`. Seen red after the commit: `seal mutate hooks/lib/routing.py --replace '    if not branch:' '    if not branch or set(found) - {"Axis", REVIEW, DESTINATION, BRANCH, IMPLEMENTATION, PLANNING, AUTOMATION}:'` over that one case read `red`, exit 0, with `parse` of the declaration with the row returning None, and the file was restored; `"Axis"` is in the set because `table_rows` returns the header row. Green at `82e9afa58` in one `bin/test -q` run of 89 modules, exit 0, 4909 passed, 12 skipped. `seal layout --pairs` (exit 0) reports the case with two others for calling `parse(two_axis_text())`; that argument is the baseline, and none of the others parses a row the reader does not read, so the case stays. `gaps.md` names its unpriced id in `.test_durations`.
```

### 2. `skills/implement/acts.md` says "the two optional rows" are read by nothing that refuses, and the section it tables lists `Automation`, which a gate reads, among its optional rows

```seal
severity: should
location: `skills/implement/acts.md:69`
evidence: read `skills/implement/acts.md:69`, `skills/implement/orchestration.md:274-275`, `skills/implement/orchestration.md:299`, `skills/implement/orchestration.md:308`, `hooks/question-gate.py:100`
```

Why it matters: phase 4 rewrote this sentence from "three optional rows" to "two optional rows" (`4be95d4ed`). The act it tables is `skills/implement/orchestration.md` *What the answer writes*. That section marks three rows OPTIONAL: `Automation` and `Implementation` in its table (`:274-275`), and `Planning` below it (`:308`). Its table shows only two OPTIONAL rows, `Automation` and `Implementation`. So "the two optional rows" most readily means those two. But `Automation` is read by something that refuses: `hooks/question-gate.py:100` refuses a question while the row reads `yes`, and the section says "`Automation` is held by a gate" (`:299`). Read that way, the sentence is false. Claimed (`trail/phases/phase-4.md`, the departure on four edits): the two rows are `Implementation` and `Planning`, which `hooks/implementer-notice.py` reads. That reading makes the sentence true, but the sentence does not say it, and a maintainer who reads this table when moving the act's delivery (`acts.md`'s opening) has to guess which two rows it means. The base's "three" had the same gap, and this diff rewrote the sentence. Contract rule 19 asks a change to rewrite the text it amends so it states the fact, and naming the rows does that.

The fix names the two rows in the one sentence. `hooks/lib/routing.py:195` says "The two optional rows" too, but its paragraph opens by naming `Implementation` and `Planning` as the third and fourth axes, so it has one reading and stays.

```markdown
| What the answer writes | `skills/implement/orchestration.md` | check: `skills/code-review/scripts/chain_check.py` | It refuses a `Review` or `Destination` value outside the vocabulary at the pull request, and `hooks/lib/routing.py` parses the same rows at every edit. The `Implementation` and `Planning` rows are read by nothing that refuses: `hooks/implementer-notice.py` says one line after a commit where a declared agent left no mark, and blocks nothing |
```

```seal
verdict: fixed 82e9afa58
answer: The finding holds: the section `acts.md:69` tables marks `Automation` OPTIONAL, and `hooks/question-gate.py` refuses on it, so "the two optional rows" read two ways. The sentence now names the `Implementation` and `Planning` rows, as the paste-ready row gives, and the row is otherwise unchanged. `trail/phases/phase-4.md` says `acts.md:69` reads "two optional rows" after `4be95d4ed` and that the two are `Implementation` and `Planning`; both are true of the commit it names and agree with the fix, so the record stands. `git grep -n -i 'optional rows'` outside `seal/` finds no other sentence on this act; `hooks/lib/routing.py:195` stays for the reason the finding gives.
```

## Confirmations

```seal
confirms: none
```
What matched: the form leaves every file outside `seal/` (`frame/design.md` A1, *Scope* 1). `git grep -n -E 'none reader|NO_TARGET' -- ':!seal/'` exits 1 at `bb5ad7a80` (executed). The diff removes 65 `check: none reader:` lines outside `seal/`, the base held 65 (`git grep -n -E '^\s*check: none' 147285fda -- ':!seal/'`), and the non-test files they leave number 23, as the census says (executed). `.github/scripts/rules.py:191-203` reads one shape and `render` (`:478-486`) prints no reader line (read). Each caller of `rules.parse` unpacks or indexes the two-tuple: `line_problems`, `render`, `tests/behaviour/test_docs_line_wrap.py:233` and `tests/github/test_rules.py:665`, `:692` (executed: `git grep -n -E 'rules\.parse'`, read). Claimed (phase 2): `EXPECTED` is pinned by `tests/github/test_rules.py`. Found: the module's `EXPECTED` at `:134` and four literal messages carry the one-form hint, and the module passed at HEAD (executed, `## Probes`).

```seal
confirms: none
```
What matched: A3, a left-over form line is refused. I re-ran the phase-2 probe: a planted `CLAUDE.md` holding `**A rule.** Its grounds.` and `check: none reader: the proofer at review` gives exit 1 from `bin/seal rules --check --root <it>`, with six refusals at `CLAUDE.md:4`: five markers no test carries and `reader: does not exist` (executed). That matches `trail/phases/phase-2.md` *A3's probe* and the changelog's second entry.

```seal
confirms: none
```
What matched: the preload reductions the changelog's first entry states. Claimed (phase 1, measured with `.github/scripts/release_report.py`): crafter -528, framer -720, proofer -528, sealer -418, tracer -595. I did not re-run `release_report.py`. The byte change of each preloaded file from `147285fda` to `bb5ad7a80`, by `wc -c` on `git show` of each, is contract -418, `agents/crafter.md` -110, `agents/framer.md` -302, `agents/proofer.md` -110, `agents/sealer.md` 0, `agents/tracer.md` -177 and core 0. The sums equal the five claimed figures, and no commit after `f5b4f2b44` touches those files (executed: `git diff --stat f5b4f2b44 bb5ad7a80 -- agents skills/core skills/agent-contract`, empty).

```seal
confirms: none
```
What matched: *Scope* 7 and A6, A7. `git diff --stat a564a2640 95afe5851` over the four documents gives four files, one insertion and four deletions (executed). `git grep -n -F 'Scope item 9' -- tests` exits 1 (executed). Line e stands at `docs/releasing/branch-and-release.md:134` naming `tests/behaviour/test_the_release_seal_is_drawn.py` (read). `docs/checks/the-stamp.md:89` names `tests/hooks/test_sealer_stamp.py` alone. That module measures the hook's output against `MESSAGE_BUDGET` (`tests/hooks/test_sealer_stamp.py:266-273`, `:387-406`), and the stamp module's one split on the budget heading (`tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py:185`) bounds the rule above it, not the budget (read).

```seal
confirms: none
```
What matched: *Scope* 8 reached every file that named the row. The 25 files outside `seal/` that named `Answer pressed` at the base are all in the diff (executed: `git grep -l 'Answer pressed' 147285fda -- ':!seal/'` against `git diff --name-only`, no file left over). `git grep -n -E 'Answer pressed|ANSWER_PRESSED' -- ':!seal/'` exits 1 at HEAD, and no code reads a `pressed` key (executed: `git grep -n -i pressed`, whose hits are the transcript press in `hooks/lib/press.py`, `hooks/routing-edit-gate.py` and their tests, and unrelated words). Claimed (phase 4): `test_refuses_the_row_name_and_the_option_label_crossed`'s first half moved into `test_refuses_an_unreadable_automation_answer` (`tests/hooks/test_routing.py:288`). Found: the spelling `automation` is in that case's list.

```seal
confirms: none
```
What matched: each phase's search for what its diff made false. Every phase record names its searches and calls the paraphrase searches a sample, as contract rule 12 asks, and none hands a sample back as a whole list. My own searches outside `seal/` (executed) covered `pressed`, `optional row`, the routing-row counts (`sixth`, `six rows`, `fifth row`), `preset`, `told apart`, `byte-identical`, `check line` and `` `check:` line `` in the shipped prose, `reader:` and `who reads it`, and the Korean editions. They found no statement the diff left false beyond finding 2. Three test modules delimit a rule by its `check:` line (`tests/text/test_a_moved_rule_leaves_its_definition.py:425`, `:443`, `tests/text/test_the_handoff_before_round_one.py:112`, `tests/text/test_the_record_is_written_in_words.py:115`). Each reads a rule that keeps its line, so no scoped case widened when phase 1 removed lines (read).

```seal
confirms: none
```
What matched: the suite's label is honest. Each phase record reports a phase-boundary run it executed. `gaps.md` *Not verified* labels the full suite, the repository-wide lint and the typecheck at HEAD, names the orchestrator at the broad gate as their answerer, and calls each boundary set a sample (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD | `gaps.md` *Not verified* | the orchestrator, at the broad gate |
| Whether the removed and renamed case ids push `test_the_durations_file_prices_the_suite` past its share | `frame/questions.md` Q1, `.test_durations` | the orchestrator, at the broad gate |
| Whether a removed line that named a person's check on a live run left a duty that no sentence above it states, as at `docs/checks/the-routing-check.md:79`, where the line named "the orchestrator on the first live run after a change here". Issue #1277's body takes every form line out, and `frame/design.md` *Scope* 1 keeps each paragraph as it reads, so I raise no finding. `docs/checks/the-stamp.md` already says the owner reads the first real stamp | `docs/checks/the-routing-check.md:73-79` | the orchestrator, against issue #1277's body |
| `.github/scripts/release_report.py` run at HEAD; this round checked the byte arithmetic only | `trail/phases/phase-1.md` *The preload measure* | the sealer, if it samples that claim |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_rules.py -q` | exit 0, 67 passed |
| `bin/test tests/hooks/test_routing.py -q` | exit 0, 51 passed |
| `bin/test tests/behaviour/test_waiver_decided_at_start.py -q` | exit 0, 24 passed |
| `bin/seal rules --check --root <planted>`, with `CLAUDE.md` holding one rule and `check: none reader: the proofer at review` | exit 1, six refusals at `CLAUDE.md:4` |
| `git grep -n -E 'none reader\|NO_TARGET' -- ':!seal/'` | exit 1 |
| `git grep -n -E 'Answer pressed\|ANSWER_PRESSED' -- ':!seal/'` | exit 1 |
| `git grep -n -F 'Scope item 9' -- tests` | exit 1 |
| `git grep -n -E 'Answer pressed' -- tests` | exit 1: no case builds a declaration carrying the row |
