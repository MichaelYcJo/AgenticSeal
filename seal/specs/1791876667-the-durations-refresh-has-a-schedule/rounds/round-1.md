# 1791876667-the-durations-refresh-has-a-schedule — review round 1

| Field | Value |
|---|---|
| Target SHA | c98576a7841100a432aee5486969a9ca0a255ee0 |
| Written late | no |
| Ran by | warden on Opus 5.5 |
| PR | 937 |
| Broad gate | not yet |
| Fixes checked by | round-2 |
| Fix range | `b16bee7f3e0d3a3627d8da009da8bca5f3e592a0..524c9783b69f673dd624c14525a47dcec7202739`, 7 commits |
| Contract changes | none |
| New units | runs_pytest (depth 1); shallow_pytest_jobs (depth 1); SHALLOW_RUNNERS (depth 1); test_a_job_that_calls_pytest_any_way_is_held_to_the_whole_history (depth 1); test_a_count_below_one_is_exit_2_naming_it (depth 1) |
| Fix of a fix | no |
| Needs a fix | yes — 1 (parts expire before a partial re-run reads them), 2 (the remedy has no path for a branch with no run), 3 (the shallow-checkout guard narrowed), 4 (`--count 0` crashes) |
| Loses a record or crashes | yes — 4: `durations_union.py --count 0` raises `ZeroDivisionError` and exits 1, an argument the workflow does not pass |
<!-- New units: .github/workflows/test.yml read by the diff-line heuristic and not by the AST -->

- [x] Pass

## What this round was asked

Round 1 of #931 against c98576a7 on base origin/release/v0.22.0: spec compliance first, then quality, over the whole diff. Judge the implementer's seven recorded divergences from the frame, check the class of a new script or job breaking a census no slice ran, and confirm no new workflow step needs a write scope or prompts a person.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | the shards' parts expire after one day, so re-running failed jobs in a later attempt leaves the `durations` job one part short and red | `.github/workflows/test.yml:175` | **fixed** `ef894749` | fixed at ef894749 — both uploads `retention-days: 7` and `overwrite: true`; T3 and T10 assert both, seen red first (`'1' == '7'`, `None == 'true'`); read: re-run failed jobs also re-runs the jobs that `need` them; the comment at lines 166–167 assumes the parts are only read in the first attempt |
| 🟡 2 | the remedy names "this branch's latest `tests` run", which a branch with no pull request does not have, and the recipe case forbids the dispatch that would make one | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:272` | **fixed** `6787cd3e` | fixed at 6787cd3e — `REMEDY` and `CONTRIBUTING.md`'s recipe give `gh workflow run test.yml --ref <branch>` for a branch with no run or one too old to re-run; T11's `gone` list no longer forbids the dispatch; both cases seen red first; read: `test.yml` `on:` and its comment at lines 15–18; the `gone` tuple of `test_the_recipe_names_the_artifact_and_the_checklist_has_no_box`; `CONTRIBUTING.md:210-215` |
| 🟡 3 | `RUNS_PYTEST` drops `uvx … pytest`, `uv run pytest`, env-prefixed and `cd … &&` invocations, which the old text match held to `fetch-depth: 0` | `tests/test_ci_gives_the_checks_what_they_need.py:325` | **fixed** `a4e67849` | fixed at a4e67849 — 24eda548 — `RUNS_PYTEST` matches pytest as a word on every code line but `needs:`; a fixture case per spelling (`uvx --with pytest pytest`, `uv run pytest`, `PYTHONPATH=x pytest`, `cd sub && pytest`, plain, `python -m`) beside a `needs: pytest` job, the four named spellings seen red first; executed: the regex evaluated against nine lines; four that run pytest are unselected |
| 🟡 4 | `--count 0` reaches `report`'s division by `len(merged)` and exits 1 with a traceback, not 2 | `.github/scripts/durations_union.py:153` | **fixed** `91e383a8` | fixed at 91e383a8 — `--count` below one is a `Refusal`, exit 2, before anything is read; cases for 0 and -1 seen red first (`ZeroDivisionError`); executed: the script run with `--count 0` over an empty parts directory, exit 1, `ZeroDivisionError` |
| 🟢 | divergence 1, the names T2, T8 and T9 kept, with bodies rewritten | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` | confirmed | read: the bodies assert what S1 and S4 say; released rows cite the names |
| 🟢 | divergences 3 and 4, the extra refusals, the two values, both directions under one share, `-D <dir>` | `.github/scripts/durations_union.py`, `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#staleness` | confirmed | read: each refusal is under "never a smaller file"; spec In 3 names the file's seconds as the denominator |
| 🟢 | divergences 5 and 6, the box removed, six jobs, the six survivors | `CONTRIBUTING.md:169`, `seal/specs/1791876667-the-durations-refresh-has-a-schedule/survivors.md` | confirmed | read: six jobs counted against `test.yml` and `hygiene.yml`; the five frames are shipped history |
| 🟢 | nothing in the new workflow needs a write scope or prompts a person | `.github/workflows/test.yml:186-207` | confirmed | read: same-run download and upload need only the default token; no `permissions:`, no input, no checklist box |
| 🟢 | the census modules a slice might not run stay green: interpreter floor, encoding, one word one meaning, no real identifiers, the workflow reader, the slow-case budget and the reader registry's neighbours | `tests/` | confirmed | executed: eleven modules, 428 passed, 7 skipped, exit 0 |
| ❓ | whether `upload-artifact@v4` refuses a name a previous attempt of the same run already uploaded, for a shard's part and for `test-durations` after `gh run rerun` | `.github/workflows/test.yml:168-175`, `.github/workflows/test.yml:201-207` | ❓ out of verified scope | the action's README says only that a duplicate name fails without `overwrite`, and is silent on attempts; the orchestrator answers it with one `gh run rerun --failed` on PR #937 |

