# Review round 1: 1794376287-check-lines-ride-in-every-preload

```seal
target: f105d4b68 against 896f50cab
```

This is the first round, so no earlier record carries a coordinate, and every fact below was established in this round. The range `896f50cab..f105d4b68` holds the routing (`f47b1d5ae`), the frame (`bc05d454d`), the build (`e9658c727`), the phase record, closing memo and changelog fragment (`6f0bd30f6`), the orchestrator's fold of the build's departure (`9b89c1395`), and `pr.md` with the title row (`f105d4b68`) (executed, `git log --oneline`). Outside `seal/`, the diff changes the five definitions under `agents/`, `skills/agent-contract/SKILL.md`, `skills/settle/rule-changes.md` and eight test modules, 15 files (executed, `git diff --stat`). Every command ran in a `git clone --no-local` at `f105d4b68` under the round's scratch directory, `<scratchpad>/1794376287-check-lines-ride-in-every-preload/round-1/clone`. The branch worktree received this record and nothing else.

The records read whole at the target are `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md` and `trail/phases/phase-1.md`. Both language keys of `seal/config.json` are English, so no `pr.<lang>.md` stands. No `seal/parity.json` stands, so no original is compared. The issue was read through `gh issue view 1475` from the main checkout, since the clone has no GitHub remote. Its *Decision* records the owner's choice of deletion on 2026-11-11, with no index file and no strip at the `dist` build, and its *Done when* asks for zero lines in the six files and a passing `seal rules --check` with no test or eval removed.

The axes for this change are: the lines removed from every preloaded file; the reach of the old fact, that a rule held by a case carries a check line, across every tracked file; the test units that sliced or asserted on a removed line; the new case D2 and its group; the sealer rule removed and the citation that moved; the preload sizes; and the records' statements against the target. The comparison table's runtime rows (authorization, query scope, concurrency, security) have no code to walk here. The diff deletes prose lines, adds one paragraph and one parametrized case, and re-slices test units, and it adds no executable path outside the suite.

## Findings

### 1. D1 tells a person to find a rule's cases by `git grep` on the file's path, and six of the cases name the file only by its name

```seal
severity: should
location: `skills/settle/rule-changes.md:122-123`, `seal/threads/1794376287-check-lines-ride-in-every-preload/changelog.md:4`, `seal/threads/1794376287-check-lines-ride-in-every-preload/frame/design.md:85-86`, `seal/threads/1794376287-check-lines-ride-in-every-preload/frame/plan.md:11`
evidence: executed, for each target of each `check:` line of the six files at `896f50cab`, `git grep -q -F <file's path> -- <target>`, then `git grep -q -F <file's name> -- <target>` where the first found nothing; read `tests/text/test_broad_gate_rule.py:219`, `tests/text/test_edits_go_through_the_edit_tool.py:28-29`, `tests/behaviour/test_a_phase_hands_the_next_one_a_record.py:46`, `tests/text/test_a_moved_rule_leaves_its_definition.py:671`
```

Why it matters: D1 is now the one statement of how a person finds the cases of a rule in a definition or the contract, because the lines that named them are gone. It says the person "finds them by `git grep` on the file's path and under `evals/behaviour/`" (`skills/settle/rule-changes.md:122-123`), and the release note says the same (`changelog.md:4`, "finds its cases by `git grep` on the file's path"). Many cases build the path from its parts, so the path string never appears in them.

I ran the probe over the 47 distinct pairs of a file and a target that the base's 41 lines name. In 25 pairs the target holds the file's path. In 6 it holds only the file's name: `tests/text/test_broad_gate_rule.py:219` reads `read("agents", "sealer.md")`, `tests/text/test_edits_go_through_the_edit_tool.py:28-29` builds both `CONTRACT` and `CRAFTER` from tuples, `tests/behaviour/test_a_phase_hands_the_next_one_a_record.py:46` and `tests/text/test_a_moved_rule_leaves_its_definition.py:671` use `os.path.join`, and `tests/text/test_the_rules_have_one_owner.py:23` and `tests/text/test_the_verifying_round_is_bounded_not_cheapest.py:38` build the proofer's path from a tuple. In 16 it holds neither. Fifteen of those are eval directories, which D1's second clause covers. The last is `tests/skills/test_settle.py`, for the proofer's reference-root rule, which neither the search nor `evals/behaviour/` reaches. So a person following D1 word for word misses 7 of the 47 pairs.

