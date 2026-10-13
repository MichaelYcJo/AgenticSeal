# 1791852613-the-test-durations-are-refreshed-and-say-when-next — review round 1

| Field | Value |
|---|---|
| Target SHA | 64afbf9fe6a40ab2c0d07850c631f3d67420c971 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #924 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are written and no round has opened them |
| Fix range | `744c610f4db52c59988b6eb967f09950db691636..dfd51a66fa4fac46483d101bcd8aa30d12ad895f`, 8 commits |
| Contract changes | none |
| New units | posix_id (depth 1); interpreter_free (depth 1); test_no_collected_id_carries_the_interpreters_path (depth 1); test_a_path_id_is_written_with_forward_slashes (depth 1) |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1 (the `STALE_SHARE` ground and the two sentences that say every leg collects the same cases; the ids fix is the root) and 🟡 2 (the release box's missing budget re-read) |
| Loses a record or crashes | no |
<!-- New units: .github/workflows/test.yml, .test_durations read by the diff-line heuristic and not by the AST -->

- [ ] Pass

## What this round was asked

Round 1 of #874, target 64afbf9f against `origin/release/v0.21.1` at 321e9de1, over the whole build, phases 1–3 (the measuring and restore commits squash away). The reviewer was asked to judge the decline rule reading `config.args`; whether the 213 POSIX-path ids left unpriced and the 625 stale entries the recipe keeps are rightly left as Not done; Q4's evidence; the 0.21.0 `Corrected · S3` row; and every doc edit against the owner's rule that a change rewrites the existing text in place.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | `STALE_SHARE`'s written ground is false on ubuntu and macOS: 213 path-carrying ids are unpriced after every refresh, so a 0.21.0-sized cycle crosses 5 % after a preparation refresh; `CONTRIBUTING.md:191` and the module docstring still say every leg collects the same cases | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:56` | **fixed** `fa4e9cce` | fixed at fa4e9cce; executed: 213 of 13,480 unpriced on the POSIX collection, red after about 485 new cases against 655 in 0.21.0; 8 of the 213 carry `sys.executable`, which `as_posix()` does not reach |
| 🟡 2 | The release-checklist box itemises the refresh and drops the macOS `timeout` re-read the recipe requires after it | `docs/release-checklist.md:55` | **fixed** `0b71b66d` | fixed at 0b71b66d; read: `CONTRIBUTING.md` §*Running the checks*, the sentence beginning *after a refresh, read the macOS shards' times* |
| ⬜ 3 | `Corrected · S3` cites the released row and `test.yml` but leaves out the test coordinate 0.21.0's S3 carried | `seal/ledger/1791852613-the-test-durations-are-refreshed-and-say-when-next.md:7` | open | read: `docs/the-evidence-ledger.md`, the paragraph on a correction superseding the whole released row |
| ⬜ 4 | A `test.yml` comment line was left short by the in-place cut | `.github/workflows/test.yml:45` | open | read |
| 🟢 | The decline rule reads `config.args`, so the sealer's pathless `bin/test -q` runs the case | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#collects_the_suite` | confirmed | executed: pathless `-k` form `1 passed`; module alone `1 skipped` with the reason |
| 🟢 | Q4: the hook records the whole collection on a GitHub shard | `tests/conftest.py#pytest_collection_modifyitems` | confirmed | executed: job 115084708572's log reads `1276 of the 13480 collected cases` under `--group 3` |
| 🟢 | The 625 entries the merge keeps are bytes only, so leaving them as a Not done candidate is right | `.test_durations` | confirmed | read: the wheel filters durations to collected ids before the mean |
| 🟢 | Every base and `timeout` in the comment and the recipe follows the rule and matches GitHub | `.github/workflows/test.yml:51` | confirmed | executed: `gh run view --json jobs` on four runs |
| 🟢 | `evidence-check --strict .` passes, and S1 to S6 and the 15 re-reads resolve | `seal/ledger/1791852613-the-test-durations-are-refreshed-and-say-when-next.md` | confirmed | executed: exit 0, `0 drifted · 0 broken` |

## Paste-ready fixes

```python
def name(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")
```
```python
@pytest.mark.parametrize(
    "surface", CONVENTION_SURFACES, ids=lambda surface: surface.replace(os.sep, "/")
)
```
```python
    ids=lambda value: value.replace(os.sep, "/") if isinstance(value, str) else None,
```
```python
    ids=lambda value: (
        value.replace(sys.executable, "python") if isinstance(value, str) else None
    ),
```
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
```python
def test_an_agent_id_is_written_with_forward_slashes():
    assert name(os.path.join(ROOT, "agents", "framer.md")) == "agents/framer.md"
```
```python
# 1791852613). A refresh measures on Windows, and 213 cases whose ids carry a
# path (1.6 % at the refresh of run 38332345615) are priced under their
# Windows spelling only, so ubuntu and macOS start each cycle with them
# unpriced and have 3.4 points of the share for the cycle's growth.
```
```markdown
      Download it, make its line ends LF, commit it in the preparation commit,
      and delete the measuring branch. When the release pull request's run
      finishes, read its macOS shards' times and set their `timeout` again by
      the rule beside the values, as `CONTRIBUTING.md` §*Running the checks*
      says after a refresh; a value the rule leaves where it is needs no commit.
```
```markdown
`seal/releases/0.21.0.md#"### 1791384162-the-macos-test-leg-runs-in-shards">"S3 · each macOS"@29f6eea6`, `.github/workflows/test.yml#"pytest:"@2ce0f2a3`, `tests/test_a_slow_case_names_itself.py#test_every_pytest_leg_has_a_timeout_and_the_job_reads_it@e49de6ba`
```

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

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| The refresh recipe merges into the old file and keeps 625 entries nobody collects | `overview.md` §*Not done*, a candidate issue | the orchestrator, who files it |
| A `workflow_dispatch` input that measures without a commit | `spec.md` Out and `plan.md` Alternatives E | the orchestrator, who files it |
