# Review round 1: 1793538228-the-release-pr-opens-after-the-last-merge

```seal
target: 583ff676 against release/v0.27.3
```

No earlier round exists, so no fact is carried into this one: every coordinate below was opened in this round. No `seal/parity.md` is declared, and the diff changes no path outside `seal/`, so the round block holds no `original:` line.

## Findings

### 1. The rule change and the fragment state that every early run re-tests a tree already tested, and 0.27.2's own release refutes it

```seal
severity: should
location: `seal/threads/1793538228-the-release-pr-opens-after-the-last-merge/frame/design.md:67-73`, `seal/threads/1793538228-the-release-pr-opens-after-the-last-merge/frame/design.md:24`, `seal/threads/1793538228-the-release-pr-opens-after-the-last-merge/changelog.md:3`, `seal/threads/1793538228-the-release-pr-opens-after-the-last-merge/frame/plan.md:11-16`, `seal/threads/1793538228-the-release-pr-opens-after-the-last-merge/frame/plan.md:23`
evidence: executed `gh pr list --repo MichaelYcJo/AgenticSeal --base release/v0.27.2 --state merged --json number,mergedAt,headRefOid`, `gh run list --repo MichaelYcJo/AgenticSeal --workflow tests --commit HEAD_REF_OID --json createdAt,event,conclusion`, `gh run list --repo MichaelYcJo/AgenticSeal --branch release/v0.27.2 --workflow tests --json createdAt,headSha,conclusion,event`
```

Why it matters: the `to` of *Rule changes* is the text the settle writes into `docs/release-checklist.md` *5*. It says that a release pull request opened early "reads a tree the merged pull request already tested on its own merge ref" (`frame/design.md:67-70`). The fragment shipped in the release note says "each push ran `tests` on a tree its own pull request had already tested" (`changelog.md:3`). Scope item 1 says "the early runs re-test trees already tested" (`frame/design.md:24`). Plan A2 checks the premise that keeps the old step and concludes that "The only thing they would catch earlier is a hotfix on `main`" (`frame/plan.md:23`).

That holds only where the merged pull request's last `tests` run started after every earlier merge into the branch. A `pull_request` run reads the head merged into the base as the base stood when the run started. GitHub starts no new run when the base moves (`.github/workflows/test.yml:3-12`, read). On 0.27.2 the condition failed once:

- #1250 merged at 09:48:00Z.
- #1252's last `tests` run started at 09:43:26Z and was never re-run. #1252 then merged at 09:48:15Z as `a8269d90`.
- No work item pull request tested `a8269d90`, which holds #1250 and #1252 together. The release pull request's run at 09:48:20Z on `a8269d90` was the first to read that tree. It passed.

The other five merges had their last run after the merge before them (executed, *Probes*).

The decision still stands. The one run after the last merge reads that combination too, later, as it reads a hotfix later. What is wrong is the stated reason. An agent that reads the settled step learns that the early runs can catch nothing, and a defect two work items make only together is a second thing they catch earlier. Plan A2 checked its premise against one kind of catch and missed this one. The plan's failure scenarios do not list it either (`frame/plan.md:11-16`). The changelog carries the same wrong fact to users.

The `to`, lines 67 to 73, rewritten, indented as the value is, each line 73 columns or fewer once the indent goes:

```markdown
    A release pull request opened earlier takes each later squash merge into
    the branch as a push to its head. Its `tests` run then reads a tree the
    merged pull request tested on its own merge ref only where nothing else
    merged into the branch after that test started, since `main` stays where
    the release branch was cut unless a hotfix moves it. Where something did,
    the run is the first to read the two together, and the one run after the
    last merge reads them together as well. Opened after the last merge, it
    runs `tests` once, on the tree the release ships, and what runs only on a
    pull request into `main` answers once: `release-report`, and the
    `hygiene` workflow's version and milestone steps.
```

`frame/design.md:24`, the reason in scope item 1:

```markdown
It also says why: an early run mostly re-tests a tree its own pull request already tested, and the one run after the last merge reads every tree the early runs would have read first, the tree that ships.
```