The frame measured something else. G13 (`frame/design.md:21`) counted the targets holding "the definition's file name, or `agent-contract` for the contract", and the issue counted those carrying "their definition's name". D1 at `frame/design.md:85-86` turned "name" into "path". `frame/plan.md:11` adds two related claims. It says "`git grep` on the definition's path finds most cases". It also says that for `tests/skills/test_settle.py` the person "opens `evals/behaviour/` and reads, which D1 tells them to do", and that directory does not hold that file.

The fix for `skills/settle/rule-changes.md:118-126` keeps D1's other sentences and holds 88 columns:

```markdown
**A file every spawn preloads carries no check line.** That is each agent
definition, `agents/<name>.md`, and each skill its `skills:` list names,
such as `skills/agent-contract/SKILL.md`. Every spawn that preloads such a
file pays for each line in it, and no agent acts on one. A rule there is
still held by its cases. A person changing it finds most of them by
`git grep` on the file's name, such as `crafter.md` or `agent-contract`,
since a case often builds the path from its parts, and the rest under
`evals/behaviour/`. `seal rules --check` reads these files as it reads
every rule file, and a suite case refuses a check line in any of them.
check: tests/text/test_every_agent_reads_the_contract.py
```

The fix for `changelog.md:4`, in the sentence that names the search:

```markdown
A person changing such a rule finds most of its cases by `git grep` on the file's name, such as `crafter.md`, since many cases build the path from its parts.
```

This snippet does not reach the frame's own statements, and the fix pass, or whoever folds the frame, owes them too. They are D1's block at `frame/design.md:85-86`, which should read as the paragraph above, and `frame/plan.md:11`, where "the definition's path" becomes "the definition's file name" and the sentence on `tests/skills/test_settle.py` stops saying `evals/behaviour/` holds it. `trail/phases/phase-1.md:25` says D1's words went in unchanged, and it describes the build commit it names, so it stays.

### 2. The README says a rule with no `check:` line is held by review alone, and every rule of the definitions and the contract now has none while cases still hold them

```seal
severity: should
location: `README.md:441-442`, `README.ko.md:436-438`, `seal/threads/1794376287-check-lines-ride-in-every-preload/frame/design.md:18`, `seal/threads/1794376287-check-lines-ride-in-every-preload/frame/design.md:58`
evidence: read `README.md:433-442`, `README.ko.md:429-438`, `skills/settle/rule-changes.md:118-126`; executed `grep -c '^check:'` over the six files at `f105d4b68`, and `bin/test` over `tests/text/test_the_agent_contract_holds_the_universal_rules.py` within the narrow run of `## Probes`
```

Why it matters: the bullet under `## Limits` reads "`seal rules --check` proves that a named test exists, not that it asserts the rule. A rule with no `check:` line is held by review alone." (`README.md:441-442`). `README.ko.md:436-438` says the same in Korean. At the base this was true in practice, because a rule held by a case carried a line. After the work, the six preloaded files carry no line (S1, executed), and D1 says "A rule there is still held by its cases" (`skills/settle/rule-changes.md:121-122`). For example, contract rule 1 is still held by `tests/text/test_the_agent_contract_holds_the_universal_rules.py`, which passes in this round's narrow run. A person who reads the README's limits and then a definition is told that the definition's rules are held by review alone. That is false, and it is the statement D1 was written to correct.

