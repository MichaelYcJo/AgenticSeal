# Review round 1: 1793201097-two-environment-variables-still-carry-the-old-brand

target: 958f2f3e against origin/release/v0.24.0

## Findings

### 1. The option's help text tells a person the system locale decides when the option is empty, while through 0.24.x `SPECSEAL_LANG` decides first

severity: should
location: `.claude-plugin/plugin.json:25`, `tests/behaviour/test_chain_hooks_hardening.py:180`
evidence: read `.claude-plugin/plugin.json:25`, `hooks/worktree-guard.py:249-252`
verdict: fixed 3bee2ec4

The plugin manifest reference that `frame/design.md` *Grounding* cites
(`code.claude.com/docs/en/plugins-reference`, *User configuration*, read this
round) says Claude Code prompts for every `userConfig` option when the plugin
is enabled, shows `description` as the help text beneath the field, and shows
each option as a row in `/config`. So this sentence is what a person reads at
the moment they decide whether to fill the field. It says *Left empty, the
system locale decides.* `hooks/worktree-guard.py:252` reads `SPECSEAL_LANG`
before the locale whenever the option is empty. The person the fallback
exists for, the owner with `SPECSEAL_LANG=ko` and an `en_US.UTF-8` locale
(`frame/design.md` *What history asks for it*), is told that leaving the
field empty gives English, which is false through every 0.24.x release.

