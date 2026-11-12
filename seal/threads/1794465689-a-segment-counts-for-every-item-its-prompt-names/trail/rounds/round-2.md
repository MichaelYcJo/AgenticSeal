# Review round 2: 1794465689-a-segment-counts-for-every-item-its-prompt-names

```seal
target: 181d2ad55, fixes 2f9d102fb..181d2ad55
```

This is the verifying round over round 1's fixes. The code read is the fix diff `2f9d102fb..181d2ad55`: the framer's fold at `0c7d94ed0`, the fixes at `58fbabd7e` and `5a69812a9`, the `gaps.md` row at `163ef9fc3` and the three close blocks at `181d2ad55`. The work item's records were read against the target. `frame/design.md`, `frame/plan.md`, `gaps.md` and `changelog.md` were read through the fix diff, on top of round 1's whole read. `routing.md`, `frame/questions.md`, `pr.md` and `trail/phases/phase-1.md` are unchanged since `7510173d9`, which round 1 read whole (executed, `git diff --stat 7510173d9..181d2ad55` on them prints nothing). The first quote of `pr.md` still stands word for word at `frame/plan.md:40` (executed, `grep -c -F`, 1 match), and the second at the title row, unchanged. Carried from round 1, not re-established: the coordinates of `branch_declarations`, `other_work_items` and `report_work_item`, and round 1's verdict that the six phase-1 cases were seen red. The seen-red run below was executed in a `git clone --no-local` at `181d2ad55` under the round's scratch directory.

The orchestrator asked about two texts, and the round opens no finding on either.

- `frame/design.md:54`: S2's title, "A later run still shows the segment it does not post", says no mode. Its Then cell limits the line to "the read without `--post`", and *Scope* item 2 (`frame/design.md:34`) says "a later run's reading", which a `--post` run with nothing left does not produce. The frame row is read whole, title and Then cell together, by the parties that act on it. The release note and the docstring that round 1's finding 3 corrected are read alone. So the target does not contradict the row. Round 1's paste-ready fix for finding 3 should still have named these two frame lines and said why it left them, as `skills/code-review/SKILL.md` *A paste-ready fix reaches every statement of the fact it repairs* asks. This record says it here.
- `docs/running/measuring-a-run.md:137-150` stands in *Where a reading goes* (`:97`). It states a constraint, that nothing sent may carry repository contents, paths or prompts. It names the transcript file name and the absent command text as how the body meets that constraint. It is not a list of every field. `frame/design.md` G13 judges that another work item's directory name is the same kind of text as the item's own, which the body carried before this work. The operation under `## Rule changes` adds to the same section that the reading names the other work items a segment names. Until the settle, `changelog.md:7` says the document states the old reading. `README.md:399` is where *What runs on your machine* discloses the directories, and it now does.

Three points about the fix diff are no finding. First, *Scope* item 5 (`frame/design.md:37`) says each listed case, S8 among them, was "seen red against `c26981960`". The S8 case was seen red with the env line removed, as the S8 row (`:60`) states. Against `c26981960` the count line it asserts does not exist, so the case would be red there too. Nobody ran it there, and the sentence still holds. Second, on a git too old to know `GIT_NO_LAZY_FETCH`, `seal cost --work-item` in a partial clone still fetches. `changelog.md:4` and `frame/plan.md:40` state this, and `README.md:399` does not. Round 1's finding 1 accepted that residue as the fix's precondition, and this round leaves it there. Third, the `held` check at `tests/skills/test_session_cost.py:5703-5709` sets the variable on its own `cat-file -e`, so the check reads the clone and does not fetch. This was read.

## Findings

### 1. The S8 case goes red on a git that does not know `GIT_NO_LAZY_FETCH`, where the code it tests behaves as documented

```seal
severity: should
location: `tests/skills/test_session_cost.py:5663-5709`, `seal/threads/1794465689-a-segment-counts-for-every-item-its-prompt-names/gaps.md:9`
evidence: read `tests/skills/test_session_cost.py:5663-5709`, `skills/verify/scripts/session_cost.py:3082-3099`, `seal/threads/1794465689-a-segment-counts-for-every-item-its-prompt-names/gaps.md:9`, `seal/threads/1794465689-a-segment-counts-for-every-item-its-prompt-names/frame/design.md:27`, `seal/threads/1794465689-a-segment-counts-for-every-item-its-prompt-names/frame/design.md:60`, `tests/skills/test_settle.py:3489`
regression: round-1#1
```

