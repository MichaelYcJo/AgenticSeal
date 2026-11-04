# Phase 1: 1793756609-an-enumeration-the-tree-does-not-hold

## What this phase found

**The frame held against the tree, with one exception in its `## Removes`.**
Before the build, the A1 search at 00a903b4a listed exactly the files that
`frame/design.md` *Scope* D1 names, and `.test_durations` held 22 matching
entries, as D1 item 10 says (executed: `git grep -n -E` with A1's pattern,
and `grep -c` on `.test_durations`). Judged against `frame/design.md` D1 and
`## Removes`.

**Departure 1: the comment above the `acts.md` entry in
`tests/behaviour/test_docs_line_wrap.py#COVERED` stays.** `## Removes` says
the entry goes "and its comment". The comment, "Cut from it in #1148, wrapped
as it was.", heads two entries, `skills/implement/acts.md` and
`skills/implement/multi-repository.md`. Both files were added by the same
commit, aa9221d3f (executed: `git log --diff-filter=A` on both paths).
Removing the comment would leave the `multi-repository.md` entry without the
reason it is covered. So only the `acts.md` line went, and the comment now
heads the one entry it still describes. Judged against `skills/core/SKILL.md`
*The rule a mechanism is kept against*: the change removes what stood on the
old fact, and the comment stands on a fact that is still true.

**Departure 2: the marker test's `headings` docstring keeps one sentence of
the removed paragraph.** D1 item 7 says the paragraph "One parser, two
readers." goes. Acceptance A4 says the docstring then "names one reader".
Removing the whole paragraph leaves a docstring that names no reader. So the
paragraph went, and its first clause stays as one sentence:
"`marked_headings` below filters it for this module's own question." The
sentences about the second reader, #330 and the case for one shared parser
are gone. Judged against `frame/design.md` A4, which is the stricter
statement of the two.

**Nothing replaces what went, and no case was added.** The phase removes
units and adds no behaviour, so contract rule 15 and `seal mutate` have
nothing to run on (`skills/verify/SKILL.md` *The narrow command still has to
be able to fail*). What the removal can break is every file that read the
deleted paths. The census of the old spellings follows.

**The census of the old spellings at e24c3b31b** (executed):

- `git grep -n -E 'acts\.md|test_every_orchestrator_act_names_its_delivery|which of these acts runs itself|Delivered by|part of its parent' -- ':!seal/threads'`
  prints nothing and exits 1.
- `git grep -n 'still a sentence' -- ':!seal/threads'` prints only
  `tests/skills/test_session_cost.py:17`, the history line O3 keeps.
- `git grep` on the removed rule's other words, "acts are counted", "what
  notices when", "act is skipped", "counted by nobody", "orchestrator's own
  table", "each of its acts is a sentence" and `#330`, outside
  `seal/threads/`, prints no line about the table. "runs itself" matches
  only `hooks/lib/launch.py:88`, which is about an interpreter.
- `.test_durations` parses as JSON and holds no key naming
  `skills/implement/acts.md`, the deleted module or the deleted case
  (executed: `python3 -c "json.load(...)"`, then `grep -n`).

**Acceptance, read at e24c3b31b.**

- A1: the two searches above (executed).
- A2: `bin/seal rules --check` exits 0 and prints "all 225 check lines in 70
  rule files hold" (executed). `docs/running/the-agent-set.md` *What a spawn
  costs* lost the acts paragraph and its check line, and the payload rule
  above it is unchanged. `docs/layout/the-pact.md:68` names
  `tests/behaviour/test_a_signer_declares_its_pact.py` alone (read, in the
  diff).
- A3: neither `skills/*/orchestration.md` cites `acts.md`, and
  `skills/code-review/orchestration.md` still says every `##` heading opens
  with `Orchestrator:` (read, in the diff).
- A4 and A5: their modules ran in the phase-boundary command below, and
  passed (executed).
- A6: the diff adds no test, check, hook, mark or rule. Each removal is a
  row of `## Removes`, and the two departures above narrow two of those rows
  (read).
- A7: `.claude-plugin/plugin.json` is outside the diff and reads `0.31.1`
  (executed: `git diff --stat HEAD~1`, `grep version`).

**The phase-boundary command** ran 70 modules in one `bin/test -q` call: the
test modules that name a changed path, and those that glob `skills/`,
`docs/` or `tests/` (executed: `git grep -l` over `tests/`). Seven modules
the search listed were left out after reading, because they match on a
fixture tree or a word and do not read a changed path:
`tests/skills/test_chain_check.py`, `tests/skills/test_settle.py`,
`tests/skills/test_seal.py`, `tests/skills/test_unverified_check.py`,
`tests/evals/test_seed_defects.py`,
`tests/skills/test_agentic_pytest_record.py` and
`tests/skills/test_session_cost.py`. On the build commit the run gave 2302
passed, 13 skipped and 1 failed. The failure was
`tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
which names this work item because `gaps.md` did not exist yet. With this
record, `gaps.md` and `changelog.md` written, the same command, with
`tests/github/test_publish_release_note.py` added for the fragment, gave
2355 passed and 13 skipped, exit 0, on the tree the record commit holds
(executed).

**One thing the removal leaves without a reader.** The marker test's
`headings` returns `(level, title, line)`, and its one caller,
`marked_headings`, discards the level. The level was read by the deleted
module. `frame/design.md` *Data & interfaces* says `headings` keeps its
signature, so it stays (`gaps.md` *Not done*).
