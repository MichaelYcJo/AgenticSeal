# Implementation Plan: the test durations are refreshed and say when next (#874)

<!-- seal/specs/1791852613-the-test-durations-are-refreshed-and-say-when-next/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-13 by the orchestrating session, under the owner's `automation` answer, when `smith` was spawned.

<!-- The line above is the record that the gate happened. Fill it in at the
spawn: reading this plan and spawning the builder IS the approval, so nothing
extra is being asked for here — only that the approval stop living in a
transcript. A later session, a reviewer and CI all read the tree, and a plan
with nobody's name on it is indistinguishable from one nobody approved. -->

## Summary

Three phases, two CI waits between them, and the pushes and dispatches are
the session's. Phase 1 plants the check that says when the file is refreshed
next, seen red on the real tree, with the two sentences that name it; then
puts `test.yml` into the recipe's measuring shape in a commit of its own and
hands back for the session to push and dispatch. Phase 2 reads that run,
downloads the artifact, and commits the LF file together with the restore of
`test.yml`, then hands back for the second push and dispatch. Phase 3 reads
the post-refresh run, re-sets the budgets by the rule beside the values, and
writes the records.

The frame is #841's and #864's one step on: the same file, the same plugin,
the same rule for a budget, and the same way of measuring (the leg's own
jobs, read with `gh`). What is new is the check: until now the file's age was
a sentence in `CONTRIBUTING.md` and a number in a framer's probe, and the
file went from 3.9 % to 9.4 % unpriced in five days with nothing saying so.

**Each phase fits one spawn.** Phase 1 is one hook, one function, one case,
its fixture cases, two documents' sentences and one workflow edit. Phase 2 is
one download and one commit. Phase 3 is reads of one run, the `timeout`
values, and the records. The CI runs between them are not the smith's clock:
the smith hands back at each push, and the orchestrating session pushes,
dispatches and polls `gh run view <id> --json status,conclusion` until the
run concludes, then spawns the next phase with the run id.

## Technical context

**Why the smith hands back at the push.** `skills/agent-contract/SKILL.md`
§6 withholds pushing from every agent whatever its file says, and #864's plan
put the push and the dispatch with the session for that reason. The spawn
prompt for this frame said the smith could push a measuring branch itself;
this plan does not take that reading, because the contract outranks a prompt
(§3), and the cost of the other reading is two commands by the session.

**Why no measuring branch.** `test.yml`'s `on:` runs on `push` only for
`main`, on `pull_request` events, and on `workflow_dispatch`. This branch has
no pull request until the chain opens one, so pushing it at the measuring
commit runs nothing; `gh workflow run test.yml --ref
chore/874-the-test-durations-are-refreshed-and-say-when-next` runs the
workflow at the branch's tip, which is the measuring commit at that moment.
The restore commit follows, so the branch's final tree has the four Windows
shards and the squash leaves no measuring commit behind. The spawn prompt
offered exactly this as its second form. A throwaway branch would need the
smith to move HEAD or the session to push a second ref for nothing.

