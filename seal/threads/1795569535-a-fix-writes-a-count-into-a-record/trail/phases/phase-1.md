# Phase 1: 1795569535-a-fix-writes-a-count-into-a-record

## What this phase found

**The frame holds against the tree, except for one sentence of `frame/plan.md` *Technical context*.** It says `tests/text/test_the_rules_have_one_owner.py` defines no constant for the contract. At `b03b0e290` the file already defines `CONTRACT = ("skills", "agent-contract", "SKILL.md")`, which row 24 of `RULES` links from. The new row uses that constant, and the phase added none. The sentence is the framer's, so the hand-back names it for the orchestrator to fold.

**Rule 19's heading reads `## 19 A change rewrites the text it amends in place, and writes no count that goes stale`.** The heading `frame/design.md` *Data & interfaces* proposes is 99 columns, and `tests/behaviour/test_docs_line_wrap.py` holds the contract to its `LIMIT` of 88. The chosen heading is 88 columns and keeps the number, which the same section allows ("or words of the same meaning that keep the number"). The rule's body defines the count and the universal, so the heading names the count alone. The boundary run found the width twice, and `685fb4da5` and `4ebcc3c2b` shortened the heading.

**Rule 19's new paragraph holds clauses R1 to R6 of `frame/design.md` *Data & interfaces* in that order.** Its first three sentences are R1, the sentence opening "Such a sentence" is R2, "In its place" is R3, the two sentences on where a count stands and on an item's own number are R4, the two sentences on what stays are R5, and the last sentence is R6.

**The `RULES` row holds one fact beside its links, which `frame/design.md` *Scope* item 7 did not name.** The fact is `## 19 ` in the owner, because each link names the rule by its number. The comment over `RULES` defines a fact as "a spelling, a path or a number a reader of the owner acts on", and the decision was judged against that comment.

**Step 1 of `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* names the orchestrator's folds as "its folds of what a crafter names".** The words come from the orchestrator's row of the party table in `frame/design.md` *Data & interfaces*, since the framer writes every other fold.

**Seen red.** Before any text was edited, the new row ran against the tree of `cbaae0c59` with only the test file changed: `bin/test -q -p no:xdist tests/text/test_the_rules_have_one_owner.py -k 30` failed `test_every_link_names_the_owner[30 a change writes no count or universal a later change makes false]` on `skills/implement/fix-pass.md`, its first link. The owner's case passed there, because `## 19 ` already stood. Each link was then shown red alone by `seal mutate` at `e044852ab`, with the same command as `--tests`:

| Mutated file | Replace | Verdict | Failing line names |
|---|---|---|---|
| `skills/implement/fix-pass.md` | `contract rule 19` with `contract rule` | red | `skills/implement/fix-pass.md` |
| `skills/implement/fold-and-reframe.md` | `contract rule 19` with `contract rule` | red | `skills/implement/fold-and-reframe.md` |
| `skills/implement/orchestration.md` | `contract rule 19` with `contract rule` | red | `skills/implement/orchestration.md` |
| `skills/code-review/orchestration.md` | `contract rule 19` with `contract rule` | red | `skills/code-review/orchestration.md` |
| `skills/agent-contract/SKILL.md` | `## 19 A change rewrites` with `## A change rewrites` | red | `test_the_owner_states_the_rule`, the fact `## 19 ` |

Each run exited 0 with the verdict `red`, and `git status --short` printed nothing after the five runs. No unit of code changed, so the row is the phase's only unit that adds behaviour.

**The searches of `frame/plan.md`'s Verified by cell print nothing at `935f8bf56`**: `git grep -n -F 'A count of a list is stated once' -- agents skills docs templates` and `git grep -n -F 'no sentence counts the examples' -- agents skills docs templates`.

**Other statements of the reworded and removed rules, a sample.** `git grep -n -i -E 'amends in place|stated once|beside the list|counts the examples|count of a list|cites the list|only one of them' -- ':!seal/threads'` at `935f8bf56` printed rule 19 itself, `skills/core/SKILL.md:146`, which states the rule's first half and stays true, and lines about other facts in `tests/behaviour/test_the_rules_command_reads_each_rule_off_its_test.py:19`, `tests/github/test_plugin_directory_check.py:153` and `tests/skills/test_fold_check.py:9`. No file of the tree cited the framer's paragraph by its opening words. A statement of the rule in other words stands outside this search.

**The read of the range against HEAD found the rule broken in the range's own text.** The `RULES` comment and the fragment's second item said every step where a party writes after round 1 cites rule 19, which the proofer's and the sealer's steps contradict. The fragment's process row and the closing memo each stated a count without its moment. `935f8bf56` rewrote each, judged against rule 19 as this phase extends it.

**The phase-boundary set.** It is `tests/text` and `tests/behaviour`, which hold the tree-wide files `CONTRIBUTING.md` names and the five files of the plan row, and the test files that load, from this tree, a module reading `.claude-plugin/plugin.json`. Those modules were listed by `grep -rln -E 'plugin\.json|\.claude-plugin' lib skills hooks bin --include='*.py'`: `lib/core.py`, `skills/verify/scripts/broad_gate.py`, `skills/code-review/scripts/pr_body.py` and `skills/verify/scripts/seal_stamp.py`. The command, run at `935f8bf56`:

```
bin/test -q tests/text tests/behaviour tests/lib/test_core.py tests/hooks/test_core_start.py tests/skills/test_chain_check.py tests/skills/test_pr_body.py tests/skills/test_broad_gate.py tests/skills/test_seal_stamp.py tests/skills/test_payload_meter.py
```

It exited 0 with 1718 passed and 10 skipped. At `7833f983f` the same command failed three cases: the work item had no closing memo yet, and two lines passed the wrap limit. At `1f287fa26` it failed the heading's width alone.

**The version moved to 0.39.0 in `7833f983f`, the commit that adds `changelog.md`.** After it, `git grep -n -F '0.38.8' -- ':!seal/threads'` printed nothing.
