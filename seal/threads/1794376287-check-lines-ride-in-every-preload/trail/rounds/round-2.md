# Review round 2: 1794376287-check-lines-ride-in-every-preload

```seal
target: ab8bddb3a, fixes f105d4b68..ab8bddb3a
```

This is the verifying round over round 1's two findings. The range `f105d4b68..ab8bddb3a` holds round 1's record (`4cb3f0096`), the framer's fold of both findings (`44bf80414`), fix pass 1 (`bceb31f1c`), its `gaps.md` row (`43b90d4ad`) and the two close blocks (`ab8bddb3a`) (executed, `git log --oneline`). Outside `seal/`, the range changes `README.md`, `README.ko.md` and `skills/settle/rule-changes.md` (executed, `git diff --stat`). Every command ran in a `git clone --no-local` checked out at `ab8bddb3a`, under the round's scratch directory `<scratchpad>/1794376287-check-lines-ride-in-every-preload/round-2/clone`. The branch worktree received this record and nothing else.

The records read whole at the target are `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/rounds/round-1.md`. Both language keys of `seal/config.json` are English, so no `pr.<lang>.md` stands. No `seal/parity.json` stands, so no original is compared.

Carried from round 1 and not re-established: S1's zero lines in the six files, S2's 32 targets, S4's preload figures, the four re-sliced units reading their base text, and D2 read against its group. The fix range touches none of the files those rest on. Re-derived here: round 1's probe of finding 1, `seal rules --check`, every verdict, and the new units of the fix diff, which are D1's rewritten sentences, the README bullet in both editions, the changelog item, the `gaps.md` row and the frame's folds.

## Findings

### 1. The README now says every rule of the agent definitions and the contract is held by its cases, and some of those rules have no case

```seal
severity: should
location: `README.md:442-445`, `README.ko.md:437-440`, `seal/threads/1794376287-check-lines-ride-in-every-preload/changelog.md:4`, `skills/settle/rule-changes.md:121-122`, `seal/threads/1794376287-check-lines-ride-in-every-preload/frame/design.md:50`, `seal/threads/1794376287-check-lines-ride-in-every-preload/frame/design.md:85-86`
evidence: executed `bin/seal rules agents/framer.md` and `bin/seal rules skills/agent-contract/SKILL.md` at `896f50cab`, and `git grep -l -i -F` of each rule's words (`count of a list`, `beside the list`, `bend the code`, `shaped around a wrong check`, `fix the check or report`, `A check that refuses`) over `tests`, `evals`, `lib`, `bin` and `.github`; read `README.md:441-445`, `README.ko.md:436-440`, `agents/framer.md:207-217`, `skills/agent-contract/SKILL.md:191-196`, `tests/text/test_the_agent_contract_holds_the_universal_rules.py:16-20`
regression: round-1#2
```

Why it matters: the `## Limits` bullet now reads "The rules of the agent definitions and the contract carry no line, and their cases still hold them" (`README.md:443-444`). The Korean edition says the same, "에이전트 정의와 계약의 규칙은 줄이 없어도 그 테스트가 지킵니다" (`README.ko.md:438-439`). Both say that every rule in those files is held by a case. A *Limits* section is where a person learns what the plugin does not guarantee, so a guarantee stated there too widely is read and relied on.

Not every rule there has a case. At `896f50cab`, before any line was deleted, `seal rules` printed `(no check line)` for 9 of the contract's 19 numbered rules, and the framer's `## Rules` held seven rules with no line (executed). Two of them have no case at all. The first is the framer's **A count of a list is stated once, beside the list.** (`agents/framer.md:207-217`). No string of its words stands anywhere under `tests`, `evals`, `lib`, `bin` or `.github` (executed). The second is contract rule 18, *A check that refuses correct code is fixed or reported* (`skills/agent-contract/SKILL.md:191-196`), and no string of its words stands there either (executed). Its module's shape case reads only that the heading's number is listed. Its docstring says "A rule's sentences are not pinned here" and "A sentence deleted from inside a rule that keeps its heading is left to review" (`tests/text/test_the_agent_contract_holds_the_universal_rules.py:16-20`). Under the old bullet, these two rules were held by review alone, and they still are. The new bullet tells a person a case holds them. The search for their words is a probe, and a case that pins them in other words would escape it, so it settles only that no case quotes them.

The unit is the bullet that `bceb31f1c` rewrote in both editions. *Scope* item 13 (`frame/design.md:50`) says the bullet reads "the rules of the agent definitions and the contract carry no line, and their cases still hold them", and the fix pass wrote that. So the defect came from round 1's own snippet, which the framer folded word for word: it widened "a rule held by a case is still held" to every rule of the six files. The same reading stands in three other places. `changelog.md:4` says the rules of the definitions and the contract "are still held by their cases", and the release note is built from it. D1's "A rule there is still held by its cases." (`skills/settle/rule-changes.md:121-122`) is the passage the README cites, and it reads either way. D1's block in the frame (`frame/design.md:85-86`) holds the same sentence. Round 1's finding 2 was right that a case-held rule is not held by review alone. The fix only had to say both halves.

