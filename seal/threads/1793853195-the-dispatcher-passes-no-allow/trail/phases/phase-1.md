# Phase 1: 1793853195-the-dispatcher-passes-no-allow

## What this phase found

**The frame holds against the tree.** `git diff --stat 71cfd170 6466441c` lists only the three frame files, so the code the build started from is the code the frame's probe measured (executed). `RANK` stood at `hooks/dispatch.py:111`, and `merge`, `readable` and `classify` read as the plan's *Technical context* says (read). No gate prints `allow`, `defer`, `approve`, `updatedInput` or a top-level `decision`: `grep -n -E 'decide\(|"allow"|"defer"|updatedInput|"decision"|"approve"' hooks/*.py` outside `dispatch.py` found only the `decide` calls of `mode-gate.py` (`deny`, `ask`), `review-skill-gate.py` (`ask`, `deny`) and `routing-edit-gate.py` (executed). The policy sentence the rule change replaces stands at `docs/checks/the-session-hooks.md` lines 13 and 14 (read).

**A dropped decision's reason joins the texts after the decisions' own reasons.** `allow` `ra` beside `ask` `rk` prints the reason `rk\n\nra` (executed under `/usr/bin/python3` 3.9.6). The merged reason was already the decisions' reasons followed by the texts, and a dropped decision's reason is now one of the texts, in gate order. Judged against `frame/design.md` *Scope* 1, which asks that the reason be kept as plain text is.

**Where a dropped decision stands beside a decision-less JSON object, its reason is not printed.** The JSON path prints the first object, and plain text beside it was not printed at `71cfd170` either. This is the reading taken of *Scope* 1's "printed as plain text where no decision passes": the reason is treated as plain text is, and that sentence holds where no such object stands beside it. No gate prints a dropped decision or decision-less JSON on `PreToolUse`, so no output changes. A dropped decision object's own `systemMessage` is not kept either, as the decision path did not keep it at `71cfd170`. Judged against `frame/design.md` *Scope* 1 and *Data & interfaces*.

**A lone `{"decision": "approve"}` is printed as `{}`.** The JSON path removes the field and prints what is left, as *Scope* 2 says. Claude Code reads an empty object as no decision. *Data & interfaces* lists the shape with a `reason`, which prints `{"reason": "r"}` (executed under 3.9.6).

**A top-level `decision` that is not a string is removed too.** *Scope* 2 keeps a value that, lowercased, is `block`. A value that is not a string has no lower case and is not `block`, so it leaves. `readable` lets such an object through, because it asks only of `hookSpecificOutput` and `systemMessage`. Judged against *Scope* 2.

**A comment the frame did not name was untrue after the change.** The comment above `EVENTS` said the event name was "Read only on the decision path". The JSON path now reads it to remove two fields on `PreToolUse` alone. The comment is rewritten in place in the same commit. Judged against `skills/core/SKILL.md` *The rule a mechanism is kept against*.

**Three assertions beyond *Scope* 4's list,** each because a unit the scope adds had no case that could fail on it. Judged against `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test* and contract rule 15.
- `test_accepts_a_deny_or_an_ask_in_any_case_and_prints_it_lower_case` is a new case. *Scope* 1 prints the lowercase word, and none of the four listed cases holds a `Deny` or an `Ask`. It is red at `6466441c`: `assert 'Deny' == 'deny'`.
- `test_refuses_to_pass_on_an_input_change_or_an_approval_without_a_decision` also asserts that both objects are printed whole on `PostToolUse`. S5's existing assertion uses an object with a falsy `hookSpecificOutput` and no `decision`, which the removal leaves alone on any event, so it cannot see the `PreToolUse` condition.
- `test_accepts_a_block_without_a_decision_as_the_gate_printed_it` also holds `Block`, so the lowercase comparison of *Scope* 2 has a case.

