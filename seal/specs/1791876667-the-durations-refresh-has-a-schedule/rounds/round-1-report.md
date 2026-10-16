# Round 1 report — 1791876667-the-durations-refresh-has-a-schedule (#931)

Reviewed by warden (Opus 5.5) on 2026-10-14, at c98576a7 against
`origin/release/v0.22.0` (a8d83663), in a `git clone --no-local` of the
branch at that SHA. This is the first round: there is no earlier
`round-N.md` to inherit, so every verdict below is this round's own.

## How the four findings relate

The mechanism works on the path it was built for. A run with four Windows
shards uploads four parts, the union is the collection, and the staleness
case reads it. Each finding is a path next to that one where the mechanism
stops working or a guard got weaker.

1. A run that is re-run in part, more than a day later, cannot rebuild its
   union (finding 1).
2. A branch with no usable run gets a remedy it cannot follow (finding 2).
3. To make room for the new job, the shallow-checkout guard was narrowed
   beyond what that job needed (finding 3).
4. The union script crashes on one argument value instead of refusing it
   (finding 4).

## Stage 1 — spec compliance

`read`: S1–S7 are each met by the code at c98576a7. The Windows entries
carry `store`, the pytest line ends with the split and then the store, the
upload step has `always() && matrix.store != ''` and `include-hidden-files`,
the `durations` job has `needs: pytest` and `if: ${{ !cancelled() }}`, the
script refuses rather than writing a smaller file, `staleness` gates in both
directions under one `STALE_SHARE`, `REMEDY` names the download, and the
checklist box is gone. The `## Removes` rows are read gone from the
diff. The implementer's two CI claims, that runs 38475370013 and
38477758775 produced the parts and the union and that `gh run download`
refuses to overwrite, are the implementer's `executed` claims. I did not
re-run either, and nothing below depends on them.

The divergences the orchestrator named, judged one by one:

- **1, names kept.** Sound. A released row cites each kept name, and a
  rename would have orphaned it. The bodies now test what the names say.
- **2, `RUNS_PYTEST`.** The `durations` job needed excluding, but the new
  rule excludes more than that job. That is finding 3.
- **3, eight refusals, `if-no-files-found: error`, `timeout-minutes: 5`.**
  Sound. Each refusal falls under the spec's *never a smaller file*. The
  bound is generous for a job measured at 7 s and 11 s. One refusal is
  missing: finding 4.
- **4, both directions, the denominator, `-D <dir>`.** Sound. The spec's
  In 3 says "the committed file's seconds", and dead seconds are part of
  them. The `-D` form follows from the implementer's executed refusal.
- **5, the box and "six jobs".** Sound. I counted the jobs against the
  sentence: lint, the suite, `durations`, arm-check, the ledger, hygiene.
  The textual collision with PR #938 is under Deferred.
- **6, survivors.** Sound. The five frames are shipped history, and the
  frozen 0.21.1 row has its `Corrected ·` row in the fragment.
- **7, price level.** Deferred to the rebase. The overview records it,
  and the branch carries nothing that would contradict it.

## Stage 2 — quality

### 1. A partial re-run more than a day later turns the `durations` job red (🟡, read)

`.github/workflows/test.yml:175` keeps each shard's part for one day. Its
comment, at lines 166–167, gives the reason: "A part is read by the
`durations` job of the same run and by nothing else, so one day is
enough". That holds only for the run's first attempt. GitHub's *Re-run
failed jobs* re-runs the failed jobs and every job that `needs` them, so
the `durations` job runs again in the new attempt. It downloads by
pattern, and three of the four parts are past their day. The script then
finds one part where `--count` says four and exits 2. The cause is one
flaky Windows shard re-run the next morning. The run stays red after the
shard turns green, and the only way out is a full re-run of every leg.

The same re-run also uploads a part under a name the first attempt already
used. Whether `upload-artifact@v4` refuses that inside one run is the ❓
row below. `overwrite: true` makes the answer irrelevant, so the fix
carries it.

This is `read`, from the workflow and GitHub's documented re-run
behaviour, and was not executed on CI. Parts cost cents at seven days,
which is `plan.md` §*Alternatives considered* E's own figure.

### 2. A branch with no usable run gets a remedy it cannot follow (🟡, read)

The remedy has three spellings that agree with each other: `REMEDY` in
`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:272`,
`CONTRIBUTING.md:210-215`, and the changelog. All three begin with "this
branch's latest `tests` run". `test.yml` runs on a pull request, on a push
to `main`, and on dispatch, and its own comment at lines 15–18 says that a
branch whose routing stops before the pull request "runs nothing on push".
On such a branch the sealer's broad run reaches the staleness case
locally, and the sentence it prints names a run that does not exist. The
same is likely for a branch whose last run is older than GitHub's re-run
window, where `gh run rerun` is refused. That window is about 30 days, a
figure I know but did not open a page for.

