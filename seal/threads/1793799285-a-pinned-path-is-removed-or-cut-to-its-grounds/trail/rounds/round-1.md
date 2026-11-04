# Review round 1: 1793799285-a-pinned-path-is-removed-or-cut-to-its-grounds

```seal
target: 5c999a1c0 against release/v0.32.0
```

This round reviewed issue #1355's branch at `5c999a1c0` against `origin/release/v0.32.0` at `c8f235df2`, which is also the merge base. The review ran in a `git clone --no-local` of the repository checked out at the target. No earlier round exists, so this round carried no fact and opened every coordinate below itself. The repository declares no `seal/parity.md` and `seal/config.md` has no `Pact` row, so neither the parity reading nor the pact reading applies.

Outside `seal/`, the diff touches 17 files: 23 comment and docstring lines, the spelling of two fixtures, and `.github/workflows/test.yml`'s comments. No code path changes. Inputs, authorization, query scope, ordering, state transitions, concurrency and security therefore have no code to judge. The fixtures are judged under the value axis below. This change has its own axes, and the round walked each of them:

- whether each G line kept the grounds a person changing the value needs;
- whether each N line reads whole without the past file;
- whether each P line leaves its rule standing;
- whether each fixture keeps its value;
- whether text elsewhere in a touched file leaned on a removed citation for its referent;
- whether the workflow diff is comments only;
- whether the censuses and the squash case still pass;
- whether each cited issue page holds what its sentence sends the reader there for.

## Findings

### 1. The Windows shard comment keeps figures that make three shards enough, once the clause naming its arithmetic is cut

```seal
severity: should
location: `.github/workflows/test.yml:81-87`, `seal/threads/1793799285-a-pinned-path-is-removed-or-cut-to-its-grounds/trail/phases/phase-1.md`, `seal/threads/1793799285-a-pinned-path-is-removed-or-cut-to-its-grounds/changelog.md`, `seal/threads/1793799285-a-pinned-path-is-removed-or-cut-to-its-grounds/frame/design.md`
evidence: executed `git show 62161701:seal/specs/1791270165-the-windows-test-leg-is-measured-and-cut/phases/phase-3.md` (the section on `K` from the durations file), `git show 67694cba:seal/specs/1791384162-the-macos-test-leg-runs-in-shards/plan.md` (lines 94-109), `gh pr view 845`; read `.github/workflows/test.yml:69-90`
```

Why it matters: `frame/design.md` D1 defines G as "The grounds stay in one short sentence, or the issue or pull request number that holds them (`#N`) replaces the commit and the path." Two records claim this held for rows 1 and 2. The phase record's Q1 answer says "The figures already stand in each sentence", and the changelog fragment says "the grounds now stand in the sentence". The removed clause's record shows otherwise. It prices a Windows shard's job as a fixed cost (37 s of checkout and install, plus 25 s to the first case) plus 1,949 s over the count. Its table gives three shards 11.9 minutes on run 37458654434's pace and 12.8 minutes on run 37457228586's, which was 1.08 times slower. It then concludes: "Three meets Q1's 12 minutes on the faster run only, and by seconds".

The comment at `.github/workflows/test.yml:81-83` now reads "Four is the smallest Windows count whose slowest shard stays under 12 minutes on the figures of run 37458654434 (7,530 s of cases, 1,974 s unsharded)." On those figures, three also stays under 12 minutes, and the comment names neither the fixed cost nor the slower run that decides the count. A person who changes the count from the comment alone computes 1,974 / 3 = 658 s, about 11 minutes, and concludes that three is enough. The sentence was already loose before this change, but it carried the coordinate of the table that corrects it, and the rewrite cut that route. The macOS sentence at `:84` opens with "the same arithmetic", and the file no longer states that arithmetic anywhere.

The phase found that #841 holds no count. This round confirmed that PR #845 holds the four shards and their times but not the arithmetic. No `#N` can stand for the grounds, so they have to go in the sentence. The figures below come from the two records named on the evidence line.