The crafter named this (`trail/phases/phase-2.md` *The manifest's description
is the frame's text, kept as given*): the text is the frame's, kept because it
states the option's lasting behaviour, and the README row states the
fallback. Claimed X: the README carries the fallback. Found: it does
(`README.md:287`, `README.ko.md:280`), but the dialog and `/config` are where
the person sets the option, and neither shows the README. The frame's text
is a defect the build copied, not grounds for it. The next minor release that
removes the read at line 252 also removes the clause below, alongside the
census entry it already removes.

The fix keeps the frame's other two sentences and pins the clause, so the
case that already pins the option's fields also catches the text drifting
back (contract rule 14). It departs from `frame/design.md` *Data and
interfaces*, so the fix pass records it as a divergence in `gaps.md`.

```json
      "description": "The language of the worktree guard's prompts: ko or en. Left empty, the variable SPECSEAL_LANG decides through 0.24.x, then the system locale. The other gates speak English."
```

```python
    # in test_every_option_the_manifest_declares_is_one_a_hook_reads, beside
    # the type assertion; the next minor release removes it with the read
    assert "SPECSEAL_LANG" in option["description"], option
```

answer: The finding holds. The description now reads "Left empty, the variable SPECSEAL_LANG decides through 0.24.x, then the system locale.", keeping the frame's other two sentences, and S5 asserts that the description names `SPECSEAL_LANG`, with a comment saying the next minor release removes the assertion with the read. The assertion was seen red first, against the old description (executed, exit 1, `assert 'SPECSEAL_LANG' in "... Left empty, the system locale decides. ..."`). A `seal mutate` mutant that puts the frame's sentence back is red (executed). `gaps.md` records the departure from `frame/design.md` *Data and interfaces* as a divergence. The sweep for other sentences that say what an empty option does without the fallback found none in the living tree: both README rows, the `_lang` docstring and comments, the census comment and the changelog fragment each name `SPECSEAL_LANG` first (executed, `git grep -n -i` for "left empty", "is empty" and "비워"). `trail/phases/phase-2.md` *The manifest's description is the frame's text, kept as given* is left as written. It records the decision phase 2 made, and a fix pass writes no phase record. The frame's own sentence at `frame/design.md:80` is not this pass's to edit. The fragment needs no change, because it does not quote the description.

### 2. The S5 case can never pass once the guard and its option both leave, though its docstring says it turns green then

severity: should
location: `tests/behaviour/test_chain_hooks_hardening.py:173-181`
evidence: read `tests/behaviour/test_chain_hooks_hardening.py:173-191`
verdict: fixed 3bee2ec4

The docstring ends *If the guard leaves, this case is red until its option
leaves with it.* `frame/plan.md` *Technical context*, second failure scenario,
asks for the same thing: #1049 may remove the guard in 0.24.1, and the case
is to go red until the option goes too, then stand as the check for whatever
options remain. Line 179 reads `declared.get("worktree_guard_language", {})`
and line 180 asserts `sorted(option) == ["description", "title", "type"]`.
Once the declaration is gone, `option` is `{}`, `sorted({})` is `[]`, and
line 180 fails whatever `hooks/` holds. So the crafter of #1049 cannot make the
case pass by removing the option, as the docstring tells them to. They have
to rewrite or delete the case, and the general check at line 191, the reason
`trail/phases/phase-2.md` gives for placing the case in this file, leaves with
it.

The fix makes the shape check apply only where the option is declared. Each
mutant `trail/phases/phase-2.md` lists stays red: a missing or misspelt
`userConfig` or key leaves the guard's read with no declaration, which the set
comparison at line 191 refuses, and a wrong `type`, an added `default` or a
removed `title` still reach the shape assertions.

```python
    declared = json.load(f).get("userConfig", {})
    option = declared.get("worktree_guard_language")
    if option is not None:
        assert sorted(option) == ["description", "title", "type"], option
        assert option["type"] == "string", option
```

answer: The finding holds. S5 now checks the option's fields, and the description assertion of finding 1, only where `userConfig` declares `worktree_guard_language`. The docstring says so, and its last sentence is now true. I removed both the declaration and the guard's read in a `git archive` extract. At `99c1649a` the case failed there on `assert [] == ['description', 'title', 'type']`, exit 1. At `3bee2ec4` it passed, exit 0 (both executed, each extract removed after its run). With the read in place, every mutant `trail/phases/phase-2.md` lists stays red at `3bee2ec4` (executed, `seal mutate`): `userConfig` misspelt, the key misspelt, `type` set to `boolean`, a `default` added, `title` removed, plus two new mutants, the description clause reverted and the whole `userConfig` block removed. That is 7 mutants, 7 red, 0 SURVIVED. The option's variable misspelt in `hooks/worktree-guard.py` is also red. `gaps.md` records the conditional check as a divergence from `frame/design.md` S5.

## Confirmations

confirms: none
S1 holds. `hooks/lint-python.py` reads no environment variable: `grep -n
environ hooks/lint-python.py` printed nothing and exited 1 (executed). The
docstring sentence and the off-switch case are gone in the diff (read).

confirms: none
The crafter named the removal of the `env` parameter of
`tests/hooks/test_lint_python.py#_ran`. Claimed: only the deleted case passed
it. Found: every remaining call at `tests/hooks/test_lint_python.py:72-108`
passes three arguments, and `grep -n 'env='` finds none (executed). The
removal is part of the case `frame/design.md` *Removes* names.

confirms: none
S2, S3 and S4 hold at `hooks/worktree-guard.py:241-256`: the option first,
then `SPECSEAL_LANG`, then `LC_ALL` and `LANG`, with an empty value counting as
unset at each step, and a comment at the old read saying the next minor
release removes it. The new case in `tests/hooks/test_worktree_guard.py`
*Test_module* covers both spellings of unset, and the module passed in this
round's narrow run (executed). The red runs and mutants in
`trail/phases/phase-2.md` are the crafter's account and were not re-run.

confirms: none
The manifest's shape matches the reference *User configuration* (read this
round): `type`, `title` and `description` are the three required fields, the
key uses letters and underscores only, and there is no `options`, which is the
one field the reference says stops Claude Code before v2.1.271 from loading
the plugin. The `/config` row needs v2.1.269 and only the row depends on it.
`claude plugin validate .` exited 0 with the one `CLAUDE.md` warning (executed).
A probe copy with a misspelt key inside the option made the same command
exit 1 with `Unrecognized key`, so the validator reads this manifest's strict
object (executed, `## Probes`).

confirms: none
The S5 widening is sound as far as it goes. The case reads every `.py` file
under `hooks/`, which holds `hooks.json`, `lib` and the scripts and no
non-Python hook script (executed, `ls hooks`). The wider reading still covers
the guard, so it holds the frame's S5 row. Finding 2 is about the first
assertion, not the widening.

