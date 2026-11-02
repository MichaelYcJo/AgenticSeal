# Review round 2: 1793593418-two-config-rows-show-the-seal-mark

```seal
target: f2c96cda7, fixes bf3efaf23..f2c96cda7
```

This is a verifying round. Its target is the diff `bf3efaf23..f2c96cda7`,
read in a `git clone --no-local` of the branch at `f2c96cda7`. The range
holds the fix pass's two commits, `863a7d2af` for finding 1 and `a8c41097a`
for finding 2, and the orchestrator's records commit `f2c96cda7`. Finding 3
was fixed at `e3981d8fb`, before the range, and this round read that commit
to answer it. No `seal/parity.md` is declared, so the round block carries no
`original:` line.

Carried from round 1 and not re-established: what `seal_stamp.py`
reads for the stamp (`:1145-1160`), the guarantee arm of `chain_check.py`
(`:1646-1692`), and round 1's confirmations of the release half, the row
reads and the untouched terminal stamp. The fix range touches none of those
files (`git diff --stat bf3efaf23..f2c96cda7`, executed). Re-established
this round: what `chain_check.py#follows` answers (`:955-986`, read), and
every verdict below.

## Findings

### 1. The design's `add` says a base that HEAD does not hold is named, where the code names the sealed commit, and two other record sentences still state the read before the fix

```seal
severity: should
location: `seal/threads/1793593418-two-config-rows-show-the-seal-mark/frame/design.md:236-239`, `seal/threads/1793593418-two-config-rows-show-the-seal-mark/frame/design.md:62-63`, `seal/threads/1793593418-two-config-rows-show-the-seal-mark/changelog.md:3`
evidence: read `seal/threads/1793593418-two-config-rows-show-the-seal-mark/frame/design.md:52-65`, `seal/threads/1793593418-two-config-rows-show-the-seal-mark/frame/design.md:228-246`, `seal/threads/1793593418-two-config-rows-show-the-seal-mark/frame/plan.md:107`, `seal/threads/1793593418-two-config-rows-show-the-seal-mark/changelog.md:3`, `skills/code-review/scripts/pr_body.py:353-367`, `skills/code-review/scripts/pr_body.py:755-760`, `skills/code-review/scripts/chain_check.py:955-971`
regression: round-1#1
```

The unit is the design's `add` for `docs/the-review-record.md` *The
guarantee*, which `f2c96cda7` changed to fold finding 1's fix. The plan's
*Judgments of the run* row for that fold (`plan.md:107`) says "a sealed
commit that checkout's HEAD does not hold puts no mark and is named". The
fold instead hung the new clause on the existing base sentence. The defect
came from that edit.

Why it matters: the `add` now reads "A base the verdict block names that git
cannot resolve there, or that the checkout's HEAD does not hold, puts no
mark either, and is named" (`design.md:236-239`). Both relative clauses
modify "A base". The code checks the base only for resolving
(`pr_body.py:353-358`). It names a sealed commit that `follows` answers
`unseen` or `off` for (`pr_body.py:365-366`, `chain_check.py:966-971`). So
the sentence names one case the code does not have, a base HEAD does not
hold, and leaves out the two it does have: a sealed commit git cannot
resolve and a sealed commit HEAD does not descend from. The settle writes
this `to` into `docs/the-review-record.md` as policy, and an agent reading
it would expect a line about the base where the code prints one about the
commit. "The work item's own checkout" also has no referent for a local-mode
work item, which sits under the common git directory and is read in the
working directory's checkout (`pr_body.py:755-760`). The plan's *Technical
context* (`plan.md:29-31`) states that fallback, and the `add` does not.

The class is every sentence in the work item's records and in the fix
diff that states where `seal pr-body` reads the mark, or which cases it
names. I listed it by taking apart `frame/design.md` whole, the plan's
*Technical context* and *Judgments of the run*, `changelog.md`,
`templates/setup/config.md` *The seal mark*, and the docstrings and comment
`863a7d2af` touched in `pr_body.py`. Two more members are wrong:

- `design.md:62-63`, *Scope* item 2: "A guarantee that is absent, refused,
  or not `sealed` at HEAD puts no mark and prints no line". A sealed commit
  HEAD does not hold is not sealed at HEAD, and since `863a7d2af` it prints
  a line. The sealer reads the frame against the tree, and here the frame
  contradicts its own `add`.
- `changelog.md:3`: "The row and HEAD are read in the work item's own
  checkout, so a run from another checkout of the repository writes the
  same body." For a local-mode work item sealed on a branch checked out in a
  linked worktree, a run from the main checkout reads the main checkout's
  HEAD, `follows` answers `off`, and the body gets no mark and a named line
  (`pr_body.py:760`, `chain_check.py:970-971`, read). A linked worktree is a
  normal-flow shape where another session works in the same clone
  (`skills/implement/orchestration.md:28-29`). The line it prints names the
  checkout, so the reader is not misled for long. The release note still
  states a promise local mode does not keep.

