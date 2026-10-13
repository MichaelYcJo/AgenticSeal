# Round 1 report — 1791852613-the-test-durations-are-refreshed-and-say-when-next (#874)

| Field | Value |
|---|---|
| Target | `chore/874-the-test-durations-are-refreshed-and-say-when-next` at `64afbf9f`; base `origin/release/v0.21.1` at `321e9de1`; phases 1 to 3, the whole build |
| Kind | first round of the run, over the whole branch |
| Where it ran | a `git clone --no-local` of the worktree at `64afbf9f`, under `<scratchpad>/1791852613-the-test-durations-are-refreshed-and-say-when-next/round-1/clone`, removed at handover |
| Ran by | specseal:warden on claude-opus-5-5 |
| Load | every `bin/test` call ran with `SPECSEAL_CASE_CEILING_S=600` |

No earlier round exists, so nothing was carried. The phase records,
`overview.md` and the commit messages were read as the implementer's
account, and each claim below that rests on them was checked against the
tree, the pytest-split 0.11.0 wheel or GitHub.

## How the findings relate

```
213 path-carrying ids stay unpriced on ubuntu and macOS after every refresh
        |
        +--> 🟡 1  STALE_SHARE's written ground (a refreshed file stays green
        |          through a cycle) is false on those legs; two documents still
        |          say every leg collects the same cases
        |
release box schedules the refresh
        +--> 🟡 2  the box lists the refresh's steps and drops the macOS
                   budget re-read the recipe requires after it
paperwork
        +--> ⬜ 3  Corrected · S3 leaves out a coordinate the released row carried
        +--> ⬜ 4  a comment line in test.yml left short by an in-place cut
```

## What the prompt asked to confirm

- **The decline rule reading `config.args` is right.** `bin/test` hands pytest
  `tests` only when it gets no argument at all
  (`.github/scripts/run_tests.py:656`), so the sealer's `bin/test -q` reaches
  pytest with no path. The plan's rule on `invocation_params.args` would skip
  the case there. I ran `bin/test -q -rs -k
  test_the_durations_file_prices_the_suite` with no path: exit 0, `1 passed`,
  not skipped. The module named alone gives `8 passed, 1 skipped` with the
  reason (executed). The xdist workers re-parse the controller's arguments in
  its directory, which is why the pathless form also works under `-n auto`.
- **Q4's evidence holds.** I read the log of job 115084708572 (macOS
  `--splits 3 --group 3` of run 38332345615). It says `1276 of the 13480
  collected cases`, which is the whole suite and not the group's 3,110. A
  record taken after the split would have held only the group (executed).
- **The 625 entries nobody collects are rightly left as a Not done
  candidate.** In the wheel's algorithms module, the durations are filtered to
  the collected ids before the mean is taken, so a dead entry changes neither
  the mean nor the division (read). They cost bytes only.
- **The 213 POSIX ids are not rightly left alone in one respect.** The ids
  fix can wait for an issue. The ground written beside `STALE_SHARE` cannot,
  because the 213 make it false. That is 🟡 1.
- **The `Corrected · S3` row is the right kind of row.** 0.21.0's S3 named
  6 m 56 s as the macOS base, and the comment now names 8 m 29 s, so the claim
  stopped holding and a correction is owed. The row leaves out one coordinate
  the released row carried, which is ⬜ 3.
- **The budgets and every figure in the comment match GitHub.** I read the
  jobs of runs 37576998008, 37577753583, 38332345615 and 38335775781 with `gh
  run view --json jobs`. Windows group 4 of 37576998008 took 12 m 42 s, macOS
  group 3 of 38332345615 took 8 m 29 s, ubuntu there 9 m 43 s, and the eight
  jobs of 38335775781 match `phases/phase-3.md` to the second. 1.5 times each
  base, rounded up to 5, gives 15, 15, 20 and 60 for the measuring leg
  (executed and computed).
