# Review round 1: 1793714292-one-kind-of-finding-recurs-across-review-rounds

```seal
target: 16431cc29 against release/v0.31.0
```

The target is the branch `feat/1020-one-kind-of-finding-recurs-across-review-rounds` against `release/v0.31.0` at `5d89ba07a`, read in a `--no-local` clone at `16431cc29`. Outside `seal/`, the diff changes `docs/releasing/release-checklist.md` *2b. Settle what earlier releases left behind*, the second paragraph of `docs/running/the-run.md` *The run*, and the `version` in `.claude-plugin/plugin.json`. Inside `seal/`, it adds the work item's frame, phase record, closing memo and changelog fragment.

No earlier round exists, so nothing is carried from one. Two facts are carried from the framer's records and not established again here. The first is which chains of three or more findings the two windows hold, from #1038's *Command C11* (G8) and the framer's probe over 34 pull requests (G10). The second is #1203's judgment rows, from G8's *Instances C11*. Every verdict below is this round's own.

The axes fixed before starting were these. The first is compliance of the three sentences with `frame/design.md` *Scope* items 1 to 3 and with the documents they cite. The second is whether every other statement of each fact moved with it (contract rule 19). The third is whether the frame's grounds G8 to G10, and the changelog fragment that rests on them, hold at the records they cite. The fourth is the issue's *Done when* and its comments against the frame's decision to build nothing. The fifth is the version move against S4. The table's code axes (inputs, authorization, query scope, concurrency, security and the rest) have no subject in a diff of prose and one version string.

## Findings

### 1. The checklist's new step files an issue with no home named, while citing the table row that has that issue name the home

```seal
severity: should
location: `docs/releasing/release-checklist.md:98-102`, `seal/threads/1793714292-one-kind-of-finding-recurs-across-review-rounds/frame/design.md:27`, `seal/threads/1793714292-one-kind-of-finding-recurs-across-review-rounds/changelog.md:5`
evidence: read `docs/releasing/release-checklist.md:98-102`, `skills/implement/orchestration.md:486`
```

Why it matters: the settling session reads this step and acts on it. It files the issue the step describes, and the step says that issue "is the home `skills/implement/orchestration.md` *Orchestrator: where a decision or a lesson is written* gives a lesson that no work item in progress changes" (`docs/releasing/release-checklist.md:100-102`). That table's row, at `skills/implement/orchestration.md:486`, reads "a lesson or a decision whose home no work item in progress changes". It gives "an issue that names the home". The checklist misstates the row in two ways. First, it drops "whose home", so it describes a lesson no work item changes, where the row describes a lesson whose home no work item changes. Second, the issue it describes names "each such stale copy and the record it stood in" and never the home. A record in a work item is removed by the settle, so it cannot be that home. A session that follows the step files an issue the cited row does not describe, and nobody is told which file the lesson should change. The frame's *Scope* item 1 (`frame/design.md:27`) states the same paraphrase, and the changelog's third entry (`changelog.md:5`) states the same issue contents. So the defect comes from the frame and not from the build. `trail/phases/phase-1.md:37-41` records what the phase built at `df433eee2` and is history, so the fix pass need not rewrite it.

The fix makes the issue name the home and quotes the row's condition as the row states it. In `docs/releasing/release-checklist.md`, lines 98 to 102 become:

```markdown
copy. The count is `worse` only where stale copies are what kept it up. Where it
is, the session files one issue that names each such stale copy, the record it
stood in, and the file the lesson belongs in. That issue is the home
`skills/implement/orchestration.md` *Orchestrator: where a decision or a lesson is
written* gives a lesson whose home no work item in progress changes. The step is
this repository's and ships to no user: the plugin's
```

The two other statements need the same change. `frame/design.md` *Scope* item 1 is the framer's or the orchestrator's to fold, since `agents/crafter.md` *Job* names no write to it. Its second and third sentences become "In its place, the settling session files one issue that names each stale copy that kept the count up, the record it stood in, and the file the lesson belongs in. That is the home `skills/implement/orchestration.md` *Orchestrator: where a decision or a lesson is written* gives a lesson whose home no work item in progress changes." In `changelog.md` entry 3, the last sentence becomes "Where stale copies kept the count up, the settling session now files one issue that names each such stale copy, the record it stood in, and the file the lesson belongs in." The replacement lines in the checklist keep the paragraph's `check: tests/github/test_finding_counts.py` line and do not change it. That case reads the count's script and not this sentence.

