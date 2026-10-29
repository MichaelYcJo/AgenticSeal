# Phase 2: 1793251204-the-framer-is-handed-the-body-without-its-comments

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | df003309 |

## What this phase was asked

Build `frame/plan.md` *Phases* row 2 as it states it, and run the checks
its *Verified by* cell names. The working rules phase 1 records apply here
too.

## What this phase found

**The frame holds against the tree (read).** The folding paragraph stands
at `skills/implement/orchestration.md:37-47` and the acts table's row
*Orchestrator: the order inside a ticket* at `:452`, both at `c1240e0b`.
Step 4's clause "The ticket and its comments" stands at
`agents/framer.md:69-70`, and the probe rule's `check:` line at `:149`.

**Where each sentence went.** The orchestration sentence follows "folds
the decision into the issue body instead (...)". It leaves every phrase
`tests/text/test_the_rules_have_one_owner.py` pins in that paragraph whole.
The acts row keeps "the three rules under the steps", because the new
sentence sits inside the folding paragraph and adds no rule of its own. The
row's list of what no check refuses gains "a framer spawned with no line
on the issue's comments". In step 4, the framer's clause cites the
orchestration section for what the line holds and does not restate it. The
two files share no run of 15 words, which
`tests/text/test_no_passage_is_pasted_into_a_second_file.py` reads.

**No other sentence stated the old fact (executed).** `git grep -n -i`
for "issue's comments", "its comments", "issue comments" and "the
comments" over `agents`, `skills`, `docs`, `templates`, `CLAUDE.md` and
`CONTRIBUTING.md` lists the two edited files, the heading
`docs/issues-and-milestones.md:288`, a sentence at `:307` about comments
as readings, and `docs/the-record-layout.md:316` about a template's
comments. The policy sentence at `docs/issues-and-milestones.md` is the
design's `## Rule changes` item, and the settle writes it.

**`agents/framer.md`'s size (executed: `wc -c`, `wc -l`).** 11,889 bytes
and 212 lines before, 12,488 bytes and 219 lines after: 599 bytes more.

**The phase boundary (executed).** The plan names every module that `git
grep -l -e framer.md -e orchestration.md -e '"framer"' -- tests/` lists,
with `tests/github/test_rules.py` and
`tests/text/test_no_passage_is_pasted_into_a_second_file.py`. Contract rule
2 also takes the modules that glob the directories holding the two files,
so the set added every module naming `"agents"`, `'agents'`,
`"implement"` or `skills/implement`. That made 68 modules in one `bin/test
... -q` command. It exited 1: 2,606 passed, 8 skipped, and one failed,
`tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
which reads "work items with no closing overview:
['1793251204-the-framer-is-handed-the-body-without-its-comments']". The
work item has held `frame/design.md` since `c1240e0b` and has no `gaps.md`
yet, so the case fails from the frame commit on and not from this phase's
edits. Phase 3 writes `gaps.md` when the build ends and runs the case
again.

**Prose only, so no case was written new and no `seal mutate` ran.** The
two files are instructions a session reads. The modules above are what
parses them (`skills/verify/SKILL.md` *The narrow command still has to be
able to fail*, the prose row).
