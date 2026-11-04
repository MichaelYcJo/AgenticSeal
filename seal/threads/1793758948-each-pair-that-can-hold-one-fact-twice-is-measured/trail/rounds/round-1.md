# Review round 1: 1793758948-each-pair-that-can-hold-one-fact-twice-is-measured

```seal
target: 654c4a374 against origin/release/v0.31.1
```

The diff against the base `94635718e` is the work item's nine records and nothing else (executed: phase 4's *Command checks*, second part, printed `0`). No earlier round exists, so no fact is carried; every coordinate below was opened this round. `seal/parity.md` is not declared, so no parity comparison is owed.

Stage 1 read the frame (`frame/design.md`, `frame/plan.md`, `frame/questions.md`), the four phase records, `gaps.md` and the issue's *Done when* against the tree at `94635718e`. Stage 2 re-ran every command block of the four phase records except the three *Command tracker* keyword searches, from fresh scratch copies, and opened each draft's instances at `94635718e`.

The implementer's account, claim by claim:

- Claimed: each row's command, run as written, prints the row's count (design S1). Found: it does, for every row. All blocks of phases 1 to 3 ran in order in one shell, and phase 4's ran in a second shell. Every printed figure the records state came back, from `prose files 457` and `R17: 3 passages over 38440 file pairs` through `pins 287 in 50 modules, corpus P8`, `orphans in P9 446 distinct (395 headings, 51 markers)`, the `293`, `ids 6323; ... 25; ... (0.47%); ... no id naming 44`, `R19 docstring and comment spans 421; ELSEWHERE 8; NO 60; NOWHERE 17; PATH 5; in 58; module 233; own 40`, `R20 figure candidates with no moment on their line 53`, and `E1 sections 17 17; blocks 100 100`. *Command R16* printed `generator exit 0`, no `differs:` line and `17`. *Command R6*'s third part printed 10, 5, 17 and 11. One difference is environmental: `git log --format=%h` in this round's clone abbreviates to 8 hex digits where the records print 9, such as `8350c578` for `8350c5788`. These are the same commits.
- Claimed: R18 holds at `2026-11-04T03:59:46Z` (gaps.md asks the proofer to run *Command R18* again). Found: run at `2026-11-04T04:40:25Z`, the reader printed `open issues 61; comments 47; milestones 83, open 9`, then 18 and 14, 14 and 10, and 1. These are the row's counts. No line differs from the instances the record reads. The run needed `GH_REPO` set, because this round's clone is a `--no-local` clone whose remote is a local path. That is this round's environment, not a defect of the block.
- Claimed: the drafts' instances stand at `94635718e`. Found: each of D1 to D12 was opened at its coordinates (*Confirmations*). Each stands as its draft says, but one draft does not hold an instance its row homes in it (finding 1).
- Claimed: the frame as folded states one design the build holds. Found: the four folds rewrote what they name. `tests/text/test_a_cited_commit_outlives_the_squash.py` now passes over the frame (executed). But the R18 fold reached three of the seven frame sentences that state the measured moment (finding 2).
- Claimed: the phase-boundary runs were green, 1920 passed at phase 4. Read, and not re-run as a whole. This round ran the plan's named case together with the citation module (*Probes*).

The plan's `## Judgments of the run` still holds the template's placeholder paragraph at `frame/plan.md:64`, above the orchestrator's rows. The paragraph opens with no complete tag, so it renders as prose, and no reader takes it for a row. It misleads nobody who acts on it, so it is no finding. The orchestrator owns that section.

## Findings

### 1. D2's draft does not hold the R19 instance R19's row homes in it, and `gaps.md` asks the orchestrator to change the draft at filing

```seal
severity: should
location: `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/trail/phases/phase-1.md:784-800`, `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/trail/phases/phase-3.md:30`, `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/trail/phases/phase-3.md:561`, `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/gaps.md:26`
evidence: read `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/trail/phases/phase-1.md:792-796`, `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/trail/phases/phase-3.md:561`, `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/gaps.md:26`, `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/frame/plan.md:58-60`, `tests/text/test_the_rules_claude_md_names_have_one_home.py:48-49`
```

