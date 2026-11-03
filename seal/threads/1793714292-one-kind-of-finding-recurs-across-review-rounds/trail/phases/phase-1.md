# Phase 1: 1793714292-one-kind-of-finding-recurs-across-review-rounds

## What this phase found

**The frame holds at the three coordinates it builds to.** Before the build,
`docs/releasing/release-checklist.md:98-100` held the sentence naming #1020's
check, and `docs/running/the-run.md:17` held both the zero-finding sentence and
the "Table B" citation, as `frame/plan.md` *Technical context* states (read).
`git grep -n '#1020' -- docs skills agents templates` printed those two lines
of the checklist alone, and `git grep -n -e 'loop having converged' -e 'Table B'
-- . ':!seal/threads'` printed `the-run.md:14` and `:17` alone (executed).
`skills/core/SKILL.md:95` opens with **Judgment is not licence to skip a
party.**, and its table holds the row *No fix that no round reads* (read).

**The frame does not hold at two commit citations of its own.**
`frame/design.md` G8 cites `3937d861` and G9 cites `1c1d18a5`. Neither commit
is on any branch, because both were commits of feature branches that were
squashed (executed: `git branch -a --contains` printed nothing for either).
`tests/text/test_a_cited_commit_outlives_the_squash.py::test_every_cited_commit_outlives_the_squash`
fails on both lines of the design at this phase's boundary run (executed). The
failure comes from the frame commit `7bc1ad12d`, since this phase's commits
leave `frame/design.md` as it stood. The squash commits on `main` hold the
same bytes: `569780eff` (#1257) for
`seal/threads/1793521558-the-record-decides-each-proposed-verifier/trail/phases/phase-2.md`,
and `783a7fe8a` (#1261) for
`seal/threads/1793528484-the-process-measured-on-0-27-2/trail/phases/phase-3.md`
(executed: `git diff --quiet` between each cited commit and its squash, over
that path, exited 0). Replacing each cited SHA with its squash commit answers
the refusal. `agents/crafter.md` *Job* names no write to `frame/design.md`, so
the correction is left to the orchestrator or the framer. The rest of the
frame holds and is built.

**Each of the three sentences was rewritten in place, and no case pinned
any of them.** `frame/plan.md` *Technical context* states that no case pins
either sentence that goes, and this phase's census agrees (executed, the S1 to
S3 commands below). The release checklist's new sentence follows the design's
*Scope* item 1: the settling session files one issue naming each stale copy
that kept the count up and the record it stood in. It cites
`skills/implement/orchestration.md` *Orchestrator: where a decision or a lesson
is written* as the home that table gives a lesson no work item in progress
changes. The regression sentence of *The run* now reads that no fix goes
unread by a round, an invariant the table of `skills/core/SKILL.md` *Judgment
is not licence to skip a party* holds. The wording is judged against that
table's row *No fix that no round reads*, whose protection is that every
change after the last round is read by a round.

**The phase adds no behaviour, so it wrote no case new and owes no `seal
mutate` run.** All three edits are prose. `skills/verify/SKILL.md` *The narrow
command still has to be able to fail* gives prose the row "whatever actually
parses those files", and those are the test modules that read either
document. `skills/implement/SKILL.md` *2. Implement test-first, and let each
rule name its test* builds test-first only where a scenario adds behaviour.
The changed citations are read by
`tests/behaviour/test_a_cited_section_stands_in_its_file.py`, which passes.

**One departure from `frame/design.md` S4.** S4 expects the diff outside
`seal/` to hold the two documents and nothing else. It also holds
`.claude-plugin/plugin.json`, whose `version` moves from `0.30.1` to `0.31.0`
in `df433eee2`, the commit that adds `changelog.md`. The spawn prompt gave
that move as the orchestrator's instruction, since this is the first work item
into `release/v0.31.0`, and `08b43c65f` did the same for 0.30.1 (read). S4's
purpose, that no mechanism is added, still holds: a version string gates
nothing.

**The changelog fragment needs no `### Process changes` section.**
`docs/layout/the-record-layout.md` *A change writes fragments, never a shared
file* asks for one where the diff changes `skills/core/SKILL.md`, `CLAUDE.md`,
an `agents/*.md` file, a `skills/*/orchestration.md` file or
`skills/implement/bootstrap.md`, and this diff changes none of them (read).

**The commands and their results** (executed, at `df433eee2`):

- S1: `git grep -n '#1020' -- docs skills agents templates` printed nothing
  and exited 1.
- S2: `grep -c 'loop having converged' docs/running/the-run.md` printed `1`.
- S3: `git grep -n 'Table B' -- docs` printed nothing and exited 1, and `grep
  -n '^\*\*Judgment is not licence to skip a party' skills/core/SKILL.md`
  printed line 95.
- S4: `git diff --stat 5d89ba07a...HEAD -- ':!seal/'` listed
  `.claude-plugin/plugin.json`, `docs/releasing/release-checklist.md` and
  `docs/running/the-run.md`. `5d89ba07a` is the merge base with
  `origin/release/v0.31.0`.
- S5 and the phase boundary: one `bin/test -q` command over 44 modules. These
  were every module under `tests/` that names `the-run.md`,
  `release-checklist.md`, `plugin.json` or `changelog.md`, plus
  `tests/github/test_finding_counts.py`,
  `tests/behaviour/test_chain_hooks_hardening.py`,
  `tests/behaviour/test_a_cited_section_stands_in_its_file.py`,
  `tests/text/test_no_passage_is_pasted_into_a_second_file.py`,
  `tests/behaviour/test_no_document_names_the_old_roots.py`,
  `tests/behaviour/test_the_set_a_work_item_always_has.py` and
  `tests/text/test_a_cited_commit_outlives_the_squash.py`, which read the
  `docs/` tree or the work items under `seal/threads/`. At `df433eee2`, 2313
  passed, 12 skipped and 2 failed. One failure was
  `test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
  which asks for the `gaps.md` this phase's record commit adds. The other was
  the citation failure above. The two modules ran again after `gaps.md` was
  written, and that run's result is in the hand-back.

**Other statements of the zero-finding round stand, as the frame leaves
them.** `git grep -n -e 'opens nothing' -e 'opening nothing' -e 'having
converged' -- docs skills agents templates README.md CONTRIBUTING.md` listed
`README.md:207` and `skills/code-review/orchestration.md:125-129` besides
`the-run.md:12-14` (executed). `frame/design.md` *Scope*, its *Out* list,
leaves both to #1288, #1318 and #1102. That grep is a sample under contract
rule 12, because it matches spellings and the class is a statement of one
fact.