- **The doc edits follow the owner's rule, except for one sentence.** The
  `CONTRIBUTING.md` paragraph was rewritten in place: the refresh moment sits
  inside the paragraph, and the 55-minute parenthesis was replaced, not
  followed by a correction. The release-checklist box states a new step and
  narrates nothing. The `test.yml` comment was rewritten in place. The
  sentence left stale is *every leg collects the same cases*
  (`CONTRIBUTING.md:191`), which phase 2 found untrue for 213 ids; it belongs
  to 🟡 1's class.
- **`evidence-check --strict .` exits 0** on the clone, `0 drifted · 0
  broken`, and the records arm reads `0 stamps read · 0 refused` (executed).

## Findings

### 🟡 1 — The share's written ground does not hold on ubuntu and macOS

The comment above `STALE_SHARE`
(`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:56`)
gives the reason for one in twenty. One release cycle grew the suite by
4.9 %, so a file refreshed at a release's preparation would stay under the
share through the next cycle. `questions.md` Q1 and `plan.md` rest the value
on the same sentence. Alternative I rejects 3 % because a refreshed file
would turn red within a cycle.

That holds on Windows only. I collected the suite on this tree and compared
it with the committed file (executed). 213 of 13,480 ids (1.58 %) have no
price right after the refresh, in six modules. Every refresh starts the
ubuntu and macOS legs at that floor, so the margin there is 3.4 points, which
is option I's failure. On this collection the case goes red on those legs
after about 485 new cases. 0.21.0 added 655.

The cause is the ids, and two kinds are mixed in the 213.

- **205 carry a relative path** built with `os.path.join` or
  `os.path.relpath`, which Windows writes with a backslash. The 170 in
  `tests/test_a_moved_rule_leaves_its_definition.py` and the 25 in
  `tests/test_every_agent_reads_the_contract.py` come from their `name`
  helpers (lines 114 and 117). The rest are in
  `tests/test_unverified_rows_close.py`,
  `tests/test_local_mode_resolves_under_the_git_dir.py` and
  `tests/test_the_contributor_has_a_procedure.py`.
- **8 carry the interpreter's absolute path.**
  `tests/test_the_seal_is_taken_once_by_the_sealer.py` builds `SUITE_ROW`
  from `sys.executable`, and three parametrizations (lines 1907, 1956, 3138)
  put it in the id. No file can price those on any machine other than the one
  that measured. `overview.md`'s Not done names `as_posix()` as the fix, and
  it does not reach these eight.

The class this belongs to is a sentence the branch's own phase 2 disproved
and left standing. I found three instances:

- the `STALE_SHARE` comment, above;
- `CONTRIBUTING.md:191`, *because every leg collects the same cases*, in the
  paragraph this branch rewrote;
- the module docstring, line 10, *One file divides both legs, because every
  leg collects the same cases*.

Phase 2 wrote *Recorded for whoever revisits Q1*. Under `automation` nobody
revisits Q1, so the floor reaches no one. The release would ship a check
whose remedy cannot clear part of what it counts. The share of path ids also
grows with every agent file or contract section added, since the 170 are
agents times sections.

The fix makes the ids the same on every machine, so the next refresh prices
them on every leg and the written ground becomes true. Until that refresh,
ubuntu and macOS keep the 213, and Windows gains about 205 under their new
spelling. Both are well under the share. If the run would rather not touch
six modules, the fallback is the comment and the `CONTRIBUTING.md` sentence
rewritten to state the floor, with Q1's margin given as 3.4 points.

### 🟡 2 — The release box drops the budget re-read the recipe requires

`docs/release-checklist.md:55` lists the refresh's steps one by one: cut the
branch, apply the measuring shape, dispatch, download, LF, commit in the
preparation commit, delete the branch. `CONTRIBUTING.md` §*Running the
checks* says that after a refresh *read the macOS shards' times in the next
run's jobs and set their `timeout` again by the rule beside the values*. The
box points at the paragraph only for the measuring shape. A release session
working down an itemised list stops where the list stops, so after each
planned refresh nobody re-reads the macOS budgets. This branch did the
re-read in phase 3 for this refresh; the box is what makes the next refresh
a routine.

A budget that is too tight still fails loudly on GitHub. One that is too
loose hides a slow shard, and that is the case the re-read exists for.

### ⬜ 3 — `Corrected · S3` leaves out the test coordinate the released row carried

