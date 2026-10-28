# Implementation Plan: 1793201097-two-environment-variables-still-carry-the-old-brand

Approved 2026-10-29 by the orchestrator under the owner's automation answer, when `crafter` was spawned.

## Summary

Phase 1 removes `SPECSEAL_LINT`: its read, its docstring sentence, its test
case, its README rows in both editions and its census entry. Phase 2 declares
the option `worktree_guard_language` in `.claude-plugin/plugin.json`, makes
`hooks/worktree-guard.py#_lang` read it before `SPECSEAL_LANG`, moves the
tests and both READMEs to it, and writes this work item's changelog fragment.
Each phase builds test first.

## Technical context

- `hooks/lint-python.py#main` (from line 84 at `faf093f1`, read) returns
  early at line 93 where `SPECSEAL_LINT` is `off`. It is the file's only
  `os.environ` read (executed, `grep -n environ`). Its case is
  `tests/hooks/test_lint_python.py:203-207` (read).
- `hooks/worktree-guard.py#_lang` (lines 241 to 247 at `faf093f1`, read)
  sets the module constant `LANG` once at import, and `tr(en, ko)` reads it.
  `hooks/dispatch.py` imports the guard inside the hook process (lines 81
  and 82, read), so the guard sees the environment Claude Code gives that
  process, which the manifest reference says carries
  `CLAUDE_PLUGIN_OPTION_<KEY>` for every option.
- `tests/conftest.py:349-353` (read) sets `SPECSEAL_LANG=en` for the whole
  suite, because the author's machine exports `SPECSEAL_LANG=ko`. Once the
  option is read first, the same file also removes
  `CLAUDE_PLUGIN_OPTION_WORKTREE_GUARD_LANGUAGE` from `os.environ`, so a
  value in the shell that runs the suite cannot flip the default-language
  assertions.
- `tests/hooks/test_worktree_guard.py:367-371` (read), the fixture `wko`,
  loads the guard with `SPECSEAL_LANG=ko`; `Test_module::test_accepts_the_language_and_the_idle_window_the_environment_names`
  (lines 1133 to 1145, read) holds the variable-then-locale order.
- `.claude-plugin/plugin.json` (read) has no `userConfig`. Its readers are
  `hooks/version-check.py` (`version`), `.github/scripts/release_seal.py`
  (`icon`), `.github/scripts/plugin_directory_check.py` (`name`),
  `.github/scripts/roll_flow_measurement_issue.py` and
  `.github/workflows/hygiene.yml` (`version`), and
  `tests/behaviour/test_chain_hooks_hardening.py` (`icon`, `description`)
  (executed, `git grep -n plugin.json`). None reads the whole object, so a
  new top-level field reaches none of them.
- `tests/censuses.py:1030-1035` (read) keeps both names in
  `KEPT_OLD_NAMES` under one comment saying *this release changes no
  behaviour*, which stops being true here.
- **The failure scenario of the chosen approach.** In six months the 0.25.0
  release ships and the guard still reads `SPECSEAL_LANG`, because a code
  comment is all that asks for its removal. The precedent this work copies
  has already failed that way once: `chain_check.py#OLD_TRAILER` says the
  next minor release after the rename removes it, 0.24.0 is that release,
  and no issue schedules it (executed, `gh search issues`). The second
  scenario: #1049 removes the worktree guard in 0.24.1 and the manifest
  keeps an option nothing reads. S5's case reads every declared option
  against `hooks/`, so the guard's removal turns that case red until the
  option goes with it.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. A `userConfig` option `worktree_guard_language` of type `string`, with no `default`, no `options` and no `required`; `_lang` reads it, then `SPECSEAL_LANG` through 0.24.x, then the locale | The `SPECSEAL_LANG` read outlives 0.24.x because nothing but a comment schedules its removal (Technical context). A person typing `Korean` gets Korean and `English` gets English, but `ja` gets English with no word said | **chosen**: the owner's decision of 2026-10-28, in the shape the manifest reference gives, with nothing that stops an older Claude Code from loading the plugin |