```yaml
          # never off the file. A shard's job is a fixed cost (about 62 s on
          # Windows and 45 s on macOS, for checkout, install and pytest's
          # start) plus the leg's pytest time over the count. Four is the
          # smallest Windows count whose slowest shard stays under 12 minutes
          # on both run 37458654434 (7,530 s of cases, 1,974 s unsharded) and
          # run 37457228586, 1.08 times slower: three gives 11.9 and 12.8
          # minutes, four 9.2 and 9.8.
          # Three is the smallest macOS count the same arithmetic puts under
```

These lines replace `.github/workflows/test.yml:81-84` up to and including "Three is the smallest macOS count the same arithmetic puts under". The lines after it stay as they are. The snippet covers only the workflow, and the fix pass owes four more statements of the same fact:

- D1 rows 1 and 2 and the `.github/workflows/test.yml` row of `## Removes` in `frame/design.md` ("the figures stay in the comment");
- rows 1 and 2 of `trail/phases/phase-1.md` and its Q1 bullet on rows 1 and 2 ("The figures already stand in each sentence");
- the changelog fragment's "the grounds now stand in the sentence", which is true of rows 1 and 2 only after this fix.

```seal
verdict: fixed a43c13166
answer: The finding holds: on run 37458654434's figures alone three shards fit under 12 minutes, and the record's fixed cost and second run are what set four (read: the phase-3 record's `K` table and the macOS plan's arithmetic, at the commits the evidence line names). The comment at `.github/workflows/test.yml:81-92` now states the arithmetic in my own wording, not the proposal's. The proposal priced a shard as the fixed cost "plus the leg's pytest time over the count", and with 1,974 s of pytest time that gives three shards 720 s, 12.0 minutes, not the record's 11.9; the record divides 1,949 s, the time after the first case, and counts the 25 s before it in the 62 s. So the sentence says "case time", names the 37 s and 25 s that make the fixed cost, and gives 1,949 s beside 1,974 s. The macOS sentence names its fixed cost of about 45 s beside its factor, so "the same arithmetic" now points at the Windows sentence above it. The diff is comment lines only (executed: `git diff -U0` on the file). `trail/phases/phase-1.md` rows 1 and 2 and its Q1 bullet now say the arithmetic went into the sentences. The changelog's "the grounds now stand in the sentence" is true at this commit and is left as it reads. D1 rows 1 and 2 and the `## Removes` row on `.github/workflows/test.yml` in `frame/design.md` still say only that the figures stay; they are the orchestrator's to fold.
```

### 2. A comment still cites "the work item's `questions.md`" after the docstring stopped naming the work item, and `gaps.md` lists the leftovers by one wording

```seal
severity: should
location: `tests/behaviour/test_first_setup_asks_once.py:28-29`, `seal/threads/1793799285-a-pinned-path-is-removed-or-cut-to-its-grounds/gaps.md`
evidence: executed `git show origin/release/v0.32.0:tests/behaviour/test_first_setup_asks_once.py` (line 4, "The work item is", and line 28), and a `grep -nE` for the work item, the frame, the spec, Q-numbers and precedent wordings over the 17 touched files; read `tests/behaviour/test_first_setup_asks_once.py:1-30`, `gaps.md` *Not done*, `trail/phases/phase-1.md` *Departures from the frame*
```

Why it matters: At the base, line 4 of the module docstring named work item `1788354065-the-tree-that-must-stay-clean-has-no-way-to-opt-in`. The comment at line 28, "The sentence a session reads (Q1 of the work item's `questions.md`)", leaned on that name. The row 12 rewrite removed the citation, and the module's title line names no issue. So line 28 now points at the `questions.md` of a work item the module never names.

The phase's second departure reaches past the paragraph for rows 15 and 18 on these grounds: "a sentence whose referent is gone costs its reader a search". `gaps.md` *Not done* then claims to list what stands outside the rewritten docstrings, but it lists only the phrase "the frame", in two files. A list built from one wording is a sample (contract rule 12). The class is closed: every sentence in the 17 touched files that leaned on its file's removed citation. Reading each file for that, this round found line 28 and no instance besides the two `gaps.md` names.

`gaps.md` also gives "rewriting them renames cases" as its reason. That reason holds for the case names in `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py`. It does not hold for the comment at `tests/block_shapes.py:297` or for that module's case docstrings, which rename nothing. Its second reason, that each reads as the frame of #667, which the title names, does hold for them. So "the frame" leftovers can stay where `gaps.md` puts them, and its first reason should be narrowed to the case names.

```python
# The sentence a session reads, which the Q1 cases below hold in each place:
# the same rule `hooks/lib/optin.py` states, moved to where a session looks.
```

These two lines replace `tests/behaviour/test_first_setup_asks_once.py:28-29`. The fix pass also owes `gaps.md` *Not done* one change: name the class by its cause rather than by the phrase, and limit the renaming reason to the case names.

```seal
verdict: fixed d15fad64a
answer: The finding holds. The comment above `SESSION_RULE` now reads as the round proposes, after I checked it against the module: `SESSION_RULE` is what the cases under the `Q1: the sentence a session reads, once in each place` heading assert (read: its uses at lines 303, 312 and 325). `gaps.md` *Not done* now names the class by its cause, a sentence in a touched file that leaned on its file's removed citation for its referent. It says which were rewritten and lists the seven that stand, each naming #667's frame in a module whose title names #667. It gives the renaming reason for the case name alone. I built the list by searching each of the 17 touched files for the words that name a record's parts (work item, spec, frame, Q-, D- and O-numbers, Scope, overview, precedent, that table or module, this release) and reading each hit for the citation the build removed in that file. That is a sample over wordings, and `gaps.md` says so. Three hits were read and kept as outside the class. `questions.md` Q1 at `tests/behaviour/test_chain_hooks_hardening.py:569` and "this work item's `gaps.md`" at `:866` mean #422's work item, which their comment block and function still name. `tests/hooks/test_mode_gate.py:271`'s "the chain spec" never leaned on the scenario-id citation the build removed.
```

## Confirmations

What matched: S1. #1355's measure, run as the issue's body gives it at the target, prints no line, and its last `grep` exits 1 (executed).

What matched: S3 and S4. `tests/text/test_a_cited_commit_outlives_the_squash.py` passes with 12 cases, and `tests/test_censuses.py` passes with 194, each run narrow through `bin/test` (executed). The phase claims `cited(ROOT)` reads 21 tokens, all under `seal/`. This round did not call `cited` and holds that count as a claim. The empty measure leaves no token outside `seal/` for the squash case to read.

What matched: S2's values. `ELSEWHERE` at the base and at the target is the same 195-character string (executed, in Probes). The S7 case `test_a_path_outside_the_repository_is_not_read_and_a_missing_file_is` passes (executed). Row 22's f-string line, with `commit` bound to `5f11923f`, joins to the base literal (read at `tests/test_censuses.py:1055-1060`), and its case passes (executed). The phase's seen-red run for row 22 was not re-run. It is a claim with its command named in `trail/phases/phase-1.md`.

What matched: S5. Every added or removed line of `.github/workflows/test.yml` in the diff opens with `#` after its indent (read: the three hunks).