`seal/ledger/1791852613-the-test-durations-are-refreshed-and-say-when-next.md:7`
cites the released row and `.github/workflows/test.yml#"pytest:"`. 0.21.0's S3
also carried
`tests/test_a_slow_case_names_itself.py#test_every_pytest_leg_has_a_timeout_and_the_job_reads_it@e49de6ba`
for the clause *the job reads `${{ matrix.timeout }}`*, which the new row
repeats. `docs/the-evidence-ledger.md` says a correction supersedes the whole
released row, so it *carries every coordinate the claim still rests on … a
coordinate it leaves out is not checked again*. Phase 3 moved tests into the
evidence cell because `::` test ids mixed with code coordinates were refused
as MALFORMED. The released row used the `#unit@hash` form, which the checker
accepts beside code (0.21.0's `Corrected · S8` carries the same coordinate
that way). This is the run's paperwork, so it is reported as a correction.

### ⬜ 4 — A comment line in `test.yml` was left short by the in-place cut

`.github/workflows/test.yml:45` reads `# job, rounded up to 5. GitHub fails`
and stops there. Removing *after that item's phases 3 and 4* left the line
unwrapped. Nothing checks comment wrap in YAML, and the text is correct.

## Regression tests to plant

- `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`: a case
  that no collected id carries `sys.executable`. It belongs with 🟡 1's ids
  fix and is red at this tree on every machine, where 8 ids fail it.
- A backslash cannot be refused across the collection: 1,645 ids on POSIX
  carry one from escaped characters such as `—`. The separator half is
  held per helper instead, by a case beside each `name` helper asserting
  that `agents/framer.md` comes back with a forward slash. It can go red only
  on the Windows leg, so its evidence is that leg's run on the fix.

## Facts for the evidence ledger

