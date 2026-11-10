# Review round 5: 1794271938-follow-up-holds-seven-owner-questions

```seal
target: 0611f4199, fixes 3225a80f8..0611f4199
```

This is the verifying round over round 4's fix pass. The code reviewed is the diff `3225a80f8..0611f4199`: `7cbfbee33`, `4a10caa05`, `64d7c6d3f`, the close commit `303fc40dc` and `0611f4199`. Its one code change is text in `tests/github/test_close_issues_on_release.py`: `argv_words`' docstring (`:84-125`) and the docstring of `Test_module::test_argv_words_reads_an_f_string_and_a_bytes_word_as_it_reads_a_string` (`:1273-1279`). The reader and every case are unchanged. The work item's present-state records were each read whole at `0611f4199`: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`. No `pr.<lang>.md` stands, and `Commit and pull request language` is English. The three phase records were read for their coordinates. `seal/parity.json` is not declared.

Carried from rounds 1 to 4 and not re-established: the confirmations of *Scope* items 2 to 6, which the fix diff does not touch; round 3's tuple mutation and round 4's `JoinedStr`, `bytes` and `str` mutations, since the reader's code did not change. Re-opened at round 4's coordinates rather than searched again: the two converted cases (`tests/github/test_release_completeness_check.py:577`, `tests/github/test_label_merged_on_release_branch.py:400-414`) and #1493's body. Round 4's `evidence: executed` lines were run again: the three modules, and its two `env` plants (`## Probes`). Its `test_tmp_round4.py` probe set the fold beside the reader, a comparison no sentence at the target makes, so it was not written again.

The spawn sets the scope: whether each statement of what the reader reads and what escapes is true of the code at HEAD, and whether a sentence still compares the reader with the fold outside a dated, measured history line. It also says that an argv shape that escapes is no finding unless a sentence says that shape is caught. This round does not argue for closing any escape. Finding 1 is about a sentence that counts the escapes as two and about a claim the label case does not make. Finding 2 is about the source a judgment row cites.

Every sentence that names the fold in the changed test files and the work item's records was read (executed, `git grep -n -i fold`, each hit read). None outside a history line says the reader matches the fold. `argv_words`' docstring at `:93` and `:95-97`, and the two new cases' docstrings at `:1260` and `:1275`, compare the fold with an earlier reader, each "measured in round N of #1493". The gate and label docstrings (`tests/github/test_release_completeness_check.py:573-576`, `tests/github/test_label_merged_on_release_branch.py:391-394`) and `changelog.md:4` say what the fold did not close, a comment between two words, and that the parse closes it. That holds of `:127-145`. `frame/plan.md:72`, the round-3 judgment row, says "what escapes is a word not written as a literal". Its subject is the spellings of an argv's first word, and it points to the next row for the rest, so it is no finding.

## Findings

### 1. The docstring and the release note count the argvs that escape the cases as two kinds and say every case judges by an argv's first three words, and a third kind escapes while the `--add-label` claim reads every word