The fix for `README.md:441-445`, inside 88 columns:

```markdown
- **`seal rules --check` proves that a named test exists, not that it asserts
  the rule.** It reads no rule without a `check:` line. In a policy document
  such a rule is held by review alone. The agent definitions and the contract
  carry no line at all, so the command reads none of their rules: a rule there
  is held by the cases that read it where any do, and by review alone where
  none does (`skills/settle/rule-changes.md` *A rule has one shape*).
```

The fix for `README.ko.md:436-440`, inside 88 display columns:

```markdown
- **`seal rules --check` 는 적어 둔 테스트가 있다는 것만 증명합니다.** 그
  테스트가 규칙을 확인한다는 뜻은 아닙니다. `check:` 줄이 없는 규칙은 읽지
  않습니다. 정책 문서에서 그런 규칙은 리뷰만 지킵니다. 에이전트 정의와
  계약에는 `check:` 줄이 하나도 없어서, 이 명령은 그 규칙을 하나도 읽지
  않습니다. 그 규칙은 읽는 테스트가 있으면 그 테스트가 지키고, 없으면
  리뷰만 지킵니다 (`skills/settle/rule-changes.md` *A rule has one shape*).
```

The fix for the last sentence of `changelog.md:4`:

```markdown
The README's *Limits* now says that a rule with no `check:` line is held by review alone in a policy document, and that a rule of the agent definitions or the contract is held by the cases that read it where any do, and by review alone where none does.
```

The fix for D1 at `skills/settle/rule-changes.md:118-127`, inside 88 columns:

```markdown
**A file every spawn preloads carries no check line.** That is each agent
definition, `agents/<name>.md`, and each skill its `skills:` list names,
such as `skills/agent-contract/SKILL.md`. Every spawn that preloads such a
file pays for each line in it, and no agent acts on one. A rule there that a
case holds is still held by it. A person changing such a rule finds most of
its cases by `git grep` on the file's name, such as `crafter.md` or
`agent-contract`, since a case often builds the path from its parts, and the
eval cases among them under `evals/behaviour/`. `seal rules --check` reads
these files as it reads every rule file, and a suite case refuses a check
line in any of them.
check: tests/text/test_every_agent_reads_the_contract.py
```

These snippets do not reach the frame, and the fold owes it: *Scope* item 13 (`frame/design.md:50`) should say the bullet's last sentence as the README fix gives it, and D1's block (`frame/design.md:79-92`) should read as the D1 fix above. The row of `frame/plan.md:52` records the judgment as it was made on 2026-11-11, so it stays, and a new row records this one. `trail/rounds/round-1.md:73-89` states its own commit and stays. The fix pass runs `tests/behaviour/test_docs_line_wrap.py` and `tests/behaviour/test_both_editions_carry_the_same_folds.py` over the two editions.

```seal
verdict: fixed d322c0cb7
answer: The finding holds, and the four fixes went in as given. The `## Limits` bullet at `README.md:441-446` and `README.ko.md:436-441` reads as this round's two README fixes give it, which is *Scope* item 13 as the framer folded it at `e8830bd8d`. `changelog.md:4`'s last sentence reads as this round's fix. `skills/settle/rule-changes.md:118-128` reads as D1's block at `frame/design.md`; a `python3` check found the block's text in the file verbatim. After `d322c0cb7`, one `bin/test` command over `tests/text`, `tests/behaviour` and the 19 other test files fix pass 1 ran gave 4,669 passed and 9 skipped, with `tests/behaviour/test_docs_line_wrap.py` and `tests/behaviour/test_both_editions_carry_the_same_folds.py` among them, and `bin/seal rules --check` holds 179 lines.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: D1 no longer sends a person to the file's path. `skills/settle/rule-changes.md:118-127` reads word for word as D1's block at `frame/design.md:79-92`, whitespace collapsed (executed, an inline `python3` comparison). It sends the person to `git grep` on the file's name, and the eval cases to `evals/behaviour/`. I re-ran round 1's probe at `896f50cab`. Of the 47 distinct pairs of a file and a target, 25 hold the path and 6 hold only the name, so 31 are found by the name, which is "most". Of the 16 that hold neither, 15 are eval directories under `evals/behaviour/`, and the last is `tests/skills/test_settle.py` (executed). So the eval clause covers the 15, and the framer's change from round 1's "the rest" keeps `test_settle.py` out of a directory that does not hold it. `frame/plan.md:11` now says that neither route reaches `test_settle.py`, which matches the probe. `changelog.md:4` says "most of its cases by `git grep` on the file's name, such as `crafter.md`" (read). No tracked file outside `seal/threads/` still sends a person to a definition's path (executed, `git grep -n -i -E "file's path|definition's path"`; the four hits concern other files).