Why it matters: R19's row gives `D11, D2` as the home of its twelve drifts (`phase-3.md:30`). *Instances R19* puts the twelfth in D2: `tests/text/test_the_rules_claude_md_names_have_one_home.py:48-49`, "This is the shape `tests/test_the_ledger_rules_have_one_home.py` set". That module is gone (executed: `git ls-tree -r --name-only 94635718e tests` lists no such file). D11's *Scope* leaves the sentence out because it stands in D2's docstring (`phase-3.md:622`).

D2 as drafted does not hold it. Its *What is wrong* names only the `CLAUDE.md` statements. Its *Done when* asks only that the docstring state the module's cases and "no row of `CLAUDE.md` it does not hold" (`phase-1.md:792`, `:796`). A fix that meets that *Done when* can leave lines 48 and 49 standing. So the instance has a home that does not hold it, which design S4 and *Scope* item 5 refuse.

`gaps.md:26` says the orchestrator "adds the sentence to D2's *What is wrong* when it files D2". That contradicts plan *Operational impact*, which files each draft with "its title and body as the draft gives them" (`frame/plan.md:58`). It also breaks the fallback at `frame/plan.md:60`. Where the harness refuses `gh issue create`, the owner files the draft from its phase record, which "already stands whole", so the owner would file D2 without the sentence.

Phase 3 says phase 1's draft "is not this phase's to rewrite". The same phase rewrote phase 1's R9 and R15 cells at the orchestrator's request (`phase-3.md:23`). The plan says a finding on a record is fixed in its one record (`frame/plan.md:14`), so the fix belongs in D2.

The fix touches four statements: D2's *What is wrong*, *Done when* and *Answers* in phase 1, the clause "whose body does not name it" in phase 3's *Instances R19*, and the `gaps.md` paragraph, which this fix makes untrue.

`trail/phases/phase-1.md`, D2, appended to *What is wrong* after "...believes `CLAUDE.md` still carries the rows.":

```markdown
The same docstring's last paragraph, at lines 48 and 49, says the module has "the shape `tests/test_the_ledger_rules_have_one_home.py` set", and that module left the tree at 5b1f6faea (#944); phase 3's R19 counts it (`seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/trail/phases/phase-3.md` *Instances R19*).
```

`trail/phases/phase-1.md`, D2, *Done when*, replacing its first sentence:

```markdown
**Done when.** The docstring states what the module's cases hold at the commit that changes it, no row of `CLAUDE.md` it does not hold, and no module the tree does not hold offered as standing.
```

`trail/phases/phase-1.md`, D2, *Answers*:

```markdown
**Answers.** R9, and R19's instance in this docstring (`trail/phases/phase-3.md` *Instances R19*).
```

`trail/phases/phase-3.md:561`, the tail of the instance:

```markdown
The module left at 5b1f6faea (#944). This sentence stands in the docstring D2 rewrites, so its home is D2, whose body names it.
```

`gaps.md:26`: delete the paragraph that begins "One of R19's drifted sentences stands in the docstring D2 rewrites". After the fix no item of it stays not done.

```seal
verdict: fixed 8caff5e2c
answer: Read against design S4 and *Scope* item 5, plan *Operational impact* and the docstring at `94635718e` (lines 48 and 49 hold the sentence, and `tests/test_the_ledger_rules_have_one_home.py` left at 5b1f6faea), the finding holds. D2 in `trail/phases/phase-1.md` now names the sentence in *What is wrong*, in the round's words except that it quotes the docstring's own "This is the shape ... set" and says what a reader finds, and its *Done when* and *Answers* are the round's text. Two statements of the same record were corrected with it, which the finding did not list: D2's measure line now cites `trail/phases/phase-3.md` *Instances R19* beside *Instances R9*, and the *Drafts* opening sentence says D2 rests on that section too. `trail/phases/phase-3.md` *Instances R19* now ends "whose body names it", and the `gaps.md` paragraph is deleted. `bin/test` over the plan's named case and `tests/text/test_a_cited_commit_outlives_the_squash.py` passed at 8caff5e2c (executed: 13 passed). Read whole against HEAD after the commit: `routing.md`, the three frame files, `gaps.md` and the four phase records hold no other sentence that leaves D2's sentence to the filing (`grep` on "does not name it", "adds the sentence" and "not this phase's to rewrite" prints only this round's own lines).
```

