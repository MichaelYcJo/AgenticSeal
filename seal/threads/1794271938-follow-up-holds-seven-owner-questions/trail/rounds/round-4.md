# Review round 4: 1794271938-follow-up-holds-seven-owner-questions

```seal
target: 80872dc9f, fixes dbc1c8ef8..80872dc9f
```

This is the verifying round over round 3's fix pass. The code reviewed is the diff `dbc1c8ef8..80872dc9f`: `515717071`, `b33cc9c2d`, `f524f9d79`, the close commit `f28932902` and `80872dc9f`. Its one code change is in `tests/github/test_close_issues_on_release.py`: `argv_words` and its docstring (`:84-140`) and the new case `Test_module::test_argv_words_reads_an_f_string_and_a_bytes_word_as_it_reads_a_string` (`:1265-1279`). The work item's present-state records were each read whole at `80872dc9f`: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`. No `pr.<lang>.md` stands, and `Commit and pull request language` is English. The three phase records were read for their coordinates. `seal/parity.json` is not declared.

Carried from rounds 1 to 3 and not re-established: the confirmations of *Scope* items 2 to 6, which the fix diff does not touch, and round 3's tuple mutation, which turned only the tuple case red. Re-opened at earlier rounds' coordinates rather than searched again: the fold at `8657297d5:tests/github/test_label_merged_on_release_branch.py:397-408` and `8657297d5:tests/github/test_release_completeness_check.py:571-574`, and #1493's body. Round 3's `evidence: executed` lines were run again: the three modules, round 3's probe sources, and `gh issue view 1493` (`## Probes`).

The round does not reopen the decision to read f-string and bytes words. It reads that decision on its own terms. Its judgment row says the reader then "reads every argv the fold read" and that "the one escape left is the module-level name". The finding below is about whether that holds.

The spawn's two notes were weighed. First, the pair that `bin/seal layout --pairs` names (executed, `:3` of its output) is two cases that cover different branches. Removing the `ast.JoinedStr` branch, the `bytes` branch or the `str` filter turned only the new case red. Round 3 found that removing `ast.Tuple` turned only the tuple case red. So each case covers something its group does not, and the pair is no finding. The listing exits 0 and gates nothing. Second, a set literal is no argv: `subprocess` turns a set into a list in hash order, so its words have no order to judge. The fold matched `{"gh", "issue", "close"}` and `argv_words` does not read it (executed, the probe). The changelog's claim is about argvs, so the set does not make it false.

One gap of a case comment, outside `## Findings`: the new case's docstring (`tests/github/test_close_issues_on_release.py:1268`) opens "No release script writes an f-string or a bytes argv word". Five `gh` argv words in the scripts are f-strings with a placeholder, such as `release_completeness_check.py:178` (executed, an `ast` scan). None is placeholder-free, so the sentence holds once it says "a placeholder-free f-string".

## Findings

### 1. The text says the converted cases now judge every argv the fold read, with a module-level name the one escape left, and an argv that puts a word before `gh` passes a forbidden verb the base refused

