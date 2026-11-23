# Guarantee: 1795398442-per-spawn-files-carry-text-their-reader-never-acts-on

The first run audited `bfbf1b487`, and this run audits `2b714e392`, both
against `release/v0.38.6`. That name resolves to `f2a664eb8` through
`release/v0.38.6@{upstream}`. `trail/gate.md` names the run
`e2551661f against f2a664eb8`. The two commits after it touch only the
work item's records: `bfbf1b487` writes `trail/gate.md`, and `2b714e392`
rewrites finding 2's close in `trail/rounds/round-2.md` (executed:
`git log --no-merges --name-only e2551661f..HEAD ^f2a664eb8`, and
`git diff bfbf1b487 HEAD`, which changes only `round-2.md:136`). At each
run, `seal pr-body seal/threads/1795398442-per-spawn-files-carry-text-their-reader-never-acts-on --body <scratchpad>/1795398442-per-spawn-files-carry-text-their-reader-never-acts-on/body.md --check`
exited 0 (executed). `seal/parity.json` is not tracked, so step 5 owes no
parity comparison.

This run re-reads only what `2b714e392` touched, which is the close of
round 2's finding 2. No claim in the table below has its coordinate in that
line, so the claims stand as the first run re-ran them at `bfbf1b487`.

Every `seen red` below was re-run in a clone at HEAD under
`<scratchpad>/1795398442-per-spawn-files-carry-text-their-reader-never-acts-on/sealer/at-base/`.
Each run restored the code from `f2a664eb8` or removed the one guard the
record names, with `bin/test -q -p no:xdist`. Each mutation was put back
with `git checkout HEAD`, and `git status --short` printed nothing after
each run.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The new case `test_accepts_a_row_a_section_citation_names_as_part_of_its_token` is red against the old pattern, failing with "assert not True" on the two links | `trail/rounds/round-1.md` finding 1, its close block | `git checkout f2a664eb8 -- skills/settle/scripts/passages.py`, then `bin/test ... tests/skills/test_passages.py -k test_accepts_a_row` | holds: exit 0 at HEAD; exit 1 with the base pattern, failing at `assert not shared(one, two)` with `AssertionError: assert not True` |
| The same case is red when the prefix is allowed to fold an italic phrase with no `of <path>` after it | the same close block | `SECTION` mutated so the path is optional, then the same case | holds: exit 1, failing at the second assertion, the bare italic phrase |
| The tree-wide paste case is red with the prefix removed, and it passes at HEAD | the same close block; `gaps.md:9` | `bin/test ... tests/text/test_no_passage_is_pasted_into_a_second_file.py` at HEAD, then with the base `passages.py` | holds: 5 passed at HEAD; with the base pattern, `test_no_pair_of_rule_documents_shares_a_run` fails, naming the 15-word run between `gate-to-pull-request.md` and `orchestration.md` |
| The language case is red against the old text: "contract rule 11 no longer names both language sections by heading; it names []" | `trail/phases/phase-1.md:64-66` | `git checkout f2a664eb8 -- agents skills/agent-contract/SKILL.md`, then `bin/test ... tests/text/test_a_language_section_of_writing_style_opens_alone.py -k opens_alone` | holds: exit 1 with that message |
| The `uncited` clause is red when a step's "rule 11" becomes "rule 12", naming its own file | `trail/phases/phase-1.md:75-77` | `agents/proofer.md` mutated, then the same case | holds: exit 1, `... no longer cites rule 11, which names the sections: ['agents/proofer.md']` |
| The heading check is red with the reader list cut to `rels` | `trail/phases/phase-1.md:82-84` | `for rel in [*rels, CONTRACT]:` mutated to `for rel in rels:`, then the same case | holds: exit 1, `the heading check no longer reads skills/agent-contract/SKILL.md` |
| Four numbering cases are red against the old text with "8 has no heading and the document does not list it" | `trail/phases/phase-1.md:61-64` | `git checkout f2a664eb8 -- agents skills/agent-contract/SKILL.md docs/running/the-agent-set.md`, then `bin/test ... tests/text/test_the_agent_contract_holds_the_universal_rules.py` | holds: 4 failed, 13 passed, each failure the "8 has no he..." list |
| The core-sentence case is red with T4's `skills/core/SKILL.md` replaced, because it reads only the opening | `trail/phases/phase-3.md:140-142` | the path in `skills/code-review/orchestration.md`'s opening mutated, then `bin/test ... tests/behaviour/test_chain_hooks_hardening.py -k opens_the_core_once` | holds: exit 0 at HEAD; exit 1 at `assert "`skills/core/SKILL.md`" in text` |
| The release table's preload rows against v0.38.5: crafter 30,613, framer 37,028, proofer 31,379, sealer 31,909, tracer 24,191, each lower | `changelog.md:3`; `trail/phases/phase-3.md:184-190` | `python3 .github/scripts/release_report.py --against v0.38.5 --at <clone at 641b6bfb5>`, from the clone at HEAD | holds at HEAD: the same five figures, each negative, exit 0 |
| Bytes: the contract 11,625 (12,029 at v0.38.5); `skills/implement/SKILL.md` 26,353 to 22,114; `skills/code-review/orchestration.md` 38,635 to 23,920; the new file 15,665 | `changelog.md:3-6`; `trail/phases/phase-3.md:192-197` | `git show <rev>:<path> \| wc -c` at `641b6bfb5`, `6edff124a` and HEAD | holds: every figure matches at HEAD |
| No measured file changed after the measurement at `236d3c5e6`, so *Scope* item 12 owes no new one | `trail/rounds/round-2.md:22-27` | `git diff --stat 236d3c5e6 HEAD -- agents skills/core skills/agent-contract skills/implement/SKILL.md skills/code-review/SKILL.md skills/code-review/orchestration.md skills/code-review/gate-to-pull-request.md` | holds: prints nothing |
| 36 work items' designs stood at `2669e43d4` | `changelog.md:9` | `git ls-tree -r --name-only 2669e43d4 -- seal/threads`, counting `/frame/design.md` | holds: 36, and 36 at HEAD |
| `chain_check.py`'s copy notice says the same before and after the normaliser change | `changelog.md:9` | `python3 skills/code-review/scripts/chain_check.py --baseline f2a664eb8 --root <clone> --worktree` with HEAD's `passages.py`, then with the base's, and `diff` of the two outputs | holds for this run: both exit 0, outputs identical, no copy notice. The 36-design probe of `trail/rounds/round-2.md:278` was read, not re-run |
| The moved paragraphs kept their words, except the split first paragraph and row 6 of the exit table | `changelog.md:4`; `trail/rounds/round-2.md:200-207` | probe `test_tmp_moved_paragraphs.py`, which locates each paragraph of the old section at `3c89a70d5` in the two files at HEAD with whitespace folded, and `git diff --no-index --word-diff` over the split | holds: 17 of 19 paragraphs stand whole, 6 in the kept file and 11 in the new one. The first paragraph gains only the pointer sentence, and row 6 changes only its citation |
| Every row of `frame/design.md` *Removes* and every removal the changelog names is gone from the tree | `frame/design.md:144-172`; `changelog.md` *Removed* | `git grep -n -F '<pattern>' HEAD -- <pathspec>` for the 21 G21 patterns, plus `orphan them earlier` in `skills` and `copy a file out of one` in `agents` | holds: all 23 print nothing. The landing places stand: `skills/code-review/orchestration.md:250` (the rebase), `skills/verify/orchestration.md:113`, `skills/implement/orchestration.md:194` and `:484`, the comment at `tests/text/test_the_rules_have_one_owner.py:155`, and `lib/config.py:280` |
| Every section citation and `check:` line that named a moved passage resolves | the issue's third *Done when* bullet; `frame/design.md` S6 | `bin/test ... tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_docs_line_wrap.py tests/text/test_the_agent_contract_holds_the_universal_rules.py tests/text/test_the_rules_have_one_owner.py` | holds: 166 passed |
| Round 2's three paste-ready fixes stand at HEAD, committed at `c5215301b` | `trail/rounds/round-2.md` findings 1 to 3, their close blocks | each fenced `markdown` block of `round-2.md` searched verbatim in `frame/plan.md`, `pr.md` and `changelog.md` | holds: the two plan rows, the `pr.md` line and the changelog sentence each stand verbatim; *Judgments of the run* holds two rows |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | Thirteen *Scope* items move or delete the passages the issue lists, cut the pull request section in two, name the language sections once in contract rule 11, and fold the normaliser fix into item 4 | the issue's *Direction* and its three *Done when* bullets; the diff, file by file; the changelog | none. The issue lists `agents/proofer.md:99-102` among the reference-root copies. G15 judges it the proofer's own review rule, and the issue's test, a passage its reader does not act on, does not reach it, because `agents/proofer.md:97-100` is a rule the proofer acts on (read) |
| the build | Three phases, each with a record and a Status commit (`d061ca6a3`, `dd9cf00d7`, `179fd6cbb`), and each seen red claim re-run above | the design; the diff; the release table at HEAD | none |
| the last round | Round 2 reads the fix diff and the merge of `f2a664eb8`, opens three records-only findings, confirms round 1's findings 2 and 3, and asks, under finding 2, that the orchestrator retitle #1579 when it titles the pull request `fix:` (`round-2.md:123-124`) | the tree at HEAD, on every claim re-run above | none |
| the fix pass's closes of round 2, the orchestrator's, read by no round | Each of the three findings is `fixed c5215301b`. At `2b714e392`, finding 2's close records that the orchestrator retitled #1579 from `refactor:` to `fix:` on 2026-11-23, as `skills/commit-pr-convention/SKILL.md` *Commit messages* states (`round-2.md:136`) | the paste-ready fixes of findings 1 to 3, which stand verbatim; the last round's request at `round-2.md:123-124`; `skills/commit-pr-convention/SKILL.md:169-172`; the tracker, where #1579 now reads "fix: files the crafter, the proofer and every agent open on each spawn carry text that reader never acts on" (executed: `gh issue view 1579 --json title`) | none. At `bfbf1b487` this close said "the issue's title stays", and the first run withheld its verdict on that |
| the changelog | Every preload falls, the new file holds the post-round steps, ten passages leave `skills/implement/SKILL.md`, rule 11 names the sections, the numbering policy moves, the normaliser folds a row's name, and the process-row list names seven files | the release table and the byte counts at HEAD; the diff; the design's *Removes* | none |
| the orchestrator's part of the pull request body | `pr.md` quotes the title row (`fix:`) and Q1 with its default, each with its coordinate, then `Closes #1579.` | `frame/plan.md:60`; `frame/questions.md`, row Q1. The `fix:` prefix is borne out by the diff: `skills/settle/scripts/passages.py#SECTION` changes what the paste check and `chain_check.py` decide, against the method the paste check's docstring stated at `f2a664eb8`, that a link shares its heading's words by design | none in its own text |
| the orchestrator's routing grounds | Under `agentic`: a work item, a framer, a crafter, the review chain, automation, and a pull request, for a change that moves text across about fifteen files | the diff. The normaliser change came out of round 1 and went through a crafter's fix pass and round 2, so each row's stated reason still covers it | none |