```seal
verdict: fixed d4697987e
answer: The finding holds against `skills/implement/orchestration.md:486`, where the row's left cell is a lesson whose home no work item in progress changes and its right cell, where the orchestrator writes it, is an issue that names the home. The paste-ready text was not applied as given: its sentence "That issue is the home ... gives" still makes the issue the home, while the row makes the home a file and the issue the place the lesson is written. The checklist now has the issue name each stale copy, the record it stood in, and the file the lesson belongs in, and says that an issue naming that file is where the cited section writes a lesson whose home no work item in progress changes; the paragraph's last sentence was reflowed and its words kept. The changelog's third entry and the first row of `gaps.md` *Not verified*, which state the same issue contents, moved with it. `frame/design.md:27` is left for the orchestrator to fold, and `trail/phases/phase-1.md:37-38` stands as the record of what phase 1 built at `df433eee2`. `tests/github/test_finding_counts.py`, the paragraph's check target, reads the count's script and no sentence of the step, so it needed no change; it and the cited-section, line-wrap and paste cases pass at `d4697987e`.
```

## Confirmations

```seal
confirms: none
```
What matched: *Scope* item 1's removal. The claim is that no shipped text still names #1020's check. Running `git grep -n '#1020' -- docs skills agents templates README.md CONTRIBUTING.md hooks bin` at `16431cc29` printed nothing and exited 1 (executed). Running `git grep -n -i -e 'recurrence' -e 'recurring finding'` over the same trees printed one line, `skills/settle/SKILL.md:133`, which is about settle rows and not about a check to come (executed). The step at `docs/releasing/release-checklist.md:98-102` now names an issue to file and no check (read). Finding 1 is about what that issue holds.

```seal
confirms: none
```
What matched: *Scope* item 2. The claim is that the first paragraph of *The run* states the zero-finding round with its reason, and the second paragraph no longer states it. `docs/running/the-run.md:12-14` reads "A round opening nothing that needs a fix does not count toward the cap: the cap stops a loop that is not converging, and such a round is the loop having converged" (read). `git grep -n 'loop having converged'` outside `seal/threads` printed `docs/running/the-run.md:14` alone (executed). The removed sentence stood before the regression sentence, so "Every such decision" follows the regression sentence as it did before the edit and refers to the same decisions (read, `git diff 5d89ba07a..16431cc29 -- docs/running/the-run.md`). The other statements of the same fact, at `skills/code-review/orchestration.md:125-129` and `README.md:207`, stand by the frame's *Out* list, and `gaps.md` *Not done* names both.

```seal
confirms: none
```
What matched: *Scope* item 3. The claim is that the regression sentence now cites a heading the core holds, whose table holds the invariant. `skills/core/SKILL.md:95` opens **Judgment is not licence to skip a party.**, and its table row at `:104`, *No fix that no round reads*, protects that "every change after the last round is read by a round" (read). The new wording, "no fix goes unread by a round", says the same as that row. `git grep -n -i 'table b'` outside `seal/threads` printed only lines that read "table below" (executed). `tests/behaviour/test_a_cited_section_stands_in_its_file.py` passes at `16431cc29` (executed, the narrow run under *Probes*).

```seal
confirms: none
```
What matched: the changelog's first entry and the second row of `gaps.md` *Not verified*. The crafter claimed that the entry rests on the framer's readings of G8 to G10 and did not re-run them. This round read each chain the claim covers at its pull request's head, fetched as `pull/<n>/head` in the clone (executed: `git show pr<n>:<work item>/frame/plan.md` and each `trail/rounds/round-*.md`). #1230's row "After round 3, the third finding round" names the signal of fixes chasing one mechanism and orders the class enumerated. #1241's row that files #1240 follows its round 3, where the third finding of the chain stands. In G10's five, #1252, #1276, #1284 and #1287 each hold a row at their third finding round, and #1320 holds one at round 3, its third finding. #1201 merged at 2026-10-31T07:14:33Z and #1202, whose squash is `96c11614`, at 07:16:17Z (executed: `gh pr view 1201 --json mergedAt`, `gh pr view 1202 --json mergedAt`). So #1201's chain ran before the paragraph, as G9 states. The ancestry command G9 cites, `git merge-base --is-ancestor 96c11614 HEAD`, is true of any later HEAD and does not settle that order, but the merge times do. #1038's C11 grounds name #1230's fourth instance as one the candidate "would have stopped". #1230's round 3 row asked what the exchange would ask: whether the findings are one class, and whether the fix enumerates it. So the entry's "would each have changed none of those chains" holds on that chain as the record shows it. The list of which chains count as three or more is carried from G8 and G10 and is not re-established here, so this confirmation covers seven chains read one by one and not the enumeration.

