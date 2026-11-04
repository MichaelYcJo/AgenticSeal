# Guarantee: 1793756609-an-enumeration-the-tree-does-not-hold

| Field | Value |
|---|---|
| Broad gate | 6fa52a5d2 against 0cb6014d1 (`trail/gate.md`, its one `seal` block; only `trail/gate.md` follows it, in aa296c059: executed, `git log --no-merges --name-only 6fa52a5d2..HEAD ^0cb6014d1`) |

The base `release/v0.31.1` resolves through `release/v0.31.1@{upstream}` to
0cb6014d1; the local branch is at 8d5a59c6c and was not used (executed:
`git rev-parse --verify --quiet`). `seal pr-body <item> --body <file>
--check` exits 0 with the tree's `bin/seal` and the installed 0.31.0 copy
alike (executed). The phase records claim no `seen red`: no case was added,
so the sample is of `executed` claims. The repository tracks no
`seal/parity.md` and `routing.md` answers `open the pull request`, so no
parity comparison is owed (executed: `git ls-files seal/parity.md`).

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| Nothing outside `seal/threads/` names the table, its test or its section | `trail/phases/phase-1.md:41-43`, `frame/design.md` A1 | `git grep -n -E 'acts\.md\|test_every_orchestrator_act_names_its_delivery\|which of these acts runs itself\|Delivered by\|part of its parent' -- ':!seal/threads'` | holds: no output, exit 1 (executed) |
| `still a sentence` stands only in the O3 history line | `trail/phases/phase-1.md:44-45` | `git grep -n 'still a sentence' -- ':!seal/threads'` | holds: only `tests/skills/test_session_cost.py:17` (executed) |
| Every `## Removes` row and every removal the changelog names is gone from the tree | `frame/design.md` *Removes*, `changelog.md:3` | `ls` of the two deleted paths; `git grep -n -E` for `test_the_acts_table_row_names_the_preflight`, `acts are counted`, `One parser, two readers`, `counted by nobody`; `git diff 0cb6014d1...HEAD` of `docs/layout/the-pact.md`, `skills/*/orchestration.md`, `tests/behaviour/test_docs_line_wrap.py` | holds: both files absent, the words stand only in this work item's records, the check line names `tests/behaviour/test_a_signer_declares_its_pact.py` alone, neither opening cites `acts.md`, the `COVERED` entry is gone and its comment heads `multi-repository.md` (executed) |
| `.test_durations` parses and holds no entry for the removed cases or `acts.md` parameters | `trail/phases/phase-1.md:51-53`, `frame/design.md` D1 item 10 | `python3 -I -c "json.load(...)"`, keys filtered for `acts` and `every_orchestrator_act` | holds: 6323 entries parse; the nine keys matching `acts` hold it inside `pacts`, `contracts` and `withheld_acts` in other modules, and none names `acts.md` or the deleted module (executed) |
| Every check line holds after the removal | `trail/phases/phase-1.md:58-59`, `frame/design.md` A2 | `./bin/seal rules --check` | holds: "all 225 check lines in 70 rule files hold", exit 0 (executed) |
| The narrow modules A4 and A5 name, and the two the fix pass ran, pass | `trail/phases/phase-1.md:67`, `frame/design.md` A4, A5, round 1 finding 1's answer | `./bin/test -q` over the marker module, `test_docs_line_wrap.py`, `test_broad_gate_rule.py`, `test_a_document_that_names_a_script_says_how_to_reach_it.py`, `test_no_passage_is_pasted_into_a_second_file.py`, `test_publish_release_note.py`, `test_chain_hooks_hardening.py` | holds: 196 passed, 9 skipped, exit 0 (executed) |
| The version stays `0.31.1` | `frame/design.md` A7 | `grep version .claude-plugin/plugin.json`; `git diff --quiet 0cb6014d1 HEAD -- .claude-plugin/plugin.json` | holds: `0.31.1`, exit 0 (executed) |
| The old table stays readable at `v0.31.0`, and the table shipped in v0.13.1 | `changelog.md:3`, `frame/design.md:28` | `git cat-file -e v0.31.0:skills/implement/acts.md`; `git tag --contains 9647894f2 \| sort -V \| head -1` | holds: exit 0; `v0.13.1` (executed) |
| The preflight fact the deleted case read stands in the tree | `frame/design.md` D1 item 8 | `grep -n -i preflight skills/code-review/orchestration.md` | holds at `:485`, as round 1 says (the frame's `:487` is at acf37c448) (executed) |
| The commits after round 1's target touch only this work item's records | round 1 finding 1 `fixed 23ce57c18`, the pull request body's *For the reviewer* | `git show --stat` of 8ac3f5b4a, 23ce57c18, 9c1de5391, 6fa52a5d2, aa296c059 | holds: each touches only files under `seal/threads/1793756609-an-enumeration-the-tree-does-not-hold/` (executed) |
| Round 1's heading and path searches add #1109 and #1163 to the `"acts.md"` search's #506, #1102, #1189 and #1231, and the Grounding row lists every issue the searches return | `frame/design.md:28`, `frame/plan.md:68` | `gh issue list --state all --limit 50 --search` for `"acts.md"`, `"which of these acts"`, `"Delivered by"`, `"still a sentence" in:body` and the deleted module's name | **does not hold**: the `"acts.md"` search returns exactly #506, #1102, #1231, #1189; the `"which of these acts"` search (round 1's heading search) returns #506, #1163, #1109 **and #1046 and #1148**, both opened after v0.13.1 (2026-10-27, 2026-10-29), which `frame/design.md:28` does not list. `"Delivered by"` returns #330 and #326, opened before the table shipped (executed). Round 1's *Probes* row lists #1046 and #1148 (read) |
| #1046 and #1148 leave the conclusion standing | `frame/design.md:28`, `changelog.md:3` | `gh issue view 1046` and `1148`, bodies searched for the table's words | holds: #1046 names two acts-table rows its move must replace (a cost), #1148 the 1,753 words every orchestrating session read (a reading cost); neither came from a `still a sentence` act (executed) |
| Re-audit at 94d6950e5: only this work item's records follow the broad run, and nothing outside them changed since aa296c059 | `trail/gate.md` (run 6fa52a5d2) | `git log --no-merges --name-only 6fa52a5d2..HEAD ^0cb6014d1`, `git log --no-merges --name-only aa296c059..HEAD` | holds: 7665c47e9 touches `guarantee.md`, 94d6950e5 `frame/design.md` and `frame/plan.md`; no path outside `seal/threads/1793756609-an-enumeration-the-tree-does-not-hold/` (executed) |
| Re-audit at 94d6950e5: the `"acts.md"` search returns #506, #1102, #1189, #1231; `"which of these acts"` returns #506, #1046, #1109, #1148, #1163; `"still a sentence" in:body` returns #506 alone | `frame/design.md:28`, `frame/plan.md:68`, the pull request body's *For the reviewer* | `gh issue list --state all --limit 50 --search` for each of the three | holds: the three lists come back exactly as the row states (executed); the row calls the searches a sample and claims no whole list beyond them (read) |
| Re-audit at 94d6950e5: the copy below the body's records line is the records' own text | the body file | `./bin/seal pr-body seal/threads/1793756609-an-enumeration-the-tree-does-not-hold --body <file> --check` | holds: exit 0 (executed) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | the table, its test and the rule stating them go with every citation and pin on them, nothing replaces them, neither of #506's repairs is built (D1, D2, `## Removes`) | the build, the issue's owner comment of 2026-11-03 and `routing.md` *Why this way* (the choice of repair is this work item's), the tree (every `## Removes` row re-run above) | the issue tracker on its own Grounding row: `frame/design.md:28` says round 1's heading search adds #1109 and #1163, and that search returns #1046 and #1148 as well |
| the build | phase 1 removes the ten D1 items in e24c3b31b, with two departures (the `COVERED` comment kept, one docstring sentence kept) the frame was folded to state | the design as folded (`frame/plan.md:67`), the diff (read), every re-run above | none |
| the last round | round 1 at 0bb601f1c: the removal holds, one `should` on the changelog's issue-search sentence, `fixed 23ce57c18`; its *Probes* row lists #1046 and #1148 among the search results | the tree, the issue tracker; the fix at HEAD: `changelog.md:3` now says the search found "several that name it, such as #1109, #1163 and #506" and none came from an unarmed act, which answers what the finding asked and holds for #1046 and #1148 too (read, executed) | none |
| the changelog | the table and test are removed, the searched issues each name a defect, a cost or a limit, none a catch; the rule, citations and pins go; the marker keeps one meaning; process rows for both orchestration files | the design, the build, the diff, the issue tracker (its "such as" makes no claim of a whole list) | none |
| the orchestrator's part of the pull request body | the same removal and grounds; Closes #506; *For the reviewer*: "The same search in `frame/design.md` *Grounding* was folded to list every issue it returns (`frame/plan.md` *Judgments of the run*, second row)"; the broad run at 6fa52a5d2 | the design, the build, the round, the changelog, `trail/gate.md` on the run's commit (read; the suite's counts it quotes are `unverified` by me, answered by the orchestrator's `seal gate` output) | the issue tracker: the Grounding row does not list every issue the search returns, #1046 and #1148 being absent; `frame/plan.md:68`, the orchestrator's own judgment row, and commit 9c1de5391's subject make the same claim |
| the design, at 94d6950e5 | `frame/design.md:28` states what each of the three searches returns, #1046 and #1148 among them, and calls them a sample | the issue tracker (the three searches re-run), round 1's *Probes* row, the changelog, `frame/plan.md:68` | none |
| the orchestrator's part of the pull request body, at 94d6950e5 | *For the reviewer* names #1046, #1102, #1109, #1148, #1163, #1189 and #1231 beside #506 as what the three searches return, none from a `still a sentence` row, and says the first audit withheld on the earlier fold; its other paragraphs are unchanged | the design and `frame/plan.md:68` at 94d6950e5, the issue tracker, the first verdict block (read, executed) | none; commit 9c1de5391's subject still says "every issue", a commit subject, not a record or the body; that the squash merge drops it is the orchestrator's claim (unverified, answered by the orchestrator) |

```seal
target: aa296c059 against 0cb6014d1
Verdict: withheld reason: the design's Grounding row (seal/threads/1793756609-an-enumeration-the-tree-does-not-hold/frame/design.md:28) says round 1's search by the table's heading adds #1109 and #1163, and the orchestrator's judgment row (frame/plan.md:68) and the pull request body's For the reviewer paragraph say that row lists every issue the searches return; gh issue list --state all --search '"which of these acts"' also returns #1046 and #1148, opened after v0.13.1 and listed in round 1's Probes row, which design.md:28, plan.md:68 and the body omit; the conclusion that none came from a still a sentence row holds for both, so only the list and the claim that it is whole need correcting
```

```seal
target: 94d6950e5 against 0cb6014d1
Verdict: sealed
```
