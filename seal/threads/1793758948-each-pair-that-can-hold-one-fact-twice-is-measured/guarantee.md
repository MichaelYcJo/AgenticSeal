# Guarantee: 1793758948-each-pair-that-can-hold-one-fact-twice-is-measured

| Field | Value |
|---|---|
| Broad gate | 4df5976b1 against 94635718e |

The base `release/v0.31.1` resolves through `release/v0.31.1@{upstream}` to `94635718ea4a79569ac612bcb814114000028be3` (executed: `git rev-parse --verify --quiet`). `trail/gate.md`'s last `seal` block names `4df5976b1`. That commit is an ancestor of HEAD, and the one commit after it, 8ca92d966, touches only `trail/gate.md` (executed: `git merge-base --is-ancestor`, and `git log --no-merges --name-only 4df5976b1..HEAD ^94635718e`). `seal pr-body <item> --body <file> --check` exited 0 with the installed plugin's `seal` and with the tree's `bin/seal` (executed). `seal/parity.md` is not tracked, so no parity comparison is owed (executed: `git ls-files seal/parity.md` printed nothing).

## Claims re-run

The sample comes from the four phase records, run at `94635718e`. Each block was extracted unchanged from the record at HEAD and run with `bash` from the repository, against a fresh `git archive` copy under a temporary directory that was removed afterwards. Round 1 ran every block except the *Command tracker* searches, so this sample takes the blocks whose rows hold a drift, and their setups.