| B. The same option with `options: ["ko", "en"]` | The manifest reference says a plugin that declares `options` on any field does not load in Claude Code before v2.1.271. A person on an older version loses every gate the plugin ships to gain a picker for one hook's language | rejected |
| C. The same option with `default: "en"` | A default is the value used when the person provides nothing, so every person has a value: neither `SPECSEAL_LANG` nor the locale is ever read, and the owner's prompts turn English on the update, which the one-release fallback exists to prevent | rejected |
| D. A `seal/config.md` row | Two people in one repository who want different languages share one row, which `templates/setup/config.md` *What no row governs* rules out for the language a session speaks to a person | rejected; the owner decided it on 2026-10-28 |
| E. Rename the variable to a new prefix | Anyone who set the old name silently loses their choice, as #1051 argued when it kept both names; and the owner decided neither stays an environment variable | rejected |
| F. Replace the structure: drop the Korean texts, so the guard speaks English like every other gate and there is nothing to set | Removes 106 Korean texts (executed, `grep -c "tr("`) the owner reads every day: the owner's settings set `SPECSEAL_LANG=ko` (executed). The premise that keeps the structure is the issue body's *Decided by the owner on 2026-10-28*, *The prompts' language becomes the plugin's own user setting* (read). If #1049 removes the guard in 0.24.1, the texts and the option go with it | not chosen; #1049 decides whether the guard stays |
| G. Read the locale alone, with no option | The owner's machine runs `LANG=en_US.UTF-8` (executed), so the owner's prompts turn English with no way back short of changing the locale for every program | rejected |
| H. Drop the `SPECSEAL_LANG` read now, with no fallback release | The owner's prompts turn English on the update until the option is set. The owner decided one minor release of fallback, as `SpecSeal-Routing:` had | rejected |
| I. Remove the read of `SPECSEAL_LINT` | A person who configures ruff and wants no fix on save loses the off switch; no record shows such a person (executed, `git grep`) | **chosen** |
| J. Replace the structure for the lint switch too: a `userConfig` option of type `boolean` | Adds a manifest field and a `/config` row for every person to serve a use nobody has recorded, which `CLAUDE.md` *The rule a mechanism is kept against* does not allow | rejected; the owner decided it on 2026-10-28 |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `hooks/lint-python.py` reads no environment variable and its docstring loses the off-switch sentence; the off-switch case is deleted; both READMEs lose the `SPECSEAL_LINT` row and the clause in the lint-python row; `tests/censuses.py#KEPT_OLD_NAMES` loses the `_LINT` item, and the comment above the `_LANG` item says the guard reads it as a fallback through 0.24.x and the next minor release removes it. Scenarios S1, S6 for `SPECSEAL_LINT`, S7 | `tests/hooks/test_lint_python.py` and the old-name census case of `tests/test_censuses.py`, run narrow; `git grep -n SPECSEAL_LINT` lists only files under `changelog/` and `seal/threads/` | |
| 2 | `.claude-plugin/plugin.json` declares `worktree_guard_language` exactly as `frame/design.md` *Data and interfaces* gives it; `_lang` reads the option, then `SPECSEAL_LANG` with a comment that the next minor release removes that read, then the locale; `tests/conftest.py` also removes the option's variable; the fixture `wko` sets the option's variable; a case for S2 and S3, seen red against `faf093f1`'s `_lang`; a case for S5, seen red with the declaration deleted; both READMEs replace the `SPECSEAL_LANG` row with the option's row; this work item's `changelog.md` fragment covers S8 | `tests/hooks/test_worktree_guard.py` *Test_module* and the cases that use `wko`, the S5 case, and the old-name census case, run narrow; `claude plugin validate .` at the worktree's root prints `Validation passed` | |

## Operational impact

- One environment variable stops being read: `SPECSEAL_LINT`. A person who
  set it to `off` in a project that configures ruff gets ruff's fixes on
  save again after the update.
- The manifest gains `userConfig`. A person sets the option with `/config`,
  which shows the row from Claude Code v2.1.269 (read, manifest reference).
  Whether Claude Code also opens a dialog for it when the updated plugin is
  enabled is not read (unverified; answerer: a measurement, by whoever
  updates first, and the changelog fragment claims neither way).
- `SPECSEAL_LANG` is still read through 0.24.x where the option is empty. The
  owner, who sets `SPECSEAL_LANG=ko`, sets the option to `ko` once and can
  then remove the variable from their settings' `env` block. The next minor
  release removes the read.
- No new dependency, no migration of any file in a repository.