### 2. The R18 fold left four frame sentences saying every drift and every command is read at `94635718e`

```seal
severity: should
location: `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/frame/design.md:28`, `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/frame/design.md:52`, `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/frame/design.md:63`, `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/frame/design.md:73`
evidence: read `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/frame/design.md:28`, `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/frame/design.md:51-52`, `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/frame/design.md:63`, `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/frame/design.md:73`, `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/frame/design.md:139`, `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/trail/phases/phase-3.md:11`
```

Why it matters: fold a433b5b55 rewrote the moment R18 is measured at, because a tracker has no commit (`phase-3.md:11`). It rewrote *Scope* item 1's first sentence, S1 and *The row* (`design.md:28`, `:51`, `:139`). Seven frame sentences state that moment, and the fold reached three of them. The other four still state the fact the fold replaced:

- `design.md:28`, *Scope* item 1, its second sentence: "Each command reads git objects at that commit or a `git archive 94635718e` copy". *Command R18* and every *Command tracker* read the tracker through `gh`.
- `design.md:52`, S2: "when a reader opens each instance's coordinates at `94635718e`". R18's two instances are a milestone description and an issue body, which have no coordinate at a commit.
- `design.md:63`, *The methods*: "The script reads a `git archive 94635718e` copy only". `probe3.py#tracker` reads `$S/issues.json` and `$S/milestones.json`, which `gh` writes.
- `design.md:73`, *The unit counted*: "*Drifted* counts units whose holders state the fact differently at `94635718e`". R18's two drifted units are counted at `2026-11-04T03:59:46Z`.

The frame is what the sealer reads the records against (`frame/plan.md:14`). A reader checking R18 against S2 or *The unit counted* finds the row out of step with the frame, although the row follows the fold. Contract rule 19 asks a change to rewrite every sentence that states the old fact. The frame's two files are the fold's whole reach and can be read whole, so this list is whole for the R18 fact.

A second unfolded sentence stands at `design.md:63`, from phase 4. "A later phase adds its functions in its own *Command setup*" does not hold for `probe4.py`, which loads no earlier probe. Phase 4 names this at `phase-4.md:15` ("*Command setup* writes a script of its own"), but the frame was not folded for it. The snippet below covers it too.

`design.md:28`, *Scope* item 1, in place of its second sentence:

```markdown
Each command that counts the tree reads git objects at that commit or a `git archive 94635718e` copy under the phase's scratch directory, and R18's reader reads the tracker through `gh`.
```

`design.md:52`, S2, in place of its *Given / When / Then* cell:

```markdown
Given a row whose drifted count is above 0, when a reader opens each instance's coordinates at `94635718e`, or for R18 in the tracker, then the two holders state the fact differently, R18's as of the moment its row states
```

`design.md:63`, *The methods*, in place of the paragraph's first, second and third sentences:

```markdown
Each method is a function of a probe script. The first phase writes the script whole in its record's *Command setup*, and a later phase adds its functions in its own *Command setup*, as #1147's phase 2 imported phase 1's, or writes a script of its own where it ports none of #1147's readers. Each script reads a `git archive 94635718e` copy, and R18's reader reads the tracker as `gh` returns it.
```

`design.md:73`, *The unit counted*, in place of the sentence on *Drifted*:

```markdown
*Drifted* counts units whose holders state the fact differently at `94635718e`, or for R18 at the moment its row states, judged by reading.
```

The snippets leave `frame/plan.md` *Judgments of the run* unchanged. The fix pass writes the row for this fold there, as it did for the four folds before it.

