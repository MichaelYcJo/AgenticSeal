# Phase 1: 1793829112-a-release-branch-requires-its-checks

## What this phase found

**The frame holds against the tree at 01c58e3c.** Each coordinate the build
stands on was opened before the first edit (read). The paragraph
**Two rulesets enforce the merge methods.**, its table and the no-bypass
sentence stand at `docs/releasing/branch-and-release.md:207-221` (G1). The
first box of *0. Before starting* stands at
`docs/releasing/release-checklist.md:13-16` (G12).
`tests/text/test_the_release_tail_does_not_end_at_the_tag.py#squash_rule`
ends its paragraph at the literal bold lead (G13). Lines 36 and 198 of
`docs/releasing/branch-and-release.md` still state facts the change keeps
true (G2), and so does line 176, which says the `main` ruleset does not
offer a squash. The job names `lint` in `.github/workflows/test.yml` and
`release` in `.github/workflows/hygiene.yml` are as G4 states (read).

**One sentence of the new paragraph is narrower than Scope 2b's wording.**
Scope 2b says the chain check refuses "a ready pull request whose suite did
not run at HEAD". The broad-gate arm reads `trail/gate.md` of the work items
a pull request declares (`docs/checks/the-pull-request-check.md` *The broad
run has one home, `trail/gate.md`, on either routing answer.*, read), and a
pull request with no work item, such as a settle's, has no such record. The
document therefore says "a work item's ready pull request whose broad run is
not at HEAD". Judged against `skills/core/SKILL.md` *Judgment is not licence
to skip a party.*, whose table row names the same arm.

**The table names the `main` ruleset's target as "the default branch,
`main`".** The setting holds `~DEFAULT_BRANCH` (G1), a token a reader would
have to resolve, and the default branch here is `main`. Judged against
Scope 2a, which asks for the target as the setting holds it.

**The version move is beyond the phase's Delivers cell, and the spawn gave
it.** `frame/design.md` *Scope*, the Out list, leaves the move of
`.claude-plugin/plugin.json` to the orchestrator, in the commit that adds
the changelog fragment of the release's first work item. The spawn named
this item as that first item, and the build made the move from 0.32.0 to
0.32.1 in fc538c70, the commit that adds `changelog.md`
(`skills/implement/orchestration.md` *Orchestrator: how the work is
routed*, the paragraph **Which branch the pull request lands on is decided
with the routing question.**; precedent 9c36bbda, read).

**No case was written and no `seal mutate` run was made.** The diff is
prose in two documents, which the *Prose only* row of
`skills/verify/SKILL.md` *The narrow command still has to be able to fail*
covers: what can fail is whatever parses those files. No unit adds
behaviour, and `frame/plan.md` *Technical context* adds no `check:` line,
because no case can read a repository setting. There was nothing to lint:
the diff holds no Python file, and `ruff` opens no Markdown file.

**The first commit of the paragraph held a 96-column line**, left by an
edit that joined two lines. `tests/behaviour/test_docs_line_wrap.py`
passed over it, since `docs/releasing/branch-and-release.md` is not among
the files its `COVERED` list names, while `release-checklist.md` is (read). It was rewrapped in 807708a1, and every line the
range adds under `docs/` is at most 76 columns (executed: an `awk` length
read over those added lines).

**The narrow modules pass at HEAD.** Each of the 18 modules
`git grep -l -E 'branch-and-release|release-checklist' -- tests/` lists,
`tests/conftest.py` aside, ran alone through `bin/test <module> -q -p
no:xdist` and exited 0 (executed), after the version move and the rewrap.
`squash_rule` still ends at `**Two rulesets enforce the merge methods.**`
(executed: `tests/text/test_the_release_tail_does_not_end_at_the_tag.py`,
7 passed).

**The other statements of the reworded rules stand true.** A
`git grep -n -i -E` over the tree for `commit that merged`, `applies to the
owner`, `bypass actor`, `required check`, `status check`, `Release
branches`, `` `release/*` `` and `ruleset` lists, outside this section,
`docs/releasing/branch-and-release.md:36`, `:176` and `:198`, which stay
true, and mentions of the `release/*` push trigger in
`.github/scripts/label_merged_on_release_branch.py`,
`.github/workflows/label-merged-on-release-branch.yml`,
`docs/releasing/issues-and-milestones.md:247` and three test modules, which
describe a workflow trigger and not a ruleset (executed). That list is a
search on words, and so a sample.