```seal
severity: should
location: `tests/github/test_close_issues_on_release.py:101-104`, `tests/github/test_close_issues_on_release.py:110-112`, `tests/github/test_release_completeness_check.py:577`, `tests/github/test_label_merged_on_release_branch.py:401`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/changelog.md:4`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/pr.md:4`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/design.md:31`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/design.md:72`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/plan.md:50`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/plan.md:72`
evidence: executed `bin/test tests/github/test_tmp_round4.py -p no:xdist -q -s -p no:cacheprovider` and `bin/test` of the two converted cases with a wrapper-word argv planted in each script, both in a clone at `80872dc9f` (`## Probes`); read `8657297d5:tests/github/test_label_merged_on_release_branch.py:397-408`, `8657297d5:tests/github/test_release_completeness_check.py:571-574`, `tests/github/test_close_issues_on_release.py:96-119`
regression: round-3#1
```

The unit is the last paragraph of `argv_words`' docstring (`tests/github/test_close_issues_on_release.py:110-119`) and the changelog's *Changed* second item, both rewritten by `b33cc9c2d`, and the judgment row at `frame/plan.md:72`, written by `515717071`. Phase 1's plan row (`frame/plan.md:44`) verifies the converted cases with forbidden-argv plants, and *Scope* item 1 says each keeps every claim it made. The fix made the reader read every word spelling the fold matched and then wrote that the cases judge every argv the fold read. The cases still judge only an argv's first three kept words, where the fold matched the three words wherever they stood. The defect came from listing the class over how the first word is spelt, as round 2's finding 1 did ("the lost catch is a first word with an `f` or `b` prefix, and nothing else"), and not over where the three words sit.

Claimed: the docstring says the reader "reads every argv a fold of the source read" (`:111-112`). The changelog says "so it reads every argv the fold read" and that a module-level name escapes both (`changelog.md:4`), and `pr.md:4` and `pr.md:5` quote it. The judgment row's grounds say "the one escape left is the module-level name the issue keeps open" (`frame/plan.md:72`). `frame/plan.md:50` says the converted cases "hold the same claims".

Found: the fold searched the folded source for `"gh", "issue", "<verb>"` anywhere in its text (`8657297d5:tests/github/test_release_completeness_check.py:571-574`). The converted cases compare `words[:3]` (`tests/github/test_release_completeness_check.py:577`, `tests/github/test_label_merged_on_release_branch.py:401`). So an argv that puts a literal word before `gh` is read by `argv_words` and judged by no case. Examples are a wrapper such as `env` or `timeout`, or a helper whose first argument is a label. The plant `closer.run("env", "GH_PROMPT_DISABLED=1", "gh", "issue", "close", "1")` in `release_completeness_check.py` left `test_the_gate_writes_nothing` green, and the base's fold search refuses that text. `"env", "GH_PROMPT_DISABLED=1",` put before `"gh"` in the label script's `gh label create` turned the label case red with "the script stopped creating" while the script still creates, and the base's fold found the create. Both reads are executed (`## Probes`). The judgment row's own aim was that "a required argv written that way cannot go red where the base stayed green". That aim fails for this shape, and a forbidden argv of this shape escapes too. No release script writes such an argv today: every `gh` triple in the three scripts is at the start of its argv (executed, `## Probes`). So no case changes its verdict at the target.

The class is every place in Python's grammar where the fold's three quoted words can stand next to each other, listed by taking the grammar apart. They can stand as elements of a list, a tuple or a set, as a call's positional arguments, or inside a string or a comment. A string or a comment is no argv, and a set is no argv (above). In a list, a tuple or a call, the triple can be the first kept words or come after one. The reader reads all three containers. The prefix judges only the first case, so a triple after a kept word is the one lost catch.

Why it matters: the release note tells a reader that the converted cases lost nothing the fold caught except what both miss. The judgment row tells the settle that the one escape left is the one the issue keeps open. A gate script that gains `env ... gh issue close` passes the case whose docstring says the gate writes nothing.

The judgment row chose to read rather than to state escapes, so the fix below follows it. The two converted cases judge every three consecutive kept words, as the fold matched them wherever they stood. With this change, both plants above turn the gate case red and leave the label case green, and the three modules pass unplanted, 114 passed (executed, `## Probes`). The closer's case keeps `words[:3]`. It compared a prefix at the base too, so it lost nothing.

`tests/github/test_release_completeness_check.py:577`, and the same names in the two asserts below it:

```python
        triples = [
            words[i : i + 3]
            for words in argv_words(read(SCRIPT))
            for i in range(len(words))
        ]
        for forbidden in ("edit", "close", "create", "delete", "comment", "reopen"):
            assert ["gh", "issue", forbidden] not in triples, f"issue {forbidden}"
            assert ["gh", "label", forbidden] not in triples, f"label {forbidden}"
```

`tests/github/test_label_merged_on_release_branch.py:401`, with `prefixes` renamed to `triples` at `:402`, `:407` and `:411`:

```python
        triples = [words[i : i + 3] for words in argvs for i in range(len(words))]
```

`argv_words`' docstring, `tests/github/test_close_issues_on_release.py:101-104`, from "A case compares" to "never matched.":

```python
    bytes literal, decoded; anything else is dropped. A case compares three
    kept words against `["gh", "issue", verb]`. The closer's case compares
    the first three. The two cases that replaced a fold compare every three
    in a row, as the fold matched them wherever they stood, so an argv that
    puts a word such as `env` before `gh` is judged too. A name in place of
    one of those three words is dropped, and the verb is never matched.
```

`:110-112`, the first sentence of the last paragraph:

```python
    So this reader reads string, placeholder-free f-string and bytes words in
    a list, a tuple or a call's positional arguments, and the two cases that
    replaced the fold judge every argv a fold of the source read.
```

Each case's red is shown with the planted wrapper word, as above (contract rule 15). This snippet does not reach four frame sentences, and the orchestrator owes them. `frame/design.md:72` says "A case selects the argvs it judges by their first three words", which then holds for the closer's case alone. `frame/design.md:31` and `frame/plan.md:50` hold once the code changes. The judgment row at `frame/plan.md:72` says "the one escape left is the module-level name". A word written as any other expression that is not a literal is dropped by the reader and missed by the fold as well, such as `shutil.which("gh")` or `self.gh` (executed, the probe), so the row should say "a word not written as a literal, such as the module-level name the issue keeps open". `changelog.md:4` and `pr.md:4` hold once the code changes. A fix pass that states the shape as an escape instead of judging it owes every sentence in `location:`.

## Confirmations

```seal
confirms: round-3#1
```
What holds: `argv_words` keeps a `str` constant, a `bytes` constant decoded as Latin-1, and an `ast.JoinedStr` whose parts are all constants, joined (`tests/github/test_close_issues_on_release.py:122-133`, read). Round 3's probe sources were read again: `run(f"gh", "label", "create", name)` and `run(b"gh", "label", "create", name)` now give the prefix `["gh", "label", "create"]`, as the fold matched them. `GH = "gh"` as the first word is still missed by both (executed). So the false red round 3 found for an f-string or bytes first word is gone. The new case's seen-red claims were reproduced through the `Edit` tool, each restored with `git checkout`. Removing the `JoinedStr` branch failed the case at its assert on the f-string source. Removing the `bytes` branch failed it on the bytes source. Removing the `str` filter failed it on the bytes source with `[b'gh', 'label', 'create']`, 1 failed and 113 passed over the three modules (executed). So the `gaps.md` *Not done* paragraph on the unpinned `str` filter rightly left in `f524f9d79`. It was a *Not done* paragraph, not a `## Not verified` row, so it owes no `closed` marking. Finding 1 above is a new defect in the text this fix wrote. It is not the claim round 3 found false.

```seal
confirms: round-3#2
```
What holds: `frame/design.md:42` now names one escape, a module-level name in one of an argv's first three positions, under the grounds written for it. #1493's row 7 says "The constant-valued escape stays open" and names nothing else (executed, `gh issue view 1493`: open, no comments). `frame/plan.md:72` records the judgment to read f-string and bytes words, with its grounds and the documents it was judged against (read). Its grounds' last clause is part of finding 1.

What matched: each of the eleven quotes in `pr.md` stands word for word, with whitespace runs collapsed, in the source its coordinate names (executed, a `python3 -I` read of `pr.md`, `changelog.md` and `frame/plan.md`).

What matched: `frame/design.md:68-69` gives the docstring's first lines as `:85-86` hold them. `frame/design.md:114` and the first judgment row (`frame/plan.md:71`) say the work adds one assertion and two cases, and the branch adds the `offered` assertion, the tuple case and the f-string and bytes case (read).