`test_the_recipe_names_the_artifact_and_the_checklist_has_no_box` makes
the missing command impossible to add: its `gone` tuple refuses
`gh workflow run` in the paragraph. The old paragraph never contained that
phrase, because the dispatch was in the checklist box, so the guard keeps
nothing out and blocks the one command such a branch needs. That command
is a dispatch the session can type itself, so it asks nobody anything,
and S7 still holds.

### 3. The shallow-checkout guard no longer sees `uv run pytest` (🟡, executed)

`tests/test_ci_gives_the_checks_what_they_need.py:325` used to select a
job when its block contained `pytest ` anywhere. It now selects one only
where a line begins with `pytest`, `run: pytest` or `python -m pytest`.
That correctly drops `needs: pytest`, which is what the `durations` job
required. It also drops every other shape that runs pytest. Evaluated
directly against the regex, these come back unselected:
`run: uvx --with pytest pytest tests/`, `run: uv run pytest`,
`run: PYTHONPATH=x pytest tests/` and `run: cd sub && pytest`. The first
is the form `CONTRIBUTING.md:165` gives contributors, in a repository
whose `CLAUDE.md` says "prefer uv".

No current job uses any of those forms, so nothing escapes today. But a
future job written that way runs pytest at depth 1, and
`test_every_job_that_runs_pytest_has_the_whole_history` passes it. That
case's own message names exactly this failure: refs come back MISSING, and
cases skip instead of failing. The narrower fix is to exclude the `needs:`
line and keep the old reach.

### 4. `durations_union.py --count 0` crashes instead of refusing (🟡, executed)

The docstring of `.github/scripts/durations_union.py` says "Exit codes: 0
wrote the union; 2 refused and wrote nothing". With `--count 0` and an
empty parts directory, `find_parts` returns no parts, which matches the
count. `union` returns `{}`, and `report` divides by `len(merged)` at
line 153: `ZeroDivisionError`, a traceback, and exit 1. A negative count
passes `type=int` too.

The workflow passes `--count 4`, and
`test_the_durations_job_needs_pytest_and_runs_unless_cancelled` pins it to
the entries that store. So this is reachable only by an argument the job
does not pass. It still breaks the exit contract the script states.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | the shards' parts expire after one day, so re-running failed jobs in a later attempt leaves the `durations` job one part short and red | `.github/workflows/test.yml:175` | open | read: re-run failed jobs also re-runs the jobs that `need` them; the comment at lines 166–167 assumes the parts are only read in the first attempt |
| 🟡 2 | the remedy names "this branch's latest `tests` run", which a branch with no pull request does not have, and the recipe case forbids the dispatch that would make one | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:272` | open | read: `test.yml` `on:` and its comment at lines 15–18; the `gone` tuple of `test_the_recipe_names_the_artifact_and_the_checklist_has_no_box`; `CONTRIBUTING.md:210-215` |
| 🟡 3 | `RUNS_PYTEST` drops `uvx … pytest`, `uv run pytest`, env-prefixed and `cd … &&` invocations, which the old text match held to `fetch-depth: 0` | `tests/test_ci_gives_the_checks_what_they_need.py:325` | open | executed: the regex evaluated against nine lines; four that run pytest are unselected |
| 🟡 4 | `--count 0` reaches `report`'s division by `len(merged)` and exits 1 with a traceback, not 2 | `.github/scripts/durations_union.py:153` | open | executed: the script run with `--count 0` over an empty parts directory, exit 1, `ZeroDivisionError` |
| 🟢 | divergence 1, the names T2, T8 and T9 kept, with bodies rewritten | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` | confirmed | read: the bodies assert what S1 and S4 say; released rows cite the names |
| 🟢 | divergences 3 and 4, the extra refusals, the two values, both directions under one share, `-D <dir>` | `.github/scripts/durations_union.py`, `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#staleness` | confirmed | read: each refusal is under "never a smaller file"; spec In 3 names the file's seconds as the denominator |
| 🟢 | divergences 5 and 6, the box removed, six jobs, the six survivors | `CONTRIBUTING.md:169`, `seal/specs/1791876667-the-durations-refresh-has-a-schedule/survivors.md` | confirmed | read: six jobs counted against `test.yml` and `hygiene.yml`; the five frames are shipped history |
| 🟢 | nothing in the new workflow needs a write scope or prompts a person | `.github/workflows/test.yml:186-207` | confirmed | read: same-run download and upload need only the default token; no `permissions:`, no input, no checklist box |
| 🟢 | the census modules a slice might not run stay green: interpreter floor, encoding, one word one meaning, no real identifiers, the workflow reader, the slow-case budget and the reader registry's neighbours | `tests/` | confirmed | executed: eleven modules, 428 passed, 7 skipped, exit 0 |
| ❓ | whether `upload-artifact@v4` refuses a name a previous attempt of the same run already uploaded, for a shard's part and for `test-durations` after `gh run rerun` | `.github/workflows/test.yml:168-175`, `.github/workflows/test.yml:201-207` | ❓ out of verified scope | the action's README says only that a duplicate name fails without `overwrite`, and is silent on attempts; the orchestrator answers it with one `gh run rerun --failed` on PR #937 |

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` over `tests/test_a_script_says_which_interpreter_it_needs.py`, `tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py`, `tests/test_one_word_one_meaning.py`, `tests/test_no_real_identifiers.py`, `tests/test_a_workflow_is_read_the_one_way.py`, `tests/test_a_slow_case_names_itself.py`, `tests/test_a_script_copied_alone_exits_2.py`, `tests/test_a_document_that_names_a_script_says_how_to_reach_it.py`, `tests/test_a_format_has_one_reader.py`, `tests/test_console_is_not_utf8.py`, `tests/test_what_the_reader_understands.py`, at c98576a7 in the review clone | 428 passed, 7 skipped, exit 0 read directly |
| `RUNS_PYTEST`'s pattern, copied verbatim, against nine workflow lines with `python3 -c` | selected: `run: pytest`, `run: python -m pytest`, a bare `pytest` line inside a block; unselected: `uvx --with pytest pytest`, `uv run pytest`, `PYTHONPATH=x pytest`, `cd sub && pytest`, `needs: pytest`, `pip install pytest` |
| `python3 .github/scripts/durations_union.py --parts <empty dir> --count 0 --committed .test_durations --out <dir>/.test_durations` | exit 1, `ZeroDivisionError: division by zero`; the scratch directory removed afterwards |
| the full suite, lint and typecheck at c98576a7 | not yet: the sealer's, after the rounds settle |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| `seal/budgets.md`'s `## Price level` row (about 1071 for this union) and any sentence in `REMEDY` or the recipe naming it | `overview.md` §*Not done*, first bullet | the session that rebases this branch onto #930 (PR #938) |
| `CONTRIBUTING.md`'s "CI runs six jobs" sentence, which PR #938 also edits | `overview.md` §*Where spec and implementation diverged*, the job-count row | the session that rebases this branch onto #930 (PR #938) |

