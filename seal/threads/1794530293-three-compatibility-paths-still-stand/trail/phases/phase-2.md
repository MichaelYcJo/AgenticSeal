# Phase 2: 1794530293-three-compatibility-paths-still-stand

## What this phase found

**The frame held against the tree, except for two searches.** Before the
build, each coordinate of `frame/design.md` *Removes* R22 to R31 was opened
at `76ba36f78`, and each stood where the row says (`read`). The readers of
each removed unit were listed by `git grep` on its name and on the update
steps' numbers: `READ_BY_AN_EARLIER_RELEASE`,
`test_the_old_block_leaves_through_update`, `**4.`, `**4b.` and `**5.`.
No reader stood outside the rows (`executed`).

**The census grep in `frame/plan.md`'s phase 2 Verified by cell cannot find
only #1492's records.** At `e7215e0e4` it finds three other groups
(`executed`). The first is `docs/checks/the-stamp.md:95`, the citation of
step 4b. No phase edits `docs/`, and the `remove` item of
`frame/design.md` *Rule changes* takes the citation out at the settle.
`tests/behaviour/test_a_cited_section_stands_in_its_file.py` excuses it
until then and says so in a warning in the boundary run (`executed`). The
second is two lines naming `${CLAUDE_PLUGIN_DATA}` in
`docs/experiments/2026-11-06-what-draws-the-stamp-without-a-plugin-hook.md`.
That dated record is under *Scope* **Out**. The third is the records of
other work items and this one's. `1794383427-asserts-pin-literal-phrases`
quotes `${CLAUDE_PLUGIN_DATA}/stamp.py` in its phase-3 and round-2 records.
This work item's frame quotes the patterns, and its `changelog.md` names
the markers and the launcher's path, as *Scope* item 12 asks. The same
holds for `frame/design.md` S8: `git grep -n 2027-02-07` also finds this
work item's own frame files, which name the date they remove. Outside
`seal/threads/`, the date stands in no file (`executed`). Both were judged
against the cell's aim: no shipped skill, template, README or test names a
removed path, and `docs/` keeps only the sentence the settle removes.

**One sentence the frame did not name was removed.** The opening of
`skills/update/SKILL.md` *Procedure* said that the plugins Claude Code
installs "and the `CLAUDE.md` it reads as the user's" stand in the config
directory in use. `git log -S` shows #1184 wrote that clause with the
config-directory work (`executed`). It named `CLAUDE.md` because step 4
opened that file. With step 4 gone, no step opens a `CLAUDE.md`, as
`frame/design.md` S4 states, and the clause described a file no command
of the skill reads. It was judged against `skills/core/SKILL.md` *The rule
a mechanism is kept against*: a change removes, in the same commit, what
stood on the old fact.

**The two moved cases were seen red in their new file.**
`test_this_repository_imports_no_core_and_names_the_tree_copy` went red
under `seal mutate CLAUDE.md`, which planted ` @lib/x.md` after "imports
nothing and copies nothing." and put the file back. The verdict was `red`,
exit 0, and the failing line was the `IMPORT` assert, "CLAUDE.md imports a
file" (`executed`). `CLAUDE.md` was clean afterwards (`executed`: `git
status`). `test_an_import_line_is_told_from_a_code_span` reads no file,
so a plant in `CLAUDE.md` cannot redden it. After the commit, `seal mutate`
was run over `IMPORT` in the new file with two mutants (`executed`). The
first, `r"@"`, went red. The second dropped the `^` alternative and kept
`\s`, and it SURVIVED: no input of the case puts `@` at the first character
of the text. The case moved word for word, so the gap predates this work,
and a move owes no case written new (`skills/verify/SKILL.md` *The narrow
command still has to be able to fail*). `gaps.md` *Not done* records it.
The new file's module docstring gained one sentence naming what the two
cases hold.

**No other unit adds behaviour.** The phase takes out two update steps, a
paragraph, a template, an exemption, a test module, three cases, pins and
prose. The step-2 paragraph lost its clause sending an already-current
update to step 4b. Step 5 was renumbered to step 4, and the cases that cut
the skill by step number cut step 3 at `**4.` (`read`). No `seal mutate`
run was owed beyond the moved cases.

**The fragment says "a command that read a setting through
`lib/config.py`", not "every command".** `docs/layout/one-root-by-lifetime.md`
*What the repository decides for itself, and how it is read* says the
readers of `Policy root` and `Reference specs` read an old `config.md` as
no file, so they never refused one (`read`). The *Updating* line gives one
sentence for each act *Scope* item 12 names, and not one sentence of six
clauses. That was judged against `skills/writing-style/SKILL.md` *English
prose rules*, "Short sentences over connector chains".

**The version move is this pull request's.** `origin/release/v0.38.1`
holds no commit after `8f6acbb0e`, and its `.claude-plugin/plugin.json`
reads `0.38.0` (`executed`: `git fetch`, then `git log` over the range).
So this is the first pull request into the release branch, as
`docs/releasing/branch-and-release.md` *Work accumulates on a release
branch* asks. `e7215e0e4` moves the version and adds `changelog.md`
together. Outside `seal/threads/`, `0.38.1` stands in
`.claude-plugin/plugin.json` alone (`executed`).

**The phase-boundary set is `tests/text` and `tests/behaviour`.** Every
file in the plan row is in those two directories, and so is every test file
the phase changed. A `git grep` over `tests/` outside them found no case that
opens the repository's own `README.md`, `README.ko.md`,
`.claude-plugin/plugin.json`, `skills/update/SKILL.md` or
`templates/setup/claude-md-block.md`. The cases it found build their own
copies under a fixture root (`executed`).