What matched: `gaps.md:6` names fix passes 1, 2 and 3 and their close blocks, and each round record holds them (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite and the repository-wide lint. They are `unverified` in this round, and `gaps.md:6` names the orchestrator's run and `trail/gate.md` as its record | `seal/config.json` `Broad gate` | the orchestrator |
| `changelog.md:9` says the measurements "are in #1493's body". At this round the body holds none (executed, `gh issue view 1493`), and the spawn says the text is appended when the pull request opens. The sentence is true from that moment | `seal/threads/1794271938-follow-up-holds-seven-owner-questions/changelog.md:9`, `seal/threads/1794271938-follow-up-holds-seven-owner-questions/frame/design.md:84` | the orchestrator, who appends the text, and the sealer, who reads the body |
| The two `tests/test_conftest.py::Test_census_case` failures. The spawn says they fail on the base too and are filed as #1498. This round did not run them | `tests/test_conftest.py`, `tests/censuses.py` | the orchestrator, through #1498 |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_close_issues_on_release.py tests/github/test_release_completeness_check.py tests/github/test_label_merged_on_release_branch.py -q -p no:cacheprovider`, in a `git clone --no-local` at `80872dc9f` under the round's scratch directory | exit 0, 114 passed |
| `bin/test tests/github/test_tmp_round4.py -p no:xdist -q -s -p no:cacheprovider` in the same clone, deleted after its one run. For each source it printed whether the fold, `argv_words` with a `words[:3]` prefix, and `argv_words` with every three consecutive words matched the triple | 1 passed. Plain, `f"gh"` and `b"gh"` first word: True, True, True. `GH = "gh"` first word: False, False, False. `run("env", "gh", "label", "create", name)`: True, False, True. `subprocess.run(["env", "GH_PROMPT_DISABLED=1", "gh", "issue", "close", n])`: True, False, True. `attempt("closing", "gh", "issue", "close", n)`: True, False, True. `attempt(n, "gh", "issue", "close", n)`: True, True, True. `shutil.which("gh")` and `self.gh` first word: False, False, False. Set literal: True, False, False. `f"{verb}"` verb: False, False, False |
| Removing the `JoinedStr` branch, then the `bytes` branch, of `argv_words` through the `Edit` tool, and running the new case after each, restored with `git checkout` after each | exit 1 each time. The first failed on `run(f"gh", ...)`, the second on `run(b"gh", ...)`, both at the case's assert, `:1279` at the target |
| Removing the `str` filter of `argv_words`' first branch through the `Edit` tool, then the three modules, restored with `git checkout` | exit 1, 1 failed, 113 passed. The failure is the new case, on `[b'gh', 'label', 'create']` |
| The plant `closer.run("env", "GH_PROMPT_DISABLED=1", "gh", "issue", "close", "1")` in `release_completeness_check.py`, and `"env", "GH_PROMPT_DISABLED=1",` before `"gh"` in the label script's `gh label create`, through the `Edit` tool. Then the two converted cases | exit 1, 1 failed, 1 passed. The gate case passed. The label case failed with "the script stopped creating". The base's fold strings searched in the same planted files: `"gh", "issue", "close"` found, `"gh", "label", "create",` found |
| The same plants with both converted cases changed to every three consecutive words through the `Edit` tool. Then the plants were removed and the three modules run. Everything was restored with `git checkout` afterwards | planted: exit 1, 1 failed, 1 passed. The gate case failed on `issue close`, and the label case passed. Unplanted: exit 0, 114 passed |
| `python3 -I -B -c` over the three scripts in `.github/scripts/`: every `gh` triple by prefix and by every three consecutive words of `argv_words`' output, and every f-string or bytes argv word | the prefix and window sets are equal in each script. Five f-string words with a placeholder stand in `gh` argvs, none placeholder-free, and there are no bytes words |
| `bin/seal layout --pairs` in the clone | exit 0, 132 lines. Line 3 names the tuple case and the new case as equal bodies once normalised |
| `gh issue view 1493 --json state,body,comments` | open, no comments. Row 7 says "The constant-valued escape stays open". The body holds no measurements yet |