```seal
verdict: fixed d2cae5644
answer: The orchestrator applied the fix, since `frame/design.md` is not a file the fix pass writes. Read at d2cae5644 against the finding: *Scope* item 1's second sentence, S2's cell, *The methods*' opening sentences and *The unit counted*'s *Drifted* sentence are the round's text, *The methods* allows a phase a script of its own as phase 4 wrote, the drafted-issue paragraph's commit clause now names R18's moment, and `frame/plan.md` *Judgments of the run* has the row. Those sentences hold. The finding's list is not whole for the R18 fact, though: `frame/plan.md` still says it in four places. *Technical context*'s first paragraph says "Each phase measures a group of the design's rows at `94635718e`". The paragraph on the review chain says "The proofer runs each row's command at `94635718e`". The failure scenario says the commands "read `94635718e` by name, so they print the same counts", which R18's reader cannot do. Phase 3's Verified by cell, "the same, for its rows", carries row 1's "each row's command, run at `94635718e`" to R18. These are plan sentences, which the fix pass does not write, and they are named for the orchestrator to fold.
```

## Confirmations

```seal
confirms: none
```
What matched: design S1, executed. Every row's command, run as its record writes it from a fresh `git archive 94635718e` copy, printed the row's count. This covers all of phase 1's blocks but *Command tracker*, all of phase 2's but *Command tracker*, all of phase 3's but *Command tracker*, and all of phase 4's but *Command tracker* (*Probes*). That is every block except the three keyword searches. It is not a sample of rows.

```seal
confirms: none
```
What matched: R18, executed. *Command R18* run at `2026-11-04T04:40:25Z` printed the counts of `trail/phases/phase-3.md:29`, `18; other than the issue's own 14`, `14; standing in another milestone 10` and `1`. It also printed the same milestone 78 events (`release: 0.29.0` at placement), `2026-11-01T03:27:48Z` for #1236's last body edit, and milestones 81 and 82 created on 2026-11-02. The two drifted statements D10 drafts still stand in the tracker.

```seal
confirms: none
```
What matched: design S3, S5 and G10, executed. Phase 4's *Command checks* at 654c4a374 printed nothing for the label count, `0` for paths outside the work item, and `1` for the absent `changelog.md`.

```seal
confirms: none
```
What matched: D1 to D12, read at `94635718e`. Each stands at the coordinates its draft names.

- D1: `seal/README.md:85-90` lists three items and says no row means the default. `seal/config.md` holds five rows, and `templates/setup/config.md:224` says an absent `Broad gate` row "is a refusal, not a default".
- D2: the module docstring's lines 1, 11 to 13 and 41 to 46 against a `CLAUDE.md` naming none of the four homes (*Command R9* printed `0`). The `LINKED` comment at lines 137 to 143 says the rows left.
- D3: `evals/scripts/rule_cases.py:159`, `:263`, `:270`, `:357`, `:363`, `:764`, `:771` and `:795` against `templates/records/sdd-design.md:1` and `:13` and `templates/records/sdd-routing.md:1`, with the later `# Design:` at `:458`.
- D4: `seal/follow-up.md:42` cites a warning that the `read_record` docstring no longer gives, and `1788817289-local-mode-from-first-setup-to-the-gate` is not under `seal/threads/`.
- D5: `.github/ISSUE_TEMPLATE/gate-misfired.md:4` applies `labels: gate`. `gh label list --limit 100` lists `hooks-gates` and no `gate` (executed).
- D6: the comment at `.github/PULL_REQUEST_TEMPLATE.md:29-34` names four items. The section names seven, and its closing paragraph says the prompt budget and what a change removes are answered in the body only.
- D7: `ruff.toml:40-42` and `CONTRIBUTING.md:126-130` against `tests/hooks/test_launch.py:210-212`.
- D8: `docs/releasing/branch-and-release.md:204-206`.
- D9: `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:46-47`. No file under `hooks/`, `skills/*/scripts/`, `.github/scripts/`, `evals/scripts/` or `bin/` holds the item's string (executed: `git grep`).
- D10: R18 above.
- D11: sampled. `tests/behaviour/test_first_setup_asks_once.py:8` and `tests/text/test_review_axes.py:105-107` were opened, and neither `tests/test_commit_review_gate.py` nor a `def test_the_core_names_where_the_routing_question_is` stands under `tests/` (executed: `git ls-tree`, `git grep` exit 1).
- D12: `docs/experiments/2026-09-03-skill-preload-and-the-copy-in-force.md:28` says three runs edited the clone, and the Results table gives runs 1 to 4 in the clone.

