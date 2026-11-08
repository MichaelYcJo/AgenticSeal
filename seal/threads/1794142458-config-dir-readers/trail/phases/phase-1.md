# Phase 1: 1794142458-config-dir-readers

## What this phase found

**The frame holds for this phase.** Every coordinate that phase 1's row
reaches stood at `f774315f7`, which differs from `b2a04d6d9` only by the
three frame files (executed: `git diff --stat b2a04d6d9 HEAD`). The
coordinates are `session_cost.py:41`, `:82-83`, `:2879-2893` and `:3100`,
`tests/skills/test_session_cost.py#Test_newest` with its `PROJECTS` patch,
the `GH_CONFIG_DIR` block of `tests/conftest.py`,
`skills/verify/orchestration.md:241`, `README.md:317` and
`README.ko.md:316` (read). `HOME` and `PROJECTS` had no reader outside the
script and `Test_newest` (executed: `git grep -n -E
'\bPROJECTS\b|session_cost\.HOME|module\.HOME' -- . ':!seal/threads'`
lists nothing after the build). The module docstring is not the script's
`--help` text, because no `__doc__` is read (executed: `grep -n __doc__`),
so the docstring edit changes nothing a person sees.

**Departure: a case in `tests/test_conftest.py` that the frame did not
name.** `frame/design.md` *Scope* item 4 adds the `conftest.py` pop with
no case, and S8 verifies it by a narrow run under an outer
`CLAUDE_CONFIG_DIR`. That run cannot fail where the pop is missing. With
the pop replaced by `pass`, `env CLAUDE_CONFIG_DIR=<scratch>
bin/test tests/skills/test_session_cost.py -q -p no:xdist` passed 255
cases, and `seal mutate` reported `SURVIVED` (executed). Every
`Test_newest` case sets or deletes the variable itself, so no case of that
module reads an inherited value. `agents/crafter.md` *Mutation-test every
unit that adds behaviour* and `skills/implement/SKILL.md` *2. Implement
test-first* ask for a case behind each unit that adds behaviour. So
`Test_module::test_the_conftest_takes_the_claude_config_directory_away`
joins its group's probe cases: the `GH_CONFIG_DIR` case and the `GITHUB_`
case run the conftest's import in a child, and this one does the same with
`CLAUDE_CONFIG_DIR` naming a directory that holds a `CLAUDE.md`. `PROBE`
gains one field, `claude_config`. `seal layout --pairs` over the two
modules names 20 pairs before the build and 20 after, none of them in
`Test_newest` or `Test_module` (executed).

**`Test_newest` builds S1's and S2's paths from the slug, not from
`projects_dir()`.** A case that located its transcripts through the unit
under test would agree with any root the unit returned. `slug_of` holds the
slug rule, and `one_transcript_under_each_root` writes one transcript under
`<config>/projects/<slug>/` and a later one under
`<home>/.claude/projects/<slug>/`. `project_of` reads `module.projects_dir()`
as *Scope* item 5 says, and only the two cases that were there before use
it. `two_roots` sets `HOME`, `USERPROFILE` and `CLAUDE_CONFIG_DIR` with
`monkeypatch.setenv`.

**Seen red** (each executed):

- S1, `test_accepts_the_transcript_under_the_config_directory_in_use`, red
  against `:82-83` as they stood. Its failing line is the `==`, and
  `newest` returned `<home>/.claude/projects/<slug>/b.jsonl`.
- S2 `[unset]` passes against the old code, because `load_script` ran after
  `HOME` moved and the old constant read the scratch home at import. It was
  shown red with the fallback's `".claude"` changed to `"claude"`.
- S2 `[empty]` red against the resolution written as
  `os.environ.get("CLAUDE_CONFIG_DIR", os.path.join(os.path.expanduser("~"), ".claude"))`,
  as the S2 row says. The run named only `[empty]` as failing.
- The conftest case, red with `os.environ.pop("CLAUDE_CONFIG_DIR", None)`
  replaced by `pass`. Its failing line is `CLAUDE_CONFIG_DIR is left set`.

**Mutation runs, after commit `c4deded61`** (executed, `seal mutate`, each
restored from its held bytes; `git status --short` was empty after each):

- `session_cost.py`, three mutants against `-k Test_newest`: the `or`
  written as `environ.get`'s default, the variable read replaced by `None`,
  and `newest`'s root built from `expanduser("~")` in place of
  `projects_dir()`. Three red, none survived. Then the second and third
  against S1 alone: both red.
- `session_cost.py`, the fallback's `".claude"` as `"claude"` against
  `-k unset`: red.
- `tests/conftest.py`, the pop as `pass`, against `-k claude_config`: red.
  Against S8's run alone, `SURVIVED`, as the departure above says.

**The comment at the old `:3100` is scoped to the default directory.** It
said that the transcript's path carries the account name twice. Under
`$HOME/.claude` it does, once in the home and once in the slug. Under a set
variable the count depends on the directory the variable names, so the
sentence now says "under the default directory". Judged against
`skills/writing-style/SKILL.md` *Hedge only what you did not verify*: the
count under a set variable was not measured.

**`skills/verify/orchestration.md:241` runs past 88 columns.** The new
spelling makes the one code span about 100 columns wide, and a code span
does not break. The file is not in `tests/behaviour/test_docs_line_wrap.py`'s
`COVERED` list (read). The two README lines are covered, and both
paragraphs were rewrapped under 88.

**S7, for items 1 and 3** (executed: G2's second search on the working
tree after the build). The search lists none of `orchestration.md:241`,
`README.md:317`, `README.ko.md:316` or the docstring and comments of item
1. Its one line in these files is `session_cost.py:90`, which is the
`"~"` literal of `projects_dir`'s fallback, code and not prose. The new
spelling `$HOME/.claude}/projects` does not match `\.claude/projects`,
because `}` stands between them. The search still lists
`payload_meter.py:8`, `:69`, `:464`, `:480` and `:1176`, which are phase
2's.

**S8, for `tests/skills/test_session_cost.py`** (executed): under an outer
`CLAUDE_CONFIG_DIR` naming a scratch directory that holds a `CLAUDE.md`,
`bin/test tests/skills/test_session_cost.py tests/test_conftest.py -q`
passed 306 cases.

**For phase 2.** The new `conftest.py` comment names
`session_cost.py#projects_dir` as the one reader of the variable, because
that is true at this phase's commit. Phase 2's reader in `payload_meter.py`
makes the sentence short of the tree, and phase 2 rewrites it in place.
