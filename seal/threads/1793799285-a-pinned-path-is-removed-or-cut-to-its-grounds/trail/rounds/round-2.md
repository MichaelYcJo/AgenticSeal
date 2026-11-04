# Review round 2: 1793799285-a-pinned-path-is-removed-or-cut-to-its-grounds

```seal
target: a4d76c990, fixes 570fe4cf6..a4d76c990
```

This verifying round reviewed the diff `570fe4cf6..a4d76c990` of issue #1355's branch, in a `git clone --no-local` of the repository checked out at `a4d76c990`. The diff holds four commits. `a43c13166` and `d15fad64a` are the fix pass's two fixes, `7044b2639` appends round 1's close blocks, and `a4d76c990` is the orchestrator's fold of `frame/design.md` D1 rows 1 and 2, the `## Removes` row on `.github/workflows/test.yml`, and a `## Judgments of the run` row in `frame/plan.md`. Outside `seal/`, the diff changes 17 comment lines in `.github/workflows/test.yml` and two comment lines in `tests/behaviour/test_first_setup_asks_once.py`. No code path, case or fixture changes, so the code axes have nothing to judge, as in round 1. This round's own axes are three. The first is whether the arithmetic the comment now states is the removed records' arithmetic and reproduces their figures. The second is whether the rewritten comment and `gaps.md` *Not done* say what the module and the touched files hold. The third is whether each record the fix pass and the fold changed agrees with HEAD.

Carried from round 1, and not re-established: the paths of the two removed records on round-1#1's evidence line, and round 1's reading of each of the 17 touched files whole for sentences that leaned on their file's removed citation, which found line 28 of `tests/behaviour/test_first_setup_asks_once.py` and the "the frame" leftovers alone. Every verdict below is this round's own.

## Findings

None. This round opens no finding.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the shard arithmetic now stands in the comment at `.github/workflows/test.yml:81-92`, and it is the removed records' arithmetic. The fix pass claimed that the record divides 1,949 s, the time after the first case, and that it counts the 25 s before that case in the 62 s fixed cost. `git show 62161701:seal/specs/1791270165-the-windows-test-leg-is-measured-and-cut/phases/phase-3.md`, section *`K`, from the durations file*, does exactly that. Its table row for three shards reads "37 + 25 + 1,949 / 3 = 712 s, 11.9 min", and its row for four reads "549 s, 9.2 min". The 1.08 factor is the ratio of the two runs' pytest times in the same record's run table, 2,132.60 s over 1,973.63 s. The comment's "three gives 11.9 and 12.8 minutes, four 9.2 and 9.8" are the record's four figures. The comment's "37 s of checkout and install, and 25 s from the step's start to the first case" are the record's 37 s and "about 25 s more". The macOS sentence's "fixed cost of about 45 s" is the sum of the "about 25 s outside pytest" and "about 20 s of start-up inside it" that `git show 67694cba:seal/specs/1791384162-the-macos-test-leg-runs-in-shards/plan.md`, paragraph *The arithmetic, in #841's form*, gives. On the comment's own figures, 45 + 1,185 / 3 x 1.45 is 618 s, about 10.3 minutes, and two shards give 904 s, about 15.1 minutes. So "Three is the smallest macOS count the same arithmetic puts under 12 minutes" reproduces, and "the same arithmetic" now points at the Windows sentence above it. The person round-1#1 worried about, who would conclude that three Windows shards are enough, now meets the 12.8 minutes that rule three out. The diff to the file adds and removes only comment lines (executed, in Probes). The other statements of the fact the finding listed agree with HEAD: `trail/phases/phase-1.md` rows 1 and 2 and its Q1 bullet on rows 1 and 2, and `frame/design.md` D1 rows 1 and 2 and its `## Removes` row on the workflow (read). The changelog fragment's "the grounds now stand in the sentence" is now true of rows 1 and 2 (read).

One figure does not reproduce from the comment alone, and it is no finding. With the comment's rounded factor, 62 + 1,949 x 1.08 / 3 gives 764 s, 12.7 minutes. The record's 765 s and 12.8 minutes come from the slower run's own 2,132.60 s less the 25 s. Either value is above 12 minutes, so the count the comment justifies does not change, and the comment quotes the record's figure.