The frame kept the README by G10 (`frame/design.md:18`, "`README.md:322` and `:441-442`, and `README.ko.md:322` and `:437`, speak of the rules of a policy document, and stay") and *Scope*, Out (`:58`). `README.md:322` does say "A rule a policy document states". The `## Limits` bullet has no such qualifier, and the list it stands in is about the plugin's commands. So that reading of G10 does not hold for `:441-442`.

The docstring of `.github/scripts/rules.py:39-40` says "a rule written with no `check:` line is read by review alone". I weighed it and leave it. It sits under **How it errs:** and describes what the reader cannot see, which stays true. It is also a docstring that no agent acts on.

The fix for `README.md:441-442`:

```markdown
- **`seal rules --check` proves that a named test exists, not that it asserts
  the rule.** It reads no rule without a `check:` line. In a policy document
  such a rule is held by review alone. The rules of the agent definitions and
  the contract carry no line, and their cases still hold them
  (`skills/settle/rule-changes.md` *A rule has one shape*).
```

The fix for `README.ko.md:436-438`:

```markdown
- **`seal rules --check` 는 적어 둔 테스트가 있다는 것만 증명합니다.** 그
  테스트가 규칙을 확인한다는 뜻은 아닙니다. `check:` 줄이 없는 규칙은 읽지
  않습니다. 정책 문서에서 그런 규칙은 리뷰만 지킵니다. 에이전트 정의와 계약의
  규칙은 줄이 없어도 그 테스트가 지킵니다
  (`skills/settle/rule-changes.md` *A rule has one shape*).
```

The fix touches files that *Scope*, Out names as unchanged, so the fold owes `frame/design.md:18` and `:58` as well, with S7's file list (`frame/design.md:72`). Any case that reads the README editions against each other is the fix pass's to run. This round did not open one.

## Confirmations

What matched: S1. At `f105d4b68`, `grep -c '^check:'` prints 0 for each of `agents/crafter.md`, `agents/framer.md`, `agents/proofer.md`, `agents/sealer.md`, `agents/tracer.md`, `skills/agent-contract/SKILL.md` and `skills/core/SKILL.md`. At `896f50cab` the six files held 10, 7, 7, 6, 2 and 9, which is 41, and the core held 0 (executed). The 41 deleted lines are the ones *Scope* item 1 lists, and each sat at the end of its paragraph, so the diff joins no two paragraphs (read, the diff).

What matched: S2 and G12. `git diff --name-status --diff-filter=DR 896f50cab HEAD -- tests evals` prints nothing, and each of the 32 distinct targets (57 in all) passes `test -e` at the target (executed).

What matched: S3 and G7. `bin/seal rules --check` exits 0 and prints `seal rules: all 179 check lines in 69 rule files hold.` at `f105d4b68`, and `all 219 check lines in 69 rule files` at `896f50cab`. That is 41 fewer plus D1's one (executed). `bin/seal rules agents/sealer.md` prints `(no check line)` under every heading, and so does the contract, 19 times (executed). G7's "16 lines in 8 other files under `skills/`" matches `git grep -c` at the base (executed).

What matched: S4 and D3. `wc -c` at both commits gives the core 9,322 B, the contract 12,806 B then 12,029 B, and the preloads 32,343 to 30,828 (crafter), 37,179 to 35,884 (framer), 32,891 to 31,474 (proofer), 33,186 to 31,866 (sealer) and 25,046 to 24,148 (tracer) (executed). The sealer's 543 B is G4's 458 B of lines, plus 99 B for the rule and its blank line (75 + 1 + 21 + 1 + 1), minus the 14 B of "(rule 2)" with its rewrap. The changelog's five figures match these.

