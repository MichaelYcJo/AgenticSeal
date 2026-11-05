# Review round 1: 1793853195-the-dispatcher-passes-no-allow

```seal
target: 93662643d against release/v0.32.4
```

The range is 71cfd170 (routing), 6466441c (frame), ecfb7b58 (`hooks/dispatch.py#merge`, `#RANK`, the *Merging* docstring, the `EVENTS` comment and five `Test_merge` cases), 07ee1b48 (phase record, `gaps.md`, fragment), 31638309 (the "holds back" wording), 663f071d (the plan's Status cell) and 93662643 (the orchestrator's fold of three frame statements). There are no earlier rounds, so no fact is carried; every fact below was established this round. `seal/parity.md` is not declared, so no parity comparison is owed. `seal/config.md` has no `Record language` row, so this record is in English.

The axes walked: which decision values pass and in what spelling (inputs); which fields of a decision-less object leave on which event (exclusions and boundaries, deliberate non-exclusions); the order of the merged reason and which object the JSON path keeps (ordering and response shape); what `merge` does with a shape the gates do not print today (error paths); and the security axis, which here is whether any output path still lets a gate approve a call or change its input. Concurrency has no subject: `merge` is a pure function over one process's gate outputs. This change's own axes are the Python 3.9 floor the dispatcher is written for, and what a case pins against what the frame states.

## Findings

### 1. An `allow` with no reason, the issue's own shape, has no case, and the guard that keeps it from raising survives deletion

```seal
severity: should
location: `tests/hooks/test_dispatch.py:525-534`, `hooks/dispatch.py:225`
evidence: executed `bin/test tests/hooks/test_dispatch.py -q -p no:xdist` in a scratch clone at 93662643d with `hooks/dispatch.py:225` changed to `else:` (54 passed, exit 0), and `merge` called on a bare `allow` under that change with `/usr/bin/python3` 3.9.6 (raised `KeyError: 'permissionDecisionReason'`)
```

Why it matters: *Scope* 1 says a dropped decision's reason joins the gate's text "where it has one", and the build holds that condition with one guard, `elif hook_out.get("permissionDecisionReason"):` at `hooks/dispatch.py:225`. The most natural shape of an approving gate is `{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "allow"}}`, with no reason, and `readable` lets a null reason through as well (`hooks/dispatch.py:189-190`). Every new case builds its decision with the module's `decision(kind, reason)` helper (`tests/hooks/test_dispatch.py:80`), which always writes a reason, so no case reaches the branch where the reason is absent. With the guard replaced by `else:`, all 54 cases of the module still pass, and the same `merge` raises `KeyError` on a bare `allow`. That exception is raised in `merge`, outside `run_gate`'s isolation, so the whole group would end with a traceback and exit 1, the failure class #661 closed for unreadable output. A null reason under the same change appends `None` to the texts, and the join at `hooks/dispatch.py:282` would raise `TypeError` (read, not run). The crafter's eight mutation runs in `trail/phases/phase-1.md` *Mutation* include none on this guard, so the account's "8 mutants, 8 red, 0 survived" is accurate for the mutants it chose and says nothing of this one. The behaviour is one the diff added, so this is the *Regression test* row's `should` in `skills/code-review/SKILL.md`.

The case belongs beside the other dropped values in the first new case. Each new assertion is red with `hooks/dispatch.py:225` replaced by `else:`: the bare body raises `KeyError`, and the null one raises `TypeError` at the join.

```python
    def test_refuses_to_pass_on_a_decision_other_than_deny_or_ask(self):
        """#1381. A group whose only decision was a gate's `allow` printed it,
        and the plugin directory's validation holds back a plugin whose hook
        can approve a call.
        `Allow` and `defer` count as no decision too, and the gate's reason is
        kept as its text. An `allow` with no reason, or a null one, prints
        nothing."""
        d = dispatch_module()
        for kind in ("allow", "Allow", "defer"):
            out = d.merge([decision(kind, "ra")], "PreToolUse")
            assert out == "ra", (kind, out)
        for reason in ({}, {"permissionDecisionReason": None}):
            bare = {"hookEventName": "PreToolUse", "permissionDecision": "allow"}
            body = json.dumps({"hookSpecificOutput": {**bare, **reason}})
            assert d.merge([body], "PreToolUse") == "", reason
```

