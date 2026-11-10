# Phase 1: 1794271937-the-readme-narrates-three-migrations

## What this phase found

**The frame's coordinates held against the tree, and two of its claims did
not.** Before the build, each coordinate `frame/design.md` *Scope* names was
opened at `8d988e1a3` (`read`): `README.md:95-99`, `:101-115` and
`:368-372`; `README.ko.md:99-118` and `:365-369`;
`docs/checks/the-stamp.md:94-99` and `:125-127`; the bold lead
**4b. The launcher an earlier release wrote.** in `skills/update/SKILL.md`.
Issue #1376's comment 6675898172 was read through `gh api` (`executed`),
and its section *The terminal stamp* holds the four facts *Scope* item 5
lists. The two claims that did not hold are the next two paragraphs.

**The acceptance grep of *User scenarios & acceptance* row 1 cannot print
nothing.** `git grep -n -e 'agentic:start' -e 'claude-md-block' -e
'stamp.py' -- README.md README.ko.md` matches `seal_stamp.py --stop` at
`README.md:356` and `README.ko.md:352`, the plugin's own `Stop` hook, which
the design keeps (`executed`). The grep that asks what the row means, with
the launcher's file name as a code span,
``git grep -n -F -e '`stamp.py`' -e 'agentic:start' -e 'claude-md-block' -- README.md README.ko.md``,
printed nothing and exited 1 at `b0cb62de0` (`executed`). Judged against the row's
own *Then* clause, which asks that nothing describe the launcher.

**G11 missed a case that needed the README's `CLAUDE.md` block paragraph.**
`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#test_every_template_is_named_by_a_document_that_ships`
asks that every file under `templates/` be named by a shipped `.md`
document. The paragraph *Scope* item 1 removes was the only one naming
`templates/setup/claude-md-block.md`, so the case went red at `b0cb62de0`
(`executed`). *Removes* row 1 says the paragraph's facts land in
`skills/update/SKILL.md` *4. Take out the preset block.*, but that step does
not name the template, and
`tests/behaviour/test_the_old_block_leaves_through_update.py#test_step_4_works_on_the_config_directorys_file_and_writes_no_block`
refuses `claude-md-block.md` in it. Three repairs were weighed:

- Keep the template's name in the README. It breaks *Scope* item 1, *Removes*
  row 1 and scenario row 1.
- Name it in another shipped document. That adds a fourth account of the
  block, which the issue is removing.
- Exempt it in the case by name. This was taken in `4544f5ed4`.

The case's premise is that a session bootstraps from every template. No
session bootstraps from this one: it holds the two markers because the
update to 0.25.0 runs 0.24.x's own update step against the marketplace
clone's copy, as the docstring of
`tests/behaviour/test_the_old_block_leaves_through_update.py` states. So
the case refused a correct tree, which contract rule 18 says to fix in the
check. `READ_BY_AN_EARLIER_RELEASE` names the file with those grounds, and
the case now also refuses an exempted entry the tree no longer holds. This
is a test change outside the list `routing.md` *Why this way* gives for the
diff under `tests/`, and the removal *Scope* item 7 schedules takes the
exemption out with the template.

**The experiment record departs from *Scope* item 5 in one clause.** The
item asks *What it did not establish* to say the scratch plugin was not
kept. The comment does not say that. It says the two portal branches were
deleted, and it gives no location for the scratch plugin. So the record
says what holds: the scratch plugin is not in this repository, and the
comment records results and not steps. The slug is
`what-draws-the-stamp-without-a-plugin-hook`, after the question the record
opens with. The record cites the comment by issue and comment number, the
way the sibling record cites `#107`, and not by URL. Its *Method* carries a
re-run outline and says it is the comment's account. Judged against
`docs/experiments/README.md`, whose *Method* asks for enough to re-run.

**The policy case gained three asserts beyond the two *Scope* item 6
names.** Item 6 asks that *The stamp* cite step 4b and drop
`${CLAUDE_PLUGIN_DATA}/stamp.py`. Scenario row 5 also asks that the
draw-once rule stay and that the measurement clause cite a
`docs/experiments/` record, verified by the same case. So the case also
asserts the draw-once sentence, the absence of "the owner's spike", and the
record's path in the part of the section after
**What the person's screen shows is not checked**.

