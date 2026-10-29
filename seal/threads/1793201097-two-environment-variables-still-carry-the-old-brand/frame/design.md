# Feature Specification: 1793201097-two-environment-variables-still-carry-the-old-brand

Issue #1096. Two environment variables keep the name of the old brand. The
plugin stops reading `SPECSEAL_LINT`. The language of the worktree guard's
prompts moves from `SPECSEAL_LANG` to an option the plugin declares in its
manifest, which each person sets once. The guard still reads `SPECSEAL_LANG`
through the 0.24.x releases where the option is empty, and the next minor
release removes that reading.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The rule a mechanism is kept against* | A mechanism stays only while its history shows what it caught against what it costs. `SPECSEAL_LINT` has no record of use: outside the records, `git grep -n SPECSEAL_LINT` at `faf093f1` finds only its reader, its docstring, its one test case, the two README editions and its census entry (executed). So it goes. The new option is a mechanism too, and *Data and interfaces* below states its cost and the history that asks for it |
| `templates/setup/config.md` *What no row governs*, the bullet *The response language* (lines 152 to 155 at `faf093f1`, read) | The language a session speaks to a person is that person's setting, not the repository's, because two people in one repository can want different answers. So the prompts' language is not a `seal/config.md` row. This work reads that file and does not edit it |
| The policy root, `docs/` | No policy document names either variable or the language of the guard's prompts: `git grep` for both names, `locale` and `LANG` over `docs/` finds nothing (executed). No unsettled frame's `## Rule changes` names them either (executed, over every `frame/design.md` under `seal/threads/`). So `## Rule changes` below holds the no-change block |
| The Claude Code plugin manifest reference, `https://code.claude.com/docs/en/plugins-reference`, section *User configuration* (read 2026-10-29, as the issue asks) | The option's shape. `userConfig` maps a key of letters, digits and underscores to a strict object; `type`, `title` and `description` are required; an unknown key inside the object stops the plugin from loading. A hook process receives every option as `CLAUDE_PLUGIN_OPTION_<KEY>`, the key uppercased. `options` stops Claude Code before v2.1.271 from loading the plugin at all. A non-sensitive value is saved under `pluginConfigs` in the person's `settings.json`, and each option appears as a row in `/config` from v2.1.269 |
| `skills/code-review/scripts/chain_check.py#OLD_TRAILER` and `hooks/lib/routing.py#OLD_BY_CRAFTER` (read) | The precedent for reading an old name for one minor release: a comment at the reader says the next minor release removes it, and `tests/censuses.py#KEPT_OLD_NAMES` carries the old spelling with its reason. This work follows the same shape for `SPECSEAL_LANG` |

## Scope

In:

- `hooks/lint-python.py` reads no environment variable. Its docstring loses
  the sentence about the off switch.
- `.claude-plugin/plugin.json` declares one option, `worktree_guard_language`,
  in the shape *Data and interfaces* gives.
- `hooks/worktree-guard.py#_lang` reads the option first, `SPECSEAL_LANG`
  second, and the system locale last.
- The tests that set either variable: `tests/conftest.py`,
  `tests/hooks/test_lint_python.py` and `tests/hooks/test_worktree_guard.py`.
- A new case that holds the manifest and the hooks to each other (S5).
- `README.md` and `README.ko.md`: the lint-python row, and the two rows of
  the switch table that name the variables.
- `tests/censuses.py#KEPT_OLD_NAMES`: the `_LINT` entry goes, and the `_LANG`
  entry's comment says the guard reads it through 0.24.x.
- This work item's changelog fragment, which names both changes and how the
  owner's `SPECSEAL_LANG=ko` carries over.

Out:

- `WORKTREE_GUARD_IDLE_MIN`. It carries no old name, and the issue scopes the
  work to the two variables of the old brand.
- The removal of `OLD_TRAILER` and `OLD_BY_CRAFTER`, whose own comments say
  the next minor release after 0.23.x removes them. That release is 0.24.0, and
  no issue schedules the removal (executed: `gh search issues` for
  `OLD_TRAILER` and for `SpecSeal-Routing` finds none). Whether this work takes
  it on is Q1 of `questions.md`, and the default leaves it out.