## Regression tests to plant

- `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`,
  `test_the_upload_step_runs_always_and_only_where_store_is_set`: the part
  is kept as long as the union and overwrites (finding 1). This is in the
  fix below.
- The same module, `test_a_missing_part_a_duplicate_id_or_an_unparseable_part_is_exit_2`:
  one more parameter, `--count 0` over an empty parts directory, which must
  be exit 2 (finding 4).
- `tests/test_ci_gives_the_checks_what_they_need.py`: a fixture workflow
  whose job runs `uvx --with pytest pytest` at depth 1, which the shallow
  check must name (finding 3).

## Facts for the evidence ledger

- S1's row says the parts are "kept one day". Finding 1's fix makes that
  seven, and the row's claim moves with it.
- S4's and S6's rows quote the remedy. Finding 2's fix adds the dispatch
  sentence, and S7's *no dispatch* should then read "no dispatch a person
  has to make", because the remedy may name one a session types.

## Paste-ready fixes

### 1 — keep the part as long as the union, and let a re-run replace it

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

### 2 — the remedy names the dispatch for a branch with no usable run

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

### 3 — exclude the `needs:` line, keep the old reach

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

### 4 — a count below one is a refusal

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

Needs a fix: yes — 1 (parts expire before a partial re-run reads them), 2 (the remedy has no path for a branch with no run), 3 (the shallow-checkout guard narrowed), 4 (`--count 0` crashes)
Loses a record or crashes: yes — 4: `durations_union.py --count 0` raises `ZeroDivisionError` and exits 1, an argument the workflow does not pass

The broad gate has not come due: this round leaves four findings open.

## Proof

Files opened in the review clone at c98576a7:
`seal/specs/1791876667-the-durations-refresh-has-a-schedule/spec.md`,
`plan.md`, `overview.md`, `questions.md`, `survivors.md`, `handoff.md`,
`changelog.md`, `phases/phase-2.md` (lines 1–80);
`seal/ledger/1791876667-the-durations-refresh-has-a-schedule.md` (first 40
lines); `.github/workflows/test.yml` (whole);
`.github/scripts/durations_union.py` (whole); the diff of
`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`,
`tests/test_ci_gives_the_checks_what_they_need.py` (lines 300–360 and the
diff), `CONTRIBUTING.md` (lines 160–235) and `docs/release-checklist.md`
(lines 40–60 and the diff); the `pytest` lines of every workflow under
`.github/workflows/`; `.gitattributes`. Not opened: `phases/phase-1.md`,
`phases/phase-3.md`, `routing.md`, the released ledger files the
corrections cite.
