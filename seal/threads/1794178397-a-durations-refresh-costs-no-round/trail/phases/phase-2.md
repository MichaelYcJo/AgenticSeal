# Phase 2: 1794178397-a-durations-refresh-costs-no-round

## What this phase found

**The frame holds for this phase.** Every coordinate the phase 2 row
stands on was where the frame and `trail/phases/phase-1.md` say at
`dd20fbc8`. These are `CONTRIBUTING.md:162-191`,
`.github/workflows/test.yml:186-194`, the union step and its upload, the
comment at `tests/conftest.py:852-857`, and the behaviour module's docstring
paragraph at `:37-46`. Everything *Removes* rows 1 to 4 name stood in
`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`
(read). `seal layout --pairs` named no pair in that module after the phase
(executed).

**`frame/questions.md` Q2: a switch on the union step.** The choice was
judged against `frame/design.md` *Data & interfaces*. That section proposes
the switch and leaves the choice to the phase.

- The union step's line now ends with
  `${{ github.base_ref == 'main' && '--stale-fails' || '' }}`. On a pull
  request into `main` the expression gives `--stale-fails`. On every other
  run it gives nothing, because `github.base_ref` is empty outside a pull
  request and names another branch on one. That is the condition
  `release-report` already uses (design *Grounding* G11).
- The upload's condition is
  `${{ !cancelled() && hashFiles('union/.test_durations') != '' }}`. The
  upload runs wherever the union file exists, not where the step passed.
  So the red verdict (exit 1), which writes the union first, still uploads
  it. A refusal (exit 2) writes nothing, so nothing is uploaded and the
  upload step adds no second red. This is the "runs whenever the union was
  written" the design asks for, read from the file itself and not from an
  exit code that both 1 and 2 turn into `failure`.
- A separate last step was rejected. It would run the script a second time
  over the same parts, and its report would land in the job summary twice.
  Keeping the sentence out of the summary would have meant clearing
  `GITHUB_STEP_SUMMARY`, and the design asks for the sentence there.
- `test_the_durations_job_needs_pytest_and_runs_unless_cancelled` reads the
  union step's words in pairs. It now strips the trailing expression
  (`ASK_THE_VERDICT`) before pairing. Without the strip the case would still
  pass, but its option map would hold the expression's words as junk keys.

**Seen red (executed).** Both cases the plan row names were written first
and run against the tree at `dd20fbc8`, before the workflow and
`CONTRIBUTING.md` changed.

- `test_the_verdict_is_asked_into_main_alone_and_the_upload_outlives_it`
  (scenario S4) failed on `assert run.endswith(" " + ASK_THE_VERDICT)`,
  because the old union line asked no verdict.
- `test_the_recipe_names_the_artifact_and_the_checklist_has_no_box`
  (scenario S5, rewritten) failed on its first pinned phrase,
  "A work item never commits `.test_durations`".

**Mutation (executed).** Each run was one `seal mutate` command with
`-p no:xdist`. The workflow mutants ran over
`-k "verdict_is_asked or needs_pytest"`, unless a line says otherwise. The
`CONTRIBUTING.md` mutants ran over `-k recipe_names`.

- Red on `test.yml`:
  - `==` turned into `!=` in the expression;
  - the expression replaced by a bare `--stale-fails`;
  - the upload's condition cut to `${{ !cancelled() }}`;
  - the upload's `if:` line deleted;
  - `hashFiles` pointed at another path;
  - a second `--stale-fails` before `--committed`, run over
    `-k verdict_is_asked` alone, so the red is the count guard's.
- Red on `CONTRIBUTING.md`, one mutant per sentence:
  - the "never commits" sentence turned into "may commit";
  - the condition "on a pull request into `main`, and on no other run"
    turned into "on every run";
  - the trailer deleted;
  - the branch cut from `release/vX.Y.Z` deleted;
  - the pull request into `release/vX.Y.Z` deleted;
  - the limit's "newest run whose `durations` job wrote the union" deleted;
  - "commits it alone" cut to "commits it";
  - `gh run rerun` added back;
  - `bin/test tests -q -k` added back.
