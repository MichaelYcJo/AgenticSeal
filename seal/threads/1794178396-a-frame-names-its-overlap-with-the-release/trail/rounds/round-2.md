# Review round 2: 1794178396-a-frame-names-its-overlap-with-the-release

```seal
target: 084ec22b, fixes dfc639f2..c666add7
```

This is the verifying round over round 1's fix pass, `fc892d57` and `2afa078b`, against the base `release/v0.36.0` at `94d04d30`. It was worked in a `git clone --no-local` of the branch worktree at `65651238`. The round also read the orchestrator's three commits since round 1 as claims: `705d6e02` commits round 1's record, `a2098f95` folds both findings into the frame, and `65651238` commits the close blocks (executed: `git show --stat` over the five commits). `seal/parity.md` is absent, `seal/config.md` has no `Pact` row and no `Record language` row, so no parity comparison applies and the record is English.

The round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/rounds/round-1.md` whole at `65651238`. The issue has no comments, as the spawn prompt states; this round did not re-run `gh issue view 1443`.

Carried from round 1 and not re-established: the `94d04d30` coordinates of `frame/design.md` *Grounding* and `frame/plan.md` *Technical context*, which round 1 opened at that commit and which the fold left unchanged; and phase 1's seen-red result for `test_the_plan_template_carries_the_overlap_table`, which round 1 re-ran, since the case file is unchanged after round 1's target. Re-opened this round: `skills/implement/orchestration.md:376-407` and `docs/releasing/branch-and-release.md:30-42`, the coordinates round 1's finding 1 names.

**The `Seal-Routing: 1794178396` report blocks the pull request.** `705d6e02` and `a2098f95` carry `Seal-Routing: 1794178396`, and the one declaration this pull request judges is the directory `1794178396-a-frame-names-its-overlap-with-the-release`. `skills/code-review/scripts/chain_check.py:1838-1853` (`trailer_findings`) classes such a trailer as a problem, not a notice, wherever the root is shared. `:1933` judges a pull request strictly unless it is a draft, and `:2042-2044` exits 1 on any problem under that judgment. `docs/checks/the-routing-check.md` *At the pull request* states the same rule. The local run exits 0 only because no pull request exists yet. Run as a ready pull request, the check printed both lines among its refusals (executed, under *Probes*). The other refusals of that run are the owed verifying round, the missing gate record and the missing guarantee, which this round, the broad run and the sealer answer in turn. Nothing later in the chain clears the two trailer lines. Both commits are committed by their author, so the exception for a commit whose committer differs from its author does not apply. The orchestrator's reason for leaving them holds in part. The close blocks that name `fc892d57` stand in `65651238`, and a rewrite from `705d6e02` re-creates that commit anyway. So the rewrite costs the two `verdict: fixed` lines in the re-created close commit, a force push of the pushed branch, and this record's `target:` line. This round reopens round 1's finding 1, so a fix pass and a third round follow. The cheapest point for the rewrite is before this record is committed: a rewritten HEAD whose tree is `3f0db7cc` is the tree this round read, since that is the tree of `65651238` (executed: `git rev-parse 65651238^{tree}`). This is no finding, because the trailers are no file a fix commit touches, and the check itself refuses the ready pull request. The orchestrator answers it before the pull request opens.

Orchestrator's note, added before this record was committed: the orchestrator rewrote both trailers to the full work item id and force-pushed. The commits this record names by their old hashes map as follows: `705d6e02` to `da7096a3`, `a2098f95` to `dfc639f2`, `fc892d57` to `6f9669aa`, `2afa078b` to `c666add7`, and `65651238` to `084ec22b`. The tree at `084ec22b` differs from `3f0db7cc` only in `trail/rounds/round-1.md`, whose two close blocks now name `6f9669aa` and `dfc639f2`. The `target:` line names the rewritten head.

## Findings

### 1. A carrier whose rounds have ended hands the move to "the next item", which a plan can order after another item, so the paragraph still lets an item merge before the carrier

```seal
severity: must
location: `skills/implement/orchestration.md:403-406`
evidence: read `skills/implement/orchestration.md:386-406`, `docs/releasing/branch-and-release.md:30-42`, `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/frame/design.md:34`, `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/frame/plan.md:38-44`, `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/trail/rounds/round-1.md:58`
reopens: round-1#1
```

Why it matters: the close of round 1's finding 1 does not hold for one sentence of the same paragraph. The close claimed that "the paragraph still reads as one" and that "the sentence on a move made after the carrier's last round stands as it was" (`trail/rounds/round-1.md:58`). That sentence, `skills/implement/orchestration.md:403-406`, says: "where the chosen item's rounds have already ended, the move goes to the next item whose rounds still read it". Lines 395 to 398 now say the move goes to "an item that no plan orders after another" and that this item merges "before every other item of the release". "The next item" is bound by neither.

This release has the shape. `frame/plan.md:38-44` orders #1443 before #1440, #1442 and #1444. Had #1443's rounds ended before the move, "the next item" could be #1440, which #1443's plan orders after #1443. The orchestrator then holds two instructions that cannot both hold. Merging "in the order their plans' ... sections state" (line 391) puts #1443 first, without the move. The first pull request into `release/v0.36.0` then does not move the version, which is finding 1's defect, against `docs/releasing/branch-and-release.md:30-42`. Merging the carrier "before every other item" (line 397) puts #1440 before #1443, against #1443's plan. The paragraph's departure rule (lines 392 to 395) writes a *Judgments of the run* row only where two plans state opposite orders, or where the item ordered first cannot be sealed before the other. Neither holds here, because #1443 is the item whose rounds have ended.

At round 1's target the same sentence already let the item ordered first merge before the fallback carrier, so it was a statement of finding 1's defect that round 1's location did not list. The fix pass listed the class from its diff and by `git grep` on "as each is sealed", "item first in" and "first in it" (`trail/rounds/round-1.md:58`). None of those phrases stands in this sentence, so the search did not reach it, and the listing was a sample of the paragraph, not the whole of it (contract rule 12).

The fix keeps the fallback carrier inside the carrier class, and where no such item is, gives the chosen item the move with the verifying round the paragraph already says it owes. The rewritten sentence is the only statement it touches. `frame/design.md:34` (*Scope* item 4), `changelog.md:3` and `changelog.md:13` each state the carrier as an item no plan orders after another, which the rewrite keeps, so none of them changes. *Scope* item 4 does not state the fallback; whether to fold it there is the orchestrator's call.

`skills/implement/orchestration.md`, lines 403 to 406:

```markdown
phase, because the crafter reads its version write there. A move made
after a work item's last round owes a verifying round of its own, so
where the chosen item's rounds have already ended, the move goes to
another item that no plan orders after another and whose rounds still
read it, and where no such item is, the chosen item takes the move and
the verifying round it owes. Where the
```

```seal
verdict: fixed ea6fa6893
answer: `skills/implement/orchestration.md` lines 404 to 409 now carry the record's block word for word. I read it against `frame/design.md` *Scope* item 4 as `1200d2c1` folded it, which states the same fallback. This time the class was listed as a closed set, by taking the paragraph apart: each sentence of `skills/implement/orchestration.md` lines 376 to 413 and each sentence of `changelog.md` lines 3, 6 and 13 was read against the carrier rule's two conditions, that the carrier is no item a plan orders after another, and that it merges before every other item. Two sentences beyond the location failed it. The paragraph's departure sentence let the orchestrator choose an order that puts another item first where the item ordered first, which can be the carrier, cannot be sealed before the other. It now reads "the orchestrator chooses the order, with the item that carries the move still first, and writes the choice", in my words; *Scope* item 4 does not carry that clause, so the frame is the orchestrator's to fold. `changelog.md` line 3 has the same departure sentence, which `pr.md` quotes, so its carrier sentence took the clause instead: the orchestrator merges the carrier before every other item "whatever order it chooses for a pair". Every other sentence holds: the merge in the plans' order (a carrier is never ordered after another item, so merging it first keeps that order), the crafter's fold of the move ("that work item" names the carrier), the unordered items merging once the carrier has landed, `changelog.md` lines 6 and 13, and the sentences on `main` and on a repository that moves the version at the release, which name no carrier. All six `pr.md` quotes stand, with whitespace collapsed (executed: a read-only Python comparison printed True for each). `bin/test tests/behaviour/test_the_set_a_work_item_always_has.py tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_docs_line_wrap.py -q` exited 0 with 149 passed.
```

### 2. Scenario S3 still gives the version move to "the item first in" a pair's order, which the folded *Scope* item 4 and the rewritten paragraph no longer guarantee

```seal
severity: should
location: `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/frame/design.md:51`
evidence: read `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/frame/design.md:34`, `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/frame/design.md:51`, `skills/implement/orchestration.md:395-400`, `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/frame/plan.md:38`, `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/trail/rounds/round-1.md:25`, `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/trail/rounds/round-1.md:58`
```

Why it matters: the fix pass's close (`trail/rounds/round-1.md:58`) and round 1's own grounds (`:25`) claimed S3 stays true under the fix. S3's Given names one order, "an order for a pair", so "the item first in it" is the item that the pair's order puts first. *Scope* item 4 as `a2098f95` folded it (`frame/design.md:34`) and `skills/implement/orchestration.md:395-397` give the move to "an item that no plan orders after another, which the orchestrator chooses where several are". Where an item no plan orders stands beside the pair, both are candidates, and the orchestrator may choose the unordered one. This release is that case: `frame/plan.md:38` says #1439 and #1441 meet this work nowhere, so each is a candidate beside #1443. S3's *Verifiable how* cell says to read G1's paragraph as rewritten, and that paragraph does not say what S3's Then says. The sealer reads S3 as the acceptance row it checks the paragraph against. S3 reads true only where "it" is taken as the release's whole merge order, which the row's Given does not name, so the row has two readings. The frame is the orchestrator's, so the orchestrator folds the fix.

`frame/design.md` line 51:

```markdown
| S3. The orchestrator merges the release's items | Given plans that state an order for a pair, when the orchestrator merges, then it merges in that order, gives the version move to an item no plan orders after another, and merges that item before every other item of the release. | Read G1's paragraph as rewritten. |
```

```seal
verdict: fixed 1200d2c1
answer: The orchestrator folded S3 at `1200d2c1`. `frame/design.md` line 51 now carries the record's row word for word (read). The fix pass wrote nothing for this finding, since the frame is not the crafter's to write. The paragraph S3 is read against still gives the move to an item no plan orders after another and merges it before every other item, at `ea6fa6893`.
```

## Confirmations

```seal
confirms: round-1#2
```
What holds: `templates/records/sdd-plan.md:23` now reads "a fact that the other's change reads or adds content to", and the line is identical to `frame/design.md:62` (executed: `diff` of the two lines exited 0). `agents/framer.md:86`, `changelog.md:3` and *Scope* item 2 (`frame/design.md:32`) read the same, so each statement of the meet definition agrees. The template's heading, header and placement are unchanged, and the module that pins them passed (executed, under *Probes*).

What matched: the four locations of round 1's finding 1 take the record's paste-ready text word for word: `skills/implement/orchestration.md:395-400`, `frame/design.md:34` as folded by `a2098f95`, the carrier sentence of `changelog.md:3`, and `changelog.md:6`. The fifth sentence the fix pass rewrote, the second `### Process changes` row (`changelog.md:13`), states the carrier as the paragraph does. Finding 1 above is about the sentence after them. Read.

