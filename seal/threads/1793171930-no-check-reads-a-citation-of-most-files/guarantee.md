# Guarantee: 1793171930-no-check-reads-a-citation-of-most-files

| Field | Value |
|---|---|
| Target SHA | 27dbc1fc against 5287dd42 |
| Broad gate | 731df38a against 5287dd42 |

The base `release/v0.24.0` resolved through `release/v0.24.0@{upstream}` to `5287dd42` (executed). `trail/gate.md` names `731df38a`, an ancestor of HEAD, and the one commit after it, `27dbc1fc`, changes only `seal/threads/1793171930-no-check-reads-a-citation-of-most-files/trail/gate.md` (executed, `git log --no-merges --name-only 731df38a..HEAD ^5287dd42`). `seal pr-body seal/threads/1793171930-no-check-reads-a-citation-of-most-files --body <the body file> --check` exited 0 and printed that the part above `## Not from the records` is the records' text (executed). The claims below were re-run in a clone of the branch at `27dbc1fc` in the sealer's scratch directory, through `bin/test` and the clone's `.venv`; each file changed for a run was restored with `git checkout HEAD --` before the next, and the clone was removed afterwards.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| S1 went red before the corrections, naming exactly the three coordinates | `trail/phases/phase-1.md`, *The red runs* | in the clone, `.github/scripts/gather_changelog.py`, `skills/verify/scripts/mutation_check.py` and `tests/behaviour/test_one_word_one_meaning.py` restored from `5287dd42`, then `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py::test_every_cited_section_stands_in_its_file -q -p no:xdist` | holds: exit 1, 1 failed, naming `.github/scripts/gather_changelog.py:43`, `skills/verify/scripts/mutation_check.py:103` and `tests/behaviour/test_one_word_one_meaning.py:461` and nothing else (executed) |
| The case fails on a heading renamed in a scratch copy | the issue's *Done when*, second bullet | in the clone, the lead at `docs/the-record-layout.md:140` edited from *Whether a line is live* to *Whether a line counts*, then the same S1 run | holds: exit 1, naming `.github/scripts/gather_changelog.py:43` and `skills/verify/scripts/unverified_check.py:261`, both citations of that lead (executed) |
| S9's excusing cases went red against a reader that excused nothing | `trail/phases/phase-2.md`, *S9's red run* | in the clone, `excuser` made to return `None` before its loop, then `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -p no:xdist` (run together with the next row's revert) | holds: all four `test_a_pending_correction_excuses_a_policy_citation_and_warns` variants failed on `assert not [(..., 9, 'manual/b.md', '*Old name*')]`; the ten refusing variants passed (executed) |
| S5 failed `assert 9 == 10` before the `skill's` reader change | `trail/rounds/round-1.md` finding 2, *answer* | the same run, with `or m.group(2)` removed from `cited_in`'s filter | holds: `test_each_spelling_of_a_citation_is_read` failed `AssertionError: assert 9 == 10`; 5 failed, 20 passed in all (executed) |
| The pin module failed on the extended `check:` line, and passes with the fix | `trail/rounds/round-1.md` finding 1, *answer* | in the clone, `tests/text/test_a_language_section_of_writing_style_opens_alone.py` restored from `5287dd42`, then `bin/test` on it alone | holds: exit 1, `test_the_rules_for_text_an_agent_or_a_check_reads_reach_both_languages` failed; at HEAD it passes in the next row (executed) |
| The changed modules pass at HEAD | `trail/phases/phase-1.md`, `trail/phases/phase-2.md`, `trail/rounds/round-2.md` probes | `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_a_language_section_of_writing_style_opens_alone.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py -q` at `27dbc1fc` | holds: exit 0, 52 passed (executed) |
| S1 reads well over its floor of 100 and finds nothing dangling at the merge with the base | `frame/design.md` S1; `frame/questions.md` Q2 | `.venv/bin/python -c` importing the module and calling `citations('.')` in the clone at `27dbc1fc` | holds: 371 read, 0 dangling, 0 excused; phase 1's 372 at `577daff6` was not re-run (executed) |
| Q1: the S9 warning prints in `bin/test -q`'s output under xdist | `frame/questions.md` Q1 Status; `trail/phases/phase-2.md` *Q1, measured* | one probe `tests/behaviour/test_tmp_sealer_q1.py` in the clone, calling `assert_resolved` on the S9 fixture with nothing capturing, run once under `bin/test ... -q` (xdist nodes started), then deleted | holds: exit 0, `1 passed, 1 warning`, the `UserWarning` naming `docs/a.md:9`, `manual/b.md` *Old name* and `seal/threads/1-x/` (executed) |
| S10: every `check:` line holds, the writing-style one naming the new module | `trail/phases/phase-2.md` *S10* | `bin/seal rules --check` in the clone | holds: exit 0, all 266 check lines in 55 rule files hold (executed) |
| The three corrected citations name sections that stand | `frame/design.md` *Scope* item 2; `changelog.md` *Fixed* | `grep -n` over `docs/the-record-layout.md` and `agents/crafter.md`; `git show f6ae6db6:docs/the-broad-gate.md` line 117; `git merge-base --is-ancestor f6ae6db6 HEAD` | holds: the lead at `docs/the-record-layout.md:140`, *Commit before you mutate* at `agents/crafter.md:101`, `## Where the stamp is drawn` at line 117, ancestor exit 0 (executed) |
| Every `## Removes` row stands nowhere in the tree | `frame/design.md` *Removes*, all six rows; `changelog.md` | `git grep -nE` for `SKILL_NAMED`, `CITED_TITLE`, `NOT_CITATIONS`, `implement_headings`, `dangling_implement_citations`, `cited_files`, `MISSING_STEP` and both removed case names over the tree outside `seal/threads`, `seal/process`, `changelog` and `CHANGELOG.md`, `.test_durations` included; read the imports at `tests/behaviour/test_the_set_a_work_item_always_has.py:30-32` | holds: grep exit 1, no match; the module imports `re` and `read` alone (executed, read) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | one case in `tests/behaviour/test_a_cited_section_stands_in_its_file.py` resolves every section citation outside the records against headings and bold rule leads and replaces the `implement`-only case; three dangling citations are corrected; a policy-root citation a pending `## Rule changes` item corrects warns and passes; writing-style names the bold lead and the new module | the issue's *Done when*; the diff `5287dd42...27dbc1fc`; the S1 red and rename runs; the Removes search | none; its five departures are rows of `gaps.md` *Where spec and implementation diverged*, read against the module |
| the build | phase 1 at `577daff6` built S1 to S8 and corrected the three citations; phase 2 at `aafe184b` built S9 and S10 and measured Q1 as (a); the round-1 fixes at `5a590a2c` | the re-run S1 red, S9 red, S5 red and pin red; the module runs; the Q1 probe | none |
| the last round | round 2: both round-1 findings are fixed at `5a590a2c`, and nothing is open | the S5 `9 == 10` and pin-module re-runs; the module run at HEAD | none |
| the changelog | the suite reads every file's section citations, case-sensitively, with the prefix rule and the policy-root warning; writing-style names the bold lead; three citations are corrected | `resolves`, `cited_in`, `excuser` and `assert_resolved` in the module (read); the three targets; the diff of `skills/writing-style/SKILL.md` | none |
| the orchestrator's part of the pull request body | `Closes #1043`, nothing else | the issue's two *Done when* bullets, each re-run above; the records part, which `seal pr-body --check` matched | none |

Not re-run, with who answers each:

- The full suite, the repository-wide lint and the typecheck. `trail/gate.md` records the orchestrator's run at `731df38a`, and the sealer read it and did not run it (unverified by the sealer; the orchestrator answers through that run).
- The mutation counts, 29 mutants in phase 1 and 14 in S9 (unverified; the crafter's records are the only account, and no party owes a re-run).
- Whether S9's warning stands in the output `seal gate` keeps under `--keep-output`, the third *Not verified* row of `gaps.md`. At `27dbc1fc` no citation is excused, so the gate's run raised no such warning to keep (unverified; the orchestrator answers at a later `seal gate`).
- `frame/questions.md` Q2 for #1053, which has not landed in `release/v0.24.0` (`git log c825fd2c..5287dd42`, executed). #1040 has landed, and S1 meets it clean at the merge (executed above) (unverified for #1053; the orchestrator answers when #1053's branch meets this case).

Verdict: sealed
