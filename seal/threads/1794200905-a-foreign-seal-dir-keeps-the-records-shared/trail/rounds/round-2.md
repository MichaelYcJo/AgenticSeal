# Review round 2: 1794200905-a-foreign-seal-dir-keeps-the-records-shared

```seal
target: b0108a2c, fixes 2159b115..b0108a2c
```

This is a verifying round over the diff of the fixes for round 1, `2159b115..b0108a2c`. That range holds the round-1 record and its close blocks, the orchestrator's fold `22e5f69e`, the fix pass's four commits `01dabf91`, `ee10f8e8`, `c8f1884e` and `180ea5db`, and the requote `b0108a2c`. The round worked in a `git clone --no-local` of the worktree, checked out at `b0108a2c`.

Carried from round 1 and not re-established: the merge base with `origin/release/v0.37.0` is `c0bf670d` (re-run: `git merge-base HEAD origin/release/v0.37.0` gave the same commit). `seal/parity.md` is not declared (executed: `ls` found no file), so no parity comparison applies. The record language and `Commit and pull request language` are both English (executed: `grep` of `seal/config.md:9-10`), so no `pr.<lang>.md` is owed. Round 1's rename probe of finding 3 is not run again: the range changes only the docstring of `chain_check.py#root_name` and no line of code in `chain_check.py` or `lib/` (executed: `git diff --stat 2159b115..b0108a2c -- skills/code-review/scripts lib`, one file, `chain_check.py`, and its hunk is the docstring alone).

The round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md` whole at `b0108a2c`. Each of the nine quotes in `pr.md` stands word for word, with runs of whitespace collapsed, in the source and the item its coordinate names (executed: a read-only script comparing each quote with `changelog.md` and `gaps.md`, nine of nine found). The round-1 record changed in the range only by 26 added lines, the five close blocks (executed: `git diff 6fae62b8..b0108a2c` of the record, no removed line).

## Findings

### 1. The changelog's process row still says the core defines `seal/` as the root's name in every shipped text, without the exception the core now states

```seal
severity: should
location: `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/changelog.md:14`
evidence: read `skills/core/SKILL.md:23-28`, `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/changelog.md:5`, `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/changelog.md:14`; executed `git grep -n "every shipped text\|every text\|root's name in"` over the work item's records except the rounds, `docs`, `skills`, `templates`, both READMEs and `CONTRIBUTING.md`
reopens: round-1#4
```

Why it matters: the close of round 1 finding 4 holds for the two statements it names. The core now says "`seal/` is that root's name in every text this plugin ships, except where a text says a `seal/` is the project's own or that its `README.md` does not open with the marker" (`skills/core/SKILL.md:23-26`), and the changelog's third item carries the same exception (`changelog.md:5`). Round 1 gave the reason the changelog was owed the exception: it paraphrases the core's sentence. The fragment paraphrases that sentence a second time, in the second row of its `### Process changes` table: "`skills/core/SKILL.md`'s opening paragraph defines `seal/` as the records root's name in every shipped text and names `agentic-seal/` once" (`changelog.md:14`). That row still states the definition without the exception. Contract rule 12 makes the work item's records, each read whole, part of the fix pass's closed set, so the second paraphrase belonged to the fix. The search in `evidence:` lists the statements of the core's sentence across the shipped text and these records. Outside the core, only `changelog.md:5` and `:14` restate it, and of those, only `:14` lacks the exception. The release note carries this row to a person updating their process. That person reads that every `seal/` in the plugin's text names the root, which is the double reading finding 4 removed from the core. `pr.md` does not quote the row, so `pr.md` needs no change.

The fix gives the row the exception in the words of the third item:

```markdown
| 2026-11-09 | `skills/core/SKILL.md`'s opening paragraph defines `seal/` as the records root's name in every shipped text, except where a text says a `seal/` is the project's own or that its `README.md` does not open with the marker, and names `agentic-seal/` once; contract rule 11 and `skills/implement/SKILL.md` point at it | The many `seal/` paths agents act on stay true under one definition, so a rename changes one sentence, `lib/optin.py` and one line of each README | https://github.com/MichaelYcJo/AgenticSeal/issues/1059 |
```

```seal
verdict: fixed 591e3fd7
answer: The second row of changelog.md's Process changes table now reads the round's paste-ready row, carrying the exception the core and the third Added item hold. The fix touches the work item's records alone; pr.md quotes no part of the row.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `install_workflow` now names the place it looked at, `display(repo, shared) or optin.HOME` (`skills/implement/scripts/seal.py:1976-1981`). Beside a package, `home_paths`'s shared entry is `<repo>/agentic-seal` (`lib/optin.py:200-202`), so the person reads "no root stands at agentic-seal/ in this tree". The fix pass claimed that a mutant replacing the name with `optin.HOME` turns the new case red. In the clone, the round replaced that line with `name = optin.HOME` and ran the case. It failed on `tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py:294`, the assertion on the place's name, and printed "no root stands at seal/ in this tree" (executed, `## Probes`). The round then put the line back, and `git status` showed a clean clone. Read against its group, the new case adds a fact the group does not hold. The parameter "a project's own seal" of `tests/skills/test_seal.py:2559-2612` asserts the kind and the shared wording but no place name, and `:280` covers the shared state. The fix pass also kept the `seal pr-checks` status line "writes it where seal/ is in the tree" (`seal.py:2236`). The round weighed that answer and agrees with it. The line uses `seal/` as the root's name in text, which *Scope* item 3's last sentence allows (`frame/design.md:34`). It is a condition, not a claim about what stands in the tree. A person who runs install on its strength beside a package gets the corrected refusal, which names `agentic-seal/`. Every other message of `seal.py` composed from `optin.HOME` is a zip member name, the local place or the release-pin line (executed: `grep -n "optin.HOME}"`, lines 594, 624, 673, 858, 1290, 1956 and 2236).