| Claim | Source | Command | Result |
|---|---|---|---|
| The probe reads the tree as `passages.words` does, and the parts have their stated sizes | `trail/phases/phase-1.md:545` | phase 1 *Command setup* | holds (executed): `prose files 457; tokens differs from words in 0`, `P1 24` … `P10 248`, `generated eval files 247; graders and prompts 197` |
| R9's counts and D2's ground: `CLAUDE.md` names none of the four homes | `trail/phases/phase-1.md:599`, `:33` | *Command R9* | holds (executed): `R9: 6 passages over 930 file pairs`, `pins 27 in 12 modules, corpus P5`, `0` |
| R11's drift, D1: the *Layout* entry lists three items, and `seal/config.md` holds five rows | `trail/phases/phase-1.md:617`, `:727` | *Command R11*; `git show 94635718e:seal/README.md` lines 85 to 90 and `seal/config.md` lines 7 to 13 | holds (executed, read): `R11: 0 passages over 3 file pairs`. The entry names `Commit and pull request language`, `Record language` and `Mode`. The file holds `Mode`, `Broad gate`, `Document token ceiling`, `Pull request seal mark` and `Release note seal mark` |
| R16's passages, and the 17 fixture cases are their generator's output byte for byte | `trail/phases/phase-1.md:655` | *Command R16* | holds (executed): `R16: 4 passages over 78 file pairs`, `generator exit 0`, no `differs:` line, `17` |
| The `seen red`: the plan's named case fails, naming this work item, while `gaps.md` is absent | `trail/phases/phase-1.md:804` | clone at `<scratchpad>/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/at-base/`, at HEAD with only `gaps.md` removed: `bin/test tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview -q -p no:xdist` | holds (executed): exit 1, `1 failed`. The failing line reads `work items with no closing overview: ['1793758948-each-pair-that-can-hold-one-fact-twice-is-measured']`. With `gaps.md` restored, that case and `tests/text/test_a_cited_commit_outlives_the_squash.py` give exit 0, `13 passed`. The clone was removed |
| R4's drift, D3: 45 orphans in P8, 32 units held | `trail/phases/phase-2.md:409` | phase 2 *Command setup*; *Command R4* | holds (executed): `units 80 (shapes 1, headings 51, headers 26, markers 2); held in P8 32`, `orphans in P8 45 distinct (42 headings, 3 markers); headings near a template heading 5; …` |
| R12's drift, D4: the marker agrees, and the `--worktree` row cites a docstring warning | `trail/phases/phase-2.md:442` | *Command R12* | holds (executed): `R12: 1 passages over 234 file pairs`, `equal` for both README files, `item names P8 holds 9; in the template 8; in seal/config.md 5; …`. Line 42 argues "the axis `read_record`'s docstring warns about" |
| F8's counts | `trail/phases/phase-2.md:452` | *Command files*, second line | holds (executed): `ids 6323; naming no test module 0; naming no function of their module 25; their seconds 7.6 of 1614.4 (0.47%); test functions 3552 in 149 modules, no id naming 44` |
| The other holders of F1, F3, F5, F6, F9 and F11, and the grounds of D5, D6, D7 and D8 | `trail/phases/phase-2.md:470` | *Command F* | holds (executed): `labels: gate`, `7` bold items, `docs/releasing/branch-and-release.md` `:204`, `marketplace.json` `:9` and `:15`, `2` install lines per README edition, `FLOOR = (3, 12)`, `ruff.toml:40`, `CONTRIBUTING.md:126`, `tests/hooks/test_launch.py:210`, `tests/censuses.py:761` and the `select` line |
| R19's counts, and the 13 spans of D11's and D2's 12 drifted statements | `trail/phases/phase-3.md:478`, `:551`-`:562` | phase 3 *Command setup*; *Command R19* | holds (executed): `R19 path:line coordinates 2; path#name coordinates 92; not resolving 3`, `R19 docstring and comment spans 421; ELSEWHERE 8; NO 60; NOWHERE 17; PATH 5; in 58; module 233; own 40`, `R19 module docstring spans 209; …`, `blocks … 9`, `figure candidates … 120`. Each of the 13 spans is listed `NO SUCH MODULE`, `PATH NOT RESOLVED` or `NOWHERE` at the coordinate the instance names. `tests/text/test_the_rules_claude_md_names_have_one_home.py:48-49` and `tests/text/test_review_axes.py:103-107` were opened at `94635718e` and read as the instances say (read) |
| The commit that removed each cited module or case | `trail/phases/phase-3.md:510` | phase 3 *Command history* | holds (executed): every commit and every pull request number the record states |
| E1 to E4: block counts agree, and E1's citations differ only in the `.ko.md` editions | `trail/phases/phase-4.md:148` | phase 4 *Command setup*; *Command E* | holds (executed): the four `E<n> sections` lines as stated; the four `.ko.md` citation lines for E1, and nothing for E2 to E4 |
| D12's ground: both counts have stood since #123 | `trail/phases/phase-4.md:157` | phase 4 *Command history* | holds (executed): `ab14194b1`, `438cffe4a`, `28: … Three runs edited the clone`, `49: the first four edited the wrong copy` |
| Design S3, S5 and G10 at HEAD | `trail/phases/phase-4.md:170` | *Command checks*, run from the repository at 8ca92d966 | holds (executed): nothing for the labels, `0`, `1` |
| D1 to D12 were filed as #1334 to #1345, each with its draft's title and body and the milestone it proposes | `frame/plan.md:73` | `gh issue view <N> --json number,title,milestone,state,body` for 1334 to 1345, compared with each `#### D<n>` section of the phase records at HEAD | holds (executed): all 12 are open. Each title equals its draft's title. Each draft's text after `**Body.**` stands verbatim in its issue's body, followed by a line naming the draft. Each milestone is the one its draft proposes: `backlog: review chain & agents` for #1336, `backlog: gates & hooks` for #1338, `backlog: release & platform` for #1343, and `backlog: docs drift` for the other nine |
| D10's two drifts still stand in the tracker | `trail/phases/phase-3.md:532`, `:538` | `gh api …/milestones?state=all` for `release: 0.32.0`'s description; `gh issue view 1020`; `gh issue view 1236` | holds (executed): the description says "every kept candidate but #1020, which stays in release: 0.30.0". #1020 is in `release: 0.31.0`. #1236's *Order* line says `release: 0.29.0` |
| Round 1, finding 1, `fixed 8caff5e2c` | `trail/rounds/round-1.md:68` | `git show --name-only 8caff5e2c`; read at HEAD | holds (executed, read): the commit touches only `gaps.md`, `trail/phases/phase-1.md` and `trail/phases/phase-3.md` of this work item. D2's *What is wrong*, *Done when* and *Answers* (`phase-1.md:792`, `:796`, `:800`) carry what the finding asked. `phase-3.md:561` ends "whose body names it". `gaps.md` holds no paragraph leaving the sentence to the filing. #1335's body carries the sentence |
| Round 1, finding 2, `fixed d2cae5644`, and the four plan sentences its answer named | `trail/rounds/round-1.md:118`, `frame/plan.md:72` | `git show --name-only d2cae5644`; read at HEAD | holds (executed, read): the commit touches only `frame/design.md` and `frame/plan.md`. `design.md:28`, `:52`, `:63` and `:73` carry the finding's text. `plan.md:5`, `:14` and `:16`, and phase 1's *Verified by* cell at `:47`, now say R18 is counted against the tracker |
| Nothing outside the work item changed, before or after the round | design S5, `frame/design.md:55` | `git diff --name-only 94635718e..HEAD \| grep -c -v '^<item>/'`; `git log --name-only 654c4a374..HEAD` | holds (executed): `0`. No commit after round 1's target touches a path outside the work item's directory |
| `seal/follow-up.md:45` is blank inside the table, and the four rows below it render as a paragraph | pull request body, *Left for the owner* | `git show 94635718e:seal/follow-up.md \| sed -n '43,49p'`; `git diff --quiet 94635718e HEAD -- seal/follow-up.md` | holds (executed): line 45 is blank and is followed by four `\|` rows, and HEAD leaves the file unchanged. That the rows render as a paragraph is phase 1's `markdown-it-py` reading, and was not re-run here (read) |