**Each new assert was seen red with only the sentence it guards broken**
(`executed`, each through `bin/seal mutate` on `b0cb62de0` or `4544f5ed4`,
each verdict `red`, each failing line read for its own assert):

| Assert | Break | Failing line |
|---|---|---|
| `README.md` says the launcher sentence | the old two sentences restored | the `said` assert for that sentence |
| `README.md` no longer holds "a launcher, `stamp.py`" | the phrase added before "No session stops another" | the `gone` assert for that phrase |
| `README.ko.md` says the launcher sentence | the old Korean sentences restored | the `said` assert for that sentence |
| `README.ko.md` no longer holds "실행기 `stamp.py`" | the phrase added before "다른 세션이 쓰고 있는" | the `gone` assert for that phrase |
| *The stamp* cites step 4b | the citation replaced by "`/agentic:update` step 4b" | the citation assert |
| the draw-once rule stays | "drawn once, since" made "drawn once either way, since" | the draw-once assert |
| `${CLAUDE_PLUGIN_DATA}/stamp.py` is gone | a sentence naming it added before the `check:` line | the absence assert |
| "the owner's spike" is gone | "So did the owner's spike." added | the absence assert |
| the measurement cites the record | the record's path replaced by "the owner's record says" | the path assert |
| the wrap list covers the new record | a 105-column line added to the record | `test_prose_stays_within_the_wrap_limit` for that file, line 64 |
| the template exemption | the tuple emptied | the unreachable assert, naming the template |
| the stale-entry guard | `templates/setup/gone.md` added to the tuple | the stale assert, naming that path |

Before the build, the two changed cases also failed against the old text on
their first new assert (`executed`).

**No `seal mutate` run beyond these is owed.** The phase changes prose and
the cases that pin it, and adds no behaviour to a script
(`skills/verify/SKILL.md` *The narrow command still has to be able to
fail*, the *Prose only* row).

**The Korean wording follows `skills/writing-style/SKILL.md` `## 문장
규칙`.** The launcher sentence names a condition, "남긴 실행기가 있으면",
where the English says "may have left", since a Korean sentence closing on
the possibility read as a guess. The link stays attached to "지웁니다" and
"줍니다", as `README.ko.md` writes "지웁니다(`skills/update/SKILL.md`)".
Both editions carry the same statements in the same order (`read`), and
`tests/behaviour/test_both_editions_carry_the_same_folds.py` passed
(`executed`).

**`gaps.md` was written although the spawn asked for it only with a gap.**
`tests/behaviour/test_chain_hooks_hardening.py#test_every_spec_directory_that_reached_the_ladder_has_an_overview`
refuses a work item with a `frame/design.md` and no `gaps.md`, and it went
red at the first boundary run (`executed`). `agents/crafter.md` *Job* and
`skills/implement/SKILL.md` *3. The SDD file set* have the first phase write
it from its template. It holds the suite's row and `nothing` under
*Not done*.

**The *Updating* paragraph was reworded after the first record, in
`03a172de4`.** Its opening said `/agentic:update` "takes care of" what an
earlier release left, while the same paragraph names what only the person
can remove, so it now says what the command does and nothing more. The
Korean edition dropped "그 일은 `/agentic:update` 가 맡습니다" the same way.

**The boundary set passed over `03a172de4` with this record and the plan's
Status cell on disk**
(`executed`): `bin/test tests/text tests/behaviour -q`, 1852 passed and 8
skipped. That set holds every module plan row 1 names. The first run, at
`b0cb62de0`, failed on the two cases above, and the run at `4544f5ed4`
with `gaps.md` on disk passed. No test file outside
`tests/text/` and `tests/behaviour/` reads a path this phase changed: the
hits of `git grep` for the READMEs, `the-stamp` and `experiments` under the
other test directories are fixtures, docstrings or a corpus list of other
paths (`read`).
