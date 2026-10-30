# Review round 5: 1793273065-the-core-reaches-no-users-repository

target: a63a9b4a, fixes f54724e3..a63a9b4a

## Findings

This round opens no finding.

## Confirmations

confirms: none
The commit is the artifact and nothing else. `git show a63a9b4a
--name-status` names one path, `.test_durations`, and `git diff --name-only
ab614222 a63a9b4a` adds only `round-4.md` beside it (executed, *Probes*).
This round downloaded the `test-durations` artifact of `gh run` 40895243786
into a directory of its own. It compared the file byte for byte with `git
show a63a9b4a:.test_durations`, and `cmp` exits 0 (executed, *Probes*). The
file holds no carriage return, so its line ends are LF as the recipe in
`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:271-281`
says. The run is the branch's own. `gh run view` gives head SHA `ab614222`,
branch `feat/1177-the-core-reaches-no-users-repository`, workflow `tests`,
and a `durations` job that succeeded (executed, *Probes*). Between
`ab614222` and HEAD nothing under `tests/` changed, so the run measured the
collection HEAD holds. The commit follows the procedure the failing case's
sentence prints (`REMEDY`, read at `:271-281`) and `CONTRIBUTING.md`
*Running the checks* names.

confirms: none
The file prices every case the suite collects at HEAD, under the pytest CI
installs. The CI legs install pytest 9.2.0, read from each leg's `pip
install` line in `gh run view 40895243786 --log` (executed, *Probes*).
Under pytest 9.2.0, `--collect-only` over `tests` at HEAD collects 6146
ids. The file holds 6146 entries. No collected id is unpriced and no entry
is gone (executed, *Probes*). The count also shows that all four Windows
shards' parts reached the union. Windows group 1 failed, and a missing part
would have left about a quarter of the ids unpriced. Before the commit, the
file held 6010 entries. The new one adds 314 and drops 178. The 314 equals
the count every failing leg printed, "314 of the 6146 collected cases
(5.1%)" (executed, *Probes*). The orchestrator claimed 5.1% to 5.2%. The log
of run 40895243786 says 5.1%, and round 4 reported 5.2% for the broad run
at `526504cd`. Both fit the claim.

confirms: none
The case that judges the file passes over the whole collection at HEAD.
`bin/test tests -q -k test_the_durations_file_prices_the_suite` exits 0
with 1 passed (executed, *Probes*). This is the command the case's own skip
message names (`:347-351`, read). The orchestrator's evidence for the fix
was different. It claimed "that module passes locally: 15 passed, 2
skipped". This round re-ran that command with `-rs`. Of the two skips, one
is `test_the_durations_file_prices_the_suite` itself, at `:347`, "the suite
was not collected". The other is `test_no_collected_id_carries_the_interpreters_path`,
at `:487` (executed, *Probes*). The module run alone does not read the file
against the suite. The whole-collection run above does.

confirms: none
The orchestrator claimed that "every leg of that CI run failed only
`test_the_durations_file_prices_the_suite`". `gh run view 40895243786` shows
something narrower. Ubuntu, Windows group 1 and macOS group 1 failed, each
with "1 failed" and this case as the only `FAILED` line. Windows groups 2
to 4 and macOS group 3 succeeded, since the case runs in one shard of each
sharded leg. macOS group 2 was cancelled and reported no result (executed,
*Probes*). The difference changes nothing this round judges. The repair is
the same file whichever shard holds the case.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `a63a9b4a`. The prompt names them unverified, and contract rule 2 keeps them from this round | the tree | the orchestrator, through `seal gate` |
| The local virtual environment that `bin/test` uses holds pytest 9.1.1, and CI installs 9.2.0. Under 9.1.1, a `--collect-only` at HEAD spells 12 ids of `tests/skills/test_chain_check.py` and `tests/skills/test_pr_body.py` differently: parameter strings with newlines become escaped values, where 9.2.0 writes the argument name and index, such as `old9`. Locally, then, 12 of 6146 cases (0.2%) read as unpriced, and 12 entries worth 0.39 s read as gone. Both are far inside `STALE_SHARE`, so the case passes. The module docstring says every leg collects the same ids, which holds between CI legs on one pytest version and not across versions. This is outside the fix diff and is not a defect of the commit | `.github/scripts/run_tests.py`, `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:9-12` | the orchestrator |
| Whether the shards balance once the refreshed file is in place. The file bounds age, not imbalance (`:87-89`, read), and only a CI run on `a63a9b4a` shows the legs' times | the next `tests` run | the orchestrator |
| Carried from round 4 and not re-examined: the `report:` lines of `bin/seal layout --check tests`, the pull request body's measured core bytes, and round 1's carried rows | `seal/threads/1793273065-the-core-reaches-no-users-repository/trail/rounds/round-4.md` | as round 4 names each |

## Probes

| Command | Result |
|---|---|
| `git show a63a9b4a --name-status`; `git diff --name-only ab614222 a63a9b4a` | `M .test_durations`; `.test_durations` and `trail/rounds/round-4.md`, nothing under `tests/` |
| `gh run view 40895243786 --json headSha,headBranch,event,workflowName,conclusion,jobs` | head `ab614222`, branch `feat/1177-the-core-reaches-no-users-repository`, `tests`, `workflow_dispatch`; `durations` success; ubuntu, Windows group 1, macOS group 1 failure; macOS group 2 cancelled; the rest success |
| `gh run download 40895243786 -n test-durations -D <scratch dir>` then `cmp` against `git show a63a9b4a:.test_durations`; `grep -c` for a carriage return | exit 0, 895911 bytes; `cmp` exit 0; 0 carriage returns |
| `gh run view 40895243786 --log-failed`, the `FAILED` and summary lines | ubuntu "1 failed, 6135 passed, 10 skipped"; Windows group 1 "1 failed, 2770 passed, 24 skipped"; macOS group 1 "1 failed, 3028 passed, 7 skipped"; each `FAILED` line is `test_the_durations_file_prices_the_suite` at "314 of the 6146 collected cases (5.1%)" |
| `gh run view 40895243786 --log`, the `pip install` lines | every pytest leg installs `pytest-9.2.0`, `pytest-split-0.11.0`, `pytest-xdist-3.8.0` |
| `uv venv` in the round's scratch directory with `pytest==9.2.0`, `pytest-xdist==3.8.0`, `pytest-split==0.11.0`, `markdown-it-py==4.2.0`, `cmarkgfm==2025.10.22`; `python -m pytest tests -q -p no:xdist -p no:cacheprovider --collect-only` at HEAD; `python3 -I` reading the ids against the file | 6146 collected, 6146 unique, 6146 entries; 0 unpriced, 0 gone. The environment and the scratch files were removed afterwards |
| `bin/test tests -q -p no:xdist --collect-only` at HEAD (pytest 9.1.1), read the same way | 6146 collected; 12 unpriced, 12 gone (0.39 s of 1174.5 s), all parametrized ids whose strings hold a newline |
| `python3 -I` comparing the keys of `git show f54724e3:.test_durations` with the new file | 6010 entries before; 314 added, 178 removed |
| `bin/test tests -q -k test_the_durations_file_prices_the_suite` | exit 0, 1 passed |
| `bin/test tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py -q -rs -p no:xdist` | 15 passed, 2 skipped: `:347` (the suite case) and `:487`, each "the suite was not collected" |