Why it matters: the unit is `Test_work_item::test_a_partial_clone_fetches_nothing`, which `58fbabd7e` added. It asserts that the page reads no other item and that the blob is still absent afterwards. Both hold only where git knows the variable. The `run_git` docstring (`session_cost.py:3087-3090`), `changelog.md:4` and G19 (`frame/design.md:27`) all say a git too old to know it ignores it and fetches. That is the documented behaviour on that git, and the case turns it red. The gaps row at `gaps.md:9` hands the question to the CI legs, and says the case "goes red" there. The legs are not the only place the suite runs. `CONTRIBUTING.md` has contributors run `bin/test`, and `config.json`'s `Broad gate` runs the whole suite on the orchestrator's machine. `tests/skills/test_settle.py:3489` records a contributor machine running git 2.39.3. This round did not establish which git release added the variable, and did not run an older git. The frame's S8 row (`frame/design.md:60`) asks for a case seen red with the variable removed, and G19 states that an older git fetches. The fix built the case as round 1's finding 1 described it, and that description named no condition for an older git. The defect came from that description.

The case can test the capability exactly, on the clone it has just built, with no version number. With the variable set, `cat-file -e` on the missing blob fails where git knows the variable. It fetches the blob and succeeds where git does not, and then the read under test would fetch too. Insert after `tests/skills/test_session_cost.py:5688`, `git(repo, "branch", "-q", "other", "origin/other")`:

```python
        # A git that does not know the variable fetches the blob here, as the
        # read would; `run_git` says so, and there is nothing left to test.
        known = subprocess.run(
            ["git", "-C", str(repo), "cat-file", "-e", blob],
            capture_output=True,
            env={**os.environ, "GIT_NO_LAZY_FETCH": "1"},
        )
        if known.returncode == 0:
            pytest.skip(
                "this git fetched a blob with GIT_NO_LAZY_FETCH set, so it does "
                "not know the variable, and the branch read fetches there"
            )
```

The fix pass also owes `gaps.md:9`. Its "on an older git the read fetches the blob and the case goes red" becomes "on an older git the case skips, naming the reason". The case's docstring also gains one sentence, that it skips where git does not know the variable. The snippet does not cover either. Contract rule 15 applies to the guard: show the skip taken by running the case with the env line removed from `known` only. The `cat-file -e` then fetches, and the case must report the skip, not a pass or a failure.

## Confirmations

```seal
confirms: round-1#1
```
What holds: `run_git` at `skills/verify/scripts/session_cost.py:3091-3096` runs every git read with `GIT_NO_LAZY_FETCH=1`. Its docstring, `changelog.md:4`, and `frame/plan.md:9`, `:11` and `:40` say the read fetches nothing, and that an older git does (read). The S8 case is red with the env line removed. In the scratch clone it failed on its count line, which read `1 also naming another work item, with 1 other work item read beside it` (executed). The module passes at the target (executed). The close's claim that `seal mutate` was run with only the env line deleted was not re-run. The run above reproduces its result by hand. The framer's fold at `0c7d94ed0` brings G19, S8, *Scope* items 1 and 5, D1 item 2 and the plan in line with the code (read). Finding 1 above is about the S8 case alone, so this close holds for the code and the texts.

```seal
confirms: round-1#2
```
What holds: `README.md:399` and `README.ko.md:395` carry the two sentences round 1 gave, word for word, at the anchors it named (read, `git diff --word-diff`). The two editions' modules `tests/behaviour/test_both_editions_carry_the_same_folds.py` and `tests/behaviour/test_docs_line_wrap.py` pass (executed). The sentence `5a69812a9` adds to `changelog.md:4` says what the two rows now say, and it is true at the target (read).

```seal
confirms: round-1#3
```
What holds: `changelog.md:3` and the `report_work_item` docstring at `session_cost.py:3303-3308` carry round 1's text word for word (read). The `--post` return at `work_item`, which comes before `other_work_items`, is unchanged, so both now describe it (read).

What matched: the `gaps.md` row `163ef9fc3` added names an answerer that exists, the `test` workflow. Finding 1 asks the fix pass to change what that row says the case does on an older git.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at the work item's HEAD; this round ran two narrow sets and labels the suite `unverified` | `seal/config.json` `Broad gate` | the orchestrator, by `seal gate --record` |
| The S8 case on each CI leg's git | `seal/threads/1794465689-a-segment-counts-for-every-item-its-prompt-names/gaps.md:9` | the `test` workflow at the pull request |
| Which git release added `GIT_NO_LAZY_FETCH` | `skills/verify/scripts/session_cost.py:3082-3090` | nobody needs to, once finding 1's skip tests for the capability instead of a version |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_session_cost.py -q`, in the branch worktree at `181d2ad55` | exit 0, 276 passed |
| `bin/test tests/behaviour/test_both_editions_carry_the_same_folds.py tests/behaviour/test_docs_line_wrap.py -q`, in the branch worktree at `181d2ad55` | exit 0, 58 passed |
| `bin/test tests/skills/test_session_cost.py -q -p no:xdist -k test_a_partial_clone_fetches_nothing`, in a `git clone --no-local` at `181d2ad55` with the `env=` line of `run_git` removed | exit 1; the case failed on its count line, the page reading `1 also naming another work item, with 1 other work item read beside it` and `agent-a.jsonl also names 1790000001-another-item` |