`changelog.md:3`, the sentence that starts "Each later squash merge" and the sentence after it:

```markdown
Each later squash merge into the branch then reached it as a push, and each push ran `tests` again, mostly on a tree its own pull request had already tested. On 0.27.2's release pull request, #1251, `tests` ran six times, and only the last run read the tree that shipped. One earlier run, at #1252's merge, was the first to read #1250 and #1252 together, because #1252's last run had started before #1250 merged. The run after the last merge reads such a pair as well, later.
```

`frame/plan.md:23`, the verdict cell of A2, from "The only thing":

```markdown
They catch two things earlier, and both show at the one run after the last merge instead: a hotfix on `main` (*Technical context*), which 0.27.2 had none of, and a defect two work items make only together where the later one's last run started before the earlier one merged, as #1252's did after #1250 on 0.27.2, where the run passed
```

`frame/plan.md`, a fifth failure scenario under *Technical context*:

```markdown
- Two work items each pass their own pull request's `tests`, and the later one's last run started before the earlier one merged. A defect they make only together then shows at the release pull request's one run, and not at the merge that made it. Its repair is one more pull request into the release branch before the merge, as with a hotfix.
```

```seal
verdict: fixed 4e4f7f3c
answer: The finding holds; `gh pr list --base release/v0.27.2` and `gh run list --commit` for #1250 and #1252 were re-run in the fix pass and give the same times: #1250 merged at 09:48:00Z, and #1252's last run started at 09:43:26Z before it merged at 09:48:15Z. 4e4f7f3c applies the paste-ready text to `changelog.md:3`, and corrects the same fact in the process row's Why cell at `changelog.md:9` ("over trees already tested" became "mostly over trees already tested; on 0.27.2 five of six runs came before the last merge"). The frame locations, `frame/design.md` *Rule changes* `to` and *Scope* item 1, `frame/plan.md` A2 and the fifth failure scenario, were rewritten by the orchestrator in 99642896.
```

### 2. The step reads the moment from the milestone check's exit code, and the script exits 0 in two shapes where it read no milestone

```seal
severity: should
location: `seal/threads/1793538228-the-release-pr-opens-after-the-last-merge/frame/design.md:77-83`, `seal/threads/1793538228-the-release-pr-opens-after-the-last-merge/changelog.md:3`, `seal/threads/1793538228-the-release-pr-opens-after-the-last-merge/changelog.md:9`
evidence: read `.github/scripts/release_completeness_check.py:355-401`, `seal/threads/1793538228-the-release-pr-opens-after-the-last-merge/frame/design.md:77-83`
```

Why it matters: the `to` makes "the release pull request's own milestone check exits 0" one of the two readings that say the last work item has merged (`frame/design.md:77-81`). The fragment says the same: "which must exit 0" (`changelog.md:3`, and the process row at `changelog.md:9`). The script answers exit 0 for more than that. Taking `main()` apart by its return statements (`release_completeness_check.py:355-401`, read) gives every exit-0 path:

- `:358-363` returns 0 when `HEAD_BRANCH` is not a `release/vX.Y.Z` name. It prints "nothing to judge" and reads no milestone. A mistyped branch, such as one without the `v`, lands here.
- `:381-390` returns 0 when no milestone of that title exists and no `feat:` failed. It prints a warning that the reading verified nothing.
- `:401` returns 0 when `M \ D` and `L \ D` are empty and no `feat:` failed. This is the only path that reads the moment.

Design G9 found a fourth way to read nothing, the redirected repository name, by one probe. The `to` closes that one by reading `REPO` from `gh repo view`. The other two stay open. An orchestrator that reads only the exit code, as the `to` tells it to, opens the release pull request on either of them while work still merges. That is the cost this work item removes. The script exits 1 for two reasons other than `M \ D`: a patch carrying a `feat:` (`:376-379`, then `:401`), and `L \ D` (`judge`). The `to` names only the milestone refusal, so an orchestrator waiting for exit 0 is not told that those two errors name their own repair.