What matched: S6. `trail/phases/phase-1.md` lists all 25 lines of D1 with a disposition and a replacement (read against D1). The changelog's counts are ten P, six G, seven N and two F, and they match D1's rows (read).

What matched: the P lines. Rows 3, 5, 6, 7, 8, 13, 14, 16, 23 and 25 each remove a clause about where something came from, and each leaves its rule standing in the sentence (read at each rewritten line in the diff). In row 6, the two decisions below it read as the guard's own, and nothing else in that comment names the module it was modelled on (executed: `grep` for "modelled", "that module" and "round 1").

What matched: the G lines other than rows 1 and 2. Row 9 cites #422, and #422's body says "Refusing more words makes legitimate definitions unwritable" (executed: `gh issue view 422`, line 45 of the body). Row 10's grounds, a bound that lets an instruction straddling a heading pass, stand in the sentence before the cut (read `tests/behaviour/test_chain_hooks_hardening.py:834-837`). Row 24's grounds, that no constant can tell a paraphrase from a heading matched against the sentence that links it, stand in the sentence before it (read `tests/text/test_no_passage_is_pasted_into_a_second_file.py:39-43`).

Row 21's "before #667 changed it" names the same behaviour as the base commit it replaced. `hooks/routing.py` at `3911a8cf` equals the file at `v0.15.6`. Between `v0.15.6` and `v0.16.0`, two commits change the file: #672, which closes #667, and #660, which changes only a comment in `rounds` (executed, in Probes). The phase claims "`v0.16.0` holds it changed, so 'before #667 changed it' names the same base", and that claim holds only because #660 changes no reading.

