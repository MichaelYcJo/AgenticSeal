# Review round 1: 1793853200-the-roll-docstring-describes-the-guard

```seal
target: 14f09766f against release/v0.32.4
```

The range is c9f08a03 (routing), a1f3145b (frame), 669d5958 (the orchestrator's fold moving the version into scope), 93063507 (the docstrings), d21323cc (the phase record, `gaps.md`, the fragment and the version), 9da16281 (the plan's Status cell) and 14f09766 (the orchestrator's fold putting the plan's technical context in the past tense). There are no earlier rounds, so no fact is carried; every fact below was established this round. `seal/parity.md` is not declared, so no parity comparison is owed.

The axes walked: the two lookups' retry on an empty reading and their refusal to retry two or more (inputs and error paths); the exclusion of the issue `main` just closed (exclusions and boundaries); the close-then-open order (state transitions); what a search-index lag changes between a write and a read (concurrency). This change's own axes are prose against code, a rule stated once against stated twice, history clauses in a docstring, and the version move. No code line changed (the S3 probe below), so the quality stage has no behaviour to judge beyond the module still importing and its cases passing.

## Findings

None. No sentence the diff wrote contradicts the code or another sentence, and every claim of the build that was checked held.

One wording observation is not a finding, because it misstates nothing. In the lag paragraph, `.github/scripts/roll_flow_measurement_issue.py:77-81` runs two sentences opening with "so": "the race is unlikely to reach `main`'s lookup in practice. So a zero reading ... gets one retry". The retry's reason is the sentence at `:70-72`, that a lag behind an add gives a reading short a result, and the second "So" now reads as following from the race being unlikely. The old text joined them with "-- but", and the reason can still be recovered two sentences up.

## Confirmations

What matched: D1 item 1, the lag paragraph at `.github/scripts/roll_flow_measurement_issue.py:68-85`. It states that `gh issue list` reads a lagging search index. A lag behind a create or a label added gives a reading short a result, and a lag behind a close gives one with an extra issue. That second direction is the one `landed_create` at `:465` guards by excluding `closed_number`. The paragraph keeps the decision the code holds: `open_flow_measurement_issues` at `:329-333` sleeps `RETRY_DELAY_SECONDS` and reads again only when the first reading is empty, and `main` at `:510-517` exits on any count other than one. The grounds for not retrying two or more are the invariant paragraph at `:62-66` and the undercount #109 measured, in one sentence naming #109; "Phase 1 of this work item" is gone from this paragraph (read).

What matched: D1 item 2, the guard paragraph at `:116-123`. It names `landed_create`'s lookup and says the ladder ends where that lookup finds the create landed, which is `open_issue` at `:487-493` returning on `landed_create(...)` true. It does not restate the condition. A word diff of 93063507 against the base shows no word changed in it beyond "a failure" becoming "a failed create" and the clause D1 replaces; the rest is reflow (executed: `git diff --word-diff=plain release/v0.32.4 93063507 -- .github/scripts/roll_flow_measurement_issue.py`).

What matched: D1 item 3, the transaction paragraph at `:139-145`. "the exact reading `main` fails on without a retry" names two open issues, and `main` at `:511` exits on two with no retry, since `open_flow_measurement_issues` retries only an empty reading (read).

What matched: D1 items 4 and 5. `open_flow_measurement_issues`'s docstring at `:322-328` cites the module docstring for the lag's direction and states its own decision, which matches `:329-333`. `landed_create`'s docstring at `:454-461` keeps its condition and cites "the module docstring's rule for a lag behind a close" instead of restating it. Its last sentence on the retry after a lag behind the create matches the loop at `:462-468` (read). The lag rule is now stated once, at `:69-73`, which is S2's requirement.

What matched: D1 item 6. The docstring of `test_refuses_two_open_issues_loudly_without_retrying` at `tests/github/test_roll_flow_measurement_issue.py:256-257` states what the case asserts at `:276-281`: the exit names "found 2", one lookup, and no sleep (read). The diff adds no test, so no case is owed a reading against its group.

What matched: the class account. The frame claims the script was read whole and its list of five sentences is closed (`frame/design.md` *Grounding*, the class row). This round read the script whole at HEAD and found no other sentence stating or leaning on the absolute; `:149`, "the open-issue count was not exactly 1 (after the retry)", predates the work and does not state a lag's direction. The phase record calls its tree-wide list a sample by wording, and it is one. A whole-word search for `lag`, `lags`, `lagged` and `lagging` outside `seal/threads/` (executed, itself a sample over spellings) also lists `tests/github/test_roll_flow_measurement_issue.py:65`, `:176`, `:442`, `:464` and `:484`, which the phase's sample did not name. Each states a lag behind a close or behind a write that adds, in the direction the new rule gives, so none of them is an instance. `hooks/version-check.py:38` is about release lag, a different subject.