The `to`, lines 77 to 83, rewritten:

```markdown
    sees it. And the release pull request's own milestone check exits 0 and
    prints its `M (open in 'release: X.Y.Z')` line, run as
    `python3 .github/scripts/release_completeness_check.py` with
    `HEAD_BRANCH=release/vX.Y.Z`, `HEAD_SHA=origin/release/vX.Y.Z` and `REPO`
    set to what `gh repo view --json nameWithOwner --jq .nameWithOwner`
    prints. Exit 0 alone does not read the moment: the script also exits 0
    when the branch name is not a release name and when no milestone of that
    title exists, and then prints a line saying so in place of the `M` line.
    That check fails the release pull request while the milestone claims an
    issue the branch does not carry, and names each one. An issue it names
    that no branch is building is step 0's milestone box, left undone. Where
    it fails for another reason, a patch carrying a `feat:` or a label on an
    issue the branch does not carry, its `::error::` line names the repair.
```

`changelog.md:3`, the clause "which must exit 0", becomes "which must exit 0 and print its `M (open in ...)` line". In the process row at `changelog.md:9`, "exiting 0" becomes "exiting 0 with its `M` line printed".

```seal
verdict: fixed 4e4f7f3c
answer: The finding holds; `.github/scripts/release_completeness_check.py:362` prints the "nothing to judge" line and `:284` the `M (open in ...)` line, read in the fix pass. 4e4f7f3c applies the paste-ready text to `changelog.md:3` ("which must exit 0 and print its `M (open in ...)` line") and to the process row at `changelog.md:9` ("exiting 0 with its `M` line printed"). The frame location, the `to` of `frame/design.md` *Rule changes*, was rewritten by the orchestrator in 99642896.
```

## Confirmations

```seal
confirms: none
```
What matched: the departure from the issue's *Done when* holds. The issue asks for a rule change in `docs/branch-and-release.md` because that document "states the same". It does not. I read the whole file at the base. Its *Cutting a release* hands the day-of steps to `docs/release-checklist.md` (`docs/branch-and-release.md:9-10`). Its mentions of the release pull request, at `:41`, `:63` and `:292`, concern the version step, the title line and the issue numbers, and none says when it opens (read). I searched the tree outside `seal/threads/` for every spelling of the release pull request and of a pull request into `main` (executed, *Probes*). Every hit was read: `docs/the-broad-gate.md:53`, `docs/the-review-record.md:131`, `docs/issues-and-milestones.md:200`, `skills/implement/orchestration.md:331`, `CONTRIBUTING.md:150` and the workflow and script comments. Only `docs/release-checklist.md:106-113` states a moment. A copy in `docs/branch-and-release.md` would give the fact a second source, so design G3 and plan A7 hold against `skills/core/SKILL.md` *The rule a mechanism is kept against*. The issue's two orchestration skills also state no moment. This search is a sample over spellings, as design G2 says of its own.

```seal
confirms: none
```
What matched: the `from` of *Rule changes* (`frame/design.md:54-61`) is word for word `docs/release-checklist.md:106-113` at the base `5f0cf7a7` (read). The modules that read a pending design or a work item's set pass at `583ff676`: `tests/github/test_rules.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and `tests/behaviour/test_the_set_a_work_item_always_has.py`, 125 passed, exit 0 (executed). I did not re-run the crafter's `rule_changes.py#parse` probe or its two `gaps.md` modules. Its claim of one `change` and 544 passed is the crafter's.

```seal
confirms: none
```
What matched: the 0.27.2 figures in design G7 and `changelog.md:3`. `tests` ran six times on #1251: `ad5246ce`, `161a42aa` cancelled, `a8269d90`, `94b03636`, `569780ef` and `783a7fe8`, and none failed (executed). On every `hygiene` run before `783a7fe8`, the failing step was the milestone step, "the milestone this release claims is the work it carries, and a patch carries no feat", and it passed at `783a7fe8` (executed). So the fragment's "the `hygiene` workflow's milestone step was red on every run before the last" names the right step.