The snippet covers the case and its docstring. The fix pass also owes the phase record's *Seen red* and *Mutation* accounts a line for how the new assertions were shown red. `frame/design.md` *Data & interfaces* has no row for a reasonless `allow`, and the case holds without one.

## Confirmations

What matched: *Scope* 1 at `hooks/dispatch.py:221-228` and `:234-238`. A decision passes only where its lowercased value is in `RANK`, which holds `deny` and `ask` alone (`:119`), and the passed word is printed lowercased. Any other value adds its reason, where one exists, to the texts. The crafter claimed the new cases were red at 6466441c, 3 failed and 5 passed. This round checked out 6466441c's `hooks/dispatch.py` under HEAD's tests in a scratch clone and got 3 failed and 5 passed: the `allow` case on `assert '{...}' == 'ra'`, the lowercase case on `'Deny' == 'deny'`, and the input-change case on the printed `updatedInput` (executed).

What matched: the two green-at-base cases are held by the guards *Scope* 4 names. With `texts.append(hook_out["permissionDecisionReason"])` at `:228` replaced by `pass`, `test_accepts_an_ask_beside_an_allow_and_keeps_both_reasons` failed on its own assertion with the reason `rk`. With the `block` exception at `:275` replaced by `False`, `test_accepts_a_block_without_a_decision_as_the_gate_printed_it` failed on `{'reason': 'r'} == {'decision': 'block', 'reason': 'r'}` (executed, both in one run in the scratch clone; each case failed on the line naming its guard). This matches the crafter's account of the failing lines.

What matched: *Scope* 2 at `hooks/dispatch.py:263-281`. On `PreToolUse` alone, the first decision-less object loses `hookSpecificOutput.updatedInput` and any top-level `decision` that is not `block` in any case, and every other field stays. On `PostToolUse` both shapes print whole. A probe over twelve shapes under `/usr/bin/python3` 3.9.6 printed what *Data & interfaces* gives and showed more. `BLOCK` stays. `decision: null` and `decision: 1` leave. A later object's `updatedInput` never reaches stdout, because the JSON path keeps only later objects' `systemMessage`s. A `deny` carrying `updatedInput` prints the three-field decision object without it. `allow`, `ask` and `deny` together print `deny` with the reason `rk`, `rd`, `ra`, the dropped reason last, as the phase record says (executed; *Probes*).

What matched: the crafter's claim that a lone `{"decision": "approve"}` prints `{}`, and its *Not done* entry that a dropped reason beside a decision-less object is not printed. The probe's `allow` beside an `updatedInput` object printed that object without `updatedInput` and without `ra`. That matches *Scope* 1 as the fold at 93662643 words it (executed).

What matched, as weighed and not a finding: a dropped decision's object is discarded whole apart from its reason. The probe's `allow` carrying a top-level `block`, a `reason` and `continue: false` printed `ra` alone. At 71cfd170 the decision path also built a fresh three-field object and dropped those fields, so the change takes nothing a gate had before. No gate prints the shape (executed: `grep -n 'permissionDecision\|"decision"\|updatedInput' hooks/*.py hooks/lib/` lists the `deny` and `ask` objects of `question-gate.py`, `review-skill-gate.py`, `mode-gate.py` and `routing-edit-gate.py` alone). The frame's and the fragment's sentence that a `block`, `continue: false` and `stopReason` still pass is said of the JSON path, and holds there.

What matched: *Scope* 3. The *Merging* paragraph at `hooks/dispatch.py:17-23`, the comment above `RANK` at `:116-118` and the rewritten `EVENTS` comment at `:110-113` each state what the code does (read). The `EVENTS` comment's claim that the JSON path now reads the event name matches `:265`.