Three members are right and stay: `plan.md:29-31`; the module docstring
(`pr_body.py:26-31`) and `seal_mark`'s docstring; and the template's "A work
item not sealed at HEAD gets no mark, and the sealer and the pull request's
check name why", which leaves the new line out but says nothing false.
`design.md:173-176`, *Data & interfaces*, lists the lines a reader sees
without the base line or the commit line. It has left out the base line
since the phase-1 fold, so it predates this range. It is left to the same
edit as the others and not raised on its own.

```text
design.md, the `add`, replacing "It reads both in the work item's own
checkout. A base ... cannot then be read." with:

    means (*The stamp*). It reads the row and HEAD in the work item's own
    checkout, and, for a work item under the common git directory, in the
    checkout the command runs in. A base the verdict block names that git
    cannot resolve there, and a sealed commit that checkout's HEAD does not
    hold, put no mark either, and are named, since whether the seal holds at
    HEAD cannot then be read.

design.md, Scope item 2, replacing its last full sentence before `--check`:

   A guarantee that is absent, refused, not `sealed`, or sealed at a commit
   a later commit outside the closing records follows, puts no mark and
   prints no line: the sealer and the pull request's check name those. A
   base that git cannot resolve, and a sealed commit HEAD does not hold, put
   no mark and are named, since whether the seal holds at HEAD cannot be
   read there.

changelog.md:3, replacing "The row and HEAD are read in the work item's own
checkout, so a run from another checkout of the repository writes the same
body." with:

    Where `seal/` is committed, the row and HEAD are read in the work item's
    own checkout, so a run from another checkout of the repository writes
    the same body; a work item under the common git directory is read in
    the checkout the command runs in.
```

```seal
verdict: fixed 332455460
answer: The finding holds; the orchestrator's fold at f2c96cda7 hung the new clause on the base sentence. The three sentences went in as given, records only: the design's `add`, *Scope* item 2 and `changelog.md`. `seal chain-check --worktree` and `seal rules --check` exited 0 after the edit (executed).
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `main` takes the root from `OPTIN.repo_root` of the work item's
path and falls back to the working directory's (`pr_body.py:760`), and
`_seal_at_head` names a sealed commit that `follows` answers `unseen` or
`off` for (`pr_body.py:365-366`). Read against `chain_check.py:955-971`,
the two answers cover a commit git cannot resolve and one HEAD does not
descend from. The `after` answer, a stale seal, stays silent as before. The
crafter claims each new case was seen red. I re-ran that in the clone,
editing `pr_body.py` with the Edit tool and restoring it. With the root read
from the working directory alone and the naming removed, the main-checkout
case and both naming cases failed and the local-mode case passed, which is
the old code's behaviour (executed). With the fallback alone dropped, the
local-mode case failed (executed). After both were restored, `git status
--porcelain` printed nothing. The full module and every module that names
`skills/code-review/orchestration.md` read 437 passed (executed). The
finding's other class members, the base's resolution and `follows`, now
read the same root, since `seal_mark` passes it to both (read). What the
fix's records say about this read is finding 1 above.

```seal
confirms: round-1#2
```
What holds: `orchestration.md:319-325` now has the orchestrator run
`seal pr-body` and send the body with `gh api -X PATCH` after each later
`sealed` verdict on an open pull request. Widening it from the repair alone
to every re-seal is right. The `withheld` repair paragraph already gives
its body to an open pull request "as the stated limit above says"
(`:399-402`), and a sentence about the repair alone would have left that
path and the merge path without the step. The sentence has one reading.
"After" governs all three paths: this repair, a merge from the base, any
other repair. "The file" and "the same way" take their referents from the
two sentences before it. It does not copy a passage: the section's opening
paragraph (`:223-230`) gives the first opening's reason, that the sealer
checks the body before its own verdict exists, and the new sentence gives a
different reason, that the body sent after a repair stood on a seal no
longer at HEAD. They share only the conclusion that a run after the verdict
writes the mark. `test_no_passage_is_pasted_into_a_second_file.py` and
`test_a_moved_rule_leaves_its_definition.py` read 225 passed (executed).
One weighing that raised nothing: on the merge path no body is sent before
the new verdict (`:282-294` runs `seal pr-body` and sends nothing), so the
grounds sentence "The body sent before that verdict carries no seal mark"
has no body to refer to there. The pull request still shows the body from
its opening, mark included. The act the sentence orders is still right on
that path, since it refreshes the copied part, so an orchestrator does
nothing different and the sentence costs no finding. The changelog's
process row states the step.

```seal
confirms: round-1#3
```
What holds: `e3981d8fb` rewrote the two `to` values as round 1 gave them.
The `branch-and-release` `to` (`design.md:201-214`) no longer restates the
values or the release row's one reader. The `the-review-record` `add`
(`design.md:228-246`) no longer restates the values or the address tie.
Both cite `templates/setup/config.md` *The seal mark*. The tree's
`chain_check.py --worktree`, whose `pins_and_copies_in` arm reads each `to`
against every tracked rule document for a shared run of 15 words and every
test literal for a pin (`chain_check.py:1239-1297`, read), printed no pin
or copy notice and exited 0 (executed). Weighed against #1216 by hand as
well: the fix range adds no `from` and takes out no pinned sentence, and
the one rewritten `to`, the `add` in finding 1, repeats no passage of
another document.

```seal
confirms: none
```
What matched: dropping the 8-character cut of the commit in the named line
is right. `NOT_IN_HISTORY` prints the commit as the guarantee's `target:`
writes it (`pr_body.py:227-230`, `:366`). `BASE_UNSEEN` prints the base as
written, and `chain_check.py#follows_reason` prints the commit as written
for `unseen` and `off` (`:992-995`), so the new line spells it the way the
other two lines about the same guarantee do. A reader can then search the
guarantee for the printed text. The cut had no grounds beyond length, the
value is 7 to 40 hex digits by `hooks/lib/fields.py`'s `COMMIT`, and the
line goes to the terminal and never into the body. Read. The case pins the
full sentence with the full commit for both answers (`Test_seal_mark`,
executed above).