```seal
confirms: none
```
What matched: the workflow facts the `to` states. `tests` runs on default `pull_request` events, and a newer push cancels the run in progress (`.github/workflows/test.yml:3-21`, read). `release-report` runs only where `github.base_ref == 'main'` (`.github/workflows/test.yml:257-259`, read). The `hygiene` version step and milestone step each exit 0 on any base but `main` (`.github/workflows/hygiene.yml:77-79`, `.github/workflows/hygiene.yml:156-158`, read). The step's inputs `HEAD_BRANCH`, `HEAD_SHA`, `REPO` and the default `BASE` are what `main()` reads (`.github/scripts/release_completeness_check.py:356-371`, read).

```seal
confirms: none
```
What matched: the `check:` line stays, as design G11 and plan A9 say. `tests/github/test_release_completeness_check.py` reads the `M \ D` refusal, and the `to` still states that refusal (read). The step's other new sentences are an orchestrator's act, and scenario S1 says no case can run one.

```seal
confirms: none
```
What matched: the phase record's departure on the process row (`trail/phases/phase-1.md:13`). `docs/the-record-layout.md` *A change writes fragments, never a shared file* owes a row where the diff changes one of five kinds of file. This diff changes none of them, and the section bars no row elsewhere (read). The row has the four columns of `templates/records/process.md` (read). The orchestrator's row at `313fcf67` (`frame/plan.md:46`) matches *Operational impact* (`frame/plan.md:40`). Holding the opening until this design merges is later than the base's step says, and the row names that cost and its ground (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and format at `583ff676`. The crafter's hand-back labels them `unverified`, and that label is honest: no agent runs them (contract rule 2) | the branch at `583ff676` | the orchestrator, through `seal gate`, before the sealer's spawn |
| Whether 0.27.3's release pull request runs `tests` once, with no `pull_request` run before the last merge (design S2, `frame/questions.md` Q1) | `gaps.md:7` | the orchestrator of 0.27.3's release, with `gh run list --branch release/v0.27.3` after the merge into `main` |
| Who moves `.claude-plugin/plugin.json` from 0.27.2 to 0.27.3. It stands at 0.27.2 at the base, and #1269 is open into `release/v0.27.3` beside this branch | `frame/design.md:34` | the orchestrator, in the first pull request into `release/v0.27.3` to merge |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/github/test_rules.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_the_set_a_work_item_always_has.py`, in a scratch clone at `583ff676` | 125 passed, exit 0 |
| `gh pr list --repo MichaelYcJo/AgenticSeal --base release/v0.27.2 --state merged --json number,mergedAt,headRefOid`, then for each head `gh run list --repo MichaelYcJo/AgenticSeal --workflow tests --commit HEAD_REF_OID --json createdAt,event,conclusion`, keeping the last `pull_request` run | #1248 merged 09:26:52Z, last run 09:18:00Z; #1250 09:48:00Z, 09:30:12Z; #1252 09:48:15Z, 09:43:26Z; #1253 10:20:11Z, 10:12:20Z; #1257 11:35:14Z, 10:33:40Z; #1261 12:42:18Z, 12:08:47Z. #1252's last run started before #1250 merged |
| `gh run list --repo MichaelYcJo/AgenticSeal --branch release/v0.27.2 --workflow tests --json createdAt,headSha,conclusion,event` | six `pull_request` runs: `ad5246ce` 09:33:44Z success, `161a42aa` cancelled, `a8269d90` 09:48:20Z success, `94b03636` success, `569780ef` success, `783a7fe8` success |
| `gh run view RUN_ID --repo MichaelYcJo/AgenticSeal --json headSha,conclusion,event,jobs` for each `hygiene` run on `release/v0.27.2` | seven runs before `783a7fe8` failed, each at the milestone step alone; the run at `783a7fe8` passed |
| `git grep -n -i -E` over the spellings of the release pull request and a pull request into `main`, outside `seal/threads/` and `tests/` | the hits named under *Confirmations*; only `docs/release-checklist.md:106-113` states when the release pull request opens |