```seal
confirms: round-1#2
```
What holds: in both files, the sentence now stands before the commands (`templates/setup/seal-README.md:39-48`, `seal/README.md:39-48`). The paragraph after the commands is gone, and the two files are byte-identical (executed: `cmp`, exit 0). The departure from the round's paste-ready text is sound. In local mode the README is `$(git rev-parse --git-common-dir)/seal/README.md`, so the folder holding it is named `seal`. Round 1's condition, "where the folder holding this file is not named `seal`", is then false for the local-to-shared move beside a package. A person would run `mv … "$(git rev-parse --show-toplevel)/seal"` and move the local root into the package. The fix pass's sentence holds in both directions. Beside a project's own `seal/`, each `--show-toplevel` path ends in the second name, and the local path keeps `seal`, which matches `home_paths` (`lib/optin.py:200-206`). The sentence sends the reader to the plugin's `README.md` *Shared or local*, which states `<repo>/agentic-seal/` on one line (`README.md:188`). It writes no `agentic-seal`, so the scanned-file case stays green. Its last clause, "run as written there, the commands would move the project's own directory", describes the shared-to-local pair exactly. For the local-to-shared pair the commands move the local root into the project's directory, which differs in detail and calls for the same action. The round judged this no finding. The cases that read the paragraph pass (executed: `bin/test tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_no_document_names_the_old_roots.py …`, 171 passed).

```seal
confirms: round-1#3
```
What holds: `frame/plan.md:24` and `frame/design.md:45` carry round 1's two sentences word for word (read). The *Out* item says the limit is stated in `chain_check.py#root_name`'s docstring, and the docstring now says it (`skills/code-review/scripts/chain_check.py:1855-1859`). It says a renamed root is read under the new name and that a declaration deleted under the old name without moving it is not judged. Round 1's probe showed both behaviours, and the code it ran is unchanged in the range. `home_paths`'s docstring states the reading-under-the-current-name limit the new sentence points to (`lib/optin.py:171-174`). The fold also added a row to *Judgments of the run* (`frame/plan.md:61`). Both sections that row cites stand in their files (read: `skills/code-review/orchestration.md:16`, `skills/implement/orchestration.md:55`). The row claims the owner's README request is now recorded on issue #1059. A comment dated 2026-11-09T07:33 records it (executed: `gh issue view 1059 --json comments`).

```seal
confirms: round-1#5
```
What holds: `changelog.md:5` says "three cases in `tests/behaviour/test_no_document_names_the_old_roots.py` hold the second name". The module holds three such cases, and they pass (executed, in the 171 above). `pr.md:7` quotes that sentence word for word (executed, the quote check above).

What matched: nothing else in the range breaks a case. The modules that read the changed text and code pass at `b0108a2c` (executed: `bin/test` over the behaviour module, `test_no_document_names_the_old_roots.py`, `test_first_setup_asks_once.py` and `tests/lib/test_optin.py`, 171 passed; over `test_docs_line_wrap.py`, `tests/lib/test_core.py`, `tests/text/test_a_rider_reaches_its_file.py`, `tests/text/test_every_agent_reads_the_contract.py`, `test_chain_hooks_hardening.py`, `tests/skills/test_chain_check.py`, `tests/skills/test_seal.py` and `test_a_cited_section_stands_in_its_file.py`, 779 passed; and `tests/text`, 466 passed). These are narrow runs, not the suite, and the suite stays `unverified`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| S7: the full suite, the lint and the typecheck at `b0108a2c`, which this round did not run (contract rule 2); the suite is `unverified` | `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/gaps.md:7` | the orchestrator, at the broad gate |
| The owner's README request. The issue comment of 2026-11-09 records the decision, but this round cannot tell the owner's words from the orchestrator's account of them | `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/frame/plan.md:60-61` | the sealer, who reads the issue against the tree |
| `pr.md` closes #1059 while `frame/questions.md` Q1, the measurement the *Done when* asks for, is `open`, and `gaps.md` names it as owed | `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/pr.md:11`, `seal/threads/1794200905-a-foreign-seal-dir-keeps-the-records-shared/frame/questions.md:17` | the orchestrator, by the measurement Q1's default names |
| The `agentic-seal/` cases, the new install case among them, on Windows | `lib/optin.py:200-202`, `tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py:286-295` | CI's Windows leg |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py -q -p no:xdist -k names_agentic_seal_where_no_root`, with `seal.py:1976` changed to `name = optin.HOME` in the clone through the `Edit` tool | 1 failed, on the assertion `"no root stands at agentic-seal/ in this tree" in out`, with the message reading "no root stands at seal/ in this tree"; the line was restored through `Edit`, and `git status --short` printed nothing |
| a read-only `python3 -I -c` script that extracts each quote of `pr.md` with its source file and checks whether the quote, with whitespace collapsed, stands in that file | nine lines, each `True` |