Not re-run here: *Command R18*, because filing #1334 to #1345 changed the tracker after the moment its row states. Round 1 ran it at `2026-11-04T04:40:25Z` (read: `trail/rounds/round-1.md:132`). Also not re-run: the four *Command tracker* keyword searches, which read the tracker of their own moment, and the blocks of R1 to R3, R5 to R8, R10, R13 to R15, R17, R20 and R21. Round 1 ran those blocks (read: `trail/rounds/round-1.md:127`). The suite count that the pull request body quotes from the broad run, `6322 passed · 12 skipped`, is not in `trail/gate.md`, and this run did not see it (unverified; the orchestrator, whose `seal gate --record` printed it, answers it).

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | Each pair R1 to R21, file F1 to F11 and edition pair E1 to E4 is measured at `94635718e`, R18 against the tracker. Each drift is drafted, or named under the open issue that holds it. Nothing is repaired, and no rule changes. `## Removes` is nothing. There is no changelog fragment (G10) | the issue's *Scope*, *Rule change* and *Done when*, and the owner's comment that moves the item to `release: 0.31.1`; the build; the tree, whose diff is this work item's records alone; G10's sentence, which stands in `docs/layout/the-record-layout.md` *A commit after the build brings its changelog fragment along* (executed: read at `94635718e`) | none. `## Removes` names nothing, and the diff removes nothing |
| the build | 36 rows, one per label, each measured and none closed. Twelve drafts, D1 to D12. The two R16 drifts are named under #1254. `gaps.md` names what stays open | the design's S3, S5 and G10 (executed above); every count in the sample (executed above); #1254 is open in `release: 0.32.0`, and its *Done when* rewrites the section's pass rules and every other statement of them (read: `gh issue view 1254`) | none |
| the last round | Round 1 re-ran every block except the *Command tracker* searches and found two `should`s. The commits it names fixed both in the records | the records at HEAD, which hold both fixes (read above); the fix commits, which touch only this work item's records (executed above) | its own count of what it did not re-run. `trail/rounds/round-1.md:9` and `:127` speak of "the three *Command tracker* keyword searches". Its per-phase list at `:127`, its *Not judged* row at `:172` and the records name four such blocks: `trail/phases/phase-1.md:673`, `phase-2.md:491`, `phase-3.md:512` and `phase-4.md:172`. The miscount changes no claim about the work, since no *Command tracker* block was re-run by the round, and this run re-ran none either |
| the changelog | none is written | design G10, and the tree: the diff changes only this work item's records, which no release note states | none |
| the orchestrator's part of the pull request body | Every pair, file and edition pair is measured and none is closed. There is no fragment. The twelve drafts were filed as #1334 to #1345 with their titles and bodies. #1254 holds R16's two drifts. Q1 is open, and each issue went to its `backlog:` milestone by Q1's default. The prefix is `chore:`. The round's two `should`s were fixed in the records. `seal/follow-up.md:45` is blank and #1337 edits that file. The broad run is the one `trail/gate.md` records | the records and the tree, at every coordinate above; #1337 is D4, whose scope is a row of `seal/follow-up.md`; the issue's title carries `chore:` | "the three keyword tracker searches" in *For the reviewer* repeats round 1's miscount (four blocks, above). The body is not in the tree, so the orchestrator can change it to four without a new audit |