```seal
confirms: none
```
What matched: the edition reading, read by a sample. *Instances E1*'s pairs `README.md:165` with `README.ko.md:170` and `README.md:298` with `README.ko.md:301` were opened at `94635718e`, and each states one fact as the record reads it. *Command E*'s third part printed the four `.ko.md` citations the record names and nothing for E2 to E4. The rest of the block pairs were not read here.

```seal
confirms: none
```
What matched: the folds G6, G7, G16, F1, F8, G11, M5 and G13. Each now states what its phase's hand-back found, read against the tree. `tests/text/test_a_cited_commit_outlives_the_squash.py` passes over the frame at 654c4a374, and the plan's named case `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview` passes (executed: 13 passed, *Probes*). `.github/scripts/plugin_directory_check.py`, `pytest-split` 0.11.0 and `test_the_durations_file_prices_the_suite` read what F1 and F8 now say they read (executed: phase 2's *Command files* third block printed both `pytest-split` functions).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the `replay-*` and `seeded-*` proofer cases are their generators' output at `94635718e`. Answering it means fetching every `refs/pull/*/head` from the remote. R16's corpus leaves those cases out by the design's own words whether or not they match, so the answer changes no row's count. | `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/gaps.md:8` | the orchestrator, who decides whether the fetch is worth its cost before the sealer reads `gaps.md` |
| The three *Command tracker* keyword searches run before the drafts. A re-run now would read today's tracker and not the tracker each phase searched. | `trail/phases/phase-1.md` *Command tracker*, `trail/phases/phase-2.md` *Command tracker*, `trail/phases/phase-3.md` *Command tracker*, `trail/phases/phase-4.md` *Command tracker* | the orchestrator, by searching again before it files each draft (plan row A5) |
| Whether the `declared_mode` docstring names a reader that the tree no longer has. It counts the absent states "the pull-request-language row has", and no script reads that row (D9). | `hooks/lib/config.py:557` | the orchestrator, when it files D9 |
| Whether D12 is filed on its own or folded into #135, and whether D2's and D11's filed bodies follow finding 1's fix | `trail/phases/phase-4.md` *Whether the frame holds*, `gaps.md` *Not done* | the orchestrator |
| `frame/questions.md` Q1, the milestone of every draft | `frame/questions.md:19` | the owner |
| The full suite, the repository-wide lint and format, and the share F8 leaves to the collection. The phase-boundary set of 29 modules was read, not re-run. | `gaps.md:7`, `gaps.md:12` | the orchestrator, by the `Broad gate` row after the rounds settle |

## Probes

| Command | Result |
|---|---|
| phase 4's blocks but *Command tracker*, extracted in order by a `test_tmp_` extractor and run with `bash` from the clone at 654c4a374 | exit 0. Printed the eight paths, the four `E<n> sections` lines as `trail/phases/phase-4.md:148` states, the four `.ko.md` citation lines, the two history lines, and `0` and `1` from *Command checks* |
| phases 1 to 3's blocks but each *Command tracker*, extracted in order and run in one `bash` shell from the clone | exit 0 after 1 min 41 s. Every count the records state came back. *Command R18* failed on `gh`'s remote lookup in this clone and was run again alone |
| phase 3's *Command R18* with `GH_REPO=MichaelYcJo/AgenticSeal`, over the same scratch copy | at `2026-11-04T04:40:25Z`: `open issues 61; comments 47; milestones 83, open 9` and the row's three counts |
| `gh label list --limit 100 --json name`, from the branch worktree | `hooks-gates` is listed, and no `gate` |
| `bin/test tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview tests/text/test_a_cited_commit_outlives_the_squash.py -q -p no:xdist`, in the clone | exit 0, 13 passed |
| `git grep -n "Commit and pull request language" 94635718e -- hooks skills/*/scripts .github/scripts evals/scripts bin` | no output |

Each scratch copy the blocks made under the system temporary directory, the extractor and its outputs, and the clone were removed after the runs.
