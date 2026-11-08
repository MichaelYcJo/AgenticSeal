# Review round 1: 1794096494-compare-reads-a-grader-with-a-string-target

```seal
target: b30ca3846 against release/v0.34.1
```

The round reviewed `8c2d60e14..b30ca3846` in a `git clone --no-local` of the repository at the target. It read `routing.md`, the three frame files, `gaps.md`, `changelog.md`, `pr.md` and `trail/phases/phase-1.md` whole at the target, and issue #1421 with its comments (none). No earlier round exists, so no fact was carried from one, and every fact below was established this round. The repository declares no `seal/parity.md` and no `Pact` row in `seal/config.md`, and `config.md` has no `Record language` row, so the record is in English.

Axes walked: inputs (the shapes `config.target` takes), exclusions and boundaries (a missing target, a string target, a mapping without `path`), error paths (the `AttributeError` that escaped `compare` and `regrade`, and whether the change adds a failure path: it adds none), response shape (the record row and the printed line), and the change's own axis, the version move into `release/v0.34.1`. Authorization, query scope, state transitions, concurrency and security have nothing to bite on: the change is one pure read of a local JSON side's field, with no new input crossing a process boundary.

## Findings

### 1. The design's reason for leaving out a `regrade` case is false: a `regrade` case needs no suite commit holding the grader

```seal
severity: should
location: `seal/threads/1794096494-compare-reads-a-grader-with-a-string-target/frame/design.md:31`
evidence: executed `bin/test tests/evals/test_tmp_regrade_string_target.py -q -p no:xdist`, once with the guard of `evals/scripts/noninferiority.py:363` removed and once at the target; read `evals/scripts/noninferiority.py:1428-1501`, `tests/evals/test_noninferiority.py:395-498`
```

Why it matters: the *Scope* Out bullet gives two grounds for leaving out a `regrade` case. The second one is "a `regrade` case needs a suite commit holding such a grader in the `_suites` fixture". The target contradicts it. `regrade` takes each case's graders from the side's own JSON. It compares the two suites only by their files other than `truth-` graders (`evals/scripts/noninferiority.py:1471-1477`), and `regraded` and `unreproduced` replace and compare `truth-` graders alone (`:1323-1324`, `:1382-1391`). So a side whose `shape-` grader targets `files` regrades onto the existing `_suites` commit, which holds only a `shape-x` `file_exists` grader. The probe built such a side with the module's own `graded_side(..., spoil=...)` and ran `regrade` onto `suites["own"]`. With the guard removed it raised `AttributeError: 'str' object has no attribute 'get'` through `:1499`, `:712` and `:363`. At the target it exited 0 and printed its `graded on` line. A framer or settle reading this bullet learns that the fixture cannot hold such a case, and that is wrong. The bullet's first ground holds, and the decision can stand on it alone. The bullet's coordinate `line 1497` also names `json.dump(out, ...)` at the target; the call is at `:1499`. The *Scope* section carries no date, unlike *Grounding*, so the bullet should name the call and not a line. No other record states the false ground: `gaps.md:9` and `frame/questions.md:9` cite the bullet without restating it, and *Grounding* row 13 is dated to `f096614f6`.

```markdown
- A `regrade` case. `regrade` reaches `reads_record` only through its last call, `side_numbers(out)`, which item 3 reaches through `compare`, so a `regrade` case would pin the guard that items 2 and 3 already pin. The fragment states that `regrade` read such a side only up to that line.
```

### 2. The closing memo's coordinate for `regrade`'s call names the wrong line at the target

```seal
severity: should
location: `seal/threads/1794096494-compare-reads-a-grader-with-a-string-target/gaps.md:9`
evidence: read `evals/scripts/noninferiority.py:1497-1499`, `seal/threads/1794096494-compare-reads-a-grader-with-a-string-target/gaps.md:9`
```

Why it matters: `gaps.md` states the present, and its `## Not verified` row 3 says `regrade` reaches `reads_record` "only through `side_numbers(out)` at `evals/scripts/noninferiority.py:1497`". At the target, `:1497` is `json.dump(out, f, indent=1, ensure_ascii=False)`, and `numbers = side_numbers(out)` stands at `:1499`. The fix added two lines to `reads_record` (`:362-363`), which moved the call. 1497 is the line the frame read at `f096614f6`. Phase 1's account says the range and the records were read whole against HEAD (`trail/phases/phase-1.md:27`). `gaps.md` is in that closed set, so the read missed this coordinate (contract rule 12). This round answers the row's question: probe 3 under `## Probes` shows `regrade` on such a side exits 0 at the target. So the fix pass may mark the row `closed` and cite this round. Whether it closes the row or keeps it open, the coordinate has to be corrected.

