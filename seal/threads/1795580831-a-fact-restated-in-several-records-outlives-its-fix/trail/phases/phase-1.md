# Phase 1: 1795580831-a-fact-restated-in-several-records-outlives-its-fix

## What this phase found

**The frame holds against the tree.** Each coordinate of `frame/plan.md` *Technical context* stood at `aa32e8473`: `#read_own` at line 444, `#first_part` at 475 and `#compared` at 1129 of `skills/code-review/scripts/pr_body.py`, `tests/skills/test_pr_body.py#OWN` at line 261, and the four prose ranges it names. G9's figures held when this phase's own code ran over the tree: `test_tmp_quotes_in_tree.py` under this phase's scratch directory, calling `quote_lines` and `_unstood` over each `seal/threads/*/pr.md` at `288cb58d9`, printed 292 quotes, 3 refused and no line unread. The 3 are G8's line and the two quotes G9 names.

**One departure: the hook clause of *Scope* item 3 waits for phase 2.** *Scope* item 3 has the rewrite paragraph say that a stale quote of `pr.md` is rewritten where `seal pr-body` refuses it, "or earlier where a hand-back or the hook of *Scope* item 9 names it". No such hook stands at this phase's commits, so `skills/code-review/orchestration.md`, the paragraph opening **Where a fix pass or a fold changes a sentence that `pr.<lang>.md` renders**, says "or earlier where a hand-back names it". Phase 2 adds the hook to that sentence once its script stands. Judged against `agents/crafter.md` *Before you hand back, your range and the work item's records are read whole against HEAD*, which has a crafter fix each statement HEAD contradicts, and against `skills/core/SKILL.md` *The rule a mechanism is kept against*.

**The refusals hold one cause beside the two of `frame/design.md` *Data & interfaces*.** A quote whose file will not read as UTF-8 text is refused at its line, naming the path and the error. *Data & interfaces* asks for the shape `#read_own`'s refusals take, and `#read_own` refuses a `pr.md` that is not UTF-8 the same way. An absolute path is refused as naming no file of the work item's directory, since *Data & interfaces* reads the path as relative to that directory.

**The quote check raises once `pr.md` is read, before the translation files are looked for.** A run whose `pr.md` holds a stale quote and whose keys differ with no `pr.<lang>.md` names the quote alone. `#first_part` already raised stage by stage, the keys first and `pr.md` next, and this phase kept that order.

**The note on unread lines stands after `seal_mark`'s sentence and before the fold's.** `#_noted` builds it from the `pr.md` text among `#first_part`'s files, so `#compared` and `main` read `pr.md` once.

**`OWN` was brought into the form, as *Scope* item 2 leaves to the crafter.** It now opens with `- `, and its quote stands in `CHANGELOG`. Left as a near miss, it put the unread note into `seal pr-body`'s output, and eleven cases of the module that assert that output failed on it before `OWN` changed. The two added characters moved `LENGTH` from 71260 to 71262. The comment over it moved from 71,379 to 71,381 by the same two characters, a figure derived and not measured. `evals/scripts/rule_cases.py#OWN_PART` and every `pr.md` an eval scaffold writes hold no `" (` before a backtick (`git grep -n -F '" (\`' -- evals tests ':!tests/skills/test_pr_body.py' ':!tests/skills/test_chain_check.py'`, executed, printed nothing), so neither changed.

**Two conditions of the first draft went, because another condition held each of them.** A path of `..` was refused by `rel == ".."` and by `os.path.isfile` alike, which reading showed. A missing closing backtick was refused by `tick` and by `rest.endswith(")")` alike, since `partition` leaves `rest` empty where no backtick follows, which mutant 4 below showed. `77ff71f15` removed the first and `19807dac3` the second.

**The `RULES` row holds no fact beside its link.** The comment over `RULES` defines a fact as "a spelling, a path or a number a reader of the owner acts on", and the owner's new sentences give the command as an example, not as a spelling a reader must type. The link is the fix pass's citation of the paragraph by its bold lead.

**Seen red, before the code.** The cases of A1, A3 and A4 ran against `aa32e8473`'s `pr_body.py` with only the test file changed: `bin/test -q -p no:xdist tests/skills/test_pr_body.py -k quote` failed 7 cases. A1 and A3 exited 0 where 1 was asserted, or printed the body's line where `pr.md`'s was asserted. A4 printed no note. A2 passed there, as an accepting case does, and takes its red from mutants 10 and 11 below. A5 ran with `pr_body.py` set back to `aa32e8473` and failed with the body's first line named in place of `pr.md:1`. Its first draft failed there on an `AttributeError` for `NOT_HELD`, a line that names something else, so the case spells the cause literally (contract rule 15).

**Mutation.** `seal mutate skills/code-review/scripts/pr_body.py`, one batch at `77ff71f15`, with `--tests "bin/test -q -p no:xdist tests/skills/test_pr_body.py tests/skills/test_chain_check.py -k quote"`:

| # | Replace | Verdict |
|---|---|---|
| 1 | `line.startswith(QUOTE_OPEN)` with `True` | red |
| 2 | `and at >= len(QUOTE_OPEN)` with `and True` | red |
| 3 | `and path` with `and True` | red |
| 4 | `and tick` with `and True` | survived; the condition went in `19807dac3` |
| 5 | `and rest.endswith(")")` with `and True` | red |
| 6 | `unread.append(i + 1)` with `pass` | red |
| 7 | `if posixpath.isabs(rel) or` with `if` | red |
| 8 | `or rel.startswith("../") or` with `or` | red |
| 9 | `or not os.path.isfile(source):` with `or False:` | red |
| 10 | the source's `_collapsed(handle.read())` with `handle.read()` | red |
| 11 | `elif _collapsed(quote) not in text:` with `elif quote not in text:` | red |
| 12 | `if exc is not None:` with `if False:` | red |
| 13 | `#first_part`'s `causes = _unstood(...)` with `causes = []` | red |
| 14 | `#_noted`'s `if lines:` with `if False:` | red |
| 15 | `hold="holds" if len(lines) == 1 else "hold"` with `hold="hold"` | red |
| 16 | `#compared`'s `_noted(note, headings, parts), []` with `_noted(note, headings), []` | red |

At `19807dac3`, mutant 5 ran again alone with `-k looks_like_a_quote` and stayed red. The `RULES` row of key `31` was seen red by `seal mutate skills/implement/fix-pass.md`, which replaced the citation of `skills/code-review/SKILL.md` *A paste-ready fix reaches every statement of the fact it repairs, or names where it stops* with "the review skill", under `bin/test -q -p no:xdist tests/text/test_the_rules_have_one_owner.py -k 31`. It failed `test_every_link_names_the_owner` on `skills/implement/fix-pass.md`.

**The searches of `frame/plan.md`'s Verified by cell print nothing at `288cb58d9`** (executed): `git grep -n -F 'that you do not find, word for word' -- agents skills docs templates`, `git grep -n -F 'in a list item or in a' -- agents skills docs templates` and `git grep -n -F 'rewrites each quote' -- agents skills docs templates` each exited 1.

**Other statements of the reworded and removed rules, a sample.** `git grep -n -E "word for word|quote of .pr\.md|quotes of .pr\.md|in a list item or in a|table cell|rewrites each quote|that .pr\.md. quotes|quote stands|a quote of a record" -- ':!seal/threads'` and `git grep -n -i quote` over `agents`, the review and implement skills, `docs/running`, `templates` and `CONTRIBUTING.md` printed, beside the passages this phase rewrote: `docs/layout/the-record-layout.md:155`, which has each quote of `pr.md` stand word for word at its coordinate and stays true; `docs/forms/the-guarantee.md:22`, `agents/sealer.md:82` and `skills/implement/routing-question.md:156`, which say what `pr.md` holds and stay true; and lines on other facts. A statement of these rules in other words stands outside the search. The read of the range against HEAD found two more in code this phase wrote to: `#compared`'s docstring and `skills/code-review/scripts/chain_check.py#body`'s named the note's parts without the new sentence, and `e57450e43` rewrote both.

**A cell of the policy in force no longer lists every refusal.** `docs/running/what-a-script-gates.md` *The checks*, the `seal pr-body` row, says the command "refuses where a language key is absent, and where the keys differ and the work item holds no `pr.<lang>.md` or more than one". `frame/design.md` `## Rule changes` items 3 and 4 change that row's reading and its judgment cells, and none changes the refusal cell. The cell already left out the refusal at a line equal to `HEADING` and at a `pr.md` that is not there. The frame is the framer's, so the hand-back names it for the orchestrator to fold.

**The phase-boundary set.** It is `tests/text` and `tests/behaviour`, which hold the tree-wide files `CONTRIBUTING.md` *The test layout* names, the three other files of the plan row, and the test files outside those directories that `git grep -l` lists as naming `pr_body`, `agents/proofer.md`, the review skill, an `orchestration.md` or `fix-pass.md`. The command, run over the tree this record's commit holds:

```
bin/test -q tests/text tests/behaviour tests/skills/test_pr_body.py tests/skills/test_chain_check.py tests/evals/test_rule_cases.py tests/evals/test_noninferiority.py tests/github/test_release_report.py tests/lib/test_closing.py tests/lib/test_core.py tests/skills/test_rules.py tests/skills/test_seal.py tests/skills/test_session_cost.py tests/skills/test_settle.py
```

It exited 0 with 2426 passed and 9 skipped, at `03ad79545` with this record, `gaps.md` and the Status cell in the working tree. Its first run, at `e57450e43` with the same records, failed `tests/text/test_a_cited_commit_outlives_the_squash.py`: four docstrings of the new cases cited `aa32e8473`, a commit of this branch the squash discards. `pr_body.py` is the same at `v0.38.8` and at `aa32e8473` (`git diff --stat v0.38.8 aa32e8473 -- skills/code-review/scripts/pr_body.py` printed nothing), so `03ad79545` has the cases name 0.38.8.