```seal
severity: should
location: `tests/github/test_close_issues_on_release.py:113-125`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/changelog.md:4`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/pr.md:4`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/pr.md:5`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/design.md:31`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/design.md:42`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/plan.md:50`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/plan.md:73`
evidence: executed `bin/test` of `test_the_gate_writes_nothing` and `test_the_script_only_ever_creates_a_label_and_adds_one` with two plants, and `gh issue -R example/repo close --help`, in a clone at `0611f4199` (`## Probes`); read `tests/github/test_label_merged_on_release_branch.py:400-405`, `tests/github/test_release_completeness_check.py:577-580`, `tests/github/test_close_issues_on_release.py:113-125`
regression: round-4#1
```

The unit is the last paragraph of `argv_words`' docstring (`tests/github/test_close_issues_on_release.py:113-125`) and the last two sentences of `changelog.md`'s *Changed* second item, both rewritten by `64d7c6d3f`, with `frame/design.md:31` and `:42` rewritten by `7cbfbee33` and `frame/plan.md:50` by `0611f4199`. *Scope* item 1 says each converted case keeps every claim it made, the forbidden verbs and, in the label case, the `gh label create` argv and an argv carrying `--add-label`, and phase 1's plan row (`frame/plan.md:44`) checks both kinds of claim. The fix listed the escapes as the two shapes measured before it, in round 3 of #450 and round 4 of #1493, and said every case judges by the first three words. The code's rule is wider on one side and narrower on the other. The defect came from listing the escapes from measured shapes rather than from the rule the cases apply, which round 4's own judgment row (`frame/plan.md:73`) calls the statement "checked against the code alone".

Claimed: the docstring says "a case judges an argv by its first three kept words. Two kinds of argv escape the cases." It closes with "Either way a forbidden argv is not seen, and a required one reads as missing" (`:114-120`). The changelog says "each case judges an argv by its first three words. Two kinds of argv escape the cases" (`changelog.md:4`), and `pr.md:4` and `pr.md:5` quote both sentences. `frame/design.md:31` says the docstring and the changelog say "which argvs escape it", and names the two. `frame/design.md:42` calls the two "the escapes of the `ast` reader". `frame/plan.md:50` says an argv with a word before `gh` "is judged by none of them".

Found, first: the verb claims select argvs by `words[:3]` (`tests/github/test_release_completeness_check.py:577`, `tests/github/test_label_merged_on_release_branch.py:401`). Any argv whose first three kept words are not `gh` and the two after it is judged by none of them. The two named kinds are two examples of that rule, not all of it. A literal flag between the noun and the verb is a third: `closer.run("gh", "issue", "--repo", repo, "close", "1")` gives `["gh", "issue", "--repo"]` as its first three words. `gh` takes that order: `gh issue -R example/repo close --help` exits 0 and prints the help of `close` (executed). Planted in `release_completeness_check.py`, it left `test_the_gate_writes_nothing` green (executed). Every word in it is a literal and no word stands before `gh`, so neither named kind covers it. The shape is not the finding, since the escapes are the run's decision. The finding is the count "Two kinds", which tells a reader that the cases see every other argv.

Found, second: the label case's `--add-label` claim does not read the first three words. It is `any("--add-label" in words for words in argvs)` (`tests/github/test_label_merged_on_release_branch.py:403`), every word of every argv. With `"env",` planted before `"gh"` in the label script's `gh issue edit ... --add-label` argv, the label case passed (executed). So "each case judges an argv by its first three words" is untrue of that claim. "a required one reads as missing" is untrue of it too. `frame/plan.md:50`'s "judged by none of them" is likewise untrue. Round 3's finding 1 listed this already: "The first-three-words escape reaches every presence claim except `--add-label`."

Neither falsity changes a verdict at the target. No release script writes a `gh issue` or `gh label` argv whose first three kept words are not `gh` and the two after it, and no argv in the three scripts carries `issue` or `label` without a leading `gh` (executed, `## Probes`).

Why it matters: the release note tells a person that two kinds of argv escape, so a person adding `gh issue --repo R close` to the gate script reads the note and trusts the case that says the gate writes nothing. The docstring is what the next agent reads before changing a case, and it says the `--add-label` claim fails on a shape it passes. A count of an open class is falsified by the next shape found, which is what the newest judgment row says of a parity claim.

The fix states the rule and gives the shapes as examples. `tests/github/test_close_issues_on_release.py:113-125`, the docstring's last paragraph:

```python
    So this reader reads string, placeholder-free f-string and bytes words in
    a list, a tuple or a call's positional arguments. A verb claim judges an
    argv by its first three kept words, so it judges no argv whose first
    three kept words are not `gh` and the two after it. Examples are an argv
    where one of those words is not written as a literal, a module-level
    name among them, as above; one where a literal word such as `env` stands
    before `gh`, measured in round 4 of #1493; and one where a flag such as
    `--repo` stands between `issue` and the verb, which `gh` accepts,
    measured in round 5 of #1493. A forbidden argv of that kind is not seen,
    and a required one reads as missing. The label case's `--add-label`
    claim is no verb claim: it reads every word of every argv. Closing the
    escape for a module-level name means resolving names before comparing,
    which is a different checker with its own false-positive argument to
    make. #1493 left these argvs unjudged, since no release script writes a
    `gh issue` or `gh label` argv whose first three kept words are not `gh`
    and the two after it.
```

`changelog.md:4`, the two sentences from "It reads string" to "before `gh`.":

