# Review round 2: 1794396808-test-files-declare-no-target

```seal
target: 617a20c4f, fixes 81515b928..617a20c4f
```

This is a verifying round over `81515b928..617a20c4f`, five commits: the two
fixes `379eb64b8` and `1ebd4cf19`, the closing memo's row `28ada57ee`, the
framer's fold of design G1 with the orchestrator's row in `frame/plan.md`
*Judgments of the run* (`6ad069d57`), and the close blocks (`617a20c4f`).
`routing.md`, the three frame files, `gaps.md`, `changelog.md` and `pr.md`
were read again at `617a20c4f`. Only `frame/design.md` G1, one row of
`frame/plan.md` and one row of `gaps.md` changed since round 1. `pr.md` and
`changelog.md` are unchanged, and neither states where a file that declares
no `TARGET` stands.

Carried from round 1 and not re-established: the class each finding named.
For finding 1, the five lines that write the readers-hide file's stem. For
finding 2, the one statement of the placement rule in the tree outside
`seal/threads/`. Re-derived here: whether each fix holds, and the grep for
each fact over the target, the work item's records included. The runs used
the round-1 clone under the work item's scratch directory, checked out at
`617a20c4f`.

## Findings

### 1. The fold of design G1 states, as a fact of the tree at `b9ca37404`, a placement that five files of that tree did not follow

```seal
severity: should
location: `seal/threads/1794396808-test-files-declare-no-target/frame/design.md:9`
evidence: executed `git show b9ca37404:<file> | grep -n '^import\|^from'` for `tests/behaviour/test_a_commit_names_its_repository.py`, `tests/behaviour/test_a_probe_that_commits_says_so.py` and `tests/behaviour/test_the_set_a_work_item_always_has.py`, `git show b9ca37404:tests/text/test_no_passage_is_pasted_into_a_second_file.py | grep -n 'passages.py\|load_module'`, `git show b9ca37404:CONTRIBUTING.md | grep -n -A2 'where its cases load or run shipped code'`; read `git diff 81515b928 617a20c4f -- seal/threads/1794396808-test-files-declare-no-target/frame/design.md`
regression: round-1#2
```

Why it matters: the unit is the G1 row of `frame/design.md`, which the fold
`6ad069d57` rewrote. Round 1's finding 2 asked that the placement sentence
in `CONTRIBUTING.md` stop stating what the tree does not hold. The fix
`1ebd4cf19` did that, and the fold restated G1 to match it. The fold then
wrote that rule into G1 as a fact of the tree. The row now reads "At this
commit a file that declares none stood in `tests/behaviour/` or
`tests/text/` by what its cases run". The section's date line makes "this
commit" `b9ca37404`. At `b9ca37404`, three files of `tests/behaviour/`
import only `read` from `tests/conftest.py` (`:19`, `:17` and `:30`), and
`tests/text/test_no_passage_is_pasted_into_a_second_file.py:58-59` loads
`skills/settle/scripts/passages.py`. Before the fold, G1 said what the
clause states ("A file that declares none stands ... by what its cases
run"), and that was true of `CONTRIBUTING.md:260` at that commit. The fold
turned it into "stood", a sentence about the files. Those are the files
round 1's finding 2 named.

A grounding row dated to the commit the framer read must state that commit,
and the sealer reads the frame against the tree. A reader of G1 now takes
the old placement as one the tree kept, and finding 2 showed it did not.

The fact stands at one place in the work item's present records,
`frame/design.md:9` (executed: `git grep -n -i -e 'by what its cases run'
-e 'only read text' -e 'load or run shipped code'` at `617a20c4f`, which
finds nothing outside `seal/threads/`). `frame/design.md:30` quotes the old
paragraph's opening only to say it is rewritten, and it stays as it is. The
other hits are history in `trail/phases/phase-1.md` and
`trail/rounds/round-1.md`. The snippet replaces the row's first two clauses after "free.", and the
rest of the row stands.

```markdown
At this commit the section placed a file that declares none in `tests/behaviour/` or `tests/text/` by what its cases run, a placement five files of the tree did not follow (`trail/rounds/round-1.md` finding 2), and called those two directories the tree-wide files `skills/verify/SKILL.md` *Scope: cheap and often, broad and once* runs at every phase boundary.
```

```seal
verdict: fixed c9b507367
answer: The finding holds: the tree at `b9ca37404` did not follow the placement its section stated. The framer restated design G1 to say the section placed such a file by what its cases run, a placement the files round 1 finding 2 lists did not follow, with each file's imports read at `b9ca37404`. The fix and the finding are in the work item's records alone, so the sealer reads it with no further round.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `tests/lib/test_blocks.py:11-18` at `617a20c4f` takes round 1's
replacement word for word. It says that the oracle's own cases stand in
`tests/test_commonmark_oracle.py`, and that the readers-hide file keeps the
import case. Both hold at the target (read:
`tests/behaviour/test_the_readers_hide_what_a_renderer_hides.py` keeps one
case). The grep `git grep -n "oracle's own cases" -- tests` lists
`tests/lib/test_blocks.py:15`, `tests/lib/test_routing.py:16` and
`tests/lib/test_tables.py:25`, and each now names the new home (executed).
`bin/test tests/lib/test_blocks.py -q` gave `17 passed` (executed). The
close block's `fixed 379eb64b8` names a commit that touches the finding's
location.

```seal
confirms: round-1#2
```
What holds: `CONTRIBUTING.md:289-290` at `617a20c4f` takes round 1's
sentence, and no other statement of the placement stands in the tree
outside `seal/threads/` (executed: the grep of finding 1 above). The close
block says no code reads the split, so no file moved and no `check:` line
was re-pointed. `bin/seal rules --check` gives `all 176 check lines in 69
rule files hold.` and `bin/seal layout --check` ends `141 files read, 0
refused, 67 declare no TARGET`, each with exit 0 (executed). The new
sentence's claim, that the two directories hold every file that declares
none, holds: the 67 files `seal layout --check` reports all stand there, as
round 1 counted, and no file under `tests/` was added or moved in the range
(read: the range's diff stat). The frame side of this fix is finding 1.

What matched: the row `28ada57ee` adds to `gaps.md` *Not verified* names
the fix pass's run set and the orchestrator's broad gate as its answerer.
No row left the memo (read: the range's diff of `gaps.md`, one line
added). The row `6ad069d57` adds to `frame/plan.md` *Judgments of the run*
names the fold, its grounds and the document it was judged against.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite beyond `tests/lib/test_blocks.py` and the two checks this round ran | `gaps.md`, the round 1 fix pass's row | the orchestrator's broad gate |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/lib/test_blocks.py -q` at `617a20c4f` | `17 passed`, exit 0 |
| `bin/seal rules --check` at `617a20c4f` | exit 0; `all 176 check lines in 69 rule files hold.` |
| `bin/seal layout --check` at `617a20c4f` | exit 0; `141 files read, 0 refused, 67 declare no TARGET` |
| `git show b9ca37404:` of the three `tests/behaviour/` files and the paste-check file, each grepped for its imports and loader | the three import only `read`; the paste-check file loads `passages.py` at `:58-59` |
| `git grep -n -i -e 'by what its cases run' -e 'only read text' -e 'load or run shipped code'` at `617a20c4f` nothing outside `seal/threads/`; in the work item, `frame/design.md:9`, the quote at `frame/design.md:30`, and history in `trail/phases/phase-1.md:101` and `trail/rounds/round-1.md` |
