# Design: 1794271938-follow-up-holds-seven-owner-questions

## Grounding

The tree as read at `eccf1bcb7`.

| Policy clause | What it fixes for this work |
|---|---|
| G1 `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | No script carries a list of the spellings a label is written in, and a reading guessed from words is reported and never used to block. Row 4 asks for exactly such a checker, so it closes as moot. Row 6's guard is a one-spelling list over a shape, so it goes. A mechanism stays only while what it caught outweighs what it costs (G8). |
| G2 `skills/core/SKILL.md` *The first value: efficient development through the workflow*, **Judgment is spent where meaning is the question, and a script answers the rest.** (read) | A script that answers "these differ" where the meaning is the same is the worst result. Row 6's guard has done that once on record (G8). |
| G3 `skills/implement/SKILL.md` *3. The SDD file set*, lines 323 to 328 (read) | The one sentence that states the Status cell as a closed set: "a **Status** column that is empty or holds the commit that closed the phase", then "a tick and the word `done` are refused where a hash is not". The owner's decision on row 2 is written into these two sentences in place (*Data & interfaces*). |
| G4 Every other statement of the Status cell (executed: `git grep -n -i` for the words `Status cell`, `Status column`, `tick and the word` and `commit that closed`, outside `seal/threads/`) | `skills/implement/SKILL.md:113-116`, `seal/README.md:113-116` with its copy `templates/setup/seal-README.md`, `agents/crafter.md:174-177`, `agents/sealer.md:99-102`, `docs/running/the-agent-set.md:117`, `docs/running/the-run.md:87` and `docs/layout/the-record-layout.md:170` each state what the cell of a phase that closed carries. None states the cell's values as a closed set, so a third value contradicts none of them. The list is a spelling search over an open class (contract rule 12), so it is a sample; the proofer's reading of the diff is where a statement it missed is found. |
| G5 No script reads a Status cell (executed: `git grep` for `Status` and `Phases` over `lib/`, `skills/*/scripts/` and `.github/scripts/`) | `skills/code-review/scripts/pr_body.py:196` quotes the plan's `## Phases` section whole and reads no cell. `deferred #N` changes no script's verdict, and no case beyond the proofer's reading is owed for it. |
| G6 `skills/settle/rule-changes.md` *Rule changes* and `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | A `## Rule changes` operation names a `.md` file of the policy root, `docs/` here. `skills/implement/SKILL.md` is a shipped skill outside it, so the row 2 sentence is an edit in this pull request and not a rule change. The work's subject is `seal/follow-up.md`, tests and their comments, and one skill paragraph, and no `docs/` section states a value this work changes (G4), so `## Rule changes` holds the no-change block. |
| G7 Row 3: `tests/behaviour/test_waiver_decided_at_start.py:177-227`, `:230-288` and `:301-345` (read); `offered`'s pattern over `templates/records/sdd-routing.md` (executed, `test_tmp_offered.py`, run once and deleted) | The `Planning` and `Automation` cases compare `offered(template, label)` to the parser's constants, and the `Implementation` case does not. `offered` reads `('crafter', 'the session')` from the `Implementation` row, `('framer', 'the session')` from `Planning` and `('yes', 'no')` from `Automation`. `lib/routing.py:72-74` holds `IMPLEMENTATION_ANSWERS = (BY_CRAFTER, BY_SESSION)`, two answers, so the case name's "three answers" names nothing the template or the parser holds. |
| G8 Row 6: `tests/text/test_a_rider_reaches_its_file.py:76-84` (read); its record, `seal/follow-up.md:47` (read) | Lines 83 and 84 assert that the one phrase `next time` is in no row of the schedulable table. Its record: on 2026-09-22 it stayed green against an answerer written *at the next change to `CONTRIBUTING.md`*, and its one recorded red was a draft row quoting its literal while describing it, a row whose answerer was already unconditional. Lines 81 and 82 pin the header sentences that state the rule, and they stay. |
| G9 Row 7: the `ast` reader at `tests/github/test_close_issues_on_release.py:1160-1178` run against the three scripts (executed, `test_tmp_argvs.py`, run once and deleted) | It finds every `gh` argv in each script. `release_completeness_check.py`: `gh api`, and `gh issue list` twice. `label_merged_on_release_branch.py`: `gh label list`, `gh label create`, and `gh issue edit` carrying `--repo` and `--add-label`. `close_issues_on_release.py`: `gh issue edit`, `gh issue close` and three `gh api`. So the reader serves the two converted cases as it serves its own. |
| G10 Row 7's class (executed: `git grep -n -E "assert f?'\"[a-z]+\", \"[a-z-]+\"" -- tests/` filtered to `not in`) | Four assertions in exactly the two cases the issue names, `tests/github/test_release_completeness_check.py:573-574` and `tests/github/test_label_merged_on_release_branch.py:401,405`. A grep for one spelling over an open class is a sample (contract rule 12); the proofer reads the diff for a third. |
| G11 What the folded cases of G10 caught (executed: `git log --follow -S folded` on each module) | Both arrive in `cbf97bf55` (2026-10-24), the commit that gathered the tests one file per module, and no later commit names a catch. `seal/follow-up.md:48` calls them "two modules that had no finding against them". Their history before `cbf97bf55` is scattered across older files and was not traced. |
| G12 Sentences outside `seal/follow-up.md` that cite one of its rows (executed: `git grep -n "follow-up"` outside `seal/threads/`, each hit read) | Five: `.github/scripts/run_tests.py:56-58` and `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py:402-405` cite row 4's class; `tests/github/test_close_issues_on_release.py:1122-1124` cites row 7; `tests/conftest.py:293-296` and `tests/test_conftest.py:364-366` cite a "first row" about the direction a checker of claims must not fail in, which `seal/follow-up.md` has not held since `a53699ec5` (#606, 2026-09-25; executed, `git log -S`). The search is the third method of contract rule 12, a command listing each file that names the file; a citation that does not name the file is outside it, so the list is a sample. |
| G13 Row 1: `skills/code-review/scripts/chain_check.py:126-127` and `docs/running/the-review-and-parity-arms.md` (read) | `--worktree` already reads the records from the working tree, and CI never passes it. The row's question arises only in local mode, where the root sits under the common git directory and nothing is committed. A local verdict CI cannot reproduce is the second guarantee the core's invariant table avoids. Closing it changes no line of the tree beyond the row. |
| G14 Row 5: the issue body's *Decided* (read) | `uvx ruff check --select E501 .` reported 292 lines at `ba4d85629` on 2026-11-10. That is the orchestrator's executed reading, carried here; this framer runs no linter (contract rule 2). `ruff.toml` sets `line-length = 88` and leaves `E501` out of `select` (read). |
| G15 The issue's comments (executed: `gh issue view 1493 --json body,comments`, 2026-11-10) | None, as the spawn's line also says. The body as folded, with *Decided*, is the request. |
| G16 `.github/scripts/durations_union.py:82-87` (read) | A work item never commits `.test_durations`. The renamed case of *Scope* item 2 keeps its old key there until CI prices the suite again. |
| G17 `docs/layout/the-record-layout.md` *A change writes fragments, never a shared file* (read) | A process row is required where the diff changes the core, `CLAUDE.md`, an agent definition, an `orchestration.md` or `bootstrap.md`. `skills/implement/SKILL.md` is none of them. The plan still asks for one row (`frame/plan.md` *Operational impact*), because the Status cell's vocabulary is a change to the way of working that a reader of the release note's *Process changes* looks for. |

## Scope

In:

1. Row 7. The `ast` reader of `tests/github/test_close_issues_on_release.py` becomes one module-level function, `argv_words` (*Data & interfaces*), whose docstring states once what the parse closes and what it does not. Three cases read through it: that module's `Test_module::test_the_script_closes_and_takes_off_one_named_label_and_nothing_else`, `tests/github/test_release_completeness_check.py#Test_module::test_the_gate_writes_nothing` and `tests/github/test_label_merged_on_release_branch.py#Test_module::test_the_script_only_ever_creates_a_label_and_adds_one`. Each converted case keeps every claim it made: the forbidden `gh issue` and `gh label` verbs, and in the label case the `gh label create` argv and an argv carrying `--add-label`. The folded reader leaves both modules. The sentence at `tests/github/test_close_issues_on_release.py:1122-1124` that says `seal/follow-up.md` carries the constant-valued escape says instead that #1493 left it open.
2. Row 3. `tests/behaviour/test_waiver_decided_at_start.py#test_the_template_PARSES_into_the_three_answers_it_ships` gains the comparison the `Planning` and `Automation` cases make (G7): `offered(template, routing.IMPLEMENTATION)` is not None and equals `routing.IMPLEMENTATION_ANSWERS`. The case is renamed `test_the_template_PARSES_into_the_THIRD_axis_it_ships`, the sibling of the `FOURTH` case's name.
3. Row 6. Lines 83 and 84 of `tests/text/test_a_rider_reaches_its_file.py` leave, and the case's docstring says that whether a row's answerer carries a condition is the reading of whoever writes or reviews the row, as `skills/core/SKILL.md` *The rule a mechanism is kept against* has it. The header pins at lines 81 and 82 stay.
4. Row 2. `skills/implement/SKILL.md` *3. The SDD file set*: the sentences G3 quotes are rewritten in place to name `deferred #N` as the third value of a Phases row's Status cell (*Data & interfaces*).
5. Rows 1 to 7. `seal/follow-up.md` *Schedulable items with nowhere else to go* loses every row and keeps its heading and its header row, as *Riders waiting on a file another branch holds* already stands. The file's header prose stays as it reads.
6. The sentences G12 lists are each rewritten to state their reason without citing a row of `seal/follow-up.md`. The sentences at `.github/scripts/run_tests.py` and `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py` say that a figure stated with no date or machine cannot be checked later. The sentences at `tests/conftest.py` and `tests/test_conftest.py` state the direction themselves: a claim removed from a corpus without a word is the direction a checker of claims must not fail in. The sentence at `tests/github/test_close_issues_on_release.py` is *Scope* item 1's.
7. The work item's `changelog.md`, written in the last phase, with one `### Process changes` row for *Scope* item 4.
8. The text that carries the closed rows' measurements (*Data & interfaces*), appended to #1493's body, where the issue's *Done when* asks for them. The orchestrator appends it; nothing in the tree holds it.

Out:

- Closing the constant-valued escape of the `ast` reader (a name in one of an argv's first three positions). The issue keeps it open, and closing it is a checker that resolves module-level names, with its own false-positive argument.
- A `gh api` call that writes. `test_the_gate_writes_nothing` reads `gh issue` and `gh label` argvs only, before and after this work, so a `gh api --method PATCH` in `release_completeness_check.py` would pass it. The issue does not name it, and whether it earns an issue is the orchestrator's call (`frame/plan.md` *Alternatives considered*).
- Merging the placeholder-axis cases G7 reads in `tests/behaviour/test_waiver_decided_at_start.py` into one (`frame/plan.md` *Alternatives considered*).
- `tests/text/test_a_rider_reaches_its_file.py#test_no_schedulable_row_carries_a_coordinate`. It reads a shape, `path.ext:N`, and the issue does not name it.
- `.test_durations` (G16).
- Any statement of the Status cell besides the sentences G3 quotes (G4).
- The version. #1495 moved `.claude-plugin/plugin.json` to 0.37.1.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 A forbidden verb written across lines | Given `release_completeness_check.py` or `label_merged_on_release_branch.py` with a forbidden `gh issue` or `gh label` argv whose words are split by a comment, when its `Test_module` case runs, then the case fails. | The crafter plants the argv in the script, runs the case red and reverts the plant (contract rule 15). The phase record names the run. check: tests/github/test_release_completeness_check.py tests/github/test_label_merged_on_release_branch.py |
| S2 The label script stops adding | Given `label_merged_on_release_branch.py` without its `--add-label` argv, or without its `gh label create` argv, when the label case runs, then it fails. | Shown red the same way as S1. check: tests/github/test_label_merged_on_release_branch.py |
| S3 The closer's case reads through the shared reader | Given `tests/github/test_close_issues_on_release.py` after *Scope* item 1, when its module runs, then every claim the case made at `eccf1bcb7` still holds. | The module green. A refactor adds no behaviour, so its red is the case's existing one (`skills/implement/SKILL.md` *2. Implement test-first*). check: tests/github/test_close_issues_on_release.py |
| S4 The template's `Implementation` placeholder drifts from the parser | Given the value of `lib/routing.py#BY_CRAFTER` changed with `templates/records/sdd-routing.md` untouched, when the third-axis case runs, then it fails on the `offered` comparison. | The crafter renames the constant's value, sees the new assertion red while the substitution loop above it stays green, and reverts. check: tests/behaviour/test_waiver_decided_at_start.py |
| S5 The schedulable table is empty | Given `seal/follow-up.md` after *Scope* item 5, when the rider module runs, then it passes, and `grep -c "the repository owner" seal/follow-up.md` prints 0. | check: tests/text/test_a_rider_reaches_its_file.py |
| S6 A session meets a deferred phase | Given a phase moved to issue #N, when a session reads `skills/implement/SKILL.md` *3. The SDD file set*, then it finds `deferred #N` as the cell's value, and a tick and `done` still refused. | The proofer reads the paragraph. No case pins prose (`frame/plan.md` *Alternatives considered*). |
| S7 No sentence cites a row that left | Given the tree after *Scope* item 6, when `git grep -n "follow-up"` runs outside `seal/threads/`, then no hit says that `seal/follow-up.md` names or carries a particular item. | The proofer reads each hit; G12 gives the method and its reach. |

## Data & interfaces

**`argv_words`**, module level in `tests/github/test_close_issues_on_release.py`, beside `load` and `read_text`:

```python
def argv_words(text):
    """The string-literal words of every argv in TEXT, a script's source:
    each list or tuple literal's elements and each call's positional arguments."""
```

It returns one list of strings per `ast.List`, per `ast.Tuple` and per `ast.Call` in the parsed source, keeping only `ast.Constant` strings, as `words` does today. A case selects the argvs it judges by their first three words, such as `words[:3] == ["gh", "issue", verb]`. The two other modules import it as `tests/github/test_label_merged_on_release_branch.py` already imports `load` from the same module.

**`skills/implement/SKILL.md` *3. The SDD file set*, lines 325 to 327**, from:

> and a **Status** column that is empty or holds the commit that closed the phase. A commit asserts a **past** state that someone can open, so a tick and the word `done` are refused where a hash is not.

to:

> and a **Status** column that is empty, holds the commit that closed the phase, or reads `deferred #N` for a phase the work item handed to issue #N. A commit and an issue each name something someone can open, so a tick and the word `done` are refused where neither is named.

The crafter rewraps the paragraph at its width and leaves line 114, which `tests/behaviour/test_the_set_a_work_item_always_has.py#KNOWN_PROSE` holds verbatim, untouched.

**The measurements' text**, which the orchestrator appends to #1493's body once the pull request opens (folded after round 1: the issue's *Done when* names the body, not a comment):

```markdown
The rows of `seal/follow-up.md` *Schedulable items with nowhere else to go* leave in this pull request. Each row's full text stands at `8657297d5:seal/follow-up.md`, lines 42 to 48. The measurements the rows carried move here.

1. **`chain_check.py --worktree` reading routing from the working tree.** Closed, not wanted. Work item 1788817289 took the notice only (#225). Its argument stands at `aa687d357:seal/specs/1788817289-local-mode-from-first-setup-to-the-gate/spec.md` *The sharp question — where an untracked declaration lands*.
2. **`deferred #N` as a third Status value.** Decided by the owner on 2026-11-10, and `skills/implement/SKILL.md` *3. The SDD file set* names it. Round 1 of #84 raised it; #84's `plan.md` row 5 carried `deferred #350`.
3. **The third routing axis's template case.** Repaired with one assertion through `offered`. The shape was measured on 2026-09-11 in #84's phase 4, on the fourth axis: renaming `BY_FRAMER` with the template untouched left the substitution case green.
4. **A checker for figures stated with no moment.** Closed as moot: `skills/core/SKILL.md` *The rule a mechanism is kept against* reports a reading guessed from words and never blocks on it. The record: review round 3 of #424 listed six sites and was three short. Work item 1789996780's phase 3 grep missed four that `survivor-check` caught, and its phase 4 left two that its review round 1 found (findings 1, 2, 3, 7 and 8).
5. **Comment-line width in shipped scripts.** Closed without a check. `uvx ruff check --select E501 .` reported 292 lines at `ba4d85629` on 2026-11-10. The instances were found by review rounds 2 and 3 of work item 1789996780: a comment line at 138 characters in a block that wraps at 75, then one at 90 in the same block, blamed to 2026-09-01.
6. **The conditional-answerer guard.** Removed. On 2026-09-22, at `11f3cde8` (a branch commit that no longer resolves), its module was green, 29 passed, against an answerer that read *the repository owner, at the next change to `CONTRIBUTING.md`, House rules*. Round 2 of work item 1790076050 found it. The guard's one recorded red was a draft row that quoted the guard's literal while describing it.
7. **Cases searching folded source.** Converted to `ast`. Measured on 2026-09-22 in round 2 of work item 1790076050: with `gh issue edit`'s argv split by one comment, the folded count read 0, and the case exited 0 while the script assigned a person on every label removal. Round 3 planted `gh issue reopen` four ways against the converted reader: written plainly or split by a comment, it was red; with the first word or the verb moved into a module constant, it stayed green. That constant-valued escape stays open.
```

## Rule changes

- nothing
  why: The work changes `seal/follow-up.md`, the tests and comments *Scope* items 1, 2, 3 and 6 name, and one paragraph of `skills/implement/SKILL.md`, a shipped skill outside the policy root (G6). No `docs/` section states a value this work changes (G4).

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| Every row of the schedulable table | `seal/follow-up.md` *Schedulable items with nowhere else to go* | Rows 2, 3, 6 and 7 land in *Scope* items 4, 2, 3 and 1. Rows 1, 4 and 5 close with no tree change (G13, G1, G14). Every row's measurements land in #1493's body, in the text of *Data & interfaces*, and the full text stays at `8657297d5:seal/follow-up.md`. |
| The `next time` guard | `tests/text/test_a_rider_reaches_its_file.py#test_the_header_stops_the_answerer_that_is_really_a_condition`, lines 83 and 84 | It tests one spelling of a shape, which the core forbids a script to carry (G1). Its catch record is one false red and one missed defect (G8). The header sentences it sits beside stay pinned, and the party that writes or reviews a row reads its answerer. |
| The folded reader | `tests/github/test_release_completeness_check.py#Test_module::test_the_gate_writes_nothing` and `tests/github/test_label_merged_on_release_branch.py#Test_module::test_the_script_only_ever_creates_a_label_and_adds_one` | `argv_words` (*Scope* item 1). No catch on record (G11), and a comment between two argv words defeats it (the issue, row 7). |
| The case-local `words` and argv collection | `tests/github/test_close_issues_on_release.py#Test_module::test_the_script_closes_and_takes_off_one_named_label_and_nothing_else` | `argv_words`, the one reader of the cases *Scope* item 1 names. The docstring's account of what the parse closes moves to `argv_words` with it. |
| The name `test_the_template_PARSES_into_the_three_answers_it_ships` | `tests/behaviour/test_waiver_decided_at_start.py` | `test_the_template_PARSES_into_the_THIRD_axis_it_ships` (G7). |
| The citations of a row of `seal/follow-up.md` | The sentences G12 lists | Each states its reason itself (*Scope* item 6). |

This work adds one assertion to an existing case and lifts one reader to module level. In return it removes the guard and the folded reader above.

Framed 2026-11-10 by framer, before the build.