confirms: none
The `claude plugin validate .` divergence in `gaps.md` holds. The single
warning is `CLAUDE.md at the plugin root is not loaded as project context`,
and it names no file this branch changed (executed this round). The reference
lists that warning for any `CLAUDE.md` at a plugin root.

confirms: none
No living sentence states either old variable as current. `git grep -n -i`
for both names over the tree outside `seal/threads/` and `changelog/0.*`
finds only the new README rows, the read and docstring at
`hooks/worktree-guard.py:242` and `:252`, the census entry with its fallback
comment, the conftest comment saying the author's machine exports
`SPECSEAL_LANG=ko`, which is still true, and the tests (executed). Nothing
under `docs/`, `skills/`, `agents/` or `templates/` names either variable or
the guard's prompt language (executed). `.github/scripts/plugin_directory_check.py`,
the other manifest reader the plan did not list, reads `name` only (read).

confirms: none
S6, S7 and S8 hold. Both README switch tables replace the `SPECSEAL_LANG` row
with the option's row, naming `/config`, the fallback and its end (read). The
`_LINT` census item is gone and the `_LANG` item's comment names the fallback
(read), and `tests/test_censuses.py` passed (executed). The fragment names the
removal, the option, and what someone with `SPECSEAL_LANG=ko` does (read). It
is in the form other work items in `faf093f1` use, so Q2's default holds:
`origin/release/v0.24.0` is still `faf093f1` (executed).

confirms: none
The suite's label is honest. `gaps.md` *Not verified* labels the full suite,
lint and typecheck unverified with the orchestrator answering.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether a Claude Code version from before `userConfig` existed strips the field and loads the plugin. The reference states that an unknown top-level key is stripped, but gives no version for when `userConfig` arrived and nothing about earlier versions. The frame names v2.1.269 and v2.1.271 only, and neither stops loading this manifest | `.claude-plugin/plugin.json:21-27` | the owner, if a supported floor below the versions the frame names matters |
| Whether Claude Code shows the configuration dialog when an already-enabled plugin updates to a version that adds `userConfig`. The reference says it prompts when the plugin is enabled, which narrows `gaps.md`'s third *Not verified* row without answering it for an update | `.claude-plugin/plugin.json:21-27` | the owner, at the first update to 0.24.0 |
| That a hook process receives `CLAUDE_PLUGIN_OPTION_WORKTREE_GUARD_LANGUAGE`. The reference says hook commands get `CLAUDE_PLUGIN_OPTION_<KEY>` for every option, but no run here went through Claude Code | `hooks/worktree-guard.py:249` | the owner, as `gaps.md` *Not verified* names |
| The full suite, the repository-wide lint and the typecheck | the branch | the orchestrator, at its one `seal gate` run (contract rule 2) |

## Probes

| Command | Result |
|---|---|
| `bin/test -q` over the 41 modules under `tests/` that name `hooks/lint-python.py`, `hooks/worktree-guard.py`, `plugin.json`, `README.ko.md` or the censuses | 2247 passed, 4 skipped, exit 0 |
| `bin/test -q tests/e2e/creation/test_creation_flow.py` | 9 passed, exit 0 |
| `bin/seal layout --check` | 160 files read, 0 refused, exit 0 |
| `bin/seal rules --check` | all 266 check lines in 55 rule files hold, exit 0 |
| `bin/seal layout --pairs` | exit 0; no pair names `test_worktree_guard`, `test_chain_hooks_hardening` or `test_lint_python` |
| `claude plugin validate .` at the worktree root, Claude Code 2.1.312 | exit 0, `Validation passed with warnings`, the one warning about `CLAUDE.md` |
| `git archive 958f2f3e` into `<scratchpad>/1793201097-two-environment-variables-still-carry-the-old-brand/round-1/probe`, a `titel` key added inside the option with the Edit tool, `claude plugin validate .` there | exit 1, `userConfig.worktree_guard_language: Unrecognized key: "titel"`, `Validation failed`; the copy was removed |
| `grep -n environ hooks/lint-python.py` | no output, exit 1 |
| `git grep -n -i` for both variable names over the tree outside `seal/threads/` and `changelog/0.*` | hits only at the lines `## Confirmations` lists |