What matched: S3 and S5. `git diff release/v0.32.4..HEAD -- tests` removes no line, so the existing `Test_merge`, `Test_classify` and `Test_report` cases are unedited, and `bin/test tests/hooks/test_dispatch.py -q -p no:xdist` ends 54 passed, exit 0, in the worktree at HEAD (executed). `uvx ruff check` and `uvx ruff format --check` on the two files exit 0 (executed).

What matched: each new test against its group. `seal layout --pairs` names no pair in `tests/hooks/test_dispatch.py`, whose `TARGET` is `hooks/dispatch.py` (executed). Read against the three cases `Test_merge` held at the base, each new case holds a fact none of them holds: a dropped value, a dropped reason kept beside an `ask`, the lowercase word, the two removed fields on `PreToolUse` and their absence on `PostToolUse`, and a `block` kept. Each holds a *Scope* 1 or *Scope* 2 sentence.

What matched: the crafter's count of 18 modules naming the dispatcher. `git grep -l -E 'dispatch\.py|"dispatch"|run_dispatch' -- tests evals`, less `tests/conftest.py` and `tests/censuses.py`, lists 18 (executed). The 818-passed run over them was not re-run here.

What matched: the rule change. Its `from:` is the text of `docs/checks/the-session-hooks.md:12-14` up to line breaks (read), and `bin/seal rules --check` exits 0 (executed). The chain check over the worktree printed no notice at a line of `frame/design.md` naming a test pin or a copy (executed).

What matched: the closed set of rule 12. The work item's files that state the present were read whole: `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `trail/phases/phase-1.md`. None contradicts HEAD. The plan's *Technical context* and the design's *Grounding* now say their line numbers are at 71cfd170, which is where they hold. The phase record calls its tree-wide list a sample by wording, and it is one.

What matched: the honesty of the `unverified` label. `gaps.md` *Not verified* names the full suite, the repository-wide lint and the format check at HEAD as unverified and names the orchestrator's broad run as their answerer (read). This round leaves one finding open. When it closes, the orchestrator's broad run and then the sealer's spawn come due.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD, among them the modules that read the records under `seal/threads/` | the `Broad gate` row of `seal/config.md` | the orchestrator's broad run, then the sealer |
| The new cases on the ubuntu and Windows legs | `.github/workflows/test.yml` | the `tests` workflow on the pull request |
| Whether the change clears `HOOK_GRANTS_PERMISSION` in the plugin directory's validation | `frame/questions.md` Q1 | the owner, on resubmitting the next release's `dist` |
| How Claude Code reads the plain text a `PreToolUse` group now prints for a lone dropped decision with a reason, which the frame's hooks-reference row says goes to the debug log | `frame/design.md` *Grounding* | the frame's reading of the hooks reference; no session here ran Claude Code against it |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the worktree into the round's scratch directory at 93662643d, then `git checkout 6466441c -- hooks/dispatch.py` and `bin/test tests/hooks/test_dispatch.py -q -p no:xdist -k Test_merge` | 3 failed, 5 passed; the failures are the three cases the crafter named, on the lines it named |
| the same run at HEAD's `hooks/dispatch.py` with `:228` changed to `pass` and the `block` exception at `:275` changed to `False` | 3 failed, 5 passed: `allow` case on `'' == 'ra'`, `ask` beside `allow` on reason `rk`, `block` case on the missing `decision` |
| the full module with `:225` changed to `else:` | 54 passed, exit 0: no case pins the guard (finding 1) |
| `/usr/bin/python3 -I` (3.9.6) calling `merge` on a bare `allow` with `:225` changed to `else:` | raised `KeyError: 'permissionDecisionReason'` |
| `/usr/bin/python3 -I test_tmp_merge_shapes.py <clone>/hooks/dispatch.py`, twelve shapes on `PreToolUse` and `PostToolUse` at HEAD | exit 0; results as *Confirmations* gives them. The file, the clone and the scratch directory were removed after the runs |
