# Review round 1: 1793750411-rule-text-carries-no-history

```seal
target: 579491bb1 against origin/release/v0.31.1
```

This round reviews the whole branch, `git diff origin/release/v0.31.1..579491bb1`.
The base `origin/release/v0.31.1` is 8d5a59c6c, which is also the merge base and
the commit the tag `v0.31.0` names (executed). The diff changes 34 files: seven
skill files, fourteen documents under `docs/`, three test modules,
`.claude-plugin/plugin.json` and the work item's own records (executed). The
repository tracks no `seal/parity.md`, so no `original:` line is owed and no
parity comparison applies. `seal/config.md` has no `Record language` row, so
this record is English. No earlier round exists, so nothing was carried. The
runs took place in a `git clone --no-local` at 579491bb1 under this round's
scratch directory, which has since been removed.

The contract is `frame/design.md` (scope, D2, D3, D4, O1 to O7, `## Removes`,
A1 to A8) and `frame/plan.md`. The account under review is the three phase
records, `gaps.md`, `changelog.md` and the commit messages. Each was read as a
claim. Each removal in the diff was read against the paragraph it left. Each
new citation was opened at the section it names.

The central question is whether a removal changed what a rule says (O7), and
whether each new citation names a section that holds the cited fact. No
removal changes what a rule says, and every citation holds. The confirmations
below set this out, one file group at a time.

Two weaker spots are noted here, and neither is a finding. First,
`skills/verify/orchestration.md:339-341` still says "Batching is the ordinary
way in and a background command is the rarer one". The sentence phase 1
removed after it was the only evidence for the frequency half of that claim.
The reading rule a reader acts on, that a share above 100 means calls ran at
once, stands on the timestamp mechanism the sentence states. Second,
`docs/forms/the-round-record.md:21` now grounds "one that has not drifted is
no finding" on "no template holds a place for a copy". That explains why
copies are rare more than why a standing copy is tolerated. The rule's act is
unchanged, and `frame/design.md` *Removes* allowed exactly this repair.

## Findings

This round opens no finding.

## Confirmations

```seal
confirms: none
```
What matched: A1. `git grep -n -F` over `skills` and `docs` on "Six of 0.27.x's fourteen", "Its first instance, #1148's frame", "read this signal in seven work items" and "With gh 2.100.0" exits 1 for each (executed).

```seal
confirms: none
```
What matched: A2 and A3. Each of the 17 named rows of `frame/design.md` *Removes* is gone at HEAD, or repaired as its row asks. Each removed or rewritten line in the diff appears in the removals table of `trail/phases/phase-1.md`, `phase-2.md` or `phase-3.md`, with its file, base line, class and grounds (read, hunk by hunk against the three tables). The four borderline candidates under *Removes* are each decided in a phase record. Three were removed: the two releases in `docs/releasing/issues-and-milestones.md`, the #1148 counts in `docs/releasing/release-checklist.md` and the frame-exchange paraphrase in `docs/running/the-agent-set.md`. The `release/v0.3.0` sentence was kept, and two cases pin it (read).

```seal
confirms: none
```
What matched: A4 and A5, re-derived by an independent probe of D4 written this round (see *Probes*). At 3bd60d29f the probe read 48 files, 595,984 bytes, 2,078 of 88,708 words, 80 pairs, 264 runs and 58 marker sentences in 22 files, with the same six largest pairs, which equals `frame/design.md` *Grounding*. At cc4d9902a and at 579491bb1 it read 48 files, 589,672 bytes, 1,799 of 87,579 words, 74 pairs, 228 runs and 36 sentences in 15 files, which equals `trail/phases/phase-3.md` *Census readings* and `changelog.md`. The per-file marker counts at HEAD match the kept lists: six in phase 1's files, three in phase 2's and 27 in phase 3's (executed). `v0.31.0` names 8d5a59c6c, so the changelog's "at `v0.31.0`" is true (executed).

```seal
confirms: none
```
What matched: A6. Each of the four sentences that pending `from` lines quote stands whole, with whitespace collapsed, in `docs/running/the-run.md` *The run* and `docs/layout/the-record-layout.md` *The root records* (executed). Every other unsettled design states `- nothing`. No directory under `seal/threads/` but this item's changed (executed).