```seal
confirms: round-1#2
```
What holds: the comment at `tests/behaviour/test_first_setup_asks_once.py:28-29` reads "The sentence a session reads, which the Q1 cases below hold in each place". It no longer points at the `questions.md` of a work item the module does not name. "The Q1 cases below" are the cases under the heading `# --- Q1: the sentence a session reads, once in each place` at line 287, and `SESSION_RULE` is what they assert at lines 303, 312 and 325 (read). The fix pass claimed those lines, and they hold. The module's docstring calls a number like Q1 the cases' own (line 4, "Each case states the clause it holds and names it by its number"), so the label reads without the past record. `gaps.md` *Not done* now names the class by its cause, a sentence in a touched file that leaned on its file's removed citation for its referent, and it gives the renaming reason for the case name alone, as round 1 asked. Its seven leftovers stand where it puts them (read): `tests/block_shapes.py:298`, and in `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py` the section comments at lines 35 and 335, the comment at line 472, the case name at line 52, that case's docstring at line 53, and the docstring at line 598. Each module's title line names #667. `gaps.md` calls its list a sample built from a word search. The class is closed, 17 files each readable whole, so the label understates the list rather than misstates it. Round 1's whole-file reading, carried above, found no instance beyond these. This round's wider word search over the 17 files found none either (executed, in Probes). It printed 51 lines. Six are on `gaps.md`'s list. The seventh, the case name, holds none of the words searched. Each of the other 45 was read, and none leans on a removed citation. Most use "the table", "the column" or "the plan" for a table, a column or a template in the case's own data. The rest refer to the module's own work and stood at the base beside text this work did not remove: `tests/behaviour/test_chain_hooks_hardening.py:627-628`, `:795`, `:811` and `:866`, `tests/behaviour/test_the_set_a_work_item_always_has.py:156`, `tests/hooks/test_routing.py:108` and `:521`, `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:95`, `tests/text/test_the_rules_claude_md_names_have_one_home.py:132`, `tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py:252` and `:293`, and `tests/behaviour/test_first_setup_asks_once.py:134` and `:613`. In each of these modules the removed citation named a different record from the one the phrase means. For example, `tests/behaviour/test_chain_hooks_hardening.py:632` cited the overview of work item 1789455558, while line 627's "this work item" is the module's own. The removed overview counts three instances of its shape, so line 628's "the fifth instance" did not rest on it either.

What matched: the orchestrator's fold at `a4d76c990`. `frame/design.md` D1 rows 1 and 2 and the `## Removes` row on `.github/workflows/test.yml` state what the comment now holds, and the `frame/plan.md` row of `## Judgments of the run` names the fold, its grounds and the document it was judged against (read, each against HEAD).

What matched: `trail/rounds/round-1.md`'s two close blocks name the two fix commits, and each of those commits touches a path its finding's `location:` names (read: `git diff --stat` of each commit).

What matched: the narrow runs of the modules that read the changed files pass at the target (executed, in Probes). These are `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, `tests/text/test_ci_gives_the_checks_what_they_need.py`, `tests/behaviour/test_first_setup_asks_once.py`, `tests/test_censuses.py` and `tests/text/test_a_cited_commit_outlives_the_squash.py`. No test reads the comment's text, so none pins the arithmetic (executed: a `git grep` for the comment's figures and phrases outside `seal/` matches only the workflow).

The diff adds no test, so no new test is read against its group.

When the orchestrator's broad gate passes at HEAD, nothing in this round stands in the way of the sealer's spawn.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD. The build labels them `unverified`, and this round did not run them (contract rule 2). The label is honest: `gaps.md` *Not verified* names them and the orchestrator | `seal/threads/1793799285-a-pinned-path-is-removed-or-cut-to-its-grounds/gaps.md` | the orchestrator, at the broad gate |
| Whether a new issue clears the bare commits in shipped text, carried from round 1's row and not re-judged. `7e44106` and `4edc5de6` still stand beside rewritten sentences | `seal/threads/1793799285-a-pinned-path-is-removed-or-cut-to-its-grounds/gaps.md` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `git show 62161701:seal/specs/1791270165-the-windows-test-leg-is-measured-and-cut/phases/phase-3.md` and `git show 67694cba:seal/specs/1791384162-the-macos-test-leg-runs-in-shards/plan.md`, in the clone | both records print. The phase record's `K` table and the plan's macOS arithmetic hold the figures the Confirmations quote |
| `git diff -U0 c8f235df2..a4d76c990 -- .github/workflows/test.yml`, each added or removed line filtered for a first character after the indent other than `#` | no line, `grep` exit 1 |
| `git grep -n -iP` over the 17 touched files for record-pointing words: frame, spec, phase, plan, design, overview, record, table and column after "the"; Q-, D-, O- and S-numbers after "its"; "frame's" and "spec's"; table, column, row, module, spec and frame after "that"; "the work item", "this work" and "this release" | 51 lines, exit 0: six of the seven `gaps.md` lists, and 45 others, each read |
| `git show aa687d35:seal/specs/1789455558-the-record-chain-disagrees-with-itself-in-five-places/overview.md`, searched for its instance count | the overview counts the work item's own subject and two repairs, three instances |
| `git grep -n -E` for `37458654434`, `1,974`, `smallest Windows`, `smallest macOS`, `same arithmetic` and `fixed cost` outside `seal/` | hits in `.github/workflows/test.yml` alone |
| `bin/test tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py tests/text/test_ci_gives_the_checks_what_they_need.py tests/behaviour/test_first_setup_asks_once.py tests/test_censuses.py tests/text/test_a_cited_commit_outlives_the_squash.py -q` | 289 passed, 2 skipped, exit 0 |