What matched: the N lines other than the comment in finding 2. Rows 11, 15, 17, 18, 19 and 20 each read whole without the past file. Row 11's #664 is the issue that PR #675 fixed, and #675 is the commit that touched that work item's directory (executed: `git log --all` on the directory). Row 12's and row 19's examples, `S2 of #952` and `S7 of #952`, stand in their modules (read `tests/behaviour/test_first_setup_asks_once.py:91`, `tests/hooks/test_mode_gate.py:73`). The unattributed labels, such as `S4 (d)` and `Q4`, read as the cases' own numbers under the new docstrings.

What matched: frame D2 and plan A1, read against `skills/core/SKILL.md` *The rule a mechanism is kept against*. That rule keeps a mechanism only while its record of what it caught outweighs what it costs. A case added by this work would have caught nothing on the day it lands, because the 25 lines are removed by hand. The one citation that misdirects a reader is one whose commit no `main` or release ref reaches, and the squash case still refuses that (executed: the module passes). Whether a line holds grounds a reader acts on is a judgment of meaning. *The first value* gives that judgment to the proofer rather than to a spelling rule. This round is that reading, and it found finding 1, which no spelling check would have found. D2's further claim, that a refused writer would move to a bare commit, rests on a count of 51 tokens. This round did not re-run that count, and the choice does not depend on it.

What matched: `gaps.md` *Not done* puts the bare commits in shipped text outside this work. #1355's *Done when* is its measure of the `<commit>:<path>` form, and a bare commit is not that form, so they belong outside. Whether they get a home is in `## Not judged`. The "the frame" leftovers also belong outside, for the reason finding 2 gives.

No test was added, so no new test is read against its group.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the bare commits in shipped text are cleared by a new issue. `frame/design.md` *Scope* says the orchestrator may file one, and no issue or `seal/follow-up.md` row holds them yet. The class includes `7e44106` and `4edc5de6`, which stand beside rewritten sentences. | `seal/threads/1793799285-a-pinned-path-is-removed-or-cut-to-its-grounds/gaps.md` | the orchestrator |
| The full suite, the repository-wide lint and the typecheck at HEAD, labelled `unverified` by the build, and not run by this round (contract rule 2) | `seal/threads/1793799285-a-pinned-path-is-removed-or-cut-to-its-grounds/gaps.md` | the orchestrator, at the broad gate |

## Probes

| Command | Result |
|---|---|
| #1355's measure as its body spells it, run in the clone at the target | no line printed, `grep` exit 1 |
| `bin/test tests/text/test_a_cited_commit_outlives_the_squash.py -q` | 12 passed, exit 0 |
| `bin/test tests/test_censuses.py -q` | 194 passed, exit 0 |
| `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -p no:xdist -k test_a_path_outside_the_repository_is_not_read_and_a_missing_file_is` | 1 passed, exit 0 |
| `python3 -I -` on stdin, executing the `AT` and `ELSEWHERE` assignments read from the file at the base and at the target, and comparing the two values | equal, 195 characters each; no file written |
| `git diff --quiet 3911a8cf v0.15.6 -- hooks/routing.py`, then `git log --oneline v0.15.6..v0.16.0 -- hooks/routing.py` and `git diff 3911a8cf f09f654e -- hooks/routing.py` | exit 0; two commits, `3fc0c5bd` (#672) and `f09f654e` (#660), and #660's change to the file is a comment in `rounds` alone |