```seal
confirms: none
```
What matched: A7 and S3. Claimed: the pins on removed text were the two `KNOWN_PROSE` entries and a comment in `tests/behaviour/test_the_set_a_work_item_always_has.py`, the `2.100.0` entry of `tests/behaviour/test_release_hygiene.py#VERSIONS_OF_ANOTHER_PRODUCT`, and one phrase of `tests/text/test_the_rules_have_one_owner.py`. Found: those three edits are the diff's only test changes. The remaining `KNOWN_PROSE` lines still stand in their files. `git grep -F` on the removed copies' wording finds each fact only at its home (`skills/agent-contract/SKILL.md:41`, `skills/core/SKILL.md:128`, `skills/commit-pr-convention/SKILL.md:164`, `skills/implement/SKILL.md:24`), and the "never converges" reason still stands at `docs/forms/the-round-record.md:14` (executed). The run of `bin/test` over the 90 test modules that name a changed file's base name exited 0 with 2,966 passed and 11 skipped. That is a narrow run, not the broad gate (executed).

```seal
confirms: none
```
What matched: A8. `.claude-plugin/plugin.json` reads `0.31.1`, and `changelog.md` ends with a `### Process changes` table of three rows, one for each orchestration file the diff changes, all in 930ac879c (read). `docs/layout/the-record-layout.md:51-56` says the orchestrator writes the process row with the fragment. Here the crafter wrote it, handed the rows by the orchestrator's spawn. The paragraph under `frame/plan.md` *Phases* and its *Judgments of the run* row record that departure with grounds. What the section protects still holds: the row was written with its fragment, in the commit that adds it.

```seal
confirms: none
```
What matched: O7 for the three orchestration files. `skills/implement/orchestration.md:19-20` now cites `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, and `skills/implement/SKILL.md:90-93` states both places the root can be and the marker (read). The spawn-as-approval citation lands on `skills/implement/SKILL.md:295`, inside *3. The SDD file set* (read). The shortened edit-gate paragraph points at `skills/implement/orchestration.md:163-171`. That paragraph names the three refused tools, says a file under the `seal/` root is not judged, and says what `seal no-work-item` records. The one act kept, running it on each branch the session edits, covers the removed "runs it there again" (read). `skills/code-review/orchestration.md:98-99` cites the opening of `skills/implement/SKILL.md`, whose lines 21-25 keep "reaches it by being opened rather than by arriving" and the `user-invocable: false` clause (read). The rewordings at `skills/implement/orchestration.md:222`, `:273`, `:434`, `:440` and `:448-449` keep each rule. The removed `2.100.0` clause leaves "exits 1 without waiting", which is what the next sentence's act stands on (read).

```seal
confirms: none
```
What matched: O7 for the other skills. Each removal from `skills/implement/SKILL.md`, `skills/code-review/SKILL.md`, `skills/settle/SKILL.md` and `skills/writing-style/SKILL.md` takes a past event or a count, and the rule stands in the sentences beside it (read). In `skills/writing-style/SKILL.md`, the removed account of `seal` naming three things is held by the *좋음* cell of the table above it at `:235`. "이 문장은 보장이 아니다" keeps its reason in the present tense at `:242-246`. The comment's reason at `:291-294` and the reviewer's reason at `:311-312` are now in the present tense and say what they said before (read).

```seal
confirms: none
```
What matched: O7 and the citations under `docs/`. `docs/releasing/release-checklist.md:194-205` *What a release pull request is held to* states why the tag and not `plugin.json` decides, which `docs/releasing/issues-and-milestones.md:116-117` now cites. `skills/commit-pr-convention/SKILL.md:162-164`, inside *Commit messages*, says the orchestrator retitles the issue when it titles the pull request, which `docs/releasing/issues-and-milestones.md:340-343` now cites. The `feat:` move is at `docs/releasing/branch-and-release.md:350`, inside *Work accumulates on a release branch* (read). `docs/releasing/issues-and-milestones.md:238-268` names the labelling script, its trigger, the `merged: X.Y.Z` label and why the label exists, which `docs/releasing/branch-and-release.md:305-310` now cites. `docs/releasing/branch-and-release.md:12-20` and `:112-118`, both in *Cutting a release*, hold the version hook's reason and the marketplace command's two reasons, which `docs/releasing/release-checklist.md:224-225` and `:289-291` now cite (read). Contract rules 2 and 5 hold the suite label and the aggregate rule that `docs/running/the-broad-gate.md:36-38` and `docs/running/the-run.md:81-82` now cite. In `docs/running/what-a-script-gates.md`, the new opening's claim that each check is listed with the agent that judges its meaning is true: the table under *The checks* has an `Agent` column. Every cut clause stands in the core sections the document cites (read). `docs/running/the-agent-set.md:60-68` keeps the bold rule, the one-exchange bound and that the orchestrator edits no frame file. Each removed step stands at `skills/implement/orchestration.md:100-122` (read). The tense repairs in `docs/running/the-agent-set.md`, `docs/layout/one-root-by-lifetime.md` and its Korean edition, and `docs/releasing/branch-and-release.md:34-37` keep each rule's reason (read). `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and the other thirteen modules this round ran first exited 0 with 506 passed (executed).