- The decision whether the worktree guard stays, which is #1049 in 0.24.1.
- Every file on #1053's list. This work edits none of `templates/setup/config.md`,
  `CLAUDE.md`, `CONTRIBUTING.md`, `skills/implement/`, `skills/update/SKILL.md`,
  `skills/verify/`, `skills/settle/SKILL.md` or `.github/`.
- The released `changelog/0.23.0.md` line 16, which names both variables. A
  released record keeps the names it shipped under
  (`tests/censuses.py#OLD_NAME_RECORDS`).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | Given a project that configures ruff and an environment with `SPECSEAL_LINT=off`, when a `.py` file is written, then the hook runs ruff on it, because the hook reads no variable | `grep -n environ hooks/lint-python.py` prints nothing; the case `test_refuses_where_the_off_switch_is_set_even_with_ruff_configured` is gone and the rest of `tests/hooks/test_lint_python.py` passes |
| S2 | Given `CLAUDE_PLUGIN_OPTION_WORKTREE_GUARD_LANGUAGE=ko`, `SPECSEAL_LANG=en` and `LANG=en_US.UTF-8`, when the guard loads, then its prompts are Korean. With the option `en` and `SPECSEAL_LANG=ko`, they are English | A case in `tests/hooks/test_worktree_guard.py` *Test_module*, shown red against the reader at `faf093f1` |
| S3 | Given the option unset, or set to the empty string, and `SPECSEAL_LANG=ko`, when the guard loads, then its prompts are Korean | The same case, both spellings of unset |
| S4 | Given neither the option nor `SPECSEAL_LANG`, when the guard loads, then `LC_ALL` and then `LANG` decide, as at `faf093f1` | The existing case `test_accepts_the_language_and_the_idle_window_the_environment_names`, kept |
| S5 | Given `.claude-plugin/plugin.json`, when its `userConfig` is read, then it declares `worktree_guard_language` with `type`, `title` and `description` and no other field; every option it declares is read under `hooks/` as `CLAUDE_PLUGIN_OPTION_` plus the key uppercased; and `hooks/worktree-guard.py` reads no `CLAUDE_PLUGIN_OPTION_` variable the manifest does not declare | A new case that reads both files, shown red with the declaration deleted; `claude plugin validate .` at the worktree's root prints `Validation passed` |
| S6 | Given the README in either edition, when a person reads the lint-python row and the switch table, then no row names `SPECSEAL_LINT`, and the row that named `SPECSEAL_LANG` names the option, how to set it (`/config`), and that `SPECSEAL_LANG` is read where the option is empty until the next minor release | `git grep -n SPECSEAL_LINT -- README.md README.ko.md` prints nothing; the row read in both editions |
| S7 | Given `tests/censuses.py#KEPT_OLD_NAMES`, when the old-name census runs, then the `_LINT` entry is gone, the `_LANG` entry stands with a comment naming the fallback, and every living file passes | The old-name census case in `tests/test_censuses.py`, run narrow |
| S8 | Given this work item's changelog fragment, when a person reads it, then it names the removal of `SPECSEAL_LINT`, the new option, and what someone who set `SPECSEAL_LANG=ko` does: set the option to `ko` in `/config`, after which the variable can leave their settings; until then the guard reads the variable, through 0.24.x | The fragment read against this row |

## Data & interfaces

The manifest gains one top-level field. Its spelling, as the crafter writes
it into `.claude-plugin/plugin.json`:

```json
"userConfig": {
  "worktree_guard_language": {
    "type": "string",
    "title": "Worktree guard language",
    "description": "The language of the worktree guard's prompts: ko or en. Left empty, the variable SPECSEAL_LANG decides through 0.24.x, then the system locale. The other gates speak English."
  }
}
```

It declares no `default`, no `options` and no `required`. A `default` would
give every person a value, so neither `SPECSEAL_LANG` nor the locale would
ever be read (plan, alternative C). `options` would stop Claude Code before
v2.1.271 from loading the plugin, and every gate with it (plan, alternative B).