- pytest-split 0.11.0 filters durations to the collected ids before taking
  the mean, so an entry nobody collects changes neither the mean nor the
  division (read from the wheel's algorithms module, 2026-10-13).
- On this tree's POSIX collection, 213 of 13,480 ids are unpriced in the
  refreshed file. 205 carry a Windows-separated relative path and 8 carry the
  interpreter's absolute path (executed 2026-10-13).

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | `STALE_SHARE`'s written ground is false on ubuntu and macOS: 213 path-carrying ids are unpriced after every refresh, so a 0.21.0-sized cycle crosses 5 % after a preparation refresh; `CONTRIBUTING.md:191` and the module docstring still say every leg collects the same cases | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:56` | open | executed: 213 of 13,480 unpriced on the POSIX collection, red after about 485 new cases against 655 in 0.21.0; 8 of the 213 carry `sys.executable`, which `as_posix()` does not reach |
| 🟡 2 | The release-checklist box itemises the refresh and drops the macOS `timeout` re-read the recipe requires after it | `docs/release-checklist.md:55` | open | read: `CONTRIBUTING.md` §*Running the checks*, the sentence beginning *after a refresh, read the macOS shards' times* |
| ⬜ 3 | `Corrected · S3` cites the released row and `test.yml` but leaves out the test coordinate 0.21.0's S3 carried | `seal/ledger/1791852613-the-test-durations-are-refreshed-and-say-when-next.md:7` | open | read: `docs/the-evidence-ledger.md`, the paragraph on a correction superseding the whole released row |
| ⬜ 4 | A `test.yml` comment line was left short by the in-place cut | `.github/workflows/test.yml:45` | open | read |
| 🟢 | The decline rule reads `config.args`, so the sealer's pathless `bin/test -q` runs the case | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#collects_the_suite` | confirmed | executed: pathless `-k` form `1 passed`; module alone `1 skipped` with the reason |
| 🟢 | Q4: the hook records the whole collection on a GitHub shard | `tests/conftest.py#pytest_collection_modifyitems` | confirmed | executed: job 115084708572's log reads `1276 of the 13480 collected cases` under `--group 3` |
| 🟢 | The 625 entries the merge keeps are bytes only, so leaving them as a Not done candidate is right | `.test_durations` | confirmed | read: the wheel filters durations to collected ids before the mean |
| 🟢 | Every base and `timeout` in the comment and the recipe follows the rule and matches GitHub | `.github/workflows/test.yml:51` | confirmed | executed: `gh run view --json jobs` on four runs |
| 🟢 | `evidence-check --strict .` passes, and S1 to S6 and the 15 re-reads resolve | `seal/ledger/1791852613-the-test-durations-are-refreshed-and-say-when-next.md` | confirmed | executed: exit 0, `0 drifted · 0 broken` |

## Executed probes

| What was run | Result |
|---|---|
| `bin/test tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py -q -rs -p no:cacheprovider` | exit 0, `8 passed, 1 skipped`, the skip naming the `-k` form |
| `bin/test -q -rs -p no:cacheprovider -k test_the_durations_file_prices_the_suite` (no path) | exit 0, `1 passed` |
| `bin/test tests/test_docs_line_wrap.py tests/test_a_slow_case_names_itself.py tests/test_a_reader_declares_its_input_class.py tests/test_ci_gives_the_checks_what_they_need.py -q -p no:cacheprovider` | exit 0, `137 passed` |
| `pytest tests --collect-only -q -p no:xdist` from the clone's runner venv, compared with `.test_durations` by a script outside the tree | 13,480 collected, 213 unpriced (1.58 %) in six modules, 838 keys not collected, about 485 new cases before 5 % |
| `python3 skills/evidence-check/scripts/evidence_check.py --strict .` | exit 0, `0 drifted · 0 broken · 0 malformed` |
| `gh run view` on runs 37576998008, 37577753583, 38332345615, 38335775781, and the logs of jobs 115084708572 and 115084708524 | every time in the comment and the phase records matches; the macOS group 3 log reads 1,276 of 13,480; the measuring Windows log reads 1,063 |
| The whole suite at `64afbf9f` (broad gate) | not yet: the sealer's, once, after the rounds |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| The refresh recipe merges into the old file and keeps 625 entries nobody collects | `overview.md` §*Not done*, a candidate issue | the orchestrator, who files it |
| A `workflow_dispatch` input that measures without a commit | `spec.md` Out and `plan.md` Alternatives E | the orchestrator, who files it |

## Paste-ready fixes

### 🟡 1 — ids that are one spelling on every machine

`tests/test_a_moved_rule_leaves_its_definition.py:114` and
`tests/test_every_agent_reads_the_contract.py:117`:

```python
def name(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")
```

`tests/test_the_contributor_has_a_procedure.py:173`:

```python
@pytest.mark.parametrize(
    "surface", CONVENTION_SURFACES, ids=lambda surface: surface.replace(os.sep, "/")
)
```

`tests/test_local_mode_resolves_under_the_git_dir.py:173` and the
parametrization ending at `tests/test_unverified_rows_close.py:1307` take the
same `ids=` argument. A callable that returns `None` lets pytest keep its own
id for that value:

```python
    ids=lambda value: value.replace(os.sep, "/") if isinstance(value, str) else None,
```

`tests/test_the_seal_is_taken_once_by_the_sealer.py`, the parametrizations
at lines 1907, 1956 and 3138:

```python
    ids=lambda value: (
        value.replace(sys.executable, "python") if isinstance(value, str) else None
    ),
```

The comment above `STALE_SHARE`, rewritten in place:

```python
# The share of the collected cases the durations file may leave unpriced
# before the suite case fails: one in twenty (`questions.md` Q1 of work item
# 1791852613). Every id is one spelling on every machine, so a file refreshed
# on Windows prices the whole collection on every leg, and one release
# cycle's growth (4.9 % in 0.21.0) stays under the share until the next
# release's refresh. It bounds the file's age, not the shards' imbalance: how
# far an unpriced case's real cost sits from the mean is what each leg's
# `--durations=50` table and `timeout` hold.
```

The interpreter case under Regression tests above, beside the suite case
(the module then needs `import sys`):

```python
def test_no_collected_id_carries_the_interpreters_path(request):
    """An id holding `sys.executable` is a key no other machine writes, so
    every refresh leaves it unpriced on every leg but the one measured."""
    config = request.config
    if not collects_the_suite(
        config.args, config.invocation_params.dir, config.rootpath
    ):
        pytest.skip("the suite was not collected")
    collected = getattr(request.session, COLLECTED_NODE_IDS)
    bad = [node for node in collected if sys.executable in node]
    assert not bad, bad[:5]
```

The separator case, once in each module with a `name` helper:

```python
def test_an_agent_id_is_written_with_forward_slashes():
    assert name(os.path.join(ROOT, "agents", "framer.md")) == "agents/framer.md"
```

Fallback, if the ids are left for an issue: rewrite the comment's second
sentence to the truth and `CONTRIBUTING.md:191` with it.

```python
# 1791852613). A refresh measures on Windows, and 213 cases whose ids carry a
# path (1.6 % at the refresh of run 38332345615) are priced under their
# Windows spelling only, so ubuntu and macOS start each cycle with them
# unpriced and have 3.4 points of the share for the cycle's growth.
```

### 🟡 2 — the box carries the re-read

`docs/release-checklist.md`, the box's fourth sentence:

```markdown
      Download it, make its line ends LF, commit it in the preparation commit,
      and delete the measuring branch. When the release pull request's run
      finishes, read its macOS shards' times and set their `timeout` again by
      the rule beside the values, as `CONTRIBUTING.md` §*Running the checks*
      says after a refresh; a value the rule leaves where it is needs no commit.
```

### ⬜ 3 — the coordinate restored

The code cell of `Corrected · S3`:

```markdown
`seal/releases/0.21.0.md#"### 1791384162-the-macos-test-leg-runs-in-shards">"S3 · each macOS"@29f6eea6`, `.github/workflows/test.yml#"pytest:"@2ce0f2a3`, `tests/test_a_slow_case_names_itself.py#test_every_pytest_leg_has_a_timeout_and_the_job_reads_it@e49de6ba`
```

Run `evidence-check --strict .` after the edit; if the unit's hash moved
since 0.21.0, the checker names the current one.

Needs a fix: yes — 🟡 1 (the `STALE_SHARE` ground and the two sentences
that say every leg collects the same cases; the ids fix is the root) and
🟡 2 (the release box's missing budget re-read)

Loses a record or crashes: no

The broad gate is not due yet: two findings are open. It comes due as the
sealer's spawn once a verifying round leaves nothing open.

## Proof block

Files opened in this round, all at `64afbf9f` in the clone or the worktree:

- `seal/specs/1791852613-the-test-durations-are-refreshed-and-say-when-next/`
  `spec.md`, `plan.md`, `questions.md`, `overview.md`, `changelog.md`,
  `phases/phase-1.md`, `phases/phase-2.md`, `phases/phase-3.md`
- `seal/ledger/1791852613-the-test-durations-are-refreshed-and-say-when-next.md`
- `seal/releases/0.21.0.md` (the 1791384162 section), and the S9, P3, A6 and
  H4 rows of 0.11.1, 0.15.1, 0.15.3 and 0.21.0
- `tests/conftest.py` (the new hook),
  `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`
- `.github/workflows/test.yml`, `CONTRIBUTING.md` lines 170 to 225,
  `docs/release-checklist.md` lines 1 to 70, `bin/test`,
  `.github/scripts/run_tests.py` (argument handling),
  `docs/the-evidence-ledger.md` lines 80 to 165, `.gitattributes`
- the parametrizations of `tests/test_a_moved_rule_leaves_its_definition.py`,
  `tests/test_every_agent_reads_the_contract.py`,
  `tests/test_the_contributor_has_a_procedure.py`,
  `tests/test_local_mode_resolves_under_the_git_dir.py`,
  `tests/test_unverified_rows_close.py` and
  `tests/test_the_seal_is_taken_once_by_the_sealer.py` named above
- pytest 9.1.1's hook marks in its stepwise, cacheprovider, main and mark
  modules; pytest-split 0.11.0's algorithms and plugin modules from the uv
  cache
- `seal/specs/1791781864-the-idle-session-rows-ask-nobody/rounds/round-3-report.md`,
  for the report's shape
