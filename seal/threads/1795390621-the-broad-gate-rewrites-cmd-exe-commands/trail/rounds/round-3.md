# Review round 3: 1795390621-the-broad-gate-rewrites-cmd-exe-commands

```seal
target: f8013d705ab132a376fa7752955915f5edcbf07a, fixes d0b7050d5..f8013d705
```

This is a verifying round. `d0b7050d5` is the commit of round 2's record, so the fix diff is `d0b7050d5..f8013d705`. It holds the orchestrator's row `1bd8b6777`, the case `286aa3e22`, the code fixes `0ab41dd04` and `747b86dc9`, the close blocks `168658a3a` and the orchestrator's fold `f8013d705` (executed: `git log --oneline origin/release/v0.38.6..HEAD`, `git diff --stat d0b7050d5..f8013d705`). The base `release/v0.38.6` resolves to `3c89a70d5`, which this branch has not merged. That merge is the orchestrator's, before the broad run.

Carried from earlier rounds and not established again: the list of cases that run the gate over a key (`trail/phases/phase-1.md` *The cases the Windows leg may now refuse, listed whole*), the phase records' mutation counts, and the fix pass's `seal mutate` counts in round 2's close blocks. Two of those mutants were written again and run, as *Probes* names. The confirmations of round 1's findings 1, 3, 4 and 6 in round 2 were not re-derived, except where the fix diff touched the text they rest on.

The records were read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, the three phase records and rounds 1 and 2. `seal/config.json` names English for both language keys, so no `pr.<lang>.md` is owed.

## Findings

### 1. The template's condition for a key that stays inside the reading still admits a name in a directory an earlier command makes, which the same bullet gives as an example of a name neither refused nor named

```seal
severity: should
location: `templates/setup/config.md:302-313`
evidence: read `templates/setup/config.md:296-313`, `skills/verify/scripts/broad_gate.py:779-795`, `skills/verify/scripts/broad_gate.py:818-823`, `skills/verify/scripts/broad_gate.py:921`; executed `python3 -I <scratchpad>/1795390621-the-broad-gate-rewrites-cmd-exe-commands/round-3/test_tmp_round3.py <clone>`
reopens: round-2#1
```

Why it matters: the close of round 2's finding 1 holds for the code and for the cut. It does not hold for the sentence of that finding at `templates/setup/config.md:308-311`, now `:310-313`. Round 2's grounds were that the sentence "gives the condition under which a key stays inside the reading", and that a key can meet every part of it "yet the reading cannot answer it". The fix added that each name "stands before the first `"`, `^` or `%`". That removes `%PY%/python.exe`, the one instance round 2 named, and leaves the rest of the class.

The bullet at `:302-313` states two things that disagree. Its first sentences say a name is neither refused nor named where its "part before the `/` is a directory only once the line has run", and they give "a name in a directory an earlier command makes or a `cd` enters" as an example. Its last sentence says a key stays inside the reading where each command name is the first word of its command, stands before the first cut character, has nothing glued in front of it, and every separator has a blank on each side. `mkdir out && out/tool -q` meets all of that. `not_as_written` asks `in_root(root)` before anything runs (`broad_gate.py:921`, `:818-823`), and the root holds no `out/`. So `out/tool` is neither refused nor named (`broad_gate.py:792-794`), and `cmd.exe` then fails on it as it does on `bin/test -q`. A person who checks a key against the condition is told it is inside the reading when it is not.

The bullet's first sentence also misses one shape that the cut now produces. The probe asked `%B%/test -q` on `cmd.exe` in a root that holds `bin/`. The gate returned `None` and wrote nothing to stderr. The name reaches the cut, so it is never refused, and its part `%B%` names no directory as written, so the not-read line does not name it either. `cmd.exe` expands `%B%` as it reads the line, before anything runs, so "only once the line has run" does not cover it. The fixed last sentence already puts this key outside the reading. Only the first sentence's account of which names escape is short.

The fix touches the two sentences of the one bullet. No other text states the condition: `not_as_written`'s docstring points at the template for it, and `changelog.md` and `frame/design.md` *Scope* item 6 do not state it (read). The snippet assumes no precondition at an OS boundary.

```markdown
- **A name `cmd.exe` runs where the reading takes none is neither refused
  nor named**, and `cmd.exe` fails on it as it does on `bin/test -q`. That
  is any command name that does not stand as the first word, or as the
  word after a separator word with a blank on each side, or whose part
  before the `/` is a directory only once `cmd.exe` has expanded a
  variable in it or the line has run. Examples are a name behind a
  leading `@`, as in `@bin/test`, a name after a redirection that opens
  its command, as in `>out.txt bin/test`, a name after a separator glued
  to a word, as in `a&& bin/x`, a name such as `%B%/test`, and a name in
  a directory an earlier command makes or a `cd` enters. A key stays
  inside the reading where each command name, with nothing glued in front
  of it, is the first word of its command and stands before the first
  `"`, `^` or `%`, where no command makes or enters a directory that a
  later command name starts in, and where every separator has a blank on
  each side.