```seal
target: 8ca92d966b260e0c75c30c114e5605fc59f19382 against 94635718ea4a79569ac612bcb814114000028be3
Verdict: sealed
```

## Re-audit at e44456f8c

| Field | Value |
|---|---|
| Broad gate | 4df5976b1 against 94635718e |

Since the block above, two commits landed. f89408963 adds this file, and its text equals the block above's run (executed: `git show f89408963:<item>/guarantee.md \| diff -`). e44456f8c touches only `frame/plan.md`, where it adds the row at `:74`. `trail/gate.md` still names `4df5976b1`, which is an ancestor of HEAD. Only `trail/gate.md`, `guarantee.md` and `frame/plan.md` follow it, all under the work item's directory (executed: `git log --no-merges --name-only 4df5976b1..HEAD ^94635718e`). `seal pr-body <item> --body <file> --check` exited 0 with the installed `seal` and with `bin/seal` (executed).

### Claims re-run

Only `frame/plan.md` changed, so this run re-runs the claims at that file's coordinates and reads the parties again. The claims of the block above stand at coordinates no commit since 8ca92d966 touched.

| Claim | Source | Command | Result |
|---|---|---|---|
| Ten issues were folded into #1346 and closed pointing at it, and #1338 and #1343 stay open | `frame/plan.md:74` | `gh issue view <N> --json number,state,stateReason,milestone,comments` for 1334 to 1346; `gh issue view 1346 --json title,body` | holds (executed): #1334 to #1337, #1339 to #1342, #1344 and #1345 are `CLOSED NOT_PLANNED`. Each one's last comment opens "Folded into #1346 on 2026-11-04 at the owner's request". #1346's *Items* lists those ten. #1338, #1343 and #1346 are open |
| #1338, #1343 and #1346 are in `release: 0.31.2`, created for them | `frame/plan.md:74` | `gh api repos/:owner/:repo/milestones/85` | holds (executed): milestone 85 is `release: 0.31.2`, open, with 3 open issues. Its description names #1346, #1338 and #1343, and says it was created on 2026-11-04 by the owner |
| `release: 0.31.1`'s description names a different purpose | `frame/plan.md:74` | `gh api …/milestones?state=open` | holds (executed): its *Purpose* is removing history and copied passages from the rule text |
| D1 to D12 were filed as #1334 to #1345 | `frame/plan.md:73` | the row is unchanged since the block above; the same `gh issue view` | holds (executed): all twelve exist with the titles the block above compared. Ten are now closed, as the row at `:74` says |

### The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | unchanged since the block above | the issue and the tree, as above | none |
| the build | unchanged since the block above | as above | none |
| the last round | unchanged since the block above | as above | no new disagreement. The "three" that the block above names is still the round's own count |
| the changelog | none is written | design G10; the new commit changes only a record | none |
| the plan, *Judgments of the run* (`frame/plan.md:74`) | The owner asked for the fold and for the milestone, and the orchestrator carried both out | the tracker (executed above) | none |
| the questions (`frame/questions.md:19`) | Q1 is `open`. Its default is that each draft proposes the `backlog:` milestone of its area and is filed there | the tracker as it stood at the filing, and `frame/plan.md:73` | the tracker now: #1338, #1343 and #1346 are in `release: 0.31.2`. `frame/plan.md:74` records the owner's answer, and the body says the owner answered Q1. `docs/layout/the-record-layout.md:152` makes "What only a person could decide, and what was assumed in its place" `frame/questions.md`'s fact, so the record that holds the answer still says it is unanswered, with the default the owner replaced. A settle that decides every open row would put Q1 to the owner again |
| the orchestrator's part of the pull request body | The twelve issues were filed, the ten folded into #1346, and the three are in `release: 0.31.2`. *A decision left to the owner* says Q1 "is open for the owner" and then that "The owner has since answered it". Round 1 skipped "the four *Command tracker* keyword searches". *Left for the owner* says "#1337 edits the same file, so it can take the line with its row" | the tracker on the fold and the milestone (executed above); the round's four tracker blocks | its own Q1 paragraph, which calls Q1 both open and answered. Its *Left for the owner* names #1337 as the issue that edits `seal/follow-up.md`, but #1337 is closed `NOT_PLANNED` and its item now stands in #1346's checklist (executed above) |

