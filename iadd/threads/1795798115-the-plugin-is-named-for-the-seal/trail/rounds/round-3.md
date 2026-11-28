# Review round 3: 1795798115-the-plugin-is-named-for-the-seal

```iadd
target: 0509790d, fixes 060ac283..0509790d
```

The round is the verifying round over the fix pass of round 2. Its code target is `git diff 060ac283..0509790d`, and `git log --oneline 060ac283..0509790d` names its four commits: `8a136af2`, the round 2 record, `55435dfb`, the row of `frame/plan.md` *Judgments of the run* that routes round 2's regression to an ordinary fix pass, `e6359a4d`, the fix, which changes `skills/settle/SKILL.md` lines 233 to 236 and nothing else, and `0509790d`, the close block of round 2's finding. The round read that diff whole. It read the work item's `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md` whole at `0509790d`, and searched the phase records for each sentence on the trailer of a settle's commit. No `pr.<lang>.md` stands, `iadd/parity.json` is absent, so no parity comparison is owed, and `iadd/threads/` holds no other work item, so no other frame is read.

The round ran in the checkout the spawn prompt named, with branch `chore/1651-the-plugin-becomes-iadd` at `0509790d`, and changed nothing there except this record.

Carried from round 2, not re-established: the coordinate of its finding, `skills/settle/SKILL.md` step 5, and the commands on its `evidence:` line, which this round ran again at the target. Every verdict below is this round's own.

The close's sample of the other lines that state a settle commit's trailer names three lines from its `git grep -n -i 'no work item'`, and calls them the whole list. The same command at `0509790d` also prints the docstring at `tests/text/test_the_direct_answer_owes_the_inspectors_record.py:66-69`, which says a settle's commit carries the `IADD-Routing: no work item` trailer. That docstring describes the release checklist's step from this release on, as the three named lines do, so its sense is right and nothing in the tree follows. A case's docstring is read by whoever next edits the case and by no party at a step, so no finding is opened for it.

The fixed sentence holds three commas, which `skills/writing-style/SKILL.md` *English prose rules*, *Short sentences over connector chains*, would split. Its reading is one: *that one* can only be the release the sentence before it names, the one that renamed the plugin IADD, and *is not one* keeps the base's sense, a route. A sentence that only reads badly is no finding (`skills/code-review/SKILL.md` *The record*).

No case reads the old spelling in step 5: `git grep -n 'Seal-Routing' -- tests evals` exits 1. The frame proves the rename by search A4 and adds no check (`frame/design.md` *User scenarios & acceptance*, row *The old root, command, trailer and fence are gone*, and *Removes*, its last paragraph), and `gaps.md` *Not done* names phase 7's reasons. A4 at the target prints the two lines of step 5 that name `Seal-Routing:` and the eight `.specseal/` lines, as that row asks. So the missing pin is the frame's decision and no finding.

## Findings

None. The round opens no finding.

## Confirmations

```iadd
confirms: round-2#1
```
What holds: step 5 of `skills/settle/SKILL.md` *The settling session's procedure* now leaves the settle commits of both spellings out of the routes. Lines 233 to 236 read *A settle's commit carries `IADD-Routing: no work item`, or `Seal-Routing: no work item` in a release before that one, with no route chosen, and is not one.* *That one* resolves to the release named at lines 231 to 232, the one that renamed the plugin IADD, so the boundary is the one `frame/design.md` *Scope*, *Out of scope*, *Committed trailers*, gives: `Seal-Routing:` is the form of commits before the release that carries this work. The 11 settle commits `git log --grep='Seal-Routing: no work item' origin/release/v0.40.0` lists, `235d41ff` among them, are commits of releases up to `v0.39.4`, which the sentence now covers; `git tag --contains 235d41ff` prints `v0.39.4` and `git merge-base --is-ancestor 235d41ff v0.39.3` exits 1, executed. The base `origin/release/v0.40.0` is `35bef264`, the commit `v0.39.4` names, so at the base no commit of the release that carries this work lies outside this branch, and no settle commit of that release falls between the two spellings, executed with `git rev-parse`. The backticked `IADD-Routing: no work item` that `tests/text/test_settle_reads_before_it_removes.py#test_the_skill_names_how_a_settle_commits` reads stands whole on line 234, and the test reads the skill through `tests/conftest.py#flattened` in any case. Executed: `bin/test tests/text/test_settle_reads_before_it_removes.py tests/behaviour/test_docs_line_wrap.py -q` passed 65, and lines 233 to 236 measure 71, 73, 71 and 7 columns. Executed: `git grep -n -F 'no route chosen' -- . ':!iadd/threads'` prints only `skills/settle/SKILL.md:235`, as the close says.