```markdown
| Whether `regrade` on a side holding a grader whose target is `files` now exits 0. No case runs `regrade` on such a side, as `frame/design.md` *Scope* puts out; phase 1 read that `regrade` reaches `reads_record` only through `side_numbers(out)` at `evals/scripts/noninferiority.py:1499`, the call the `compare` case covers | the proofer, at round 1, by reading `regrade` against the `compare` case |
```

### 3. `routing.md` says `regrade` now prints a verdict, and it prints a count line

```seal
severity: should
location: `seal/threads/1794096494-compare-reads-a-grader-with-a-string-target/routing.md:16`
evidence: read `evals/scripts/noninferiority.py:1499-1501`, `evals/scripts/noninferiority.py:1153-1154`
```

Why it matters: *Why this way* says the fix changes what `compare` and `regrade` print "from a traceback to a verdict a person reads". For `compare` that holds: it prints the record's `Verdict:` line (`:1153-1154`). `regrade` prints `graded on <rev>: <n> rows, <m> false` (`:1500`) and no verdict. The sealer reads this sentence against the tree, and it is wrong for one of the two commands it names.

```markdown
The owner answered automation to question 1. The fix changes what `noninferiority.py compare` and `regrade` print for a side holding a grader whose target is a string: `compare` prints its `Verdict:` line and `regrade` its `graded on` line, where each stopped on a traceback. So the work runs through the whole chain.
```

### 4. The fragment says `evals/` is not in what the plugin ships from, and a marketplace install carries it

```seal
severity: should
location: `seal/threads/1794096494-compare-reads-a-grader-with-a-string-target/changelog.md:3`, `seal/threads/1794096494-compare-reads-a-grader-with-a-string-target/pr.md:2`, `seal/threads/1794096494-compare-reads-a-grader-with-a-string-target/frame/plan.md:32`
evidence: executed `git grep -l 'noninferiority' -- . ':!evals' ':!tests' ':!seal' ':!docs' ':!.github/workflows'` (prints `.test_durations` alone) and `ls /Users/x/.claude/plugins/cache/agenticseal/agentic/0.34.0/evals/scripts/noninferiority.py` (present); read `.gitattributes:20-21`, `.claude-plugin/marketplace.json`, `docs/releasing/branch-and-release.md:15-16`, `docs/releasing/branch-and-release.md:30-34`
```

Why it matters: the fragment's sentence goes into the release notes and, through `pr.md`'s second quote, into the pull request body. It reads: "`evals/` is not in the archive the plugin ships from, so no verdict, output or instruction the installed plugin gives changes." The plugin ships two ways. `dist`, which the plugin directory reads, is `git archive` of the tag, and `.gitattributes:21` takes `evals/` out of it. But `.claude-plugin/marketplace.json` names `"source": "./"`, and `claude plugin update` installs from the marketplace clone of `main` (`docs/releasing/branch-and-release.md:15-16`, `:33`). That copy holds the whole tree: the installed 0.34.0 copy holds `evals/scripts/noninferiority.py`. So a reader learns that `evals/` is not installed, and a marketplace install has it. The conclusion still holds, on another ground: nothing the plugin ships runs `noninferiority.py`. The search over every shipped path found only `.test_durations`, which also leaves `dist`. `frame/plan.md:32` *Operational impact* draws the same conclusion from the same premise ("The changed files leave `dist` ..., so no installed plugin changes behaviour") and is repaired the same way. `frame/design.md:9` and `frame/plan.md:41` say no installed plugin *runs* the changed code, which the search confirms, so they stand. `pr.md:2` is the orchestrator's to rewrite from the new sentence (`skills/code-review/orchestration.md` *Where a fix pass or a fold changes a sentence that `pr.md` quotes*).

```markdown
`evals/` leaves `dist`, and no command, skill or agent the plugin ships runs `noninferiority.py`, so no verdict, output or instruction the installed plugin gives changes.
```

For `frame/plan.md:32`:

```markdown
No migration, environment variable or dependency. The changed files leave `dist` (`frame/design.md` *Grounding*, the ladder row), and no command, skill or agent the plugin ships runs them, so no installed plugin changes behaviour.
```

## Confirmations

What matched: *Scope* item 1. `evals/scripts/noninferiority.py:362-363` reads `config.target` and takes `path` only where `isinstance(target, dict)`, so the guard tests for a mapping and not for a string, as the item asks. The docstring adds one sentence saying so (`:359-360`). The signature and the True cases are unchanged. Read, and executed through probe 2.

What matched: the class is closed. Phase 1 claimed the one reader of a grader's target is `noninferiority.py:362`. This round's `git grep -n -E '\["target"\]|\.get\("target"|target:'` over `evals/scripts`, `lib`, `.github/scripts` and `skills/*/scripts` listed only replay, rule and record `target:` readers besides that line (executed). The producers the frame names (`evals/scripts/rule_cases.py:428-433`) and the five `target: 'files'` grader files (`grep -rln`, executed) match *Grounding* row 14.

