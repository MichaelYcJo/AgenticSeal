# Review round 6: 1794271938-follow-up-holds-seven-owner-questions

```seal
target: 48e3b76da, fixes 0611f4199..48e3b76da
```

This is the verifying round over round 5's fix pass. The code reviewed is the diff `0611f4199..48e3b76da`: the record commit `ce2785e64`, the orchestrator's frame repair `2a059f2a9`, the fix pass `46e6d49e0`, the close commit `5e8267516` and the orchestrator's fold `48e3b76da`. Its one code change is the last paragraph of `argv_words`' docstring (`tests/github/test_close_issues_on_release.py:113-128`). The reader and every case are unchanged, and no file under `.github/scripts/` changed (executed, `git diff --stat 0611f4199..HEAD`). The work item's present-state records were each read whole at `48e3b76da`: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`. No `pr.<lang>.md` stands, and `Commit and pull request language` is English. `seal/parity.json` is not declared.

Carried from rounds 1 to 5 and not re-established: the confirmations of *Scope* items 2 to 6, which the fix diff does not touch; the phase records, which the fix diff does not change; round 5's account of the docstring's kept and dropped words at `:102-110`. Re-opened at round 5's coordinates rather than searched again: the two converted cases (`tests/github/test_release_completeness_check.py:577-580`, `tests/github/test_label_merged_on_release_branch.py:400-414`) and the closer's `issue_argvs` (`tests/github/test_close_issues_on_release.py:1219-1221`). Round 5's `evidence: executed` lines were run again in a new form: the three modules, `gh issue -R example/repo close --help`, and the `words[:3]` the converted cases compute, here read from `argv_words` over each planted argv rather than planted into the scripts (`## Probes`).

The spawn sets the scope: whether each round-5 finding is closed by the commit its close block names, and whether the new text is true of the code at HEAD. It also says that an argv shape fitting the stated rule is no finding, and that a statement the code contradicts is one.

The fix pass changed the round's phrase "`gh` and the two after it" to "`gh`, its noun and its verb". Claimed in the close block: the round's phrase was untrue of its own `--repo` example. Found: `argv_words('closer.run("gh", "issue", "--repo", repo, "close", "1")')` gives `["gh", "issue", "--repo"]` as the first three words, and `argv_words('run("gh", ISSUE, "close", "1")')` gives `["gh", "close", "1"]` (executed). Each list is `gh` and the two words after it, so the round's phrase would have left both examples outside the class it named. Neither list is `gh`, its noun and its verb, so the new phrase puts both inside it. The `env` plant gives `["env", "GH_PROMPT_DISABLED=1", "gh"]`, outside both phrases' "`gh` first". The correction is right, and the round's snippet was the defect it repairs.

One further shape was weighed and is no finding. `run("gh", "issue", VERB, "close")`, with the verb held in a module-level name, gives `["gh", "issue", "close"]` (executed). Its true verb is the name's value, so its first three kept words are not `gh`, its noun and its verb, and the gate case still reads a `close` there. That contradicts "it judges no argv whose first three kept words are not `gh`, its noun and its verb" only on a strict reading of "its verb". The shape errs red, on an argv whose word after the true verb spells a forbidden verb, and no sentence tells a reader that such an argv passes. No release script writes one (executed, `## Probes`). The docstring's earlier paragraph, "the prefix shifts by one, and the verb is never matched" (`:106-107`), describes the same shift and is outside the fix diff.

## Findings

None. Both round-5 findings are closed by the commits their close blocks name, and every sentence the fix diff wrote is true of the code at `48e3b76da`.

## Confirmations

```seal
confirms: round-5#1
```
What holds: the count "Two kinds" and the claim that every case judges by an argv's first three words have left every file round 5 located. `git grep` for "the two after it", "Two kinds", "judges an argv" and "first three words" over `tests/github/` and the work item's present-state records finds no count of escapes and no sentence saying the `--add-label` claim reads the first three words (executed, each hit read). The docstring now says "A verb claim judges an argv by its first three kept words" and "The label case's `--add-label` claim is no verb claim: it reads every word of every argv" (`tests/github/test_close_issues_on_release.py:114-123`). The code holds both: the verb claims are `words[:3]` comparisons (`tests/github/test_release_completeness_check.py:577-580`, `tests/github/test_label_merged_on_release_branch.py:400-415`), and the `--add-label` claim is `any("--add-label" in words for words in argvs)` (`tests/github/test_label_merged_on_release_branch.py:403`). Its three examples hold: the name and `env` lists above, and `gh` taking `--repo` before the verb (executed, `gh issue -R example/repo close --help`, exit 0). "A forbidden argv of that kind is not seen, and a required one reads as missing" holds of the gate's forbidden list, the label case's `gh label create` and the closer's `len(closes) == 1`. The docstring's last clause holds at HEAD: across every script in `.github/scripts/`, each argv carrying `issue` or `label` as a word either starts `gh`, its noun and a verb, or is a one-word `plural(..., "issue")` argument (`release_seal.py:180`, `publish_release_note.py:638`), and no `gh issue` or `gh label` argv has a flag as its third word (executed, `## Probes`). The `gh(*args)` wrapper at `release_seal.py:444` is called with `release` only (read, `:558-593`). The changelog's *Changed* second item states the same rule and examples, and "which `argv_words` drops" holds of `word`, which returns `None` for a name (`:131-142`). `46e6d49e0` touches `tests/github/test_close_issues_on_release.py` and `changelog.md`, two of the finding's locations.