What matched: the row `55435dfb` adds to `frame/plan.md` *Judgments of the run* (`frame/plan.md:85`) routes round 2's regression to an ordinary fix pass, on the grounds that the fix applied round 1's paste-ready fix as given and the frame already names `Seal-Routing:` for the commits before this release. That is the second row of the table under `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame*, *a review record's paste-ready fix applied as given*, and the third row does not apply, since no earlier regression of this unit was routed in this run. `658d6777` applied round 1's snippet word for word, and `frame/design.md:58` names the old spelling, read. Both cited sections stand: `docs/running/the-run.md` *The run* at line 6 and the orchestration heading at line 263, and `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q` passed 64, executed.

What matched: the fix leaves no sentence of the work item's records false. `changelog.md` line 5 says the settle reads `Seal-Routing:` as the trailer of the commits of releases before the one that renamed the plugin, and `frame/design.md:58` and its acceptance row for search A4 say the same of step 5, read. `trail/phases/phase-7.md:55` says the sentence on the settle's own commits says `IADD-Routing: no work item`, which it still does beside the old spelling; that record states what phase 7 did, read. `pr.md` quotes the third and second rows of 2026-11-28 in *Judgments of the run*, and the new row is the fourth, so both quotes still point at the rows they name, read.

What matched: the close's account of the other lines that state a settle commit's trailer. `skills/settle/SKILL.md:460-461`, `docs/checks/the-fold.md:74` and `docs/releasing/release-checklist.md:71` each say what a settle's commits carry from this release on, and none reads the commits of an earlier release, read. The close names `skills/settle/SKILL.md:460`, where that sentence opens; the trailer itself stands on line 461.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite, the lint and the format check over the branch, under contract rule 2 | the `Broad gate` key of `iadd/config.json` | the orchestrator, at the broad run |
| The units outside the fix diff, which earlier rounds reviewed and this round's bound leaves out | the range `origin/release/v0.40.0..060ac283` | no one this round; rounds 1 and 2 read them |
| Whether `TRADEMARKS.md` should reserve the name IADD, which `frame/questions.md` Q1 holds open | `TRADEMARKS.md` | the repository owner |

## Probes

| Command | Result |
|---|---|
| `git log --format='%h %s' --grep='Seal-Routing: no work item' origin/release/v0.40.0` | 23 commits, 11 of them titled `chore: settle` |
| `git log -1 --format=%B 235d41ff`, `git tag --contains 235d41ff`, `git merge-base --is-ancestor 235d41ff v0.39.3` | the body holds `Seal-Routing: no work item` as a trailer; `v0.39.4`; exit 1 |
| `git rev-parse --short origin/release/v0.40.0` and `git rev-parse --short 'v0.39.4^{commit}'` | `35bef264` both |
| `git grep -n -F 'no route chosen' -- . ':!iadd/threads'` | `skills/settle/SKILL.md:235` |
| `git grep -n -i 'no work item' -- . ':!iadd/threads' ':!docs/experiments' ':!evals/behaviour'` | among its lines, `skills/settle/SKILL.md:234` and `:461`, `docs/checks/the-fold.md:74`, `docs/releasing/release-checklist.md:71` and `tests/text/test_the_direct_answer_owes_the_inspectors_record.py:69` |
| search A4 of `frame/design.md` *The searches* | the two `Seal-Routing` lines of `skills/settle/SKILL.md`, 232 and 234, and the eight `.specseal/` lines |
| `git grep -n 'Seal-Routing' -- tests evals` | exit 1 |
| `bin/test tests/text/test_settle_reads_before_it_removes.py tests/behaviour/test_docs_line_wrap.py -q` | 65 passed |
| `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q` | 64 passed, 1 warning |
