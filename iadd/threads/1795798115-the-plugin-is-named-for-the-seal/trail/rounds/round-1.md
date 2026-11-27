# Review round 1: 1795798115-the-plugin-is-named-for-the-seal

```iadd
target: 32719b79 against origin/release/v0.40.0
```

The round read the branch `chore/1651-the-plugin-becomes-iadd` at `32719b79` against `origin/release/v0.40.0`, 450 files. It read the work item's `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md` and the nine phase records whole at the target. No earlier round exists, so no fact was carried and every verdict below is this round's own. The work item declares no `iadd/parity.json` (`ls iadd/` at the target), so no parity comparison is owed.

The method for the class the plan names in *Technical context*, the paragraph opening **The failure scenario of the chosen approach**, a word renamed in the wrong sense, was this. `git diff -M --word-diff=porcelain -U0 origin/release/v0.40.0...HEAD -- . ':!iadd/threads' ':!evals/behaviour'` printed every changed word of the range outside the records and the eval cases, 38112 lines. A script under the round's scratch directory paired each removed run with its added run and printed each changed line whole. The round read every line whose removed run held *guarantee* in any form, 202 lines, every line where a `seal`-family word became something other than its mechanical replacement (`iadd`, `inspector`, `inspection`, `cleared`), 491 lines, and every line where a backticked `` `seal` `` became `` `iadd` ``, 151 lines. That list is whole for the lines the range changed. It is a sample for a sentence the rename made false without changing its own words, such as a pronoun whose antecedent moved, which finding 2 is. The unchanged lines around each hunk were read only where a finding or a claim sent the round there.

## Findings

### 1. Two Korean lines of the writing-style skill took the rename of `seal` in a sense they do not mean

```iadd
severity: should
location: `skills/writing-style/SKILL.md:175`, `skills/writing-style/SKILL.md:273`
evidence: executed `git grep -n -F '만들어 낸 말' -- . ':!iadd/threads'` and ``git grep -n -F '절의 `iadd`' -- skills/writing-style``; read `skills/writing-style/SKILL.md:175`, `skills/writing-style/SKILL.md:228-240`, `skills/writing-style/SKILL.md:269-273`, and the same lines of `git show origin/release/v0.40.0:skills/writing-style/SKILL.md`
```

Why it matters: every agent that writes Korean prose opens this file, and both lines now tell it something the tree contradicts.

Line 273 closes the paragraph on terms the repository defines with *사례도 그 절의 `iadd` 다*, the example being the one in *여럿이 가질 수 있는 것은 누구 것인지 밝힌다*. At the base the line read *그 절의 `seal` 이다*, and that section's table opened with the row `the seal`. At the target the row is `the inspection` (`skills/writing-style/SKILL.md:235`). The section holds no `iadd`. Phase 7's global rule renamed every backticked `` `seal` `` to `` `iadd` `` (`trail/phases/phase-7.md`, the paragraph opening **The root and the template were moved**), and here the word named the record, which is *inspection*.

Line 175, under *용어는 실물을 확인하고 고른다*, gives `inspector` as an example of a word the product coined, which a Korean text keeps in English. `frame/design.md` *The Korean names* gives the inspector the Korean name 검수자, grounded in this same section (`frame/design.md` G14), and `docs/method/iadd.md` *The names* states that a Korean document names the inspector 검수자. `README.ko.md` lines 26 and 175 do so. An agent following line 175 keeps `inspector` in English where the definition gives 검수자. At the base the example was `seal`, which the Korean README then kept in English. The fix keeps the line's point with a coined name the Korean documents do keep in English: `proofer` (`README.ko.md` line 38).

The two `git grep` runs printed only these two lines. A statement of the same fact in other words is outside what they find, so they are a sample.

```markdown
- **고유 용어인가** — 그 제품이 만들어 낸 말(`mark`, `proofer`, `crafter`)이면 영어를 그대로 쓰고 첫 등장에서 실체를 괄호로 푼다. 억지 번역어를 만들면 원문 문서·코드와 대조가 끊긴다.
```