**Seen red** (executed). The five new cases were written before the code. `bin/test tests/hooks/test_dispatch.py -p no:xdist -q -k Test_merge` ran the eight cases of `Test_merge` against the code at `6466441c` and ended 3 failed, 5 passed.
- `test_refuses_to_pass_on_a_decision_other_than_deny_or_ask` failed on `assert out == "ra"`, with the `allow` decision printed as JSON. The loop stops at its first value, so `Allow` and `defer` were read apart: `merge` from `git show 6466441c:hooks/dispatch.py`, called in one `python3 -I` process, printed each as the group's `permissionDecision`. The same run printed `ASK` in the gate's spelling, and the `approve` object whole.
- `test_accepts_a_deny_or_an_ask_in_any_case_and_prints_it_lower_case` failed on `'Deny' == 'deny'`.
- `test_refuses_to_pass_on_an_input_change_or_an_approval_without_a_decision` failed on its first assertion, with `updatedInput` printed.
- `test_accepts_an_ask_beside_an_allow_and_keeps_both_reasons` and `test_accepts_a_block_without_a_decision_as_the_gate_printed_it` passed there, as *Scope* 4 expects. Each was shown red by the mutation *Scope* 4 names, below. Their failing lines were read: `assert "ra" in reason and "rk" in reason` with the reason `rk`, and `{'reason': 'r'} == {'decision': ..., 'reason': 'r'}`.

**Mutation** (executed, after commit `ecfb7b58`). One `seal mutate hooks/dispatch.py` per break, each over `bin/test tests/hooks/test_dispatch.py -q -p no:xdist -k Test_merge`. Each baseline passed, and each verdict was `red`, exit 0.
- The filter `if hook_out["permissionDecision"].lower() in RANK:` replaced by `if True:`. The `allow` case and the `ask` beside `allow` case went red.
- The line that keeps a dropped decision's reason, `texts.append(hook_out["permissionDecisionReason"])`, replaced by `pass`. The same two cases went red.
- The `.lower()` on the passed word removed. The lowercase case went red.
- The `updatedInput` condition replaced by `False`. The input-change case went red.
- `del merged["decision"]` replaced by `pass`. The input-change case went red.
- The `block` exception replaced by `False`. The `block` case went red.
- `verdict.lower() == "block"` replaced by `verdict == "block"`. The `block` case went red on `Block`.
- `if event_name == "PreToolUse":` replaced by `if True:`. The input-change case went red on its `PostToolUse` assertion.
- Result: 8 mutants, 8 red, 0 survived. `git status --short` was empty after the runs.

**S3 and S5** (executed). `git diff 6466441c ecfb7b58 -- tests/hooks/test_dispatch.py` removes no line, so the existing `Test_merge`, `Test_classify` and `Test_report` cases are unedited. `bin/test tests/hooks/test_dispatch.py -q` ended 54 passed, exit 0.

**Python 3.9** (executed). `merge` was loaded and called under `/usr/bin/python3` 3.9.6 for a lone `allow`, `allow` beside `Ask`, and an `approve` with and without a reason. Each printed what *Data & interfaces* gives. CI has no 3.9 leg (`frame/design.md` *What a change to a gate must carry*).

**The phase boundary** (executed). One `bin/test ... -q` command ran the 18 test modules that name `dispatch.py`, `"dispatch"` or `run_dispatch` (`git grep -l` under `tests/` and `evals/`; `tests/conftest.py` and `tests/censuses.py` are not test modules). It ran over the tree of `ecfb7b58` with `gaps.md`, `changelog.md`, this record and the Status cell written, and ended 818 passed, exit 0. The spawn narrowed the run to those modules, so no other module that reads `seal/threads/` for its records was added, and `gaps.md` `## Not verified` names them.

**Other statements of the rule across the tree, a sample by wording** (contract rule 12). `git grep -n -i -E 'strictest|deny over ask|deny, then ask|over silence|\bRANK\b|updatedInput|permissionDecision.{0,20}allow|"allow"'` and `git grep -n -i 'permissionDecision'` ran outside `seal/threads/` over `docs`, `skills`, `agents`, `hooks`, `templates`, `README.md` and `CONTRIBUTING.md`. Rewritten in place: the module docstring's *Merging* paragraph, the comment above `RANK`, and the comment above `EVENTS`. Left standing, with why:
- `docs/checks/the-session-hooks.md` lines 13 and 14. `frame/design.md` *Rule changes* replaces them at the settle.
- `.test_durations` names `test_accepts_the_strictest_decision_and_keeps_every_reason`. That case still exists and still holds: `deny` over `ask` is the stricter of the two.
- The docstring's "A skipped gate used to read exactly like an allow" and `run_gate`'s comment on reading like an allow. Both say that a failed gate prints nothing, and that is unchanged.

**Removals.** Each row of `## Removes` went as it says. The `0` default of `RANK.get` and the `winner` variable went with the second row's winner. No removal falls outside `## Removes`.