What matched: the crafter's departure. Claimed: the removed rule held `agents/sealer.md`'s only citation of rule 2, which `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py#test_the_sealer_cites_contract_rule_2` reads. Found: that case asserts `"rule 2" in text` over the whole definition (`sealer_text()` reads `SEALER` whole), and step 1 now ends "Nothing broad is run in its place (rule 2)." (`agents/sealer.md:65-66`). The case passes in this round's run (executed). Step 1 states the verdict for an absent record and for one followed by another path, the stale case, so the removed rule's first sentence pointed at what step 1 states whole (read). No tracked file outside `seal/threads/` holds the removed rule's words, "missing or stale gate", "earns what step 1" or "holds the run rule 2" (executed, `git grep -i`), and no file under `evals/behaviour/sealer/` names the rule or the definition (executed). Whether the sealer still withholds in the two evals the line named is `gaps.md`'s row 3, which names the owner, and this round did not run an eval.

What matched: S6 and G8. The slices of *Scope* items 6 to 9 read the text they read at the base. I compared each old slice at `896f50cab` with its new slice at `f105d4b68`, whitespace collapsed, for `framer_rule`'s one lead "Bound each call, not the reading.", the crafter's two leads, and the sealer's *The guarantee covers HEAD*, and all four pairs are equal (executed, an inline `python3` over `git show`). The assertions *Scope* items 5 and 10 remove each asserted a line now gone, and the clause and phrase pins around them stay (read, the diff). The docstrings of items 5, 6, 10 and 11 lose exactly the clauses on a check line (read). No string constant under `tests/` that slices a preloaded file at `"check: "` or `^check` is left. The remaining hits read `skills/implement/SKILL.md`, `docs/checks/the-stamp.md`, `skills/writing-style/SKILL.md`, `docs/forms/the-round-record.md` or `skills/legacy-parity/SKILL.md`, which keep their lines (executed, `git grep -n -E`).

What matched: D2, read against its group. `tests/text/test_every_agent_reads_the_contract.py#test_a_file_every_spawn_preloads_carries_no_check_line` derives its set from each definition's `skills:` list through the module's own `split` and `listed_skills`, the shape case's helpers. It reads each file through `rules.check_lines`, the reader `seal rules` uses, loaded by `conftest.load`, and its message names the file, each line and D1's section (read, `:161-189` and `.github/scripts/rules.py:174-182`). No other case in the module, in `tests/github/test_rules.py`, or in the two other callers of `check_lines` (`tests/behaviour/test_docs_line_wrap.py:242`, `tests/behaviour/test_this_repository_passes_its_own_checks.py:63`) asserts that a file holds no check line (executed, `git grep -n 'check_lines('`, each caller read). `bin/seal layout --pairs` names no pair touching the module (executed). The crafter's claim that D2 was red at the base and red with one line restored at the build commit is not re-run here. Reading settles that it bites: a restored `check: ` line outside a fence is a row `check_lines` returns, and the case asserts the list is empty. The `seen red` is the sealer's sample to re-run.

What matched: the reach of the old fact outside the six files, apart from the two findings. `git grep -n -i -E 'check(:`)? lines?'` outside `seal/threads/`, and the docstrings it lists under `tests/` that say a file names a module on its `check:` line, all name a policy document under `docs/` that keeps its lines (executed, each hit read). `skills/implement/SKILL.md:177-182` sends a rule's line "in its home under `docs/`, or in the *Verifiable how* cell", so it never sends one into a preloaded file, as G15 says (read). The three sentences G7 keeps, now at `agents/crafter.md:173`, `agents/framer.md:60` and `agents/proofer.md:111`, concern the rules of files that keep their lines (read). `CONTRIBUTING.md:62-65` speaks of a `check:` target a change renames or removes, which stays true (read). That search is a sample, since a paraphrase of the fact is an open class, and it found finding 2.

What matched: the narrow run. `bin/test` over the eight changed test modules, `tests/github/test_rules.py`, `tests/behaviour/test_this_repository_passes_its_own_checks.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/text/test_the_agent_contract_holds_the_universal_rules.py` and `tests/text/test_broad_gate_rule.py` gave 493 passed, exit 0 (executed). `uvx ruff check` and `uvx ruff format --check` over the eight changed test modules exit 0 (executed). The crafter's 483 passed and 1 failed at `e9658c727`, and its phase-boundary 3,238 passed, were not re-run.