```markdown
것은 위의 *여럿이 가질 수 있는 것은 누구 것인지 밝힌다* 를 따르고, 사례도 그
절의 `inspection` 이다.
```

### 2. The settle's sentence on its own commits now points at the old trailer, and phase 7's record says it names the new one

```iadd
severity: should
location: `skills/settle/SKILL.md:233-234`, `iadd/threads/1795798115-the-plugin-is-named-for-the-seal/trail/phases/phase-7.md:55`
evidence: executed `git grep -n -F 'that trailer with no route chosen' -- . ':!iadd/threads'`; read `skills/settle/SKILL.md:228-236`, `skills/settle/SKILL.md:459`, `git show origin/release/v0.40.0:skills/settle/SKILL.md` lines 229-232, `iadd/threads/1795798115-the-plugin-is-named-for-the-seal/trail/phases/phase-7.md:55`
```

Why it matters: the settle session reads step 5 to tell the routes the orchestrator chose from commits that chose none, and the sentence now gives two readings of which trailer a settle's own commit carries.

At the base, step 5 named the trailer `Seal-Routing: no work item` and then said *A settle's commit carries that trailer with no route chosen and is not one*. Phase 7 renamed the trailer to `IADD-Routing: no work item` and inserted, between the two, the sentence that commits of earlier releases carry `Seal-Routing: no work item`. *That trailer* now follows that sentence, so its nearest antecedent is `Seal-Routing: no work item`. A settle's commit carries `IADD-Routing: no work item` (`skills/settle/SKILL.md:459`). A settle that reads *that trailer* as the old one counts each settle commit of this release and later ones, whose trailer reads `IADD-Routing: no work item`, among the routes chosen with no work item. `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* asks a text an agent follows to have one reading.

Claimed: `trail/phases/phase-7.md` line 55 says *The sentence on the settle's own commits says `IADD-Routing: no work item`*. Found: `skills/settle/SKILL.md:233-234` says *that trailer* and names no spelling. The fix below makes the claim true, so the phase record needs no edit of its own.

The `git grep` printed this one line. A statement of the same fact in other words is outside what it finds, so it is a sample.

```markdown
   renamed the plugin IADD carries the trailer as `Seal-Routing: no work
   item`, and `git log --grep` on that spelling lists those. A settle's
   commit carries `IADD-Routing: no work item` with no route chosen and is
   not one.