- One survived. Replacing "entries no shard ran" at its second place in the
  paragraph leaves the same words at the first place, where the paragraph
  describes the summary's two shares. The case pins the phrase and does not
  pin where it stands. The sentence that carries the verdict still names
  `STALE_SHARE` and the seconds side, and the "on every run" mutant shows
  that sentence is watched.

**The removals.** Every unit *Removes* rows 1 to 4 name left the behaviour
module: the suite case, `unpriced`, `dead`, `staleness`, `REMEDY`,
`STALE_SHARE`, `_collection`, `FIXTURE_SIZE`, `AT_THE_SHARE`, `_with_gone`
and the seven fixture cases. Each fixture case's rewrite in
`tests/github/test_durations_union.py` is listed in `trail/phases/phase-1.md`.
Removing these units adds no behaviour, so no mutant ran over them.
`collects_the_suite`, `test_only_the_suite_or_the_repository_is_the_whole_collection`
and `test_no_collected_id_carries_the_interpreters_path` stay, as *Scope*
item 1 says. The docstring paragraph (*Removes* row 7) and the conftest
comment (row 8) were rewritten in place. The conftest section heading,
"the durations file prices the suite", named the removed case's purpose.
It now reads "the whole collection, recorded".

**The census the plan row asks for (executed).**
`git grep -n 'prices_the_suite\|STALE_SHARE' -- ':!seal/threads'` lists
the script, its cases and `CONTRIBUTING.md`, as the row expects. It also
lists four hits the row did not foresee, each judged to stand:

- the `durations` job's comment in `test.yml`, which states the new verdict
  and names the constant it reads;
- the behaviour module's rewritten docstring paragraph (*Removes* row 7),
  which names the script's `STALE_SHARE` as what the release pull
  request's job reads;
- the S5 case's pin of `` `STALE_SHARE` `` in the paragraph, which the old S5
  case also held;
- `.test_durations:1234`, the removed case's entry. No work item commits
  that file any more, so the entry stays until the release refresh drops
  it. It holds 0.016 s, a dead entry far inside the share.

`git grep -n 'durations' -- docs skills agents` lists two lines. Both are
about the duration of an agent's run (`docs/running/measuring-a-run.md:24`,
`skills/verify/scripts/session_cost.py:2181`), and this work made neither
false. Design scenario S1's check, `git grep -n 'prices_the_suite' -- tests`,
prints nothing (executed). To keep it that way, the S5 case's list of
words that must be gone pins `bin/test tests -q -k`, the old paragraph's
command, and not the removed case's name (commit `608f2df7`).

**`CONTRIBUTING.md` beyond the paragraph.** The jobs list in *Running the
checks* said only that `durations` "unions what the Windows shards
measured". A work item that reads the list would not learn that the job now
fails the release pull request, so the entry now adds that it fails a pull
request into `main` where the committed file is stale. The first sentence
of the paragraph now says the file goes stale as cases are added, renamed
or removed, because design *Grounding* G9 found that renames and removals
caused the crossings. The paragraph's text follows *Scope* items 4 and 5 and
the limit sentence as the design states them. `test_docs_line_wrap` caught
one line past 88 columns in the phase boundary run, and `a1c2879b` rewraps
it.

**The phase boundary set (executed).** One `bin/test` command ran every
module under `tests/` that names `CONTRIBUTING`, `test.yml` or the
workflows directory: 45 modules, the plan row's three among them. It passed
at `608f2df7` with 1,935 passed and 9 skipped. `tests/conftest.py` changed
only in a comment, and every module imports it. The lint and the format
check over the changed Python files passed (executed). The workflow parses
as YAML, and the parsed union line and upload condition are the ones above
(executed, through PyYAML). No `actionlint` is installed here, and no run
evaluated either expression on GitHub (`gaps.md`).