```seal
target: e44456f8c9761eb56065d29f04db62a67103e41e against 94635718ea4a79569ac612bcb814114000028be3
Verdict: withheld reason: frame/questions.md:19 (the framer's row, closed by the orchestrator on the owner's answer) still reads Q1 `open` with the default that every draft goes to its backlog: milestone, which the tracker (milestone 85, release: 0.31.2, holding #1338, #1343 and #1346) and frame/plan.md:74 contradict; and the orchestrator's part of the pull request body calls Q1 both open and answered in *A decision left to the owner*, and in *Left for the owner* names #1337, now closed into #1346, as the issue that edits seal/follow-up.md
```

## Re-audit at de19e0f3c

| Field | Value |
|---|---|
| Broad gate | 4df5976b1 against 94635718e |

Two commits landed since the block above. 16a937b7e adds that block, and the committed file equals this run's text up to it (executed: `git show HEAD~1:<item>/guarantee.md \| diff -`). de19e0f3c touches only `frame/questions.md` (executed: `git log --no-merges --name-only e44456f8c..HEAD`). `trail/gate.md` still names `4df5976b1`, an ancestor of HEAD, and every path after it lies under the work item's directory (executed). `git diff --name-only 94635718e..HEAD` prints nothing outside that directory (executed: `0`). `seal pr-body <item> --body <file> --check` exited 0 with the installed `seal` and with `bin/seal` (executed).

### Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| Q1's Status cell holds the owner's answer, and nothing else in the file changed | `frame/questions.md:19` | the file at HEAD compared with `e44456f8c:` line by line, and Q1's row cell by cell | holds (executed): only line 19 differs, and on it only the sixth cell. The cell reads "answered 2026-11-04 by the owner, after the filing", names the fold into #1346 and the three issues in `release: 0.31.2`, and cites `frame/plan.md` *Judgments of the run*, the last row. The tracker holds that state (executed in the block above; the issues and milestone 85 were read for this run as well) |
| #1346's item for `seal/follow-up.md` names the blank line | the body's *Left for the owner* | `gh issue view 1346 --json body` | holds (executed): its #1337 item ends "the same file's table *Schedulable items with nowhere else to go* holds a blank line that renders its last rows as a paragraph" |

### The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | unchanged | the issue and the tree, as the first block found | none |
| the build | unchanged | as the first block found | none |
| the last round | unchanged | as the first block found | none new; the round's "three" stays its own count, as the first block names |
| the changelog | none is written | design G10; the new commit changes only a record | none |
| the plan (`frame/plan.md:73`, `:74`) | The drafts were filed on Q1's default, and the owner then had them folded and placed in `release: 0.31.2` | the tracker; `frame/questions.md:19` | none |
| the questions (`frame/questions.md:19`) | The owner answered Q1 on 2026-11-04, after the filing, with the fold and `release: 0.31.2` | the plan's last row; the tracker | none |
| the orchestrator's part of the pull request body | *A decision left to the owner* says Q1 asked, the run filed on its default, and the owner answered after the filing, as Q1's Status cell holds. *Left for the owner* sends the blank line of `seal/follow-up.md:45` to #1346's item for that file. The rest is as the block above read it | `frame/questions.md:19`; #1346's body; the tracker; the records | none |

```seal
target: de19e0f3c21dfc1f2497094e2a1ec0c8504d01fd against 94635718ea4a79569ac612bcb814114000028be3
Verdict: sealed
```