**The measuring shape, from `CONTRIBUTING.md`'s recipe** (`read`
2026-10-13): the four `windows-latest` entries replaced by one,
`{ os: windows-latest, python: "3.12", store: "--store-durations", timeout: 55 }`;
the three macOS entries and ubuntu untouched; `${{ matrix.store }}` appended
to the pytest line after `${{ matrix.split }}`; an
`actions/upload-artifact@v4` step after it with `if: always() &&
matrix.store != ''`, `path: .test_durations`, `include-hidden-files: true`.
On that commit the shard case fails on every leg (the Windows leg has no
shards) and the new staleness case fails on every leg (9.4 % today); the
Windows job is therefore red and `always()` is what uploads the file
regardless. `--store-durations` under `-n auto` worked when the file was
first made (#841, phase 3), and the file's 13,042 entries are that run's.
The Windows leg ran 1,974 s of pytest unsharded at #841's size and the file
sums 7,530 s of case time; 655 cases later, 40 minutes is the expectation
and 55 the budget the recipe already gives.

**Where the check reads the collection.** `pytest-split` 0.11.0's
`PytestSplitPlugin.pytest_collection_modifyitems` is `@hookimpl(trylast=True)`
and replaces `items[:]` with the group (`read` 2026-10-13 from the wheel,
through `uvx`, lines 152–169 of `pytest_split/plugin.py`). A default-order
hook in `tests/conftest.py` therefore runs before it and sees every collected
item, on a shard as on ubuntu; `-n auto` changes nothing, because each xdist
worker collects the whole suite and runs the hook itself. `-k` is applied by
pytest's own mark plugin, registered before `conftest.py` and so called after
it, which is why `bin/test tests -k test_the_durations_file_prices_the_suite`
runs the case alone against the whole collection — the form the smith types
and the recipe names. `pytest-split` is CI-only (`run_tests.py`'s
`PYTEST_SPLIT` comment: not in `PACKAGES`, `bin/test` never divides), so the
local proof of S3 under `--splits` goes through
`uvx --with pytest --with pytest-xdist --with pytest-split==0.11.0 --with
markdown-it-py==4.2.0 --with pillow==12.3.0 --with cmarkgfm==2025.10.22
python3 -m pytest tests -q -p no:cacheprovider -k
test_the_durations_file_prices_the_suite --splits 3 --group k` for k in 1..3
rather than by installing the plugin into `.venv`, which `bin/test` reuses
and which would then differ from what `run_tests.py` built. Node ids are
relative to pytest's rootdir, which is the repository root for every
invocation that names `tests/` from it; the file's keys are the same ids,
written by the same plugin.

**Declining a partial collection.** The suite has one convention for a case
whose verdict needs the whole corpus: `tests/conftest.py#decline_if_shrunken`
skips with a reason naming what is missing. The staleness case follows the
shape, not the helper: when no argument of
`session.config.invocation_params.args` resolves to the `tests` directory,
it skips with a reason saying the suite was not collected and which form
runs it. Running one module by name is the common local case and must not
read as a stale file.

**The share, and why one in twenty.** Grounds, in order of weight: the issue
was opened at 3.9 % unpriced, so the line sits where the owner's own
judgment already called the file stale, not above it; one release cycle
added 655 cases, 4.9 % of the suite, so a file refreshed at each release's
preparation stays under the line through the next cycle and a release that
skipped the refresh is refused by the one after, mid-cycle, where the recipe
costs the session one measuring run; and today's 9.4 % is over it, so the
case is red on the real tree before the refresh, which is §15's red without
a fixture. What the number is not: a bound on imbalance. An unpriced case
takes the file's mean, and how far its real cost sits from the mean is what
the division cannot know; the budgets and each leg's `--durations=50` table
are what hold the shards, and S5 reads them. The owner may overturn the
value at approval (`questions.md` Q1), and the constant is one line.

**The planned refresh at release preparation.** `docs/release-checklist.md`
§0 is a list of boxes a release session ticks before the preparation branch;
a box there that dispatches the measuring run from the release branch —
by the recipe, on a branch cut for it — and commits the file in the
preparation commit makes the refresh a planned act at the one moment the
file can price every case of the release. The check is then the backstop:
it fires only when a release skipped the box or a cycle grew past a
twentieth. This is one box in a `docs/` file, which the plan's approval
covers (`questions.md` Q5).

**The budgets after the refresh.** The rule is `test.yml`'s comment: 1.5
times the leg's slowest measured job rounded up to 5, the base being the
slowest of the runs measured. The comment's bases today (`read`): ubuntu
9 m 03 s → 15; macOS 6 m 56 s per shard (run 37700567455) → 15; Windows
10 m 34 s per shard (run 37469595104) → 20, although #864's phase 2 measured
Windows shards at 11 m 25 s and 11 m 52 s in run 37700567455 and did not
move the comment, which 1.5 × 11 m 52 s = 17.8 → 20 explains. Phase 3 reads
the post-refresh run's eight jobs, takes each leg's slowest, and moves a
base only upward; where the rounded value changes the `timeout` changes,
and the comment names the run either way. The macOS re-set is the sentence
in `CONTRIBUTING.md` that the refresh owes: the file prices a case as
Windows ran it, so the macOS groups move when the file does.

**The ledger.** `seal/config.md` declares `Ledger frozen from 1790993141`,
so no released row changes. Rows this work drifts (`read` 2026-10-13):
0.21.0's S1–S5 and its re-reads of 0.20.0's S1, S2, S8 all anchor
`.github/workflows/test.yml#"pytest:"@fd3a49c3`, which phase 3's `timeout`
and comment edits move — `evidence-check --reverify --into
seal/ledger/1791852613-the-test-durations-are-refreshed-and-say-when-next.md
--checked <date>` writes the `Re-read ·` rows after each claim is read and
holds. 0.21.0's S5 and its re-read of 0.20.0's S9 anchor three quoted
`CONTRIBUTING.md` lines; the recipe paragraph's first line, *`.test_durations`
goes stale as cases are added, which unbalances the*, is not one of them
but the line below it, *Windows and macOS shards and drops no case. The file
is the Windows leg's,* is — phase 1's sentence edit lands after it, so the
anchor holds unless the smith rewraps that line, in which case the row takes
a `Corrected ·` entry re-pointing it. 0.20.0's S4 anchors the three existing
cases of the shard module by name and hash; adding a function to the module
does not move them. `tests/conftest.py`'s S7 anchors (`CASE_CEILING_S`,
`over_the_ceiling`, `pytest_runtest_makereport`) are untouched by a new hook
placed beside them. Between phase 3's edit and its fragment, `evidence-check
.` reads DRIFTED and nothing BROKEN, and the CI `ledger` job warns and does
not fail.

**What breaks in six months.** The file ages again, and this time the case
says so at a twentieth: the red lands on whichever pull request crosses it,
and the recipe costs that session one measuring run of about forty minutes
on Windows, with no person asked — the direction is *block more* and the
prompt budget is zero. The second thing is the hook: a plugin added later
with a `tryfirst` `pytest_collection_modifyitems` that trims the list would
make the record partial on a shard and the case red on every leg after the
next refresh — loudly, and the S3 proof through `uvx` is how it is read.
The third is a contributor running `pytest` from inside `tests/`, where node
ids lose their `tests/` prefix: the case declines, because no argument
resolves to the suite directory, and `pytest-split` would misprice
everything in that invocation anyway, which nobody runs sharded locally.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. A sentence: *refreshed at each minor release* | #874 is what a sentence buys: the recipe said what to do and nothing said when, and the file reached 9.4 % with no reader. `CLAUDE.md`'s first goal refuses a design that depends on a person remembering | Rejected |
| B. A suite case that fails past a share of unpriced cases, with the release box as the planned moment | The red lands mid-cycle on an unrelated pull request when a release skipped the box; that session runs the recipe, forty minutes unattended. The share is a proxy and not a bound on imbalance | **Chosen** |
| C. A release-only step in `hygiene.yml` that collects the suite and refuses a stale file at the release pull request | Needs the test-only pins installed in a job that installs nothing today, a second copy of the pip line a case holds to `run_tests.py`, and it fires at the release's own pull request, which is the moment the owner's `CLAUDE.md` calls the worst to stop a release | Rejected |
| D. The case warns below the share and fails above it | A pytest warning is printed once at the end of a run that prints 13,000 dots and nobody reads it; that is the sentence of A with a digit | Rejected |
| E. A `workflow_dispatch` input that runs the Windows leg unsharded with `--store-durations` and uploads, no measuring commit | One command per refresh and the shard cases never red. Costs: three `${{ }}` expressions on lines two cases pin by shape, `matrix` unreadable in a job-level `if` so the other three Windows shards still start, and a design that has to be proved on a real run before the recipe can point at it. The right next design if the per-release box proves costly by the recipe; the report asks the orchestrator to file it | Rejected here |
| F. The case collects the suite in a subprocess (`pytest --collect-only -q`) rather than reading the session | Always the whole suite whatever the invocation, at 6 s on this machine (`executed`) and an unmeasured figure on Windows, paid by one shard per run; and a second pytest inside pytest is a shape the suite has no precedent for | Rejected; the hook is free and `pytest-split`'s `trylast` makes it correct |
| G. A count instead of a share (`> 500 unpriced`) | Does not scale with the suite; 500 was 3.9 % at 12,819 and would be 3.7 % at 13,474 | Rejected |
| H. A share of 10 % | Today's 9.4 % would pass, and the owner opened #874 at 3.9 %; the check would let the file get where it is now with nothing said | Rejected |
| I. A share of 3 % | Under one cycle's growth (4.9 %), so a release that refreshed at preparation would still see the red before the next; the planned moment would stop being the schedule | Rejected |
| J. A throwaway measuring branch pushed from a second ref | The smith cannot move HEAD or push; the session would push `HEAD:refs/heads/measure/874` for a run the branch itself can be dispatched for, and delete it after | Rejected; the branch is dispatched at the measuring commit |
| K. Plant the check in phase 2, after the refresh, seen red by the smith against the old file before committing | Loses the one red the real tree gives for free, and the measuring run would not price the case | Rejected; phase 1 plants it |

## Phases

Vertical slices — each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **The check, the sentences, and the measuring commit.** Commit A: `tests/conftest.py` gains the `pytest_collection_modifyitems` hook recording every collected node id on the session, placed beside the ceiling hook with a docstring saying why it must run before `pytest-split`'s. `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` gains `STALE_SHARE = 0.05`, one pure function returning the unpriced ids of `(collected, durations)`, `test_the_durations_file_prices_the_suite` reading the session's record, declining with a reason when no invocation argument resolves to `tests/`, and failing with the counts, the share and the recipe's section; and the fixture cases at the boundary (one in twenty passes, one more fails, an empty collection is refused, a dead entry does not count). The module docstring says what the file is now held to. `CONTRIBUTING.md`'s recipe paragraph: the file is refreshed at each release's preparation and whenever that case goes red, naming the case and the `-k` form that runs it alone. `docs/release-checklist.md` §0: the box. Every new case seen red (§15): the suite case red on this tree before the refresh with its message quoted in `phases/phase-1.md`, each fixture case red with its comparison inverted or `STALE_SHARE` set so it passes. Commit B: `test.yml` in the measuring shape, exactly as `CONTRIBUTING.md` writes it, nothing else in the commit. The hand-back names the push and the dispatch for the session, and the budget of 55 the run is held to | Locally, exit read directly (§1): `bin/test tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py tests/test_a_slow_case_names_itself.py tests/test_ci_gives_the_checks_what_they_need.py tests/test_a_workflow_is_read_the_one_way.py tests/test_docs_line_wrap.py -q` at commit A, with the suite case reported skipped (one module named) and the fixture cases green; `bin/test tests -q -k test_the_durations_file_prices_the_suite` red at commit A with the message; the `uvx` form of S3 under `--splits 3`, groups 1–3, exactly one group running the case and it red for the same reason; at commit B the shard case red for `windows-latest`, as the recipe says. **Needs a CI run** the session starts: `git -C <wt> push`, then `gh workflow run test.yml --ref chore/874-the-test-durations-are-refreshed-and-say-when-next`, and `gh run list --workflow test.yml --branch <branch> --limit 1` for the id | |
| 2 | **The file.** Read the measuring run: the Windows job's `startedAt` to `completedAt`, its summary line, and that the artifact exists (`gh run view <id> --json jobs`, `gh run download <id> -n <artifact>`). Convert line ends to LF, confirm the file parses and its entry count against the job's `passed` plus `skipped`, and that the unpriced count against this tree's collection is zero. One commit: the downloaded `.test_durations` and `test.yml` restored byte for byte to commit A's content (`git diff <A> -- .github/workflows/test.yml` empty). `phases/phase-2.md`: the run id and SHA, the job's time and summary, the entry count, the sum of seconds, the unpriced and dead counts before and after. The hand-back names the second push and dispatch | Locally, exit read directly: `bin/test tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py -q` green with the suite case skipped; `bin/test tests -q -k test_the_durations_file_prices_the_suite` green; `python3 -c` over the file for CRLF absence, or `file`. **Needs a CI run** the session starts the same way, at the restore commit | |
| 3 | **The balance, the budgets and the records.** Read the post-refresh run's eight jobs: `startedAt` to `completedAt`, each summary line, each shard's `--durations=50` head, the shards' sums against ubuntu's (S5), the slowest Windows shard against 12 minutes and the slowest shard's ratio to the mean by pytest seconds on both legs. Apply the rule to every leg: a base that moved upward changes the comment's figures and run id, a rounded value that changed moves the `timeout` (S6). `seal/ledger/1791852613-the-test-durations-are-refreshed-and-say-when-next.md`: one row per S1–S7 with run ids and dates; the `Re-read ·` rows by `--reverify --into` for every released row `test.yml#"pytest:"` moved, each claim read first; a `Corrected ·` row for any quoted `CONTRIBUTING.md` line phase 1 rewrapped. `changelog.md`: one `### Changed` entry — the file's age before (1,270 unpriced of 13,474, 838 dead) and after, the measuring run's id and the Windows job's time, what each leg's slowest shard took before and after, the case and its share, and what a contributor does when it goes red. `overview.md` closed, its `## Not verified` table naming the sealer for the whole suite and the pull request's run for GitHub reading the new budgets. `phases/phase-3.md` with every figure | Locally, exit read directly: the five modules of phase 1 again; `python3 skills/evidence-check/scripts/evidence_check.py --strict .` exit 0 after the fragment. The pull request's run at the final SHA is what confirms the job reads the budgets | |

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true, which is the failure the evidence ledger exists to prevent.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past one
— someone can open it — which is the same trick that lets a round record live
beside the contract rather than in tool state.