```

```seal
verdict: deferred the pull request body
answer: The run stops at this round, as the orchestrator's row in `frame/plan.md` *Judgments of the run* on round 2's three findings said it would unless this round opened a `must`, and the stop row on round 3 weighs it. The finding is a `should` in two sentences of `templates/setup/config.md` *Broad gate*: the code and the cut sentences hold, and the gate's behaviour for `mkdir out && out/tool -q` and `%B%/test -q`, neither refused nor named, is what the bullet's first sentence states. A fix to a shipped file after the last round is owed a verifying round, and the stop row spends no round on a finding that is not a `must`. No open issue owns the template's *Broad gate* paragraphs and no party has agreed to act on it, so it takes rung 4: this record and the pull request body, which quotes the finding's heading.
```

## Confirmations

```seal
confirms: round-2#2
```
What holds: `Test_not_as_written#test_refuses_a_wrapped_value_with_only_its_form_off_as_meant` (`tests/skills/test_broad_gate.py:685-708`) asks the three older forms under `/bin/sh`, under a `COMSPEC` naming another shell and under `cmd.exe`, in a root that holds `bin/`, and asserts the key as meant `bin/test -q` (read). The unit round 2's finding named, `as_cmd_exe_runs`, is gone, so its evidence line cannot be run again as written. Its probe was written again as the mutant that matters now: the backtick branch turning `bin/test` in the key as meant. The new case's three backtick rows went red, and so did one row of the older `test_refuses_a_wrapped_or_backgrounded_value` (executed, *Probes*). A mutant that turned names on `cmd.exe` alone, as `as_cmd_exe_runs` did, is held by the `cmd-exe` rows alone, and those rows are new.

```seal
confirms: round-2#3
```
What holds: no sentence in the tree now says the key a refusal offers is one the gate runs (executed: `git grep -n -i -E 'one the gate runs|one it runs|as_cmd_exe_runs'` outside `seal/threads`, no line). The three branches of the older forms take off their form and nothing else (`broad_gate.py:899`, `:907`, `:917`, read). `changelog.md:3`, `not_as_written`'s docstring at `broad_gate.py:875-877` and `templates/setup/config.md:343-349` each say the key as meant removes the named form and nothing else, and that a second refused form is refused by name on the next run (read). The probe followed each key as meant until the gate answered `None`. `` `bin/test -q &` `` is refused three times on `cmd.exe`, first for the backticks, then for the `&`, then for `bin/test`. `` $(`bin/test -q`) `` is refused three times as well. Each refusal names its own form, and the chain ends at `bin\test -q` (executed, *Probes*). That is what the four texts say.

What matched: the code half of round 2's finding 1. `names_in_a_directory` refuses a name only where it ends before the cut (`broad_gate.py:792-794`), and `backslashed` turns only such a name (`broad_gate.py:812-814`, read). A word cannot end at the cut, because the cut character is no blank and so belongs to the word before it. So `<=` and `<` give the same lists, as the close says. `bin/%TOOL%/x -q` and `bin/"a b"/x -q`, round 2's two probe values, now return `None` and name their word on stderr (executed). Changing the bound to `at < cut` turned the three new rows of `test_names_what_it_did_not_read_and_runs_it_as_written` red, and nothing else (executed). The refusal's `cmd.exe runs` list is each refused name with every `/` turned (`broad_gate.py:929`). A refused name holds no cut character, so the list names only spellings the gate read whole (read). The template's sentences at `:282-283` and `:285-294` and the changelog sentence on the cut match the code (read). Finding 1 is the part that does not hold.

What matched: `frame/design.md` *Scope* items 1 and 2, as folded at `f8013d705`, state the code at the target: a name refused and turned only where it ends before the cut, the older forms' key as meant on every shell, and the not-read list (read). The *User scenarios* row *A value the reading stops in* still holds. `bin/test` in `bin/test "a b" && bin/x` ends before the cut and is refused, and `bin/x` is named (read: `test_a_refusal_carries_what_it_did_not_read`). `frame/plan.md:11` and its first *Alternatives considered* row still hold at the target (read).