## Paste-ready fixes

```yaml
      # A shard's part, uploaded whether its cases passed or failed: a red
      # case still has a price. Only where `store` is set, because anywhere
      # else `.test_durations` is the committed file, and a part holding the
      # whole suite would read to the union as every id in two parts. The
      # name starts with a dot, which the action skips by default. A part is
      # kept as long as the union it makes: re-running failed jobs re-runs
      # the `durations` job too, which reads every part again, and the
      # re-run shard's part replaces the one its first attempt uploaded.
      - if: always() && matrix.store != ''
        uses: actions/upload-artifact@v4
        with:
          name: test-durations-${{ strategy.job-index }}
          path: .test_durations
          include-hidden-files: true
          if-no-files-found: error
          overwrite: true
          retention-days: 7
```
```yaml
      - uses: actions/upload-artifact@v4
        with:
          name: test-durations
          path: union/.test_durations
          include-hidden-files: true
          if-no-files-found: error
          overwrite: true
          retention-days: 7
```
```python
    assert fields.get("retention-days") == "7", fields
    assert fields.get("overwrite") == "true", fields
```
```python
REMEDY = (
    "Refresh it from this branch's latest `tests` run, whose `durations` job "
    "unioned the Windows shards' parts: `gh run download <run id> -n "
    "test-durations -D <dir>`, then move <dir>/.test_durations over the "
    "committed .test_durations and commit it; its line ends are already LF. "
    "A run older than the artifact's seven days is re-run first, with "
    "`gh run rerun <run id>`; a branch with no pull request, or whose run "
    "is too old to re-run, gets one with `gh workflow run test.yml --ref "
    "<branch>` (CONTRIBUTING.md §Running the checks)."
)
```
```markdown
`gh` will not write over a file that is already there. A run older than
seven days is re-run first, with `gh run rerun <run id>`. A branch with no
pull request has no `tests` run until one is dispatched, and neither has a
branch whose run is too old to re-run:
`gh workflow run test.yml --ref <branch>` starts one.
```
```python
        "`gh run rerun <run id>`",
        "`gh workflow run test.yml --ref <branch>`",
        "`durations` job",
        "`STALE_SHARE`",
        "entries the suite no longer collects",
    ):
        assert said in flat, f"the recipe paragraph does not say {said}"
    for gone in ("restore the shards", "one job again"):
        assert gone not in flat, f"the recipe paragraph still says {gone!r}"
```
```python
    assert "gh workflow run test.yml --ref <branch>" in sentence
```
```python
# A job runs pytest where a line of its code names it as a command word:
# `run: pytest …`, `uvx --with pytest pytest`, `python -m pytest`, a line of
# a `run: |` block. `needs: pytest` names the job of that name and runs
# nothing (#931's `durations` job, which reads no SHA), so a `needs:` line
# and a comment are not read.
RUNS_PYTEST = re.compile(r"(?<![\w.-])pytest(?:\s|$)")


def runs_pytest(block):
    """Whether a line of `block`'s code, not its `needs:` or a comment,
    names pytest as a word."""
    return any(
        RUNS_PYTEST.search(line)
        for line in block.splitlines()
        if not re.match(r"^\s*(?:needs:|#)", line)
    )
```
```python
            if not runs_pytest(block):
                continue
```
```python
    try:
        if args.count < 1:
            raise Refusal(
                f"--count is {args.count}: a union of no parts is no suite"
            )
        found = find_parts(args.parts)
```
```python
        pytest.param(
            {}, 0, "--count is 0: a union of no parts is no suite", id="no-count"
        ),
```

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` over `tests/test_a_script_says_which_interpreter_it_needs.py`, `tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py`, `tests/test_one_word_one_meaning.py`, `tests/test_no_real_identifiers.py`, `tests/test_a_workflow_is_read_the_one_way.py`, `tests/test_a_slow_case_names_itself.py`, `tests/test_a_script_copied_alone_exits_2.py`, `tests/test_a_document_that_names_a_script_says_how_to_reach_it.py`, `tests/test_a_format_has_one_reader.py`, `tests/test_console_is_not_utf8.py`, `tests/test_what_the_reader_understands.py`, at c98576a7 in the review clone | 428 passed, 7 skipped, exit 0 read directly |
| `RUNS_PYTEST`'s pattern, copied verbatim, against nine workflow lines with `python3 -c` | selected: `run: pytest`, `run: python -m pytest`, a bare `pytest` line inside a block; unselected: `uvx --with pytest pytest`, `uv run pytest`, `PYTHONPATH=x pytest`, `cd sub && pytest`, `needs: pytest`, `pip install pytest` |
| `python3 .github/scripts/durations_union.py --parts <empty dir> --count 0 --committed .test_durations --out <dir>/.test_durations` | exit 1, `ZeroDivisionError: division by zero`; the scratch directory removed afterwards |
| the full suite, lint and typecheck at c98576a7 | not yet: the sealer's, after the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| `seal/budgets.md`'s `## Price level` row (about 1071 for this union) and any sentence in `REMEDY` or the recipe naming it | `overview.md` §*Not done*, first bullet | the session that rebases this branch onto #930 (PR #938) |
| `CONTRIBUTING.md`'s "CI runs six jobs" sentence, which PR #938 also edits | `overview.md` §*Where spec and implementation diverged*, the job-count row | the session that rebases this branch onto #930 (PR #938) |