What matched: the crafter's S1 claim. The S1 `git grep` over HEAD's script and test module exits 1 (executed).

What matched: the crafter's S3 claim. It said the docstring-stripped `ast.dump` of each file is equal at 31558c76 and 93063507 and that the comparison can fail. This round's own probe strips module, class and function docstrings: 14 from the script and 40 from the test module at each commit, as claimed. Both files are equal between 31558c76 and HEAD 14f09766, so no later commit changed code either. The same probe prints DIFFER for the script between `ea220c9c^` and 31558c76 (executed; *Probes*).

What matched: the crafter's S4 and lint claims. The two roll modules end 40 passed, and `ruff check` and `ruff format --check` on the two touched files exit 0 at HEAD (executed).

What matched: *Scope* item 5. `.claude-plugin/plugin.json:4` reads `0.32.4`, moved in d21323cc, the commit that adds `changelog.md`, as `docs/releasing/branch-and-release.md` *Cutting a release* places it. `git grep -n "0\.32\.[34]"` outside `seal/threads/` lists that line alone (executed).

What matched: S5. `changelog.md` names the two mutation cases #146 asked for as not carried by the 0.32.4 milestone, and the ledger rows as gone with `seal/ledger/`. Its other sentences match the diff: three sentences of the script and one test docstring changed, and no code line (read, against `gh issue view 146` and the milestone 88 description, both executed). The milestone carries "#146's two docstrings ... (its request for mutation pins is not carried)", which is the frame's scope.

What matched: the honesty of the `unverified` label. `gaps.md` *Not verified* names the full suite, the lint and the format check at HEAD as unverified, including the modules that read `.claude-plugin/plugin.json` and the records under `seal/threads/`, and it names the orchestrator's broad run as their answerer. The phase record's count of twenty-one such modules is right (executed: `git grep -l plugin.json -- tests | wc -l`).

What matched: the two folds. 669d5958 moved the version into *Scope* and removed the out-of-scope bullet that said the opposite, so no stale sentence remains. 14f09766 put the plan's description of the absolute in the past tense, dated to c9f08a03, so `frame/plan.md` *Technical context* no longer contradicts HEAD (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD, among them the twenty-one modules under `tests/` that read `.claude-plugin/plugin.json` and the modules that read the work item's records | the `Broad gate` row of `seal/config.md` | the orchestrator's broad run, then the sealer |
| Whether the release's own close step (`close_issues_on_release.py`) could close a `flow-measurement` issue before `main`'s lookup, so that a lag behind that close reaches `main` as two open issues. That needs a pull request whose closing keyword names the open log, a shape outside the normal flow, and the docstring's claim that the race is unlikely concerns the label write alone | `.github/workflows/close-issues-on-release.yml:40`, `.github/scripts/roll_flow_measurement_issue.py:77-80` | the owner, should such a pull request ever be written |

## Probes

| Command | Result |
|---|---|
| `git grep -n -i -E "only ever undercount\|can only undercount\|never one with an extra\|never what a .*lag produces\|never a lag artifact\|no longer empty" HEAD -- .github/scripts/roll_flow_measurement_issue.py tests/github/test_roll_flow_measurement_issue.py` | exit 1, nothing printed |
| `python3 -I test_tmp_docstring_only.py <worktree> 31558c76 14f09766`, a scratch file under the round's scratch directory that strips docstrings with `ast` and compares `ast.dump` from `git show` | script: 14 and 14 removed, EQUAL; test module: 40 and 40 removed, EQUAL; exit 0 |
| the same probe, `ea220c9c^` against 31558c76 | script DIFFER, test module EQUAL, exit 1: the comparison can fail on a code change. The file and its directories were removed after this run |
| `bin/test tests/github/test_roll_flow_measurement_issue.py tests/behaviour/test_a_release_rolls_the_flow_measurement_issue.py -q` | 40 passed, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` on the script and the test module | both exit 0 |
| `git grep -n -i -w -E "lag\|lags\|lagged\|lagging" -- . ':!seal/threads' ':!.test_durations'` | the script's new lines, five test-module lines that agree with the rule, and `hooks/version-check.py:38` on another subject |
| `python3 skills/code-review/scripts/chain_check.py --baseline release/v0.32.4 --root <worktree> --worktree` | exit 0. With this record in place it lists only the gate record and the guarantee, both owed later by the orchestrator and the sealer; no notice named a test pin or a copy in `frame/design.md` |