```seal
confirms: round-1#2
```
What holds: the bullet no longer says that a rule held by a case in a definition or the contract is held by review alone. `README.md:441-445` and `README.ko.md:436-440` say a policy document's rule with no line is held by review alone, and both cite D1 (read). `tests/behaviour/test_both_editions_carry_the_same_folds.py` and `tests/behaviour/test_docs_line_wrap.py` pass in this round's narrow run (executed). The bullet now says too much in the other direction, and that is finding 1.

What matched: S3. `bin/seal rules --check` exits 0 and prints `seal rules: all 179 check lines in 69 rule files hold.` at `ab8bddb3a`, which is the count the close of round 1's finding 1 claims (executed).

What matched: S7 after the fold. `git diff --name-only 896f50cab...HEAD -- ':!seal/'` lists 17 files: the 15 of *Scope* items 1 to 12 and the two READMEs of item 13 (executed).

What matched: the framer's fold at `44bf80414`. G10 now names the `## Limits` bullet at `README.md:441-442` and `README.ko.md:436-438`. Those are the lines it held at `f47b1d5ae`, the commit G10's section is dated to (executed, `git show f47b1d5ae:README.md`). G13's added sentences give the probe's 47, 25 and 6, which this round's re-run matches. *Scope*, Out now keeps only `README.md:322` and `README.ko.md:322`, S6 names the two README cases, and `## Rule changes` names the README bullet among what the work edits outside `docs/` (read).

What matched: `gaps.md` row 3. It says one `bin/test` command after `bceb31f1c` ran `tests/text`, `tests/behaviour`, `tests/test_censuses.py` and "the 18 test files a `git grep -l` on `README` and `rule-changes` listed outside those two directories". That `git grep -l` lists 20 files under `tests/` outside the two directories. Two of them, `tests/censuses.py` and `tests/conftest.py`, are not test modules, which leaves 18 (executed). The row calls the list a sample and names the orchestrator. The count of 4,669 passed and 9 skipped was not re-run. The row was added with no row taken out (read, the diff of `43b90d4ad`).

What matched: `pr.md`. Its four quotes stand word for word at `frame/plan.md:17`, `:18`, `:49` and `:50`, the rows their coordinates name, which the fold left in place (executed, `grep -n -F`).

What matched: the rest of the records that state the present. `routing.md`, `frame/questions.md`, the changelog's *Removed* items 1 and 3, its *Changed* item and its *Process changes* row are unchanged in the range, and nothing in the fix diff contradicts them (read). The close block of round 1's finding 1 gives D1's coordinate in the frame as `frame/design.md:77-91`, where the block stands at `:79-92`. That record states its own commit, and the slip misleads nobody who opens D1 by name.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the sealer withholds on a missing or a stale `trail/gate.md` now that the rule naming the two evals is gone | `evals/behaviour/sealer/rule-sealer-no-gate/`, `evals/behaviour/sealer/rule-sealer-stale-gate/` | the owner, by the release's eval run, as `gaps.md` row 4 names |
| The broad gate at HEAD, and fix pass 1's run of 4,669 passed and 9 skipped, which this round did not re-run | the work item's HEAD | the orchestrator, by `seal gate --record` |
| D2's `seen red` at the base and with one line restored, claimed in `trail/phases/phase-1.md:21` and `:29` | `tests/text/test_every_agent_reads_the_contract.py` | the sealer, by its sample |

## Probes

| Command | Result |
|---|---|
| For each target of each `check:` line of the six files at `896f50cab`, `git grep -q -F <path> 896f50cab -- <target>`, then the same with the file's name (round 1's probe, re-run) | 47 distinct pairs: 25 hold the path, 6 only the name, 16 neither, which are 15 eval directories and `tests/skills/test_settle.py` |
| `bin/seal rules <file>` for the five definitions and the contract at `896f50cab` (the clone checked out there and back) | the contract prints `(no check line)` under rules 3, 4, 12, 13, 14, 15, 17, 18 and 19; the framer's `## Rules` holds 7 lines among 14 rules |
| `git grep -l -i -F` of the words of the framer's count rule and of contract rule 18 over `tests`, `evals`, `lib`, `bin` and `.github` | no file |
| `bin/test` over `tests/behaviour/test_both_editions_carry_the_same_folds.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/skills/test_rule_changes.py`, `tests/text/test_every_agent_reads_the_contract.py`, `tests/behaviour/test_this_repository_passes_its_own_checks.py` and `tests/github/test_rules.py`, `-q` | 274 passed, exit 0 |
| `bin/seal rules --check` at `ab8bddb3a` | `all 179 check lines in 69 rule files hold.`, exit 0 |