```seal
confirms: none
```
What matched: the four new cases against their groups. `bin/seal layout
--pairs tests/skills/test_pr_body.py` read 1 file and 0 pairs (executed).
Each case covers what no other case in its group does. The main-checkout
case is the only one that runs `main` from a checkout that does not hold
the work item. The local-mode case is the only one where `repo_root` of the
work item answers "", and with the fallback dropped it alone fails
(executed). The two `Test_seal_mark` cases are the only ones that reach
`follows`'s `off` and `unseen` answers, and `BASE_UNSEEN`'s case stops
before `follows`. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at `f2c96cda7`: the full suite, the repository-wide lint and the format check. This round ran the narrow modules under *Probes* alone, and the suite stays `unverified` | the branch at `f2c96cda7` | the orchestrator, by `seal gate` once the rounds settle; the sealer's spawn follows it |
| Whether a pull request page draws the mark line as the icon, carried from round 1 | `frame/questions.md` Q1 | a measurement on the first body written after a seal by 0.28.0 or later |
| Whether the mark at width 128 looks as the owner wants, carried from round 1 | `frame/questions.md` Q2 | the owner |
| The new cases on Linux and Windows. They build a linked worktree and a local-mode root, and ran on macOS alone | `tests/skills/test_pr_body.py` | the orchestrator, by the `tests` workflow or CI on the pull request |
| Edges weighed and not raised. A local-mode run from a directory outside every checkout gives `root` "", and the named line would read "HEAD in  does not hold"; the flow runs `seal pr-body` from a checkout. `NOT_IN_HISTORY` prints the checkout's absolute path, and only on the terminal, never into the body | `skills/code-review/scripts/pr_body.py:227-230`, `skills/code-review/scripts/pr_body.py:760` | none owed; recorded so the next round does not search again |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_pr_body.py <every test module naming skills/code-review/orchestration.md> -q`, in the clone at `f2c96cda7` | 437 passed, exit 0 |
| The same runner, `-k "another_checkout or local_mode_work_item or head_does_not_hold"`, with `pr_body.py:760` set to the working directory's root alone and `:365-366` removed, through the Edit tool | 3 failed (both naming cases, the main-checkout case), 1 passed (the local-mode case), exit 1 |
| The same runner, `-k local_mode_work_item`, with the `or` fallback alone removed from `pr_body.py:760` | 1 failed, exit 1. Both edits were restored with the Edit tool, and `git status --porcelain` in the clone printed nothing |
| `bin/test tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/text/test_a_moved_rule_leaves_its_definition.py -q` | 225 passed, exit 0 |
| `bin/seal layout --pairs tests/skills/test_pr_body.py` | 1 file read, 0 pairs, exit 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline 4ab345cba --root <the worktree> --worktree`, before this record was written | exit 0. It names the three round-1 findings and the commit after round 1 as owing a verifying round, and the missing `trail/gate.md` and `guarantee.md`. It prints no rule-change, pin or copy notice |
| `bin/seal rules --check`, in the worktree | exit 0 |