```

### 3. The Korean README still forbids translating the product name as a seal

```iadd
severity: should
location: `README.ko.md:28-29`
evidence: executed `git grep -n -F '도장 체인' -- . ':!iadd/threads'`; read `README.ko.md:25-31`, `README.md:24-29`, and the same lines of `git show origin/release/v0.40.0:README.ko.md`
```

Why it matters: `README.ko.md` is the first page a Korean reader opens, and this sentence keeps the plugin's old identity in front of that reader. `frame/design.md` *User scenarios & acceptance*, the row *The plugin's old identity is gone*, is held by search A3, which reads no Korean rendering of the old name.

The paragraph says the IADD process is a product name, so it is not translated, *"도장 체인"이나 "인장 과정"처럼 옮기지 않습니다*. Both phrases render the word *seal*, from the old name AgenticSeal and *the AgenticSeal process*. The name is now IADD, which no reader would render as either phrase. The English edition says only *It is a product name and is not translated* (`README.md:26-27`), and holds no such example.

The `git grep` printed this one line. A statement of the same fact in other words is outside what it finds, so it is a sample.

```markdown
저장소에서 이 과정을 가리킬 때도 이 이름을 씁니다. 제품 이름이므로 번역하지
않습니다. 검수는 마지막 에이전트의
```

The fix pass rewraps the paragraph if `tests/behaviour/test_docs_line_wrap.py` asks for it.

### 4. A test docstring renamed the plain word *guarantee* of contract rule 13 to *inspection*

```iadd
severity: should
location: `tests/skills/test_stamp.py:2034`
evidence: executed `git grep -n -i 'guarant' HEAD -- . ':!iadd/threads' ':!docs/experiments'` and `git grep -n -B2 'rule 13' -- . ':!iadd/threads' ':!docs/experiments'`; read `tests/skills/test_stamp.py:2030-2037` and `git show origin/release/v0.40.0:tests/skills/test_seal_stamp.py` lines 2024-2031
```

Why it matters: this is the failure the plan names in *Technical context*, **The failure scenario of the chosen approach**, a sense misread where *guarantee* is the plain word of contract rule 13. `frame/design.md` *The words* keeps that word: *guarantee, in a platform guarantee and other plain uses*, unchanged.

The docstring of `test_refuses_to_claim_a_file_that_reads_and_labels_but_does_not_draw` read, at the base, *the draw before the claim is faked to fail for one file's rows, to remove that guarantee (contract rule 13; ...)*. The guarantee removed is the platform's, the one rule 13 names. At the target it reads *to remove that inspection*, and nothing in that case removes an inspection. The case pins the stamp's claim and not the frame, so its docstring is read by whoever next edits the case, and it now misstates what the case does.

Claimed: `trail/phases/phase-4.md` line 17 says that plain uses of *guarantee* stay, *the cases that name a platform's guarantee* among them. Found: this one did not. The `git grep` on `rule 13` with two lines before each match found no other renamed word beside a citation of the rule. The `guarant` grep lists every remaining *guarantee* at the target, and each one is a plain use. These two searches are a sample: a plain *guarantee* renamed in a sentence that neither cites rule 13 nor says *platform* would escape them.

```python
        """Every file the module reads also draws, so the draw before the
        claim is faked to fail for one file's rows, to remove that guarantee
        (contract rule 13; #1017, round 3's s4). The file is the older one, so
```

## Confirmations

What matched: the searches of `frame/design.md` *The searches* print at `32719b79` what the acceptance table of `frame/design.md` *User scenarios & acceptance* states, executed. A1, A2, A3, A6 and A9 print nothing. A4 prints `skills/settle/SKILL.md:232` and the eight `.specseal/` lines. A5 prints `evals/scripts/noninferiority.py:299`, `tests/evals/test_noninferiority.py:650-654`, `tests/skills/test_chain_check.py:2964` and `:3168`, `tests/text/test_the_record_is_written_in_words.py:34` and `:68`, and `iadd/follow-up.md:48`. A7 prints 12 lines, all in `assets/seals/README.md`, and each one names a file as a release tag holds it or says what a release from 0.16.0 to 0.25.0 read. A8 prints `evals/behaviour/proofer/seeded-ea73e94f/prompt.md:5` and `iadd/follow-up.md:48`. This matches `trail/phases/phase-9.md`.

What matched: every remaining `agentic` outside the records, `docs/experiments/`, `LICENSE` and the repository's address names the routing answer, executed with `git grep -n -i agentic` and each of its 39 lines read. The lines A3's filter hides hold no use of the word as the plugin, as `trail/phases/phase-9.md` says.

What matched: `lib/optin.py#home_paths`, `#home_at` and `#home_name` read two places, `<repo>/iadd/` and then `<git-common-dir>/iadd/`, and the opening paragraph of `skills/core/SKILL.md` states the same two in the same order. Read.

What matched: `skills/code-review/scripts/chain_check.py#inspection` refuses a `cleared` block whose commit another path follows as `LAPSED`, and an absent file, a verdict other than `cleared`, and a commit HEAD does not descend from as `NOT_CLEARED`. `docs/forms/the-inspection.md` *The three states* says the same. Read at `chain_check.py:1700-1800`.

What matched: `skills/implement/scripts/iadd.py#destination_root` refuses `--into shared` where the project's own `iadd/` stands, as `changelog.md` *Removed* says. Read.

What matched: each principle of `docs/method/iadd.md` *The principles* says what the section it cites says. `gaps.md` *Not verified* names the proofer as this row's answerer. The round opened each cited section and read it against the principle: `skills/core/SKILL.md` *Each agent judges its own target, independently of the others*, *Judgment is spent where meaning is the question, and a script answers the rest*, *A judgment stands on a source document, and is written down with both*, *Asking a person is the most expensive step*, the table of *Judgment is not licence to skip a party*, *The rule a mechanism is kept against* and *A document is cut by who opens it and at which step, so a party opens only what its step needs*; `docs/running/the-agent-set.md` *The party that draws a contract is not the party that executes it*; and `docs/forms/the-inspection.md` *The three states*. Read.

What matched: the plain uses of *guarantee* that `trail/phases/phase-4.md` lists stand at the target. They are contract rule 13, `CONTRIBUTING.md:398`, `skills/verify/scripts/pact_check.py:181`, `skills/verify/scripts/session_cost.py:550` and `:3644`, and `tests/run_tests.py`. Finding 4 is the one the phase missed. Executed.

What matched: the broad gate's labels are honest. Each phase's row of `gaps.md` *Not verified* names the orchestrator as the answerer of the broad run, and no record claims the suite passed. Read.

What matched: `chain_check.py --baseline origin/release/v0.40.0 --worktree` printed no notice at a line of `frame/design.md` naming a test pin or a copy. Executed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The unchanged lines around each hunk of the Python, shell and YAML files, and the bodies of the renamed files beyond their changed words. The round read the changed words, as the paragraph above the findings says, and opened whole only the functions it names. A sentence made false by a change elsewhere, as in finding 2, is found there only by reading | the range's Python, test and workflow files | the next round, and the orchestrator's broad run for behaviour |
| The eval cases under `evals/behaviour/`, which the word diff left out. `tests/behaviour/test_evals_layout.py` holds the generated ones to `evals/scripts/rule_cases.py`, whose changed lines were read; the replay and seeded cases are `frame/questions.md` Q2's | `evals/behaviour/` | the repository owner, at the next run of `evals/scripts/noninferiority.py` |
| The suite, the lint and the format check over the branch, under contract rule 2 | the `Broad gate` key of `iadd/config.json` | the orchestrator, at the broad run |
| The `workflow_dispatch` run of `tests` in progress on this branch, which the round did not wait on | the repository's Actions run for the branch | the orchestrator |
| Whether `TRADEMARKS.md` should reserve the name IADD, which `frame/questions.md` Q1 holds open | `TRADEMARKS.md` | the repository owner |
| `docs/experiments/`, which `frame/design.md` *Scope* leaves out | `docs/experiments/` | no one this round; the frame excludes it |

## Probes

| Command | Result |
|---|---|
| `git diff -M --word-diff=porcelain -U0 origin/release/v0.40.0...HEAD -- . ':!iadd/threads' ':!evals/behaviour'`, paired by a script under the round's scratch directory | 38112 lines; 3775 distinct pairs of removed and added runs; 202 changed lines whose removed run held *guarantee*, and 491 where a `seal`-family word took a non-mechanical replacement |
| searches A1 to A9 of `frame/design.md` *The searches* at `32719b79` | the output the first confirmation names |
| `git grep -n -i 'guarant' HEAD -- . ':!iadd/threads' ':!docs/experiments'` | 21 lines; `tests/skills/test_stamp.py:2034` is the one plain use that was renamed, and it no longer holds the word |
| `git grep -n -F '만들어 낸 말' -- . ':!iadd/threads'`, and ``git grep -n -F '절의 `iadd`' -- skills/writing-style`` | `skills/writing-style/SKILL.md:175`, and `skills/writing-style/SKILL.md:273` |
| `git grep -n -F 'that trailer with no route chosen' -- . ':!iadd/threads'` | `skills/settle/SKILL.md:234` |
| `git grep -n -F '도장 체인' -- . ':!iadd/threads'` | `README.ko.md:29` |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.40.0 --root <the checkout> --worktree`, before the record was written | exit 0; it named no round record, no `trail/gate.md` and no `inspection.md`, and printed no notice at `frame/design.md` |