What matched: *Scope* items 2 and 3, and both seen-red claims. With only the guard reverted to `(target or {}).get("path")`, the two new cases failed on `AttributeError` at `:363`, `2 failed, 4 passed`. At the target the module passed, 256 cases (probes 1 and 2, executed). That matches the red runs and the `seal mutate` run `trail/phases/phase-1.md:19` and `:23` claim. The compare case's grader text is the front matter of the committed `evals/behaviour/crafter/rule-crafter-slugify/graders/shape-no-probe-left.md` (read), and `grader_from` gives it `config.target == "files"` (`:1215-1236`, read).

What matched: each new test against its group. The new `Test_reads_record` parameter (`tests/evals/test_noninferiority.py:941`) is the group's only string target, and the existing `no target` id covers a missing one. The new `Test_compare` case (`:2060-2079`) is the group's only side whose grader is not the `shape-x` `file_exists` default. `bin/seal layout --pairs tests/evals/test_noninferiority.py` printed `1 files read, 0 pairs` (executed). `eval_side`'s default keeps the ten earlier calls on the `shape-x` grader (`:244-249`, read). The count of ten matches `trail/phases/phase-1.md:9`: `git show 8069495d:tests/evals/test_noninferiority.py | grep -c 'eval_side('` gives 11, the definition included (executed).

What matched: `gaps.md` *Not verified* row 3, the item handed to this round. `regrade` on a side holding a grader whose target is `files` exits 0 at the target and raised before the fix, after writing its output file (probe 3, executed; `:1495-1499`, read). The fragment's sentence "it now reads the side there as `compare` does" holds. Finding 2 names the coordinate of that row.

What matched: the version move. `e2803d29` changes `.claude-plugin/plugin.json` from `0.34.0` to `0.34.1` and adds `changelog.md`, in one commit (`git show --stat`, executed). `origin/release/v0.34.1` still stands at `8c2d60e14` (`git ls-remote`, executed). Milestone `release: 0.34.1` holds #1421 and #1426 alone (`gh issue list`, executed). That is what `frame/plan.md` *Operational impact* and its first *Judgments of the run* row say, against `docs/releasing/branch-and-release.md:30-38`. No other file outside `CHANGELOG.md` carries `0.34.x` (`git grep`, executed).

What matched: `pr.md`. Each of its five quotes stands word for word, runs of whitespace collapsed, in the record its coordinate names (executed, a Python comparison over the files). It holds the `Closes #1421.` line and the attribution line, and no sentence of the orchestrator's own, as `skills/code-review/orchestration.md:385-406` gives its shape (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at the target. This round ran one module, and the broad gate is not a proofer's (contract rule 2), so the suite stays `unverified` | `seal/config.md` *Broad gate* | the orchestrator, at the broad run |
| Whether `compare` reads the paid crafter pair of #1178 as `Verdict: pass` at the target. The side files are not in this environment | `frame/questions.md` Q1 | the repository owner |
| The ground of the first *Judgments of the run* row, that the owner deferred #1426 on 2026-11-07. Issue #1426 holds no comment that records it, so the tree does not show it | `seal/threads/1794096494-compare-reads-a-grader-with-a-string-target/frame/plan.md:40` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| 1. `bin/test tests/evals/test_noninferiority.py -q -p no:xdist` in the clone at `b30ca3846` | exit 0, `256 passed` |
| 2. `evals/scripts/noninferiority.py:363` reverted by `Edit` to `path = (target or {}).get("path") or ""`, then `bin/test tests/evals/test_noninferiority.py -q -p no:xdist -rf -k 'test_refuses_any_other_grader or whose_target_is_a_string'` | exit 1, `2 failed, 4 passed`: `Test_reads_record::test_refuses_any_other_grader[a target that is not a mapping]` and `Test_compare::test_accepts_sides_holding_a_grader_whose_target_is_a_string`, each on `AttributeError: 'str' object has no attribute 'get'` at `:363` |
| 3. `tests/evals/test_tmp_regrade_string_target.py`, written by `Write`, importing `graded_side`, `regraded_to`, `ROWS` and the `suites` fixtures from `tests/evals/test_noninferiority.py`. Its `spoil` sets case c1's `shape-x` config to `{"target": "files", "pattern": "test_tmp_", "match": "not_contains"}`, then it runs `regrade` onto `suites["own"]`. Run with `bin/test ... -q -p no:xdist`, first with the guard reverted as in probe 2, then with the guard restored by `Edit` | guard reverted: exit 1, `AttributeError` through `:1499` (`regrade`), `:712` (`side_numbers`), `:363`. Guard restored: exit 0, `1 passed`, with `regrade` returning 0 and printing its `graded on` line. The file was then deleted, and `git status --short` printed nothing |
| 4. `bin/seal layout --pairs tests/evals/test_noninferiority.py` | exit 0, `1 files read, 0 pairs` |