The broad gate's record names `e2551661f`, and `gate.log` reads
"suite ✓ 5644 passed · 9 skipped" and "chain ✓ exit 0" (read). Nothing
broad was run in this audit.

Q1 of `frame/questions.md` stays open for whoever prepares the release: the
release pull request's table after the release's other items merge. The
table at HEAD confirms this work's reading (executed, above).

The first run withheld its verdict on finding 2's close alone. The
orchestrator rewrote that close at `2b714e392` and retitled #1579. That
commit touches the work item's records alone, so `trail/gate.md` at
`e2551661f` still serves. Run over the worktree before this block was
written, `chain_check.py --baseline f2a664eb8 --worktree` named only
`guarantee.md`, as behind HEAD and withheld, and refused nothing else
(executed).

```seal
target: bfbf1b487e6e26454ae2b26f3153cc96e6e04941 against f2a664eb85677c4a4656c76d2e01b7091b1609fe
Verdict: withheld reason: the orchestrator's close of round-2 finding 2 (trail/rounds/round-2.md:136) says the issue's title stays, and skills/commit-pr-convention/SKILL.md:169-172 (Commit messages, the paragraph opening "An issue's title takes the prefix the pull request that closes it will take") has the orchestrator retitle #1579, filed refactor:, when it titles the pull request fix:, as the finding asked at round-2.md:123-124
```

```seal
target: 2b714e39297ca97531628b336d61c572f5ec2be5 against f2a664eb85677c4a4656c76d2e01b7091b1609fe
Verdict: sealed
```
