# Guarantee: 1793795355-the-census-reads-every-entry-point

The sealer audited `592936753` against `release/v0.32.0`, resolved as
`release/v0.32.0@{upstream}` to `a9487d83e` (executed: `git rev-parse
--verify --quiet`). Every run took place in a clone of the worktree at
`592936753` and in an at-base clone under the session scratchpad, and both
clones were removed after the runs. No `seal/parity.md` is tracked
(executed: `git ls-files seal/parity.md` printed nothing), so no `original:`
line is owed.

`trail/gate.md`'s newest run is `61db006cf against a9487d83e`. `61db006cf` is
an ancestor of HEAD, and `git log --no-merges --name-only
61db006cf..HEAD ^a9487d83e` lists one commit, `592936753`, which touches
`trail/gate.md` alone, under this work item's directory (executed). The
command `seal pr-body seal/threads/1793795355-the-census-reads-every-entry-point
--body <scratchpad>/1793795355/pr-body.md --check` exited 0: "below `## From
the records` is the records' text" (executed).

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The new `Test_entry_point` cases fail against the census before the change, except the accept case and the `skills/verify/scripts/x.py` arm | `trail/phases/phase-1.md`, *Seen red, each new case* | in the at-base clone, `tests/censuses.py` restored from `a9487d83e`: `bin/test -q -p no:xdist tests/test_censuses.py -k Test_entry_point -rA` | holds (executed): 18 failed and 2 passed, the two the record names. The record's 13 of 15 predates the three target arms and the two shape arms added later; each of those five also failed. Each failure is the old census's: line 1 where the case expects line 2, `[]` for a file outside `hooks/`, the old message, `hooks/two.py:6` read from the second block, and `console_streams` absent |
| M6: `test_reads_the_first_main_block_and_no_later_one`, a case that a block is not read, goes red with its guard alone removed | `trail/phases/phase-1.md`, mutation table row M6 | in the at-base clone with HEAD's `tests/censuses.py`, `entry_point` made to take the last `__main__` block, then `bin/test -q -p no:xdist tests/test_censuses.py -k test_reads_the_first_main_block_and_no_later_one` | holds (executed): 1 failed, `assert ['hooks/two.p...'] == []`, the later block read |
| M2: the accept case's two arms go red when `loop_pairs` returns `None` for a loop of the form | `trail/phases/phase-1.md`, row M2 | the same clone, `return pairs` made `return None`, `-k test_accepts_a_loop_over_the_streams_pairs_as_the_first_statement` | holds (executed): 2 failed, the `hooks/x.py` and `skills/verify/scripts/x.py` arms each refused |
| M3: the drift case goes red when the comparison with `STREAMS` is made `is None` | `trail/phases/phase-1.md`, row M3 | the same clone, `!= streams` made `is None`, `-k test_refuses_a_loop_whose_pairs_are_not_the_streams_pairs_at_its_for_line` | holds (executed): 2 failed, both arms `assert [] == ['skills/x.py...']` |
| The `three-names` arm goes red with the length guard alone removed | `trail/rounds/round-1.md` finding 2's close; `trail/rounds/round-2.md` `confirms: round-1#2` | the same clone, `len(target.elts) == 2` made `>= 2`, `-k three-names` | holds (executed): 1 failed, `ValueError: too many values to unpack (expected 2)` |
| The text pin fails against the old `CONTRIBUTING.md` bullet | `trail/phases/phase-2.md`, *Seen red, the text pin* | the at-base clone, `CONTRIBUTING.md` restored from `a9487d83e`, `bin/test -q -p no:xdist tests/text/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py` | holds (executed): failed at `assert "opens its first such block with the answer" in flat` |
| The exemptions of `broad_gate.py` and `seal_stamp.py` excuse the order alone | `trail/phases/phase-1.md`, *The exemptions … hold only the order* | the at-base clone at HEAD's code, each exemption line deleted, `censuses.entry_point` over both files | holds (executed): `broad_gate.py:3246` names the answer at 3252, `seal_stamp.py:1508` the answer at 1512 |
| The census over the tree prints no `entry_point` line, and the plan's *Verified by* modules pass | `trail/phases/phase-1.md`; `frame/plan.md` *Phases* | in the HEAD clone, `bin/test -q tests/test_censuses.py tests/hooks/test_console.py tests/hooks/test_dispatch.py tests/text/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py` | holds (executed): exit 0, 250 passed |
| Every entry point gives `STREAMS`' answer as its first block's first statement, except `launch.py`, and `broad_gate.py` and `seal_stamp.py` after their exempted statements | `frame/design.md` *User scenarios & acceptance*, last row | a probe written apart from the census: each tracked `.py` parsed, its first `__main__` block's first `console.to_utf8()` or `reconfigure` loop found, each loop run against a stand-in `sys` | holds (executed): 221 tracked `.py`, 48 entry points; 19 open with the call, 26 with a loop giving `STREAMS`' pairs, `broad_gate.py` at index 2, `seal_stamp.py` at index 1, `hooks/lib/launch.py` none. Each of the seven call sites the diff changed binds `console` at module level (executed: `grep`) |
| `git grep -n 'exempt from entry_point'` outside `seal/threads/` and `tests/` lists `launch.py`, `broad_gate.py` and `seal_stamp.py` alone | `frame/design.md` *User scenarios & acceptance*; `trail/phases/phase-1.md`, `phase-2.md` | `git grep -n 'exempt from entry_point' HEAD -- . ':!seal/threads' ':!tests'` | holds (executed): those three lines |
| A call nested under another statement, and a loop over `console.STREAMS`, are refused | `changelog.md`, first bullet | two files planted under a scratch root, `censuses.entry_point` over each | holds (executed): the nested call is refused at the `if` line with the no-answer message, the `console.STREAMS` loop at its `for` line with the loop message |
| Every `## Removes` row and every removal the changelog names stands nowhere in the tree | `frame/design.md` `## Removes`; `changelog.md`, second bullet | `git diff a9487d83e...HEAD` over `tests/censuses.py`, `hooks/`, `CONTRIBUTING.md`, `tests/hooks/test_console.py` and the pin; `git grep` for `opens_with_to_utf8`, `held by test_dispatch`, `test_a_release_script_run_on_its_own`, `Every hook entry point`, `second over \`hooks/\``, `#1255's` and `opens its \`__main__\` with` outside `seal/threads/`; `grep -n to_utf8` in the five scripts | holds (executed): `_python(rel, root)` takes no `under`, the `dispatch.py` exemption, the run-time case, the `tests/x.py` arm, the open question and the `CONTRIBUTING.md` clauses and pin are gone, and each of the five scripts makes one `to_utf8()` call, the first statement of its block. The removed case's name stands only as three keys of `.test_durations:2473-2475`, measurement data that `gaps.md` *Not done* names and leaves to CI's durations job (read) |
| The five scripts moved out of `main()` called `console.to_utf8()` there before the change | `frame/design.md` *Grounding*, the row on the 18 with no answer; `changelog.md`, second bullet | `git show a9487d83e:.github/scripts/<f>.py \| grep -n 'def main\|to_utf8()\|^if __name__'` for the five | holds (executed): each `main()` opens with the call, `finding_counts.py:175`, `plugin_directory_check.py:289`, `publish_release_note.py:845`, `tag_release.py:183`, `tracker_labels.py:159` |
| `tests` run 41841899784 at `ef44cb519` passed every Windows, macOS and Ubuntu leg | the orchestrator's part of the pull request body, *Platforms* | `gh run view 41841899784 --json headSha,conclusion,event,workflowName,jobs` | holds (executed): `workflow_dispatch` at `ef44cb519`, `success`; every `pytest` leg, `lint` and both `arms-grammar` legs `success`, `release-report` skipped |
| The two merges of `release/v0.32.0` carried no conflict resolution | the same part, *Merges* | `git show --cc --format= ef44cb519` and `61db006cf`; `git log -1 --format='%h parents %p'` | holds (executed): neither prints a combined diff; their second parents are `f93d70ea4` (#1254's squash) and `a9487d83e` |
| The changelog fragment holds the fragment's prose and nothing else | `changelog.md` | `git grep -n -e '</content>' -e '</invoke>' HEAD -- seal/`; `git log -S'</invoke>'` over the fragment and `phase-2.md` | does not hold (executed): `changelog.md:6-7` read `</content>` and `</invoke>`, and `trail/phases/phase-2.md:116-117` the same, each since `fb50fbeae`. The pull request body's copy carries them at its lines 33-34 (executed: `grep -n`). `.github/scripts/publish_release_note.py`'s module docstring says the note keeps the fragments beneath, each "its text" (read), so the v0.32.0 release note would print both lines |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | the census reads the first `__main__` block of every tracked `.py`, accepts the call or a literal loop equal to `STREAMS`, refuses at three lines; every entry point gives the answer or carries its reason; `CONTRIBUTING.md` and the console docstring say so; seven `## Removes` rows | the issue body's *What changes* and *Done when*, the build, the tree (the census code at `tests/censuses.py#entry_point`, the probe, the `git grep`s above), the changelog | none. Its line numbers are stated as `215ad6020`'s, and `frame/plan.md` *Judgments of the run* records the folds |
| the build | phase 1 widens the census, adds the cases, repairs 17 entry points and five loops, and moves two exemptions; phase 2 rewrites the bullet, the pin and the console paragraph | the design, the tree, and every claim re-run above but the last | `trail/phases/phase-2.md:116-117` carry `</content>` and `</invoke>` below its last paragraph, text no part of the record states |
| the last round | `trail/rounds/round-2.md` confirms round-1#1 and round-1#2 and opens round-2#1, located in `frame/plan.md` and `changelog.md` alone, closed `fixed 6e22d54f7` | read at HEAD as its reader, since no round read the fix: `frame/plan.md` *Operational impact* states the paste-ready sentence, the fragment's first bullet names the `if` and `for` refusals alone and adds the order refusal's line, and `a483cbb43`, `f4ac057ae` and `6e22d54f7` touch only this work item's directory (executed: `git diff-tree`); the order refusal at `tests/censuses.py#answer_problems` names the answer's line and no form (read) | none |
| the changelog | three bullets: the census widened and its forms and refusals, the seventeen scripts and five loops repaired, and the two prose homes | the design, the build, the tree on every statement checked above, including that five scripts "called `console.to_utf8()` inside `main()`" | its own lines 6-7, `</content>` and `</invoke>`, which are not a fragment's text and which the release note copies |
| the orchestrator's part of the pull request body | the census widens to every tracked `.py` with a `__main__` block and "repairs the seventeen that gave none and the five whose loop left out `stdin`"; Q1's default; the rounds and fixes; the platform run; the merges; the broad run | the issue, `routing.md`, `frame/questions.md` Q1, the round records, `frame/plan.md` *Judgments of the run*, `gh run view 41841899784`, `trail/gate.md` and the gate's printout (`<scratchpad>/1793795355/gate.log:6`, `:13`, `:14`, read) | "the seventeen that gave none": five of the seventeen gave `STREAMS`' answer at the base from `main()`'s first statement (`a9487d83e:.github/scripts/finding_counts.py:175` and the four rows above), as the changelog's second bullet says and as `78fb4d31b` corrected the fragment to say |

```seal
target: 592936753 against a9487d83e
Verdict: withheld reason: (1) the changelog fragment, written at fb50fbeae, ends with the two lines `</content>` and `</invoke>` at seal/threads/1793795355-the-census-reads-every-entry-point/changelog.md:6-7, which the v0.32.0 release note copies as the fragment's text and the pull request body's copy carries at its lines 33-34, and trail/phases/phase-2.md:116-117 carries the same two lines; (2) the orchestrator's part of the pull request body says the build "repairs the seventeen that gave none", and five of the seventeen gave STREAMS' answer from main()'s first statement at the base (a9487d83e:.github/scripts/finding_counts.py:175, plugin_directory_check.py:289, publish_release_note.py:845, tag_release.py:183, tracker_labels.py:159), as the changelog's second bullet says
```

## Re-audit at `a4ad23283`

The sealer audited `a4ad23283` against `release/v0.32.0`, resolved as
`release/v0.32.0@{upstream}` to `a9487d83e` (executed: `git rev-parse
--verify --quiet`). Every run took place in a clone of the worktree at
`a4ad23283` under the session scratchpad, removed after the runs. No
`seal/parity.md` is tracked (executed: `git ls-files seal/parity.md` printed
nothing), so no `original:` line is owed.

`trail/gate.md`'s newest run is still `61db006cf against a9487d83e`.
`61db006cf` is an ancestor of HEAD (executed: `git merge-base
--is-ancestor`), and `git log --no-merges --name-only 61db006cf..HEAD
^a9487d83e` lists `592936753` (`trail/gate.md`), `30c555733`
(`guarantee.md`) and `a4ad23283` (`changelog.md`, `trail/phases/phase-2.md`),
each under this work item's directory alone (executed). The command `bin/seal
pr-body seal/threads/1793795355-the-census-reads-every-entry-point --body <scratchpad>/1793795355/pr-body.md
--check` exited 0: "below `## From the
records` is the records' text" (executed).

Since the earlier block's target `592936753`, `git diff --stat 592936753
HEAD` names `changelog.md` (2 lines removed), `trail/phases/phase-2.md`
(2 lines removed) and `guarantee.md` (the earlier block) and nothing else
(executed), and `git show a4ad23283` removes the lines `</content>` and
`</invoke>` from the end of each of the two records and changes no other
line (executed). The claims whose coordinates that touched are re-run below;
every other row of the earlier tables rests on code, cases and records no
commit since has changed, and stands as it was.

### Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The changelog fragment and the phase 2 record hold their prose and nothing else | `changelog.md`; `trail/phases/phase-2.md`; the orchestrator's statement that `a4ad23283` removes the two lines | `git show a4ad23283`; `git grep -n -e '^</content>$' -e '^</invoke>$' HEAD`; `tail -c` over each file | holds (executed): neither line stands anywhere in the tree at HEAD; the only `</content>` and `</invoke>` text under `seal/` is the earlier block's own quotation in `guarantee.md:38,45,47,52`, which the body's copy and the release note do not carry. The fragment now ends with its third bullet and the phase record with its last paragraph, each closed by one newline |
| The pull request body's copy of the records carries no residue | the body file the prompt names | `grep -n -e '</content>' -e '</invoke>' <scratchpad>/1793795355/pr-body.md` | holds (executed): no line, exit 1 |
| The build repairs seventeen entry points, "twelve that gave no answer and five that called `console.to_utf8()` inside `main()` rather than as their block's first statement" | the orchestrator's part of the pull request body, first paragraph | for each of the twelve the changelog's second bullet names, `git show a9487d83e:<f> \| grep -c -e to_utf8 -e reconfigure` and the same at HEAD; the five rows of the earlier table's `main()` claim | holds (executed): each of the twelve counts 0 at the base and 1 or 2 at HEAD; the five called it inside `main()` at the base (`a9487d83e:.github/scripts/finding_counts.py:175` and the four the earlier row names, executed in the earlier audit, on code no commit since touched) |

### The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | unchanged since `592936753` (executed: `git diff --stat`) | as the earlier table states | none |
| the build | phase 1 as before; phase 2 as before, less the two residue lines | the design, the tree, and every claim re-run in both audits | none: `trail/phases/phase-2.md` ends with its last paragraph (executed) |
| the last round | unchanged since `592936753`, `trail/rounds/round-2.md` with round-2#1 closed `fixed 6e22d54f7`, read at HEAD in the earlier audit as its reader | as the earlier table states | none |
| the changelog | the same three bullets, less the two residue lines | the design, the build, and the tree on every statement checked in both audits, including the twelve with no call and the five that called inside `main()` | none: the fragment ends with its third bullet (executed) |
| the orchestrator's part of the pull request body | the census widens to every tracked `.py` with a `__main__` block and repairs seventeen entry points, twelve with no answer and five that called `console.to_utf8()` inside `main()`, and the five loops that left out `stdin`; Q1's default and the three exemptions; the rounds and fixes; the platform run; the merges; the broad run at `61db006cf` | the issue, `routing.md`, `frame/questions.md` Q1, the round records, `frame/plan.md` *Judgments of the run*, the changelog's second bullet, the tree (the count above), `trail/gate.md`, and the earlier audit's runs on each other paragraph, read again whole (read) | none |

```seal
target: a4ad23283 against a9487d83e
Verdict: sealed
```