```markdown
It reads string, placeholder-free f-string and bytes words in an argv written as a list, as a tuple or as call arguments, and each verb a case forbids or requires is looked for in an argv's first three words. So an argv whose first three words are not `gh` and the two after it is judged by none of those claims: for example one with a module-level name among them, a word such as `env` before `gh`, or a flag such as `--repo` before the verb.
```

`pr.md:4` and `pr.md:5` then quote those two sentences, each with its coordinate unchanged.

`frame/design.md:31`, from "and the converted cases judge" to "(folded after round 4).":

```markdown
and the converted cases judge each verb by an argv's first three words. Neither the docstring nor the changelog compares the reader with the fold: they say what it reads, and that an argv whose first three kept words are not `gh` and the two after it escapes every verb claim, with examples such as a word not written as a literal (a module-level name among them), a word such as `env` before `gh`, or a flag such as `--repo` before the verb (folded after rounds 4 and 5).
```

`frame/design.md:42`, the first sentence:

```markdown
- Closing what escapes the verb claims: an argv whose first three kept words are not `gh` and the two after it, such as one with a word not written as a literal among them (a module-level name among them, the constant-valued escape #1493 row 7 keeps open), a literal word such as `env` before `gh`, or a flag such as `--repo` before the verb.
```

`frame/plan.md:50`, from "After:" to the end of the item:

```markdown
After: the same cases, reading through `argv_words`, assert the same verbs over argvs whose first three kept words are `gh` and the two after it, and the label case's `--add-label` over every word of every argv. A comment inside an argv no longer escapes them, and an argv whose first three kept words are not `gh` and the two after it, such as one with `env` before `gh`, is judged by none of the verb claims (folded after rounds 4 and 5).
```

These snippets reach every sentence this round found that counts the escapes or says every claim reads the first three words. The new judgment row's first clause, "the cases judge an argv by its first three words" (`frame/plan.md:73`), states the decision in the same words. It holds once "an argv" reads "each verb". Its grounds are finding 2. The fix pass owes that clause too.

### 2. The newest judgment row cites #1493 row 7 for keeping every escape open, and row 7 keeps one

