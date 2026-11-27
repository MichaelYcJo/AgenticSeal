# Review round 2: 1795798115-the-plugin-is-named-for-the-seal

```iadd
target: 060ac283, fixes 32719b79..060ac283
```

The round is the verifying round over the fix pass of round 1. Its code target is `git diff 32719b79..060ac283`, which changes `README.ko.md`, `skills/settle/SKILL.md`, `skills/writing-style/SKILL.md` and `tests/skills/test_stamp.py`, seven lines removed in all, and adds `trail/rounds/round-1.md`. The round read that diff whole, and `git log --oneline 32719b79..060ac283` names its three commits: `85cb8405`, the round 1 record, `658d6777`, the fix, and `060ac283`, the close blocks. It read the work item's `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md` whole at `060ac283`, and searched the nine phase records for each sentence the fix diff touches. No `pr.<lang>.md` stands, and `iadd/parity.json` is absent, so no parity comparison is owed.

Carried from round 1, not re-established: the coordinates of its four findings and the commands on their `evidence:` lines, which this round ran again at the target. Every verdict below is this round's own.

The fix pass's sample under finding 1 of round 1 says that 10 lines the range added to `skills/writing-style/` and `*.ko.md` hold a backticked `iadd`, and that apart from line 273 each one names the command, the root or the fence. The round ran the same diff and counted 10. One of them, `docs/layout/one-root-by-lifetime.ko.md:67`, names a package called `iadd` that a project might have, not the command, the root or the fence. Its sense is right, so the close's wording is loose and no defect follows.

## Findings

### 1. The settle's sentence on its own commits now names only the new trailer, and the settle commits of earlier releases carry the old one

```iadd
severity: should
location: `skills/settle/SKILL.md:233-235`
evidence: executed `git log --format='%h %s' --grep='Seal-Routing: no work item' origin/release/v0.40.0`, `git log -1 --format=%B 235d41ff`, `git tag --contains 235d41ff`, `git merge-base --is-ancestor 235d41ff v0.39.3` and `git grep -n -F 'no route chosen' -- . ':!iadd/threads'`; read `skills/settle/SKILL.md:224-240`, `skills/settle/SKILL.md:456-461`, and the same step of `git show origin/release/v0.40.0:skills/settle/SKILL.md`
regression: round-1#2
```

Why it matters: the unit is step 5 of `skills/settle/SKILL.md` *The settling session's procedure*, the sentence `658d6777` rewrote. The settle session reads it to tell the routes the orchestrator chose with no work item from the commits that chose none. The step now sends the settle to two lists, and the sentence that leaves the settle's own commits out of the routes covers only one of them.

At the base the step named one trailer, `Seal-Routing: no work item`, and *A settle's commit carries that trailer with no route chosen and is not one* covered every settle commit, since every one carried that spelling. Phase 7 added the sentence that a commit of a release before the rename carries `Seal-Routing: no work item`, and that `git log --grep` on that spelling lists those. Round 1's finding 2 found *that trailer* had two antecedents. Its paste-ready fix, which the fix pass applied as written, names the new spelling alone: *A settle's commit carries `IADD-Routing: no work item` with no route chosen and is not one.* The frame names the old spelling as the form of the commits before this release (`frame/design.md` *Scope*, *Out of scope*, *Committed trailers*), and the fix replaced *that trailer* with that one form where the step lists commits in both forms. So the defect came from the fix: it repaired the reading for the settle commits from this release on and dropped the reading for the earlier ones.

`git log --grep='Seal-Routing: no work item' origin/release/v0.40.0` prints 23 commits, 11 of them titled `chore: settle`. One is `235d41ff`, *settle 0.37.1 to 0.39.3*, which `git tag --contains` places in `v0.39.4` and not in `v0.39.3`. Its body ends with `Seal-Routing: no work item`. A settle that follows step 5 lists those 11 commits with the old spelling, then reads that a settle's commit carries `IADD-Routing: no work item`, which none of them does. It can then count each one as a route chosen with no work item and read its body as the grounds of one. `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* asks a text an agent follows to have one reading.

The `git grep` on *no route chosen* printed `skills/settle/SKILL.md:234` and no other line. A statement of the same fact in other words is outside what it finds, so it is a sample. `skills/settle/SKILL.md:456-461` states the trailer a settle's commits carry from now on, `IADD-Routing: no work item`, which is true going forward, so it needs no change. The fix keeps the backticked `IADD-Routing: no work item` that `tests/text/test_settle_reads_before_it_removes.py#test_the_skill_names_how_a_settle_commits` reads.

```markdown
   renamed the plugin IADD carries the trailer as `Seal-Routing: no work
   item`, and `git log --grep` on that spelling lists those. A settle's
   commit carries the trailer in its release's spelling, `IADD-Routing: no
   work item` or, before that release, `Seal-Routing: no work item`, with
   no route chosen, and is not one.
```

```iadd
verdict: fixed e6359a4d
answer: The sentence now names both spellings, each for its commits: *A settle's commit carries `IADD-Routing: no work item`, or `Seal-Routing: no work item` in a release before that one, with no route chosen, and is not one.* *That one* is the release the sentence before it names, the one that renamed the plugin IADD. The pass wrote this in its own words. The paste-ready text's *its release's spelling ... before that release* leaves *that release* to be resolved through *its release*, which can be read as the commit's own release. The backticked `IADD-Routing: no work item` that `tests/text/test_settle_reads_before_it_removes.py` reads stands on one line, and the review-round set passed. After the fix, `git grep -n -F 'no route chosen' -- . ':!iadd/threads'` prints only `skills/settle/SKILL.md:235`, the fixed sentence. The other lines that state a settle commit's trailer, from `git grep -n -i 'no work item' -- . ':!iadd/threads' ':!docs/experiments' ':!evals/behaviour'`, are `skills/settle/SKILL.md:460`, `docs/checks/the-fold.md:74` and `docs/releasing/release-checklist.md:71`. Each one tells a settle what its commits carry from this release on, and none reads the commits of earlier releases, so each stands.
```

