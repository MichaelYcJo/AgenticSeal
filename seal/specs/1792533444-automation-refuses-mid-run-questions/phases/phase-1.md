# 1792533444-automation-refuses-mid-run-questions — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 30cf4f44 |

## What this phase was asked

`hooks/question-gate.py` in its own dispatch group `pre-question`,
registered in `hooks/hooks.json` for `AskUserQuestion`. It reads the
branch's declaration through `hooks/routing.py` and denies when `Automation`
reads `yes`, unless the call is the routing question put alone, recognised by
`worktree_consent.is_routing_question`. That predicate replaces the two
inline copies in `_routing_preset` and `_routing_answer`. Every other case is
silent. A new module, `tests/test_an_automation_run_puts_no_question.py`,
covers S1 to S13, each case seen red first.

The owner's direction for the build: no symbol a reader can trip on as
syntax, no value stated twice, no spelling a near miss could pass, the rule
once and compact. At the phase boundary the repository-wide meta modules,
every module naming `hooks.json` or `dispatch.py`, `bin/rules --check`,
`bin/fold-check`, `bin/settle --released-at HEAD` and `bin/unverified-check
seal/specs/` run beside the touched modules.

## What this phase found

- **The predicate keeps today's comparison, so each label counts once.**
  `spec.md` calls it a set comparison and also names `_routing_answer`'s
  inline comparison as the one to share. That comparison sorts both lists,
  so a doubled `automation` beside the three labels is refused. Kept, and
  held by `test_a_near_miss_of_the_routing_labels_is_refused`; the divergence
  is a row of `overview.md`.
- **The gate checks the exemption before it reads the declaration.** The
  routing question put alone passes whatever the declaration says, so the
  check that costs no `git` call goes first. A resumed run pays nothing for
  its re-ask.
- **The gate keeps no guard on `cwd`.** A draft refused a `cwd` that was no
  directory. `optin.repo_root` already answers an empty root for it, and
  `routing.for_branch` answers no declaration for that, so the guard stayed
  green under its mutation. A missing `cwd` is held instead by a case run
  from inside a declared repository
  (`test_a_payload_that_names_no_directory_is_silent`), so a gate that read
  its own process directory would refuse there.
- **The fallback for a path with no relative spelling has its case in the
  fail-open group.** `tests/test_gates_do_not_fail_open.py` already induces
  the Windows `relpath` raise for the commit gate's hint, and the question
  gate's case sits beside it.
- **The silent cases pass against a tree with no gate, so each was seen red
  by a mutation of the condition it holds.** Through `mutation-check`: the
  exact tool name, the one-question condition, the exemption, the `yes`
  comparison, the declaration read, the missing `cwd`, the JSON and object
  guards, each pinned phrase of the reason, the relative spelling and its
  fallback, the predicate's three conditions, its call in each of the two
  press readers, the `hooks.json` matcher and the `GROUPS` entry. Every run
  came back red. Replacing the predicate with `False` turned 48 cases of the
  two press-reader modules red, which is S13's evidence that both readers
  call it.
- **S12's census modules needed nothing.** `tests/test_chain_hooks_hardening.py`
  and `tests/test_a_script_says_which_interpreter_it_needs.py` pass with the
  new entry. `ruff.toml`'s `hooks/*.py` row already holds the gate at `py39`.