What matched: each of the eight quotes of `pr.md` stands word for word at its source, once, with runs of whitespace collapsed (executed: a comparison of each quote with `frame/plan.md`, `routing.md`, `gaps.md` and `frame/questions.md`). The new line 8 quotes `gaps.md:11`. No sentence `pr.md` quotes changed in the fix diff except by that addition. The fix diff changes no `gaps.md` row (executed: `git diff --stat d0b7050d5..f8013d705`).

What matched: the narrow run of the four modules over `broad_gate.py` and its documents passed at the target (executed, *Probes*). The fix diff's new cases, read against `Test_not_as_written`: the three new rows of `test_names_what_it_did_not_read_and_runs_it_as_written` each hold a name that reaches the cut, which no other row does. The three-shell wrapped case holds the older forms' key as meant in a root that holds `bin/`, which `test_refuses_a_wrapped_or_backgrounded_value` does not. `test_refuses_a_name_the_cut_splits_by_naming_it_whole` left with the behaviour it pinned. `test_refuses_a_name_that_stands_again_past_the_cut_with_one_spelling` still holds `backslashed`'s bound. Its docstring speaks of "the one spelling", which the list's de-duplication no longer decides, and the round opens nothing for that (`tests/skills/test_broad_gate.py:855-863`, read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether `pr.md` quotes the row of `frame/plan.md` *Judgments of the run* on round 2's three findings. That row decides that a name reaching the cut is never refused, and it reverses round 1's fix of its finding 2. Both change what a Windows user sees, and the owner has not seen either | `frame/plan.md:60`, `pr.md:1-8` | the orchestrator, who writes `pr.md` |
| What `cmd.exe` does with the template's examples, with a drive path written with `/`, with a name that holds a `"`, `^` or `%` after its `/`, and with this repository's key | `gaps.md:8-11`, `frame/questions.md:14` | a measurement on a Windows machine, as `gaps.md` names. Finding 1 rests on the gate's code and the template's own text, not on such a run |
| The broad gate: the full suite, the lint and the format check, after the merge of `3c89a70d5`. No crafter hand-back reached this round, so no `unverified` label was there to check | `seal/config.json:5` | the orchestrator's broad run |
| The `cmd.exe` half of `Test_run`'s two real-platform cases | `gaps.md:7` | CI's `windows-latest` leg, read by the orchestrator at the pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_broad_gate.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py tests/text/test_broad_gate_rule.py -q -p no:xdist`, in a `git clone --no-local` of the branch at the target | exit 0, 234 passed and 1 skipped |
| `python3 -I <scratchpad>/1795390621-the-broad-gate-rewrites-cmd-exe-commands/round-3/test_tmp_round3.py <clone>`, run once. It loads `broad_gate.py` from the clone, asks `not_as_written` in a temporary root holding `bin/`, and follows each key as meant until the gate answers `None` | On `cmd.exe`: `bin/%TOOL%/x -q`, `bin/"a b"/x -q` and `bin/test%X% -q` each return `None` and name the word on stderr. `%B%/test -q` and `%PY%/python.exe -m pytest` return `None` with nothing on stderr (finding 1). `` `bin/test -q &` `` and `` $(`bin/test -q`) `` are each refused three times, once per form, and end at `bin\test -q`. This repository's key returns `None`. Under `/bin/sh` the three older forms are offered `bin/test -q`, and that value returns `None` |
| `Test_not_as_written` over `tests/skills/test_broad_gate.py` and `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`, in the clone, with the backtick branch's key as meant changed through `Edit` to `backslashed(value[1:-1].strip(), ["bin/test"])` | exit 1, 4 failed: the three backtick rows of `test_refuses_a_wrapped_value_with_only_its_form_off_as_meant` and the backtick row of `test_refuses_a_wrapped_or_backgrounded_value` (confirmation of round-2#2) |
| `Test_not_as_written` over `tests/skills/test_broad_gate.py`, in the clone, with `names_in_a_directory`'s bound changed through `Edit` from `at + len(word) <= cut` to `at < cut`, and then restored through `Edit`. `git diff --quiet` exited 0 afterwards | exit 1, 3 failed: the `bin/%TOOL% -q`, `bin/"a b"/x -q` and `bin/x^& && echo` rows of `test_names_what_it_did_not_read_and_runs_it_as_written` |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.38.6 --root <worktree> --worktree`, before this record stood | exit 0. No notice at `frame/design.md`. It names round 2's three closed findings as owing a verifying round, and names the gate and guarantee records as absent |