The test reads the skill through `tests/conftest.py#flattened`, which makes each run of whitespace one space, so the trailer wrapped across two lines still reads whole.

## Confirmations

```iadd
confirms: round-1#1
```
What holds: `skills/writing-style/SKILL.md:175` gives `mark`, `proofer`, `crafter` as coined words a Korean text keeps in English. `README.ko.md:38`, `:168` and `:266` keep `proofer` in English, and `docs/method/iadd.md` *The names* gives no Korean name for the proofer. `skills/writing-style/SKILL.md:273` names `inspection`, and the table of *여럿이 가질 수 있는 것은 누구 것인지 밝힌다* opens its bad column with `the inspection` (`skills/writing-style/SKILL.md:235`). Executed: `git grep -n -F '만들어 낸 말' -- . ':!iadd/threads'` prints only line 175, and ``git grep -n -F '절의 `iadd`' -- skills/writing-style`` exits 1. Read: the lines named.

```iadd
confirms: round-1#2
```
What holds: the defect the finding named is gone. Step 5 names `IADD-Routing: no work item` as the trailer of a settle's commit (`skills/settle/SKILL.md:234`), as `skills/settle/SKILL.md:460` does, so the claim of `trail/phases/phase-7.md:55` holds. `git grep -n -F 'that trailer with no route chosen' -- . ':!iadd/threads'` exits 1, executed. The fix left the settle commits of earlier releases out of the sentence, which finding 1 of this round holds as a regression.

```iadd
confirms: round-1#3
```
What holds: `README.ko.md:28-29` says only that the name is a product name and is not translated, as `README.md:26-27` does. Executed: `git grep -n -F '도장 체인' -- . ':!iadd/threads'` exits 1. The sample of the close prints `README.ko.md:3`, `:179` and `:501`, and each describes the red wax seal of the drawing, which `frame/design.md` *Scope*, *Out of scope*, *The drawings*, keeps. The rewrapped lines 26 to 31 measure 72, 63, 75, 78, 76 and 18 display columns, and `tests/behaviour/test_docs_line_wrap.py` passed.

```iadd
confirms: round-1#4
```
What holds: the docstring at `tests/skills/test_stamp.py:2034` says *to remove that guarantee* again, the plain word of contract rule 13. Executed: `git grep -n -i 'guarant' HEAD -- . ':!iadd/threads' ':!docs/experiments'` prints 22 lines, and ``git grep -n -B2 'rule 13' -- . ':!iadd/threads' ':!docs/experiments'`` holds no *inspect* word. The close's sample names `skills/code-review/scripts/chain_check.py:133` and `skills/verify/SKILL.md:114`. Read: each names the inspector's record, where the base read *that guarantee* and *that seal*, so both senses are right.

What matched: the narrow modules of the four fixed files pass at `060ac283`, executed: `bin/test tests/behaviour/test_docs_line_wrap.py tests/text/test_settle_reads_before_it_removes.py tests/skills/test_stamp.py -q` passed 269, and `bin/test tests/text/test_a_language_section_of_writing_style_opens_alone.py tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_a_cited_section_stands_in_its_file.py -q` passed 108.

What matched: the fix diff adds no unit beyond the four sentences, no case, and no record line other than `trail/rounds/round-1.md`, read. No sentence of `routing.md`, the frame, `gaps.md`, `changelog.md` or `pr.md` states what the four fixed lines say, so the fix leaves none of them false, executed with `grep -n -i -e 'writing-style' -e '도장' -e 'that trailer' -e 'test_stamp.py'` over the work item's records.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite, the lint and the format check over the branch, under contract rule 2 | the `Broad gate` key of `iadd/config.json` | the orchestrator, at the broad run |
| The units outside the fix diff, which round 1 reviewed and this round's bound leaves out | the range `origin/release/v0.40.0..32719b79` | no one this round; round 1 read them |
| Whether `TRADEMARKS.md` should reserve the name IADD, which `frame/questions.md` Q1 holds open | `TRADEMARKS.md` | the repository owner |

## Probes

| Command | Result |
|---|---|
| `git log --format='%h %s' --grep='Seal-Routing: no work item' origin/release/v0.40.0` | 23 commits, 11 of them titled `chore: settle`, `235d41ff` among them |
| `git log -1 --format=%B 235d41ff`, `git tag --contains 235d41ff`, `git merge-base --is-ancestor 235d41ff v0.39.3` | the body ends with `Seal-Routing: no work item`; `v0.39.4`; exit 1 |
| `git grep -n -F 'no route chosen' -- . ':!iadd/threads'` | `skills/settle/SKILL.md:234` |
| the evidence commands of round 1's four findings, at `060ac283` | the outputs the four confirmations name |
| `git diff -U0 origin/release/v0.40.0...32719b79 -- skills/writing-style '*.ko.md'`, its added lines holding `` `iadd` `` | 10 lines |
| the six narrow modules the confirmations name, through `bin/test` | 269 passed, and 108 passed |
