# Phase 2: 1793201097-two-environment-variables-still-carry-the-old-brand

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | b1df3266 |

## What this phase was asked

Build phase 2 of `frame/plan.md` against the frame at `0c451b8c`, under the
owner's automation answer, with `frame/questions.md` Q1 on default (a) and Q2
on its default. `.claude-plugin/plugin.json` declares `worktree_guard_language`
exactly as `frame/design.md` *Data and interfaces* gives it.
`hooks/worktree-guard.py#_lang` reads the option, then `SPECSEAL_LANG` with a
comment saying the next minor release removes that read, then the locale.
`tests/conftest.py` also removes the option's variable, and the fixture `wko`
sets it. A case for S2 and S3 is seen red against the base's `_lang`, and a
case for S5 is seen red with the declaration deleted. Both READMEs replace
the `SPECSEAL_LANG` row with the option's row. The phase writes this work
item's `changelog.md` for S8. The manifest change is verified with
`claude plugin validate .`, its exit code read directly.

## What this phase found

**The defaults this phase built on.** Q1 (a): `chain_check.py#OLD_TRAILER`
and `hooks/lib/routing.py#OLD_BY_CRAFTER` are not touched, and `gaps.md`
*Not done* names them as overdue. Q2: #1053 had not merged into
`release/v0.24.0` when this phase ran. `origin/release/v0.24.0` stood at
`faf093f1`, an ancestor of this branch (executed, `git merge-base
--is-ancestor`). So the fragment takes the form the tree asks for here,
`seal/threads/1793201097-two-environment-variables-still-carry-the-old-brand/changelog.md`,
under `### Changed` and `### Removed` headings with no line starting `## `.

**How each case was seen red (executed).** The cases and the fixture change
were written first, with the manifest and `_lang` as at `0c451b8c`.
`bin/test -q -p no:xdist -rf tests/hooks/test_worktree_guard.py
tests/behaviour/test_chain_hooks_hardening.py::test_every_option_the_manifest_declares_is_one_a_hook_reads`
exited 1, with 14 cases red:

- both parameters of
  `Test_module::test_accepts_the_option_first_and_the_old_variable_where_it_is_empty`,
  on `assert 'en' == 'ko'`, the first assertion;
- the S5 case, on `assert [] == ['description', 'title', 'type']`, with the
  manifest carrying no `userConfig`;
- eleven `Test_main` cases that load the guard through `wko`. With the
  fixture setting the option's variable, the base's guard ignored it and
  read the suite's `SPECSEAL_LANG=en`, so their Korean assertions failed.

With the manifest, `_lang` and `tests/conftest.py` changed, the same command
passed, 357 cases and 3 skipped, exit 0.

**Each unit added has a case behind it (executed, `seal mutate` at
`b1df3266`).** `git status` was clean after every run.

| File | Mutant | Cases run | Verdict |
|---|---|---|---|
| `hooks/worktree-guard.py` | the option's read replaced by `v = ""` | the S2 and S3 case | red |
| `hooks/worktree-guard.py` | `SPECSEAL_LANG` read before the option | the S2 and S3 case | red |
| `hooks/worktree-guard.py` | the `SPECSEAL_LANG` read removed | the S2 and S3 case | red |
| `hooks/worktree-guard.py` | the fallback taken only where the option's variable is absent, so an empty option wins | the S2 and S3 case | red; `[empty]` failed and `[absent]` passed |
| `hooks/worktree-guard.py` | the option's variable misspelt `..._LANG` | the S5 case | red |
| `.claude-plugin/plugin.json` | `userConfig` misspelt, the key misspelt, `type` set to `boolean`, a `default` added, `title` removed | the S5 case | 5 mutants, 5 red, 0 SURVIVED, exit 0 |
| `tests/conftest.py` | the removal of the option's variable deleted | `tests/hooks/test_worktree_guard.py`, with the shell exporting the option as `ko` | red, 84 cases failed |

The conftest mutant needs its green side shown as well, because the
single-mutant form runs no baseline. With the line in place and the shell
exporting `CLAUDE_PLUGIN_OPTION_WORKTREE_GUARD_LANGUAGE=ko`, the module
passed, 356 cases and 3 skipped, exit 0.

**S5's case reads every script under `hooks/`, not the guard alone.**
`frame/design.md` S5 asks that `hooks/worktree-guard.py` read no undeclared
option. The case reads every `.py` file under `hooks/` for
`CLAUDE_PLUGIN_OPTION_` followed by upper-case letters, digits and
underscores, and requires that set to equal the declared keys uppercased.
That holds the guard and every other hook script to the manifest. It sits in
`tests/behaviour/test_chain_hooks_hardening.py` beside the other cases that
read `plugin.json`. A case in `tests/hooks/test_worktree_guard.py` would leave
with the guard if #1049 removes it, and the plan's second failure scenario
needs the case to stay and turn red. `gaps.md` records the widening as a
divergence.

**`claude plugin validate .` (executed).** At the worktree's root it exited
0 and printed `Validation passed with warnings`, where the frame expects
`Validation passed`. The one warning is `CLAUDE.md at the plugin root is not
loaded as project context`. The same command over a `git archive` extract of
`0c451b8c` printed the same warning and the same last line, exit 0. The
extract was removed after the run. The warning predates this work and names
no file it changed. `gaps.md` records it as a divergence.

**The manifest's description is the frame's text, kept as given.**
`frame/design.md` *Data and interfaces* spells the description as "Left
empty, the system locale decides." Through 0.24.x, `SPECSEAL_LANG` decides
before the locale where the option is empty. The description stays as the
frame wrote it, because it states the option's lasting behaviour, and the
READMEs' row states the fallback. A reviewer may judge the description's
silence on the fallback.

**The group check (executed).** `bin/seal layout --pairs` exited 0 and named
no pair in `tests/hooks/test_worktree_guard.py` or
`tests/behaviour/test_chain_hooks_hardening.py`. The S2 and S3 case sits in
`Test_module` next to S4's case, which holds the variable-then-locale order
and stands unchanged. The constant `OPTION` near the top of the guard's test
module names the option's variable once, for that case and the fixture.

**Sentences read and left standing (executed, `git grep -n -i` over the
living tree for both names, "off switch", "system locale" and `_lang()`).**
The hits are the lines this work wrote, the S4 case, and the conftest
comment, which still states a true fact: the author's machine exports
`SPECSEAL_LANG=ko`. No document under `docs/`, `skills/`, `agents/` or
`templates/` names either variable or the language of the guard's prompts.