```seal
confirms: none
```
What matched: the first row of `gaps.md` *Not verified*. The crafter claimed that no case reads the checklist's new sentence. `git grep -n -e 'stale copy' -e 'files one issue' -- tests` printed nothing (executed). No case is owed. The sentence states an act a settling session takes on its own judgment, and a case that held the sentence could hold only its wording. That is the pin `docs/running/what-a-script-gates.md:76` drops: "a case pins a fact a reader acts on; one that pins wording goes" (read).

```seal
confirms: none
```
What matched: the departure from S4 that `trail/phases/phase-1.md:56-63` names. Outside `seal/`, the diff holds only the `version` move to `0.31.0` besides the two documents (executed, `git diff --stat 5d89ba07a..16431cc29`). `08b43c65f` moved 0.30.1 in the same way, changing only `.claude-plugin/plugin.json` beside its fragment (executed, `git show --stat 08b43c65f`). `git grep -n '0\.30\.1'` outside `seal/` and `CHANGELOG.md` printed only the new `plugin.json` line, which reads `0.31.0` (executed). So no second version string was left behind.

```seal
confirms: none
```
What matched: the orchestrator's fold `16431cc29`. `git show 569780eff:seal/threads/1793521558-the-record-decides-each-proposed-verifier/trail/phases/phase-2.md` holds the row C11 at line 26 and *Instances C11* at line 352, as G8 cites them (executed). `tests/text/test_a_cited_commit_outlives_the_squash.py` passes at `16431cc29` (executed, the narrow run). G7's claim was also checked: the four other unsettled designs under `seal/threads/` each print `- nothing` under `## Rule changes` (executed).

```seal
confirms: none
```
What matched: the frame against #1020's *Done when* and its comments (read: `gh issue view 1020 --json body,comments`). `frame/design.md:36` answers each bullet. The first, a check seen red on fixture records, falls with *Scope* item 4. The second has its homes in contract rule 12 and in `skills/code-review/orchestration.md:140` and `:155`, which hold the signal and the paragraph G4 quotes (read). The third holds inside *The run* after item 2. The comment of 2026-10-30 calls the exchange "the case to make" where records-alone findings fall and shipped-text recurrences remain. Both conditions hold on G8's and G10's counts. `frame/plan.md:20` makes that case and weighs it, as the same comment asks ("Compare it ... on cost and on what each catches"). The comment of 2026-11-01 reads "build" on #1201's chain, which ran with no judgment row. The merge times above place that chain before `96c11614`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether #1020 closes with its first *Done when* bullet unmet. The frame declines the check on the record's grounds, against the comment of 2026-11-01 that reads "build". This round found the grounds hold on the record, but whether the issue's decision is honoured is a reading against the issue | `frame/plan.md:38`, `frame/design.md:36` | the sealer, reading the accounts against the issue |
| Whether G8's and G10's lists of chains of three or more are whole. The framer's probe over 34 pull requests was not run again, and only the chains it names were read | `frame/design.md:16-18` | the sealer, in its sample of the framer's claims |
| The suite and the lint across the repository: `unverified`, since rule 2 keeps the broad gate from every agent | `seal/config.md` `Broad gate` row | the orchestrator, at its broad run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_finding_counts.py tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_a_cited_commit_outlives_the_squash.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_the_set_a_work_item_always_has.py -q`, in the clone at `16431cc29` | 118 passed, exit 0 |
| `git grep -n '#1020' -- docs skills agents templates README.md CONTRIBUTING.md hooks bin` | nothing printed, exit 1 |
| `git fetch gh pull/<n>/head:pr<n>` for 1230, 1241, 1252, 1276, 1284, 1287 and 1320, then `git show pr<n>:` over each plan's *Judgments of the run* and each round's `regression:` and `reopens:` lines | each chain's row stands at or before its third finding round, as the confirmation above gives them |
| `gh pr view 1201 --json mergedAt`, `gh pr view 1202 --json mergedAt` | 2026-10-31T07:14:33Z and 2026-10-31T07:16:17Z |