```seal
confirms: round-5#2
```
What holds: the grounds of `frame/plan.md:73` end "#1493 row 7 keeps the constant-valued escape open; this row leaves the other argvs the verb claims do not judge open with it", the round's clause, written by `2a059f2a9`. Row 7 of #1493's body still ends "The constant-valued escape stays open" (executed, `gh issue view 1493`: open, no comments). `frame/design.md:42` says "The issue keeps the first open", so the two records now agree on what the issue decided.

What matched: `frame/design.md:31` says the converted cases "judge each verb by an argv's first three words" and that the docstring and changelog say an argv whose first three kept words are not `gh`, its noun and its verb escapes every verb claim, with the three examples. Both texts say so (read, `tests/github/test_close_issues_on_release.py:113-128`, `changelog.md:4`).

What matched: `frame/design.md:42` names the same class and examples as *Out*, and its claim that the issue keeps the first open matches row 7 (executed, `gh issue view 1493`).

What matched: `frame/design.md:72` says "A verb claim selects the argvs it judges by their first three words, such as `words[:3] == ["gh", "issue", verb]`". The gate, label and closer cases each select so (read, the coordinates above and `tests/github/test_close_issues_on_release.py:1219-1221`).

What matched: `frame/plan.md:50` says the cases assert the verbs over argvs whose first three kept words are `gh`, its noun and its verb, and `--add-label` over every word of every argv, and that an argv with `env` before `gh` is judged by none of the verb claims. The code and the `env` list above hold each part (executed and read).

What matched: the first clause of `frame/plan.md:73`, "the cases judge each verb by an argv's first three words", and its "No release script writes an escaping argv today", which this round's scan of `.github/scripts/` holds at HEAD (executed).

What matched: each of the eleven quotes in `pr.md` stands word for word, with whitespace runs collapsed, in the source its coordinate names, and quotes 4 and 5 are the two sentences of `changelog.md`'s *Changed* second item that `46e6d49e0` wrote (executed, a `python3 -I` read of `pr.md`, `changelog.md` and `frame/plan.md`).

What matched: `gaps.md:6` names fix pass 5 and its close blocks in `trail/rounds/round-5.md`, which `5e8267516` appended (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite and the repository-wide lint. They are `unverified` in this round, and `gaps.md:6` names the orchestrator's run and `trail/gate.md` as its record. This round leaves nothing open, so what comes due is the orchestrator's broad run, and the sealer's spawn after it | `seal/config.json` `Broad gate` | the orchestrator |
| `changelog.md:9` says the measurements "are in #1493's body". At this round the body still holds none: it does not carry "move here", the first sentence of the text `frame/design.md` *Data & interfaces* gives (executed, `gh issue view 1493`). The text is appended when the pull request opens, and the sentence is true from that moment | `seal/threads/1794271938-follow-up-holds-seven-owner-questions/changelog.md:9`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/design.md:84` | the orchestrator, who appends the text, and the sealer, who reads the body |
| The two `tests/test_conftest.py::Test_census_case` failures, which `gaps.md:12` says predate the work item. This round did not run them | `tests/test_conftest.py`, `tests/censuses.py` | the orchestrator, through #1498 |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_close_issues_on_release.py tests/github/test_release_completeness_check.py tests/github/test_label_merged_on_release_branch.py -q -p no:cacheprovider`, in a `git clone --no-local` at `48e3b76da` under the round's scratch directory | exit 0, 114 passed |
| `tests/github/test_tmp_round6.py`, written through the `Write` tool and run once with the clone's `.venv/bin/python -m pytest -q -s -p no:xdist`, then deleted: it printed `[w[:3] for w in argv_words(src)]` for five snippets, and every argv of `.github/scripts/*.py` that carries `issue` or `label` or starts `gh issue` or `gh label` | exit 0, 1 passed. `--repo` plant: `["gh", "issue", "--repo"]`. Name as noun: `["gh", "close", "1"]`. `env` plant: `["env", "GH_PROMPT_DISABLED=1", "gh"]`. Name as verb then `"close"`: `["gh", "issue", "close"]`. Plain: `["gh", "issue", "close"]`. Every `gh issue` and `gh label` argv in the scripts has a verb third: `close_issues_on_release.py` `edit`, `close`; `label_merged_on_release_branch.py` `label list`, `label create`, `issue edit`; `release_completeness_check.py` `list` twice; `roll_flow_measurement_issue.py` `create`, `list`, `close`, `list`; `tracker_labels.py` `label create`. The only argvs with `issue` and no leading `gh` are `["issue"]` at `release_seal.py:180` and `publish_release_note.py:638`, each a `plural` call. No `gh issue` or `gh label` argv has a flag third |
| `gh issue -R example/repo close --help` | exit 0 |
| `gh issue view 1493 --json state,body,comments` | open, no comments. The body holds "The constant-valued escape stays open" and does not hold "move here" |