What matched: `pr.md`. Its four quotes stand word for word at `frame/plan.md:17`, `:18`, `:49` and `:50`, the rows their coordinates name (read).

What matched: `changelog.md`, apart from finding 1. The *Removed* figures are D3's. The *Changed* item's set, "today `skills/core/SKILL.md` and `skills/agent-contract/SKILL.md`", is what every definition's `skills:` list names (read, the five frontmatters). Its sentence "Without it, `seal rules --check` would resolve such a line and pass" matches `tests/github/test_rules.py:518-527` and `RULE_FILES` keeping `agents/*.md` (read). The *Process changes* row agrees with the issue's *Decision* (read).

What matched: `gaps.md`. Row 1 labels the broad gate unverified and names the orchestrator. Row 2 calls the phase-boundary list a sample and gives the rest to the broad gate. Row 3 names the owner for the sealer evals. Each is honest against `trail/phases/phase-1.md:50`. The file is new in the range, so no row left it (read).

What matched: `routing.md`, `frame/questions.md`, and the frame's dated statements. The routing agrees with the issue's *Decision*. `frame/questions.md` holds no row, and each line of its head points at a section that stands (read). G4, G6, G13 (41 of 57 targets by name, executed in the probe of finding 1), G14's 97 B and 179 B (flattened rule, and line with its newline, executed `wc -c`), *Scope* items 1 to 12, S7's 15 files, and `.claude-plugin/plugin.json`'s `0.37.3` at the base (`frame/plan.md:43`) all hold at the target (executed or read as named). `trail/phases/phase-1.md:15` gives D3's sealer figure as 31,852 B, the frame's figure at the commit the record describes, which `9b89c1395` folded. The record states that commit and stays.

What matched: the chain check over this record. `python3 skills/code-review/scripts/chain_check.py --baseline 896f50cab --root <the branch worktree> --worktree` exited 0. It printed no notice at a line of `frame/design.md` naming a test pin or a copy. Its other lines say that findings 1 and 2 stand open, that no pull request exists yet, and that git carries no `trail/gate.md` and no `guarantee.md`, which the orchestrator's broad run and the sealer write after the rounds (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the sealer withholds on a missing or a stale `trail/gate.md` now that the rule naming the two evals is gone | `evals/behaviour/sealer/rule-sealer-no-gate/`, `evals/behaviour/sealer/rule-sealer-stale-gate/` | the owner, by the release's eval run, as `gaps.md` row 3 names |
| The broad gate at HEAD, and the test files outside this round's narrow run that read a changed file | the work item's HEAD | the orchestrator, by `seal gate --record` |
| D2's `seen red` at the base and with one line restored, claimed in `trail/phases/phase-1.md:21` and `:29` | `tests/text/test_every_agent_reads_the_contract.py:177-189` | the sealer, by its sample |

## Probes

| Command | Result |
|---|---|
| For each target of each `check:` line of the six files at `896f50cab`, `git grep -q -F <path> -- <target>`, then `git grep -q -F <name> -- <target>` (finding 1) | 47 distinct pairs: 25 hold the path, 6 only the name, 16 neither, which are 15 eval directories and `tests/skills/test_settle.py` |
| `bin/test` over the 13 modules named under the narrow run, `-q` | 493 passed, exit 0 |
| `bin/seal rules --check` at `f105d4b68`, then at `896f50cab` (the clone checked out there and back) | `all 179 check lines in 69 rule files hold.`; `all 219 check lines in 69 rule files hold.` |
| `bin/seal layout --pairs` | exit 0; no pair names `tests/text/test_every_agent_reads_the_contract.py` |
| an inline `python3` comparing each old slice at `896f50cab` with its new slice at `f105d4b68`, whitespace collapsed | four pairs, each equal |
