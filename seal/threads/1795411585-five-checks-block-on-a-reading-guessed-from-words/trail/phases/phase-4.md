# Phase 4: 1795411585-five-checks-block-on-a-reading-guessed-from-words

## What this phase found

**The frame holds against the tree at `fc8482c5f`, with one count off by
one.** `git diff --stat 22803718e fc8482c5f -- tests/behaviour/
tests/test_censuses.py` printed two other files and neither of this
phase's (executed). So every coordinate of `frame/design.md` G11 and G13
reads at HEAD as the framer read it. G13's range `:568-935` opens on a
blank line, and the comment block starts at `:569`. Removing the range
left three blank lines above the next case, which `ruff format` folded to
two. Search 3 printed 19 lines at `22803718e` and at `fc8482c5f`
(executed: `git grep -n -w ... 22803718e`, piped to `wc -l`), where the
design says 20.

**The near-miss sweep reads through one function, `warn_near_misses`.**
`frame/design.md` *Scope* item 6 asks a case to feed the sweep's reporting
function. Before this phase the sweep's walk and its assert stood inside
the case, so there was no function to feed. `warn_near_misses(files)` now
holds the walk and the warning, and the sweep calls it over
`corpus(ROOT)[1]`. The warning reads `<path>:<line> reads as a contract
citation in a spelling the citation check does not read; cite one contract
rule as `contract rule <N>`, one number each`, through `warnings.warn` with
`stacklevel=2`, as `assert_resolved` reports an excused citation (judged
against `frame/design.md` *Scope* item 6 and G11).

**The sweep is renamed too, beyond the two reader cases *Scope* item 6
names.** Its name, `test_no_file_cites_the_contract_in_a_near_miss`,
claimed what it no longer asserts: it passes where a file does. It is now
`test_every_near_miss_in_the_tree_is_reported`. The two reader cases are
`test_a_near_miss_citation_is_named_at_its_line` and
`test_a_near_miss_wrapped_across_comment_markers_is_named_at_its_line`, and
their docstrings say `named` where they said `refused`. The docstring of
`near_citations` said a near miss is not let pass, and now says
`warn_near_misses` names it. Their bodies are unchanged, so they are the
*Names or places only* row of `skills/verify/SKILL.md` *The narrow command
still has to be able to fail*: they ran green at their new names, and `git
grep -n -e test_no_file_cites_the_contract_in_a_near_miss -e
is_refused_at_its_line -- ':!seal/threads'` printed four cases of other
modules, which refuse a line, and none of this one (executed). Judged
against `skills/core/SKILL.md` *The rule a mechanism is kept against*: a
change removes what stood on the old fact in the same commit.

**S8's case feeds two near misses, not one.**
`test_each_near_miss_is_named_in_a_warning_and_decides_nothing` feeds one
file holding a capital `Rule` at line 2 and a possessive at line 3. It
asserts two warnings, each naming its line, and the call raises nothing.
The first draft fed one near miss, as *Scope* item 6 has it, and a `seal
mutate` run that stops the walk after the first warning SURVIVED it. The
second near miss was added in `d39b50633`, and the same mutant then went
red. Both shapes are built from `n = 7` in an f-string, so the file holds
no near miss of its own (judged against `frame/design.md` S8 and the
module docstring's rule that a fixture builds its numbers when the case
runs).

**Seen red (executed).** S8's case was written first, against
`warn_near_misses` holding the old sweep's body as it stands at
`22803718e`: the list of near misses and `assert not found` with its
message. It failed on that assert, `AssertionError: cite one contract rule
as ... docs/x.md:2`. `near_citations` and `NEAR_CITATION`, which that body
calls, are the bytes `22803718e` holds, since the file had not changed.
After the two-shape case, a mutant that raises an `AssertionError` with the
warning's text in place of the warning failed the case on that line.

**Mutation (executed, `bin/seal mutate`, 6 runs after `d39b50633`, 6
red, 0 SURVIVED).** Each ran `bin/test -q -p no:xdist
tests/behaviour/test_a_cited_section_stands_in_its_file.py -k near_miss`.
The mutants: a `break` after the first warning; the near misses of a file
read as `[:0]`; the files read as `[:0]`; the line printed one higher; the
spelling to write dropped from the message; and the warning raised as an
`AssertionError`. The tree was clean after each call. The batch sweep's
removal adds no behaviour and owes no run.

**The module docstring of `tests/behaviour/test_chain_hooks_hardening.py`
names what the file holds after the removal.** It said the cases hold the
packaging, the READMEs and the agent definitions' wording. The file also
holds the wording of skills, of `docs/running/the-run.md`, and the work
item directories under `seal/threads/`. That was true before this phase,
and *Scope* item 7 asks the docstring to name what the file still holds,
so it now names all of them. The `# No TARGET:` comment, which gives the
reason the module declares no target, still holds and was left as it
stood. `re` and every other module import are still used (`uvx ruff
check` passed on the file).

**`changelog.md` holds a `### Changed` section beyond *Scope* item 8's two
sections.** *Scope* item 8 names `### Fixed` for items 1 and 2 and
`### Removed` for items 5 and 7. Item 3 changes what `seal cost` charges to
a family and what `seal deferrals` names, which `frame/plan.md` *Operational
impact* names as a change a user meets. Item 6 changes what a contributor
of this repository sees in the suite's summary. `docs/layout/the-record-layout.md`
says what changed for a user is `changelog.md`'s, so each takes one entry
under `### Changed`. Item 4 is told inside item 2's entry. The work item's
diff changes no file `docs/layout/the-record-layout.md` *A change writes
fragments, never a shared file* names for a process row, so the fragment
holds no `### Process changes` table, and `frame/plan.md` *Operational
impact* moves no version (read: `git log --no-merges --name-only
22803718e..HEAD`).

**Search 3 prints nothing (executed after the removal).**

**The phase boundary set (executed, one `bin/test -q` command).** It held
the plan row's four files, the two tree-wide directories `tests/text` and
`tests/behaviour`, which hold the changed modules and the one file that
imports from them, `tests/text/test_a_cited_commit_outlives_the_squash.py`.
No test file outside those was found reading this repository's records
(read: of the files outside them that name `changelog.md` or
`seal/threads`, none joins `ROOT` to `seal` but to reach `bin/seal`). Result: 1294 passed, 9 skipped. Its five warnings are citations
that pending rule changes of other work items excuse, and no near-miss
warning stood among them.