Fill it in as each phase closes, not at the end. What a phase discovers while
it is being built, and needs the next phase to know, goes to
`seal/specs/1791852613-the-test-durations-are-refreshed-and-say-when-next/phases/phase-N.md`,
from `templates/sdd-phase.md`, when the phase closes. **Re-read the Status
column after any rebase**: a squash orphans these commits in every clone but
the one that wrote them.

## Operational impact

- **CI only; one new red a contributor can meet.** No migration, no
  environment variable, no new package: `pytest-split` is already pinned on
  the pip line and the hook is stdlib. `hooks/` and `skills/` are untouched,
  so nothing that ships moves and no version bump is owed.
- **Two Windows runs of the whole suite on this branch**, about forty
  minutes each at budget 55 for the measuring one, started and polled by the
  session; one more sharded run after the restore. GitHub's concurrent-job
  cap is shared with the release's other branches, as #864 recorded.
- **The planned refresh is a box at every release's preparation**, by the
  recipe, from the release branch: one dispatch, one download, one file in
  the preparation commit. A release that skips it meets the case the next
  time the suite grows past a twentieth, on whichever pull request crosses
  it, and that session runs the recipe. The direction is *block more*; the
  prompt budget is zero; the cost of a wrong red is one measuring run.
- **`bin/test <module>` reports one skip** for the suite case with its
  reason; `bin/test` over `tests/` runs it. `-k` selects it alone against
  the whole collection, which collects 13,474 cases in about six seconds
  here.