What matched: `frame/plan.md:59`, the fold row `a2098f95` adds, describes that commit's diff, and its citation of `docs/releasing/branch-and-release.md` *Work accumulates on a release branch* holds: that section (heading at `:176`) says at `:257-259` why the version moves in the release's first pull request. Read.

What matched: `2afa078b` amends the first row of `gaps.md` *Not verified* in place, and no row left the memo. Its claim that the fix pass changed no Python file holds (executed: `git show --stat` lists `changelog.md`, `skills/implement/orchestration.md`, `templates/records/sdd-plan.md` and `gaps.md`). Its claim that the fix pass ran the plan row's three modules and `tests/behaviour/test_docs_line_wrap.py` was re-run here with the same count, 149 passed (executed, under *Probes*). The row keeps the full suite, the lint and the format check `unverified`, with the orchestrator at the broad gate as their answerer, so the label is honest.

What matched: each of the six quotes in `pr.md` stands word for word, with runs of whitespace collapsed, at the file its coordinate names (executed: a Python comparison over `changelog.md`, `frame/plan.md` and `gaps.md` printed True for each).

What matched: the fix diff adds no test, so no new case is read against its group. `frame/design.md` *Rule changes* holds the no-change block, and the `chain_check.py --worktree` run printed no notice at a line of it. Read and executed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the overlap rows for #1440, #1442 and #1444, and "none meets" for #1439 and #1441, match those items' real diffs; they rest on issue bodies and guessed file lists | `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/frame/plan.md:36-44` | the orchestrator, reading the six plans, as `frame/design.md` G16 names |
| The full suite, the repository-wide lint and the format check at `65651238`; contract rule 2 keeps them out of a round | `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/gaps.md:7` | the orchestrator, at the broad gate |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_the_set_a_work_item_always_has.py tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_docs_line_wrap.py -q -p no:randomly`, in the clone at `65651238` | exit 0, 149 passed |
| `GITHUB_EVENT_PATH=<scratch>/ready-event.json python3 skills/code-review/scripts/chain_check.py --baseline 94d04d30 --root <clone>`, with a payload reading `{"pull_request": {"draft": false}}`, in the clone at `65651238` | exit 1; among its refusals, the two lines naming `705d6e02` and `a2098f95` as carrying `Seal-Routing: 1794178396` with no declaration naming that work item; the payload file was removed afterwards |