```seal
severity: should
location: `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/plan.md:73`
evidence: executed `gh issue view 1493 --json state,body,comments`; read `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/design.md:42`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/plan.md:73`
regression: round-4#1
```

The unit is the grounds cell of the newest row of `frame/plan.md` *Judgments of the run* (`:73`), added by `7cbfbee33`. *Scope* item 1's *Out* (`frame/design.md:42`) says "The issue keeps the first open", the module-level name, and the fix's row says #1493 row 7 keeps "the reader's escapes" open. The defect came from citing the issue for a decision the row itself makes.

Claimed: the grounds end "#1493 row 7 keeps the reader's escapes open", and the row's *Judged against* cell names "#1493 row 7". The spawn says the same: "#1493 row 7 keeps them open".

Found: row 7 of #1493's body ends "The constant-valued escape stays open" and names no other (executed, `gh issue view 1493`: open, no comments). The argv with a word before `gh` was found in round 4, after the issue was written. Leaving it open is this row's decision. `frame/design.md:42` says only the first is the issue's. So `frame/plan.md:73` and `frame/design.md:42` disagree on what the issue decided.

Why it matters: `skills/core/SKILL.md` *The first value* asks that a judgment be written with its grounds and the document it was judged against. The settle reads the row against that source. It finds row 7 silent on the `env` argv, and cannot tell whether the run decided it or misread the issue.

`frame/plan.md:73`, the last clause of the grounds cell, from "and #1493 row 7":

```markdown
and #1493 row 7 keeps the constant-valued escape open; this row leaves the other argvs the verb claims do not judge open with it
```

## Confirmations

```seal
confirms: round-4#1
```
What holds: no sentence at `0611f4199` says the converted cases judge every argv the fold read, or that the module-level name is the one escape left. The two sentences round 4 named, "so it reads every argv a fold of the source read" and "as it escaped the fold", left `argv_words`' docstring. The changelog's "so it reads every argv the fold read" left `changelog.md:4`, and `pr.md:4` and `pr.md:5` quote the new sentences (executed, `git grep -n -i fold` over the three test modules and the work item's present-state records, each hit read). The two kinds the docstring names do escape: round 4's plants, run again, left the gate case green and turned the label case red with "the script stopped creating" (executed). Finding 1 above is a new defect in the text this fix wrote, not the claim round 4 found false.

What matched: `argv_words` keeps a `str` constant, a `bytes` constant decoded as Latin-1 and an `ast.JoinedStr` whose parts are all constants, from every `ast.List`, `ast.Tuple` and `ast.Call` (`tests/github/test_close_issues_on_release.py:127-145`). The docstring's account of kept and dropped words at `:102-110` matches it (read).

What matched: the new case's docstring says no release script writes a placeholder-free f-string or a bytes word in a `gh` argv (`:1273-1274`). An `ast` scan of every script in `.github/scripts/` found one bytes literal, at `release_report.py:119`, in no `gh` argv, and no placeholder-free f-string in a `gh` argv (executed).

What matched: each of the eleven quotes in `pr.md` stands word for word, with whitespace runs collapsed, in the source its coordinate names, and quotes 4 and 5 stand in `changelog.md`'s *Changed* second item (executed, a `python3 -I` read of `pr.md`, `changelog.md` and `frame/plan.md`).

What matched: `gaps.md:6` names fix pass 4 and its close block, which `303fc40dc` appended to `trail/rounds/round-4.md` (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite and the repository-wide lint. They are `unverified` in this round, and `gaps.md:6` names the orchestrator's run and `trail/gate.md` as its record. Nothing is open beyond the two findings above | `seal/config.json` `Broad gate` | the orchestrator |
| `changelog.md:9` says the measurements "are in #1493's body". At this round the body holds none (executed, `gh issue view 1493`), and the spawn says the text is appended when the pull request opens. The sentence is true from that moment | `seal/threads/1794271938-follow-up-holds-seven-owner-questions/changelog.md:9`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/design.md:84` | the orchestrator, who appends the text, and the sealer, who reads the body |
| The two `tests/test_conftest.py::Test_census_case` failures. The spawn says they fail on the base too and are filed as #1498. This round did not run them | `tests/test_conftest.py`, `tests/censuses.py` | the orchestrator, through #1498 |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_close_issues_on_release.py tests/github/test_release_completeness_check.py tests/github/test_label_merged_on_release_branch.py -q -p no:cacheprovider`, in a `git clone --no-local` at `0611f4199` under the round's scratch directory | exit 0, 114 passed |
| `closer.run("gh", "issue", "--repo", repo, "close", "1")` planted in `release_completeness_check.py`, and `"env",` before `"gh"` in the label script's `gh issue edit ... --add-label` argv, through the `Edit` tool. Then `bin/test` of the two converted cases. Restored with `git checkout` | exit 0, 2 passed. The gate case missed the close, and the label case's `--add-label` claim saw the flag |
| Round 4's plants: `closer.run("env", "GH_PROMPT_DISABLED=1", "gh", "issue", "close", "1")` in `release_completeness_check.py`, and `"env", "GH_PROMPT_DISABLED=1",` before `"gh"` in the label script's `gh label create`, through the `Edit` tool. Then the two converted cases. Restored with `git checkout` | exit 1, 1 failed, 1 passed. The gate case passed. The label case failed at `tests/github/test_label_merged_on_release_branch.py:402` with "the script stopped creating" |
| `gh issue -R example/repo close --help` | exit 0. It printed the help of `close`, so `gh` resolves the verb after a `--repo` flag |
| `python3 -I -B -c`, loading `argv_words` from the module's source and reading every script in `.github/scripts/`: argvs with `gh` not first, argvs of the three scripts carrying `issue` or `label` without a leading `gh`, `gh issue` or `gh label` argvs with a flag before the verb, and every bytes or placeholder-free f-string word | none of the first three kinds. One bytes literal, `release_report.py:119`, in no `gh` argv. No placeholder-free f-string in a `gh` argv. The only string holding `gh issue` is an f-string message at `close_issues_on_release.py:382`, which is no argv |
| `gh issue view 1493 --json state,body,comments` | open, no comments. Row 7 ends "The constant-valued escape stays open". The body holds no measurements yet |