A hook process receives the value as
`CLAUDE_PLUGIN_OPTION_WORKTREE_GUARD_LANGUAGE`. `hooks/worktree-guard.py#_lang`
(lines 241 to 247 at `faf093f1`, read) reads, in order:

1. the option, where it is a non-empty string;
2. `SPECSEAL_LANG`, where it is a non-empty string, with a comment at the
   read saying the next minor release removes it, as at
   `chain_check.py#OLD_TRAILER`;
3. `LC_ALL`, then `LANG`, as now.

Each of the first two maps a value starting with `ko`, case folded, to
Korean and every other value to English, as `SPECSEAL_LANG` is mapped now.
An empty option counts as unset, so it does not matter whether Claude Code
exports an empty variable or none for an option nobody set.

**What the option costs.** One field in the manifest, whose schema is strict:
a misspelt key inside it stops the plugin from loading, which S5's
`claude plugin validate .` guards. One row in every person's `/config`. One
more branch in `_lang` and one test case. Through 0.24.x, a second reader of
the old variable, and in the next minor release a change that removes it.

**What history asks for it.** The owner's user settings set
`SPECSEAL_LANG=ko` in their `env` block (the issue's table, and executed:
`grep` of that settings file finds the line). The system locale on that
machine is `en_US.UTF-8` (executed, `echo $LANG` in this session's shell),
so the locale alone would turn the owner's prompts English.
`tests/conftest.py:349-353` records that the variable is set session-wide
on the author's machine (read). The guard holds 106 `tr(` calls, each a
prompt with a Korean text (executed, `grep -c`).

**What history asks for `SPECSEAL_LINT`: nothing.** The hook already runs
only where a project configures ruff, so the variable served only a project
that configures ruff and wants no fix on save. No record names it used.

## Rule changes

- nothing
  why: no document of the policy root names either variable or the language of the worktree guard's prompts, so this work changes where a hook reads a setting and no rule

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The read of `SPECSEAL_LINT` | `hooks/lint-python.py#main`, lines 93 and 94 at `faf093f1` | Nowhere. No record shows it used, and the hook already runs only where a project configures ruff |
| The docstring sentence *`SPECSEAL_LINT=off` turns the hook off even there.* | `hooks/lint-python.py`, line 14 at `faf093f1` | Nowhere; it described the read above |
| The test case of the off switch | `tests/hooks/test_lint_python.py#test_refuses_where_the_off_switch_is_set_even_with_ruff_configured` | Nowhere; the behaviour it pins is gone |
| The README row `SPECSEAL_LINT=off`, and the clause *`SPECSEAL_LINT=off` disables it* in the lint-python row | `README.md` *Inline switches* and the hook table, lines 186 and 287 at `faf093f1` | Nowhere |
| The same row and clause in the Korean edition | `README.ko.md`, lines 180 and 280 at `faf093f1` | Nowhere |
| The README row `SPECSEAL_LANG=ko\|en`, in both editions | `README.md` line 288 and `README.ko.md` line 281 at `faf093f1` | The row for the option `worktree_guard_language`, in the same table of each edition (S6) |
| The census entry that keeps `SPECSEAL_LINT` | `tests/censuses.py#KEPT_OLD_NAMES`, the `f"{_OLD.upper()}_LINT"` item and the shared comment above it | Nowhere; no living file spells the name after this work. The comment is rewritten for the `_LANG` item alone |
| `SPECSEAL_LANG` as the first source of the language | `hooks/worktree-guard.py#_lang`, lines 241 to 247 at `faf093f1` | The option `worktree_guard_language` in `.claude-plugin/plugin.json`; the variable stays second, through 0.24.x |
| `SPECSEAL_LANG` as the variable the `wko` fixture sets for Korean | `tests/hooks/test_worktree_guard.py#wko`, line 370 at `faf093f1` | The option's variable, so the Korean cases run through the option |

## Open questions

<none here: each is a row of `questions.md`>

Framed 2026-10-29 by framer, before the build.
