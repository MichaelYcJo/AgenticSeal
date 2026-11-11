# Design: the literal asserts of tests/text and tests/behaviour are weighed a second time (#1488)

## Grounding

The tree as read at `c9ed2c6ee`.

| Policy clause | What it fixes for this work |
|---|---|
| **G1** `docs/running/what-a-script-gates.md` *The checks*, the row for the cases under `tests/text/` and `tests/behaviour/` that read prose (read); `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest* (read); `agents/proofer.md:59-63` (read) | The policy in force is "a case pins a fact a reader acts on; one that pins wording goes", and the proofer reads prose for meaning. The row says nothing of an assert that a phrase is absent. The issue's *Change* adds that an absence assert for a removed design goes once the release that removed it has shipped. `## Rule changes` writes that into the row, with the exception *The criterion* keeps for a literal a rule of that text itself forbids, so the proofer and #1489 hold later asserts to it after this work item's directory is gone. |
| **G2** #1233's frame, `c3e020961:seal/threads/1793542348-each-wording-pin-is-kept-or-removed/frame/design.md` *The criterion*, *Scope* and *Out*, and its `frame/plan.md` *Alternatives considered* A1 to A5 (executed: `git show`) | #1233 ruled the asserts its lister printed: an `in` comparison, a literal of four words or more, standing in a file of `docs/`, `skills/` or `agents/`. It left out an absence assert, a shorter literal, a literal reached through a name, and a literal whose home is a template, a README or a script. It read each case whole (its A2), and a kept assert took a comment above it naming the fact and who reads it. Those comments stand at this commit, for example `tests/behaviour/test_waiver_decided_at_start.py:157-159` (read). This design carries the four kinds of fact of its *The criterion* forward and does not argue them again. |
| **G3** The issue (executed: `gh issue view 1488 --json title,body,comments`, no comment) and its counts re-taken (executed: *The counts* under `## Data & interfaces`) | The issue counted 388 presence and 158 absence asserts at `ba4d85629` and does not state its command. *The counts* reproduces the first number at that commit and reaches the second by none of its three commands, so it names the commands this work records with. Releases 0.37.1 to 0.37.3 moved the listing's totals between the two commits of that table (executed: *The listing* at both). |
| **G4** The three regions the issue names (read): `tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py:137-156`, `tests/text/test_a_segment_feeds_the_flow_log.py:165-235`, `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:125-188` | Each region reads a file of the tree as text: a template's section, a skill's section, the docstrings of `skills/verify/scripts/seal_stamp.py` and `skills/verify/scripts/broad_gate.py`. They hold all three things *The criterion* tells apart: a fact (`/agentic:config`, `Exit 0`, `seal cost --work-item`, `flow-baseline`), wording (`Nothing is stripped`, `quietly repaired`, `no-op`, `never`), and the absence of a removed design (the loop over `gone` at `:132-160` and the `not in` asserts at `:161-188`). *Worked examples* rules them. |
| **G5** `tests/behaviour/test_no_document_names_the_old_roots.py` (read whole); `docs/layout/one-root-by-lifetime.md:22-29` and `docs/layout/one-root-by-lifetime.ko.md:29` (read); `tests/lib/test_optin.py:552-570` (read); the files that name the module (executed: `git grep -n test_no_document_names_the_old_roots -- . ':!seal/threads'`) | The module holds two things. Above the comment `#1059` at `:302` it scans the shipped documents and `lib/` for the roots 0.4.0 removed, with an allowlist, a coverage check and their own cases. Below that comment it holds three cases of #1059 that keep the root's second name stated in the core and on one line of each README, and they call the module's `tracked`. The policy rule the check line closes says "no code of the plugin opens a top-level `specs/` or `.specseal/` on its own", which is behaviour, and `tests/lib/test_optin.py#test_refuses_the_legacy_directory` and `#test_accepts_the_old_scratch_file_as_an_ordinary_file` read it. No sentence of the rule says a document does not name the old roots. The scan is the absence of a design a shipped release removed, so it goes (*Scope* item 5), the three cases of #1059 stay, and the check line keeps `tests/lib/test_optin.py` alone (`## Rule changes`). Three places outside the module name a unit of it: `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:65` names `#tracked`, which stays; `tests/behaviour/test_both_editions_carry_the_same_folds.py:94` cites `#uncovered`, which goes; `.test_durations` holds its rows (G8). |
| **G6** `.github/scripts/rules.py`, its docstring (read); `skills/settle/rule-changes.md` *A rule has one shape* (read); `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | A check line names files, and `seal rules --check` refuses one naming a path that is no file of the repository. A pending `change` excuses nothing, so a module a `docs/` check line names stays a file until the settle writes the line. This work item's subject is the tests, so it states each change to a `docs/` check line in `## Rule changes` and edits no file under `docs/`. A check line outside the policy root is edited in place. A rule no case holds carries no check line, so a line that loses its last target is removed and not re-pointed at a reader. |
| **G7** The check lines that name a module of the two directories (executed: `git grep -n '^ *check: ' -- . ':!seal/threads' ':!tests' ':!*.py'`, then each target under `tests/text/` or `tests/behaviour/` counted) | 47 of the modules are named by at least one check line, 44 of them by a line under `docs/`. Which of those lines loses its last reader depends on each ruling, which is the build's (`frame/questions.md` Q3). The one line whose answer the frame can give is G5's. |
| **G8** `.test_durations` and its readers (executed: `git grep -ln test_durations`); `.github/scripts/durations_union.py:70` and `#verdict` (read); `docs/releasing/release-checklist.md:136-146` (read); #1486 (executed: `gh issue view 1486`) | A row of `.test_durations` for a removed case is a dead entry. The `durations` job fails only on the release pull request, only where dead entries hold more than `STALE_SHARE`, 5 percent, of the file's seconds, and the checklist's refresh answers that. #1486 removed the file in this release (`dbed1d5ff`), and this branch took that removal with the merge `ab3d6bc8c`; this work writes no row of it (`frame/plan.md` A11). |
| **G9** The unsettled designs' `## Rule changes` under `seal/threads/` (read, each) | Four designs state operations and the rest state none. `1794289597-pr-md-copies-the-changelog-below-the-fold` changes another row of `docs/running/what-a-script-gates.md` *The checks*, and its `from` shares no text with this design's. `1794289597` also changes `docs/layout/one-root-by-lifetime.md` and its Korean edition under another section. No pending operation touches the two texts this design changes. |
| **G10** `seal/follow-up.md` (read) | Both tables are empty. No item waits on this work. |
| **G11** The release's other open work items (executed: `git diff --name-only 18a7e18fb...<branch>` for each of the five branches; `gh issue view` for #1483, #1486, #1487 and #1489) | No sibling has committed a frame. #1498's branch changes `tests/censuses.py` and `.claude-plugin/plugin.json` and no file of the two directories. `frame/plan.md` *Overlap with the release* states where the others meet this work. |
| **G12** The latest release's `### Process changes` (executed: `gh release view --json body`, v0.37.3) | Its rows move agent rules between files. Two bear on this build: a fix pass opens `skills/implement/fix-pass.md`, and the agent definitions and the contract carry no check line, so no line of *Scope* item 8 stands in `agents/` or `skills/agent-contract/SKILL.md`. |
| **G13** `docs/layout/the-record-layout.md` *A change writes fragments, never a shared file* (read) | The work writes a `changelog.md`. Its diff changes none of the files that owe a `### Process changes` table, so the fragment carries none. |
| **G14** `skills/settle/scripts/rule_changes.py#parse` (executed: `parse(<this file's text>, "docs")` from a `git clone --no-local` of the worktree under the framer's scratch directory) | `parse` returns every operation of `## Rule changes` with no error and nothing unread, at the frame and again after the fold that followed phase 4, at `92337c2f9`, and after the fold that followed round 1, at `ea1328097`. Each `from`, whitespace collapsed, stands exactly once in its section at the commit it was read at (executed). |

## Scope

In:

1. The cases of group A (*The groups*) are ruled. Each case that holds a listed assert is read whole. Each assert of that case that reads a file of the tree as text (*What an assert reads*) is kept or removed by *The criterion*, whether its literal stands in the assert, in a name, in a tuple a loop walks or in an f-string. A kept assert carries, on the comment line or lines directly above it, the fact it pins and who reads that fact, and its literal is cut to that fact (*The criterion*, *A kept literal*). Where the literal sits in a tuple or table a loop asserts, the comment stands beside that entry. An assert that already carries such a comment stays as it stands (G2), except `tests/behaviour/test_first_setup_asks_once.py:415`, which *A kept literal* names and whose comment came with #1233 (`c3e020961`).
2. The cases of group B are ruled the same way.
3. The cases of group C are ruled the same way.
4. The cases of group D are ruled the same way, except `tests/behaviour/test_no_document_names_the_old_roots.py`, which item 5 holds.
5. In `tests/behaviour/test_no_document_names_the_old_roots.py`, every case and helper of the old-roots scan goes: the cases from `test_no_shipped_document_names_the_old_roots` to `test_a_real_loss_of_coverage_survives_a_neighbour_being_mid_edit`, and `OLD_ROOT`, `KEEP`, `offenders`, `offenders_under`, `COVERED`, `DECLINES_COVERAGE`, `DECLINES_KEEP`, `uncovered` and `keep_entries_not_in_use`. The three cases under the comment `#1059`, with `tracked`, `SCANNED`, `SUFFIXES` and what those three import, stay unchanged. The module docstring is rewritten to say what the module now holds. The file keeps its name and its place, because a `docs/` check line names it until the settle (G6).
6. After a ruling, a case left with no assert is removed. A helper, constant, fixture or import that nothing uses any more is removed with it. A module left with no `test_*` function is deleted, unless a check line under `docs/` names it. That module stays as a file, and the phase names it in its `trail/phases/phase-N.md`.
7. Each docstring or comment that states what a removed assert pinned, or that cites a removed case, helper or module, is rewritten in place to state what the code now holds (contract rule 19). `tests/behaviour/test_both_editions_carry_the_same_folds.py:94` is one (G5).
8. Each check line outside `docs/` that names a module a phase deleted, or a module that keeps no case reading the line's rule after the phase, is edited in place: the target leaves the line, and a line left with no target is removed (G6). The rule files outside the policy root are those `.github/scripts/rules.py#RULE_FILES` lists.
9. Each check line under `docs/`, other than the old-roots line and its Korean edition's, that names a module which keeps no case reading the line's rule after a phase's ruling is named in that phase's `trail/phases/phase-N.md` with the module. The phase edits no file under `docs/` and keeps no assert for the line's sake. The orchestrator sends the framer those lines as one decision to fold, and the framer adds one operation per line to `## Rule changes`, with the edition's operation where the document has one: a `change` that takes the module off a line that keeps another target, and a `remove` of a line whose one target is the module. Phases 1, 3 and 4 named one line each, in `docs/forms/the-round-record.md`, `docs/running/the-broad-gate.md` and `docs/layout/the-pact.md`, and `## Rule changes` holds them. A line phase 5 names is folded the same way before the first round.
10. The counts of *The counts* are taken at the base and at the last phase's commit. Phase 4 wrote both in its `trail/phases/phase-4.md` and in the work item's `changelog.md`. Phase 5 takes the second again at its own commit, writes it in `trail/phases/phase-5.md`, and rewrites the fragment's after-build counts in place.
11. The work item's `changelog.md`, written by phase 4 (G13) and brought to the tree phase 5 leaves.
12. The merge of #1486. Once #1486 has merged into `release/v0.37.4`, the orchestrator merges that branch into this one and resolves each conflict: inside a case #1486's diff changed, the case is taken as #1486 wrote it, and everywhere else this branch's text stands. Phase 5 then lists the modules both branches changed, with `git diff --name-only <merge base> <each parent> -- tests/text tests/behaviour` at that merge, reads whole each case of those modules that #1486's diff changed or added, and rules it by items 1 to 4, with items 6 to 9. A ruling phases 1 to 4 made in a case #1486's diff did not change stands and is not made again. At `60838ede9`, #1486's branch before its last phase, the two branches both change ten modules of the two directories (executed), so the list is taken at the merge and not from this sentence.

Out, each with its reason:

- **An assert that reads a program's behaviour or a text the case built** (*What an assert reads*). It pins no document. The issue says its count holds such asserts and did not weigh them.
- **A case that holds no listed assert.** A case can pin wording through a regular expression, a `count`, an equality or a helper, and those spellings are unbounded, so no method lists them whole (contract rule 12). The listing is the method here and its edge is stated in *The listing*. #1489 applies this criterion to each case it moves, and the proofer reads the rest at the next change that breaks one.
- **Three modules and one case that a sibling work item removes or rewrites**: `tests/behaviour/test_the_gate_names_every_step_ci_runs.py` (#1483), `tests/text/test_ci_gives_the_checks_what_they_need.py` and `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` (#1486), and `tests/behaviour/test_a_release_publishes_its_note.py#test_the_workflow_fires_on_the_tag_and_writes_one_release_one_asset_one_edit`, which holds the lines #1486 names. An assert there is that item's.
- **The test modules outside `tests/text/` and `tests/behaviour/`.** The issue scopes the work to the two directories.
- **`.test_durations`** (G8).
- **Every sentence under `docs/`.** The operations of `## Rule changes` reach the policy root at the settle.
- **Deleting or renaming a module a `docs/` check line names** (G6). Where item 6 leaves such a module with no case, the orchestrator files one issue for its deletion after the settle, and the pull request body names it. `tests/behaviour/test_no_document_names_the_old_roots.py` keeps three cases and is no such module. Its name is #1489's to change when it moves those cases.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 Every listed assert of the scope is accounted for | Given a phase's last commit, when the phase record is read, then for each module of its group it gives the number of listed asserts at the base that were kept, removed and not ruled because they read behaviour or a built text, and the three add up to the module's count in *The listing* at `18a7e18fb` | each phase boundary, executed by the crafter with *The listing* at both commits |
| S2 A kept assert pins a fact, and a removed one pinned wording or a removed design | Given the diff, when each kept assert and its comment, and each removed assert, are read against *The criterion*, then each kept one names a fact of one of the four kinds and its reader, with its literal cut to the fact, and each removed one held wording, or an absence that no rule of that text itself forbids there | the proofer at review |
| S3 An assert on behaviour is unchanged | Given the diff, when each changed or removed assert is read, then none read a program's output, return value or written file, unless its case was removed for holding no assert of its own after the ruling | the proofer at review |
| S4 Every check line resolves | Given a phase's last commit, when `seal rules --check` runs, then it exits 0 | each phase boundary, executed |
| S5 No line names a deleted module or a removed unit | Given a phase's last commit, when `git grep -n <name> -- . ':!seal/threads' ':!.test_durations'` runs for each deleted module and each removed case or helper another file cited, then it lists nothing | the phase that removes it, executed |
| S6 The old-roots module holds the three cases of #1059 | Given phase 4's commit, when `grep -n '^def ' tests/behaviour/test_no_document_names_the_old_roots.py` runs, then it lists `tracked`, `lines_naming_the_second_root` and the three cases of #1059 and nothing else, and `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` passes | phase 4, executed |
| S7 The counts are recorded before and after | Given the last phase's commit, when `changelog.md` and that phase's record are read, then each gives the three counts of *The counts* at `18a7e18fb` and at that commit | phases 4 and 5, executed; the sealer reads the fragment against a re-run |
| S8 The rule changes parse | Given this file, when `skills/settle/scripts/rule_changes.py#parse` reads it with root `docs`, then it returns each operation with no error and nothing unread | executed by the framer (G14); the pull request's chain check |
| S9 The narrow run passes | Given a phase's last commit, when the modules *The narrow run* gives for it run in one command, then each passes | each phase boundary, executed; the rest of the suite is `unverified`, answered by the orchestrator's broad gate |

## Data & interfaces

### The listing

The listing prints every `assert` under `tests/text/` and `tests/behaviour/` whose test holds an `in` or `not in` comparison with a string literal or an f-string on its left, one row per comparison as `path:line case left op right`, and a last line of totals. The crafter saves the script under its scratch directory (contract rule 17) and runs it as `python3 -I <script> <root of a tree>`. It reads and writes nothing else.

```python
import ast
import pathlib
import sys

root = pathlib.Path(sys.argv[1])
rows = []
for folder in ("tests/text", "tests/behaviour"):
    for path in sorted((root / folder).glob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        owner = {}
        for unit in ast.walk(tree):
            if isinstance(unit, (ast.FunctionDef, ast.AsyncFunctionDef)):
                for inner in ast.walk(unit):
                    if isinstance(inner, ast.Assert):
                        owner.setdefault(inner.lineno, unit.name)
        for node in ast.walk(tree):
            if not isinstance(node, ast.Assert):
                continue
            for compare in ast.walk(node.test):
                if not isinstance(compare, ast.Compare):
                    continue
                left = compare.left
                literal = isinstance(left, ast.JoinedStr) or (
                    isinstance(left, ast.Constant) and isinstance(left.value, str)
                )
                for op, right in zip(compare.ops, compare.comparators):
                    if literal and isinstance(op, (ast.In, ast.NotIn)):
                        rows.append(
                            (
                                path.relative_to(root).as_posix(),
                                node.lineno,
                                owner.get(node.lineno, "<module>"),
                                "in" if isinstance(op, ast.In) else "not in",
                                ast.unparse(left),
                                ast.unparse(right),
                            )
                        )
for rel, line, case, op, left, right in rows:
    print(f"{rel}:{line} {case} {left} {op} {right}")
print(
    f"comparisons {len(rows)}",
    f"asserts {len({(r[0], r[1]) for r in rows})}",
    f"absence asserts {len({(r[0], r[1]) for r in rows if r[3] == 'not in'})}",
    f"cases {len({(r[0], r[2]) for r in rows})}",
    f"modules {len({r[0] for r in rows})}",
)
```

Its edge: it lists no assert whose literal is reached through a name, such as the loop at `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:132-160`, and no assert that reads a text by another spelling. *Scope* item 1 reaches the first kind inside a case that holds a listed assert. The second kind is *Out*.

### The counts

Three counts are recorded at the base and at the last phase's commit (*Scope* item 10). The first two are the forms the issue names, taken with `git grep` from the worktree. The third is the last line of *The listing*.

| Count | Command | At `ba4d85629` | At `18a7e18fb` |
|---|---|---|---|
| presence form | `git grep -E 'assert +"[^"]{6,}" +in +[A-Za-z_]' <commit> -- tests/text tests/behaviour \| wc -l` | 388 | 388 |
| absence form | `git grep -E 'assert +"[^"]{6,}" +not in +[A-Za-z_]' <commit> -- tests/text tests/behaviour \| wc -l` | 132 | 134 |
| the listing | the last line of *The listing* | comparisons 736, asserts 693, absence asserts 151, cases 346, modules 72 | comparisons 735, asserts 696, absence asserts 151, cases 342, modules 72 |

All six cells are executed. The tree at `ba4d85629` was written under the framer's scratch directory with `git show`, because `.gitattributes` keeps `tests/` out of `git archive`.

### What an assert reads

The right side of a listed comparison is one of three things, and the case's code says which.

- **A file of the tree read as text.** A document, a template, a README, a workflow or a config file, or a script's source, docstring or help constant read from its file or from `__doc__`. It may be cut to a section, a paragraph, a row or a line, and it may have its whitespace folded. A line a workflow step or a script prints to a person is a file's text where the case takes it from the file and runs nothing, such as the `::error::` line that `tests/behaviour/test_the_release_check_watches_what_ships.py#refusal` takes from the `run:` text of `.github/workflows/hygiene.yml`. *The criterion* rules these asserts.
- **A program's behaviour.** What code the case ran printed, returned, raised or wrote: a subprocess's output, a function's result, a captured stream, a file a script produced. A value the case takes from a module it imported, such as a message constant of `skills/verify/scripts/broad_gate.py`, is the program's behaviour too. These asserts are not ruled and are not changed.
- **A text the case built.** A fixture, a string the case composed, a message the case's own helper returns. These asserts are not ruled and are not changed.

Where one name holds a file's text in one case and a program's output in another, each assert is read in its own case.

### The criterion

**A presence assert on a file's text is kept where its literal is a fact a reader acts on, of one of four kinds.**

- **A spelling a script, a parser or the harness matches**: a field name, a block or line keyword, a routing answer, a config key, a front-matter key, a table header a walker reads, a marker, a label a command resolves.
- **A citation a reader resolves**: a path, a `path#unit`, a heading cited in italics, a heading a citation elsewhere resolves, a contract rule number.
- **A command, flag or value a reader copies or runs**: a shell command, a `seal` subcommand, a `gh` call, an exit code, a number a person or a script waits on.
- **In a workflow or a config file, a key with the value its runner acts on**: a trigger, a permission, a `needs` or `if` line, an environment binding, a step's command.

**A presence assert is removed where its literal is wording**: a rule's lead sentence, its grounds, its example or a clause of it, and a word or phrase of ordinary prose whatever its length, such as `no-op`, `never`, `default` or `either place`. Three shapes count as wording whatever they hold: an assert that a check line names the asserting module, an assert that only locates the text a removed assert read, and an assert that a sentence stands in two files in the same words.

**A kept literal holds the fact and no word of the sentence around it.** The literal at `tests/behaviour/test_first_setup_asks_once.py:415`, which holds the words "then runs" before the command `seal pr-checks install`, becomes the command in its code span. It is the one assert carrying #1233's comment that is cut; every other one stays as it stands (*Scope* item 1). The sentence stays in the literal only where its words are what the reader matches or copies, such as a table row, a heading or a line a person pastes, and the comment says so. Where cutting a literal makes it equal to another assert of the same case on the same text, the second one goes. The assert keeps reading the narrowest text its case already cuts, a section or a paragraph, and is not widened to the whole file.

**An absence assert on a file's text is removed where its literal is text or a design that a shipped release removed**: a former sentence, a former name, constant, row, label, path or command. Every release up to v0.37.3 has shipped, so every such assert at the base goes, except one whose literal a rule of that text itself forbids there, which the two paragraphs below keep. The test: the literal stood in that text before a change and the assert was written to hold the change.

**An absence assert is kept where a rule in force forbids its literal in that text, and the literal is a command, a path, an expression or a spelling a reader or a runner would act on were it written there.** The rule is one of that text itself: it forbids the act the literal would hand that text's reader, or it names what that text must not hold. `agents/sealer.md` *Never*, which says the sealer draws no stamp, is such a rule for `seal stamp --from` in `agents/sealer.md`. A rule that binds every text alike is not: `skills/core/SKILL.md` *The rule a mechanism is kept against*, "a fact has one source", forbids every copy of every text, so it keeps no absence assert. The comment above a kept absence assert cites the rule as a backticked path and its heading or bold lead in italics. A kept absence assert reads the text the rule forbids the literal in. Where the case cut another text, the phase corrects the cut and names it in its phase record, as phase 4 did at `f25de2b52` for the first of the two rows below, whose right side it cut from the workflow's last `run:` block to the claims step's own. #1486 has since rewritten that case to read every step's `run:` block of the parsed workflow, and at HEAD it holds no listed assert (`trail/phases/phase-5.md`). An absence assert whose rule the crafter cannot cite is removed. Two rows of the listing that look like this kind, each for its phase to rule after reading the case: `tests/behaviour/test_a_body_naming_two_issues_claims_one.py:56`, a pull request's body kept out of a workflow's `run:` line, and `tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py:166`, `rm -rf` kept out of the contract and the definitions.

**Where an absence assert meets both paragraphs above, the second rules.** A literal that a shipped release removed from a text, and that a rule of that text itself forbids there, is kept with the comment the second paragraph asks for, because the rule outlives the release that removed the text. A literal that a shipped release removed and that only a rule binding every text alike forbids goes, as `def split_row` in `skills/code-review/scripts/chain_check.py` and the close-block values in the files a fix pass reads went: whether a copy has come back is the proofer's to read, and `tests/text/test_no_passage_is_pasted_into_a_second_file.py` reads pasted passages.

**Where an old phrase's absence and a new phrase's presence are asserted together, the absence goes and the presence is ruled as any presence assert**, unless the paragraph above keeps the absence.

### Worked examples

Each is a ruling the framer made on lines it read (G4). The phases follow them.

| Assert | Ruling | Why |
|---|---|---|
| `tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py:152-153`, `Nothing is stripped` and `quietly repaired` | removed | wording of the template's section |
| the same case, `:154`, `/agentic:config` | kept | the command a person types to rewrite the key |
| `tests/text/test_a_segment_feeds_the_flow_log.py:173-174`, `Exit 0`, `Exit 1`, `Exit 2` | kept as they stand | exit codes the orchestrator acts on, and the comment above already names them |
| the same case, `:179`, `the run's hand-over` | removed | wording |
| the same module, `:186` and `:192-193`, `no-op` and three phrases through a loop | removed, and the case with them | a word alone and clauses of one sentence |
| the same module, `:198`, `never` and `question` | removed, and the case with it | two words alone |
| the same module, `:212`, `seal cost --work-item` | kept | the command the orchestrator runs |
| the same module, `:216`, the `# <file name>` line | kept, cut to the code span | the line's spelling is what `seal cost --work-item` reads on the log |
| the same module, `:225`, `flow-baseline` | kept | the label the command resolves |
| `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:132-165` and `:177-188`, each `not in`, the loop over `gone` among them | removed | names and phrases of the stamp and the panel that shipped releases removed, read in two scripts' docstrings |
| the scan of `tests/behaviour/test_no_document_names_the_old_roots.py` | removed (*Scope* item 5) | the roots 0.4.0 removed (G5) |

### The groups

Each row is a phase. The counts are *The listing*'s at `18a7e18fb`, less the three modules and the one case under *Out*, which hold 30 listed asserts in 10 cases.

| Group | Modules | Listed asserts | Absence asserts among them | Cases holding one |
|---|---|---|---|---|
| A | the 30 listed modules of `tests/text/` | 189 | 37 | 109 |
| B | `tests/behaviour/`: `test_first_setup_asks_once.py`, `test_the_broad_gate_row_is_asked_for_and_runs_as_written.py`, `test_waiver_decided_at_start.py`, `test_the_pull_request_language_is_the_repositorys.py`, `test_the_set_a_work_item_always_has.py`, `test_the_sealer_guarantees.py` | 183 | 37 | 84 |
| C | `tests/behaviour/`: `test_the_seal_is_taken_once_by_the_sealer.py`, `test_the_stamp_reaches_the_person_it_is_drawn_for.py`, `test_the_suite_has_a_command_that_is_cheap_twice.py`, `test_chain_hooks_hardening.py`, `test_release_hygiene.py`, `test_a_foreign_seal_dir_keeps_the_records_shared.py` | 181 | 53 | 72 |
| D | the other 27 listed modules of `tests/behaviour/` | 113 | 19 | 67 |

A group's modules are the rows *The listing* prints under its directory at `18a7e18fb`, less the modules named in another row and under *Out* (executed).

### The narrow run

Each phase runs, in one command at its boundary, the modules it edited and the modules that read a path it changed, taken by `git grep -l` on each changed path's name at the phase's own base. The kinds are: its edited modules; `tests/github/test_rules.py` where a check line changed; the modules that read an edited skill or template file, by its path; and, where it deleted a module or removed a helper, `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`, `tests/behaviour/test_every_tracked_file_meets_every_census.py` and each module that names the removed unit. A module that reads a changed path by another spelling is outside the list, so the list is a sample (contract rule 12) and the orchestrator's broad gate answers the rest.

## Rule changes

- change
  file: docs/running/what-a-script-gates.md
  section: The checks
  from: a case pins a fact a reader acts on; one that pins wording goes
  to: a case pins a fact a reader acts on, and the absence of a command, a path or a spelling is such a fact where a rule of that text itself forbids it there, whether or not a shipped release removed it; one that pins wording goes, and so does one that pins the absence of text or a design that a shipped release removed and that no rule of that text forbids. A rule that binds every text alike, such as one source for a fact, keeps no absence. A line a step or a script prints, read from its file by a case that runs nothing, is weighed as any other text
- change
  file: docs/layout/one-root-by-lifetime.md
  section: The root and its lifetimes
  from: check: tests/behaviour/test_no_document_names_the_old_roots.py tests/lib/test_optin.py
  to: check: tests/lib/test_optin.py
- change
  file: docs/layout/one-root-by-lifetime.ko.md
  section: 루트와 그 안의 수명
  from: check: tests/behaviour/test_no_document_names_the_old_roots.py tests/lib/test_optin.py
  to: check: tests/lib/test_optin.py
- change
  file: docs/forms/the-round-record.md
  section: The round record
  from: check: tests/text/test_the_rules_have_one_owner.py tests/text/test_a_moved_rule_leaves_its_definition.py
  to: check: tests/text/test_the_rules_have_one_owner.py
- change
  file: docs/running/the-broad-gate.md
  section: One act, one owner, and the owner is the orchestrator
  from: check: tests/skills/test_broad_gate.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py
  to: check: tests/skills/test_broad_gate.py
- remove
  file: docs/layout/the-pact.md
  section: When there is a pact at all
  from: check: tests/behaviour/test_a_signer_declares_its_pact.py

## Removes

The first operation of `## Rule changes` adds one clause to a rule. What goes in return is the first two rows below, and the catch record of what goes is the issue's: none of the 17 recent red CI runs was such an assert catching a defect (read in the issue, not re-run).

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| each assert on a file's text ruled wording, and each absence assert of what a shipped release removed that no rule of that text itself forbids there | the cases of *The groups* that hold a row of *The listing* at `18a7e18fb` | nowhere: wording is the proofer's to read for meaning (`docs/running/what-a-script-gates.md` *The checks*), and a fact one of them carried stays as a kept assert of the same case |
| each case left with no assert, each helper, constant, fixture and import nothing uses after it, and each module left with no case that no `docs/` check line names | the same cases and their modules | nowhere; each phase names them in its `trail/phases/phase-N.md` |
| the old-roots scan, its cases, helpers and constants | `tests/behaviour/test_no_document_names_the_old_roots.py`, the units *Scope* item 5 names | nowhere: `tests/lib/test_optin.py` reads the rule's behaviour, that no code opens the old roots (G5) |
| a check line's target, at the settle | `docs/layout/one-root-by-lifetime.md` *The root and its lifetimes*, line 29, and line 29 of the Korean edition | `tests/lib/test_optin.py`, the line's other target (`## Rule changes`) |
| a citation of a removed helper | `tests/behaviour/test_both_editions_carry_the_same_folds.py:94` | rewritten to state what its own case does (*Scope* item 7) |
| check-line targets outside `docs/`, and docstrings and comments, that a phase's ruling makes false | the lines *Scope* items 7 and 8 reach | each phase names them in its `trail/phases/phase-N.md` |
| a check line's target, at the settle | `docs/forms/the-round-record.md` *The round record*, line 107, the line after **Each finding's close block has one writer, and the blocks written at one step reach the branch in a single commit.** | `tests/text/test_the_rules_have_one_owner.py`, the line's other target, whose `RULES` row 19 reads the rule (`trail/phases/phase-1.md`) |
| a check line's target, at the settle | `docs/running/the-broad-gate.md` *One act, one owner, and the owner is the orchestrator*, line 33 | `tests/skills/test_broad_gate.py`, the line's other target, which reads the run's first line and that it draws nothing (`trail/phases/phase-3.md`) |
| a check line, at the settle | `docs/layout/the-pact.md` *When there is a pact at all*, line 39 | nowhere: no case of `tests/behaviour/test_a_signer_declares_its_pact.py` reads the rule, at the base or after phase 4 (`trail/phases/phase-4.md`), and a rule no case holds carries no check line (G6) |
| check-line targets under `docs/` that phase 5's ruling leaves with no reader | the lines *Scope* item 9 reaches | the operations the framer folds into `## Rule changes` |

Framed 2026-11-11 by framer, before the build.
