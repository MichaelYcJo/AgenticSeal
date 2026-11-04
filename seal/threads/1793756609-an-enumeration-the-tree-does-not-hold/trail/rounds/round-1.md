# Review round 1: 1793756609-an-enumeration-the-tree-does-not-hold

```seal
target: 0bb601f1c against origin/release/v0.31.1
```

This round reviews the whole branch, `git diff origin/release/v0.31.1..0bb601f1c`.
The base `origin/release/v0.31.1` is 0cb6014d1, which is also the merge base
(executed). The diff changes 17 files: seven work item records, two skill
files, two documents under `docs/`, four test modules (one deleted),
`skills/implement/acts.md` (deleted) and `.test_durations` (executed:
`git diff --stat`). The repository tracks no `seal/parity.md`, so no
`original:` line is owed and no parity comparison applies. `seal/config.md`
has no `Record language` row, so this record is English. No earlier round
exists, so nothing was carried. The runs took place in a
`git clone --no-local` at 0bb601f1c under this round's scratch directory,
which has since been removed.

The contract is `frame/design.md` (D1 items 1 to 10, D2, O1 to O6,
`## Removes`, A1 to A7, the no-change block of `## Rule changes`) and
`frame/plan.md`. The account under review is `trail/phases/phase-1.md`,
`gaps.md`, `changelog.md` and the commit messages. Each was read as a claim.

The round asked three questions. Does the diff remove what the frame names,
and nothing else? Does anything in the tree still read the removed rule,
file or test, under the old words or other words? Do the removal's grounds
hold against `skills/core/SKILL.md` *The rule a mechanism is kept against*?
The first two hold, as the confirmations below set out. The grounds hold
too. The deleted module's every finding message is about the table (read at
0cb6014d1). The cost records the frame cites say what the frame says they
say. A wider issue search than the frame's found more issues naming the
table, and each names a cost or a stale row, not a catch. One sentence of
the changelog fragment states that search's result wider than the search
supports, which is finding 1.