```seal
confirms: none
```
What matched: D3's choice of which side stays. Each removed copy leaves the side that `docs/README.md`'s index, the skill, or the document itself names as the home: the contract for agent rules, the core for the script-gate rule, `branch-and-release.md` for the checklist's reasons, `issues-and-milestones.md` for the `merged:` label, and `skills/implement/SKILL.md` for what the orchestrator reads beside it (read). Each kept copy has a D3 ground in its phase record. Among them are `skills/verify/orchestration.md` *The broad gate*, the `seal/` root in `skills/commit-pr-convention/SKILL.md` and `skills/config/SKILL.md`, and the release checklist's step 2b, and some are held by a case as text a reader acts on (contract rule 14). This round read each ground against D3 and found it consistent (read).

```seal
confirms: none
```
What matched: the method claims of contract rule 12. Each phase claims a whole list of history sentences for its files, by reading each file whole, and calls its list of paraphrases a sample (`frame/questions.md` Q2). Restatements in other words across the tree are an open class, so a sample is the honest label. As a check on the whole-list claim, this round ran two searches over the 47 in-scope files at HEAD, on issue numbers and on past-tense and version phrasing (executed). Each hit is a sentence a phase record lists as kept, an example inside a fenced block, or a present-tense rule. No history sentence turned up that the records missed. These searches are a sample.

```seal
confirms: none
```
What matched: the closing memo. The `## Not verified` rows that name the proofer as answerer are answered by the confirmations above, by reading for the orchestration files and the skills, and by the probe for the census at HEAD. `gaps.md` *Not done* names the duplicated `check: last-record-at-head` line in `docs/checks/the-pull-request-check.md`. That line stands at the base too, so it is not this diff's (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and format check, and the typecheck at 579491bb1. The suite stays `unverified`. This round leaves nothing open, so what comes due is the orchestrator's broad run, and the sealer's spawn after it. | the whole tree | the orchestrator |
| Whether an orchestrator at the next release reads the shortened orchestration text and still acts as before. This round settled it by reading. No session of this run loads the new text, because sessions load the installed 0.31.0. | `skills/implement/orchestration.md`, `skills/code-review/orchestration.md`, `skills/verify/orchestration.md` | the first orchestrator that runs on 0.31.1, and the settle |
| The commit messages of 36c88cc9c ("Fourteen files" for ten that lose history) and of 3bd60d29f to 8b30ef79b (no `Seal-Routing:` trailer). The branch squashes, so neither survives into the base. | the branch's commits | the orchestrator, who writes the squash message |

## Probes

| Command | Result |
|---|---|
| `python3 -I test_tmp_census.py 3bd60d29f cc4d9902a 579491bb1`, a probe of D4 written this round in the clone. It reads each file through `git show` and uses `skills/settle/scripts/passages.py#in_corpus` and `#words` with D4's regex and sentence split. A second run printed each marker sentence per file at 579491bb1. | exit 0. At 3bd60d29f: 48 files, 595,984 bytes, 2,078 of 88,708 words, 80 pairs, 264 runs, 58 sentences in 22 files. At cc4d9902a and at 579491bb1: 48 files, 589,672 bytes, 1,799 of 87,579 words, 74 pairs, 228 runs, 36 sentences in 15 files. The probe file was deleted, and the clone was removed with it. |
| `bin/test -q -p no:randomly` over the 14 modules that pin cited sections, shared runs, wrap, both editions, `KNOWN_PROSE`, the release hygiene, the one-owner phrases, the handoff, the broad-gate rule, the acts table, moved rules, the contributor procedure, the finding counts and the rules | exit 0; 506 passed |
| `bin/test -q -p no:randomly` over the 90 test modules that `git grep -l -F` lists for the changed files' base names | exit 0; 2,966 passed, 11 skipped |
| `git grep -n -F` on the A1 phrases over `skills` and `docs`, and on the removed copies' wording over the tree outside `seal/threads/` | exit 1 for each A1 phrase. The copies' wording appears only at each home named under *Confirmations* |