Three weaker spots are noted here, and none is a finding. First,
`tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py:71`
still returns `(level, title, line)`, and no caller reads the level.
9647894f2 (#330) widened `headings` to that shape for the deleted reader
(executed: `git log -S "len(match.group(1))"`). `frame/design.md`
*Data & interfaces* keeps the signature, and `gaps.md` *Not done* names the
gap. The docstring's description of the tuple is still true, so nothing
tells a reader something false. Second, D1 item 8 says the deleted case
pinned "that a session skipping the preflight loses only time". The case
asserted three things about the acts row: that one row names the section,
that it reads `still a sentence`, and that it names the preflight. The
"loses only time" sentence stood in its docstring as grounds, not in an
assertion (read: `git show 0cb6014d1:tests/text/test_broad_gate_rule.py`).
That sentence stands at `skills/code-review/orchestration.md:485` at HEAD
(the frame's `:487` is at acf37c448, as the frame's opening says). No case
pinned it before the diff or after, so no behaviour moved. Third,
`docs/layout/the-record-layout.md` *A change to the way of working writes
its process row in its own fragment* says the orchestrator writes the
process rows. The crafter wrote them, as the phase's spawn asked, and
`frame/plan.md` *Judgments of the run* records it. Both rows hold for the
two orchestration files the diff changes.

## Findings

### 1. The changelog fragment says an issue search found no issue but #506 that took its subject from the table, and a wider search lists #1109 and #1163, which did

```seal
severity: should
location: `seal/threads/1793756609-an-enumeration-the-tree-does-not-hold/changelog.md:3`
evidence: executed `gh issue list --state all --limit 50 --search '"acts.md"'`, `gh issue list --state all --limit 50 --search '"which of these acts"'`, `gh issue list --state all --limit 50 --search '"Delivered by"'`, `gh issue view 1109 --json body,comments`, `gh issue view 1163 --json body,comments`
```

Why it matters: the fragment becomes the release note, which a person reads
as the record of why the table went. It says "a search of the issues since
the table shipped found none, #506 aside, that took its subject from it".
The frame's search, `frame/design.md:28`, matched two phrases and calls
itself a sample. Its narrower claim is that no issue took its subject from a
`still a sentence` row. A search on the table's section title and the
`acts.md` path lists more issues. #1163's title names "the acts table": the
table's words were read by every orchestrating session, and that issue
moved it out of `skills/implement/orchestration.md`. #1109 names a stale row
of the table, a rename that left "detracers" in the *Question 1* row. #1102
and #1189 name `acts.md` as a paste pair and as a phase's output. Each is a
cost of the table or a defect in it. None arose from an act the table showed
as unarmed. So the fragment's conclusion, that the table caught nothing,
holds. But "took its subject from it" is false as written for #1163 and
#1109, and those two issues support the removal.

The fix changes the one sentence. `frame/design.md:28` names its own search
and calls it a sample, so the fix pass owes nothing there. It may add the
wider search's issue numbers to that row. `frame/plan.md` A3's "the record
shows it did not" speaks of a catch and stays true.

```markdown
Every message the test could report was about the table itself, and a search of the issues since the table shipped found none, #506 aside, that a row of it led to: those that name it, such as #1109 and #1163, name a stale row or what the table cost.
```

The text it replaces, at `changelog.md:3`: "Every message the test could
report was about the table itself, and a search of the issues since the
table shipped found none, #506 aside, that took its subject from it."

```seal
verdict: fixed 23ce57c18
answer: The finding holds: #1163 takes its subject from the cost of reading the table and #1109 from a rename defect in its Question 1 row (executed: `gh issue view 1163`, `gh issue view 1109`), so "found none that took its subject from it" was false. The paste-ready text was not applied as written, and `changelog.md:3` now says it in my own words: the search found several issues that name the table, such as #1109, #1163 and #506, and each names a defect in a row, a cost to its readers or a limit of the table, and none came from an act the table listed as one nothing notices when skipped. The proposed "#506 aside, that a row of it led to" leaves unclear what "led to" means, and it sets #506 apart even though #506 is itself an issue about the table's limits. "A stale row" was narrowed to "a defect in one of its rows", because #1109's row was garbled by a substitution and was not out of date. `tests/github/test_publish_release_note.py` and `tests/behaviour/test_chain_hooks_hardening.py` pass at 23ce57c18 (executed: `bin/test -q`, exit 0).
```

## Confirmations

```seal
confirms: none
```
What matched: A1. `git grep -n -E 'acts\.md|test_every_orchestrator_act_names_its_delivery|which of these acts runs itself|Delivered by|part of its parent' -- ':!seal/threads'` prints nothing and exits 1, and `git grep -n 'still a sentence' -- ':!seal/threads'` prints only `tests/skills/test_session_cost.py:17` (executed). A scan of every tracked file outside `seal/threads/` and `.test_durations`, with line breaks and comment leaders folded into spaces, for those words and for "acts are counted", "counted by nobody", "each of its acts", "the orchestrator's table" and "table of the acts", finds only the same `test_session_cost.py` line (executed: a `python3 -I` scan run once from the shell). That catches the line-break split #506 item 1 describes. It is a search of wordings over an open class, so it is a sample. Neither search lists a statement of the removed rule.

```seal
confirms: none
```
What matched: the claim in `trail/phases/phase-1.md` that the removal list is whole. At 0cb6014d1 the same A1 pattern, with `still a sentence` added, lists eleven files: the ten D1 items name every one, and the eleventh is the O3 history line (executed: `git grep -l` at 0cb6014d1). `.test_durations` loses exactly 22 entries and parses as JSON (executed: `git diff` counted, `json.load`). Of the 22, 18 name the deleted module, one the deleted case, and three the `acts.md` parameters of `test_docs_line_wrap.py` and `test_a_document_that_names_a_script_says_how_to_reach_it.py` (read, in the diff). Every `## Removes` row has its hunk in the diff, and the diff has no hunk outside them and the work item's records (read).

```seal
confirms: none
```
What matched: A2. `bin/seal rules --check` exits 0 with "all 225 check lines in 70 rule files hold" (executed). `docs/running/the-agent-set.md` *What a spawn costs* loses the acts paragraph and its check line, and its other three rules are unchanged (read, `docs/running/the-agent-set.md:135-160` and the diff). `docs/layout/the-pact.md:68` names `tests/behaviour/test_a_signer_declares_its_pact.py` alone (read).

```seal
confirms: none
```
What matched: A3. Neither `skills/implement/orchestration.md:1-20` nor `skills/code-review/orchestration.md:1-14` cites `acts.md` (read). `skills/code-review/orchestration.md:14` says every `##` heading opens with `Orchestrator:`, and every `##` heading in that file does (executed: `grep -n "^## "` filtered for the marker, exit 1).

```seal
confirms: none
```
What matched: A4 and A5. `bin/test` over the marker module, `tests/behaviour/test_docs_line_wrap.py`, `tests/text/test_broad_gate_rule.py`, `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py` and `tests/text/test_no_passage_is_pasted_into_a_second_file.py` gave 116 passed and 9 skipped, exit 0 (executed). The `headings` docstring names one reader, `marked_headings` (read, `tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py:71-84`).

```seal
confirms: none
```
What matched: A6 and A7. The diff adds no test, check, hook, mark or rule. Its only added lines outside the work item's records are the shortened check line, the shortened code-review opening and the docstring's kept clause (read, in the diff). `.claude-plugin/plugin.json` is outside the diff and reads `0.31.1` (executed: `git diff --stat`, `grep version`).

```seal
confirms: none
```
What matched: the two departures in `trail/phases/phase-1.md` and the fold 0bb601f1c made of them. The comment "Cut from it in #1148, wrapped as it was." heads the `skills/implement/multi-repository.md` entry at `tests/behaviour/test_docs_line_wrap.py:150-151`. aa9221d3f added both `acts.md` and `multi-repository.md` (read: `git log --oneline -1 aa9221d3`). The docstring's kept sentence is the removed paragraph's first clause. D1 items 7 and 9, their `## Removes` rows, the process-row cell of *Grounding* and *Operational impact* now say what the build did (read, `frame/design.md` and `frame/plan.md`).

```seal
confirms: none
```
What matched: the claim in `gaps.md` *Not verified* that seven modules read no changed path. `tests/skills/test_settle.py:1125` and `:1376` name `skills/implement/orchestration.md` inside a fixture string and do not open the file. The other six name none of the changed paths (executed: `grep -n` over the seven). The 27 modules under `tests/`, `evals/` and `.github/` that name a changed file or section, `test_settle.py` among them, gave 751 passed, exit 0 (executed, see *Probes*).

```seal
confirms: none
```
What matched: the removal's grounds (`frame/design.md` *Grounding*, D1). The deleted module's finding messages, read at 0cb6014d1, each name a row, a heading's relation to a row, or the table's absence. None names an orchestrator act that went undelivered. The cost records exist as cited: `1793688270-a-check-line-names-a-case-or-the-rule-carries-none/trail/rounds/round-1.md` finding 2 is a `should` on `acts.md:69`, `1793726048-the-stop-judgment-holds-against-later-rows/trail/phases/phase-1.md:146` re-reads `acts.md:76`, `1793661729-each-document-is-cut-by-who-opens-it/trail/phases/phase-4.md:35-48` adds rows for three marked headings, and `1793732301-the-readme-is-written-for-a-first-reader/trail/phases/phase-2.md:12` names the README pair (read). The issue's *What is not here* says the table makes the unarmed acts "findable when one of them misses". `frame/plan.md` *Technical context* answers that a miss is measured from a run's records, and names the failure scenario. The owner's comment of 2026-11-03 on #506 leaves whether the table stays to this release (executed: `gh issue view 506`). `git show v0.31.0:skills/implement/acts.md` resolves, as the fragment says (executed: `git cat-file -e`).

```seal
confirms: none
```
What matched: O3 and O5. `tests/skills/test_session_cost.py:15-20` sits under the module's "Their docstrings follow, as they stood." and states no fact of the table. `skills/verify/scripts/session_cost.py:38` and `:2901` cite #330 for the posting command, not for the table (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| the full suite, the repository-wide lint, the format check and the typecheck at the work item's HEAD; this round ran the narrow modules named under *Probes* and nothing broader | the `Broad gate` row of `seal/config.md` | the orchestrator, at the broad run after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the five modules A4 and A5 name, `-q` | 116 passed, 9 skipped, exit 0 |
| `bin/test` over the 27 modules `git grep -l` lists under `tests`, `evals` and `.github` for the changed files' paths and the two changed section titles, `-q` | 751 passed, exit 0 |
| `bin/seal rules --check` | exit 0, "all 225 check lines in 70 rule files hold" |
| `python3 -I` scan of every tracked file outside `seal/threads/` and `.test_durations`, line breaks folded, for the table's and the rule's words | one hit, `tests/skills/test_session_cost.py`, the O3 line |
| `gh issue list --state all` searched for `"acts.md"`, `"which of these acts"`, `"Delivered by"`, `"still a sentence" in:body` and the deleted module's name | #506, #1102, #1231, #1189, #1163, #1109, #1046, #1148, #330 and #326; none arose from an act the table listed as unarmed |
